import random
import string
from model.contact import Contact
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

f = "data/contacts.json"
n = 2

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", last_name="", address="")] + [
    Contact(name=random_string("name", 10), last_name=random_string("lastname", 20),
            address=random_string("tankovaya", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fl:
    jsonpickle.set_encoder_options("json", indent=2)
    fl.write(jsonpickle.encode(testdata))
