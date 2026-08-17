import unreal


ASSETS = (
    "/Game/OUTTRIGGER/Blueprints/BP_CharacterSpawnPoint",
    "/Game/OUTTRIGGER/Blueprints/BP_BaseGameMode",
    "/Game/OUTTRIGGER/Blueprints/BP_BaseGameState",
)


def prop(obj, name, default=None):
    try:
        return obj.get_editor_property(name)
    except Exception:
        return default


def describe_pin(pin):
    name = prop(pin, "pin_name", "?")
    default = prop(pin, "default_value", "")
    linked = []
    for other in prop(pin, "linked_to", ()) or ():
        owner = prop(other, "owning_node")
        linked.append(f"{owner.get_name() if owner else '?'}:{prop(other, 'pin_name', '?')}")
    return f"      pin={name!s} default={str(default)!r} links={linked}"


for asset_path in ASSETS:
    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    print(f"\n=== {asset_path} ({asset.get_class().get_name() if asset else 'MISSING'}) ===")
    if not asset:
        continue

    for graphs_property in ("ubergraph_pages", "function_graphs", "macro_graphs"):
        graphs = prop(asset, graphs_property, ()) or ()
        print(f"  {graphs_property}: {len(graphs)}")
        for graph in graphs:
            print(f"    GRAPH {graph.get_name()}")
            for node in prop(graph, "nodes", ()) or ():
                title = ""
                try:
                    title = node.get_node_title(unreal.NodeTitleType.FULL_TITLE)
                except Exception:
                    pass
                print(f"    NODE {node.get_name()} class={node.get_class().get_name()} title={title}")
                for pin in prop(node, "pins", ()) or ():
                    print(describe_pin(pin))

    generated_class = None
    try:
        generated_class = asset.generated_class()
    except Exception:
        generated_class = prop(asset, "generated_class")
    if generated_class:
        cdo = unreal.get_default_object(generated_class)
        print(f"  CDO {cdo.get_name()}")
        for property_name in ("is_reserved", "spawn_points"):
            value = prop(cdo, property_name, "<unavailable>")
            print(f"    {property_name}={value}")

    if generated_class:
        world = unreal.get_editor_subsystem(
            unreal.UnrealEditorSubsystem
        ).get_editor_world()
        unreal.SystemLibrary.execute_console_command(
            world, f"DISASMSCRIPT {generated_class.get_name()}"
        )
