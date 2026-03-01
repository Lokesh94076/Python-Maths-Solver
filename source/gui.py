### THIS CODE WAS WRITEN WITH AI, ENTIRELY!
### THIS WAS CREATED AS A DEMO THAT GUI WRAPPER CAN BE USED.
### LATER A VISUAL WRAPPER WILL BE CREATED, SAME AS THIS-


import dearpygui.dearpygui as dpg
import uuid
from . import main as maths
dpg.create_context()
TERMINAL_HEIGHT = 200
BUTTON_HEIGHT = 40
MARGIN = 20
nodes = {}
links = {}
PRESETS = {
    "Add": {"domain": "smp", "operation": "add", "args": 2},
    "Subtract": {"domain": "smp", "operation": "sub", "args": 2},
    "Multiply": {"domain": "smp", "operation": "mul", "args": 2},
    "Divide": {"domain": "smp", "operation": "div", "args": 2},
    "Power": {"domain": "adv", "operation": "pow", "args": 2},
    "Pi": {"domain": "const", "operation": "pi", "args": 0},
}
output = "No Output"

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # Increase this number (e.g., 10, 15, 20) for more roundness
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 7)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 9)
        # Optional: round the borders of buttons and inputs too
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 7)
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
        dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0)
        dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, 0.5)
        dpg.add_theme_style(dpg.mvNodeStyleVar_GridSpacing, 25)
        dpg.add_theme_style(dpg.mvNodeStyleVar_NodeCornerRounding, 15)
        dpg.add_theme_style(dpg.mvNodeStyleVar_NodeBorderThickness, 2)
        dpg.add_theme_style(dpg.mvNodeStyleVar_LinkThickness, 5)
        dpg.add_theme_style(dpg.mvNodeStyleVar_PinCircleRadius, 5)
# 2. Bind the theme globally
dpg.bind_theme(global_theme)

with dpg.font_registry():
    # Load a larger font and set it as the default
    with dpg.font("C:\\Windows\\Fonts\\Arial.ttf", 17) as main_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range(0x25A0, 0x25FF) 
ad = 0
def resize_layout():
    global ad
    vh = dpg.get_viewport_client_height()
    wdth = dpg.get_item_width("main_window")
    editor_height = vh - TERMINAL_HEIGHT - BUTTON_HEIGHT - MARGIN
    if editor_height < 100:
        editor_height = 100
    dpg.configure_item("editor_container", height=editor_height)
    if ad != 0:
        dpg.set_item_pos("run_window", pos=(((wdth/2)-118), -50))
    else:
        dpg.set_item_pos("run_window", pos=(((1600/2)-118), -50))
    ad+=1
# --------------------------
# UTIL
# --------------------------

def uid():
    return str(uuid.uuid4())

# --------------------------
# BUILD
# --------------------------

def build(node_id):
    node = nodes[node_id]
    args = []

    for arg in node["args"]:
        if arg["type"] == "literal":
            args.append(arg["value"])
        elif arg["type"] == "node":
            args.append(build(arg["value"]))

    arg_string = ", ".join(args)

    if arg_string:
        return f'maths.{node["domain"]}("{node["operation"]}", {arg_string})'
    else:
        return f'maths.{node["domain"]}("{node["operation"]}")'

# --------------------------
# ROOT LOGIC
# --------------------------

def detect_root():
    # 1️⃣ If user selected node → use that
    selected = dpg.get_selected_nodes("editor")
    if selected:
        return selected[0]

    # 2️⃣ Otherwise auto-detect
    children = set()
    for parent, index in links.values():
        arg = nodes[parent]["args"][index]
        if arg["type"] == "node":
            children.add(arg["value"])

    for node_id in nodes:
        if node_id not in children:
            return node_id

    return None

# --------------------------
# NODE CREATION
# --------------------------
available_preset = []

def create_preset_node(sender, app_data, user_data):

    preset_name = app_data
    preset = PRESETS[preset_name]
    mouse_pos = dpg.get_mouse_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    node_id = dpg.generate_uuid()

    nodes[node_id] = {
        "domain": preset["domain"],
        "operation": preset["operation"],
        "args": []
    }

    with dpg.node(parent="editor", tag=node_id, pos=(x, y)):

        # Header
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=False):

                dpg.add_combo(
                    ["smp", "adv", "cmplx", "const", "doc"],
                    default_value=preset["domain"],
                    width=90,
                    callback=update_domain,
                    user_data=node_id
                )

                with dpg.group():
                    dpg.add_combo(
                        maths.get_all_commands(),
                        default_value=None,
                        width=130,
                        callback=update_operation,
                        user_data=node_id
                    )
                    dpg.add_input_text(label="Custom Command", width=130, callback=update_operation, user_data=node_id)
                dpg.add_button(
                    label="+",
                    width=25,
                    height=25,
                    callback=add_argument,
                    user_data=node_id
                )

        # Add correct number of arguments
        for _ in range(preset["args"]):
            add_argument(None, None, node_id)

        # Output attribute
        with dpg.node_attribute(
            attribute_type=dpg.mvNode_Attr_Output,
            user_data=node_id
        ):
            dpg.add_separator()
            dpg.add_text("Input-")

    
