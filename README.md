# AppleCodingTest

##Instructions

Created using python 3.5.1, using PyCharm IDE
Requires standard libraries only.

To run:
siritest.py "I would like some thai food"

This will return the matches to the command line.


##Assumptions

Using Siri in IOS 9.3.1 as the primary oracle when determining certain behaviours, the following assumptions have been made:
- words are case insensitive
- accented characters are treated the same as their non-accented equivalent

Other assumptions
- a concept can be any number of words
- the language being used is a left-to-right language.



##Architecture
There are 3 main modules: interpreter, concepts and trie.

Trie is an imported module written by B.F. Dimmick (https://github.com/bdimmick/python-trie)

Concepts performs the processing of words against the trie, and contains the basic test dataset.

Interpreter takes the sentence and iterates over it, calling methods from concepts.


##Tests
There are several tests the Test folder that further exercise the code.

There are tests against each of the modules.

- test_interpreter contains many test cases ranging from the provided examples, to repeated words and additional whitespace.
- test_concepts contains a few tests that make sure the key functionality of first letter matching and word matching are checked.
- test_trie are tests provided by the author of the trie module.

The tests were mostly developed first and continuously run through the Pycharm test runner on every save.

The tests can also be run from the command line.


##Larger data set
The default data set is the sample list as provided in the task documentation.

There is a larger data set that can be used by uncommenting line 21 in concepts.py. This has over 100,000 words.



##Performance

Using native Python trie code is not efficient and when using the larger word dataset. Options available are using a C++ trie module which can be 30-100x faster according to the documentation.

The implemented method for reading and storing the dataset is far from optimal, and accounts of the majority of the time spent during an operation. Options for this would be a caching mechanism and storing in a more suitable data store.

For example:

- reading and storing data set (532,738 words) - ~11secs
- performing a search - ~0.0005secs

With some further thought, the algorithm for traversing the sentence could be made more efficient.

Performance testing, and profiling would be performed to identify potential bottlenecks and areas of improvement in the system.

##Issues

- Apostrophes (ie Italian's) will currently be removed, leaving Italians, but this will not match unless Italians is present in the dataset.
