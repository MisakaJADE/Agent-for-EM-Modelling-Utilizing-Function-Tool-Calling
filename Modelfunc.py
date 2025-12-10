import openai
from openai import OpenAI
import os
import json
from datetime import datetime
import numpy as np
import gpt_tool
import gpt_tool_array

openai_api_key = os.getenv("OPENAI_API_KEYS")
tools = gpt_tool.tools
array_tools = gpt_tool_array.tools
#######################################################################################################################
## basic operation of modelling
#######################################################################################################################

def store_parameter(vba, parameter_name, parameter_value):
    vba += f'''
    AddtoHistory "AddParameter.{parameter_name}", "StoreParameter(""{parameter_name}"",""{parameter_value}"")"
    '''
    return vba

def define_material_RogersAD260Clossy(vba):
    vba += f'''
    AddtoHistory "Material.RogersAD260Clossy", _
    "With Material" + vbCrLf + _
    "    .Reset" + vbCrLf + _
    "    .Name ""Rogers AD 260C (lossy)"" " + vbCrLf + _
    "    .Folder """" " + vbCrLf + _
    "    .FrqType ""all"" " + vbCrLf + _
    "    .Type ""Normal"" " + vbCrLf + _
    "    .Epsilon ""2.65""  " + vbCrLf + _
    "    .Mu ""1.0"" " + vbCrLf + _
    "    .Kappa ""0.0"" " + vbCrLf + _
    "    .TanD ""0.0017"" " + vbCrLf + _
    "    .TanDFreq ""10.0"" " + vbCrLf + _
    "    .TanDGiven ""True"" " + vbCrLf + _
    "    .TanDModel ""ConstTanD"" " + vbCrLf + _
    "    .DispModelEps ""None"" " + vbCrLf + _
    "    .DispModelMu ""None"" " + vbCrLf + _
    "    .DispersiveFittingSchemeEps ""General 1st"" " + vbCrLf + _
    "    .DispersiveFittingSchemeMu ""General 1st"" " + vbCrLf + _
    "    .UseGeneralDispersionEps ""False"" " + vbCrLf + _
    "    .UseGeneralDispersionMu ""False"" " + vbCrLf + _
    "    .Rho ""0.0"" " + vbCrLf + _
    "    .ThermalType ""Normal"" " + vbCrLf + _
    "    .SetActiveMaterial ""all"" " + vbCrLf + _
    "    .Colour ""0.94"", ""0.82"", ""0.76"" " + vbCrLf + _
    "    .Wireframe ""False"" " + vbCrLf + _
    "    .Transparency ""0"" " + vbCrLf + _
    "    .Create " + vbCrLf + _
    "End With "
    '''
    return vba

def define_material_FR4lossy(vba):
    vba += f'''
    AddtoHistory "define material: FR-4 (lossy)", _
    "With Material" + vbCrLf + _
    "    .Reset" + vbCrLf + _
    "    .Name ""FR-4 (lossy)"" " + vbCrLf + _
    "    .Folder """" " + vbCrLf + _
    "    .FrqType ""all"" " + vbCrLf + _
    "    .Type ""Normal"" " + vbCrLf + _
    "    .SetMaterialUnit ""GHz"", ""mm""" + vbCrLf + _
    "    .Epsilon ""4.3""  " + vbCrLf + _
    "    .Mu ""1.0"" " + vbCrLf + _
    "    .Kappa ""0.0"" " + vbCrLf + _
    "    .TanD ""0.0025"" " + vbCrLf + _
    "    .TanDFreq ""10.0"" " + vbCrLf + _
    "    .TanDGiven ""True"" " + vbCrLf + _
    "    .TanDModel ""ConstTanD"" " + vbCrLf + _
    "    .KappaM ""0.0"" " + vbCrLf + _
    "    .TanDM ""0.0"" " + vbCrLf + _
    "    .TanDMFreq ""0.0"" " + vbCrLf + _
    "    .TanDMGiven ""False"" " + vbCrLf + _
    "    .TanDMModel ""ConstKappa"" " + vbCrLf + _
    "    .DispModelEps ""None"" " + vbCrLf + _
    "    .DispModelMu ""None"" " + vbCrLf + _
    "    .DispersiveFittingSchemeEps ""General 1st"" " + vbCrLf + _
    "    .DispersiveFittingSchemeMu ""General 1st"" " + vbCrLf + _
    "    .UseGeneralDispersionEps ""False"" " + vbCrLf + _
    "    .UseGeneralDispersionMu ""False"" " + vbCrLf + _
    "    .Rho ""0.0"" " + vbCrLf + _
    "    .ThermalType ""Normal"" " + vbCrLf + _
    "    .ThermalConductivity ""0.3"" " + vbCrLf + _
    "    .SetActiveMaterial ""all"" " + vbCrLf + _
    "    .Colour ""0.94"", ""0.82"", ""0.76"" " + vbCrLf + _
    "    .Wireframe ""False"" " + vbCrLf + _
    "    .Transparency ""0"" " + vbCrLf + _
    "    .Create " + vbCrLf + _
    "End With "
    '''
    return vba

