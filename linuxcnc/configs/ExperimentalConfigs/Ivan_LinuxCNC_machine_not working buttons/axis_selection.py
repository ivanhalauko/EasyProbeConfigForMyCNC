
# setup joint/axis selection from halui pins
halui_ja_selection = {'valid':False}
if hal.component_is_ready('halui'):
    halui_ja_selection['valid'] = True
    halui_ja_selection['joints'] = list(range(num_joints))
    for joint in halui_ja_selection['joints']:
        halui_ja_selection[joint] = False
    halui_ja_selection['axes'] = list(unique_axes(trajcoordinates, 'XYZABCUVW').lower())
    for axis in halui_ja_selection['axes']:
        halui_ja_selection[axis] = False
    print('halui_ja_selection = {}'.format(halui_ja_selection))
def user_live_update():
    # if halui is running then halui joint/axis selection will select
    # the corresponding radio button on the low to high transition
    if halui_ja_selection['valid']:
        if not vars.teleop_mode.get():
            for j in halui_ja_selection['joints']:
                if hal.get_value('halui.joint.{}.select'.format(j)):
                    if not halui_ja_selection[j]:
                        halui_ja_selection[j] = True
                        root_window.tk.eval('$_tabs_manual.joints.joint{} invoke'.format(j))
                else:
                    halui_ja_selection[j] = False
        else:
            for a in (halui_ja_selection['axes']):
                if hal.get_value('halui.axis.{}.select'.format(a)):
                    if not halui_ja_selection[a]:
                        halui_ja_selection[a] = True
                        root_window.tk.eval('$_tabs_manual.axes.axis{} invoke'.format(a))
                else:
                    halui_ja_selection[a] = False
