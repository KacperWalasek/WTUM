import PySimpleGUI as sg


def create_picture_window(picture, label=''):
    window = sg.Window(title=label + ' - ' + picture.label,
                       layout=[[sg.Graph(canvas_size=(280, 280), graph_bottom_left=(0, 0), graph_top_right=(280, 280),
                                         background_color='red', enable_events=True, key='graph')]],
                       finalize=True)
    graph = window['graph']
    for i in range(0, 28):
        for j in range(0, 28):
            val = int(picture.pixels[j][i])
            graph.draw_rectangle((10*i, 270-10*j), (10*i+10, 280-10*j),
                                 line_width=0, fill_color='#%02x%02x%02x' % (val, val, val))


def show_pictures(picture_list):
    for picture in picture_list:
        create_picture_window(picture[0], picture[1])
    sg.read_all_windows()