def create_node():

    node_id = dpg.generate_uuid()
    mouse_pos = dpg.get_mouse_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    nodes[node_id] = {
        "domain": "smp",
        "operation": "add",
        "args": []
    }

    with dpg.node(parent="editor", tag=node_id, pos=(x, y)):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=False):
                with dpg.group(horizontal=True):
                    dpg.add_combo(
                        ["smp", "adv", "cmplx", "const", "doc"],
                        default_value="smp",
                        width=130,
                        callback=update_domain,
                        user_data=node_id
                    )
                    dpg.add_button(
                    label="+",
                    width=25,
                    height=25,
                    callback=add_argument,
                    user_data=node_id
                )
                
                with dpg.group():
                    dpg.add_combo(
                        maths.get_all_commands(),
                        default_value=None,
                        width=130,
                        callback=update_operation,
                        user_data=node_id
                    )
                    dpg.add_input_text(label="Custom Command", width=130, callback=update_operation, user_data=node_id)

                

        with dpg.node_attribute(
            attribute_type=dpg.mvNode_Attr_Output,
            user_data=node_id
        ):
            dpg.add_separator()
            dpg.add_text("Input-")
        add_argument(None, None, node_id)
        add_argument(None, None, node_id)
         # Right click popup for node
# Get viewport size
        

MASTER_NODE = None

def create_master_node():
    global MASTER_NODE

    MASTER_NODE = dpg.generate_uuid()

    nodes[MASTER_NODE] = {
        "domain": "smp",
        "operation": "OUTPUT",
        "args": [{"type": "literal", "value": "0"}]
    }

    with dpg.node(parent="editor", tag=MASTER_NODE):

        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_text((output+" -Output"), tag="masternode_text")
            dpg.add_text((output+" -Command"), tag="masternode_command")

        with dpg.node_attribute(
            attribute_type=dpg.mvNode_Attr_Input,
            user_data={"node_id": MASTER_NODE, "arg_index": 0}
        ):
            dpg.add_text("")

    # Position it nicely
    dpg.set_item_pos(MASTER_NODE, [1000, 200])

def rebuild_node(node_id):
    children = dpg.get_item_children(node_id, 1)
    for child in children:
        meta = dpg.get_item_user_data(child)
        if isinstance(meta, dict) and "arg_index" in meta:
            dpg.delete_item(child)

    old = nodes[node_id]["args"].copy()
    nodes[node_id]["args"] = []
    for arg in old:
        add_argument(None, None, node_id)
        nodes[node_id]["args"][-1] = arg

# --------------------------
# UPDATE CALLBACKS
# --------------------------

def update_domain(sender, app_data, user_data):
    if user_data in nodes:
        nodes[user_data]["domain"] = app_data


def update_operation(sender, app_data, user_data):
    if user_data in nodes:
        nodes[user_data]["operation"] = app_data

def update_argument(sender, app_data, user_data):
    node_id, index = user_data
    if node_id in nodes:
        nodes[node_id]["args"][index] = {
            "type": "literal",
            "value": app_data
        }

# --------------------------
# ARGUMENT MANAGEMENT
# --------------------------

def add_argument(sender, app_data, user_data):
    node_id = user_data

    if node_id not in nodes:
        return

    index = len(nodes[node_id]["args"])
    nodes[node_id]["args"].append({"type": "literal", "value": "0"})

    input_attr = dpg.generate_uuid()
    textbox_id = dpg.generate_uuid()

    with dpg.node_attribute(
        parent=node_id,
        tag=input_attr,
        attribute_type=dpg.mvNode_Attr_Input,
        user_data={
            "node_id": node_id,
            "arg_index": index,
            "textbox": textbox_id
        }
    ):
        with dpg.group(horizontal=True):

            dpg.add_input_text(
                tag=textbox_id,
                default_value="0",
                width=120,
                multiline=True,
                height=20,
                callback=update_argument,
                user_data=(node_id, index)
            )

            dpg.add_button(
                label="X",
                width=25,
                callback=delete_argument,
                user_data=(node_id, index)
            )

def delete_argument(sender, app_data, user_data):
    node_id, index = user_data

    if node_id not in nodes:
        return

    if index >= len(nodes[node_id]["args"]):
        return

    nodes[node_id]["args"].pop(index)
    rebuild_inputs(node_id)

