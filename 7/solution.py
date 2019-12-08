#!/usr/bin/env python3
import argparse
import io


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Solves the Space Image Format puzzle")
    parser.add_argument("filename", type=argparse.FileType("r"))
    parser.add_argument("-W", "--width", default=25, type=int)
    parser.add_argument("-H", "--height", default=6, type=int)

    args = parser.parse_args()
    width = args.width
    height = args.height
    print(f"Width: {width!r}, Height: {height!r}")

    data = args.filename.readline().strip()

    layer_size = width * height
    layers = []
    position = 0
    while position < len(data):
        layer_data = data[position:position+layer_size]
        layer = []
        row_num = 0
        for _ in range(height):
            layer.append(layer_data[row_num*width:(row_num+1)*width])
            row_num += 1        
        layers.append(layer)
        position += layer_size

    flattened_img = []
    for i in range(height):
        row = ''
        for j in range(width):
            for layer in layers:
                if layer[i][j] != "2":
                    row += layer[i][j]
                    break
        flattened_img.append(row)

    for row in flattened_img:
        print(row)