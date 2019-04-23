import numpy as np
import os

def load_topic(fname):
    f = open(fname)
    cnt, idx, pidx, title_char, title_word, desc_char, desc_word = 0, [], [], [], [], [], []
    print "Load topic start!"
    with open(fname,"r") as f:
        for line in f:
            cnt += 1
            if cnt % 100 == 0:
                print cnt
            terms = line.strip().split('\t')
            idx.append(terms[0])
            if len(terms) == 6:
                pidx.append(terms[1])
                title_char.append(terms[2])
                title_word.append(terms[3])
                desc_char.append(terms[4])
                desc_word.append(terms[5])
            elif len(terms) == 5:
                pidx.append(terms[1])
                title_char.append(terms[2])
                title_word.append(terms[3])
                desc_char.append(terms[4])
                desc_word.append('')
            elif len(terms) == 4:
                pidx.append(terms[1])
                title_char.append(terms[2])
                title_word.append(terms[3])
                desc_char.append('')
                desc_word.append('')
    print "Load topic finish!"
    return idx, pidx, title_char, title_word, desc_char, desc_word

topic_file = '../ieee_zhihu_cup/topic_info.txt'
topic_idx, topic_pidx, topic_title_char, topic_title_word, topic_desc_char, \
                                topic_desc_word = load_topic(topic_file)

basedir = './topic'
if not os.path.exists(basedir):
    os.mkdir(basedir)

np.save('{}/topic_idx.npy'.format(basedir), topic_idx)