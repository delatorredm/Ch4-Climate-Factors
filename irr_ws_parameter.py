# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# irr_ws_parameter.py
# Created on: 2021-11-05 23:45:05.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: irr_ws_parameter <Climate_Variable> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")

# Script arguments
Climate_Variable = arcpy.GetParameterAsText(0)

# Local variables:
main_irr_ws_intersect_admbnda = "main.irr_ws_intersect_admbnda"
Zone_field = "ADM3_EN"
Ignore_NoData_in_calculations = "true"
Output_table = "\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1"
irr_ws__Value__csv = Output_table
ArcGIS = "H:\\ArcGIS"
Value = "FILE"

# Process: Zonal Statistics as Table
arcpy.gp.ZonalStatisticsAsTable_sa(main_irr_ws_intersect_admbnda, Zone_field, Climate_Variable, Output_table, Ignore_NoData_in_calculations, "ALL")

# Process: Table to Table
arcpy.TableToTable_conversion(Output_table, ArcGIS, "irr_ws_%Value%.csv", "", "ADM3_EN \"ADM3_EN\" true true false 0 Text 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,ADM3_EN,-1,-1;MIN \"MIN\" true true false 0 Double 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,MIN,-1,-1;MAX \"MAX\" true true false 0 Double 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,MAX,-1,-1;RANGE \"RANGE\" true true false 0 Double 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,RANGE,-1,-1;MEAN \"MEAN\" true true false 0 Double 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,MEAN,-1,-1;STD \"STD\" true true false 0 Double 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,STD,-1,-1;SUM \"SUM\" true true false 0 Double 0 0 ,First,#,\\\\unifiles.uoa.auckland.ac.nz\\myhome\\Documents\\ArcGIS\\Default.gdb\\ZonalSt_rf_ws_i1,SUM,-1,-1", "")

# Process: Parse Path
arcpy.ParsePath_mb(Climate_Variable, "FILE")

