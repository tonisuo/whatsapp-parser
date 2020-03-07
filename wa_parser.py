import codecs

# If media is omitted when exporting, this const is used to remove those lines
MEDIA_OMITTED_TEXT = '<Media omitted>'

class WhatsAppParser():
    def __init__(self, inputFilePath, speakerName):
        if not inputFilePath:
            raise ValueError('Empty file path not allowed')
        self.speakerName = speakerName
        self.inputFilePath = inputFilePath
        self.raw_messages = []
        self.formatted_speaker_lines = []
        self.formatted_lines = []
        self.full_corpus = ''
        self.speakers = []

    def open_file(self):
        arq = codecs.open(self.inputFilePath, 'r', 'utf-8-sig')
        content = arq.read()
        arq.close()
        lines = content.split('\n')
        lines = [l for l in lines if len(l) > 4]
        for line in lines:
            if (MEDIA_OMITTED_TEXT not in line and line[0].isdigit()):
        	    self.raw_messages.append(line.encode('utf-8'))
    
    def filter_lines_by_speaker(self):
        speakerLines = list(filter(lambda line: self.speakerName+':' in line, self.raw_messages))
        return speakerLines

    def extract_speakers_words(self, lines):
        speakerNameLength = len(self.speakerName)
        offsetToMessage = 2
        for line in lines:
            index = line.find(self.speakerName+':') + speakerNameLength + offsetToMessage
            formatted = line[index:]
            self.formatted_speaker_lines.append(formatted)
    
    def extract_all_messages(self):
        offsetToMessage = 2
        for line in self.raw_messages:
            if(':' in line):
                index = line.find(':') + offsetToMessage
                formatted = line[index:]
                self.formatted_lines.append(formatted)
    
    def print_all_messages_formatted(self):
        if not self.formatted_lines:
            self.extract_all_messages()
        for line in self.formatted_lines:
            print(line)
    
    def get_speakers(self):
        offsetFromPartition = 2
        for line in self.raw_messages:
            if(':' in line):
                index = line.find('-') + offsetFromPartition
                speaker = line[index:line.find(':')]
                if(speaker not in self.speakers):
                    self.speakers.append(speaker)
    
    def print_speakers(self):
        if not self.speakers:
            self.get_speakers()
        print(self.speakers)

    def write_speakers_lines_to_file_newLine(self, outputFileName):
        file = open(outputFileName, 'w+')
        for line in self.formatted_speaker_lines:
            file.write(line + '\n')
    
    def write_speakers_lines_to_file_corpus(self, outputFileName):
        file = open(outputFileName, 'w+')
        for line in self.formatted_speaker_lines:
            end = ' ' if line.endswith('.') else '. '
            file.write(line + end)