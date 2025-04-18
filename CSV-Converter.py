# This will only work for Skiley Spotify CSV files

import csv
import argparse


def convert_csv_to_playlist(input_csv, output_txt=None):
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        lines = []
        for row in reader:
            artist = row.get('artistName', '').strip()
            title = row.get('trackName', '').strip()
            if artist and title:
                lines.append(f"{artist} - {title}")

    # Sort alphabetically, case-insensitive
    lines.sort(key=lambda x: x.lower())

    if output_txt:
        with open(output_txt, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
        print(f"Playlist saved to {output_txt}")
    else:
        for line in lines:
            print(line)


def main():
    parser = argparse.ArgumentParser(description='Convert Spotify songs CSV to playlist format.')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('-o', '--output', help='Output text file (optional)', default=None)
    args = parser.parse_args()

    convert_csv_to_playlist(args.csv_file, args.output)


if __name__ == '__main__':
    main()
