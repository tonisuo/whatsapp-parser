from os import path
from wa_parser import *


def parse_whatsapp_file():
    parser = WhatsAppParser('whatsapp_chat.txt', 'Chat Person1')
    parser.open_file()
    lines = parser.filter_lines_by_speaker()
    parser.extract_speakers_words(lines)
    parser.print_speakers()
    parser.write_speakers_lines_to_file_newLine('Person1.txt')
    parser.write_speakers_lines_to_file_corpus('Person1Corpus.txt')
    parser.print_all_messages_formatted()

if __name__ == '__main__':
    parse_whatsapp_file()