# Robust OrCAD Tcl script using DboSession interface
# This interface is standard across OrCAD Capture versions

proc export_schematic_to_data {outputFile} {
    if { [info exists ::DboSession_s_pDboSession] == 0 } {
        puts "Error: DboSession global variable not found."
        return
    }
    set lSession $::DboSession_s_pDboSession
    DboSession -this $lSession
    set lDesign [$lSession GetActiveDesign]
    if {$lDesign == "NULL" || $lDesign == "" || $lDesign == 0} {
        puts "Error: No active design found."
        return
    }

    set fh [open $outputFile w]
    puts -nonewline $fh "\xEF\xBB\xBF"
    puts $fh "Type,Reference,Value,PartNumber,NetName,Nodes"

    # Initialize Debug State
    set lState [DboState]

    # Get Root Schematic
    set lRootSchematic [$lDesign GetRootSchematic $lState]
    if {$lRootSchematic == "NULL"} {
        puts "Error: Could not get root schematic."
        close $fh
        return
    }

    # Iterate Pages in Root Schematic
    set lPageIter [$lRootSchematic NewPagesIter $lState]
    set lPage [$lPageIter NextPage $lState]
    while {$lPage != "NULL" && $lPage != ""} {
        # Export Parts on Page
        set lPartInstIter [$lPage NewPartInstsIter $lState]
        set lPartInst [$lPartInstIter NextPartInst $lState]
        while {$lPartInst != "NULL" && $lPartInst != ""} {
            set lRef [DboTclHelper_sMakeCString]
            # Confirmed method: GetReferenceDesignator
            $lPartInst GetReferenceDesignator $lRef
            set ref [DboTclHelper_sGetConstCharPtr $lRef]
            
            set lVal [DboTclHelper_sMakeCString]
            # Confirmed method: GetPartValue
            $lPartInst GetPartValue $lVal
            set val [DboTclHelper_sGetConstCharPtr $lVal]
            
            set mpn $val
            set lMPN [DboTclHelper_sMakeCString]
            set lPropName [DboTclHelper_sMakeCString "Part Number"]
            # Confirmed method: GetEffectivePropStringValue
            catch { $lPartInst GetEffectivePropStringValue $lPropName $lMPN }
            set mpn [DboTclHelper_sGetConstCharPtr $lMPN]
            if {$mpn == ""} { set mpn $val }

            puts $fh "PART,$ref,$val,$mpn,,"
            set lPartInst [$lPartInstIter NextPartInst $lState]
        }
        delete_DboPagePartInstsIter $lPartInstIter

        # Export Nets on Page
        set lNetIter [$lPage NewNetsIter $lState]
        set lNet [$lNetIter NextNet $lState]
        while {$lNet != "NULL" && $lNet != ""} {
            set lName [DboTclHelper_sMakeCString]
            $lNet GetNetName $lName
            set netName [DboTclHelper_sGetConstCharPtr $lName]
            puts $fh "NET,,,,$netName,"
            set lNet [$lNetIter NextNet $lState]
        }
        delete_DboPageNetsIter $lNetIter

        set lPage [$lPageIter NextPage $lState]
    }
    delete_DboSchematicPagesIter $lPageIter

    close $fh
    puts "Exported schematic data to $outputFile"
}

# Helper to export BOM using the built-in OrCAD command
proc export_bom {outputFile} {
    set lDesign [capGetCurrentDesign]
    if {$lDesign == "NULL" || $lDesign == "" || $lDesign == 0} {
        puts "Error: No active design found."
        return
    }
    set dsnPath [DboTclHelper_sMakeCString]
    $lDesign GetName $dsnPath
    set dsn [DboTclHelper_sGetConstCharPtr $dsnPath]
    
    set header "{Item}\t{Quantity}\t{Reference}\t{Value}\t{Part Number}\t{PCB Footprint}"
    set propString "{Item}\t{Quantity}\t{Reference}\t{Value}\t{Part Number}\t{PCB Footprint}"
    
    # Arguments: dsn, output, header, propString, includeFile, useMapping, separateRows
    if {[catch {capBillOfMaterials $dsn $outputFile $header $propString "" 0 0} err]} {
        puts "Error exporting BOM: $err"
    } else {
        puts "BOM successfully exported to $outputFile"
    }
}

# Usage instructions for the user
puts "--------------------------------------------------------"
puts "Usage in Capture Command Window:"
puts "1. source {C:/Users/lixiaogang/.gemini/antigravity/skills/schematic_analyzer/scripts/export_schematic.tcl}"
puts "2. export_bom \"C:/path/to/your_design.BOM\""
puts "3. export_schematic_to_data \"C:/path/to/netlist_data.csv\" (Legacy)"
puts "--------------------------------------------------------"