def define_material_PTFElossy(vba):
    vba += f'''
        AddtoHistory "define material: FR-4 (lossy)", _
        "With Material" + vbCrLf + _
        "    .Reset" + vbCrLf + _
        "    .Name ""PTFE (lossy)"" " + vbCrLf + _
        "    .Folder """" " + vbCrLf + _
        "    .FrqType ""all"" " + vbCrLf + _
        "    .Type ""Normal"" " + vbCrLf + _
        "    .SetMaterialUnit ""GHz"", ""mm""" + vbCrLf + _
        "    .Epsilon ""2.1""  " + vbCrLf + _
        "    .Mu ""1.0"" " + vbCrLf + _
        "    .Kappa ""0.0"" " + vbCrLf + _
        "    .TanD ""0.0002"" " + vbCrLf + _
        "    .TanDFreq ""10.0"" " + vbCrLf + _
        "    .TanDGiven ""True"" " + vbCrLf + _
        "    .TanDModel ""ConstTanD"" " + vbCrLf + _
        "    .KappaM ""0.0"" " + vbCrLf + _
        "    .TanDM ""0.0"" " + vbCrLf + _
        "    .TanDMFreq ""0.0"" " + vbCrLf + _
        "    .TanDMGiven ""False"" " + vbCrLf + _
        "    .TanDMModel ""ConstKappa"" " + vbCrLf + _
        "    .DispModelEps ""None"" " + vbCrLf + _
        "    .DispModelMu ""None"" " + vbCrLf + _
        "    .DispersiveFittingSchemeEps ""General 1st"" " + vbCrLf + _
        "    .DispersiveFittingSchemeMu ""General 1st"" " + vbCrLf + _
        "    .UseGeneralDispersionEps ""False"" " + vbCrLf + _
        "    .UseGeneralDispersionMu ""False"" " + vbCrLf + _
        "    .Rho ""2200.0"" " + vbCrLf + _
        "    .ThermalType ""Normal"" " + vbCrLf + _
        "    .ThermalConductivity ""0.2"" " + vbCrLf + _
        "    .SpecificHeat ""1000"", ""J/K/kg"" " + vbCrLf + _
        "    .SetActiveMaterial ""all"" " + vbCrLf + _
        "    .MechanicsType ""Isotropic"" " + vbCrLf + _
        "    .YoungsModulus ""0.5"" " + vbCrLf + _
        "    .PoissonsRatio ""0.4"" " + vbCrLf + _
        "    .ThermalExpansionRate ""140"" " + vbCrLf + _
        "    .Colour ""0.94"", ""0.82"", ""0.76"" " + vbCrLf + _
        "    .Wireframe ""False"" " + vbCrLf + _
        "    .Transparency ""0"" " + vbCrLf + _
        "    .Create " + vbCrLf + _
        "End With "
        '''
    return vba

def change_material(vba,origin_material,model_name,new_material):
    vba += f'''
    AddtoHistory "change material: {origin_material}:{model_name} to: {new_material} ", "Solid.ChangeMaterial ""{origin_material}:{model_name}"", ""{new_material}"" "
    '''
    return vba