def rebuild_inputs(node_id):

    children = dpg.get_item_children(node_id, 1)

    for child in children:
        meta = dpg.get_item_user_data(child)
        if isinstance(meta, dict) and "arg_index" in meta:
            dpg.delete_item(child)

    old_args = nodes[node_id]["args"].copy()
    nodes[node_id]["args"] = []

    for arg in old_args:
        add_argument(None, None, node_id)
        nodes[node_id]["args"][-1] = arg

# --------------------------
# LINKING
# --------------------------

def link_callback(sender, app_data):
    output_attr, input_attr = app_data

    input_meta = dpg.get_item_user_data(input_attr)
    output_meta = dpg.get_item_user_data(output_attr)

    # Ensure we have valid metadata for both input and output
    if not input_meta or output_meta is None:
        return

    parent = input_meta["node_id"]
    index = input_meta["arg_index"]
    child = output_meta  # The child node connected to the parent

    # Prevent a node from linking to itself
    if parent == child:
        return

    # Update the nodes' arguments with the new connection
    nodes[parent]["args"][index] = {
        "type": "node",
        "value": child
    }

    # Hide the textbox (since it's no longer needed after linking)
    textbox_id = input_meta.get("textbox")
    if textbox_id:
        dpg.hide_item(textbox_id)

    # Generate the link and store it
    link_id = dpg.generate_uuid()
    dpg.add_node_link(output_attr, input_attr, parent="editor", tag=link_id)

    # Store the link in the links dictionary
    links[link_id] = (parent, index)

    # Optional: Hide the output pin if it’s no longer used
    if len(nodes[parent]["args"]) == 0:  # If the output pin has no connections
        dpg.hide_item(output_attr)

def delink_callback(sender, app_data):
    link_id = app_data

    if link_id in links:
        parent, index = links[link_id]
        nodes[parent]["args"][index] = {"type": "literal", "value": "0"}

        # Find attribute and show textbox again
        children = dpg.get_item_children(parent, 1)
        for child in children:
            meta = dpg.get_item_user_data(child)
            if isinstance(meta, dict) and meta.get("arg_index") == index:
                textbox_id = meta.get("textbox")
                if textbox_id:
                    dpg.show_item(textbox_id)
                break

        del links[link_id]

    dpg.delete_item(link_id)

# --------------------------
# DELETE + CLEAR
# --------------------------
def duplicate_node(sender, app_data, user_data):
    original = nodes[user_data]
    create_node()
    new_id = list(nodes.keys())[-1]
    nodes[new_id]["domain"] = original["domain"]
    nodes[new_id]["operation"] = original["operation"]

def connect_to_master(sender, app_data, user_data):
    node_id = user_data
    master_children = dpg.get_item_children(MASTER_NODE, 1)

    for child in master_children:
        meta = dpg.get_item_user_data(child)
        if isinstance(meta, dict):
            output_children = dpg.get_item_children(node_id, 1)
            for oc in output_children:
                config = dpg.get_item_configuration(oc)
                if config.get("attribute_type") == dpg.mvNode_Attr_Output:
                    link_callback(None, [oc, child])
                    return

def delete_selected():
    for link in dpg.get_selected_links("editor"):
        delink_callback(None, link)

    for node in dpg.get_selected_nodes("editor"):
        if node == MASTER_NODE:
            continue  # cannot delete master

        if node in nodes:
            del nodes[node]
        dpg.delete_item(node)
def clear_all():

    # Remove all links
    for link_id in list(links.keys()):
        dpg.delete_item(link_id)
    links.clear()

    # Delete all nodes except master
    for node_id in list(nodes.keys()):
        if node_id != MASTER_NODE:
            dpg.delete_item(node_id)
            del nodes[node_id]

    # Reset master argument
    nodes[MASTER_NODE]["args"][0] = {
        "type": "literal",
        "value": "0"
    }

    # Show master textbox again if hidden
    children = dpg.get_item_children(MASTER_NODE, 1)
    for child in children:
        meta = dpg.get_item_user_data(child)
        if isinstance(meta, dict):
            textbox_id = meta.get("textbox")
            if textbox_id:
                dpg.show_item(textbox_id)
    
# --------------------------
# GENERATE
# --------------------------

def generate():

    if MASTER_NODE not in nodes:
        log("Master node missing.")
        return

    arg = nodes[MASTER_NODE]["args"][0]

    if arg["type"] != "node":
        log("Master node not connected.")
        return

    root = arg["value"]

    command = build(root)

    # Print to terminal
    log(command)
    dpg.set_value("masternode_command", (str(command)+" -Command"))
    # Copy to clipboard
    dpg.set_clipboard_text(command)

# LOG

