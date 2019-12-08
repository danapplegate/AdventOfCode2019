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
    print(data)

    layer_size = width * height
    layers = []
    position = 0
    while position < len(data):
        layers.append(data[position:position+layer_size])
        position += layer_size

    print(layers)
    zero_counts = [layer.count('0') for layer in layers]
    final_layer = layers[zero_counts.index(min(zero_counts))]
    answer = final_layer.count('1') * final_layer.count('2')
    print(f"Anser: {answer}")