def define_component(vba,component_name):
    vba += f'''
    AddtoHistory "Component.New ""{component_name}"" ", "Component.New ""{component_name}"" "
    '''
    return vba

def define_brick(vba, brick_name, component_name, material, x_min, x_max, y_min, y_max, z_min, z_max):
    vba += f'''
    AddtoHistory "Brick.{brick_name}", _
    "With Brick" + vbCrLf + _
    "    .Reset" + vbCrLf + _
    "    .Name ""{brick_name}""" + vbCrLf + _
    "    .Component ""{component_name}""" + vbCrLf + _
    "    .Material ""{material}""" + vbCrLf + _
    "    .Xrange ""{x_min}"", ""{x_max}""" + vbCrLf + _
    "    .Yrange ""{y_min}"", ""{y_max}""" + vbCrLf + _
    "    .Zrange ""{z_min}"", ""{z_max}""" + vbCrLf + _
    "    .Create" + vbCrLf + _
    "End With"
    '''
    return vba

def define_cylinder_z(vba, cylinder_name, component_name, material_name, outer_radius, inner_radius, z_min, z_max,
                          x_center, y_center):
    vba += f'''
    AddtoHistory "Cyinder{cylinder_name}", _
    "With Cylinder "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{cylinder_name}"" " + vbCrLf + _
    "     .Component ""{component_name}"" " + vbCrLf + _
    "     .Material ""{material_name}"" " + vbCrLf + _
    "     .OuterRadius ""{outer_radius}"" " + vbCrLf + _
    "     .InnerRadius ""{inner_radius}"" " + vbCrLf + _
    "     .Axis ""z"" " + vbCrLf + _
    "     .Zrange ""{z_min}"", ""{z_max}"" " + vbCrLf + _
    "     .Xcenter ""{x_center}"" " + vbCrLf + _
    "     .Ycenter ""{y_center}"" " + vbCrLf + _
    "     .Segments ""0"" " + vbCrLf + _
    "     .Create "+ vbCrLf + _
    "End With"
    '''
    return vba

def define_line_xy(vba, line_name, curve_name, start_point_x, end_point_x, start_point_y, end_point_y):
    vba += f'''
    AddtoHistory "Curve.{line_name}", _
    "With Polygon "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{line_name}"" " + vbCrLf + _
    "     .Curve ""{curve_name}"" " + vbCrLf + _
    "     .Point ""{start_point_x}"", ""{start_point_y}"" " + vbCrLf + _
    "     .LineTo ""{end_point_x}"", ""{end_point_y}"" " + vbCrLf + _
    "     .Create "+ vbCrLf + _
    "End With"
    '''
    return vba

#######################################################################################################################
## transform and boolean operation of the model
#######################################################################################################################

def rotate_around_origin(vba, model_name, component_name, angle_x, angle_y, angle_z, multipleobjects, repetition):
    vba += f'''
    AddtoHistory "transform:rotate:{model_name}", _
    "With Transform "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{component_name}:{model_name}"" " + vbCrLf + _
    "     .Origin ""Free"" " + vbCrLf + _
    "     .Center ""0"", ""0"", ""0""  " + vbCrLf + _
    "     .Angle ""{angle_x}"", ""{angle_y}"", ""{angle_z}""  " + vbCrLf + _
    '''
    if multipleobjects == True:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}"" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""{repetition}"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .Destination """"  " + vbCrLf + _
    "     .Material """"   " + vbCrLf + _
    "     .AutoDestination ""True"" " + vbCrLf + _
    "     .Transform ""Shape"", ""Rotate"" " + vbCrLf + _
'''
    elif multipleobjects == False:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}""" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""1"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .Destination """"  " + vbCrLf + _
    "     .Material """"   " + vbCrLf + _
    "     .AutoDestination ""True"" " + vbCrLf + _
    "     .Transform ""Shape"", ""Rotate"" " + vbCrLf + _
'''
    vba += \
        f''' "End With"
    '''
    return vba

