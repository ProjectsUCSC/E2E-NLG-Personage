
voices_list=['AGREEABLE', 'DISAGREEABLE', 'EXTRAVERT', 'INTROVERT', 'OPEN','NOT_OPEN', 'SHY',
             'FORMAL', 'CONSCIENTIOUSNESS', 'UNCONSCIENTIOUSNESS' ]
voice_opp_dict = {'AGREEABLE': 'DISAGREEABLE', 'DISAGREEABLE': 'AGREEABLE',
              'OPEN':'NOT_OPEN', 'NOT_OPEN':'OPEN',
              'CONSCIENTIOUSNESS':'UNCONSCIENTIOUSNESS','UNCONSCIENTIOUSNESS': 'CONSCIENTIOUSNESS',
              'EXTRAVERT': 'INTROVERT', 'INTROVERT':'EXTRAVERT'}

def add_multiple_voices(das_filename, abst_filename):

    # print("in multiple voices")
    template = "convert(personality="

    filename2 = das_filename.replace(".txt", "_multi.txt")
    file2 = open(filename2, "w+")

    abst = open(abst_filename, "r")
    abst_filename2 = abst_filename.replace(".txt", "_multi.txt")
    abst2 = open(abst_filename2, "w+")

    with open(das_filename) as fp:
        line = fp.readline()
        abst_line = abst.readline()
        print("starting while line")
        while line:
            voice_old = line.split('&')[0].split('=')[1].replace(')','')
            # print(voice_old)
            for voice in voices_list:
                if voice == voice_old:
                    continue
                if voice == voice_opp_dict.get(voice_old):
                    continue
                line2 = template + voice + ")&" + line
                # print(abst_line)
                abst2.write(abst_line)
                file2.write(line2)


            line = fp.readline()
            abst_line = abst.readline()


    file2.close()
    fp.close()
    abst.close()
    abst2.close()

das_filename = "voices_dev_mtv_da-das_sample.txt"
abst_filename = "voices_dev_mtv_da-abst_sample.txt"
add_multiple_voices(das_filename, abst_filename)
