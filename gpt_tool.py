tools = [
    {
        "type": "function",
        "name": "define_material_RogersAD260Clossy",
        "description": "Define the material named 'Rogers AD 260C', and the material is lossy or without specifically note it is not lossy.",
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_material_FR4lossy",
        "description": "Define the material named 'FR-4', and the material is lossy or without specifically note it is not lossy.",
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_material_PTFElossy",
        "description": "Define the material named 'PTFE', and the material is lossy or without specifically note it is not lossy.",
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "store_parameter",
        "description": "Define the parameters by the name and the value, and can also be used to change the value of an existing parameter.",
        "parameters": {
            "type": "object",
            "properties": {
                "parameter_name" : {"type": "string",
                                    "description":"The name of the parameter, e.g., width, length"},
                "parameter_value" : {"type": ["string","number"],
                                    "description":"The value of the parameter, and it can be either a number or a value or the name of another parameter, e.g., width, length, 5, 20"},
            },
            "required": ["parameter_name","parameter_value"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "store_parameter_list",
        "description": "Define the parameters by the name and the value, and can also be used to change the value of an existing parameter."
                       "The function will load a file claimed by the user and the file contains the values of the parameters, as a result, a list of parameters will be defined with the list of the values. ",
        "parameters": {
            "type": "object",
            "properties": {
                "parameter_name" : {"type": "string",
                                    "description":"The name of the parameter, e.g., width, length"},
                "value_list_path" : {"type": "string",
                                    "description":"The file that contains the values of the parameter"},
            },
            "required": ["parameter_name","value_list_path"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_component",
        "description": "Define a new component with its name.",
        "parameters": {
            "type": "object",
            "properties": {
                "component_name" : {"type": "string",
                                    "description":"The name of the new component, e.g., component1, substrate"},
            },
            "required": ["component_name"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_brick",
        "description": "Define a brick model or rectangular model with its name, which component it belongs to, material used, and its boundary values.",
        "parameters": {
            "type": "object",
            "properties": {"brick_name" : {"type": "string",
                                           "description":"The name of the new brick, e.g., brick1, patch1"},
                           "component_name" : {"type": "string",
                                               "description":"The name of the component that the brick belongs to, e.g., component1, substrate"},
                           "material" : {"type": "string",
                                         "description":"The name of the material that used to build the model, e.g., PEC, FR-4 (lossy)"},
                           "x_min" : {"type": ["string","number"],
                                      "description":"The lower x boundary of the defined brick (rectangular), and it can either be a name of a parameter or a number, e.g., len/2, -wid/2"},
                           "x_max" : {"type": ["string","number"],
                                      "description":"The higher x boundary of the defined brick (rectangular), and it can either be a name of a parameter or a number, e.g., len/2, -wid/2"},
                           "y_min" : {"type": ["string","number"],
                                      "description":"The lower y boundary of the defined brick (rectangular), and it can either be a name of a parameter or a number, e.g., len/2, -wid/2"},
                           "y_max" : {"type": ["string","number"],
                                      "description":"The higher y boundary of the defined brick (rectangular), and it can either be a name of a parameter or a number, e.g., len/2, -wid/2"},
                           "z_min" : {"type": ["string","number"],
                                      "description":"The lower z boundary of the defined brick (rectangular), and it can either be a name of a parameter or a number, e.g., len/2, -wid/2"},
                           "z_max" : {"type": ["string","number"],
                                      "description":"The higher z boundary of the defined brick (rectangular), and it can either be a name of a parameter or a number, e.g., len/2, -wid/2"},
                           },
            "required": ["brick_name", "component_name", "material", "x_min", "x_max", "y_min", "y_max", "z_min", "z_max"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "rotate_around_origin",
        "description": "Rotate a model around an axis (x, y, or z).",
        "parameters": {
            "type": "object",
            "properties": {"model_name": {"type": "string",
                                          "description": "The name of the model to be rotated, e.g., brick1, patch1"},
                           "component_name": {"type": "string",
                                              "description": "The name of the component that the model belongs to, e.g., component1, substrate"},
                           "angle_x" : {"type": ["string","number"],
                                      "description":"The rotation angle around x axis, and it can either be a name of a parameter or a number, the default value is 0, e.g., angle1, angle_x"},
                           "angle_y" : {"type": ["string","number"],
                                      "description":"The rotation angle around y axis, and it can either be a name of a parameter or a number, the default value is 0, e.g., angle2, angle_y"},
                           "angle_z" : {"type": ["string","number"],
                                      "description":"The rotation angle around z axis, and it can either be a name of a parameter or a number, the default value is 0, e.g., angle1, angle_z"},
                           "multipleobjects" : {"type": "boolean",
                                                "description":"This parameter shows whether the model is duplicated or copied during the rotation, and it has only two choices: 'True' or 'False'."},
                           "repetition" : {"type": "number",
                                           "description":"When the multipleobjects is 'False' (the model will not be duplicated), the value of this parameter is set as 1, and when the multipleobjects is 'True', this parameter is decide by how many new models will be created during the duplication, for example, if the model is required to be duplicated three times, the value of this parameter is 3. "},
                           },
            "required": ["model_name", "component_name", "angle_x", "angle_y", "angle_z", "multipleobjects", "repetition"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "boolean_add",
        "description": "Add two models together, the first model the user mentioned is the model 1, and the component it belongs to is the component 1.",
        "parameters": {
            "type": "object",
            "properties": {"component_name_1": {"type": "string",
                                                "description": "The name of the component the model, and this model is the first model to be added, e.g., brick1, patch1"},
                           "model_name_1": {"type": "string",
                                            "description": "The name of the first model to be added, e.g., component1, substrate"},
                           "component_name_2" : {"type": "string",
                                                 "description":"The name of the component the model, and this model is the second model to be added, e.g., brick1, patch1"},
                           "model_name_2" : {"type": "string",
                                             "description":"The name of the second model to be added, e.g., component1, substrate"},
                           },
            "required": ["component_name_1", "model_name_1", "component_name_2", "model_name_2"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "rename_model",
        "description": "Change the name of a model without changing the component name it belongs to or the component it belongs to",
        "parameters": {
            "type": "object",
            "properties": {"model_old_name": {"type": "string",
                                              "description": "The old name of the the model (the model that needs to be renamed), e.g., brick1, patch1"},
                           "component_name": {"type": "string",
                                              "description": "The name of the component the model belongs to, e.g., component 1, sub1"},
                           "model_new_name": {"type": "string",
                                              "description": "The new name of the model, e.g., brick2, patch2"},
                           },
            "required": ["model_old_name", "component_name", "model_new_name"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_cylinder_z",
        "description": "Define a cylinder model, the top and bottom are parallel to the xoy plane and it is stretched along z direction, and the model is defined by its material, and the cylinder can be solid or hollowed, depending on the definition of the parameters.",
        "parameters": {
            "type": "object",
            "properties": {"cylinder_name": {"type": "string",
                                              "description": "The name of the cylinder model to be defined), e.g., via, model_1"},
                           "component_name": {"type": "string",
                                              "description": "The name of the component the model belongs to, e.g., component 1, sub1"},
                           "material_name": {"type": "string",
                                             "description": "The name of the material used for modeling the cylinder"},
                           "outer_radius": {"type": ["string","number"],
                                            "description": "The outer radius of the cylinder, e.g., r1, r_out,9"},
                           "inner_radius": {"type": ["string","number"],
                                            "description": "The inner radius of the hollowed part of the cylinder, if the cylinder is solid, this value is 0, if now special description about whether the cylinder is solid or hollowed, the default value of this parameter is 0 e.g., r1, r_out,5,0"},
                           "z_min": {"type": ["string","number"],
                                     "description": "The z coordinate of the bottom or the lower plane of te cylinder, e.g., 2, a, h1"},
                           "z_max": {"type": ["string","number"],
                                     "description": "The z coordinate of the top or the higher plane of te cylinder, e.g., 9, b, h2"},
                           "x_center": {"type": ["string","number"],
                                        "description": "The x coordinate of the center of the cylinder, e.g., x, 0"},
                           "y_center": {"type": ["string","number"],
                                        "description": "The y coordinate of the center of the cylinder, e.g., y, 0"},
                           },
            "required": ["cylinder_name", "component_name", "material_name", "outer_radius", "inner_radius", "z_min", "z_max", "x_center", "y_center"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_line_xy",
        "description": "Define a line in the xoy plane with the coordinate of the beginning point to the ending point, the line will be under the directory of the curve.",
        "parameters": {
            "type": "object",
            "properties": {"line_name": {"type": "string",
                                         "description": "The name of the line, e.g., line1"},
                           "curve_name": {"type": "string",
                                          "description": "The name of the curve the line belongs to, e.g., curve 1"},
                           "start_point_x": {"type": ["string","number"],
                                             "description": "The x coordinate of the starting point of the line, e.g., x1, 2"},
                           "end_point_x": {"type": ["string","number"],
                                           "description": "The x coordinate of the ending point of the line, e.g., x2, 4"},
                           "start_point_y": {"type": ["string","number"],
                                             "description": "The y coordinate of the starting point of the line, e.g., y1, 2"},
                           "end_point_y": {"type": ["string","number"],
                                           "description": "The y coordinate of the ending point of the line, e.g., y2, 4"},
                           },
            "required": ["line_name", "curve_name", "start_point_x", "end_point_x", "start_point_y", "end_point_y"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "transform_curve",
        "description": "Transform or movement operation of the curve (including line)",
        "parameters": {
            "type": "object",
            "properties": {"curve_name": {"type": "string",
                                          "description": "The name of the curve, e.g., curve1"},
                           "vector_x": {"type": ["string","number"],
                                        "description": "The x value of the movement vector, it can be either a string or a nuber, "
                                                       "the abs value of this parameter is the distance of the movement and it can be a string or a number, "
                                                       "and the sign of this parameter means the direction of the movement, positive sign means moving towards +x, negative sign means moving towards -x, e.g., P, -a, -4, 3"},
                           "vector_y": {"type": ["string","number"],
                                        "description": "The y value of the movement vector, it can be either a string or a nuber, "
                                                       "the abs value of this parameter is the distance of the movement and it can be a string or a number, "
                                                       "and the sign of this parameter means the direction of the movement, positive sign means moving towards +y, negative sign means moving towards -y, e.g., P, -a, -4, 3"},
                           "vector_z": {"type": ["string","number"],
                                        "description": "The z value of the movement vector, it can be either a string or a nuber, "
                                                       "the abs value of this parameter is the distance of the movement and it can be a string or a number, "
                                                       "and the sign of this parameter means the direction of the movement, positive sign means moving towards +z, negative sign means moving towards -z, e.g., P, -a, -4, 3"},
                           "multipleobjects": {"type": "boolean",
                                               "description":"This parameter shows whether the model is duplicated or copied during the rotation, and it has only two choices: 'True' or 'False'."
                                                             "The default value is false if there is no description. "},
                           "repetition": {"type": ["string","number"],
                                          "description": "When the multipleobjects is 'False' (the model will not be duplicated), the value of this parameter is set as 1, and when the multipleobjects is 'True', this parameter is decide by how many new models will be created during the duplication, for example, if the model is required to be duplicated three times, the value of this parameter is 3."},
                           },
            "required": ["curve_name", "vector_x", "vector_y", "vector_z", "multipleobjects", "repetition"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "pick_end_points",
        "description": "pick the two end points of a line under the directory of a curve",
        "parameters": {
            "type": "object",
            "properties": {"curve_name": {"type": "string",
                                          "description": "The name of the curve the line belongs to, e.g., curve1"},
                           "line_name": {"type": ["string","number"],
                                         "description": "The name of the line to be picked"},
                           },
            "required": ["curve_name", "line_name"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "define_lumped_element_RLC_wire",
        "description": "Define a lumped element, the element is on a wire and is composed of (equivalent of) a series or parallel RLC circuit.",
        "parameters": {
            "type": "object",
            "properties": {"lumped_element_name": {"type": "string",
                                                   "description": "The name of the curve the lumped element, e.g., element 1"},
                           "folder_name": {"type": "string",
                                           "description": "The name of the folder the lumped element belongs to, e.g., folder1"},
                           "type": {"type": "string",
                                    "description": "The type of the lumped element, based on the description, the value of this parameter should be chosen from the following only:"
                                                   "RLCSerial or RLCParallel"},
                           "R": {"type": ["string","number"],
                                 "description": "The value of the R in the RLC lumped element, the default value is 0, e.g., R1, 1e-9"},
                           "L": {"type": ["string","number"],
                                 "description": "The value of the L in the RLC lumped element, the default value is 0, e.g., L1, 1e-9"},
                           "C": {"type": ["string","number"],
                                 "description": "The value of the C in the RLC lumped element, the default value is 0, e.g., C1, 1e-9"},
                           "p1_x": {"type": "string",
                                    "description": "The x coordinate of the starting point of the wire, e.g., x1, 2"},
                           "p1_y": {"type": "string",
                                    "description": "The y coordinate of the starting point of the wire, e.g., y1, 2"},
                           "p1_z": {"type": "string",
                                    "description": "The z coordinate of the starting point of the wire, e.g., z1, 2"},
                           "p2_x": {"type": "string",
                                    "description": "The x coordinate of the ending point of the wire, e.g., x2, 3"},
                           "p2_y": {"type": "string",
                                    "description": "The y coordinate of the ending point of the wire, e.g., y2, 3"},
                           "p2_z": {"type": "string",
                                    "description": "The z coordinate of the ending point of the wire, e.g., z2, 3"},
                           },
            "required": ["lumped_element_name", "folder_name", "type", "R", "L", "C", "p1_x", "p1_y", "p1_z", "p2_x", "p2_y", "p2_z"],
            "additionalProperties": False
        },
        "strict": True
    },
# Array modelling mode
    {
        "type": "function",
        "name": "array_mode_start",
        "description": "Call this function when the user wants to use the array mode.",
        "parameters": {
            "type": "object",
            "properties": {"x_size": {"type": "number",
                                      "description": "The number of the elements (also known as unit cells) in the array along the x direction, e.g., 3, 16"},
                           "y_size": {"type": "number",
                                      "description": "The number of the elements (also known as unit cells) in the array along the y direction, e.g., 3, 16"},
                           "period": {"type": ["number","string"],
                                      "description": "The period of the element (also known as unit cells), which is the length of the element, and the element is a square shape."},
                           },
            "required": ["x_size", "y_size", "period"],
            "additionalProperties": False
        },
        "strict": True
    },
]