def transform_curve(vba, curve_name, vector_x, vector_y, vector_z, multipleobjects, repetition):
    vba += f'''
    AddtoHistory "Transform.{curve_name}", _
    "With Transform "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{curve_name}"" " + vbCrLf + _
    "     .Vector ""{vector_x}"", ""{vector_y}"", ""{vector_z}"" " + vbCrLf + _
    "     .UsePickedPoints ""False"" " + vbCrLf + _
    "     .InvertPickedPoints ""False"" " + vbCrLf + _
    '''
    if multipleobjects == True:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}"" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""{repetition}"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .Transform ""Shape"", ""Translate"" " + vbCrLf + _
'''
    elif multipleobjects == False:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}"" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""1"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .Transform ""Curve"", ""Translate"" " + vbCrLf + _
'''
    vba += f''' "End With"
    '''
    return vba

def boolean_add(vba, component_name_1, model_name_1, component_name_2, model_name_2):
    vba += f'''
    AddtoHistory "Solid.Add", _
    "Solid.Add ""{component_name_1}:{model_name_1}"", ""{component_name_2}:{model_name_2}"" "
'''
    return vba

def rename_model(vba,model_old_name,component_name,model_new_name):
    vba += f'''
        AddtoHistory "Rename model", _
        "Solid.Rename ""{component_name}:{model_old_name}"", ""{model_new_name}"" "
    '''
    return vba

def pick_end_points(vba, curve_name, line_name):
    vba += f'''
    AddtoHistory "pick_end_point_1_{curve_name}_{line_name}", "Pick.PickCurveEndpointFromId ""{curve_name}:{line_name}"", ""1"" "
    AddtoHistory "pick_end_point_2_{curve_name}_{line_name}", "Pick.PickCurveEndpointFromId ""{curve_name}:{line_name}"", ""2"" "
        '''
    return vba

def delete_curve(vba, curve_name):
    vba += f'''
        AddtoHistory "delete auxiliary curve for modelling", "Curve.DeleteCurve ""{curve_name}"" "
        '''
    return vba
#######################################################################################################################
## combination of the basic operations
#######################################################################################################################

def define_lumped_element_RLC_wire(vba, lumped_element_name, folder_name, type, R, L, C, p1_x, p1_y, p1_z, p2_x, p2_y, p2_z):
    # the whole process: define a line, pick the two end points of the line, and define the elements
    vba = define_line_xy(vba,"line_aux", "curve_aux", p1_x, p2_x, p1_y, p2_y)
    vba = transform_curve(vba, "curve_aux",0,0, p1_z, False, 1)
    vba = pick_end_points(vba,"curve_aux","line_aux")

    vba += f'''
    AddtoHistory "DefineLumpedElement.{lumped_element_name}", _
    "With LumpedElement "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .SetName ""{lumped_element_name}"" " + vbCrLf + _
    "     .Folder ""{folder_name}"" " + vbCrLf + _
    "     .SetType ""{type}"" " + vbCrLf + _
    "     .SetR ""{R}"" " + vbCrLf + _
    "     .SetL ""{L}"" " + vbCrLf + _
    "     .SetC ""{C}"" " + vbCrLf + _
    "     .SetGs ""0"" " + vbCrLf + _
    "     .SetI0 ""1e-14"" " + vbCrLf + _
    "     .SetT ""300"" " + vbCrLf + _
    "     .SetMonitor ""True"" " + vbCrLf + _
    "     .SetRadius ""0.0"" " + vbCrLf + _
    "     .CircuitFileName """" " + vbCrLf + _
    "     .CircuitId ""1"" " + vbCrLf + _
    "     .UseCopyOnly ""True"" " + vbCrLf + _
    "     .UseRelativePath ""False"" " + vbCrLf + _
    "     .SetP1 ""True"", ""{p1_x}"", ""{p1_y}"", ""{p1_z}"" " + vbCrLf + _
    "     .SetP2 ""True"", ""{p2_x}"", ""{p2_y}"", ""{p2_z}"" " + vbCrLf + _
    "     .Create "+ vbCrLf + _
    "End With"
    '''
    # delete the auxiliary line for modelling
    vba = delete_curve(vba, "curve_aux")
    return vba