def log(message):
    dpg.add_text(message, parent="terminal")
    dpg.set_y_scroll("terminal", dpg.get_y_scroll_max("terminal"))


def run_command():

    if MASTER_NODE not in nodes:
        log("Master node missing.")
        return

    arg = nodes[MASTER_NODE]["args"][0]

    if arg["type"] != "node":
        log("Master node not connected.")
        return

    root = arg["value"]

    command = build(root)

    log("")
    log(">> " + command)

    try:
        # Execute using your wrapper
        result = eval(command, {"maths": maths})
        dpg.set_value("masternode_text", (str(result)+" -Output"))
        log("= " + str(result))
    except Exception as e:
        log("ERROR: " + str(e))
        dpg.set_value("masternode_text", (str(e)+" -Output"))

def clear_terminal():
    dpg.delete_item("terminal", children_only=True)
    dpg.add_text("=== Terminal ===", parent="terminal")   
    
# --------------------------
# GUI
# --------------------------


context_open = False

def show_context_menu(sender, app_data):
    global context_open

    if context_open:
        return

    mouse_pos = dpg.get_mouse_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    dpg.configure_item("editor_context_menu", pos=(x, y), show=True)
    dpg.focus_item("editor_context_menu")
    context_open = True


def left_click_handler(sender, app_data):
    global context_open

    if not context_open:
        return

    mouse_x, mouse_y = dpg.get_mouse_pos()
    win_x, win_y = dpg.get_item_pos("editor_context_menu")
    width, height = dpg.get_item_rect_size("editor_context_menu")

    inside_x = win_x <= mouse_x <= win_x + width
    inside_y = win_y <= mouse_y <= win_y + height

    if inside_x and inside_y:
        return

    dpg.configure_item("editor_context_menu", show=False)
    context_open = False


def close_context():
    global context_open
    dpg.configure_item("editor_context_menu", show=False)
    context_open = False

   
with dpg.window(tag="main_window"):
    
    with dpg.window(tag="run_window",
                    no_title_bar=True,
                    no_resize=True,
                    no_scrollbar=True,
                    no_move=True,
                    no_collapse=True, width=236, height=5, pos=(700, -50)):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Run \u25BA", pos=(7, 65), callback=run_command)
            dpg.add_button(label="Generate Command \u25CF", callback=generate)

    with dpg.window(
    tag="editor_context_menu",
    show=False,
    no_title_bar=True,
    no_resize=True,
    no_move=True,
    autosize=True,
    on_close=lambda: close_context()
):
       dpg.add_button(label="New Node", callback=lambda: (create_node(), close_context()))
       dpg.add_button(label="Clear Graph", callback=lambda: (clear_all(), close_context()))
       dpg.add_combo(
          list(PRESETS.keys()),
          label="Presets",
          width=150,
          callback=lambda sender, app_data: (
              create_preset_node(sender, app_data, None),
              close_context()
          )
      )
       dpg.add_button(label="Delete Node", callback=lambda: (delete_selected(), close_context()))
    dpg.add_child_window(tag="editor_container", autosize_x=True, height=500)

    with dpg.node_editor(
        parent="editor_container",
        tag="editor",
        callback=link_callback,
        delink_callback=delink_callback,
        minimap=True,
        minimap_location=dpg.mvNodeMiniMap_Location_BottomLeft,
        
    ):
        pass

    with dpg.group(horizontal=True):
        dpg.add_button(label="New Node", callback=create_node)
        dpg.add_button(label="Delete Selected", callback=delete_selected)
        dpg.add_button(label="Clear Editor", callback=clear_all)
        dpg.add_button(label="Clear Terminal", callback=clear_terminal)
        dpg.add_combo(
          list(PRESETS.keys()),
          label="Presets",
          width=150,
          callback=create_preset_node
      )
        dpg.add_button(label="Style Editor", callback=lambda: dpg.show_style_editor())
        dpg.add_button(label="Font Editor", callback=lambda: dpg.show_font_manager())
    dpg.add_child_window(tag="terminal", autosize_x=True,
                         height=TERMINAL_HEIGHT, border=True)
    dpg.add_text("=== TERMINAL ===", parent="terminal")


dpg.set_primary_window("main_window", True)

with dpg.handler_registry():
    dpg.add_mouse_click_handler(
        button=dpg.mvMouseButton_Right,
        callback=show_context_menu
    )

    dpg.add_key_press_handler(dpg.mvKey_Delete, callback=delete_selected)

create_master_node()

def main():
    dpg.create_viewport(title="Maths Visual Editor-PMS", width=1600, height=900)
    dpg.set_viewport_resize_callback(lambda: resize_layout())
    dpg.setup_dearpygui()
    dpg.bind_font(main_font)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


