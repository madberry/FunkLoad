# (C) Copyright 2005 Nuxeo SAS <http://nuxeo.com>
# Author: bdelbosc@nuxeo.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#
"""A very simple Lorem ipsum generator.

$Id: Lipsum.py 24649 2005-08-29 14:20:19Z bdelbosc $
"""
import random

VOCAB = ('ad', 'aquam', 'albus', 'archaeos', 'arctos', 'argentatus',
         'arvensis', 'australis', 'biscort' 'borealis', 'brachy', 'bradus',
         'brevis', 'campus', 'cauda', 'caulos', 'cephalus', 'chilensis',
         'chloreus', 'cola', 'cristatus', 'cyanos', 'dactylus', 'deca',
         'dermis', 'delorum', 'di', 'diplo', 'dodeca', 'dolicho',
         'domesticus', 'dorsum', 'dulcis', 'echinus', 'ennea', 'erythro',
         'familiaris', 'flora', 'folius', 'fuscus', 'fulvus', 'gaster',
         'glycis', 'hexa', 'hortensis', 'it', 'indicus', 'lateralis',
         'leucus', 'lineatus', 'lipsem', 'lutea', 'maculatus', 'major',
         'maximus', 'melanus', 'minimus', 'minor', 'mono', 'montanus',
         'morphos', 'mauro', 'niger', 'nona', 'nothos', 'notos',
         'novaehollandiae', 'novaeseelandiae', 'noveboracensis', 'obscurus',
         'occidentalis', 'octa', 'oeos', 'officinalis', 'oleum',
         'orientalis', 'ortho', 'pachys', 'palustris', 'parvus', 'pedis',
         'pelagius', 'penta', 'petra', 'phyllo', 'phyton', 'platy',
         'pratensis', 'protos', 'pteron', 'punctatus', 'rhiza', 'rhytis',
         'rubra', 'rostra', 'rufus', 'sativus', 'saurus', 'sinensis',
         'stoma', 'striatus', 'silvestris', 'sit', 'so', 'tetra',
         'tinctorius', 'tomentosus', 'tres tris', 'trich thrix', 'unus',
         'variabilis', 'variegatus', 'ventrus', 'verrucosus', 'via',
         'viridis', 'volans', 'vulgaris', 'xanthos', 'zygos')

CHARS = "abcdefghjkmnopqrstuvwxyz123456789"

class Lipsum:
    """Kind of Lorem ipsum generator."""

    def __init__(self, vocab=VOCAB, chars=CHARS):
        self.vocab = vocab
        self.chars = chars

    def getWord(self):
        """Return a random word."""
        return random.choice(self.vocab)

    def getUniqWord(self):
        """Generate a kind of uniq id"""
        length = random.randrange(5, 9)
        chars = self.chars
        return ''.join([random.choice(chars) for i in range(length)])

    def getSubject(self, length=5, prefix=None, uniq=False):
        """Return a subject of length words."""
        subject = []
        if prefix:
            subject.append(prefix)
        if uniq:
            subject.append(self.getUniqWord())
        for i in range(length):
            subject.append(self.getWord())
        return ' '.join(subject).capitalize()

    def getSentence(self):
        """Return a random sentence."""
        length = random.randrange(5, 20)
        sentence = [self.getWord() for i in range(length)]
        for i in range(random.randrange(0, 3)):
            sentence.insert(random.randrange(length-4)+2, ',')
        sentence = ' '.join(sentence).capitalize() + '.'
        sentence = sentence.replace(' ,', ',')
        sentence = sentence.replace(',,', ',')
        return sentence

    def getParagraph(self, length=4):
        """Return a paragraph"""
        return ' '.join([self.getSentence() for i in range(length)])

    def getMessage(self, length=7):
        """Return a message paragraph length."""
        return '\n'.join([self.getParagraph() for i in range(
            random.randrange(3,length))])


if __name__ == '__main__':
    print 'Word: %s' % (Lipsum().getWord())
    print 'UniqWord: %s' % (Lipsum().getUniqWord())
    print 'Subject: %s' % (Lipsum().getSubject())
    print 'Subject uniq: %s' % (Lipsum().getSubject(uniq=True))
    print
    print 'Sentence: %s' % (Lipsum().getSentence())
    print
    print 'Paragraph: %s' % (Lipsum().getParagraph())
    print
    print 'Message: %s' % (Lipsum().getMessage())