#######################################################################################################################
## array drawing
#######################################################################################################################

# multi-agent: call another agent that is used specifically for array modeling
def array_mode_start(vba, x_size, y_size, period):
    print("\tNow your are in the array modelling mode, enter your request about one model and it will be expanded to an array. \n")
    additional_prompt = f"\tNow is in the array modelling mode. The scale of the array is {x_size} along x and {y_size} along y, the period is {period}."
    vba += f'''
    Dim i As Integer
    Dim j As Integer
    For i = 1 To {x_size}
    For j = 1 To {y_size}
    '''
    client = OpenAI(api_key=openai_api_key)
    continue_input = True
    while continue_input:
        # Entering the requests
        text_request2gpt = input("\tEnter your request here:\n")
        input_messages = [{"role": "user", "content": additional_prompt+text_request2gpt}]
        response = client.responses.create(
            model="gpt-4o-mini-2024-07-18",
            input=input_messages,
            tools=array_tools,
        )

        # Output and conduct the functions
        for tool_call in response.output:
            if tool_call.type != "function_call":
                continue

            name = tool_call.name
            args = json.loads(tool_call.arguments)

            if name == "array_mode_end":
                continue_input = False

            func_called = globals().get(name)
            vba = func_called(vba, **args)
            print(vba)

        while continue_input == True:
            continue_input = input("\tContinue array mode? [y/n] ")
            if continue_input == 'y':
                continue_input = True
                break
            if continue_input == 'n':
                continue_input = False
                vba = array_mode_end(vba)
                break
            else:
                print('\tInvalid input, please input y or n ')
                continue_input = True

    return vba

def array_mode_end(vba):
    vba += f'''
    Next j
    Next i
'''
    return vba



def store_parameter_array(vba, parameter_name, parameter_value):
    vba += f'''
    AddtoHistory "AddParameter.{parameter_name}", _ 
    "StoreParameter(""{parameter_name}"",""{parameter_value}"") "
    '''
    return vba

def define_component_array(vba,component_name):
    vba += f'''
    AddtoHistory "Component.New ""{component_name}_" & i & "_" & j & """ ", "Component.New ""{component_name}_" & i & "_" & j & """"
    '''
    return vba

def define_brick_array(vba, brick_name, component_name, material, x_min, x_max, y_min, y_max, z_min, z_max, x_size, y_size, period):
    vba += f'''
    AddtoHistory "Brick.{brick_name}", _
    "With Brick" + vbCrLf + _
    "    .Reset" + vbCrLf + _
    "    .Name ""{brick_name}_" & i & "_" & j & """ " + vbCrLf + _
    "    .Component ""{component_name}" & "_" & i & "_" & j & """ " + vbCrLf + _
    "    .Material ""{material}""" + vbCrLf + _
    "    .Xrange ""{x_min}+{period}*(-{x_size}/2-0.5+" & i & ")"", " & " ""{x_max}+{period}*(-{x_size}/2-0.5+" & i & ")"" " + vbCrLf + _
    "    .Yrange ""{y_min}+{period}*(-{y_size}/2-0.5+" & j & ")"", " & " ""{y_max}+{period}*(-{y_size}/2-0.5+" & j & ")"" " + vbCrLf + _
    "    .Zrange ""{z_min}"", ""{z_max}""" + vbCrLf + _
    "    .Create" + vbCrLf + _
    "End With"
    '''
    return vba

def define_cylinder_z_array(vba, cylinder_name, component_name, material_name, outer_radius, inner_radius, z_min, z_max,
                          x_center, y_center, x_size, y_size, period):
    vba += f'''
    AddtoHistory "Cyinder{cylinder_name}", _
    "With Cylinder "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{cylinder_name}_" & i & "_" & j & """"+ vbCrLf + _
    "     .Component ""{component_name}_" & i & "_" & j & """"+ vbCrLf + _
    "     .Material ""{material_name}"" " + vbCrLf + _
    "     .OuterRadius ""{outer_radius}"" " + vbCrLf + _
    "     .InnerRadius ""{inner_radius}"" " + vbCrLf + _
    "     .Axis ""z"" " + vbCrLf + _
    "     .Zrange ""{z_min}"", ""{z_max}"" " + vbCrLf + _
    "     .Xcenter ""{x_center}+{period}*(-{x_size}/2-0.5+" & i & ")"" " + vbCrLf + _
    "     .Ycenter ""{y_center}+{period}*(-{y_size}/2-0.5+" & j & ")"" " + vbCrLf + _
    "     .Segments ""0"" " + vbCrLf + _
    "     .Create "+ vbCrLf + _
    "End With"
    '''
    return vba

def rotate_around_origin_array(vba, model_name, component_name, angle_x, angle_y, angle_z,
                                          multipleobjects, repetition, x_size, y_size, period):
    vba += f'''
    AddtoHistory "transform:rotate:{model_name}", _
    "With Transform "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{component_name}_" & i & "_" & j & ":{model_name}_" & i & "_" & j & """ " + vbCrLf + _
    "     .Origin ""Free"" " + vbCrLf + _
    "     .Center ""0+{period}*(-{x_size}/2-0.5+" & i & ")"", ""0+{period}*(-{y_size}/2-0.5+" & j & ")"", ""0""  " + vbCrLf + _
    "     .Angle ""{angle_x}"", ""{angle_y}"", ""{angle_z}""  " + vbCrLf + _
    '''
    if multipleobjects == True:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}"" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""{repetition}"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .AutoDestination ""True"" " + vbCrLf + _
    "     .Transform ""Shape"", ""Rotate"" " + vbCrLf + _
'''
    elif multipleobjects == False:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}""" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""1"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .AutoDestination ""True"" " + vbCrLf + _
    "     .Transform ""Shape"", ""Rotate"" " + vbCrLf + _
'''
    vba += \
        f''' "End With"
    '''
    return vba

def boolean_add_array(vba, component_name_1, model_name_1, component_name_2, model_name_2):
    vba += f'''
    AddtoHistory "Solid.Add", _
    "Solid.Add ""{component_name_1}_" & i & "_" & j & ":{model_name_1}_" & i & "_" & j & """, ""{component_name_2}_" & i & "_" & j & ":{model_name_2}_" & i & "_" & j & """ "
'''
    return vba

def rename_model_array(vba,model_old_name,component_name,model_new_name):
    vba += f'''
        AddtoHistory "Rename model", _
        "Solid.Rename ""{component_name}_" & i & "_" & j & ":{model_old_name}_" & i & "_" & j & """, ""{model_new_name}_" & i & "_" & j & """ "
    '''
    return vba

def define_line_xy_array(vba, line_name, curve_name, start_point_x, end_point_x, start_point_y, end_point_y, x_size, y_size, period):
    vba += f'''
    AddtoHistory "Curve.{line_name}", _
    "With Polygon "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{line_name}"" " + vbCrLf + _
    "     .Curve ""{curve_name}"" " + vbCrLf + _
    "     .Point ""{start_point_x}+{period}*(-{x_size}/2-0.5+" & i & ")" & """, ""{start_point_y}+{period}*(-{y_size}/2-0.5+" & j & ")" & """ " + vbCrLf + _
    "     .LineTo ""{end_point_x}+{period}*(-{x_size}/2-0.5+" & i & ")" & """, ""{end_point_y}+{period}*(-{y_size}/2-0.5+" & j & ")" & """ " + vbCrLf + _
    "     .Create "+ vbCrLf + _
    "End With"
    '''
    return vba

def transform_curve_array(vba, curve_name, vector_x, vector_y, vector_z, multipleobjects, repetition):
    vba += f'''
    AddtoHistory "Transform.{curve_name}", _
    "With Transform "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .Name ""{curve_name}"" " + vbCrLf + _
    "     .Vector ""{vector_x}"", ""{vector_y}"", ""{vector_z}"" " + vbCrLf + _
    "     .UsePickedPoints ""False"" " + vbCrLf + _
    "     .InvertPickedPoints ""False"" " + vbCrLf + _
    '''
    if multipleobjects == True:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}"" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""{repetition}"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .Transform ""Shape"", ""Translate"" " + vbCrLf + _
'''
    elif multipleobjects == False:
        vba += \
f'''"     .MultipleObjects ""{multipleobjects}"" " + vbCrLf + _
    "     .GroupObjects ""False"" " + vbCrLf + _
    "     .Repetitions ""1"" " + vbCrLf + _
    "     .MultipleSelection ""False"" " + vbCrLf + _
    "     .Transform ""Curve"", ""Translate"" " + vbCrLf + _
'''
    vba += f''' "End With"
    '''
    return vba

def pick_end_points_array(vba, curve_name, line_name):
    vba += f'''
    AddtoHistory "pick_end_point_1_{curve_name}_{line_name}", "Pick.PickCurveEndpointFromId ""{curve_name}:{line_name}"", ""1"" "
    AddtoHistory "pick_end_point_2_{curve_name}_{line_name}", "Pick.PickCurveEndpointFromId ""{curve_name}:{line_name}"", ""2"" "
        '''
    return vba

def define_lumped_element_RLC_wire_array(vba, lumped_element_name, folder_name, type, R, L, C, p1_x, p1_y, p1_z, p2_x, p2_y, p2_z, x_size, y_size, period):
    # the whole process: define a line, pick the two end points of the line, and define the elements
    vba = define_line_xy_array(vba,"line_aux", "curve_aux", p1_x, p2_x, p1_y, p2_y, x_size, y_size, period)
    vba = transform_curve_array(vba, "curve_aux",0,0, p1_z, False, 1)
    vba = pick_end_points_array(vba,"curve_aux","line_aux")

    vba += f'''
    AddtoHistory "DefineLumpedElement.{lumped_element_name}_" & i & "_" & j, _
    "With LumpedElement "  + vbCrLf + _
    "     .Reset " + vbCrLf + _
    "     .SetName ""{lumped_element_name}_" & i & "_" & j &""" " + vbCrLf + _
    "     .Folder ""{folder_name}"" " + vbCrLf + _
    "     .SetType ""{type}"" " + vbCrLf + _
    "     .SetR ""{R}_" & i & "_" & j & """ " + vbCrLf + _
    "     .SetL ""{L}_" & i & "_" & j & """ " + vbCrLf + _
    "     .SetC ""{C}_" & i & "_" & j & """ " + vbCrLf + _
    "     .SetGs ""0"" " + vbCrLf + _
    "     .SetI0 ""1e-14"" " + vbCrLf + _
    "     .SetT ""300"" " + vbCrLf + _
    "     .SetMonitor ""True"" " + vbCrLf + _
    "     .SetRadius ""0.0"" " + vbCrLf + _
    "     .CircuitFileName """" " + vbCrLf + _
    "     .CircuitId ""1"" " + vbCrLf + _
    "     .UseCopyOnly ""True"" " + vbCrLf + _
    "     .UseRelativePath ""False"" " + vbCrLf + _
    "     .SetP1 ""True"", ""{p1_x}+{period}*(-{x_size}/2-0.5+" & i & ")"", ""{p1_y}+{period}*(-{y_size}/2-0.5+" & j & ")"", ""{p1_z}"" " + vbCrLf + _
    "     .SetP2 ""True"", ""{p2_x}+{period}*(-{x_size}/2-0.5+" & i & ")"", ""{p2_y}+{period}*(-{y_size}/2-0.5+" & j & ")"", ""{p2_z}"" " + vbCrLf + _
    "     .Create "+ vbCrLf + _
    "End With"
    '''
    # delete the auxiliary line for modelling
    vba = delete_curve(vba, "curve_aux")
    return vba

def store_parameter_list(vba, parameter_name, value_list_path):
    A = np.loadtxt(value_list_path, delimiter=';', dtype=float)
    line_num = A.shape[0]
    row_num = A.shape[1]
    for i in range(0,line_num):
        for j in range(0,row_num):
            value = A[i,j]
            vba += f'''
             AddtoHistory "AddParameter.{parameter_name}_{i+1}_{j+1}", _ 
             "StoreParameter(""{parameter_name}_{i+1}_{j+1}"",""{value}"") "
            '''
    return vba