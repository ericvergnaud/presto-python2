# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .EParserListener import EParserListener
else:
    from EParserListener import EParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u0097\u081e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\4")
        buf.write(u"8\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@")
        buf.write(u"\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\t")
        buf.write(u"I\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R")
        buf.write(u"\tR\4S\tS\4T\tT\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4")
        buf.write(u"[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\t")
        buf.write(u"c\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l")
        buf.write(u"\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4")
        buf.write(u"u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}")
        buf.write(u"\4~\t~\4\177\t\177\4\u0080\t\u0080\4\u0081\t\u0081\4")
        buf.write(u"\u0082\t\u0082\4\u0083\t\u0083\4\u0084\t\u0084\4\u0085")
        buf.write(u"\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087\4\u0088\t\u0088")
        buf.write(u"\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b\t\u008b\4\u008c")
        buf.write(u"\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e\4\u008f\t\u008f")
        buf.write(u"\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092\t\u0092\4\u0093")
        buf.write(u"\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095\4\u0096\t\u0096")
        buf.write(u"\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099\t\u0099\4\u009a")
        buf.write(u"\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c\4\u009d\t\u009d")
        buf.write(u"\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0\t\u00a0\4\u00a1")
        buf.write(u"\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3\4\u00a4\t\u00a4")
        buf.write(u"\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7\t\u00a7\4\u00a8")
        buf.write(u"\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa\4\u00ab\t\u00ab")
        buf.write(u"\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae\t\u00ae\4\u00af")
        buf.write(u"\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1\4\u00b2\t\u00b2")
        buf.write(u"\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5\t\u00b5\4\u00b6")
        buf.write(u"\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8\4\u00b9\t\u00b9")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u017a\n\2\3\2\3\2\3")
        buf.write(u"\2\5\2\u017f\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u019f\n\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\5\6\u01a8\n\6\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\5\7\u01b0\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\3\7\5\7\u01bb\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write(u"\u01c4\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\5\b\u01d4\n\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\5\b\u01dd\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u01e4\n\t")
        buf.write(u"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u01ee\n\n\3\n\3")
        buf.write(u"\n\3\n\5\n\u01f3\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0206")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\5\17\u0239\n\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0251")
        buf.write(u"\n\21\f\21\16\21\u0254\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\5\22\u0260\n\22\5\22\u0262")
        buf.write(u"\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5")
        buf.write(u"\23\u026d\n\23\3\23\3\23\3\23\5\23\u0272\n\23\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u027c\n\24\3\24")
        buf.write(u"\3\24\3\24\5\24\u0281\n\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write(u"\u0292\n\25\3\25\3\25\3\25\5\25\u0297\n\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u02a2\n\26\3")
        buf.write(u"\27\3\27\3\27\5\27\u02a7\n\27\3\27\3\27\5\27\u02ab\n")
        buf.write(u"\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\5\30\u02bc\n\30\3\31\3\31\5")
        buf.write(u"\31\u02c0\n\31\3\31\5\31\u02c3\n\31\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u02e4\n\34\3\34")
        buf.write(u"\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\35\5\35\u02f7\n\35\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\5\36\u02fe\n\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write(u"!\5!\u0320\n!\3!\3!\3!\3!\3!\3!\3!\5!\u0329\n!\3\"\3")
        buf.write(u"\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\3\"\3\"\7\"\u033e\n\"\f\"\16\"\u0341\13\"")
        buf.write(u"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0350\n$\3")
        buf.write(u"$\3$\3$\5$\u0355\n$\3$\3$\3$\3$\3$\3$\5$\u035d\n$\3$")
        buf.write(u"\3$\3$\3$\3$\3$\3$\5$\u0366\n$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u037d\n%")
        buf.write(u"\3&\3&\5&\u0381\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\5\'\u039d\n\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u03fd")
        buf.write(u"\n\'\f\'\16\'\u0400\13\'\3(\3(\3(\3(\3(\7(\u0407\n(\f")
        buf.write(u"(\16(\u040a\13(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3,\3")
        buf.write(u",\3,\3,\3,\7,\u041c\n,\f,\16,\u041f\13,\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u042e\n-\3.\3.\3/\3/\3/")
        buf.write(u"\3/\5/\u0436\n/\3/\3/\3/\5/\u043b\n/\5/\u043d\n/\3/\3")
        buf.write(u"/\3/\3/\5/\u0443\n/\5/\u0445\n/\5/\u0447\n/\3\60\3\60")
        buf.write(u"\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write(u"\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write(u"\3\64\3\64\3\64\3\64\3\64\5\64\u0465\n\64\3\65\3\65\3")
        buf.write(u"\65\3\65\3\65\5\65\u046c\n\65\5\65\u046e\n\65\3\65\3")
        buf.write(u"\65\3\65\5\65\u0473\n\65\5\65\u0475\n\65\3\66\3\66\3")
        buf.write(u"\66\3\66\3\66\3\66\3\66\7\66\u047e\n\66\f\66\16\66\u0481")
        buf.write(u"\13\66\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39\3")
        buf.write(u"9\39\39\39\59\u0493\n9\3:\3:\3:\3:\3;\7;\u049a\n;\f;")
        buf.write(u"\16;\u049d\13;\3<\6<\u04a0\n<\r<\16<\u04a1\3=\6=\u04a5")
        buf.write(u"\n=\r=\16=\u04a6\3=\3=\3>\7>\u04ac\n>\f>\16>\u04af\13")
        buf.write(u">\3>\3>\3?\3?\3@\5@\u04b6\n@\3@\3@\3@\3A\3A\3A\3A\3A")
        buf.write(u"\3A\3A\7A\u04c2\nA\fA\16A\u04c5\13A\3B\3B\3B\3B\3B\5")
        buf.write(u"B\u04cc\nB\3C\3C\3D\3D\5D\u04d2\nD\3E\3E\3E\3E\3E\3E")
        buf.write(u"\3E\7E\u04db\nE\fE\16E\u04de\13E\3F\3F\3F\3F\3F\3F\3")
        buf.write(u"F\7F\u04e7\nF\fF\16F\u04ea\13F\3G\3G\3G\3G\3G\3G\7G\u04f2")
        buf.write(u"\nG\fG\16G\u04f5\13G\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5")
        buf.write(u"H\u0501\nH\3I\3I\5I\u0505\nI\3I\3I\3J\3J\5J\u050b\nJ")
        buf.write(u"\3J\3J\3K\3K\3K\3K\3K\3K\7K\u0515\nK\fK\16K\u0518\13")
        buf.write(u"K\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M")
        buf.write(u"\7M\u052b\nM\fM\16M\u052e\13M\3N\3N\5N\u0532\nN\3O\3")
        buf.write(u"O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u053e\nO\3P\3P\3Q\3Q\3R")
        buf.write(u"\3R\3S\3S\3S\5S\u0549\nS\3T\3T\3T\3T\3T\3T\7T\u0551\n")
        buf.write(u"T\fT\16T\u0554\13T\3U\3U\5U\u0558\nU\3V\3V\3V\5V\u055d")
        buf.write(u"\nV\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\7Z\u056b\nZ\f")
        buf.write(u"Z\16Z\u056e\13Z\3[\3[\5[\u0572\n[\3\\\3\\\5\\\u0576\n")
        buf.write(u"\\\3]\3]\3]\5]\u057b\n]\3^\3^\3^\3_\3_\5_\u0582\n_\3")
        buf.write(u"`\3`\3`\3`\3`\3`\3`\3`\3`\7`\u058d\n`\f`\16`\u0590\13")
        buf.write(u"`\3a\3a\3a\3a\3a\3a\3a\7a\u0599\na\fa\16a\u059c\13a\3")
        buf.write(u"b\3b\3b\3b\5b\u05a2\nb\3c\3c\3c\3c\3c\3c\3c\3c\3c\3c")
        buf.write(u"\5c\u05ae\nc\3d\3d\5d\u05b2\nd\3e\3e\3e\3e\3e\3e\7e\u05ba")
        buf.write(u"\ne\fe\16e\u05bd\13e\3f\3f\3f\3g\3g\5g\u05c4\ng\3h\3")
        buf.write(u"h\3h\3h\5h\u05ca\nh\3h\3h\3h\7h\u05cf\nh\fh\16h\u05d2")
        buf.write(u"\13h\3h\3h\5h\u05d6\nh\3i\3i\3i\3i\3i\3i\7i\u05de\ni")
        buf.write(u"\fi\16i\u05e1\13i\3j\3j\3j\5j\u05e6\nj\3k\3k\3k\3k\3")
        buf.write(u"k\3k\3k\7k\u05ef\nk\fk\16k\u05f2\13k\3l\3l\3l\3l\3l\3")
        buf.write(u"l\3l\3l\3l\3l\5l\u05fe\nl\3m\3m\5m\u0602\nm\3m\5m\u0605")
        buf.write(u"\nm\3n\3n\5n\u0609\nn\3n\5n\u060c\nn\3o\3o\3o\3o\3o\3")
        buf.write(u"o\3o\7o\u0615\no\fo\16o\u0618\13o\3p\3p\3p\3p\3p\3p\3")
        buf.write(u"p\7p\u0621\np\fp\16p\u0624\13p\3q\3q\3q\3q\3q\3q\3q\7")
        buf.write(u"q\u062d\nq\fq\16q\u0630\13q\3r\3r\3r\3r\3r\3r\3r\3r\3")
        buf.write(u"r\3r\3r\3r\3r\3r\5r\u0640\nr\3s\3s\3s\3s\3s\3s\3s\3s")
        buf.write(u"\3s\3s\3s\3s\3s\5s\u064f\ns\3t\3t\3t\3t\3t\3t\7t\u0657")
        buf.write(u"\nt\ft\16t\u065a\13t\3u\3u\3u\3u\5u\u0660\nu\3v\3v\3")
        buf.write(u"w\3w\3w\3w\3x\3x\5x\u066a\nx\3y\3y\3y\3y\3y\5y\u0671")
        buf.write(u"\ny\3z\3z\5z\u0675\nz\3z\3z\3{\3{\5{\u067b\n{\3{\3{\3")
        buf.write(u"|\3|\3|\3|\3|\3|\7|\u0685\n|\f|\16|\u0688\13|\3}\3}\3")
        buf.write(u"}\3}\3}\3}\7}\u0690\n}\f}\16}\u0693\13}\3~\3~\3~\3~\3")
        buf.write(u"\177\3\177\3\177\3\177\3\177\3\177\3\177\3\177\3\177")
        buf.write(u"\5\177\u06a2\n\177\3\u0080\3\u0080\3\u0080\3\u0080\3")
        buf.write(u"\u0081\3\u0081\3\u0081\3\u0081\3\u0081\7\u0081\u06ad")
        buf.write(u"\n\u0081\f\u0081\16\u0081\u06b0\13\u0081\3\u0082\3\u0082")
        buf.write(u"\3\u0082\3\u0082\5\u0082\u06b6\n\u0082\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083\u06be\n\u0083")
        buf.write(u"\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085\3\u0085\3\u0086")
        buf.write(u"\3\u0086\3\u0086\3\u0087\3\u0087\3\u0088\3\u0088\3\u0089")
        buf.write(u"\3\u0089\3\u008a\3\u008a\3\u008b\3\u008b\3\u008c\3\u008c")
        buf.write(u"\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\5\u008c\u06da")
        buf.write(u"\n\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\7\u008d")
        buf.write(u"\u06e1\n\u008d\f\u008d\16\u008d\u06e4\13\u008d\3\u008e")
        buf.write(u"\3\u008e\3\u008e\5\u008e\u06e9\n\u008e\3\u008f\3\u008f")
        buf.write(u"\3\u008f\5\u008f\u06ee\n\u008f\3\u0090\3\u0090\3\u0090")
        buf.write(u"\5\u0090\u06f3\n\u0090\3\u0090\3\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0091\3\u0091\7\u0091\u06fd\n\u0091")
        buf.write(u"\f\u0091\16\u0091\u0700\13\u0091\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\3\u0093\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094")
        buf.write(u"\3\u0094\3\u0094\3\u0094\3\u0094\7\u0094\u0710\n\u0094")
        buf.write(u"\f\u0094\16\u0094\u0713\13\u0094\3\u0095\3\u0095\3\u0095")
        buf.write(u"\3\u0095\3\u0095\5\u0095\u071a\n\u0095\3\u0096\3\u0096")
        buf.write(u"\3\u0097\3\u0097\3\u0097\5\u0097\u0721\n\u0097\3\u0098")
        buf.write(u"\3\u0098\3\u0098\3\u0098\3\u0098\7\u0098\u0728\n\u0098")
        buf.write(u"\f\u0098\16\u0098\u072b\13\u0098\3\u0099\3\u0099\3\u0099")
        buf.write(u"\3\u0099\5\u0099\u0731\n\u0099\3\u009a\3\u009a\3\u009a")
        buf.write(u"\3\u009a\3\u009a\3\u009a\5\u009a\u0739\n\u009a\3\u009b")
        buf.write(u"\3\u009b\3\u009b\5\u009b\u073e\n\u009b\3\u009b\3\u009b")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\5\u009c")
        buf.write(u"\u0748\n\u009c\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d")
        buf.write(u"\3\u009d\7\u009d\u0750\n\u009d\f\u009d\16\u009d\u0753")
        buf.write(u"\13\u009d\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\7\u009e\u0760")
        buf.write(u"\n\u009e\f\u009e\16\u009e\u0763\13\u009e\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\7\u00a0\u076f\n\u00a0\f\u00a0\16\u00a0\u0772")
        buf.write(u"\13\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\5\u00a1")
        buf.write(u"\u0779\n\u00a1\3\u00a2\3\u00a2\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\5\u00a3\u0784\n\u00a3")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4\7\u00a4\u078b")
        buf.write(u"\n\u00a4\f\u00a4\16\u00a4\u078e\13\u00a4\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\5\u00a5\u0793\n\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\5\u00a6\u0798\n\u00a6\3\u00a7\3\u00a7\3\u00a7\5\u00a7")
        buf.write(u"\u079d\n\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\7\u00a8\u07a7\n\u00a8\f\u00a8")
        buf.write(u"\16\u00a8\u07aa\13\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\7\u00ab\u07ba\n\u00ab\f\u00ab")
        buf.write(u"\16\u00ab\u07bd\13\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\7\u00ac\u07c5\n\u00ac\f\u00ac\16\u00ac")
        buf.write(u"\u07c8\13\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write(u"\5\u00ad\u07cf\n\u00ad\3\u00ae\3\u00ae\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\5\u00af\u07da")
        buf.write(u"\n\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\7\u00b0")
        buf.write(u"\u07e1\n\u00b0\f\u00b0\16\u00b0\u07e4\13\u00b0\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\5\u00b1\u07e9\n\u00b1\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\5\u00b2\u07ee\n\u00b2\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\5\u00b3\u07f3\n\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\3\u00b4\7\u00b4\u07fd\n\u00b4")
        buf.write(u"\f\u00b4\16\u00b4\u0800\13\u00b4\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\3\u00b7\7\u00b7\u0810\n\u00b7")
        buf.write(u"\f\u00b7\16\u00b7\u0813\13\u00b7\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\5\u00b8\u081a\n\u00b8\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\2) BLNVj\u0080\u0088\u008a\u008c\u0094\u0098")
        buf.write(u"\u00a6\u00b2\u00be\u00c0\u00d0\u00d4\u00dc\u00de\u00e0")
        buf.write(u"\u00e6\u00f6\u00f8\u0100\u0118\u0120\u0126\u012e\u0138")
        buf.write(u"\u013a\u013e\u0146\u014e\u0154\u0156\u015e\u0166\u016c")
        buf.write(u"\u00ba\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(u",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write(u"\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write(u"\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write(u"\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6")
        buf.write(u"\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8")
        buf.write(u"\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da")
        buf.write(u"\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec")
        buf.write(u"\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe")
        buf.write(u"\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110")
        buf.write(u"\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122")
        buf.write(u"\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134")
        buf.write(u"\u0136\u0138\u013a\u013c\u013e\u0140\u0142\u0144\u0146")
        buf.write(u"\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158")
        buf.write(u"\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a")
        buf.write(u"\u016c\u016e\u0170\2\7\3\2\"#\4\2zz\177\177\4\2\'\'h")
        buf.write(u"h\6\2\64<uu\u0087\u0087\u008c\u008e\4\2\64<\u008c\u008e")
        buf.write(u"\u087b\2\u0172\3\2\2\2\4\u0187\3\2\2\2\6\u0194\3\2\2")
        buf.write(u"\2\b\u019a\3\2\2\2\n\u01a0\3\2\2\2\f\u01a9\3\2\2\2\16")
        buf.write(u"\u01c5\3\2\2\2\20\u01e3\3\2\2\2\22\u01e5\3\2\2\2\24\u01fa")
        buf.write(u"\3\2\2\2\26\u020d\3\2\2\2\30\u0216\3\2\2\2\32\u021f\3")
        buf.write(u"\2\2\2\34\u022e\3\2\2\2\36\u0240\3\2\2\2 \u0249\3\2\2")
        buf.write(u"\2\"\u0261\3\2\2\2$\u0263\3\2\2\2&\u0273\3\2\2\2(\u0288")
        buf.write(u"\3\2\2\2*\u029e\3\2\2\2,\u02a3\3\2\2\2.\u02bb\3\2\2\2")
        buf.write(u"\60\u02c2\3\2\2\2\62\u02c4\3\2\2\2\64\u02cd\3\2\2\2\66")
        buf.write(u"\u02d6\3\2\2\28\u02f6\3\2\2\2:\u02f8\3\2\2\2<\u0306\3")
        buf.write(u"\2\2\2>\u030f\3\2\2\2@\u0316\3\2\2\2B\u032a\3\2\2\2D")
        buf.write(u"\u0342\3\2\2\2F\u0345\3\2\2\2H\u037c\3\2\2\2J\u037e\3")
        buf.write(u"\2\2\2L\u039c\3\2\2\2N\u0401\3\2\2\2P\u040b\3\2\2\2R")
        buf.write(u"\u040f\3\2\2\2T\u0414\3\2\2\2V\u0416\3\2\2\2X\u042d\3")
        buf.write(u"\2\2\2Z\u042f\3\2\2\2\\\u0446\3\2\2\2^\u0448\3\2\2\2")
        buf.write(u"`\u044c\3\2\2\2b\u0451\3\2\2\2d\u0455\3\2\2\2f\u045d")
        buf.write(u"\3\2\2\2h\u0474\3\2\2\2j\u0476\3\2\2\2l\u0482\3\2\2\2")
        buf.write(u"n\u0486\3\2\2\2p\u0492\3\2\2\2r\u0494\3\2\2\2t\u049b")
        buf.write(u"\3\2\2\2v\u049f\3\2\2\2x\u04a4\3\2\2\2z\u04ad\3\2\2\2")
        buf.write(u"|\u04b2\3\2\2\2~\u04b5\3\2\2\2\u0080\u04ba\3\2\2\2\u0082")
        buf.write(u"\u04cb\3\2\2\2\u0084\u04cd\3\2\2\2\u0086\u04d1\3\2\2")
        buf.write(u"\2\u0088\u04d3\3\2\2\2\u008a\u04df\3\2\2\2\u008c\u04eb")
        buf.write(u"\3\2\2\2\u008e\u0500\3\2\2\2\u0090\u0502\3\2\2\2\u0092")
        buf.write(u"\u0508\3\2\2\2\u0094\u050e\3\2\2\2\u0096\u0519\3\2\2")
        buf.write(u"\2\u0098\u051f\3\2\2\2\u009a\u0531\3\2\2\2\u009c\u053d")
        buf.write(u"\3\2\2\2\u009e\u053f\3\2\2\2\u00a0\u0541\3\2\2\2\u00a2")
        buf.write(u"\u0543\3\2\2\2\u00a4\u0548\3\2\2\2\u00a6\u054a\3\2\2")
        buf.write(u"\2\u00a8\u0557\3\2\2\2\u00aa\u055c\3\2\2\2\u00ac\u055e")
        buf.write(u"\3\2\2\2\u00ae\u0560\3\2\2\2\u00b0\u0562\3\2\2\2\u00b2")
        buf.write(u"\u0564\3\2\2\2\u00b4\u0571\3\2\2\2\u00b6\u0575\3\2\2")
        buf.write(u"\2\u00b8\u0577\3\2\2\2\u00ba\u057c\3\2\2\2\u00bc\u0581")
        buf.write(u"\3\2\2\2\u00be\u0583\3\2\2\2\u00c0\u0591\3\2\2\2\u00c2")
        buf.write(u"\u05a1\3\2\2\2\u00c4\u05ad\3\2\2\2\u00c6\u05af\3\2\2")
        buf.write(u"\2\u00c8\u05b3\3\2\2\2\u00ca\u05be\3\2\2\2\u00cc\u05c1")
        buf.write(u"\3\2\2\2\u00ce\u05c5\3\2\2\2\u00d0\u05d7\3\2\2\2\u00d2")
        buf.write(u"\u05e5\3\2\2\2\u00d4\u05e7\3\2\2\2\u00d6\u05fd\3\2\2")
        buf.write(u"\2\u00d8\u05ff\3\2\2\2\u00da\u0606\3\2\2\2\u00dc\u060d")
        buf.write(u"\3\2\2\2\u00de\u0619\3\2\2\2\u00e0\u0625\3\2\2\2\u00e2")
        buf.write(u"\u063f\3\2\2\2\u00e4\u064e\3\2\2\2\u00e6\u0650\3\2\2")
        buf.write(u"\2\u00e8\u065f\3\2\2\2\u00ea\u0661\3\2\2\2\u00ec\u0663")
        buf.write(u"\3\2\2\2\u00ee\u0669\3\2\2\2\u00f0\u0670\3\2\2\2\u00f2")
        buf.write(u"\u0672\3\2\2\2\u00f4\u0678\3\2\2\2\u00f6\u067e\3\2\2")
        buf.write(u"\2\u00f8\u0689\3\2\2\2\u00fa\u0694\3\2\2\2\u00fc\u06a1")
        buf.write(u"\3\2\2\2\u00fe\u06a3\3\2\2\2\u0100\u06a7\3\2\2\2\u0102")
        buf.write(u"\u06b5\3\2\2\2\u0104\u06bd\3\2\2\2\u0106\u06bf\3\2\2")
        buf.write(u"\2\u0108\u06c2\3\2\2\2\u010a\u06c5\3\2\2\2\u010c\u06c8")
        buf.write(u"\3\2\2\2\u010e\u06ca\3\2\2\2\u0110\u06cc\3\2\2\2\u0112")
        buf.write(u"\u06ce\3\2\2\2\u0114\u06d0\3\2\2\2\u0116\u06d9\3\2\2")
        buf.write(u"\2\u0118\u06db\3\2\2\2\u011a\u06e8\3\2\2\2\u011c\u06ed")
        buf.write(u"\3\2\2\2\u011e\u06ef\3\2\2\2\u0120\u06f6\3\2\2\2\u0122")
        buf.write(u"\u0701\3\2\2\2\u0124\u0705\3\2\2\2\u0126\u0709\3\2\2")
        buf.write(u"\2\u0128\u0719\3\2\2\2\u012a\u071b\3\2\2\2\u012c\u0720")
        buf.write(u"\3\2\2\2\u012e\u0722\3\2\2\2\u0130\u0730\3\2\2\2\u0132")
        buf.write(u"\u0738\3\2\2\2\u0134\u073a\3\2\2\2\u0136\u0747\3\2\2")
        buf.write(u"\2\u0138\u0749\3\2\2\2\u013a\u0754\3\2\2\2\u013c\u0764")
        buf.write(u"\3\2\2\2\u013e\u0768\3\2\2\2\u0140\u0778\3\2\2\2\u0142")
        buf.write(u"\u077a\3\2\2\2\u0144\u0783\3\2\2\2\u0146\u0785\3\2\2")
        buf.write(u"\2\u0148\u0792\3\2\2\2\u014a\u0797\3\2\2\2\u014c\u0799")
        buf.write(u"\3\2\2\2\u014e\u07a0\3\2\2\2\u0150\u07ab\3\2\2\2\u0152")
        buf.write(u"\u07af\3\2\2\2\u0154\u07b3\3\2\2\2\u0156\u07be\3\2\2")
        buf.write(u"\2\u0158\u07ce\3\2\2\2\u015a\u07d0\3\2\2\2\u015c\u07d9")
        buf.write(u"\3\2\2\2\u015e\u07db\3\2\2\2\u0160\u07e8\3\2\2\2\u0162")
        buf.write(u"\u07ed\3\2\2\2\u0164\u07ef\3\2\2\2\u0166\u07f6\3\2\2")
        buf.write(u"\2\u0168\u0801\3\2\2\2\u016a\u0805\3\2\2\2\u016c\u0809")
        buf.write(u"\3\2\2\2\u016e\u0819\3\2\2\2\u0170\u081b\3\2\2\2\u0172")
        buf.write(u"\u0173\7Q\2\2\u0173\u0174\5\u00aeX\2\u0174\u0175\7E\2")
        buf.write(u"\2\u0175\u0176\7\20\2\2\u0176\u0179\7W\2\2\u0177\u017a")
        buf.write(u"\7K\2\2\u0178\u017a\5\u00aeX\2\u0179\u0177\3\2\2\2\u0179")
        buf.write(u"\u0178\3\2\2\2\u017a\u017e\3\2\2\2\u017b\u017c\5\"\22")
        buf.write(u"\2\u017c\u017d\7\22\2\2\u017d\u017f\3\2\2\2\u017e\u017b")
        buf.write(u"\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write(u"\u0181\7\u0083\2\2\u0181\u0182\5\u010a\u0086\2\u0182")
        buf.write(u"\u0183\7\20\2\2\u0183\u0184\5x=\2\u0184\u0185\5\u008a")
        buf.write(u"F\2\u0185\u0186\5z>\2\u0186\3\3\2\2\2\u0187\u0188\7Q")
        buf.write(u"\2\2\u0188\u0189\5\u00aeX\2\u0189\u018a\7E\2\2\u018a")
        buf.write(u"\u018b\7\20\2\2\u018b\u018c\7W\2\2\u018c\u018d\5\u009c")
        buf.write(u"O\2\u018d\u018e\7\u0083\2\2\u018e\u018f\5\u010a\u0086")
        buf.write(u"\2\u018f\u0190\7\20\2\2\u0190\u0191\5x=\2\u0191\u0192")
        buf.write(u"\5\u0088E\2\u0192\u0193\5z>\2\u0193\5\3\2\2\2\u0194\u0195")
        buf.write(u"\5\u00b0Y\2\u0195\u0196\7\u0083\2\2\u0196\u0197\5L\'")
        buf.write(u"\2\u0197\u0198\7E\2\2\u0198\u0199\5\u0108\u0085\2\u0199")
        buf.write(u"\7\3\2\2\2\u019a\u019b\5\u00b0Y\2\u019b\u019e\5j\66\2")
        buf.write(u"\u019c\u019d\7C\2\2\u019d\u019f\5l\67\2\u019e\u019c\3")
        buf.write(u"\2\2\2\u019e\u019f\3\2\2\2\u019f\t\3\2\2\2\u01a0\u01a1")
        buf.write(u"\7Q\2\2\u01a1\u01a2\5\u00acW\2\u01a2\u01a3\7E\2\2\u01a3")
        buf.write(u"\u01a4\7\20\2\2\u01a4\u01a5\5\u0098M\2\u01a5\u01a7\7")
        buf.write(u"G\2\2\u01a6\u01a8\5\u008eH\2\u01a7\u01a6\3\2\2\2\u01a7")
        buf.write(u"\u01a8\3\2\2\2\u01a8\13\3\2\2\2\u01a9\u01aa\7Q\2\2\u01aa")
        buf.write(u"\u01ab\5\u00aeX\2\u01ab\u01ac\7E\2\2\u01ac\u01af\7\20")
        buf.write(u"\2\2\u01ad\u01b0\7K\2\2\u01ae\u01b0\5\20\t\2\u01af\u01ad")
        buf.write(u"\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01c3\3\2\2\2\u01b1")
        buf.write(u"\u01ba\5\"\22\2\u01b2\u01b3\7\22\2\2\u01b3\u01b4\7C\2")
        buf.write(u"\2\u01b4\u01b5\7g\2\2\u01b5\u01b6\7\20\2\2\u01b6\u01b7")
        buf.write(u"\5x=\2\u01b7\u01b8\5\u00c0a\2\u01b8\u01b9\5z>\2\u01b9")
        buf.write(u"\u01bb\3\2\2\2\u01ba\u01b2\3\2\2\2\u01ba\u01bb\3\2\2")
        buf.write(u"\2\u01bb\u01c4\3\2\2\2\u01bc\u01bd\7\u0083\2\2\u01bd")
        buf.write(u"\u01be\7g\2\2\u01be\u01bf\7\20\2\2\u01bf\u01c0\5x=\2")
        buf.write(u"\u01c0\u01c1\5\u00c0a\2\u01c1\u01c2\5z>\2\u01c2\u01c4")
        buf.write(u"\3\2\2\2\u01c3\u01b1\3\2\2\2\u01c3\u01bc\3\2\2\2\u01c3")
        buf.write(u"\u01c4\3\2\2\2\u01c4\r\3\2\2\2\u01c5\u01c6\7Q\2\2\u01c6")
        buf.write(u"\u01c7\5\u00aeX\2\u01c7\u01c8\7E\2\2\u01c8\u01c9\7\20")
        buf.write(u"\2\2\u01c9\u01dc\7|\2\2\u01ca\u01d3\5\"\22\2\u01cb\u01cc")
        buf.write(u"\7\22\2\2\u01cc\u01cd\7C\2\2\u01cd\u01ce\7g\2\2\u01ce")
        buf.write(u"\u01cf\7\20\2\2\u01cf\u01d0\5x=\2\u01d0\u01d1\5\u00c0")
        buf.write(u"a\2\u01d1\u01d2\5z>\2\u01d2\u01d4\3\2\2\2\u01d3\u01cb")
        buf.write(u"\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01dd\3\2\2\2\u01d5")
        buf.write(u"\u01d6\7\u0083\2\2\u01d6\u01d7\7g\2\2\u01d7\u01d8\7\20")
        buf.write(u"\2\2\u01d8\u01d9\5x=\2\u01d9\u01da\5\u00c0a\2\u01da\u01db")
        buf.write(u"\5z>\2\u01db\u01dd\3\2\2\2\u01dc\u01ca\3\2\2\2\u01dc")
        buf.write(u"\u01d5\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\17\3\2\2\2\u01de")
        buf.write(u"\u01e4\5\u00a6T\2\u01df\u01e0\5\u00a6T\2\u01e0\u01e1")
        buf.write(u"\7C\2\2\u01e1\u01e2\5\u00aeX\2\u01e2\u01e4\3\2\2\2\u01e3")
        buf.write(u"\u01de\3\2\2\2\u01e3\u01df\3\2\2\2\u01e4\21\3\2\2\2\u01e5")
        buf.write(u"\u01e6\7Q\2\2\u01e6\u01e7\5\u00a8U\2\u01e7\u01e8\7E\2")
        buf.write(u"\2\u01e8\u01e9\7\20\2\2\u01e9\u01ed\7f\2\2\u01ea\u01eb")
        buf.write(u"\7v\2\2\u01eb\u01ec\7\20\2\2\u01ec\u01ee\5*\26\2\u01ed")
        buf.write(u"\u01ea\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f2\3\2\2")
        buf.write(u"\2\u01ef\u01f0\7y\2\2\u01f0\u01f1\7\20\2\2\u01f1\u01f3")
        buf.write(u"\5\u0098M\2\u01f2\u01ef\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write(u"\u01f4\3\2\2\2\u01f4\u01f5\7S\2\2\u01f5\u01f6\7\20\2")
        buf.write(u"\2\u01f6\u01f7\5x=\2\u01f7\u01f8\5\u00dco\2\u01f8\u01f9")
        buf.write(u"\5z>\2\u01f9\23\3\2\2\2\u01fa\u01fb\7Q\2\2\u01fb\u01fc")
        buf.write(u"\5\u0104\u0083\2\u01fc\u01fd\7E\2\2\u01fd\u01fe\7\20")
        buf.write(u"\2\2\u01fe\u01ff\7p\2\2\u01ff\u0200\7v\2\2\u0200\u0201")
        buf.write(u"\7\20\2\2\u0201\u0205\5\u00b6\\\2\u0202\u0203\7y\2\2")
        buf.write(u"\u0203\u0204\7\20\2\2\u0204\u0206\5\u0098M\2\u0205\u0202")
        buf.write(u"\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write(u"\u0208\7S\2\2\u0208\u0209\7\20\2\2\u0209\u020a\5x=\2")
        buf.write(u"\u020a\u020b\5\u00dco\2\u020b\u020c\5z>\2\u020c\25\3")
        buf.write(u"\2\2\2\u020d\u020e\7Q\2\2\u020e\u020f\5\u00acW\2\u020f")
        buf.write(u"\u0210\7{\2\2\u0210\u0211\7S\2\2\u0211\u0212\7\20\2\2")
        buf.write(u"\u0212\u0213\5x=\2\u0213\u0214\5\u00dco\2\u0214\u0215")
        buf.write(u"\5z>\2\u0215\27\3\2\2\2\u0216\u0217\7Q\2\2\u0217\u0218")
        buf.write(u"\5\u00acW\2\u0218\u0219\7_\2\2\u0219\u021a\7S\2\2\u021a")
        buf.write(u"\u021b\7\20\2\2\u021b\u021c\5x=\2\u021c\u021d\5\u00dc")
        buf.write(u"o\2\u021d\u021e\5z>\2\u021e\31\3\2\2\2\u021f\u0220\7")
        buf.write(u"Q\2\2\u0220\u0221\5\u00aeX\2\u0221\u0222\7E\2\2\u0222")
        buf.write(u"\u0223\7\20\2\2\u0223\u0224\7i\2\2\u0224\u0225\7K\2\2")
        buf.write(u"\u0225\u0226\5\"\22\2\u0226\u0227\7\22\2\2\u0227\u0228")
        buf.write(u"\7C\2\2\u0228\u0229\7d\2\2\u0229\u022a\7\20\2\2\u022a")
        buf.write(u"\u022b\5x=\2\u022b\u022c\5\36\20\2\u022c\u022d\5z>\2")
        buf.write(u"\u022d\33\3\2\2\2\u022e\u022f\7Q\2\2\u022f\u0230\5\u00ae")
        buf.write(u"X\2\u0230\u0231\7E\2\2\u0231\u0232\7\20\2\2\u0232\u0233")
        buf.write(u"\7i\2\2\u0233\u0238\7w\2\2\u0234\u0235\5\"\22\2\u0235")
        buf.write(u"\u0236\7\22\2\2\u0236\u0237\7C\2\2\u0237\u0239\3\2\2")
        buf.write(u"\2\u0238\u0234\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a")
        buf.write(u"\3\2\2\2\u023a\u023b\7d\2\2\u023b\u023c\7\20\2\2\u023c")
        buf.write(u"\u023d\5x=\2\u023d\u023e\5\36\20\2\u023e\u023f\5z>\2")
        buf.write(u"\u023f\35\3\2\2\2\u0240\u0241\7Q\2\2\u0241\u0242\7K\2")
        buf.write(u"\2\u0242\u0243\7d\2\2\u0243\u0244\7E\2\2\u0244\u0245")
        buf.write(u"\7\20\2\2\u0245\u0246\5x=\2\u0246\u0247\5 \21\2\u0247")
        buf.write(u"\u0248\5z>\2\u0248\37\3\2\2\2\u0249\u024a\b\21\1\2\u024a")
        buf.write(u"\u024b\5\u00c4c\2\u024b\u0252\3\2\2\2\u024c\u024d\f\3")
        buf.write(u"\2\2\u024d\u024e\5v<\2\u024e\u024f\5\u00c4c\2\u024f\u0251")
        buf.write(u"\3\2\2\2\u0250\u024c\3\2\2\2\u0251\u0254\3\2\2\2\u0252")
        buf.write(u"\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253!\3\2\2\2\u0254")
        buf.write(u"\u0252\3\2\2\2\u0255\u0256\7\u0083\2\2\u0256\u0257\7")
        buf.write(u"G\2\2\u0257\u0258\7\20\2\2\u0258\u0262\5\u00acW\2\u0259")
        buf.write(u"\u025a\7\u0083\2\2\u025a\u025b\7H\2\2\u025b\u025c\7\20")
        buf.write(u"\2\2\u025c\u025f\5\u00d0i\2\u025d\u025e\7C\2\2\u025e")
        buf.write(u"\u0260\5\u00acW\2\u025f\u025d\3\2\2\2\u025f\u0260\3\2")
        buf.write(u"\2\2\u0260\u0262\3\2\2\2\u0261\u0255\3\2\2\2\u0261\u0259")
        buf.write(u"\3\2\2\2\u0262#\3\2\2\2\u0263\u0264\7Q\2\2\u0264\u0265")
        buf.write(u"\5\u00a8U\2\u0265\u0266\7E\2\2\u0266\u0267\7\20\2\2\u0267")
        buf.write(u"\u0268\7@\2\2\u0268\u026c\7f\2\2\u0269\u026a\7v\2\2\u026a")
        buf.write(u"\u026b\7\20\2\2\u026b\u026d\5*\26\2\u026c\u0269\3\2\2")
        buf.write(u"\2\u026c\u026d\3\2\2\2\u026d\u0271\3\2\2\2\u026e\u026f")
        buf.write(u"\7y\2\2\u026f\u0270\7\20\2\2\u0270\u0272\5\u0098M\2\u0271")
        buf.write(u"\u026e\3\2\2\2\u0271\u0272\3\2\2\2\u0272%\3\2\2\2\u0273")
        buf.write(u"\u0274\7Q\2\2\u0274\u0275\5\u00a8U\2\u0275\u0276\7E\2")
        buf.write(u"\2\u0276\u0277\7\20\2\2\u0277\u027b\7f\2\2\u0278\u0279")
        buf.write(u"\7v\2\2\u0279\u027a\7\20\2\2\u027a\u027c\5*\26\2\u027b")
        buf.write(u"\u0278\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u0280\3\2\2")
        buf.write(u"\2\u027d\u027e\7y\2\2\u027e\u027f\7\20\2\2\u027f\u0281")
        buf.write(u"\5\u0098M\2\u0280\u027d\3\2\2\2\u0280\u0281\3\2\2\2\u0281")
        buf.write(u"\u0282\3\2\2\2\u0282\u0283\7S\2\2\u0283\u0284\7\20\2")
        buf.write(u"\2\u0284\u0285\5x=\2\u0285\u0286\5\u00dco\2\u0286\u0287")
        buf.write(u"\5z>\2\u0287\'\3\2\2\2\u0288\u0289\7Q\2\2\u0289\u028a")
        buf.write(u"\5\u00a8U\2\u028a\u028b\7E\2\2\u028b\u028c\7\20\2\2\u028c")
        buf.write(u"\u028d\7i\2\2\u028d\u0291\7f\2\2\u028e\u028f\7v\2\2\u028f")
        buf.write(u"\u0290\7\20\2\2\u0290\u0292\5*\26\2\u0291\u028e\3\2\2")
        buf.write(u"\2\u0291\u0292\3\2\2\2\u0292\u0296\3\2\2\2\u0293\u0294")
        buf.write(u"\7y\2\2\u0294\u0295\7\20\2\2\u0295\u0297\5\u0098M\2\u0296")
        buf.write(u"\u0293\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0298\3\2\2")
        buf.write(u"\2\u0298\u0299\7S\2\2\u0299\u029a\7\20\2\2\u029a\u029b")
        buf.write(u"\5x=\2\u029b\u029c\5\u00d4k\2\u029c\u029d\5z>\2\u029d")
        buf.write(u")\3\2\2\2\u029e\u02a1\5\u00b2Z\2\u029f\u02a0\7C\2\2\u02a0")
        buf.write(u"\u02a2\5\u00b4[\2\u02a1\u029f\3\2\2\2\u02a1\u02a2\3\2")
        buf.write(u"\2\2\u02a2+\3\2\2\2\u02a3\u02a4\5\u00bc_\2\u02a4\u02a6")
        buf.write(u"\5\u00acW\2\u02a5\u02a7\5\"\22\2\u02a6\u02a5\3\2\2\2")
        buf.write(u"\u02a6\u02a7\3\2\2\2\u02a7\u02aa\3\2\2\2\u02a8\u02a9")
        buf.write(u"\7-\2\2\u02a9\u02ab\5\u00eex\2\u02aa\u02a8\3\2\2\2\u02aa")
        buf.write(u"\u02ab\3\2\2\2\u02ab-\3\2\2\2\u02ac\u02bc\5n8\2\u02ad")
        buf.write(u"\u02bc\5\60\31\2\u02ae\u02bc\5r:\2\u02af\u02bc\5J&\2")
        buf.write(u"\u02b0\u02bc\5@!\2\u02b1\u02bc\5\66\34\2\u02b2\u02bc")
        buf.write(u"\5:\36\2\u02b3\u02bc\5> \2\u02b4\u02bc\5<\37\2\u02b5")
        buf.write(u"\u02bc\5D#\2\u02b6\u02bc\5F$\2\u02b7\u02bc\5`\61\2\u02b8")
        buf.write(u"\u02bc\5\62\32\2\u02b9\u02bc\5\64\33\2\u02ba\u02bc\5")
        buf.write(u"&\24\2\u02bb\u02ac\3\2\2\2\u02bb\u02ad\3\2\2\2\u02bb")
        buf.write(u"\u02ae\3\2\2\2\u02bb\u02af\3\2\2\2\u02bb\u02b0\3\2\2")
        buf.write(u"\2\u02bb\u02b1\3\2\2\2\u02bb\u02b2\3\2\2\2\u02bb\u02b3")
        buf.write(u"\3\2\2\2\u02bb\u02b4\3\2\2\2\u02bb\u02b5\3\2\2\2\u02bb")
        buf.write(u"\u02b6\3\2\2\2\u02bb\u02b7\3\2\2\2\u02bb\u02b8\3\2\2")
        buf.write(u"\2\u02bb\u02b9\3\2\2\2\u02bb\u02ba\3\2\2\2\u02bc/\3\2")
        buf.write(u"\2\2\u02bd\u02bf\5N(\2\u02be\u02c0\5h\65\2\u02bf\u02be")
        buf.write(u"\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02c3\3\2\2\2\u02c1")
        buf.write(u"\u02c3\5R*\2\u02c2\u02bd\3\2\2\2\u02c2\u02c1\3\2\2\2")
        buf.write(u"\u02c3\61\3\2\2\2\u02c4\u02c5\7\u0083\2\2\u02c5\u02c6")
        buf.write(u"\5\u00fe\u0080\2\u02c6\u02c7\7\22\2\2\u02c7\u02c8\7R")
        buf.write(u"\2\2\u02c8\u02c9\7\20\2\2\u02c9\u02ca\5x=\2\u02ca\u02cb")
        buf.write(u"\5\u00dco\2\u02cb\u02cc\5z>\2\u02cc\63\3\2\2\2\u02cd")
        buf.write(u"\u02ce\7\u0083\2\2\u02ce\u02cf\5\u00aeX\2\u02cf\u02d0")
        buf.write(u"\7\22\2\2\u02d0\u02d1\7R\2\2\u02d1\u02d2\7\20\2\2\u02d2")
        buf.write(u"\u02d3\5x=\2\u02d3\u02d4\5\u00dco\2\u02d4\u02d5\5z>\2")
        buf.write(u"\u02d5\65\3\2\2\2\u02d6\u02d7\7~\2\2\u02d7\u02d8\7n\2")
        buf.write(u"\2\u02d8\u02d9\5L\'\2\u02d9\u02da\7\20\2\2\u02da\u02db")
        buf.write(u"\5x=\2\u02db\u02e3\5\u00dep\2\u02dc\u02dd\5v<\2\u02dd")
        buf.write(u"\u02de\7r\2\2\u02de\u02df\7\20\2\2\u02df\u02e0\5x=\2")
        buf.write(u"\u02e0\u02e1\5\u00dco\2\u02e1\u02e2\5z>\2\u02e2\u02e4")
        buf.write(u"\3\2\2\2\u02e3\u02dc\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4")
        buf.write(u"\u02e5\3\2\2\2\u02e5\u02e6\5z>\2\u02e6\67\3\2\2\2\u02e7")
        buf.write(u"\u02e8\7\u0084\2\2\u02e8\u02e9\5\u00e4s\2\u02e9\u02ea")
        buf.write(u"\7\20\2\2\u02ea\u02eb\5x=\2\u02eb\u02ec\5\u00dco\2\u02ec")
        buf.write(u"\u02ed\5z>\2\u02ed\u02f7\3\2\2\2\u02ee\u02ef\7\u0084")
        buf.write(u"\2\2\u02ef\u02f0\7a\2\2\u02f0\u02f1\5\u00e2r\2\u02f1")
        buf.write(u"\u02f2\7\20\2\2\u02f2\u02f3\5x=\2\u02f3\u02f4\5\u00dc")
        buf.write(u"o\2\u02f4\u02f5\5z>\2\u02f5\u02f7\3\2\2\2\u02f6\u02e7")
        buf.write(u"\3\2\2\2\u02f6\u02ee\3\2\2\2\u02f79\3\2\2\2\u02f8\u02f9")
        buf.write(u"\7]\2\2\u02f9\u02fa\7T\2\2\u02fa\u02fd\5\u00acW\2\u02fb")
        buf.write(u"\u02fc\7\22\2\2\u02fc\u02fe\5\u00acW\2\u02fd\u02fb\3")
        buf.write(u"\2\2\2\u02fd\u02fe\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff")
        buf.write(u"\u0300\7a\2\2\u0300\u0301\5L\'\2\u0301\u0302\7\20\2\2")
        buf.write(u"\u0302\u0303\5x=\2\u0303\u0304\5\u00dco\2\u0304\u0305")
        buf.write(u"\5z>\2\u0305;\3\2\2\2\u0306\u0307\7R\2\2\u0307\u0308")
        buf.write(u"\7\20\2\2\u0308\u0309\5x=\2\u0309\u030a\5\u00dco\2\u030a")
        buf.write(u"\u030b\5z>\2\u030b\u030c\5v<\2\u030c\u030d\7\u0086\2")
        buf.write(u"\2\u030d\u030e\5L\'\2\u030e=\3\2\2\2\u030f\u0310\7\u0086")
        buf.write(u"\2\2\u0310\u0311\5L\'\2\u0311\u0312\7\20\2\2\u0312\u0313")
        buf.write(u"\5x=\2\u0313\u0314\5\u00dco\2\u0314\u0315\5z>\2\u0315")
        buf.write(u"?\3\2\2\2\u0316\u0317\7`\2\2\u0317\u0318\5L\'\2\u0318")
        buf.write(u"\u0319\7\20\2\2\u0319\u031a\5x=\2\u031a\u031b\5\u00dc")
        buf.write(u"o\2\u031b\u031f\5z>\2\u031c\u031d\5v<\2\u031d\u031e\5")
        buf.write(u"B\"\2\u031e\u0320\3\2\2\2\u031f\u031c\3\2\2\2\u031f\u0320")
        buf.write(u"\3\2\2\2\u0320\u0328\3\2\2\2\u0321\u0322\5v<\2\u0322")
        buf.write(u"\u0323\7U\2\2\u0323\u0324\7\20\2\2\u0324\u0325\5x=\2")
        buf.write(u"\u0325\u0326\5\u00dco\2\u0326\u0327\5z>\2\u0327\u0329")
        buf.write(u"\3\2\2\2\u0328\u0321\3\2\2\2\u0328\u0329\3\2\2\2\u0329")
        buf.write(u"A\3\2\2\2\u032a\u032b\b\"\1\2\u032b\u032c\7U\2\2\u032c")
        buf.write(u"\u032d\7`\2\2\u032d\u032e\5L\'\2\u032e\u032f\7\20\2\2")
        buf.write(u"\u032f\u0330\5x=\2\u0330\u0331\5\u00dco\2\u0331\u0332")
        buf.write(u"\5z>\2\u0332\u033f\3\2\2\2\u0333\u0334\f\3\2\2\u0334")
        buf.write(u"\u0335\5v<\2\u0335\u0336\7U\2\2\u0336\u0337\7`\2\2\u0337")
        buf.write(u"\u0338\5L\'\2\u0338\u0339\7\20\2\2\u0339\u033a\5x=\2")
        buf.write(u"\u033a\u033b\5\u00dco\2\u033b\u033c\5z>\2\u033c\u033e")
        buf.write(u"\3\2\2\2\u033d\u0333\3\2\2\2\u033e\u0341\3\2\2\2\u033f")
        buf.write(u"\u033d\3\2\2\2\u033f\u0340\3\2\2\2\u0340C\3\2\2\2\u0341")
        buf.write(u"\u033f\3\2\2\2\u0342\u0343\7t\2\2\u0343\u0344\5L\'\2")
        buf.write(u"\u0344E\3\2\2\2\u0345\u0346\7~\2\2\u0346\u0347\7n\2\2")
        buf.write(u"\u0347\u0348\5\u00acW\2\u0348\u0349\7S\2\2\u0349\u034a")
        buf.write(u"\7\20\2\2\u034a\u034b\5x=\2\u034b\u034c\5\u00dco\2\u034c")
        buf.write(u"\u034d\5z>\2\u034d\u034f\5t;\2\u034e\u0350\5\u00e0q\2")
        buf.write(u"\u034f\u034e\3\2\2\2\u034f\u0350\3\2\2\2\u0350\u035c")
        buf.write(u"\3\2\2\2\u0351\u0355\7r\2\2\u0352\u0353\7\u0084\2\2\u0353")
        buf.write(u"\u0355\7D\2\2\u0354\u0351\3\2\2\2\u0354\u0352\3\2\2\2")
        buf.write(u"\u0355\u0356\3\2\2\2\u0356\u0357\7\20\2\2\u0357\u0358")
        buf.write(u"\5x=\2\u0358\u0359\5\u00dco\2\u0359\u035a\5z>\2\u035a")
        buf.write(u"\u035b\5t;\2\u035b\u035d\3\2\2\2\u035c\u0354\3\2\2\2")
        buf.write(u"\u035c\u035d\3\2\2\2\u035d\u0365\3\2\2\2\u035e\u035f")
        buf.write(u"\7B\2\2\u035f\u0360\7\20\2\2\u0360\u0361\5x=\2\u0361")
        buf.write(u"\u0362\5\u00dco\2\u0362\u0363\5z>\2\u0363\u0364\5t;\2")
        buf.write(u"\u0364\u0366\3\2\2\2\u0365\u035e\3\2\2\2\u0365\u0366")
        buf.write(u"\3\2\2\2\u0366\u0367\3\2\2\2\u0367\u0368\5t;\2\u0368")
        buf.write(u"G\3\2\2\2\u0369\u036a\7\u0084\2\2\u036a\u036b\5\u00b0")
        buf.write(u"Y\2\u036b\u036c\7\20\2\2\u036c\u036d\5x=\2\u036d\u036e")
        buf.write(u"\5\u00dco\2\u036e\u036f\5z>\2\u036f\u0370\5t;\2\u0370")
        buf.write(u"\u037d\3\2\2\2\u0371\u0372\7\u0084\2\2\u0372\u0373\7")
        buf.write(u"a\2\2\u0373\u0374\7\27\2\2\u0374\u0375\5\u008cG\2\u0375")
        buf.write(u"\u0376\7\30\2\2\u0376\u0377\7\20\2\2\u0377\u0378\5x=")
        buf.write(u"\2\u0378\u0379\5\u00dco\2\u0379\u037a\5z>\2\u037a\u037b")
        buf.write(u"\5t;\2\u037b\u037d\3\2\2\2\u037c\u0369\3\2\2\2\u037c")
        buf.write(u"\u0371\3\2\2\2\u037dI\3\2\2\2\u037e\u0380\7x\2\2\u037f")
        buf.write(u"\u0381\5L\'\2\u0380\u037f\3\2\2\2\u0380\u0381\3\2\2\2")
        buf.write(u"\u0381K\3\2\2\2\u0382\u0383\b\'\1\2\u0383\u0384\7#\2")
        buf.write(u"\2\u0384\u039d\5L\'(\u0385\u0386\7k\2\2\u0386\u039d\5")
        buf.write(u"L\'\'\u0387\u0388\7>\2\2\u0388\u0389\7\20\2\2\u0389\u039d")
        buf.write(u"\5L\'\f\u038a\u039d\5V,\2\u038b\u039d\5N(\2\u038c\u038d")
        buf.write(u"\5N(\2\u038d\u038e\5h\65\2\u038e\u039d\3\2\2\2\u038f")
        buf.write(u"\u0390\7Y\2\2\u0390\u0391\7\20\2\2\u0391\u039d\5\u00ac")
        buf.write(u"W\2\u0392\u0393\7=\2\2\u0393\u0394\7\20\2\2\u0394\u039d")
        buf.write(u"\5\u00a8U\2\u0395\u039d\5Z.\2\u0396\u039d\5\\/\2\u0397")
        buf.write(u"\u039d\5d\63\2\u0398\u039d\5^\60\2\u0399\u039d\5f\64")
        buf.write(u"\2\u039a\u039d\5b\62\2\u039b\u039d\5R*\2\u039c\u0382")
        buf.write(u"\3\2\2\2\u039c\u0385\3\2\2\2\u039c\u0387\3\2\2\2\u039c")
        buf.write(u"\u038a\3\2\2\2\u039c\u038b\3\2\2\2\u039c\u038c\3\2\2")
        buf.write(u"\2\u039c\u038f\3\2\2\2\u039c\u0392\3\2\2\2\u039c\u0395")
        buf.write(u"\3\2\2\2\u039c\u0396\3\2\2\2\u039c\u0397\3\2\2\2\u039c")
        buf.write(u"\u0398\3\2\2\2\u039c\u0399\3\2\2\2\u039c\u039a\3\2\2")
        buf.write(u"\2\u039c\u039b\3\2\2\2\u039d\u03fe\3\2\2\2\u039e\u039f")
        buf.write(u"\f&\2\2\u039f\u03a0\5\u010e\u0088\2\u03a0\u03a1\5L\'")
        buf.write(u"\'\u03a1\u03fd\3\2\2\2\u03a2\u03a3\f%\2\2\u03a3\u03a4")
        buf.write(u"\5\u0110\u0089\2\u03a4\u03a5\5L\'&\u03a5\u03fd\3\2\2")
        buf.write(u"\2\u03a6\u03a7\f$\2\2\u03a7\u03a8\5\u0114\u008b\2\u03a8")
        buf.write(u"\u03a9\5L\'%\u03a9\u03fd\3\2\2\2\u03aa\u03ab\f#\2\2\u03ab")
        buf.write(u"\u03ac\5\u0112\u008a\2\u03ac\u03ad\5L\'$\u03ad\u03fd")
        buf.write(u"\3\2\2\2\u03ae\u03af\f\"\2\2\u03af\u03b0\t\2\2\2\u03b0")
        buf.write(u"\u03fd\5L\'#\u03b1\u03b2\f!\2\2\u03b2\u03b3\7*\2\2\u03b3")
        buf.write(u"\u03fd\5L\'\"\u03b4\u03b5\f \2\2\u03b5\u03b6\7+\2\2\u03b6")
        buf.write(u"\u03fd\5L\'!\u03b7\u03b8\f\37\2\2\u03b8\u03b9\7(\2\2")
        buf.write(u"\u03b9\u03fd\5L\' \u03ba\u03bb\f\36\2\2\u03bb\u03bc\7")
        buf.write(u")\2\2\u03bc\u03fd\5L\'\37\u03bd\u03be\f\33\2\2\u03be")
        buf.write(u"\u03bf\7-\2\2\u03bf\u03fd\5L\'\34\u03c0\u03c1\f\32\2")
        buf.write(u"\2\u03c1\u03c2\7,\2\2\u03c2\u03fd\5L\'\33\u03c3\u03c4")
        buf.write(u"\f\31\2\2\u03c4\u03c5\7\61\2\2\u03c5\u03fd\5L\'\32\u03c6")
        buf.write(u"\u03c7\f\30\2\2\u03c7\u03c8\7q\2\2\u03c8\u03fd\5L\'\31")
        buf.write(u"\u03c9\u03ca\f\27\2\2\u03ca\u03cb\7C\2\2\u03cb\u03fd")
        buf.write(u"\5L\'\30\u03cc\u03cd\f\26\2\2\u03cd\u03ce\7`\2\2\u03ce")
        buf.write(u"\u03cf\5L\'\2\u03cf\u03d0\7U\2\2\u03d0\u03d1\5L\'\27")
        buf.write(u"\u03d1\u03fd\3\2\2\2\u03d2\u03d3\f\24\2\2\u03d3\u03d4")
        buf.write(u"\7a\2\2\u03d4\u03fd\5L\'\25\u03d5\u03d6\f\23\2\2\u03d6")
        buf.write(u"\u03d7\7N\2\2\u03d7\u03fd\5L\'\24\u03d8\u03d9\f\22\2")
        buf.write(u"\2\u03d9\u03da\7N\2\2\u03da\u03db\7A\2\2\u03db\u03fd")
        buf.write(u"\5L\'\23\u03dc\u03dd\f\21\2\2\u03dd\u03de\7N\2\2\u03de")
        buf.write(u"\u03df\7D\2\2\u03df\u03fd\5L\'\22\u03e0\u03e1\f\20\2")
        buf.write(u"\2\u03e1\u03e2\7k\2\2\u03e2\u03e3\7a\2\2\u03e3\u03fd")
        buf.write(u"\5L\'\21\u03e4\u03e5\f\17\2\2\u03e5\u03e6\7k\2\2\u03e6")
        buf.write(u"\u03e7\7N\2\2\u03e7\u03fd\5L\'\20\u03e8\u03e9\f\16\2")
        buf.write(u"\2\u03e9\u03ea\7k\2\2\u03ea\u03eb\7N\2\2\u03eb\u03ec")
        buf.write(u"\7A\2\2\u03ec\u03fd\5L\'\17\u03ed\u03ee\f\r\2\2\u03ee")
        buf.write(u"\u03ef\7k\2\2\u03ef\u03f0\7N\2\2\u03f0\u03f1\7D\2\2\u03f1")
        buf.write(u"\u03fd\5L\'\16\u03f2\u03f3\f\35\2\2\u03f3\u03f4\7c\2")
        buf.write(u"\2\u03f4\u03f5\7k\2\2\u03f5\u03fd\5\u0102\u0082\2\u03f6")
        buf.write(u"\u03f7\f\34\2\2\u03f7\u03f8\7c\2\2\u03f8\u03fd\5\u0102")
        buf.write(u"\u0082\2\u03f9\u03fa\f\25\2\2\u03fa\u03fb\7E\2\2\u03fb")
        buf.write(u"\u03fd\5\u00bc_\2\u03fc\u039e\3\2\2\2\u03fc\u03a2\3\2")
        buf.write(u"\2\2\u03fc\u03a6\3\2\2\2\u03fc\u03aa\3\2\2\2\u03fc\u03ae")
        buf.write(u"\3\2\2\2\u03fc\u03b1\3\2\2\2\u03fc\u03b4\3\2\2\2\u03fc")
        buf.write(u"\u03b7\3\2\2\2\u03fc\u03ba\3\2\2\2\u03fc\u03bd\3\2\2")
        buf.write(u"\2\u03fc\u03c0\3\2\2\2\u03fc\u03c3\3\2\2\2\u03fc\u03c6")
        buf.write(u"\3\2\2\2\u03fc\u03c9\3\2\2\2\u03fc\u03cc\3\2\2\2\u03fc")
        buf.write(u"\u03d2\3\2\2\2\u03fc\u03d5\3\2\2\2\u03fc\u03d8\3\2\2")
        buf.write(u"\2\u03fc\u03dc\3\2\2\2\u03fc\u03e0\3\2\2\2\u03fc\u03e4")
        buf.write(u"\3\2\2\2\u03fc\u03e8\3\2\2\2\u03fc\u03ed\3\2\2\2\u03fc")
        buf.write(u"\u03f2\3\2\2\2\u03fc\u03f6\3\2\2\2\u03fc\u03f9\3\2\2")
        buf.write(u"\2\u03fd\u0400\3\2\2\2\u03fe\u03fc\3\2\2\2\u03fe\u03ff")
        buf.write(u"\3\2\2\2\u03ffM\3\2\2\2\u0400\u03fe\3\2\2\2\u0401\u0402")
        buf.write(u"\b(\1\2\u0402\u0403\5\u00aaV\2\u0403\u0408\3\2\2\2\u0404")
        buf.write(u"\u0405\f\3\2\2\u0405\u0407\5P)\2\u0406\u0404\3\2\2\2")
        buf.write(u"\u0407\u040a\3\2\2\2\u0408\u0406\3\2\2\2\u0408\u0409")
        buf.write(u"\3\2\2\2\u0409O\3\2\2\2\u040a\u0408\3\2\2\2\u040b\u040c")
        buf.write(u"\6)\37\3\u040c\u040d\7\24\2\2\u040d\u040e\5\u00aaV\2")
        buf.write(u"\u040eQ\3\2\2\2\u040f\u0410\7b\2\2\u0410\u0411\7\20\2")
        buf.write(u"\2\u0411\u0412\5\u00acW\2\u0412\u0413\5T+\2\u0413S\3")
        buf.write(u"\2\2\2\u0414\u0415\6+ \3\u0415U\3\2\2\2\u0416\u0417\b")
        buf.write(u",\1\2\u0417\u0418\5\u00e8u\2\u0418\u041d\3\2\2\2\u0419")
        buf.write(u"\u041a\f\3\2\2\u041a\u041c\5X-\2\u041b\u0419\3\2\2\2")
        buf.write(u"\u041c\u041f\3\2\2\2\u041d\u041b\3\2\2\2\u041d\u041e")
        buf.write(u"\3\2\2\2\u041eW\3\2\2\2\u041f\u041d\3\2\2\2\u0420\u0421")
        buf.write(u"\6-\"\3\u0421\u0422\7\24\2\2\u0422\u042e\5\u00acW\2\u0423")
        buf.write(u"\u0424\6-#\3\u0424\u0425\7\27\2\2\u0425\u0426\5\u00fc")
        buf.write(u"\177\2\u0426\u0427\7\30\2\2\u0427\u042e\3\2\2\2\u0428")
        buf.write(u"\u0429\6-$\3\u0429\u042a\7\27\2\2\u042a\u042b\5L\'\2")
        buf.write(u"\u042b\u042c\7\30\2\2\u042c\u042e\3\2\2\2\u042d\u0420")
        buf.write(u"\3\2\2\2\u042d\u0423\3\2\2\2\u042d\u0428\3\2\2\2\u042e")
        buf.write(u"Y\3\2\2\2\u042f\u0430\5\u00a2R\2\u0430[\3\2\2\2\u0431")
        buf.write(u"\u0432\5\u009eP\2\u0432\u0433\7^\2\2\u0433\u043c\5L\'")
        buf.write(u"\2\u0434\u0436\7\22\2\2\u0435\u0434\3\2\2\2\u0435\u0436")
        buf.write(u"\3\2\2\2\u0436\u0437\3\2\2\2\u0437\u043a\5j\66\2\u0438")
        buf.write(u"\u0439\7C\2\2\u0439\u043b\5l\67\2\u043a\u0438\3\2\2\2")
        buf.write(u"\u043a\u043b\3\2\2\2\u043b\u043d\3\2\2\2\u043c\u0435")
        buf.write(u"\3\2\2\2\u043c\u043d\3\2\2\2\u043d\u0447\3\2\2\2\u043e")
        buf.write(u"\u0444\5\u009eP\2\u043f\u0442\5j\66\2\u0440\u0441\7C")
        buf.write(u"\2\2\u0441\u0443\5l\67\2\u0442\u0440\3\2\2\2\u0442\u0443")
        buf.write(u"\3\2\2\2\u0443\u0445\3\2\2\2\u0444\u043f\3\2\2\2\u0444")
        buf.write(u"\u0445\3\2\2\2\u0445\u0447\3\2\2\2\u0446\u0431\3\2\2")
        buf.write(u"\2\u0446\u043e\3\2\2\2\u0447]\3\2\2\2\u0448\u0449\7u")
        buf.write(u"\2\2\u0449\u044a\7^\2\2\u044a\u044b\5L\'\2\u044b_\3\2")
        buf.write(u"\2\2\u044c\u044d\7\u0087\2\2\u044d\u044e\5L\'\2\u044e")
        buf.write(u"\u044f\7\u0081\2\2\u044f\u0450\5L\'\2\u0450a\3\2\2\2")
        buf.write(u"\u0451\u0452\5N(\2\u0452\u0453\7#\2\2\u0453\u0454\5L")
        buf.write(u"\'\2\u0454c\3\2\2\2\u0455\u0456\7[\2\2\u0456\u0457\7")
        buf.write(u"D\2\2\u0457\u0458\5\u00acW\2\u0458\u0459\7^\2\2\u0459")
        buf.write(u"\u045a\5L\'\2\u045a\u045b\7\u0085\2\2\u045b\u045c\5L")
        buf.write(u"\'\2\u045ce\3\2\2\2\u045d\u045e\7}\2\2\u045e\u0464\5")
        buf.write(u"V,\2\u045f\u0460\7\u0083\2\2\u0460\u0461\5V,\2\u0461")
        buf.write(u"\u0462\7E\2\2\u0462\u0463\5\u0106\u0084\2\u0463\u0465")
        buf.write(u"\3\2\2\2\u0464\u045f\3\2\2\2\u0464\u0465\3\2\2\2\u0465")
        buf.write(u"g\3\2\2\2\u0466\u0467\6\65%\3\u0467\u046d\5L\'\2\u0468")
        buf.write(u"\u046b\5j\66\2\u0469\u046a\7C\2\2\u046a\u046c\5l\67\2")
        buf.write(u"\u046b\u0469\3\2\2\2\u046b\u046c\3\2\2\2\u046c\u046e")
        buf.write(u"\3\2\2\2\u046d\u0468\3\2\2\2\u046d\u046e\3\2\2\2\u046e")
        buf.write(u"\u0475\3\2\2\2\u046f\u0472\5j\66\2\u0470\u0471\7C\2\2")
        buf.write(u"\u0471\u0473\5l\67\2\u0472\u0470\3\2\2\2\u0472\u0473")
        buf.write(u"\3\2\2\2\u0473\u0475\3\2\2\2\u0474\u0466\3\2\2\2\u0474")
        buf.write(u"\u046f\3\2\2\2\u0475i\3\2\2\2\u0476\u0477\b\66\1\2\u0477")
        buf.write(u"\u0478\7\u0083\2\2\u0478\u0479\5l\67\2\u0479\u047f\3")
        buf.write(u"\2\2\2\u047a\u047b\f\3\2\2\u047b\u047c\7\22\2\2\u047c")
        buf.write(u"\u047e\5l\67\2\u047d\u047a\3\2\2\2\u047e\u0481\3\2\2")
        buf.write(u"\2\u047f\u047d\3\2\2\2\u047f\u0480\3\2\2\2\u0480k\3\2")
        buf.write(u"\2\2\u0481\u047f\3\2\2\2\u0482\u0483\5L\'\2\u0483\u0484")
        buf.write(u"\7E\2\2\u0484\u0485\5\u00acW\2\u0485m\3\2\2\2\u0486\u0487")
        buf.write(u"\5\u0100\u0081\2\u0487\u0488\5\u010c\u0087\2\u0488\u0489")
        buf.write(u"\5L\'\2\u0489o\3\2\2\2\u048a\u048b\69\'\3\u048b\u048c")
        buf.write(u"\7\24\2\2\u048c\u0493\5\u00acW\2\u048d\u048e\69(\3\u048e")
        buf.write(u"\u048f\7\27\2\2\u048f\u0490\5L\'\2\u0490\u0491\7\30\2")
        buf.write(u"\2\u0491\u0493\3\2\2\2\u0492\u048a\3\2\2\2\u0492\u048d")
        buf.write(u"\3\2\2\2\u0493q\3\2\2\2\u0494\u0495\5\u00d0i\2\u0495")
        buf.write(u"\u0496\5\u010c\u0087\2\u0496\u0497\5L\'\2\u0497s\3\2")
        buf.write(u"\2\2\u0498\u049a\7\7\2\2\u0499\u0498\3\2\2\2\u049a\u049d")
        buf.write(u"\3\2\2\2\u049b\u0499\3\2\2\2\u049b\u049c\3\2\2\2\u049c")
        buf.write(u"u\3\2\2\2\u049d\u049b\3\2\2\2\u049e\u04a0\7\7\2\2\u049f")
        buf.write(u"\u049e\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1\u049f\3\2\2")
        buf.write(u"\2\u04a1\u04a2\3\2\2\2\u04a2w\3\2\2\2\u04a3\u04a5\7\7")
        buf.write(u"\2\2\u04a4\u04a3\3\2\2\2\u04a5\u04a6\3\2\2\2\u04a6\u04a4")
        buf.write(u"\3\2\2\2\u04a6\u04a7\3\2\2\2\u04a7\u04a8\3\2\2\2\u04a8")
        buf.write(u"\u04a9\7\3\2\2\u04a9y\3\2\2\2\u04aa\u04ac\7\7\2\2\u04ab")
        buf.write(u"\u04aa\3\2\2\2\u04ac\u04af\3\2\2\2\u04ad\u04ab\3\2\2")
        buf.write(u"\2\u04ad\u04ae\3\2\2\2\u04ae\u04b0\3\2\2\2\u04af\u04ad")
        buf.write(u"\3\2\2\2\u04b0\u04b1\7\4\2\2\u04b1{\3\2\2\2\u04b2\u04b3")
        buf.write(u"\7l\2\2\u04b3}\3\2\2\2\u04b4\u04b6\5\u0080A\2\u04b5\u04b4")
        buf.write(u"\3\2\2\2\u04b5\u04b6\3\2\2\2\u04b6\u04b7\3\2\2\2\u04b7")
        buf.write(u"\u04b8\5t;\2\u04b8\u04b9\7\2\2\3\u04b9\177\3\2\2\2\u04ba")
        buf.write(u"\u04bb\bA\1\2\u04bb\u04bc\5\u0082B\2\u04bc\u04c3\3\2")
        buf.write(u"\2\2\u04bd\u04be\f\3\2\2\u04be\u04bf\5v<\2\u04bf\u04c0")
        buf.write(u"\5\u0082B\2\u04c0\u04c2\3\2\2\2\u04c1\u04bd\3\2\2\2\u04c2")
        buf.write(u"\u04c5\3\2\2\2\u04c3\u04c1\3\2\2\2\u04c3\u04c4\3\2\2")
        buf.write(u"\2\u04c4\u0081\3\2\2\2\u04c5\u04c3\3\2\2\2\u04c6\u04cc")
        buf.write(u"\5\n\6\2\u04c7\u04cc\5\u00a4S\2\u04c8\u04cc\5\u0084C")
        buf.write(u"\2\u04c9\u04cc\5\u0086D\2\u04ca\u04cc\5\u00d2j\2\u04cb")
        buf.write(u"\u04c6\3\2\2\2\u04cb\u04c7\3\2\2\2\u04cb\u04c8\3\2\2")
        buf.write(u"\2\u04cb\u04c9\3\2\2\2\u04cb\u04ca\3\2\2\2\u04cc\u0083")
        buf.write(u"\3\2\2\2\u04cd\u04ce\5\34\17\2\u04ce\u0085\3\2\2\2\u04cf")
        buf.write(u"\u04d2\5\2\2\2\u04d0\u04d2\5\4\3\2\u04d1\u04cf\3\2\2")
        buf.write(u"\2\u04d1\u04d0\3\2\2\2\u04d2\u0087\3\2\2\2\u04d3\u04d4")
        buf.write(u"\bE\1\2\u04d4\u04d5\5\6\4\2\u04d5\u04dc\3\2\2\2\u04d6")
        buf.write(u"\u04d7\f\3\2\2\u04d7\u04d8\5v<\2\u04d8\u04d9\5\6\4\2")
        buf.write(u"\u04d9\u04db\3\2\2\2\u04da\u04d6\3\2\2\2\u04db\u04de")
        buf.write(u"\3\2\2\2\u04dc\u04da\3\2\2\2\u04dc\u04dd\3\2\2\2\u04dd")
        buf.write(u"\u0089\3\2\2\2\u04de\u04dc\3\2\2\2\u04df\u04e0\bF\1\2")
        buf.write(u"\u04e0\u04e1\5\b\5\2\u04e1\u04e8\3\2\2\2\u04e2\u04e3")
        buf.write(u"\f\3\2\2\u04e3\u04e4\5v<\2\u04e4\u04e5\5\b\5\2\u04e5")
        buf.write(u"\u04e7\3\2\2\2\u04e6\u04e2\3\2\2\2\u04e7\u04ea\3\2\2")
        buf.write(u"\2\u04e8\u04e6\3\2\2\2\u04e8\u04e9\3\2\2\2\u04e9\u008b")
        buf.write(u"\3\2\2\2\u04ea\u04e8\3\2\2\2\u04eb\u04ec\bG\1\2\u04ec")
        buf.write(u"\u04ed\5\u00b0Y\2\u04ed\u04f3\3\2\2\2\u04ee\u04ef\f\3")
        buf.write(u"\2\2\u04ef\u04f0\7\22\2\2\u04f0\u04f2\5\u00b0Y\2\u04f1")
        buf.write(u"\u04ee\3\2\2\2\u04f2\u04f5\3\2\2\2\u04f3\u04f1\3\2\2")
        buf.write(u"\2\u04f3\u04f4\3\2\2\2\u04f4\u008d\3\2\2\2\u04f5\u04f3")
        buf.write(u"\3\2\2\2\u04f6\u04f7\7a\2\2\u04f7\u0501\5\u0090I\2\u04f8")
        buf.write(u"\u04f9\7a\2\2\u04f9\u0501\5\u0092J\2\u04fa\u04fb\7a\2")
        buf.write(u"\2\u04fb\u0501\5\u0096L\2\u04fc\u04fd\7e\2\2\u04fd\u0501")
        buf.write(u"\7\u008f\2\2\u04fe\u04ff\7e\2\2\u04ff\u0501\5L\'\2\u0500")
        buf.write(u"\u04f6\3\2\2\2\u0500\u04f8\3\2\2\2\u0500\u04fa\3\2\2")
        buf.write(u"\2\u0500\u04fc\3\2\2\2\u0500\u04fe\3\2\2\2\u0501\u008f")
        buf.write(u"\3\2\2\2\u0502\u0504\7\27\2\2\u0503\u0505\5\u0094K\2")
        buf.write(u"\u0504\u0503\3\2\2\2\u0504\u0505\3\2\2\2\u0505\u0506")
        buf.write(u"\3\2\2\2\u0506\u0507\7\30\2\2\u0507\u0091\3\2\2\2\u0508")
        buf.write(u"\u050a\7*\2\2\u0509\u050b\5\u0094K\2\u050a\u0509\3\2")
        buf.write(u"\2\2\u050a\u050b\3\2\2\2\u050b\u050c\3\2\2\2\u050c\u050d")
        buf.write(u"\7(\2\2\u050d\u0093\3\2\2\2\u050e\u050f\bK\1\2\u050f")
        buf.write(u"\u0510\5L\'\2\u0510\u0516\3\2\2\2\u0511\u0512\f\3\2\2")
        buf.write(u"\u0512\u0513\7\22\2\2\u0513\u0515\5L\'\2\u0514\u0511")
        buf.write(u"\3\2\2\2\u0515\u0518\3\2\2\2\u0516\u0514\3\2\2\2\u0516")
        buf.write(u"\u0517\3\2\2\2\u0517\u0095\3\2\2\2\u0518\u0516\3\2\2")
        buf.write(u"\2\u0519\u051a\7\27\2\2\u051a\u051b\5L\'\2\u051b\u051c")
        buf.write(u"\7\23\2\2\u051c\u051d\5L\'\2\u051d\u051e\7\30\2\2\u051e")
        buf.write(u"\u0097\3\2\2\2\u051f\u0520\bM\1\2\u0520\u0521\5\u009a")
        buf.write(u"N\2\u0521\u052c\3\2\2\2\u0522\u0523\f\5\2\2\u0523\u052b")
        buf.write(u"\7,\2\2\u0524\u0525\f\4\2\2\u0525\u0526\7\27\2\2\u0526")
        buf.write(u"\u052b\7\30\2\2\u0527\u0528\f\3\2\2\u0528\u0529\7\31")
        buf.write(u"\2\2\u0529\u052b\7\32\2\2\u052a\u0522\3\2\2\2\u052a\u0524")
        buf.write(u"\3\2\2\2\u052a\u0527\3\2\2\2\u052b\u052e\3\2\2\2\u052c")
        buf.write(u"\u052a\3\2\2\2\u052c\u052d\3\2\2\2\u052d\u0099\3\2\2")
        buf.write(u"\2\u052e\u052c\3\2\2\2\u052f\u0532\5\u009cO\2\u0530\u0532")
        buf.write(u"\5\u009eP\2\u0531\u052f\3\2\2\2\u0531\u0530\3\2\2\2\u0532")
        buf.write(u"\u009b\3\2\2\2\u0533\u053e\7\64\2\2\u0534\u053e\7\65")
        buf.write(u"\2\2\u0535\u053e\7\66\2\2\u0536\u053e\7\67\2\2\u0537")
        buf.write(u"\u053e\78\2\2\u0538\u053e\79\2\2\u0539\u053e\7;\2\2\u053a")
        buf.write(u"\u053e\7:\2\2\u053b\u053e\7<\2\2\u053c\u053e\7>\2\2\u053d")
        buf.write(u"\u0533\3\2\2\2\u053d\u0534\3\2\2\2\u053d\u0535\3\2\2")
        buf.write(u"\2\u053d\u0536\3\2\2\2\u053d\u0537\3\2\2\2\u053d\u0538")
        buf.write(u"\3\2\2\2\u053d\u0539\3\2\2\2\u053d\u053a\3\2\2\2\u053d")
        buf.write(u"\u053b\3\2\2\2\u053d\u053c\3\2\2\2\u053e\u009d\3\2\2")
        buf.write(u"\2\u053f\u0540\7\u008d\2\2\u0540\u009f\3\2\2\2\u0541")
        buf.write(u"\u0542\7>\2\2\u0542\u00a1\3\2\2\2\u0543\u0544\7?\2\2")
        buf.write(u"\u0544\u00a3\3\2\2\2\u0545\u0549\5\f\7\2\u0546\u0549")
        buf.write(u"\5\32\16\2\u0547\u0549\5\16\b\2\u0548\u0545\3\2\2\2\u0548")
        buf.write(u"\u0546\3\2\2\2\u0548\u0547\3\2\2\2\u0549\u00a5\3\2\2")
        buf.write(u"\2\u054a\u054b\bT\1\2\u054b\u054c\5\u00aeX\2\u054c\u0552")
        buf.write(u"\3\2\2\2\u054d\u054e\f\3\2\2\u054e\u054f\7\22\2\2\u054f")
        buf.write(u"\u0551\5\u00aeX\2\u0550\u054d\3\2\2\2\u0551\u0554\3\2")
        buf.write(u"\2\2\u0552\u0550\3\2\2\2\u0552\u0553\3\2\2\2\u0553\u00a7")
        buf.write(u"\3\2\2\2\u0554\u0552\3\2\2\2\u0555\u0558\5\u00acW\2\u0556")
        buf.write(u"\u0558\5\u00aeX\2\u0557\u0555\3\2\2\2\u0557\u0556\3\2")
        buf.write(u"\2\2\u0558\u00a9\3\2\2\2\u0559\u055d\5\u00acW\2\u055a")
        buf.write(u"\u055d\5\u00aeX\2\u055b\u055d\5\u00b0Y\2\u055c\u0559")
        buf.write(u"\3\2\2\2\u055c\u055a\3\2\2\2\u055c\u055b\3\2\2\2\u055d")
        buf.write(u"\u00ab\3\2\2\2\u055e\u055f\7\u008e\2\2\u055f\u00ad\3")
        buf.write(u"\2\2\2\u0560\u0561\7\u008d\2\2\u0561\u00af\3\2\2\2\u0562")
        buf.write(u"\u0563\7\u008c\2\2\u0563\u00b1\3\2\2\2\u0564\u0565\b")
        buf.write(u"Z\1\2\u0565\u0566\5\u00b4[\2\u0566\u056c\3\2\2\2\u0567")
        buf.write(u"\u0568\f\3\2\2\u0568\u0569\7\22\2\2\u0569\u056b\5\u00b4")
        buf.write(u"[\2\u056a\u0567\3\2\2\2\u056b\u056e\3\2\2\2\u056c\u056a")
        buf.write(u"\3\2\2\2\u056c\u056d\3\2\2\2\u056d\u00b3\3\2\2\2\u056e")
        buf.write(u"\u056c\3\2\2\2\u056f\u0572\5\u00ba^\2\u0570\u0572\5\u00b6")
        buf.write(u"\\\2\u0571\u056f\3\2\2\2\u0571\u0570\3\2\2\2\u0572\u00b5")
        buf.write(u"\3\2\2\2\u0573\u0576\5\u00b8]\2\u0574\u0576\5,\27\2\u0575")
        buf.write(u"\u0573\3\2\2\2\u0575\u0574\3\2\2\2\u0576\u00b7\3\2\2")
        buf.write(u"\2\u0577\u057a\5\u00acW\2\u0578\u0579\7-\2\2\u0579\u057b")
        buf.write(u"\5\u00eex\2\u057a\u0578\3\2\2\2\u057a\u057b\3\2\2\2\u057b")
        buf.write(u"\u00b9\3\2\2\2\u057c\u057d\5\u00a0Q\2\u057d\u057e\5\u00ac")
        buf.write(u"W\2\u057e\u00bb\3\2\2\2\u057f\u0582\5\u0098M\2\u0580")
        buf.write(u"\u0582\5\u00be`\2\u0581\u057f\3\2\2\2\u0581\u0580\3\2")
        buf.write(u"\2\2\u0582\u00bd\3\2\2\2\u0583\u0584\b`\1\2\u0584\u0585")
        buf.write(u"\7D\2\2\u0585\u058e\3\2\2\2\u0586\u0587\f\4\2\2\u0587")
        buf.write(u"\u0588\7\27\2\2\u0588\u058d\7\30\2\2\u0589\u058a\f\3")
        buf.write(u"\2\2\u058a\u058b\7\31\2\2\u058b\u058d\7\32\2\2\u058c")
        buf.write(u"\u0586\3\2\2\2\u058c\u0589\3\2\2\2\u058d\u0590\3\2\2")
        buf.write(u"\2\u058e\u058c\3\2\2\2\u058e\u058f\3\2\2\2\u058f\u00bf")
        buf.write(u"\3\2\2\2\u0590\u058e\3\2\2\2\u0591\u0592\ba\1\2\u0592")
        buf.write(u"\u0593\5\u00c2b\2\u0593\u059a\3\2\2\2\u0594\u0595\f\3")
        buf.write(u"\2\2\u0595\u0596\5v<\2\u0596\u0597\5\u00c2b\2\u0597\u0599")
        buf.write(u"\3\2\2\2\u0598\u0594\3\2\2\2\u0599\u059c\3\2\2\2\u059a")
        buf.write(u"\u0598\3\2\2\2\u059a\u059b\3\2\2\2\u059b\u00c1\3\2\2")
        buf.write(u"\2\u059c\u059a\3\2\2\2\u059d\u05a2\5\26\f\2\u059e\u05a2")
        buf.write(u"\5\30\r\2\u059f\u05a2\5\22\n\2\u05a0\u05a2\5\24\13\2")
        buf.write(u"\u05a1\u059d\3\2\2\2\u05a1\u059e\3\2\2\2\u05a1\u059f")
        buf.write(u"\3\2\2\2\u05a1\u05a0\3\2\2\2\u05a2\u00c3\3\2\2\2\u05a3")
        buf.write(u"\u05a4\7\n\2\2\u05a4\u05ae\5\u0156\u00ac\2\u05a5\u05a6")
        buf.write(u"\7\13\2\2\u05a6\u05ae\5\u016c\u00b7\2\u05a7\u05a8\7\f")
        buf.write(u"\2\2\u05a8\u05ae\5\u00c6d\2\u05a9\u05aa\7\r\2\2\u05aa")
        buf.write(u"\u05ae\5\u00c6d\2\u05ab\u05ac\7\16\2\2\u05ac\u05ae\5")
        buf.write(u"\u00ccg\2\u05ad\u05a3\3\2\2\2\u05ad\u05a5\3\2\2\2\u05ad")
        buf.write(u"\u05a7\3\2\2\2\u05ad\u05a9\3\2\2\2\u05ad\u05ab\3\2\2")
        buf.write(u"\2\u05ae\u00c5\3\2\2\2\u05af\u05b1\5\u00aaV\2\u05b0\u05b2")
        buf.write(u"\5\u00c8e\2\u05b1\u05b0\3\2\2\2\u05b1\u05b2\3\2\2\2\u05b2")
        buf.write(u"\u00c7\3\2\2\2\u05b3\u05b4\7^\2\2\u05b4\u05b5\5\u00ca")
        buf.write(u"f\2\u05b5\u05b6\7\20\2\2\u05b6\u05bb\5\u00aaV\2\u05b7")
        buf.write(u"\u05b8\7\24\2\2\u05b8\u05ba\5\u00aaV\2\u05b9\u05b7\3")
        buf.write(u"\2\2\2\u05ba\u05bd\3\2\2\2\u05bb\u05b9\3\2\2\2\u05bb")
        buf.write(u"\u05bc\3\2\2\2\u05bc\u00c9\3\2\2\2\u05bd\u05bb\3\2\2")
        buf.write(u"\2\u05be\u05bf\7\u008e\2\2\u05bf\u05c0\6f\66\3\u05c0")
        buf.write(u"\u00cb\3\2\2\2\u05c1\u05c3\5\u00aaV\2\u05c2\u05c4\5\u00ce")
        buf.write(u"h\2\u05c3\u05c2\3\2\2\2\u05c3\u05c4\3\2\2\2\u05c4\u00cd")
        buf.write(u"\3\2\2\2\u05c5\u05c6\7^\2\2\u05c6\u05c7\5\u00caf\2\u05c7")
        buf.write(u"\u05c9\7\20\2\2\u05c8\u05ca\7%\2\2\u05c9\u05c8\3\2\2")
        buf.write(u"\2\u05c9\u05ca\3\2\2\2\u05ca\u05cb\3\2\2\2\u05cb\u05d0")
        buf.write(u"\5\u00aaV\2\u05cc\u05cd\7%\2\2\u05cd\u05cf\5\u00aaV\2")
        buf.write(u"\u05ce\u05cc\3\2\2\2\u05cf\u05d2\3\2\2\2\u05d0\u05ce")
        buf.write(u"\3\2\2\2\u05d0\u05d1\3\2\2\2\u05d1\u05d5\3\2\2\2\u05d2")
        buf.write(u"\u05d0\3\2\2\2\u05d3\u05d4\7\24\2\2\u05d4\u05d6\5\u00aa")
        buf.write(u"V\2\u05d5\u05d3\3\2\2\2\u05d5\u05d6\3\2\2\2\u05d6\u00cf")
        buf.write(u"\3\2\2\2\u05d7\u05d8\bi\1\2\u05d8\u05d9\5\u00acW\2\u05d9")
        buf.write(u"\u05df\3\2\2\2\u05da\u05db\f\3\2\2\u05db\u05dc\7\22\2")
        buf.write(u"\2\u05dc\u05de\5\u00acW\2\u05dd\u05da\3\2\2\2\u05de\u05e1")
        buf.write(u"\3\2\2\2\u05df\u05dd\3\2\2\2\u05df\u05e0\3\2\2\2\u05e0")
        buf.write(u"\u00d1\3\2\2\2\u05e1\u05df\3\2\2\2\u05e2\u05e6\5$\23")
        buf.write(u"\2\u05e3\u05e6\5&\24\2\u05e4\u05e6\5(\25\2\u05e5\u05e2")
        buf.write(u"\3\2\2\2\u05e5\u05e3\3\2\2\2\u05e5\u05e4\3\2\2\2\u05e6")
        buf.write(u"\u00d3\3\2\2\2\u05e7\u05e8\bk\1\2\u05e8\u05e9\5\u00d6")
        buf.write(u"l\2\u05e9\u05f0\3\2\2\2\u05ea\u05eb\f\3\2\2\u05eb\u05ec")
        buf.write(u"\5v<\2\u05ec\u05ed\5\u00d6l\2\u05ed\u05ef\3\2\2\2\u05ee")
        buf.write(u"\u05ea\3\2\2\2\u05ef\u05f2\3\2\2\2\u05f0\u05ee\3\2\2")
        buf.write(u"\2\u05f0\u05f1\3\2\2\2\u05f1\u00d5\3\2\2\2\u05f2\u05f0")
        buf.write(u"\3\2\2\2\u05f3\u05f4\7\n\2\2\u05f4\u05fe\5\u0144\u00a3")
        buf.write(u"\2\u05f5\u05f6\7\13\2\2\u05f6\u05fe\5\u015c\u00af\2\u05f7")
        buf.write(u"\u05f8\7\f\2\2\u05f8\u05fe\5\u00d8m\2\u05f9\u05fa\7\r")
        buf.write(u"\2\2\u05fa\u05fe\5\u00d8m\2\u05fb\u05fc\7\16\2\2\u05fc")
        buf.write(u"\u05fe\5\u00dan\2\u05fd\u05f3\3\2\2\2\u05fd\u05f5\3\2")
        buf.write(u"\2\2\u05fd\u05f7\3\2\2\2\u05fd\u05f9\3\2\2\2\u05fd\u05fb")
        buf.write(u"\3\2\2\2\u05fe\u00d7\3\2\2\2\u05ff\u0601\5\u012c\u0097")
        buf.write(u"\2\u0600\u0602\7\21\2\2\u0601\u0600\3\2\2\2\u0601\u0602")
        buf.write(u"\3\2\2\2\u0602\u0604\3\2\2\2\u0603\u0605\5\u00c8e\2\u0604")
        buf.write(u"\u0603\3\2\2\2\u0604\u0605\3\2\2\2\u0605\u00d9\3\2\2")
        buf.write(u"\2\u0606\u0608\5\u0116\u008c\2\u0607\u0609\7\21\2\2\u0608")
        buf.write(u"\u0607\3\2\2\2\u0608\u0609\3\2\2\2\u0609\u060b\3\2\2")
        buf.write(u"\2\u060a\u060c\5\u00ceh\2\u060b\u060a\3\2\2\2\u060b\u060c")
        buf.write(u"\3\2\2\2\u060c\u00db\3\2\2\2\u060d\u060e\bo\1\2\u060e")
        buf.write(u"\u060f\5.\30\2\u060f\u0616\3\2\2\2\u0610\u0611\f\3\2")
        buf.write(u"\2\u0611\u0612\5v<\2\u0612\u0613\5.\30\2\u0613\u0615")
        buf.write(u"\3\2\2\2\u0614\u0610\3\2\2\2\u0615\u0618\3\2\2\2\u0616")
        buf.write(u"\u0614\3\2\2\2\u0616\u0617\3\2\2\2\u0617\u00dd\3\2\2")
        buf.write(u"\2\u0618\u0616\3\2\2\2\u0619\u061a\bp\1\2\u061a\u061b")
        buf.write(u"\58\35\2\u061b\u0622\3\2\2\2\u061c\u061d\f\3\2\2\u061d")
        buf.write(u"\u061e\5v<\2\u061e\u061f\58\35\2\u061f\u0621\3\2\2\2")
        buf.write(u"\u0620\u061c\3\2\2\2\u0621\u0624\3\2\2\2\u0622\u0620")
        buf.write(u"\3\2\2\2\u0622\u0623\3\2\2\2\u0623\u00df\3\2\2\2\u0624")
        buf.write(u"\u0622\3\2\2\2\u0625\u0626\bq\1\2\u0626\u0627\5H%\2\u0627")
        buf.write(u"\u062e\3\2\2\2\u0628\u0629\f\3\2\2\u0629\u062a\5v<\2")
        buf.write(u"\u062a\u062b\5H%\2\u062b\u062d\3\2\2\2\u062c\u0628\3")
        buf.write(u"\2\2\2\u062d\u0630\3\2\2\2\u062e\u062c\3\2\2\2\u062e")
        buf.write(u"\u062f\3\2\2\2\u062f\u00e1\3\2\2\2\u0630\u062e\3\2\2")
        buf.write(u"\2\u0631\u0632\7\27\2\2\u0632\u0633\5\u00e4s\2\u0633")
        buf.write(u"\u0634\7\23\2\2\u0634\u0635\5\u00e4s\2\u0635\u0636\7")
        buf.write(u"\30\2\2\u0636\u0640\3\2\2\2\u0637\u0638\7\27\2\2\u0638")
        buf.write(u"\u0639\5\u00e6t\2\u0639\u063a\7\30\2\2\u063a\u0640\3")
        buf.write(u"\2\2\2\u063b\u063c\7*\2\2\u063c\u063d\5\u00e6t\2\u063d")
        buf.write(u"\u063e\7(\2\2\u063e\u0640\3\2\2\2\u063f\u0631\3\2\2\2")
        buf.write(u"\u063f\u0637\3\2\2\2\u063f\u063b\3\2\2\2\u0640\u00e3")
        buf.write(u"\3\2\2\2\u0641\u064f\7\u008a\2\2\u0642\u064f\7\u008b")
        buf.write(u"\2\2\u0643\u064f\7\u0090\2\2\u0644\u064f\7\u0091\2\2")
        buf.write(u"\u0645\u064f\7\u0089\2\2\u0646\u064f\7\u0095\2\2\u0647")
        buf.write(u"\u064f\7\u0094\2\2\u0648\u064f\7\u008f\2\2\u0649\u064f")
        buf.write(u"\7\u0092\2\2\u064a\u064f\7\u0093\2\2\u064b\u064f\7\u0088")
        buf.write(u"\2\2\u064c\u064f\7\u0096\2\2\u064d\u064f\5|?\2\u064e")
        buf.write(u"\u0641\3\2\2\2\u064e\u0642\3\2\2\2\u064e\u0643\3\2\2")
        buf.write(u"\2\u064e\u0644\3\2\2\2\u064e\u0645\3\2\2\2\u064e\u0646")
        buf.write(u"\3\2\2\2\u064e\u0647\3\2\2\2\u064e\u0648\3\2\2\2\u064e")
        buf.write(u"\u0649\3\2\2\2\u064e\u064a\3\2\2\2\u064e\u064b\3\2\2")
        buf.write(u"\2\u064e\u064c\3\2\2\2\u064e\u064d\3\2\2\2\u064f\u00e5")
        buf.write(u"\3\2\2\2\u0650\u0651\bt\1\2\u0651\u0652\5\u00e4s\2\u0652")
        buf.write(u"\u0658\3\2\2\2\u0653\u0654\f\3\2\2\u0654\u0655\7\22\2")
        buf.write(u"\2\u0655\u0657\5\u00e4s\2\u0656\u0653\3\2\2\2\u0657\u065a")
        buf.write(u"\3\2\2\2\u0658\u0656\3\2\2\2\u0658\u0659\3\2\2\2\u0659")
        buf.write(u"\u00e7\3\2\2\2\u065a\u0658\3\2\2\2\u065b\u0660\5\u00ec")
        buf.write(u"w\2\u065c\u0660\5\u00eex\2\u065d\u0660\5\u00aaV\2\u065e")
        buf.write(u"\u0660\5\u00eav\2\u065f\u065b\3\2\2\2\u065f\u065c\3\2")
        buf.write(u"\2\2\u065f\u065d\3\2\2\2\u065f\u065e\3\2\2\2\u0660\u00e9")
        buf.write(u"\3\2\2\2\u0661\u0662\t\3\2\2\u0662\u00eb\3\2\2\2\u0663")
        buf.write(u"\u0664\7\25\2\2\u0664\u0665\5L\'\2\u0665\u0666\7\26\2")
        buf.write(u"\2\u0666\u00ed\3\2\2\2\u0667\u066a\5\u00e4s\2\u0668\u066a")
        buf.write(u"\5\u00f0y\2\u0669\u0667\3\2\2\2\u0669\u0668\3\2\2\2\u066a")
        buf.write(u"\u00ef\3\2\2\2\u066b\u0671\5\u0096L\2\u066c\u0671\5\u0090")
        buf.write(u"I\2\u066d\u0671\5\u0092J\2\u066e\u0671\5\u00f4{\2\u066f")
        buf.write(u"\u0671\5\u00f2z\2\u0670\u066b\3\2\2\2\u0670\u066c\3\2")
        buf.write(u"\2\2\u0670\u066d\3\2\2\2\u0670\u066e\3\2\2\2\u0670\u066f")
        buf.write(u"\3\2\2\2\u0671\u00f1\3\2\2\2\u0672\u0674\7\25\2\2\u0673")
        buf.write(u"\u0675\5\u00f6|\2\u0674\u0673\3\2\2\2\u0674\u0675\3\2")
        buf.write(u"\2\2\u0675\u0676\3\2\2\2\u0676\u0677\7\26\2\2\u0677\u00f3")
        buf.write(u"\3\2\2\2\u0678\u067a\7\31\2\2\u0679\u067b\5\u00f8}\2")
        buf.write(u"\u067a\u0679\3\2\2\2\u067a\u067b\3\2\2\2\u067b\u067c")
        buf.write(u"\3\2\2\2\u067c\u067d\7\32\2\2\u067d\u00f5\3\2\2\2\u067e")
        buf.write(u"\u067f\b|\1\2\u067f\u0680\5L\'\2\u0680\u0686\3\2\2\2")
        buf.write(u"\u0681\u0682\f\3\2\2\u0682\u0683\7\22\2\2\u0683\u0685")
        buf.write(u"\5L\'\2\u0684\u0681\3\2\2\2\u0685\u0688\3\2\2\2\u0686")
        buf.write(u"\u0684\3\2\2\2\u0686\u0687\3\2\2\2\u0687\u00f7\3\2\2")
        buf.write(u"\2\u0688\u0686\3\2\2\2\u0689\u068a\b}\1\2\u068a\u068b")
        buf.write(u"\5\u00fa~\2\u068b\u0691\3\2\2\2\u068c\u068d\f\3\2\2\u068d")
        buf.write(u"\u068e\7\22\2\2\u068e\u0690\5\u00fa~\2\u068f\u068c\3")
        buf.write(u"\2\2\2\u0690\u0693\3\2\2\2\u0691\u068f\3\2\2\2\u0691")
        buf.write(u"\u0692\3\2\2\2\u0692\u00f9\3\2\2\2\u0693\u0691\3\2\2")
        buf.write(u"\2\u0694\u0695\5L\'\2\u0695\u0696\7\20\2\2\u0696\u0697")
        buf.write(u"\5L\'\2\u0697\u00fb\3\2\2\2\u0698\u0699\5L\'\2\u0699")
        buf.write(u"\u069a\7\20\2\2\u069a\u069b\5L\'\2\u069b\u06a2\3\2\2")
        buf.write(u"\2\u069c\u069d\5L\'\2\u069d\u069e\7\20\2\2\u069e\u06a2")
        buf.write(u"\3\2\2\2\u069f\u06a0\7\20\2\2\u06a0\u06a2\5L\'\2\u06a1")
        buf.write(u"\u0698\3\2\2\2\u06a1\u069c\3\2\2\2\u06a1\u069f\3\2\2")
        buf.write(u"\2\u06a2\u00fd\3\2\2\2\u06a3\u06a4\5\u00acW\2\u06a4\u06a5")
        buf.write(u"\5\u010c\u0087\2\u06a5\u06a6\5L\'\2\u06a6\u00ff\3\2\2")
        buf.write(u"\2\u06a7\u06a8\b\u0081\1\2\u06a8\u06a9\5\u00acW\2\u06a9")
        buf.write(u"\u06ae\3\2\2\2\u06aa\u06ab\f\3\2\2\u06ab\u06ad\5p9\2")
        buf.write(u"\u06ac\u06aa\3\2\2\2\u06ad\u06b0\3\2\2\2\u06ae\u06ac")
        buf.write(u"\3\2\2\2\u06ae\u06af\3\2\2\2\u06af\u0101\3\2\2\2\u06b0")
        buf.write(u"\u06ae\3\2\2\2\u06b1\u06b2\6\u0082@\3\u06b2\u06b3\7\u008e")
        buf.write(u"\2\2\u06b3\u06b6\5\u00bc_\2\u06b4\u06b6\5L\'\2\u06b5")
        buf.write(u"\u06b1\3\2\2\2\u06b5\u06b4\3\2\2\2\u06b6\u0103\3\2\2")
        buf.write(u"\2\u06b7\u06be\7\"\2\2\u06b8\u06be\7#\2\2\u06b9\u06be")
        buf.write(u"\5\u010e\u0088\2\u06ba\u06be\5\u0110\u0089\2\u06bb\u06be")
        buf.write(u"\5\u0112\u008a\2\u06bc\u06be\5\u0114\u008b\2\u06bd\u06b7")
        buf.write(u"\3\2\2\2\u06bd\u06b8\3\2\2\2\u06bd\u06b9\3\2\2\2\u06bd")
        buf.write(u"\u06ba\3\2\2\2\u06bd\u06bb\3\2\2\2\u06bd\u06bc\3\2\2")
        buf.write(u"\2\u06be\u0105\3\2\2\2\u06bf\u06c0\7\u008e\2\2\u06c0")
        buf.write(u"\u06c1\6\u0084A\3\u06c1\u0107\3\2\2\2\u06c2\u06c3\7\u008e")
        buf.write(u"\2\2\u06c3\u06c4\6\u0085B\3\u06c4\u0109\3\2\2\2\u06c5")
        buf.write(u"\u06c6\7\u008e\2\2\u06c6\u06c7\6\u0086C\3\u06c7\u010b")
        buf.write(u"\3\2\2\2\u06c8\u06c9\7-\2\2\u06c9\u010d\3\2\2\2\u06ca")
        buf.write(u"\u06cb\7$\2\2\u06cb\u010f\3\2\2\2\u06cc\u06cd\7%\2\2")
        buf.write(u"\u06cd\u0111\3\2\2\2\u06ce\u06cf\7&\2\2\u06cf\u0113\3")
        buf.write(u"\2\2\2\u06d0\u06d1\t\4\2\2\u06d1\u0115\3\2\2\2\u06d2")
        buf.write(u"\u06d3\7x\2\2\u06d3\u06d4\5\u0118\u008d\2\u06d4\u06d5")
        buf.write(u"\7\21\2\2\u06d5\u06da\3\2\2\2\u06d6\u06d7\5\u0118\u008d")
        buf.write(u"\2\u06d7\u06d8\7\21\2\2\u06d8\u06da\3\2\2\2\u06d9\u06d2")
        buf.write(u"\3\2\2\2\u06d9\u06d6\3\2\2\2\u06da\u0117\3\2\2\2\u06db")
        buf.write(u"\u06dc\b\u008d\1\2\u06dc\u06dd\5\u011a\u008e\2\u06dd")
        buf.write(u"\u06e2\3\2\2\2\u06de\u06df\f\3\2\2\u06df\u06e1\5\u011c")
        buf.write(u"\u008f\2\u06e0\u06de\3\2\2\2\u06e1\u06e4\3\2\2\2\u06e2")
        buf.write(u"\u06e0\3\2\2\2\u06e2\u06e3\3\2\2\2\u06e3\u0119\3\2\2")
        buf.write(u"\2\u06e4\u06e2\3\2\2\2\u06e5\u06e9\5\u0124\u0093\2\u06e6")
        buf.write(u"\u06e9\5\u0126\u0094\2\u06e7\u06e9\5\u0128\u0095\2\u06e8")
        buf.write(u"\u06e5\3\2\2\2\u06e8\u06e6\3\2\2\2\u06e8\u06e7\3\2\2")
        buf.write(u"\2\u06e9\u011b\3\2\2\2\u06ea\u06eb\7\24\2\2\u06eb\u06ee")
        buf.write(u"\5\u011e\u0090\2\u06ec\u06ee\5\u0122\u0092\2\u06ed\u06ea")
        buf.write(u"\3\2\2\2\u06ed\u06ec\3\2\2\2\u06ee\u011d\3\2\2\2\u06ef")
        buf.write(u"\u06f0\5\u012a\u0096\2\u06f0\u06f2\7\25\2\2\u06f1\u06f3")
        buf.write(u"\5\u0120\u0091\2\u06f2\u06f1\3\2\2\2\u06f2\u06f3\3\2")
        buf.write(u"\2\2\u06f3\u06f4\3\2\2\2\u06f4\u06f5\7\26\2\2\u06f5\u011f")
        buf.write(u"\3\2\2\2\u06f6\u06f7\b\u0091\1\2\u06f7\u06f8\5\u0118")
        buf.write(u"\u008d\2\u06f8\u06fe\3\2\2\2\u06f9\u06fa\f\3\2\2\u06fa")
        buf.write(u"\u06fb\7\22\2\2\u06fb\u06fd\5\u0118\u008d\2\u06fc\u06f9")
        buf.write(u"\3\2\2\2\u06fd\u0700\3\2\2\2\u06fe\u06fc\3\2\2\2\u06fe")
        buf.write(u"\u06ff\3\2\2\2\u06ff\u0121\3\2\2\2\u0700\u06fe\3\2\2")
        buf.write(u"\2\u0701\u0702\7\27\2\2\u0702\u0703\5\u0118\u008d\2\u0703")
        buf.write(u"\u0704\7\30\2\2\u0704\u0123\3\2\2\2\u0705\u0706\7\25")
        buf.write(u"\2\2\u0706\u0707\5\u0118\u008d\2\u0707\u0708\7\26\2\2")
        buf.write(u"\u0708\u0125\3\2\2\2\u0709\u070a\b\u0094\1\2\u070a\u070b")
        buf.write(u"\5\u012a\u0096\2\u070b\u0711\3\2\2\2\u070c\u070d\f\3")
        buf.write(u"\2\2\u070d\u070e\7\24\2\2\u070e\u0710\5\u012a\u0096\2")
        buf.write(u"\u070f\u070c\3\2\2\2\u0710\u0713\3\2\2\2\u0711\u070f")
        buf.write(u"\3\2\2\2\u0711\u0712\3\2\2\2\u0712\u0127\3\2\2\2\u0713")
        buf.write(u"\u0711\3\2\2\2\u0714\u071a\7\u0090\2\2\u0715\u071a\7")
        buf.write(u"\u0092\2\2\u0716\u071a\7\u008f\2\2\u0717\u071a\7\u0088")
        buf.write(u"\2\2\u0718\u071a\7\u0089\2\2\u0719\u0714\3\2\2\2\u0719")
        buf.write(u"\u0715\3\2\2\2\u0719\u0716\3\2\2\2\u0719\u0717\3\2\2")
        buf.write(u"\2\u0719\u0718\3\2\2\2\u071a\u0129\3\2\2\2\u071b\u071c")
        buf.write(u"\t\5\2\2\u071c\u012b\3\2\2\2\u071d\u071e\7x\2\2\u071e")
        buf.write(u"\u0721\5\u012e\u0098\2\u071f\u0721\5\u012e\u0098\2\u0720")
        buf.write(u"\u071d\3\2\2\2\u0720\u071f\3\2\2\2\u0721\u012d\3\2\2")
        buf.write(u"\2\u0722\u0723\b\u0098\1\2\u0723\u0724\5\u0130\u0099")
        buf.write(u"\2\u0724\u0729\3\2\2\2\u0725\u0726\f\3\2\2\u0726\u0728")
        buf.write(u"\5\u0132\u009a\2\u0727\u0725\3\2\2\2\u0728\u072b\3\2")
        buf.write(u"\2\2\u0729\u0727\3\2\2\2\u0729\u072a\3\2\2\2\u072a\u012f")
        buf.write(u"\3\2\2\2\u072b\u0729\3\2\2\2\u072c\u0731\5\u013c\u009f")
        buf.write(u"\2\u072d\u0731\5\u013e\u00a0\2\u072e\u0731\5\u0140\u00a1")
        buf.write(u"\2\u072f\u0731\5\u0134\u009b\2\u0730\u072c\3\2\2\2\u0730")
        buf.write(u"\u072d\3\2\2\2\u0730\u072e\3\2\2\2\u0730\u072f\3\2\2")
        buf.write(u"\2\u0731\u0131\3\2\2\2\u0732\u0733\7\24\2\2\u0733\u0739")
        buf.write(u"\5\u0134\u009b\2\u0734\u0735\7\27\2\2\u0735\u0736\5\u012e")
        buf.write(u"\u0098\2\u0736\u0737\7\30\2\2\u0737\u0739\3\2\2\2\u0738")
        buf.write(u"\u0732\3\2\2\2\u0738\u0734\3\2\2\2\u0739\u0133\3\2\2")
        buf.write(u"\2\u073a\u073b\5\u0142\u00a2\2\u073b\u073d\7\25\2\2\u073c")
        buf.write(u"\u073e\5\u0136\u009c\2\u073d\u073c\3\2\2\2\u073d\u073e")
        buf.write(u"\3\2\2\2\u073e\u073f\3\2\2\2\u073f\u0740\7\26\2\2\u0740")
        buf.write(u"\u0135\3\2\2\2\u0741\u0748\5\u0138\u009d\2\u0742\u0748")
        buf.write(u"\5\u013a\u009e\2\u0743\u0744\5\u0138\u009d\2\u0744\u0745")
        buf.write(u"\7\22\2\2\u0745\u0746\5\u013a\u009e\2\u0746\u0748\3\2")
        buf.write(u"\2\2\u0747\u0741\3\2\2\2\u0747\u0742\3\2\2\2\u0747\u0743")
        buf.write(u"\3\2\2\2\u0748\u0137\3\2\2\2\u0749\u074a\b\u009d\1\2")
        buf.write(u"\u074a\u074b\5\u012e\u0098\2\u074b\u0751\3\2\2\2\u074c")
        buf.write(u"\u074d\f\3\2\2\u074d\u074e\7\22\2\2\u074e\u0750\5\u012e")
        buf.write(u"\u0098\2\u074f\u074c\3\2\2\2\u0750\u0753\3\2\2\2\u0751")
        buf.write(u"\u074f\3\2\2\2\u0751\u0752\3\2\2\2\u0752\u0139\3\2\2")
        buf.write(u"\2\u0753\u0751\3\2\2\2\u0754\u0755\b\u009e\1\2\u0755")
        buf.write(u"\u0756\5\u0142\u00a2\2\u0756\u0757\7-\2\2\u0757\u0758")
        buf.write(u"\5\u012e\u0098\2\u0758\u0761\3\2\2\2\u0759\u075a\f\3")
        buf.write(u"\2\2\u075a\u075b\7\22\2\2\u075b\u075c\5\u0142\u00a2\2")
        buf.write(u"\u075c\u075d\7-\2\2\u075d\u075e\5\u012e\u0098\2\u075e")
        buf.write(u"\u0760\3\2\2\2\u075f\u0759\3\2\2\2\u0760\u0763\3\2\2")
        buf.write(u"\2\u0761\u075f\3\2\2\2\u0761\u0762\3\2\2\2\u0762\u013b")
        buf.write(u"\3\2\2\2\u0763\u0761\3\2\2\2\u0764\u0765\7\25\2\2\u0765")
        buf.write(u"\u0766\5\u012e\u0098\2\u0766\u0767\7\26\2\2\u0767\u013d")
        buf.write(u"\3\2\2\2\u0768\u0769\b\u00a0\1\2\u0769\u076a\5\u0142")
        buf.write(u"\u00a2\2\u076a\u0770\3\2\2\2\u076b\u076c\f\3\2\2\u076c")
        buf.write(u"\u076d\7\24\2\2\u076d\u076f\5\u0142\u00a2\2\u076e\u076b")
        buf.write(u"\3\2\2\2\u076f\u0772\3\2\2\2\u0770\u076e\3\2\2\2\u0770")
        buf.write(u"\u0771\3\2\2\2\u0771\u013f\3\2\2\2\u0772\u0770\3\2\2")
        buf.write(u"\2\u0773\u0779\7\u0090\2\2\u0774\u0779\7\u0092\2\2\u0775")
        buf.write(u"\u0779\7\u008f\2\2\u0776\u0779\7\u0088\2\2\u0777\u0779")
        buf.write(u"\7\u0089\2\2\u0778\u0773\3\2\2\2\u0778\u0774\3\2\2\2")
        buf.write(u"\u0778\u0775\3\2\2\2\u0778\u0776\3\2\2\2\u0778\u0777")
        buf.write(u"\3\2\2\2\u0779\u0141\3\2\2\2\u077a\u077b\t\6\2\2\u077b")
        buf.write(u"\u0143\3\2\2\2\u077c\u077d\7x\2\2\u077d\u077e\5\u0146")
        buf.write(u"\u00a4\2\u077e\u077f\7\21\2\2\u077f\u0784\3\2\2\2\u0780")
        buf.write(u"\u0781\5\u0146\u00a4\2\u0781\u0782\7\21\2\2\u0782\u0784")
        buf.write(u"\3\2\2\2\u0783\u077c\3\2\2\2\u0783\u0780\3\2\2\2\u0784")
        buf.write(u"\u0145\3\2\2\2\u0785\u0786\b\u00a4\1\2\u0786\u0787\5")
        buf.write(u"\u0148\u00a5\2\u0787\u078c\3\2\2\2\u0788\u0789\f\3\2")
        buf.write(u"\2\u0789\u078b\5\u014a\u00a6\2\u078a\u0788\3\2\2\2\u078b")
        buf.write(u"\u078e\3\2\2\2\u078c\u078a\3\2\2\2\u078c\u078d\3\2\2")
        buf.write(u"\2\u078d\u0147\3\2\2\2\u078e\u078c\3\2\2\2\u078f\u0793")
        buf.write(u"\5\u0152\u00aa\2\u0790\u0793\5\u0154\u00ab\2\u0791\u0793")
        buf.write(u"\5\u0158\u00ad\2\u0792\u078f\3\2\2\2\u0792\u0790\3\2")
        buf.write(u"\2\2\u0792\u0791\3\2\2\2\u0793\u0149\3\2\2\2\u0794\u0795")
        buf.write(u"\7\24\2\2\u0795\u0798\5\u014c\u00a7\2\u0796\u0798\5\u0150")
        buf.write(u"\u00a9\2\u0797\u0794\3\2\2\2\u0797\u0796\3\2\2\2\u0798")
        buf.write(u"\u014b\3\2\2\2\u0799\u079a\5\u015a\u00ae\2\u079a\u079c")
        buf.write(u"\7\25\2\2\u079b\u079d\5\u014e\u00a8\2\u079c\u079b\3\2")
        buf.write(u"\2\2\u079c\u079d\3\2\2\2\u079d\u079e\3\2\2\2\u079e\u079f")
        buf.write(u"\7\26\2\2\u079f\u014d\3\2\2\2\u07a0\u07a1\b\u00a8\1\2")
        buf.write(u"\u07a1\u07a2\5\u0146\u00a4\2\u07a2\u07a8\3\2\2\2\u07a3")
        buf.write(u"\u07a4\f\3\2\2\u07a4\u07a5\7\22\2\2\u07a5\u07a7\5\u0146")
        buf.write(u"\u00a4\2\u07a6\u07a3\3\2\2\2\u07a7\u07aa\3\2\2\2\u07a8")
        buf.write(u"\u07a6\3\2\2\2\u07a8\u07a9\3\2\2\2\u07a9\u014f\3\2\2")
        buf.write(u"\2\u07aa\u07a8\3\2\2\2\u07ab\u07ac\7\27\2\2\u07ac\u07ad")
        buf.write(u"\5\u0146\u00a4\2\u07ad\u07ae\7\30\2\2\u07ae\u0151\3\2")
        buf.write(u"\2\2\u07af\u07b0\7\25\2\2\u07b0\u07b1\5\u0146\u00a4\2")
        buf.write(u"\u07b1\u07b2\7\26\2\2\u07b2\u0153\3\2\2\2\u07b3\u07b4")
        buf.write(u"\b\u00ab\1\2\u07b4\u07b5\5\u015a\u00ae\2\u07b5\u07bb")
        buf.write(u"\3\2\2\2\u07b6\u07b7\f\3\2\2\u07b7\u07b8\7\24\2\2\u07b8")
        buf.write(u"\u07ba\5\u015a\u00ae\2\u07b9\u07b6\3\2\2\2\u07ba\u07bd")
        buf.write(u"\3\2\2\2\u07bb\u07b9\3\2\2\2\u07bb\u07bc\3\2\2\2\u07bc")
        buf.write(u"\u0155\3\2\2\2\u07bd\u07bb\3\2\2\2\u07be\u07bf\b\u00ac")
        buf.write(u"\1\2\u07bf\u07c0\5\u0154\u00ab\2\u07c0\u07c6\3\2\2\2")
        buf.write(u"\u07c1\u07c2\f\3\2\2\u07c2\u07c3\7\35\2\2\u07c3\u07c5")
        buf.write(u"\7\u008d\2\2\u07c4\u07c1\3\2\2\2\u07c5\u07c8\3\2\2\2")
        buf.write(u"\u07c6\u07c4\3\2\2\2\u07c6\u07c7\3\2\2\2\u07c7\u0157")
        buf.write(u"\3\2\2\2\u07c8\u07c6\3\2\2\2\u07c9\u07cf\7\u0090\2\2")
        buf.write(u"\u07ca\u07cf\7\u0092\2\2\u07cb\u07cf\7\u008f\2\2\u07cc")
        buf.write(u"\u07cf\7\u0088\2\2\u07cd\u07cf\7\u0089\2\2\u07ce\u07c9")
        buf.write(u"\3\2\2\2\u07ce\u07ca\3\2\2\2\u07ce\u07cb\3\2\2\2\u07ce")
        buf.write(u"\u07cc\3\2\2\2\u07ce\u07cd\3\2\2\2\u07cf\u0159\3\2\2")
        buf.write(u"\2\u07d0\u07d1\t\6\2\2\u07d1\u015b\3\2\2\2\u07d2\u07d3")
        buf.write(u"\7x\2\2\u07d3\u07d4\5\u015e\u00b0\2\u07d4\u07d5\7\21")
        buf.write(u"\2\2\u07d5\u07da\3\2\2\2\u07d6\u07d7\5\u015e\u00b0\2")
        buf.write(u"\u07d7\u07d8\7\21\2\2\u07d8\u07da\3\2\2\2\u07d9\u07d2")
        buf.write(u"\3\2\2\2\u07d9\u07d6\3\2\2\2\u07da\u015d\3\2\2\2\u07db")
        buf.write(u"\u07dc\b\u00b0\1\2\u07dc\u07dd\5\u0160\u00b1\2\u07dd")
        buf.write(u"\u07e2\3\2\2\2\u07de\u07df\f\3\2\2\u07df\u07e1\5\u0162")
        buf.write(u"\u00b2\2\u07e0\u07de\3\2\2\2\u07e1\u07e4\3\2\2\2\u07e2")
        buf.write(u"\u07e0\3\2\2\2\u07e2\u07e3\3\2\2\2\u07e3\u015f\3\2\2")
        buf.write(u"\2\u07e4\u07e2\3\2\2\2\u07e5\u07e9\5\u016a\u00b6\2\u07e6")
        buf.write(u"\u07e9\5\u016c\u00b7\2\u07e7\u07e9\5\u016e\u00b8\2\u07e8")
        buf.write(u"\u07e5\3\2\2\2\u07e8\u07e6\3\2\2\2\u07e8\u07e7\3\2\2")
        buf.write(u"\2\u07e9\u0161\3\2\2\2\u07ea\u07eb\7\24\2\2\u07eb\u07ee")
        buf.write(u"\5\u0164\u00b3\2\u07ec\u07ee\5\u0168\u00b5\2\u07ed\u07ea")
        buf.write(u"\3\2\2\2\u07ed\u07ec\3\2\2\2\u07ee\u0163\3\2\2\2\u07ef")
        buf.write(u"\u07f0\5\u0170\u00b9\2\u07f0\u07f2\7\25\2\2\u07f1\u07f3")
        buf.write(u"\5\u0166\u00b4\2\u07f2\u07f1\3\2\2\2\u07f2\u07f3\3\2")
        buf.write(u"\2\2\u07f3\u07f4\3\2\2\2\u07f4\u07f5\7\26\2\2\u07f5\u0165")
        buf.write(u"\3\2\2\2\u07f6\u07f7\b\u00b4\1\2\u07f7\u07f8\5\u015e")
        buf.write(u"\u00b0\2\u07f8\u07fe\3\2\2\2\u07f9\u07fa\f\3\2\2\u07fa")
        buf.write(u"\u07fb\7\22\2\2\u07fb\u07fd\5\u015e\u00b0\2\u07fc\u07f9")
        buf.write(u"\3\2\2\2\u07fd\u0800\3\2\2\2\u07fe\u07fc\3\2\2\2\u07fe")
        buf.write(u"\u07ff\3\2\2\2\u07ff\u0167\3\2\2\2\u0800\u07fe\3\2\2")
        buf.write(u"\2\u0801\u0802\7\27\2\2\u0802\u0803\5\u015e\u00b0\2\u0803")
        buf.write(u"\u0804\7\30\2\2\u0804\u0169\3\2\2\2\u0805\u0806\7\25")
        buf.write(u"\2\2\u0806\u0807\5\u015e\u00b0\2\u0807\u0808\7\26\2\2")
        buf.write(u"\u0808\u016b\3\2\2\2\u0809\u080a\b\u00b7\1\2\u080a\u080b")
        buf.write(u"\5\u0170\u00b9\2\u080b\u0811\3\2\2\2\u080c\u080d\f\3")
        buf.write(u"\2\2\u080d\u080e\7\24\2\2\u080e\u0810\5\u0170\u00b9\2")
        buf.write(u"\u080f\u080c\3\2\2\2\u0810\u0813\3\2\2\2\u0811\u080f")
        buf.write(u"\3\2\2\2\u0811\u0812\3\2\2\2\u0812\u016d\3\2\2\2\u0813")
        buf.write(u"\u0811\3\2\2\2\u0814\u081a\7\u0090\2\2\u0815\u081a\7")
        buf.write(u"\u0092\2\2\u0816\u081a\7\u008f\2\2\u0817\u081a\7\u0088")
        buf.write(u"\2\2\u0818\u081a\7\u0089\2\2\u0819\u0814\3\2\2\2\u0819")
        buf.write(u"\u0815\3\2\2\2\u0819\u0816\3\2\2\2\u0819\u0817\3\2\2")
        buf.write(u"\2\u0819\u0818\3\2\2\2\u081a\u016f\3\2\2\2\u081b\u081c")
        buf.write(u"\t\6\2\2\u081c\u0171\3\2\2\2\u00a1\u0179\u017e\u019e")
        buf.write(u"\u01a7\u01af\u01ba\u01c3\u01d3\u01dc\u01e3\u01ed\u01f2")
        buf.write(u"\u0205\u0238\u0252\u025f\u0261\u026c\u0271\u027b\u0280")
        buf.write(u"\u0291\u0296\u02a1\u02a6\u02aa\u02bb\u02bf\u02c2\u02e3")
        buf.write(u"\u02f6\u02fd\u031f\u0328\u033f\u034f\u0354\u035c\u0365")
        buf.write(u"\u037c\u0380\u039c\u03fc\u03fe\u0408\u041d\u042d\u0435")
        buf.write(u"\u043a\u043c\u0442\u0444\u0446\u0464\u046b\u046d\u0472")
        buf.write(u"\u0474\u047f\u0492\u049b\u04a1\u04a6\u04ad\u04b5\u04c3")
        buf.write(u"\u04cb\u04d1\u04dc\u04e8\u04f3\u0500\u0504\u050a\u0516")
        buf.write(u"\u052a\u052c\u0531\u053d\u0548\u0552\u0557\u055c\u056c")
        buf.write(u"\u0571\u0575\u057a\u0581\u058c\u058e\u059a\u05a1\u05ad")
        buf.write(u"\u05b1\u05bb\u05c3\u05c9\u05d0\u05d5\u05df\u05e5\u05f0")
        buf.write(u"\u05fd\u0601\u0604\u0608\u060b\u0616\u0622\u062e\u063f")
        buf.write(u"\u064e\u0658\u065f\u0669\u0670\u0674\u067a\u0686\u0691")
        buf.write(u"\u06a1\u06ae\u06b5\u06bd\u06d9\u06e2\u06e8\u06ed\u06f2")
        buf.write(u"\u06fe\u0711\u0719\u0720\u0729\u0730\u0738\u073d\u0747")
        buf.write(u"\u0751\u0761\u0770\u0778\u0783\u078c\u0792\u0797\u079c")
        buf.write(u"\u07a8\u07bb\u07c6\u07ce\u07d9\u07e2\u07e8\u07ed\u07f2")
        buf.write(u"\u07fe\u0811\u0819")
        return buf.getvalue()
		

class EParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"'Java:'", 
                     u"'C#:'", u"'Python2:'", u"'Python3:'", u"'JavaScript:'", 
                     u"'Swift:'", u"':'", u"';'", u"','", u"'..'", u"'.'", 
                     u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'?'", 
                     u"'!'", u"'$'", u"'&'", u"'&&'", u"'|'", u"'||'", u"'+'", 
                     u"'-'", u"'*'", u"'/'", u"'\\'", u"'%'", u"'>'", u"'>='", 
                     u"'<'", u"'<='", u"'<>'", u"'='", u"'!='", u"'=='", 
                     u"'~='", u"'~'", u"'<-'", u"'->'", u"'Boolean'", u"'Character'", 
                     u"'Text'", u"'Integer'", u"'Decimal'", u"'Date'", u"'Time'", 
                     u"'DateTime'", u"'Period'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"'attr'", u"'attribute'", 
                     u"'attributes'", u"'case'", u"'catch'", u"'category'", 
                     u"'class'", u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'do'", u"'doing'", u"'each'", u"'else'", 
                     u"'enum'", u"'enumerated'", u"'except'", u"'execute'", 
                     u"'extends'", u"'fetch'", u"'finally'", u"'for'", u"'from'", 
                     u"'getter'", u"'if'", u"'in'", u"'invoke'", u"'is'", 
                     u"'mappings'", u"'matching'", u"'method'", u"'methods'", 
                     u"'modulo'", u"'native'", u"'None'", u"'not'", u"<INVALID>", 
                     u"'null'", u"'on'", u"'open'", u"'operator'", u"'or'", 
                     u"'otherwise'", u"'pass'", u"'raise'", u"'read'", u"'receiving'", 
                     u"'resource'", u"'return'", u"'returning'", u"'self'", 
                     u"'setter'", u"'singleton'", u"'sorted'", u"'switch'", 
                     u"'this'", u"'throw'", u"'to'", u"'try'", u"'with'", 
                     u"'when'", u"'where'", u"'while'", u"'write'", u"<INVALID>", 
                     u"<INVALID>", u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"INDENT", u"DEDENT", u"LF_TAB", u"LF_MORE", 
                      u"LF", u"TAB", u"WS", u"JAVA", u"CSHARP", u"PYTHON2", 
                      u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", u"SEMI", 
                      u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", u"LBRAK", 
                      u"RBRAK", u"LCURL", u"RCURL", u"QMARK", u"XMARK", 
                      u"DOLLAR", u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", 
                      u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", 
                      u"DOCUMENT", u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", 
                      u"ANY", u"AS", u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", 
                      u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DO", 
                      u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXTENDS", u"FETCH", u"FINALLY", 
                      u"FOR", u"FROM", u"GETTER", u"IF", u"IN", u"INVOKE", 
                      u"IS", u"MAPPINGS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"NATIVE", u"NONE", u"NOT", u"NOTHING", 
                      u"NULL", u"ON", u"OPEN", u"OPERATOR", u"OR", u"OTHERWISE", 
                      u"PASS", u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", 
                      u"RETURN", u"RETURNING", u"SELF", u"SETTER", u"SINGLETON", 
                      u"SORTED", u"SWITCH", u"THIS", u"THROW", u"TO", u"TRY", 
                      u"WITH", u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"TEXT_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL", u"COMMENT" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_concrete_category_declaration = 5
    RULE_singleton_category_declaration = 6
    RULE_derived_list = 7
    RULE_member_method_declaration = 8
    RULE_operator_method_declaration = 9
    RULE_setter_method_declaration = 10
    RULE_getter_method_declaration = 11
    RULE_native_category_declaration = 12
    RULE_native_resource_declaration = 13
    RULE_native_category_mappings = 14
    RULE_native_category_mapping_list = 15
    RULE_attribute_list = 16
    RULE_abstract_method_declaration = 17
    RULE_concrete_method_declaration = 18
    RULE_native_method_declaration = 19
    RULE_full_argument_list = 20
    RULE_typed_argument = 21
    RULE_statement = 22
    RULE_method_call_statement = 23
    RULE_with_resource_statement = 24
    RULE_with_singleton_statement = 25
    RULE_switch_statement = 26
    RULE_switch_case_statement = 27
    RULE_for_each_statement = 28
    RULE_do_while_statement = 29
    RULE_while_statement = 30
    RULE_if_statement = 31
    RULE_else_if_statement_list = 32
    RULE_raise_statement = 33
    RULE_try_statement = 34
    RULE_catch_statement = 35
    RULE_return_statement = 36
    RULE_expression = 37
    RULE_unresolved_expression = 38
    RULE_unresolved_selector = 39
    RULE_invocation_expression = 40
    RULE_invocation_trailer = 41
    RULE_instance_expression = 42
    RULE_instance_selector = 43
    RULE_document_expression = 44
    RULE_constructor_expression = 45
    RULE_read_expression = 46
    RULE_write_statement = 47
    RULE_ambiguous_expression = 48
    RULE_fetch_expression = 49
    RULE_sorted_expression = 50
    RULE_argument_assignment_list = 51
    RULE_with_argument_assignment_list = 52
    RULE_argument_assignment = 53
    RULE_assign_instance_statement = 54
    RULE_child_instance = 55
    RULE_assign_tuple_statement = 56
    RULE_lfs = 57
    RULE_lfp = 58
    RULE_indent = 59
    RULE_dedent = 60
    RULE_null_literal = 61
    RULE_declaration_list = 62
    RULE_declarations = 63
    RULE_declaration = 64
    RULE_resource_declaration = 65
    RULE_enum_declaration = 66
    RULE_native_symbol_list = 67
    RULE_category_symbol_list = 68
    RULE_symbol_list = 69
    RULE_attribute_constraint = 70
    RULE_list_literal = 71
    RULE_set_literal = 72
    RULE_expression_list = 73
    RULE_range_literal = 74
    RULE_typedef = 75
    RULE_primary_type = 76
    RULE_native_type = 77
    RULE_category_type = 78
    RULE_code_type = 79
    RULE_document_type = 80
    RULE_category_declaration = 81
    RULE_type_identifier_list = 82
    RULE_method_identifier = 83
    RULE_identifier = 84
    RULE_variable_identifier = 85
    RULE_type_identifier = 86
    RULE_symbol_identifier = 87
    RULE_argument_list = 88
    RULE_argument = 89
    RULE_operator_argument = 90
    RULE_named_argument = 91
    RULE_code_argument = 92
    RULE_category_or_any_type = 93
    RULE_any_type = 94
    RULE_category_method_declaration_list = 95
    RULE_category_method_declaration = 96
    RULE_native_category_mapping = 97
    RULE_python_category_mapping = 98
    RULE_python_module = 99
    RULE_module_token = 100
    RULE_javascript_category_mapping = 101
    RULE_javascript_module = 102
    RULE_variable_identifier_list = 103
    RULE_method_declaration = 104
    RULE_native_statement_list = 105
    RULE_native_statement = 106
    RULE_python_native_statement = 107
    RULE_javascript_native_statement = 108
    RULE_statement_list = 109
    RULE_switch_case_statement_list = 110
    RULE_catch_statement_list = 111
    RULE_literal_collection = 112
    RULE_atomic_literal = 113
    RULE_literal_list_literal = 114
    RULE_selectable_expression = 115
    RULE_this_expression = 116
    RULE_parenthesis_expression = 117
    RULE_literal_expression = 118
    RULE_collection_literal = 119
    RULE_tuple_literal = 120
    RULE_dict_literal = 121
    RULE_expression_tuple = 122
    RULE_dict_entry_list = 123
    RULE_dict_entry = 124
    RULE_slice_arguments = 125
    RULE_assign_variable_statement = 126
    RULE_assignable_instance = 127
    RULE_is_expression = 128
    RULE_operator = 129
    RULE_key_token = 130
    RULE_value_token = 131
    RULE_symbols_token = 132
    RULE_assign = 133
    RULE_multiply = 134
    RULE_divide = 135
    RULE_idivide = 136
    RULE_modulo = 137
    RULE_javascript_statement = 138
    RULE_javascript_expression = 139
    RULE_javascript_primary_expression = 140
    RULE_javascript_selector_expression = 141
    RULE_javascript_method_expression = 142
    RULE_javascript_arguments = 143
    RULE_javascript_item_expression = 144
    RULE_javascript_parenthesis_expression = 145
    RULE_javascript_identifier_expression = 146
    RULE_javascript_literal_expression = 147
    RULE_javascript_identifier = 148
    RULE_python_statement = 149
    RULE_python_expression = 150
    RULE_python_primary_expression = 151
    RULE_python_selector_expression = 152
    RULE_python_method_expression = 153
    RULE_python_argument_list = 154
    RULE_python_ordinal_argument_list = 155
    RULE_python_named_argument_list = 156
    RULE_python_parenthesis_expression = 157
    RULE_python_identifier_expression = 158
    RULE_python_literal_expression = 159
    RULE_python_identifier = 160
    RULE_java_statement = 161
    RULE_java_expression = 162
    RULE_java_primary_expression = 163
    RULE_java_selector_expression = 164
    RULE_java_method_expression = 165
    RULE_java_arguments = 166
    RULE_java_item_expression = 167
    RULE_java_parenthesis_expression = 168
    RULE_java_identifier_expression = 169
    RULE_java_class_identifier_expression = 170
    RULE_java_literal_expression = 171
    RULE_java_identifier = 172
    RULE_csharp_statement = 173
    RULE_csharp_expression = 174
    RULE_csharp_primary_expression = 175
    RULE_csharp_selector_expression = 176
    RULE_csharp_method_expression = 177
    RULE_csharp_arguments = 178
    RULE_csharp_item_expression = 179
    RULE_csharp_parenthesis_expression = 180
    RULE_csharp_identifier_expression = 181
    RULE_csharp_literal_expression = 182
    RULE_csharp_identifier = 183

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"member_method_declaration", u"operator_method_declaration", 
                   u"setter_method_declaration", u"getter_method_declaration", 
                   u"native_category_declaration", u"native_resource_declaration", 
                   u"native_category_mappings", u"native_category_mapping_list", 
                   u"attribute_list", u"abstract_method_declaration", u"concrete_method_declaration", 
                   u"native_method_declaration", u"full_argument_list", 
                   u"typed_argument", u"statement", u"method_call_statement", 
                   u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"return_statement", u"expression", 
                   u"unresolved_expression", u"unresolved_selector", u"invocation_expression", 
                   u"invocation_trailer", u"instance_expression", u"instance_selector", 
                   u"document_expression", u"constructor_expression", u"read_expression", 
                   u"write_statement", u"ambiguous_expression", u"fetch_expression", 
                   u"sorted_expression", u"argument_assignment_list", u"with_argument_assignment_list", 
                   u"argument_assignment", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"lfs", 
                   u"lfp", u"indent", u"dedent", u"null_literal", u"declaration_list", 
                   u"declarations", u"declaration", u"resource_declaration", 
                   u"enum_declaration", u"native_symbol_list", u"category_symbol_list", 
                   u"symbol_list", u"attribute_constraint", u"list_literal", 
                   u"set_literal", u"expression_list", u"range_literal", 
                   u"typedef", u"primary_type", u"native_type", u"category_type", 
                   u"code_type", u"document_type", u"category_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"type_identifier", u"symbol_identifier", 
                   u"argument_list", u"argument", u"operator_argument", 
                   u"named_argument", u"code_argument", u"category_or_any_type", 
                   u"any_type", u"category_method_declaration_list", u"category_method_declaration", 
                   u"native_category_mapping", u"python_category_mapping", 
                   u"python_module", u"module_token", u"javascript_category_mapping", 
                   u"javascript_module", u"variable_identifier_list", u"method_declaration", 
                   u"native_statement_list", u"native_statement", u"python_native_statement", 
                   u"javascript_native_statement", u"statement_list", u"switch_case_statement_list", 
                   u"catch_statement_list", u"literal_collection", u"atomic_literal", 
                   u"literal_list_literal", u"selectable_expression", u"this_expression", 
                   u"parenthesis_expression", u"literal_expression", u"collection_literal", 
                   u"tuple_literal", u"dict_literal", u"expression_tuple", 
                   u"dict_entry_list", u"dict_entry", u"slice_arguments", 
                   u"assign_variable_statement", u"assignable_instance", 
                   u"is_expression", u"operator", u"key_token", u"value_token", 
                   u"symbols_token", u"assign", u"multiply", u"divide", 
                   u"idivide", u"modulo", u"javascript_statement", u"javascript_expression", 
                   u"javascript_primary_expression", u"javascript_selector_expression", 
                   u"javascript_method_expression", u"javascript_arguments", 
                   u"javascript_item_expression", u"javascript_parenthesis_expression", 
                   u"javascript_identifier_expression", u"javascript_literal_expression", 
                   u"javascript_identifier", u"python_statement", u"python_expression", 
                   u"python_primary_expression", u"python_selector_expression", 
                   u"python_method_expression", u"python_argument_list", 
                   u"python_ordinal_argument_list", u"python_named_argument_list", 
                   u"python_parenthesis_expression", u"python_identifier_expression", 
                   u"python_literal_expression", u"python_identifier", u"java_statement", 
                   u"java_expression", u"java_primary_expression", u"java_selector_expression", 
                   u"java_method_expression", u"java_arguments", u"java_item_expression", 
                   u"java_parenthesis_expression", u"java_identifier_expression", 
                   u"java_class_identifier_expression", u"java_literal_expression", 
                   u"java_identifier", u"csharp_statement", u"csharp_expression", 
                   u"csharp_primary_expression", u"csharp_selector_expression", 
                   u"csharp_method_expression", u"csharp_arguments", u"csharp_item_expression", 
                   u"csharp_parenthesis_expression", u"csharp_identifier_expression", 
                   u"csharp_literal_expression", u"csharp_identifier" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    LF_TAB=3
    LF_MORE=4
    LF=5
    TAB=6
    WS=7
    JAVA=8
    CSHARP=9
    PYTHON2=10
    PYTHON3=11
    JAVASCRIPT=12
    SWIFT=13
    COLON=14
    SEMI=15
    COMMA=16
    RANGE=17
    DOT=18
    LPAR=19
    RPAR=20
    LBRAK=21
    RBRAK=22
    LCURL=23
    RCURL=24
    QMARK=25
    XMARK=26
    DOLLAR=27
    AMP=28
    AMP2=29
    PIPE=30
    PIPE2=31
    PLUS=32
    MINUS=33
    STAR=34
    SLASH=35
    BSLASH=36
    PERCENT=37
    GT=38
    GTE=39
    LT=40
    LTE=41
    LTGT=42
    EQ=43
    XEQ=44
    EQ2=45
    TEQ=46
    TILDE=47
    LARROW=48
    RARROW=49
    BOOLEAN=50
    CHARACTER=51
    TEXT=52
    INTEGER=53
    DECIMAL=54
    DATE=55
    TIME=56
    DATETIME=57
    PERIOD=58
    METHOD_T=59
    CODE=60
    DOCUMENT=61
    ABSTRACT=62
    ALL=63
    ALWAYS=64
    AND=65
    ANY=66
    AS=67
    ATTR=68
    ATTRIBUTE=69
    ATTRIBUTES=70
    CASE=71
    CATCH=72
    CATEGORY=73
    CLASS=74
    CLOSE=75
    CONTAINS=76
    DEF=77
    DEFAULT=78
    DEFINE=79
    DO=80
    DOING=81
    EACH=82
    ELSE=83
    ENUM=84
    ENUMERATED=85
    EXCEPT=86
    EXECUTE=87
    EXTENDS=88
    FETCH=89
    FINALLY=90
    FOR=91
    FROM=92
    GETTER=93
    IF=94
    IN=95
    INVOKE=96
    IS=97
    MAPPINGS=98
    MATCHING=99
    METHOD=100
    METHODS=101
    MODULO=102
    NATIVE=103
    NONE=104
    NOT=105
    NOTHING=106
    NULL=107
    ON=108
    OPEN=109
    OPERATOR=110
    OR=111
    OTHERWISE=112
    PASS=113
    RAISE=114
    READ=115
    RECEIVING=116
    RESOURCE=117
    RETURN=118
    RETURNING=119
    SELF=120
    SETTER=121
    SINGLETON=122
    SORTED=123
    SWITCH=124
    THIS=125
    THROW=126
    TO=127
    TRY=128
    WITH=129
    WHEN=130
    WHERE=131
    WHILE=132
    WRITE=133
    BOOLEAN_LITERAL=134
    CHAR_LITERAL=135
    MIN_INTEGER=136
    MAX_INTEGER=137
    SYMBOL_IDENTIFIER=138
    TYPE_IDENTIFIER=139
    VARIABLE_IDENTIFIER=140
    TEXT_LITERAL=141
    INTEGER_LITERAL=142
    HEXA_LITERAL=143
    DECIMAL_LITERAL=144
    DATETIME_LITERAL=145
    TIME_LITERAL=146
    DATE_LITERAL=147
    PERIOD_LITERAL=148
    COMMENT=149

    def __init__(self, input):
        super(EParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.symbols = None # Category_symbol_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(EParser.Category_symbol_listContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = EParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(EParser.DEFINE)
            self.state = 369 
            localctx.name = self.type_identifier()
            self.state = 370
            self.match(EParser.AS)
            self.state = 371
            self.match(EParser.COLON)
            self.state = 372
            self.match(EParser.ENUMERATED)
            self.state = 375
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 373
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 374 
                localctx.derived = self.type_identifier()

            else:
                raise NoViableAltException(self)

            self.state = 380
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 377 
                localctx.attrs = self.attribute_list()
                self.state = 378
                self.match(EParser.COMMA)


            self.state = 382
            self.match(EParser.WITH)
            self.state = 383 
            self.symbols_token()
            self.state = 384
            self.match(EParser.COLON)
            self.state = 385 
            self.indent()
            self.state = 386 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 387 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_native_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(EParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(EParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = EParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(EParser.DEFINE)
            self.state = 390 
            localctx.name = self.type_identifier()
            self.state = 391
            self.match(EParser.AS)
            self.state = 392
            self.match(EParser.COLON)
            self.state = 393
            self.match(EParser.ENUMERATED)
            self.state = 394 
            localctx.typ = self.native_type()
            self.state = 395
            self.match(EParser.WITH)
            self.state = 396 
            self.symbols_token()
            self.state = 397
            self.match(EParser.COLON)
            self.state = 398 
            self.indent()
            self.state = 399 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 400 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def value_token(self):
            return self.getTypedRuleContext(EParser.Value_tokenContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_symbol

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = EParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402 
            localctx.name = self.symbol_identifier()
            self.state = 403
            self.match(EParser.WITH)
            self.state = 404 
            localctx.exp = self.expression(0)
            self.state = 405
            self.match(EParser.AS)
            self.state = 406 
            self.value_token()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_category_symbol

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = EParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408 
            localctx.name = self.symbol_identifier()
            self.state = 409 
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 412
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 410
                self.match(EParser.AND)
                self.state = 411 
                localctx.arg = self.argument_assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def attribute_constraint(self):
            return self.getTypedRuleContext(EParser.Attribute_constraintContext,0)


        def getRuleIndex(self):
            return EParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = EParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(EParser.DEFINE)
            self.state = 415 
            localctx.name = self.variable_identifier()
            self.state = 416
            self.match(EParser.AS)
            self.state = 417
            self.match(EParser.COLON)
            self.state = 418 
            localctx.typ = self.typedef(0)
            self.state = 419
            self.match(EParser.ATTRIBUTE)
            self.state = 421
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 420 
                localctx.match = self.attribute_constraint()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Category_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def derived_list(self):
            return self.getTypedRuleContext(EParser.Derived_listContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def category_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Category_method_declaration_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = EParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(EParser.DEFINE)
            self.state = 424 
            localctx.name = self.type_identifier()
            self.state = 425
            self.match(EParser.AS)
            self.state = 426
            self.match(EParser.COLON)
            self.state = 429
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 427
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 428 
                localctx.derived = self.derived_list()

            else:
                raise NoViableAltException(self)

            self.state = 449
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 431 
                localctx.attrs = self.attribute_list()
                self.state = 440
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 432
                    self.match(EParser.COMMA)
                    self.state = 433
                    self.match(EParser.AND)
                    self.state = 434
                    self.match(EParser.METHODS)
                    self.state = 435
                    self.match(EParser.COLON)
                    self.state = 436 
                    self.indent()
                    self.state = 437 
                    localctx.methods = self.category_method_declaration_list(0)
                    self.state = 438 
                    self.dedent()



            elif la_ == 2:
                self.state = 442
                self.match(EParser.WITH)
                self.state = 443
                self.match(EParser.METHODS)
                self.state = 444
                self.match(EParser.COLON)
                self.state = 445 
                self.indent()
                self.state = 446 
                localctx.methods = self.category_method_declaration_list(0)
                self.state = 447 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Singleton_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Category_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def SINGLETON(self):
            return self.getToken(EParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def category_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Category_method_declaration_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = EParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(EParser.DEFINE)
            self.state = 452 
            localctx.name = self.type_identifier()
            self.state = 453
            self.match(EParser.AS)
            self.state = 454
            self.match(EParser.COLON)
            self.state = 455
            self.match(EParser.SINGLETON)
            self.state = 474
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 456 
                localctx.attrs = self.attribute_list()
                self.state = 465
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 457
                    self.match(EParser.COMMA)
                    self.state = 458
                    self.match(EParser.AND)
                    self.state = 459
                    self.match(EParser.METHODS)
                    self.state = 460
                    self.match(EParser.COLON)
                    self.state = 461 
                    self.indent()
                    self.state = 462 
                    localctx.methods = self.category_method_declaration_list(0)
                    self.state = 463 
                    self.dedent()



            elif la_ == 2:
                self.state = 467
                self.match(EParser.WITH)
                self.state = 468
                self.match(EParser.METHODS)
                self.state = 469
                self.match(EParser.COLON)
                self.state = 470 
                self.indent()
                self.state = 471 
                localctx.methods = self.category_method_declaration_list(0)
                self.state = 472 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_derived_list

     
        def copyFrom(self, ctx):
            super(EParser.Derived_listContext, self).copyFrom(ctx)



    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.copyFrom(ctx)

        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDerivedList(self)


    class DerivedListItemContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDerivedListItem(self)



    def derived_list(self):

        localctx = EParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.state = 481
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 476 
                localctx.items = self.type_identifier_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 477 
                localctx.items = self.type_identifier_list(0)
                self.state = 478
                self.match(EParser.AND)
                self.state = 479 
                localctx.item = self.type_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = EParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_member_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(EParser.DEFINE)
            self.state = 484 
            localctx.name = self.method_identifier()
            self.state = 485
            self.match(EParser.AS)
            self.state = 486
            self.match(EParser.COLON)
            self.state = 487
            self.match(EParser.METHOD)
            self.state = 491
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 488
                self.match(EParser.RECEIVING)
                self.state = 489
                self.match(EParser.COLON)
                self.state = 490 
                localctx.args = self.full_argument_list()


            self.state = 496
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 493
                self.match(EParser.RETURNING)
                self.state = 494
                self.match(EParser.COLON)
                self.state = 495 
                localctx.typ = self.typedef(0)


            self.state = 498
            self.match(EParser.DOING)
            self.state = 499
            self.match(EParser.COLON)
            self.state = 500 
            self.indent()
            self.state = 501 
            localctx.stmts = self.statement_list(0)
            self.state = 502 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def OPERATOR(self):
            return self.getToken(EParser.OPERATOR, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(EParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(EParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = EParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(EParser.DEFINE)
            self.state = 505 
            localctx.op = self.operator()
            self.state = 506
            self.match(EParser.AS)
            self.state = 507
            self.match(EParser.COLON)
            self.state = 508
            self.match(EParser.OPERATOR)
            self.state = 509
            self.match(EParser.RECEIVING)
            self.state = 510
            self.match(EParser.COLON)
            self.state = 511 
            localctx.arg = self.operator_argument()
            self.state = 515
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 512
                self.match(EParser.RETURNING)
                self.state = 513
                self.match(EParser.COLON)
                self.state = 514 
                localctx.typ = self.typedef(0)


            self.state = 517
            self.match(EParser.DOING)
            self.state = 518
            self.match(EParser.COLON)
            self.state = 519 
            self.indent()
            self.state = 520 
            localctx.stmts = self.statement_list(0)
            self.state = 521 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def SETTER(self):
            return self.getToken(EParser.SETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = EParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(EParser.DEFINE)
            self.state = 524 
            localctx.name = self.variable_identifier()
            self.state = 525
            self.match(EParser.SETTER)
            self.state = 526
            self.match(EParser.DOING)
            self.state = 527
            self.match(EParser.COLON)
            self.state = 528 
            self.indent()
            self.state = 529 
            localctx.stmts = self.statement_list(0)
            self.state = 530 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def GETTER(self):
            return self.getToken(EParser.GETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = EParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(EParser.DEFINE)
            self.state = 533 
            localctx.name = self.variable_identifier()
            self.state = 534
            self.match(EParser.GETTER)
            self.state = 535
            self.match(EParser.DOING)
            self.state = 536
            self.match(EParser.COLON)
            self.state = 537 
            self.indent()
            self.state = 538 
            localctx.stmts = self.statement_list(0)
            self.state = 539 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.mappings = None # Native_category_mappingsContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def MAPPINGS(self):
            return self.getToken(EParser.MAPPINGS, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def native_category_mappings(self):
            return self.getTypedRuleContext(EParser.Native_category_mappingsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = EParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(EParser.DEFINE)
            self.state = 542 
            localctx.name = self.type_identifier()
            self.state = 543
            self.match(EParser.AS)
            self.state = 544
            self.match(EParser.COLON)
            self.state = 545
            self.match(EParser.NATIVE)
            self.state = 546
            self.match(EParser.CATEGORY)
            self.state = 547 
            localctx.attrs = self.attribute_list()
            self.state = 548
            self.match(EParser.COMMA)
            self.state = 549
            self.match(EParser.AND)
            self.state = 550
            self.match(EParser.MAPPINGS)
            self.state = 551
            self.match(EParser.COLON)
            self.state = 552 
            self.indent()
            self.state = 553 
            localctx.mappings = self.native_category_mappings()
            self.state = 554 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.mappings = None # Native_category_mappingsContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(EParser.RESOURCE, 0)

        def MAPPINGS(self):
            return self.getToken(EParser.MAPPINGS, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_mappings(self):
            return self.getTypedRuleContext(EParser.Native_category_mappingsContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = EParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(EParser.DEFINE)
            self.state = 557 
            localctx.name = self.type_identifier()
            self.state = 558
            self.match(EParser.AS)
            self.state = 559
            self.match(EParser.COLON)
            self.state = 560
            self.match(EParser.NATIVE)
            self.state = 561
            self.match(EParser.RESOURCE)
            self.state = 566
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 562 
                localctx.attrs = self.attribute_list()
                self.state = 563
                self.match(EParser.COMMA)
                self.state = 564
                self.match(EParser.AND)


            self.state = 568
            self.match(EParser.MAPPINGS)
            self.state = 569
            self.match(EParser.COLON)
            self.state = 570 
            self.indent()
            self.state = 571 
            localctx.mappings = self.native_category_mappings()
            self.state = 572 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_mappingsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_mappingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_mapping_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def MAPPINGS(self):
            return self.getToken(EParser.MAPPINGS, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def native_category_mapping_list(self):
            return self.getTypedRuleContext(EParser.Native_category_mapping_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_mappings

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_mappings(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_mappings(self)




    def native_category_mappings(self):

        localctx = EParser.Native_category_mappingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_category_mappings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(EParser.DEFINE)
            self.state = 575
            self.match(EParser.CATEGORY)
            self.state = 576
            self.match(EParser.MAPPINGS)
            self.state = 577
            self.match(EParser.AS)
            self.state = 578
            self.match(EParser.COLON)
            self.state = 579 
            self.indent()
            self.state = 580 
            localctx.items = self.native_category_mapping_list(0)
            self.state = 581 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_mapping_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_mapping_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_mapping_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_mapping_listContext, self).copyFrom(ctx)


    class NativeCategoryMappingListContext(Native_category_mapping_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mapping_listContext)
            super(EParser.NativeCategoryMappingListContext, self).__init__(parser)
            self.item = None # Native_category_mappingContext
            self.copyFrom(ctx)

        def native_category_mapping(self):
            return self.getTypedRuleContext(EParser.Native_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryMappingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryMappingList(self)


    class NativeCategoryMappingListItemContext(Native_category_mapping_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mapping_listContext)
            super(EParser.NativeCategoryMappingListItemContext, self).__init__(parser)
            self.items = None # Native_category_mapping_listContext
            self.item = None # Native_category_mappingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_category_mapping_list(self):
            return self.getTypedRuleContext(EParser.Native_category_mapping_listContext,0)

        def native_category_mapping(self):
            return self.getTypedRuleContext(EParser.Native_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryMappingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryMappingListItem(self)



    def native_category_mapping_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_category_mapping_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_native_category_mapping_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryMappingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 584 
            localctx.item = self.native_category_mapping()
            self._ctx.stop = self._input.LT(-1)
            self.state = 592
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryMappingListItemContext(self, EParser.Native_category_mapping_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_mapping_list)
                    self.state = 586
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 587 
                    self.lfp()
                    self.state = 588 
                    localctx.item = self.native_category_mapping() 
                self.state = 594
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_list

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_listContext, self).copyFrom(ctx)



    class AttributeListItemContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTES(self):
            return self.getToken(EParser.ATTRIBUTES, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeListItem(self)


    class AttributeListContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeList(self)



    def attribute_list(self):

        localctx = EParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attribute_list)
        try:
            self.state = 607
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(EParser.WITH)
                self.state = 596
                self.match(EParser.ATTRIBUTE)
                self.state = 597
                self.match(EParser.COLON)
                self.state = 598 
                localctx.item = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.match(EParser.WITH)
                self.state = 600
                self.match(EParser.ATTRIBUTES)
                self.state = 601
                self.match(EParser.COLON)
                self.state = 602 
                localctx.items = self.variable_identifier_list(0)
                self.state = 605
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 603
                    self.match(EParser.AND)
                    self.state = 604 
                    localctx.item = self.variable_identifier()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def ABSTRACT(self):
            return self.getToken(EParser.ABSTRACT, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = EParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_abstract_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(EParser.DEFINE)
            self.state = 610 
            localctx.name = self.method_identifier()
            self.state = 611
            self.match(EParser.AS)
            self.state = 612
            self.match(EParser.COLON)
            self.state = 613
            self.match(EParser.ABSTRACT)
            self.state = 614
            self.match(EParser.METHOD)
            self.state = 618
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 615
                self.match(EParser.RECEIVING)
                self.state = 616
                self.match(EParser.COLON)
                self.state = 617 
                localctx.args = self.full_argument_list()


            self.state = 623
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 620
                self.match(EParser.RETURNING)
                self.state = 621
                self.match(EParser.COLON)
                self.state = 622 
                localctx.typ = self.typedef(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = EParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.match(EParser.DEFINE)
            self.state = 626 
            localctx.name = self.method_identifier()
            self.state = 627
            self.match(EParser.AS)
            self.state = 628
            self.match(EParser.COLON)
            self.state = 629
            self.match(EParser.METHOD)
            self.state = 633
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 630
                self.match(EParser.RECEIVING)
                self.state = 631
                self.match(EParser.COLON)
                self.state = 632 
                localctx.args = self.full_argument_list()


            self.state = 638
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 635
                self.match(EParser.RETURNING)
                self.state = 636
                self.match(EParser.COLON)
                self.state = 637 
                localctx.typ = self.typedef(0)


            self.state = 640
            self.match(EParser.DOING)
            self.state = 641
            self.match(EParser.COLON)
            self.state = 642 
            self.indent()
            self.state = 643 
            localctx.stmts = self.statement_list(0)
            self.state = 644 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = EParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(EParser.DEFINE)
            self.state = 647 
            localctx.name = self.method_identifier()
            self.state = 648
            self.match(EParser.AS)
            self.state = 649
            self.match(EParser.COLON)
            self.state = 650
            self.match(EParser.NATIVE)
            self.state = 651
            self.match(EParser.METHOD)
            self.state = 655
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 652
                self.match(EParser.RECEIVING)
                self.state = 653
                self.match(EParser.COLON)
                self.state = 654 
                localctx.args = self.full_argument_list()


            self.state = 660
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 657
                self.match(EParser.RETURNING)
                self.state = 658
                self.match(EParser.COLON)
                self.state = 659 
                localctx.typ = self.typedef(0)


            self.state = 662
            self.match(EParser.DOING)
            self.state = 663
            self.match(EParser.COLON)
            self.state = 664 
            self.indent()
            self.state = 665 
            localctx.stmts = self.native_statement_list(0)
            self.state = 666 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Full_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Full_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext

        def argument_list(self):
            return self.getTypedRuleContext(EParser.Argument_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_full_argument_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFull_argument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFull_argument_list(self)




    def full_argument_list(self):

        localctx = EParser.Full_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_full_argument_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668 
            localctx.items = self.argument_list(0)
            self.state = 671
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 669
                self.match(EParser.AND)
                self.state = 670 
                localctx.item = self.argument()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.name = None # Variable_identifierContext
            self.attrs = None # Attribute_listContext
            self.value = None # Literal_expressionContext

        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_typed_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = EParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673 
            localctx.typ = self.category_or_any_type()
            self.state = 674 
            localctx.name = self.variable_identifier()
            self.state = 676
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 675 
                localctx.attrs = self.attribute_list()


            self.state = 680
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 678
                self.match(EParser.EQ)
                self.state = 679 
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(EParser.StatementContext, self).copyFrom(ctx)



    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(EParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssignInstanceStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(EParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWithResourceStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(EParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssignTupleStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(EParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(EParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWhileStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitClosureStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_call_statementContext
            self.copyFrom(ctx)

        def method_call_statement(self):
            return self.getTypedRuleContext(EParser.Method_call_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodCallStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(EParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWithSingletonStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(EParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReturnStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(EParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDoWhileStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(EParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(EParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(EParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRaiseStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(EParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitForEachStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(EParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTryStatement(self)



    def statement(self):

        localctx = EParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 697
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 682 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 683 
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 684 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 685 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 5:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 686 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 6:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 687 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 7:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 688 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 8:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 689 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 9:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 690 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 10:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 691 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 11:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 692 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 12:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 693 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 13:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 694 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 14:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 695 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 15:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 696 
                localctx.decl = self.concrete_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_call_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_call_statement

     
        def copyFrom(self, ctx):
            super(EParser.Method_call_statementContext, self).copyFrom(ctx)



    class UnresolvedWithArgsStatementContext(Method_call_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_call_statementContext)
            super(EParser.UnresolvedWithArgsStatementContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedWithArgsStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedWithArgsStatement(self)


    class InvokeStatementContext(Method_call_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_call_statementContext)
            super(EParser.InvokeStatementContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvokeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvokeStatement(self)



    def method_call_statement(self):

        localctx = EParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_call_statement)
        try:
            self.state = 704
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 699 
                localctx.exp = self.unresolved_expression(0)
                self.state = 701
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 700 
                    localctx.args = self.argument_assignment_list()



            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 703 
                localctx.exp = self.invocation_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_resource_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(EParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = EParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(EParser.WITH)
            self.state = 707 
            localctx.stmt = self.assign_variable_statement()
            self.state = 708
            self.match(EParser.COMMA)
            self.state = 709
            self.match(EParser.DO)
            self.state = 710
            self.match(EParser.COLON)
            self.state = 711 
            self.indent()
            self.state = 712 
            localctx.stmts = self.statement_list(0)
            self.state = 713 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_singleton_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = EParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
            self.match(EParser.WITH)
            self.state = 716 
            localctx.typ = self.type_identifier()
            self.state = 717
            self.match(EParser.COMMA)
            self.state = 718
            self.match(EParser.DO)
            self.state = 719
            self.match(EParser.COLON)
            self.state = 720 
            self.indent()
            self.state = 721 
            localctx.stmts = self.statement_list(0)
            self.state = 722 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(EParser.SWITCH, 0)

        def ON(self):
            return self.getToken(EParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(EParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(EParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_switch_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = EParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(EParser.SWITCH)
            self.state = 725
            self.match(EParser.ON)
            self.state = 726 
            localctx.exp = self.expression(0)
            self.state = 727
            self.match(EParser.COLON)
            self.state = 728 
            self.indent()
            self.state = 729 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 737
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 730 
                self.lfp()
                self.state = 731
                self.match(EParser.OTHERWISE)
                self.state = 732
                self.match(EParser.COLON)
                self.state = 733 
                self.indent()
                self.state = 734 
                localctx.stmts = self.statement_list(0)
                self.state = 735 
                self.dedent()


            self.state = 739 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(EParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statementContext)
            super(EParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statementContext)
            super(EParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(EParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = EParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_switch_case_statement)
        try:
            self.state = 756
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 741
                self.match(EParser.WHEN)
                self.state = 742 
                localctx.exp = self.atomic_literal()
                self.state = 743
                self.match(EParser.COLON)
                self.state = 744 
                self.indent()
                self.state = 745 
                localctx.stmts = self.statement_list(0)
                self.state = 746 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 748
                self.match(EParser.WHEN)
                self.state = 749
                self.match(EParser.IN)
                self.state = 750 
                localctx.exp = self.literal_collection()
                self.state = 751
                self.match(EParser.COLON)
                self.state = 752 
                self.indent()
                self.state = 753 
                localctx.stmts = self.statement_list(0)
                self.state = 754 
                self.dedent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_each_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(EParser.FOR, 0)

        def EACH(self):
            return self.getToken(EParser.EACH, 0)

        def IN(self):
            return self.getToken(EParser.IN, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def getRuleIndex(self):
            return EParser.RULE_for_each_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = EParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            self.match(EParser.FOR)
            self.state = 759
            self.match(EParser.EACH)
            self.state = 760 
            localctx.name1 = self.variable_identifier()
            self.state = 763
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 761
                self.match(EParser.COMMA)
                self.state = 762 
                localctx.name2 = self.variable_identifier()


            self.state = 765
            self.match(EParser.IN)
            self.state = 766 
            localctx.source = self.expression(0)
            self.state = 767
            self.match(EParser.COLON)
            self.state = 768 
            self.indent()
            self.state = 769 
            localctx.stmts = self.statement_list(0)
            self.state = 770 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(EParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_do_while_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = EParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
            self.match(EParser.DO)
            self.state = 773
            self.match(EParser.COLON)
            self.state = 774 
            self.indent()
            self.state = 775 
            localctx.stmts = self.statement_list(0)
            self.state = 776 
            self.dedent()
            self.state = 777 
            self.lfp()
            self.state = 778
            self.match(EParser.WHILE)
            self.state = 779 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(EParser.WHILE, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_while_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = EParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 781
            self.match(EParser.WHILE)
            self.state = 782 
            localctx.exp = self.expression(0)
            self.state = 783
            self.match(EParser.COLON)
            self.state = 784 
            self.indent()
            self.state = 785 
            localctx.stmts = self.statement_list(0)
            self.state = 786 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(EParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(EParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(EParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_if_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = EParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 788
            self.match(EParser.IF)
            self.state = 789 
            localctx.exp = self.expression(0)
            self.state = 790
            self.match(EParser.COLON)
            self.state = 791 
            self.indent()
            self.state = 792 
            localctx.stmts = self.statement_list(0)
            self.state = 793 
            self.dedent()
            self.state = 797
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 794 
                self.lfp()
                self.state = 795 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 806
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 799 
                self.lfp()
                self.state = 800
                self.match(EParser.ELSE)
                self.state = 801
                self.match(EParser.COLON)
                self.state = 802 
                self.indent()
                self.state = 803 
                localctx.elseStmts = self.statement_list(0)
                self.state = 804 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_if_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Else_if_statement_listContext)
            super(EParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def IF(self):
            return self.getToken(EParser.IF, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Else_if_statement_listContext)
            super(EParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def IF(self):
            return self.getToken(EParser.IF, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(EParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 809
            self.match(EParser.ELSE)
            self.state = 810
            self.match(EParser.IF)
            self.state = 811 
            localctx.exp = self.expression(0)
            self.state = 812
            self.match(EParser.COLON)
            self.state = 813 
            self.indent()
            self.state = 814 
            localctx.stmts = self.statement_list(0)
            self.state = 815 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 829
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 817
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 818 
                    self.lfp()
                    self.state = 819
                    self.match(EParser.ELSE)
                    self.state = 820
                    self.match(EParser.IF)
                    self.state = 821 
                    localctx.exp = self.expression(0)
                    self.state = 822
                    self.match(EParser.COLON)
                    self.state = 823 
                    self.indent()
                    self.state = 824 
                    localctx.stmts = self.statement_list(0)
                    self.state = 825 
                    self.dedent() 
                self.state = 831
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(EParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_raise_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = EParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 832
            self.match(EParser.RAISE)
            self.state = 833 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Try_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(EParser.SWITCH, 0)

        def ON(self):
            return self.getToken(EParser.ON, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfsContext)
            else:
                return self.getTypedRuleContext(EParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(EParser.Statement_listContext,i)


        def ALWAYS(self):
            return self.getToken(EParser.ALWAYS, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(EParser.Catch_statement_listContext,0)


        def OTHERWISE(self):
            return self.getToken(EParser.OTHERWISE, 0)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def getRuleIndex(self):
            return EParser.RULE_try_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = EParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 835
            self.match(EParser.SWITCH)
            self.state = 836
            self.match(EParser.ON)
            self.state = 837 
            localctx.name = self.variable_identifier()
            self.state = 838
            self.match(EParser.DOING)
            self.state = 839
            self.match(EParser.COLON)
            self.state = 840 
            self.indent()
            self.state = 841 
            localctx.stmts = self.statement_list(0)
            self.state = 842 
            self.dedent()
            self.state = 843 
            self.lfs()
            self.state = 845
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 844 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 858
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 850
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 847
                    self.match(EParser.OTHERWISE)

                elif token in [EParser.WHEN]:
                    self.state = 848
                    self.match(EParser.WHEN)
                    self.state = 849
                    self.match(EParser.ANY)

                else:
                    raise NoViableAltException(self)

                self.state = 852
                self.match(EParser.COLON)
                self.state = 853 
                self.indent()
                self.state = 854 
                localctx.anyStmts = self.statement_list(0)
                self.state = 855 
                self.dedent()
                self.state = 856 
                self.lfs()


            self.state = 867
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 860
                self.match(EParser.ALWAYS)
                self.state = 861
                self.match(EParser.COLON)
                self.state = 862 
                self.indent()
                self.state = 863 
                localctx.finalStmts = self.statement_list(0)
                self.state = 864 
                self.dedent()
                self.state = 865 
                self.lfs()


            self.state = 869 
            self.lfs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(EParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statementContext)
            super(EParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statementContext)
            super(EParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(EParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = EParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_catch_statement)
        try:
            self.state = 890
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 871
                self.match(EParser.WHEN)
                self.state = 872 
                localctx.name = self.symbol_identifier()
                self.state = 873
                self.match(EParser.COLON)
                self.state = 874 
                self.indent()
                self.state = 875 
                localctx.stmts = self.statement_list(0)
                self.state = 876 
                self.dedent()
                self.state = 877 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 879
                self.match(EParser.WHEN)
                self.state = 880
                self.match(EParser.IN)
                self.state = 881
                self.match(EParser.LBRAK)
                self.state = 882 
                localctx.exp = self.symbol_list(0)
                self.state = 883
                self.match(EParser.RBRAK)
                self.state = 884
                self.match(EParser.COLON)
                self.state = 885 
                self.indent()
                self.state = 886 
                localctx.stmts = self.statement_list(0)
                self.state = 887 
                self.dedent()
                self.state = 888 
                self.lfs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_return_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = EParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 892
            self.match(EParser.RETURN)
            self.state = 894
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 893 
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(EParser.ExpressionContext, self).copyFrom(ctx)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ClosureExpressionContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def METHOD_T(self):
            return self.getToken(EParser.METHOD_T, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitClosureExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(EParser.IF, 0)
        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTernaryExpression(self)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntDivideExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEqualsExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(EParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsAnyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(EParser.TILDE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRoughlyEqualsExpression(self)


    class SortedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(EParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSortedExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeExpression(self)


    class AmbiguousExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AmbiguousExpressionContext, self).__init__(parser)
            self.exp = None # Ambiguous_expressionContext
            self.copyFrom(ctx)

        def ambiguous_expression(self):
            return self.getTypedRuleContext(EParser.Ambiguous_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAmbiguousExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAmbiguousExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(EParser.LTGT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(EParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCastExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInstanceExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(EParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGreaterThanExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(EParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAddExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModuloExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(EParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsAllExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(EParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLessThanOrEqualExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMultiplyExpression(self)


    class MethodCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodCallExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAndExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDivideExpression(self)


    class UnresolvedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.UnresolvedExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedExpression(self)


    class ConstructorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(EParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(EParser.EXECUTE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExecuteExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsAllExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLessThanExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotInExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsAnyExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(EParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(EParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsExpression(self)


    class InvocationExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InvocationExpressionContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocationExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocationExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMinusExpression(self)


    class ReadExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(EParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReadExpression(self)


    class FetchExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FetchExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_expressionContext
            self.copyFrom(ctx)

        def fetch_expression(self):
            return self.getTypedRuleContext(EParser.Fetch_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(EParser.IS, 0)
        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(EParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsNotExpression(self)


    class DocumentExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(EParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocumentExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 922
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 897
                self.match(EParser.MINUS)
                self.state = 898 
                localctx.exp = self.expression(38)
                pass

            elif la_ == 2:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 899
                self.match(EParser.NOT)
                self.state = 900 
                localctx.exp = self.expression(37)
                pass

            elif la_ == 3:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 901
                self.match(EParser.CODE)
                self.state = 902
                self.match(EParser.COLON)
                self.state = 903 
                localctx.exp = self.expression(10)
                pass

            elif la_ == 4:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 904 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 905 
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 6:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 906 
                localctx.exp = self.unresolved_expression(0)
                self.state = 907 
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 909
                self.match(EParser.EXECUTE)
                self.state = 910
                self.match(EParser.COLON)
                self.state = 911 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 912
                self.match(EParser.METHOD_T)
                self.state = 913
                self.match(EParser.COLON)
                self.state = 914 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 915 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 10:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 916 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 11:
                localctx = EParser.FetchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 917 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 12:
                localctx = EParser.ReadExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 918 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 13:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 919 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 14:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 920 
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 15:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 921 
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1020
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1018
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 924
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 925 
                        self.multiply()
                        self.state = 926 
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 928
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 929 
                        self.divide()
                        self.state = 930 
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 932
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 933 
                        self.modulo()
                        self.state = 934 
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 936
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 937 
                        self.idivide()
                        self.state = 938 
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 940
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 941
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 942 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 943
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 944
                        self.match(EParser.LT)
                        self.state = 945 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 946
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 947
                        self.match(EParser.LTE)
                        self.state = 948 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 949
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 950
                        self.match(EParser.GT)
                        self.state = 951 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 952
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 953
                        self.match(EParser.GTE)
                        self.state = 954 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 955
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 956
                        self.match(EParser.EQ)
                        self.state = 957 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 958
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 959
                        self.match(EParser.LTGT)
                        self.state = 960 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 961
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 962
                        self.match(EParser.TILDE)
                        self.state = 963 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 13:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 964
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 965
                        self.match(EParser.OR)
                        self.state = 966 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 14:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 967
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 968
                        self.match(EParser.AND)
                        self.state = 969 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 15:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 970
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 971
                        self.match(EParser.IF)
                        self.state = 972 
                        localctx.test = self.expression(0)
                        self.state = 973
                        self.match(EParser.ELSE)
                        self.state = 974 
                        localctx.ifFalse = self.expression(21)
                        pass

                    elif la_ == 16:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 976
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 977
                        self.match(EParser.IN)
                        self.state = 978 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 17:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 979
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 980
                        self.match(EParser.CONTAINS)
                        self.state = 981 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 18:
                        localctx = EParser.ContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 982
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 983
                        self.match(EParser.CONTAINS)
                        self.state = 984
                        self.match(EParser.ALL)
                        self.state = 985 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 19:
                        localctx = EParser.ContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 986
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 987
                        self.match(EParser.CONTAINS)
                        self.state = 988
                        self.match(EParser.ANY)
                        self.state = 989 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 990
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 991
                        self.match(EParser.NOT)
                        self.state = 992
                        self.match(EParser.IN)
                        self.state = 993 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 994
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 995
                        self.match(EParser.NOT)
                        self.state = 996
                        self.match(EParser.CONTAINS)
                        self.state = 997 
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 998
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 999
                        self.match(EParser.NOT)
                        self.state = 1000
                        self.match(EParser.CONTAINS)
                        self.state = 1001
                        self.match(EParser.ALL)
                        self.state = 1002 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 23:
                        localctx = EParser.NotContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1003
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1004
                        self.match(EParser.NOT)
                        self.state = 1005
                        self.match(EParser.CONTAINS)
                        self.state = 1006
                        self.match(EParser.ANY)
                        self.state = 1007 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 24:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1008
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1009
                        self.match(EParser.IS)
                        self.state = 1010
                        self.match(EParser.NOT)
                        self.state = 1011 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 25:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1012
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1013
                        self.match(EParser.IS)
                        self.state = 1014 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1015
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1016
                        self.match(EParser.AS)
                        self.state = 1017 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1022
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Unresolved_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Unresolved_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_unresolved_expression

     
        def copyFrom(self, ctx):
            super(EParser.Unresolved_expressionContext, self).copyFrom(ctx)


    class UnresolvedSelectorContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedSelectorContext, self).__init__(parser)
            self.parent = None # Unresolved_expressionContext
            self.selector = None # Unresolved_selectorContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def unresolved_selector(self):
            return self.getTypedRuleContext(EParser.Unresolved_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedSelector(self)


    class UnresolvedIdentifierContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedIdentifierContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedIdentifier(self)



    def unresolved_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Unresolved_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1024 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1030
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1026
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1027 
                    localctx.selector = self.unresolved_selector() 
                self.state = 1032
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Unresolved_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Unresolved_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext

        def DOT(self):
            return self.getToken(EParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_unresolved_selector

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolved_selector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolved_selector(self)




    def unresolved_selector(self):

        localctx = EParser.Unresolved_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1033
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1034
            self.match(EParser.DOT)
            self.state = 1035 
            localctx.name = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Invocation_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def INVOKE(self):
            return self.getToken(EParser.INVOKE, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def invocation_trailer(self):
            return self.getTypedRuleContext(EParser.Invocation_trailerContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_invocation_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocation_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocation_expression(self)




    def invocation_expression(self):

        localctx = EParser.Invocation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1037
            self.match(EParser.INVOKE)
            self.state = 1038
            self.match(EParser.COLON)
            self.state = 1039 
            localctx.name = self.variable_identifier()
            self.state = 1040 
            self.invocation_trailer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_trailerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Invocation_trailerContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_invocation_trailer

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocation_trailer(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocation_trailer(self)




    def invocation_trailer(self):

        localctx = EParser.Invocation_trailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1042
            if not self.willBe(EParser.LF):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBe(EParser.LF)")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(EParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(EParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSelectableExpression(self)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(EParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSelectorExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1045 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1051
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1047
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1048 
                    localctx.selector = self.instance_selector() 
                self.state = 1053
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Instance_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(EParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(EParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = EParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_instance_selector)
        try:
            self.state = 1067
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1054
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1055
                self.match(EParser.DOT)
                self.state = 1056 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1057
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1058
                self.match(EParser.LBRAK)
                self.state = 1059 
                localctx.xslice = self.slice_arguments()
                self.state = 1060
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1062
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1063
                self.match(EParser.LBRAK)
                self.state = 1064 
                localctx.exp = self.expression(0)
                self.state = 1065
                self.match(EParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def document_type(self):
            return self.getTypedRuleContext(EParser.Document_typeContext,0)


        def getRuleIndex(self):
            return EParser.RULE_document_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = EParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1069 
            self.document_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(EParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Category_typeContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorNoFrom(self)


    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Category_typeContext
            self.firstArg = None # ExpressionContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)
        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorFrom(self)



    def constructor_expression(self):

        localctx = EParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1092
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1071 
                localctx.typ = self.category_type()
                self.state = 1072
                self.match(EParser.FROM)
                self.state = 1073 
                localctx.firstArg = self.expression(0)
                self.state = 1082
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 1075
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1074
                        self.match(EParser.COMMA)


                    self.state = 1077 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1080
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        self.state = 1078
                        self.match(EParser.AND)
                        self.state = 1079 
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1084 
                localctx.typ = self.category_type()
                self.state = 1090
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 1085 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1088
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        self.state = 1086
                        self.match(EParser.AND)
                        self.state = 1087 
                        localctx.arg = self.argument_assignment()




                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = EParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1094
            self.match(EParser.READ)
            self.state = 1095
            self.match(EParser.FROM)
            self.state = 1096 
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TO(self):
            return self.getToken(EParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_write_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = EParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1098
            self.match(EParser.WRITE)
            self.state = 1099 
            localctx.what = self.expression(0)
            self.state = 1100
            self.match(EParser.TO)
            self.state = 1101 
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ambiguous_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Ambiguous_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Unresolved_expressionContext
            self.exp = None # ExpressionContext

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_ambiguous_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAmbiguous_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAmbiguous_expression(self)




    def ambiguous_expression(self):

        localctx = EParser.Ambiguous_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1103 
            localctx.method = self.unresolved_expression(0)
            self.state = 1104
            self.match(EParser.MINUS)
            self.state = 1105 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Fetch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_fetch_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetch_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetch_expression(self)




    def fetch_expression(self):

        localctx = EParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_fetch_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1107
            self.match(EParser.FETCH)
            self.state = 1108
            self.match(EParser.ANY)
            self.state = 1109 
            localctx.name = self.variable_identifier()
            self.state = 1110
            self.match(EParser.FROM)
            self.state = 1111 
            localctx.source = self.expression(0)
            self.state = 1112
            self.match(EParser.WHERE)
            self.state = 1113 
            localctx.xfilter = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sorted_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(EParser.SORTED, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(EParser.Instance_expressionContext,i)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def key_token(self):
            return self.getTypedRuleContext(EParser.Key_tokenContext,0)


        def getRuleIndex(self):
            return EParser.RULE_sorted_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = EParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_sorted_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1115
            self.match(EParser.SORTED)
            self.state = 1116 
            localctx.source = self.instance_expression(0)
            self.state = 1122
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 1117
                self.match(EParser.WITH)
                self.state = 1118 
                localctx.key = self.instance_expression(0)
                self.state = 1119
                self.match(EParser.AS)
                self.state = 1120 
                self.key_token()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(EParser.Argument_assignment_listContext, self).copyFrom(ctx)



    class ArgumentAssignmentListExpressionContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListExpression(self)


    class ArgumentAssignmentListNoExpressionContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListNoExpressionContext, self).__init__(parser)
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListNoExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListNoExpression(self)



    def argument_assignment_list(self):

        localctx = EParser.Argument_assignment_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_argument_assignment_list)
        try:
            self.state = 1138
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1124
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1125 
                localctx.exp = self.expression(0)
                self.state = 1131
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 1126 
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1129
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        self.state = 1127
                        self.match(EParser.AND)
                        self.state = 1128 
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1133 
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1136
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 1134
                    self.match(EParser.AND)
                    self.state = 1135 
                    localctx.item = self.argument_assignment()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_with_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(EParser.With_argument_assignment_listContext, self).copyFrom(ctx)


    class ArgumentAssignmentListContext(With_argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.With_argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(With_argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.With_argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def with_argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.With_argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1141
            self.match(EParser.WITH)
            self.state = 1142 
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1144
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1145
                    self.match(EParser.COMMA)
                    self.state = 1146 
                    localctx.item = self.argument_assignment() 
                self.state = 1151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = EParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152 
            localctx.exp = self.expression(0)
            self.state = 1153
            self.match(EParser.AS)
            self.state = 1154 
            localctx.name = self.variable_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = EParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156 
            localctx.inst = self.assignable_instance(0)
            self.state = 1157 
            self.assign()
            self.state = 1158 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Child_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(EParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Child_instanceContext)
            super(EParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Child_instanceContext)
            super(EParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = EParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_child_instance)
        try:
            self.state = 1168
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1160
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1161
                self.match(EParser.DOT)
                self.state = 1162 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1163
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1164
                self.match(EParser.LBRAK)
                self.state = 1165 
                localctx.exp = self.expression(0)
                self.state = 1166
                self.match(EParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_tuple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = EParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1170 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1171 
            self.assign()
            self.state = 1172 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_lfs

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = EParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1174
                    self.match(EParser.LF) 
                self.state = 1179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_lfp

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = EParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1180
                self.match(EParser.LF)
                self.state = 1183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(EParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_indent

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = EParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1185
                self.match(EParser.LF)
                self.state = 1188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1190
            self.match(EParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(EParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_dedent

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = EParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1192
                self.match(EParser.LF)
                self.state = 1197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1198
            self.match(EParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NOTHING(self):
            return self.getToken(EParser.NOTHING, 0)

        def getRuleIndex(self):
            return EParser.RULE_null_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = EParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1200
            self.match(EParser.NOTHING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Declaration_listContext)
            super(EParser.FullDeclarationListContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def EOF(self):
            return self.getToken(EParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(EParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = EParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1203
            _la = self._input.LA(1)
            if _la==EParser.DEFINE:
                self.state = 1202 
                localctx.items = self.declarations(0)


            self.state = 1205 
            self.lfs()
            self.state = 1206
            self.match(EParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declarations

     
        def copyFrom(self, ctx):
            super(EParser.DeclarationsContext, self).copyFrom(ctx)


    class DeclarationListContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationsContext)
            super(EParser.DeclarationListContext, self).__init__(parser)
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(EParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclarationList(self)


    class DeclarationListItemContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationsContext)
            super(EParser.DeclarationListItemContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def declarations(self):
            return self.getTypedRuleContext(EParser.DeclarationsContext,0)

        def declaration(self):
            return self.getTypedRuleContext(EParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclarationListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclarationListItem(self)



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1209 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DeclarationListItemContext(self, EParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1211
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1212 
                    self.lfp()
                    self.state = 1213 
                    localctx.item = self.declaration() 
                self.state = 1219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declaration

     
        def copyFrom(self, ctx):
            super(EParser.DeclarationContext, self).copyFrom(ctx)



    class CategoryDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.CategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Category_declarationContext
            self.copyFrom(ctx)

        def category_declaration(self):
            return self.getTypedRuleContext(EParser.Category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryDeclaration(self)


    class ResourceDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.ResourceDeclarationContext, self).__init__(parser)
            self.decl = None # Resource_declarationContext
            self.copyFrom(ctx)

        def resource_declaration(self):
            return self.getTypedRuleContext(EParser.Resource_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterResourceDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitResourceDeclaration(self)


    class AttributeDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.AttributeDeclarationContext, self).__init__(parser)
            self.decl = None # Attribute_declarationContext
            self.copyFrom(ctx)

        def attribute_declaration(self):
            return self.getTypedRuleContext(EParser.Attribute_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeDeclaration(self)


    class MethodDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.MethodDeclarationContext, self).__init__(parser)
            self.decl = None # Method_declarationContext
            self.copyFrom(ctx)

        def method_declaration(self):
            return self.getTypedRuleContext(EParser.Method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodDeclaration(self)


    class EnumDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.EnumDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_declarationContext
            self.copyFrom(ctx)

        def enum_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnumDeclaration(self)



    def declaration(self):

        localctx = EParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_declaration)
        try:
            self.state = 1225
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1220 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1221 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1222 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1223 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = EParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1224 
                localctx.decl = self.method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.decl = None # Native_resource_declarationContext

        def native_resource_declaration(self):
            return self.getTypedRuleContext(EParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = EParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1227 
            localctx.decl = self.native_resource_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_enum_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Enum_declarationContext, self).copyFrom(ctx)



    class EnumNativeDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Enum_declarationContext)
            super(EParser.EnumNativeDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_native_declarationContext
            self.copyFrom(ctx)

        def enum_native_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_native_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnumNativeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnumNativeDeclaration(self)


    class EnumCategoryDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Enum_declarationContext)
            super(EParser.EnumCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_category_declarationContext
            self.copyFrom(ctx)

        def enum_category_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnumCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnumCategoryDeclaration(self)



    def enum_declaration(self):

        localctx = EParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_enum_declaration)
        try:
            self.state = 1231
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                localctx = EParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1229 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1230 
                localctx.decl = self.enum_native_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_symbol_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_symbol_listContext, self).copyFrom(ctx)


    class NativeSymbolListContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_symbol_listContext)
            super(EParser.NativeSymbolListContext, self).__init__(parser)
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def native_symbol(self):
            return self.getTypedRuleContext(EParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeSymbolList(self)


    class NativeSymbolListItemContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_symbol_listContext)
            super(EParser.NativeSymbolListItemContext, self).__init__(parser)
            self.items = None # Native_symbol_listContext
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_symbol_list(self):
            return self.getTypedRuleContext(EParser.Native_symbol_listContext,0)

        def native_symbol(self):
            return self.getTypedRuleContext(EParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeSymbolListItem(self)



    def native_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1234 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeSymbolListItemContext(self, EParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1236
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1237 
                    self.lfp()
                    self.state = 1238 
                    localctx.item = self.native_symbol() 
                self.state = 1244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_symbol_list

     
        def copyFrom(self, ctx):
            super(EParser.Category_symbol_listContext, self).copyFrom(ctx)


    class CategorySymbolListItemContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_symbol_listContext)
            super(EParser.CategorySymbolListItemContext, self).__init__(parser)
            self.items = None # Category_symbol_listContext
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def category_symbol_list(self):
            return self.getTypedRuleContext(EParser.Category_symbol_listContext,0)

        def category_symbol(self):
            return self.getTypedRuleContext(EParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategorySymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategorySymbolListItem(self)


    class CategorySymbolListContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_symbol_listContext)
            super(EParser.CategorySymbolListContext, self).__init__(parser)
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def category_symbol(self):
            return self.getTypedRuleContext(EParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategorySymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategorySymbolList(self)



    def category_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Category_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1246 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategorySymbolListItemContext(self, EParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1248
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1249 
                    self.lfp()
                    self.state = 1250 
                    localctx.item = self.category_symbol() 
                self.state = 1256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_symbol_list

     
        def copyFrom(self, ctx):
            super(EParser.Symbol_listContext, self).copyFrom(ctx)


    class SymbolListContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Symbol_listContext)
            super(EParser.SymbolListContext, self).__init__(parser)
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolList(self)


    class SymbolListItemContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Symbol_listContext)
            super(EParser.SymbolListItemContext, self).__init__(parser)
            self.items = None # Symbol_listContext
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(EParser.Symbol_listContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolListItem(self)



    def symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1258 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SymbolListItemContext(self, EParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1260
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1261
                    self.match(EParser.COMMA)
                    self.state = 1262 
                    localctx.item = self.symbol_identifier() 
                self.state = 1267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(EParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingExpression(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingRange(self)


    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(EParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingPattern(self)



    def attribute_constraint(self):

        localctx = EParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_attribute_constraint)
        try:
            self.state = 1278
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1268
                self.match(EParser.IN)
                self.state = 1269 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1270
                self.match(EParser.IN)
                self.state = 1271 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1272
                self.match(EParser.IN)
                self.state = 1273 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1274
                self.match(EParser.MATCHING)
                self.state = 1275
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1276
                self.match(EParser.MATCHING)
                self.state = 1277 
                localctx.exp = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_list_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = EParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1280
            self.match(EParser.LBRAK)
            self.state = 1282
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)) | (1 << (EParser.DATE_LITERAL - 87)) | (1 << (EParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1281 
                localctx.items = self.expression_list(0)


            self.state = 1284
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LT(self):
            return self.getToken(EParser.LT, 0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_set_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = EParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1286
            self.match(EParser.LT)
            self.state = 1288
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)) | (1 << (EParser.DATE_LITERAL - 87)) | (1 << (EParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1287 
                localctx.items = self.expression_list(0)


            self.state = 1290
            self.match(EParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_expression_list

     
        def copyFrom(self, ctx):
            super(EParser.Expression_listContext, self).copyFrom(ctx)


    class ValueListItemContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_listContext)
            super(EParser.ValueListItemContext, self).__init__(parser)
            self.items = None # Expression_listContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueListItem(self)


    class ValueListContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_listContext)
            super(EParser.ValueListContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueList(self)



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1293 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueListItemContext(self, EParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1295
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1296
                    self.match(EParser.COMMA)
                    self.state = 1297 
                    localctx.item = self.expression(0) 
                self.state = 1302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(EParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_range_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = EParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1303
            self.match(EParser.LBRAK)
            self.state = 1304 
            localctx.low = self.expression(0)
            self.state = 1305
            self.match(EParser.RANGE)
            self.state = 1306 
            localctx.high = self.expression(0)
            self.state = 1307
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(EParser.TypedefContext, self).copyFrom(ctx)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitListType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(EParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPrimaryType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(EParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1310 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1320
                    la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                    if la_ == 1:
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1312
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1313
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1314
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1315
                        self.match(EParser.LBRAK)
                        self.state = 1316
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1317
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1318
                        self.match(EParser.LCURL)
                        self.state = 1319
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(EParser.Primary_typeContext, self).copyFrom(ctx)



    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryType(self)


    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(EParser.Native_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeType(self)



    def primary_type(self):

        localctx = EParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_primary_type)
        try:
            self.state = 1327
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1325 
                localctx.n = self.native_type()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1326 
                localctx.c = self.category_type()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(EParser.Native_typeContext, self).copyFrom(ctx)



    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TextTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CodeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.IntegerTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DecimalTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalType(self)


    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.PeriodTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CharacterTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BooleanTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanType(self)



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_native_type)
        try:
            self.state = 1339
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1329
                localctx.t1 = self.match(EParser.BOOLEAN)

            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1330
                localctx.t1 = self.match(EParser.CHARACTER)

            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1331
                localctx.t1 = self.match(EParser.TEXT)

            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1332
                localctx.t1 = self.match(EParser.INTEGER)

            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1333
                localctx.t1 = self.match(EParser.DECIMAL)

            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1334
                localctx.t1 = self.match(EParser.DATE)

            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1335
                localctx.t1 = self.match(EParser.DATETIME)

            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1336
                localctx.t1 = self.match(EParser.TIME)

            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1337
                localctx.t1 = self.match(EParser.PERIOD)

            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1338
                localctx.t1 = self.match(EParser.CODE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_category_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = EParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1341
            localctx.t1 = self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def getRuleIndex(self):
            return EParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = EParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1343
            localctx.t1 = self.match(EParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Document_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def getRuleIndex(self):
            return EParser.RULE_document_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocument_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocument_type(self)




    def document_type(self):

        localctx = EParser.Document_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345
            localctx.t1 = self.match(EParser.DOCUMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(EParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(EParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = EParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_category_declaration)
        try:
            self.state = 1350
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1347 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1348 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1349 
                localctx.decl = self.singleton_category_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_type_identifier_list

     
        def copyFrom(self, ctx):
            super(EParser.Type_identifier_listContext, self).copyFrom(ctx)


    class TypeIdentifierListItemContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Type_identifier_listContext)
            super(EParser.TypeIdentifierListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifierListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifierListItem(self)


    class TypeIdentifierListContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Type_identifier_listContext)
            super(EParser.TypeIdentifierListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifierList(self)



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 164
        self.enterRecursionRule(localctx, 164, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1353 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.TypeIdentifierListItemContext(self, EParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1355
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1356
                    self.match(EParser.COMMA)
                    self.state = 1357 
                    localctx.item = self.type_identifier() 
                self.state = 1362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_identifier

     
        def copyFrom(self, ctx):
            super(EParser.Method_identifierContext, self).copyFrom(ctx)



    class MethodVariableIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_identifierContext)
            super(EParser.MethodVariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodVariableIdentifier(self)


    class MethodTypeIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_identifierContext)
            super(EParser.MethodTypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodTypeIdentifier(self)



    def method_identifier(self):

        localctx = EParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_method_identifier)
        try:
            self.state = 1365
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1363 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1364 
                localctx.name = self.type_identifier()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(EParser.IdentifierContext, self).copyFrom(ctx)



    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.SymbolIdentifierContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.VariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableIdentifier(self)


    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.TypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifier(self)



    def identifier(self):

        localctx = EParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_identifier)
        try:
            self.state = 1370
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1367 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1368 
                localctx.name = self.type_identifier()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1369 
                localctx.name = self.symbol_identifier()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = EParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1372
            self.match(EParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = EParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1374
            self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = EParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1376
            self.match(EParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Argument_listContext, self).copyFrom(ctx)


    class ArgumentListItemContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_listContext)
            super(EParser.ArgumentListItemContext, self).__init__(parser)
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def argument_list(self):
            return self.getTypedRuleContext(EParser.Argument_listContext,0)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentListItem(self)


    class ArgumentListContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_listContext)
            super(EParser.ArgumentListContext, self).__init__(parser)
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentList(self)



    def argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 176
        self.enterRecursionRule(localctx, 176, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1379 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentListItemContext(self, EParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1381
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1382
                    self.match(EParser.COMMA)
                    self.state = 1383 
                    localctx.item = self.argument() 
                self.state = 1388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(EParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(EParser.Operator_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(EParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = EParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_argument)
        try:
            self.state = 1391
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1389 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1390 
                localctx.arg = self.operator_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_operator_argument

     
        def copyFrom(self, ctx):
            super(EParser.Operator_argumentContext, self).copyFrom(ctx)



    class NamedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a EParser.Operator_argumentContext)
            super(EParser.NamedArgumentContext, self).__init__(parser)
            self.arg = None # Named_argumentContext
            self.copyFrom(ctx)

        def named_argument(self):
            return self.getTypedRuleContext(EParser.Named_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNamedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNamedArgument(self)


    class TypedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a EParser.Operator_argumentContext)
            super(EParser.TypedArgumentContext, self).__init__(parser)
            self.arg = None # Typed_argumentContext
            self.copyFrom(ctx)

        def typed_argument(self):
            return self.getTypedRuleContext(EParser.Typed_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypedArgument(self)



    def operator_argument(self):

        localctx = EParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_operator_argument)
        try:
            self.state = 1395
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1393 
                localctx.arg = self.named_argument()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1394 
                localctx.arg = self.typed_argument()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Named_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_named_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = EParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1397 
            localctx.name = self.variable_identifier()
            self.state = 1400
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.state = 1398
                self.match(EParser.EQ)
                self.state = 1399 
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(EParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_code_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = EParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1402 
            self.code_type()
            self.state = 1403 
            localctx.name = self.variable_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_or_any_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_or_any_type

     
        def copyFrom(self, ctx):
            super(EParser.Category_or_any_typeContext, self).copyFrom(ctx)



    class AnyArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_or_any_typeContext)
            super(EParser.AnyArgumentTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyArgumentType(self)


    class CategoryArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_or_any_typeContext)
            super(EParser.CategoryArgumentTypeContext, self).__init__(parser)
            self.typ = None # TypedefContext
            self.copyFrom(ctx)

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryArgumentType(self)



    def category_or_any_type(self):

        localctx = EParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_category_or_any_type)
        try:
            self.state = 1407
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1405 
                localctx.typ = self.typedef(0)

            elif token in [EParser.ANY]:
                localctx = EParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1406 
                localctx.typ = self.any_type(0)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Any_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(EParser.Any_typeContext, self).copyFrom(ctx)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyType(self)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyListTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyListType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyDictTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)
        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 188
        self.enterRecursionRule(localctx, 188, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1410
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1418
                    la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1412
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1413
                        self.match(EParser.LBRAK)
                        self.state = 1414
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1415
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1416
                        self.match(EParser.LCURL)
                        self.state = 1417
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_method_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Category_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListContext(Category_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_method_declaration_listContext)
            super(EParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Category_method_declarationContext
            self.copyFrom(ctx)

        def category_method_declaration(self):
            return self.getTypedRuleContext(EParser.Category_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryMethodList(self)


    class CategoryMethodListItemContext(Category_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_method_declaration_listContext)
            super(EParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Category_method_declaration_listContext
            self.item = None # Category_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def category_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Category_method_declaration_listContext,0)

        def category_method_declaration(self):
            return self.getTypedRuleContext(EParser.Category_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryMethodListItem(self)



    def category_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Category_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 190
        self.enterRecursionRule(localctx, 190, self.RULE_category_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1424 
            localctx.item = self.category_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategoryMethodListItemContext(self, EParser.Category_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_method_declaration_list)
                    self.state = 1426
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1427 
                    self.lfp()
                    self.state = 1428 
                    localctx.item = self.category_method_declaration() 
                self.state = 1434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_method_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Category_method_declarationContext, self).copyFrom(ctx)



    class GetterMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_method_declarationContext)
            super(EParser.GetterMethodContext, self).__init__(parser)
            self.decl = None # Getter_method_declarationContext
            self.copyFrom(ctx)

        def getter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Getter_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGetterMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGetterMethod(self)


    class MemberMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_method_declarationContext)
            super(EParser.MemberMethodContext, self).__init__(parser)
            self.decl = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberMethod(self)


    class SetterMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_method_declarationContext)
            super(EParser.SetterMethodContext, self).__init__(parser)
            self.decl = None # Setter_method_declarationContext
            self.copyFrom(ctx)

        def setter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Setter_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetterMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetterMethod(self)


    class OperatorMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_method_declarationContext)
            super(EParser.OperatorMethodContext, self).__init__(parser)
            self.decl = None # Operator_method_declarationContext
            self.copyFrom(ctx)

        def operator_method_declaration(self):
            return self.getTypedRuleContext(EParser.Operator_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMethod(self)



    def category_method_declaration(self):

        localctx = EParser.Category_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_category_method_declaration)
        try:
            self.state = 1439
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                localctx = EParser.SetterMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1435 
                localctx.decl = self.setter_method_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.GetterMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1436 
                localctx.decl = self.getter_method_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.MemberMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1437 
                localctx.decl = self.member_method_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.OperatorMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1438 
                localctx.decl = self.operator_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_mappingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_mappingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_mapping

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_mappingContext, self).copyFrom(ctx)



    class CSharpCategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mappingContext)
            super(EParser.CSharpCategoryMappingContext, self).__init__(parser)
            self.mapping = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCategoryMapping(self)


    class JavaCategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mappingContext)
            super(EParser.JavaCategoryMappingContext, self).__init__(parser)
            self.mapping = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCategoryMapping(self)


    class JavaScriptCategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mappingContext)
            super(EParser.JavaScriptCategoryMappingContext, self).__init__(parser)
            self.mapping = None # Javascript_category_mappingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_category_mapping(self):
            return self.getTypedRuleContext(EParser.Javascript_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptCategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptCategoryMapping(self)


    class Python3CategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mappingContext)
            super(EParser.Python3CategoryMappingContext, self).__init__(parser)
            self.mapping = None # Python_category_mappingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_category_mapping(self):
            return self.getTypedRuleContext(EParser.Python_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3CategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3CategoryMapping(self)


    class Python2CategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_mappingContext)
            super(EParser.Python2CategoryMappingContext, self).__init__(parser)
            self.mapping = None # Python_category_mappingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_category_mapping(self):
            return self.getTypedRuleContext(EParser.Python_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2CategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2CategoryMapping(self)



    def native_category_mapping(self):

        localctx = EParser.Native_category_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_native_category_mapping)
        try:
            self.state = 1451
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1441
                self.match(EParser.JAVA)
                self.state = 1442 
                localctx.mapping = self.java_class_identifier_expression(0)

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1443
                self.match(EParser.CSHARP)
                self.state = 1444 
                localctx.mapping = self.csharp_identifier_expression(0)

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1445
                self.match(EParser.PYTHON2)
                self.state = 1446 
                localctx.mapping = self.python_category_mapping()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1447
                self.match(EParser.PYTHON3)
                self.state = 1448 
                localctx.mapping = self.python_category_mapping()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1449
                self.match(EParser.JAVASCRIPT)
                self.state = 1450 
                localctx.mapping = self.javascript_category_mapping()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_category_mappingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_category_mappingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_category_mapping

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_category_mapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_category_mapping(self)




    def python_category_mapping(self):

        localctx = EParser.Python_category_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_python_category_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453 
            localctx.id_ = self.identifier()
            self.state = 1455
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 1454 
                localctx.module = self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(EParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(EParser.DOT)
            else:
                return self.getToken(EParser.DOT, i)

        def getRuleIndex(self):
            return EParser.RULE_python_module

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = EParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1457
            self.match(EParser.FROM)
            self.state = 1458 
            self.module_token()
            self.state = 1459
            self.match(EParser.COLON)
            self.state = 1460 
            self.identifier()
            self.state = 1465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1461
                    self.match(EParser.DOT)
                    self.state = 1462 
                    self.identifier() 
                self.state = 1467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = EParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1468
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1469
            if not self.isText(localctx.i1,"module"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"module\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_mappingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_category_mappingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_category_mapping

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_category_mapping(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_category_mapping(self)




    def javascript_category_mapping(self):

        localctx = EParser.Javascript_category_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_javascript_category_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1471 
            localctx.id_ = self.identifier()
            self.state = 1473
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.state = 1472 
                localctx.module = self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(EParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EParser.IdentifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(EParser.SLASH)
            else:
                return self.getToken(EParser.SLASH, i)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_module

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = EParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1475
            self.match(EParser.FROM)
            self.state = 1476 
            self.module_token()
            self.state = 1477
            self.match(EParser.COLON)
            self.state = 1479
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1478
                self.match(EParser.SLASH)


            self.state = 1481 
            self.identifier()
            self.state = 1486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1482
                    self.match(EParser.SLASH)
                    self.state = 1483 
                    self.identifier() 
                self.state = 1488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

            self.state = 1491
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 1489
                self.match(EParser.DOT)
                self.state = 1490 
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_variable_identifier_list

     
        def copyFrom(self, ctx):
            super(EParser.Variable_identifier_listContext, self).copyFrom(ctx)


    class VariableListContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Variable_identifier_listContext)
            super(EParser.VariableListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableList(self)


    class VariableListItemContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Variable_identifier_listContext)
            super(EParser.VariableListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableListItem(self)



    def variable_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Variable_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 206
        self.enterRecursionRule(localctx, 206, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1494 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1501
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,99,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.VariableListItemContext(self, EParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1496
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1497
                    self.match(EParser.COMMA)
                    self.state = 1498 
                    localctx.item = self.variable_identifier() 
                self.state = 1503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,99,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Method_declarationContext, self).copyFrom(ctx)



    class ConcreteMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.ConcreteMethodContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcreteMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcreteMethod(self)


    class AbstractMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.AbstractMethodContext, self).__init__(parser)
            self.decl = None # Abstract_method_declarationContext
            self.copyFrom(ctx)

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAbstractMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAbstractMethod(self)


    class NativeMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.NativeMethodContext, self).__init__(parser)
            self.decl = None # Native_method_declarationContext
            self.copyFrom(ctx)

        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeMethod(self)



    def method_declaration(self):

        localctx = EParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_method_declaration)
        try:
            self.state = 1507
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                localctx = EParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1504 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1505 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1506 
                localctx.decl = self.native_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_statement_listContext, self).copyFrom(ctx)


    class NativeStatementListContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statement_listContext)
            super(EParser.NativeStatementListContext, self).__init__(parser)
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def native_statement(self):
            return self.getTypedRuleContext(EParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeStatementList(self)


    class NativeStatementListItemContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statement_listContext)
            super(EParser.NativeStatementListItemContext, self).__init__(parser)
            self.items = None # Native_statement_listContext
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)

        def native_statement(self):
            return self.getTypedRuleContext(EParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeStatementListItem(self)



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 210
        self.enterRecursionRule(localctx, 210, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1510 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeStatementListItemContext(self, EParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1512
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1513 
                    self.lfp()
                    self.state = 1514 
                    localctx.item = self.native_statement() 
                self.state = 1520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(EParser.Native_statementContext, self).copyFrom(ctx)



    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python2NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2NativeStatement(self)


    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.CSharpNativeStatementContext, self).__init__(parser)
            self.stmt = None # Csharp_statementContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(EParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaNativeStatementContext, self).__init__(parser)
            self.stmt = None # Java_statementContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(EParser.Java_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.stmt = None # Javascript_native_statementContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptNativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python3NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = EParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_native_statement)
        try:
            self.state = 1531
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1521
                self.match(EParser.JAVA)
                self.state = 1522 
                localctx.stmt = self.java_statement()

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1523
                self.match(EParser.CSHARP)
                self.state = 1524 
                localctx.stmt = self.csharp_statement()

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1525
                self.match(EParser.PYTHON2)
                self.state = 1526 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1527
                self.match(EParser.PYTHON3)
                self.state = 1528 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1529
                self.match(EParser.JAVASCRIPT)
                self.state = 1530 
                localctx.stmt = self.javascript_native_statement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Python_statementContext
            self.module = None # Python_moduleContext

        def python_statement(self):
            return self.getTypedRuleContext(EParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_native_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = EParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1533 
            localctx.stmt = self.python_statement()
            self.state = 1535
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                self.state = 1534
                self.match(EParser.SEMI)


            self.state = 1538
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 1537 
                localctx.module = self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Javascript_statementContext
            self.module = None # Javascript_moduleContext

        def javascript_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = EParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1540 
            localctx.stmt = self.javascript_statement()
            self.state = 1542
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 1541
                self.match(EParser.SEMI)


            self.state = 1545
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.state = 1544 
                localctx.module = self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Statement_listContext, self).copyFrom(ctx)


    class StatementListItemContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Statement_listContext)
            super(EParser.StatementListItemContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)

        def statement(self):
            return self.getTypedRuleContext(EParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStatementListItem(self)


    class StatementListContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Statement_listContext)
            super(EParser.StatementListContext, self).__init__(parser)
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(EParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStatementList(self)



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 218
        self.enterRecursionRule(localctx, 218, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1548 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1556
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.StatementListItemContext(self, EParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1550
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1551 
                    self.lfp()
                    self.state = 1552 
                    localctx.item = self.statement() 
                self.state = 1558
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,107,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Switch_case_statement_listContext, self).copyFrom(ctx)


    class SwitchCaseStatementListItemContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statement_listContext)
            super(EParser.SwitchCaseStatementListItemContext, self).__init__(parser)
            self.items = None # Switch_case_statement_listContext
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def switch_case_statement_list(self):
            return self.getTypedRuleContext(EParser.Switch_case_statement_listContext,0)

        def switch_case_statement(self):
            return self.getTypedRuleContext(EParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchCaseStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchCaseStatementListItem(self)


    class SwitchCaseStatementListContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statement_listContext)
            super(EParser.SwitchCaseStatementListContext, self).__init__(parser)
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def switch_case_statement(self):
            return self.getTypedRuleContext(EParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchCaseStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchCaseStatementList(self)



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 220
        self.enterRecursionRule(localctx, 220, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1560 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1568
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,108,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SwitchCaseStatementListItemContext(self, EParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1562
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1563 
                    self.lfp()
                    self.state = 1564 
                    localctx.item = self.switch_case_statement() 
                self.state = 1570
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_catch_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Catch_statement_listContext, self).copyFrom(ctx)


    class CatchStatementListContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statement_listContext)
            super(EParser.CatchStatementListContext, self).__init__(parser)
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def catch_statement(self):
            return self.getTypedRuleContext(EParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchStatementList(self)


    class CatchStatementListItemContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statement_listContext)
            super(EParser.CatchStatementListItemContext, self).__init__(parser)
            self.items = None # Catch_statement_listContext
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(EParser.Catch_statement_listContext,0)

        def catch_statement(self):
            return self.getTypedRuleContext(EParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchStatementListItem(self)



    def catch_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Catch_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 222
        self.enterRecursionRule(localctx, 222, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1572 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1580
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,109,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CatchStatementListItemContext(self, EParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1574
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1575 
                    self.lfp()
                    self.state = 1576 
                    localctx.item = self.catch_statement() 
                self.state = 1582
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(EParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralSetLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralSetLiteral(self)


    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralListLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(EParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(EParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralRangeLiteral(self)



    def literal_collection(self):

        localctx = EParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_literal_collection)
        try:
            self.state = 1597
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1583
                self.match(EParser.LBRAK)
                self.state = 1584 
                localctx.low = self.atomic_literal()
                self.state = 1585
                self.match(EParser.RANGE)
                self.state = 1586 
                localctx.high = self.atomic_literal()
                self.state = 1587
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1589
                self.match(EParser.LBRAK)
                self.state = 1590 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1591
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1593
                self.match(EParser.LT)
                self.state = 1594 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1595
                self.match(EParser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atomic_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(EParser.Atomic_literalContext, self).copyFrom(ctx)



    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(EParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(EParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNullLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(EParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitHexadecimalLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(EParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(EParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(EParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalLiteral(self)


    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(EParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(EParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanLiteral(self)



    def atomic_literal(self):

        localctx = EParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_atomic_literal)
        try:
            self.state = 1612
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1599
                localctx.t = self.match(EParser.MIN_INTEGER)

            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1600
                localctx.t = self.match(EParser.MAX_INTEGER)

            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1601
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1602
                localctx.t = self.match(EParser.HEXA_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1603
                localctx.t = self.match(EParser.CHAR_LITERAL)

            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1604
                localctx.t = self.match(EParser.DATE_LITERAL)

            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1605
                localctx.t = self.match(EParser.TIME_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1606
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1607
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1608
                localctx.t = self.match(EParser.DATETIME_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1609
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1610
                localctx.t = self.match(EParser.PERIOD_LITERAL)

            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1611 
                localctx.n = self.null_literal()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_list_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_literal_list_literal

     
        def copyFrom(self, ctx):
            super(EParser.Literal_list_literalContext, self).copyFrom(ctx)


    class LiteralListContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_list_literalContext)
            super(EParser.LiteralListContext, self).__init__(parser)
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralList(self)


    class LiteralListItemContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_list_literalContext)
            super(EParser.LiteralListItemContext, self).__init__(parser)
            self.items = None # Literal_list_literalContext
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralListItem(self)



    def literal_list_literal(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Literal_list_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1615 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1622
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,112,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.LiteralListItemContext(self, EParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1617
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1618
                    self.match(EParser.COMMA)
                    self.state = 1619 
                    localctx.item = self.atomic_literal() 
                self.state = 1624
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,112,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(EParser.Selectable_expressionContext, self).copyFrom(ctx)



    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIdentifierExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralExpression(self)


    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitThisExpression(self)



    def selectable_expression(self):

        localctx = EParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_selectable_expression)
        try:
            self.state = 1629
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1625 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1626 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1627 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1628 
                localctx.exp = self.this_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class This_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

        def getRuleIndex(self):
            return EParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = EParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631
            _la = self._input.LA(1)
            if not(_la==EParser.SELF or _la==EParser.THIS):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = EParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633
            self.match(EParser.LPAR)
            self.state = 1634 
            localctx.exp = self.expression(0)
            self.state = 1635
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Literal_expressionContext, self).copyFrom(ctx)



    class CollectionLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_expressionContext)
            super(EParser.CollectionLiteralContext, self).__init__(parser)
            self.exp = None # Collection_literalContext
            self.copyFrom(ctx)

        def collection_literal(self):
            return self.getTypedRuleContext(EParser.Collection_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollectionLiteral(self)


    class AtomicLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_expressionContext)
            super(EParser.AtomicLiteralContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAtomicLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAtomicLiteral(self)



    def literal_expression(self):

        localctx = EParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_literal_expression)
        try:
            self.state = 1639
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                localctx = EParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1637 
                localctx.exp = self.atomic_literal()

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT]:
                localctx = EParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1638 
                localctx.exp = self.collection_literal()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Collection_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_collection_literal

     
        def copyFrom(self, ctx):
            super(EParser.Collection_literalContext, self).copyFrom(ctx)



    class TupleLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.TupleLiteralContext, self).__init__(parser)
            self.exp = None # Tuple_literalContext
            self.copyFrom(ctx)

        def tuple_literal(self):
            return self.getTypedRuleContext(EParser.Tuple_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTupleLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTupleLiteral(self)


    class ListLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.ListLiteralContext, self).__init__(parser)
            self.exp = None # List_literalContext
            self.copyFrom(ctx)

        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitListLiteral(self)


    class DictLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.DictLiteralContext, self).__init__(parser)
            self.exp = None # Dict_literalContext
            self.copyFrom(ctx)

        def dict_literal(self):
            return self.getTypedRuleContext(EParser.Dict_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictLiteral(self)


    class RangeLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.RangeLiteralContext, self).__init__(parser)
            self.exp = None # Range_literalContext
            self.copyFrom(ctx)

        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRangeLiteral(self)


    class SetLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.SetLiteralContext, self).__init__(parser)
            self.exp = None # Set_literalContext
            self.copyFrom(ctx)

        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetLiteral(self)



    def collection_literal(self):

        localctx = EParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_collection_literal)
        try:
            self.state = 1646
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                localctx = EParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1641 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = EParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1642 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = EParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1643 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = EParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1644 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = EParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1645 
                localctx.exp = self.tuple_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_tupleContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(EParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_tuple_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = EParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1648
            self.match(EParser.LPAR)
            self.state = 1650
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)) | (1 << (EParser.DATE_LITERAL - 87)) | (1 << (EParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1649 
                localctx.items = self.expression_tuple(0)


            self.state = 1652
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Dict_entry_listContext

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(EParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_dict_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = EParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1654
            self.match(EParser.LCURL)
            self.state = 1656
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)) | (1 << (EParser.DATE_LITERAL - 87)) | (1 << (EParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1655 
                localctx.items = self.dict_entry_list(0)


            self.state = 1658
            self.match(EParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_expression_tuple

     
        def copyFrom(self, ctx):
            super(EParser.Expression_tupleContext, self).copyFrom(ctx)


    class ValueTupleItemContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_tupleContext)
            super(EParser.ValueTupleItemContext, self).__init__(parser)
            self.items = None # Expression_tupleContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def expression_tuple(self):
            return self.getTypedRuleContext(EParser.Expression_tupleContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueTupleItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueTupleItem(self)


    class ValueTupleContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_tupleContext)
            super(EParser.ValueTupleContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueTuple(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueTuple(self)



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 244
        self.enterRecursionRule(localctx, 244, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1661 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1668
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueTupleItemContext(self, EParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1663
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1664
                    self.match(EParser.COMMA)
                    self.state = 1665 
                    localctx.item = self.expression(0) 
                self.state = 1670
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_dict_entry_list

     
        def copyFrom(self, ctx):
            super(EParser.Dict_entry_listContext, self).copyFrom(ctx)


    class DictEntryListContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Dict_entry_listContext)
            super(EParser.DictEntryListContext, self).__init__(parser)
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def dict_entry(self):
            return self.getTypedRuleContext(EParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictEntryList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictEntryList(self)


    class DictEntryListItemContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Dict_entry_listContext)
            super(EParser.DictEntryListItemContext, self).__init__(parser)
            self.items = None # Dict_entry_listContext
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def dict_entry_list(self):
            return self.getTypedRuleContext(EParser.Dict_entry_listContext,0)

        def dict_entry(self):
            return self.getTypedRuleContext(EParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictEntryListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictEntryListItem(self)



    def dict_entry_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Dict_entry_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 246
        self.enterRecursionRule(localctx, 246, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1672 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1679
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DictEntryListItemContext(self, EParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1674
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1675
                    self.match(EParser.COMMA)
                    self.state = 1676 
                    localctx.item = self.dict_entry() 
                self.state = 1681
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_dict_entry

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = EParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1682 
            localctx.key = self.expression(0)
            self.state = 1683
            self.match(EParser.COLON)
            self.state = 1684 
            localctx.value = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Slice_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceFirstAndLast(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceFirstOnly(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceLastOnly(self)



    def slice_arguments(self):

        localctx = EParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_slice_arguments)
        try:
            self.state = 1695
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1686 
                localctx.first = self.expression(0)
                self.state = 1687
                self.match(EParser.COLON)
                self.state = 1688 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1690 
                localctx.first = self.expression(0)
                self.state = 1691
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1693
                self.match(EParser.COLON)
                self.state = 1694 
                localctx.last = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_variable_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = EParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1697 
            localctx.name = self.variable_identifier()
            self.state = 1698 
            self.assign()
            self.state = 1699 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignable_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(EParser.Assignable_instanceContext, self).copyFrom(ctx)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.RootInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRootInstance(self)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.ChildInstanceContext, self).__init__(parser)
            self.parent = None # Assignable_instanceContext
            self.child = None # Child_instanceContext
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(EParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitChildInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 254
        self.enterRecursionRule(localctx, 254, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1702 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1708
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1704
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1705 
                    localctx.child = self.child_instance() 
                self.state = 1710
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(EParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsATypeExpressionContext, self).__init__(parser)
            self.typ = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsOtherExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = EParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_is_expression)
        try:
            self.state = 1715
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1711
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1712
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1713 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1714 
                localctx.exp = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(EParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(EParser.PLUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorModulo(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMinus(self)



    def operator(self):

        localctx = EParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_operator)
        try:
            self.state = 1723
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1717
                self.match(EParser.PLUS)

            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1718
                self.match(EParser.MINUS)

            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1719 
                self.multiply()

            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1720 
                self.divide()

            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1721 
                self.idivide()

            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1722 
                self.modulo()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Key_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = EParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1725
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1726
            if not self.isText(localctx.i1,"key"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"key\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = EParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1728
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1729
            if not self.isText(localctx.i1,"value"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"value\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbols_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = EParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1731
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1732
            if not self.isText(localctx.i1,"symbols"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"symbols\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def getRuleIndex(self):
            return EParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = EParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1734
            self.match(EParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(EParser.STAR, 0)

        def getRuleIndex(self):
            return EParser.RULE_multiply

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = EParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1736
            self.match(EParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(EParser.SLASH, 0)

        def getRuleIndex(self):
            return EParser.RULE_divide

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = EParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1738
            self.match(EParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(EParser.BSLASH, 0)

        def getRuleIndex(self):
            return EParser.RULE_idivide

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = EParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1740
            self.match(EParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(EParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(EParser.MODULO, 0)

        def getRuleIndex(self):
            return EParser.RULE_modulo

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = EParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1742
            _la = self._input.LA(1)
            if not(_la==EParser.PERCENT or _la==EParser.MODULO):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_statementContext)
            super(EParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptReturnStatement(self)


    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_statementContext)
            super(EParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptStatement(self)



    def javascript_statement(self):

        localctx = EParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_javascript_statement)
        try:
            self.state = 1751
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1744
                self.match(EParser.RETURN)
                self.state = 1745 
                localctx.exp = self.javascript_expression(0)
                self.state = 1746
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1748 
                localctx.exp = self.javascript_expression(0)
                self.state = 1749
                self.match(EParser.SEMI)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptPrimaryExpression(self)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptSelectorExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 278
        self.enterRecursionRule(localctx, 278, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1754 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1760
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1756
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1757 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1762
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_primary_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_primary_expressionContext, self).copyFrom(ctx)



    class JavascriptParenthesisExpressionContext(Javascript_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_primary_expressionContext)
            super(EParser.JavascriptParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_parenthesis_expressionContext
            self.copyFrom(ctx)

        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptParenthesisExpression(self)


    class JavascriptLiteralExpressionContext(Javascript_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_primary_expressionContext)
            super(EParser.JavascriptLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_literal_expressionContext
            self.copyFrom(ctx)

        def javascript_literal_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptLiteralExpression(self)


    class JavascriptIdentifierExpressionContext(Javascript_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_primary_expressionContext)
            super(EParser.JavascriptIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_identifier_expressionContext
            self.copyFrom(ctx)

        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptIdentifierExpression(self)



    def javascript_primary_expression(self):

        localctx = EParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_javascript_primary_expression)
        try:
            self.state = 1766
            token = self._input.LA(1)
            if token in [EParser.LPAR]:
                localctx = EParser.JavascriptParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1763 
                localctx.exp = self.javascript_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.JavascriptIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1764 
                localctx.exp = self.javascript_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1765 
                localctx.exp = self.javascript_literal_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavascriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavascriptMethodExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptMethodExpression(self)


    class JavascriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavascriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptItemExpression(self)



    def javascript_selector_expression(self):

        localctx = EParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_javascript_selector_expression)
        try:
            self.state = 1771
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavascriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1768
                self.match(EParser.DOT)
                self.state = 1769 
                localctx.exp = self.javascript_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavascriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1770 
                localctx.exp = self.javascript_item_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(EParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = EParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1773 
            localctx.name = self.javascript_identifier()
            self.state = 1774
            self.match(EParser.LPAR)
            self.state = 1776
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (EParser.READ - 115)) | (1 << (EParser.WRITE - 115)) | (1 << (EParser.BOOLEAN_LITERAL - 115)) | (1 << (EParser.CHAR_LITERAL - 115)) | (1 << (EParser.SYMBOL_IDENTIFIER - 115)) | (1 << (EParser.TYPE_IDENTIFIER - 115)) | (1 << (EParser.VARIABLE_IDENTIFIER - 115)) | (1 << (EParser.TEXT_LITERAL - 115)) | (1 << (EParser.INTEGER_LITERAL - 115)) | (1 << (EParser.DECIMAL_LITERAL - 115)))) != 0):
                self.state = 1775 
                localctx.args = self.javascript_arguments(0)


            self.state = 1778
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_argumentsContext)
            super(EParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(EParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptArgumentListItem(self)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_argumentsContext)
            super(EParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptArgumentList(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 286
        self.enterRecursionRule(localctx, 286, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1781 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1788
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1783
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1784
                    self.match(EParser.COMMA)
                    self.state = 1785 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1790
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = EParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1791
            self.match(EParser.LBRAK)
            self.state = 1792 
            localctx.exp = self.javascript_expression(0)
            self.state = 1793
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = EParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795
            self.match(EParser.LPAR)
            self.state = 1796 
            localctx.exp = self.javascript_expression(0)
            self.state = 1797
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_identifier_expressionContext, self).copyFrom(ctx)


    class JavascriptIdentifierContext(Javascript_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_identifier_expressionContext)
            super(EParser.JavascriptIdentifierContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptIdentifier(self)


    class JavascriptChildIdentifierContext(Javascript_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_identifier_expressionContext)
            super(EParser.JavascriptChildIdentifierContext, self).__init__(parser)
            self.parent = None # Javascript_identifier_expressionContext
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_identifier_expressionContext,0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptChildIdentifier(self)



    def javascript_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 292
        self.enterRecursionRule(localctx, 292, self.RULE_javascript_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1800 
            localctx.name = self.javascript_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1807
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptChildIdentifierContext(self, EParser.Javascript_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_identifier_expression)
                    self.state = 1802
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1803
                    self.match(EParser.DOT)
                    self.state = 1804 
                    localctx.name = self.javascript_identifier() 
                self.state = 1809
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptDecimalLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptTextLiteral(self)



    def javascript_literal_expression(self):

        localctx = EParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_javascript_literal_expression)
        try:
            self.state = 1815
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1810
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1811
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1812
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1813
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1814
                localctx.t = self.match(EParser.CHAR_LITERAL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = EParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1817
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (EParser.READ - 115)) | (1 << (EParser.WRITE - 115)) | (1 << (EParser.SYMBOL_IDENTIFIER - 115)) | (1 << (EParser.TYPE_IDENTIFIER - 115)) | (1 << (EParser.VARIABLE_IDENTIFIER - 115)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(EParser.Python_statementContext, self).copyFrom(ctx)



    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_statementContext)
            super(EParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonReturnStatement(self)


    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_statementContext)
            super(EParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonStatement(self)



    def python_statement(self):

        localctx = EParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_python_statement)
        try:
            self.state = 1822
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1819
                self.match(EParser.RETURN)
                self.state = 1820 
                localctx.exp = self.python_expression(0)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1821 
                localctx.exp = self.python_expression(0)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(EParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPrimaryExpression(self)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(EParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonSelectorExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 300
        self.enterRecursionRule(localctx, 300, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1825 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1831
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1827
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1828 
                    localctx.child = self.python_selector_expression() 
                self.state = 1833
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonGlobalMethodExpression(self)


    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(EParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonLiteralExpression(self)



    def python_primary_expression(self):

        localctx = EParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_python_primary_expression)
        try:
            self.state = 1838
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1834 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1835 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1836 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1837 
                localctx.exp = self.python_method_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_selector_expressionContext)
            super(EParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonItemExpression(self)


    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_selector_expressionContext)
            super(EParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonMethodExpression(self)



    def python_selector_expression(self):

        localctx = EParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_python_selector_expression)
        try:
            self.state = 1846
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1840
                self.match(EParser.DOT)
                self.state = 1841 
                localctx.exp = self.python_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1842
                self.match(EParser.LBRAK)
                self.state = 1843 
                localctx.exp = self.python_expression(0)
                self.state = 1844
                self.match(EParser.RBRAK)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = EParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1848 
            localctx.name = self.python_identifier()
            self.state = 1849
            self.match(EParser.LPAR)
            self.state = 1851
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (EParser.BOOLEAN_LITERAL - 134)) | (1 << (EParser.CHAR_LITERAL - 134)) | (1 << (EParser.SYMBOL_IDENTIFIER - 134)) | (1 << (EParser.TYPE_IDENTIFIER - 134)) | (1 << (EParser.VARIABLE_IDENTIFIER - 134)) | (1 << (EParser.TEXT_LITERAL - 134)) | (1 << (EParser.INTEGER_LITERAL - 134)) | (1 << (EParser.DECIMAL_LITERAL - 134)))) != 0):
                self.state = 1850 
                localctx.args = self.python_argument_list()


            self.state = 1853
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonArgumentList(self)


    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)



    def python_argument_list(self):

        localctx = EParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_python_argument_list)
        try:
            self.state = 1861
            la_ = self._interp.adaptivePredict(self._input,137,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1855 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1856 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1857 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1858
                self.match(EParser.COMMA)
                self.state = 1859 
                localctx.named = self.python_named_argument_list(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_ordinal_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_ordinal_argument_listContext)
            super(EParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_ordinal_argument_listContext)
            super(EParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalArgumentList(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1864 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1871
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1866
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1867
                    self.match(EParser.COMMA)
                    self.state = 1868 
                    localctx.item = self.python_expression(0) 
                self.state = 1873
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_named_argument_listContext)
            super(EParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedArgumentListItem(self)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_named_argument_listContext)
            super(EParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedArgumentList(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 312
        self.enterRecursionRule(localctx, 312, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1875 
            localctx.name = self.python_identifier()
            self.state = 1876
            self.match(EParser.EQ)
            self.state = 1877 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1887
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1879
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1880
                    self.match(EParser.COMMA)
                    self.state = 1881 
                    localctx.name = self.python_identifier()
                    self.state = 1882
                    self.match(EParser.EQ)
                    self.state = 1883 
                    localctx.exp = self.python_expression(0) 
                self.state = 1889
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = EParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1890
            self.match(EParser.LPAR)
            self.state = 1891 
            localctx.exp = self.python_expression(0)
            self.state = 1892
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 316
        self.enterRecursionRule(localctx, 316, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1895 
            localctx.name = self.python_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1902
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1897
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1898
                    self.match(EParser.DOT)
                    self.state = 1899 
                    localctx.name = self.python_identifier() 
                self.state = 1904
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonDecimalLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonBooleanLiteral(self)



    def python_literal_expression(self):

        localctx = EParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_python_literal_expression)
        try:
            self.state = 1910
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1905
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1906
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1907
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1908
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1909
                localctx.t = self.match(EParser.CHAR_LITERAL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def getRuleIndex(self):
            return EParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = EParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1912
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (EParser.SYMBOL_IDENTIFIER - 138)) | (1 << (EParser.TYPE_IDENTIFIER - 138)) | (1 << (EParser.VARIABLE_IDENTIFIER - 138)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(EParser.Java_statementContext, self).copyFrom(ctx)



    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_statementContext)
            super(EParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaStatement(self)


    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_statementContext)
            super(EParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaReturnStatement(self)



    def java_statement(self):

        localctx = EParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_java_statement)
        try:
            self.state = 1921
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1914
                self.match(EParser.RETURN)
                self.state = 1915 
                localctx.exp = self.java_expression(0)
                self.state = 1916
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1918 
                localctx.exp = self.java_expression(0)
                self.state = 1919
                self.match(EParser.SEMI)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(EParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaPrimaryExpression(self)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(EParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaSelectorExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 324
        self.enterRecursionRule(localctx, 324, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1924 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1930
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,143,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 1926
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1927 
                    localctx.child = self.java_selector_expression() 
                self.state = 1932
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,143,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_primary_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_primary_expressionContext, self).copyFrom(ctx)



    class JavaIdentifierExpressionContext(Java_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_primary_expressionContext)
            super(EParser.JavaIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIdentifierExpression(self)


    class JavaLiteralExpressionContext(Java_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_primary_expressionContext)
            super(EParser.JavaLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Java_literal_expressionContext
            self.copyFrom(ctx)

        def java_literal_expression(self):
            return self.getTypedRuleContext(EParser.Java_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaLiteralExpression(self)


    class JavaParenthesisExpressionContext(Java_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_primary_expressionContext)
            super(EParser.JavaParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Java_parenthesis_expressionContext
            self.copyFrom(ctx)

        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Java_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaParenthesisExpression(self)



    def java_primary_expression(self):

        localctx = EParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_java_primary_expression)
        try:
            self.state = 1936
            token = self._input.LA(1)
            if token in [EParser.LPAR]:
                localctx = EParser.JavaParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1933 
                localctx.exp = self.java_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.JavaIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1934 
                localctx.exp = self.java_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1935 
                localctx.exp = self.java_literal_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_selector_expressionContext)
            super(EParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(EParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_selector_expressionContext)
            super(EParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(EParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = EParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_java_selector_expression)
        try:
            self.state = 1941
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1938
                self.match(EParser.DOT)
                self.state = 1939 
                localctx.exp = self.java_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1940 
                localctx.exp = self.java_item_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(EParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = EParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1943 
            localctx.name = self.java_identifier()
            self.state = 1944
            self.match(EParser.LPAR)
            self.state = 1946
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (EParser.BOOLEAN_LITERAL - 134)) | (1 << (EParser.CHAR_LITERAL - 134)) | (1 << (EParser.SYMBOL_IDENTIFIER - 134)) | (1 << (EParser.TYPE_IDENTIFIER - 134)) | (1 << (EParser.VARIABLE_IDENTIFIER - 134)) | (1 << (EParser.TEXT_LITERAL - 134)) | (1 << (EParser.INTEGER_LITERAL - 134)) | (1 << (EParser.DECIMAL_LITERAL - 134)))) != 0):
                self.state = 1945 
                localctx.args = self.java_arguments(0)


            self.state = 1948
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaArgumentList(self)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(EParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaArgumentListItem(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 332
        self.enterRecursionRule(localctx, 332, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1951 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1958
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,147,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 1953
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1954
                    self.match(EParser.COMMA)
                    self.state = 1955 
                    localctx.item = self.java_expression(0) 
                self.state = 1960
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,147,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = EParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1961
            self.match(EParser.LBRAK)
            self.state = 1962 
            localctx.exp = self.java_expression(0)
            self.state = 1963
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = EParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1965
            self.match(EParser.LPAR)
            self.state = 1966 
            localctx.exp = self.java_expression(0)
            self.state = 1967
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_identifier_expressionContext)
            super(EParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_identifier_expressionContext)
            super(EParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 338
        self.enterRecursionRule(localctx, 338, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1970 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1977
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,148,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 1972
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1973
                    self.match(EParser.DOT)
                    self.state = 1974 
                    localctx.name = self.java_identifier() 
                self.state = 1979
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,148,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def DOLLAR(self):
            return self.getToken(EParser.DOLLAR, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildClassIdentifier(self)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 340
        self.enterRecursionRule(localctx, 340, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1981 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1988
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,149,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 1983
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1984
                    self.match(EParser.DOLLAR)
                    self.state = 1985
                    localctx.name = self.match(EParser.TYPE_IDENTIFIER) 
                self.state = 1990
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,149,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaDecimalLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaTextLiteral(self)



    def java_literal_expression(self):

        localctx = EParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_java_literal_expression)
        try:
            self.state = 1996
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1991
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1992
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1993
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1994
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1995
                localctx.t = self.match(EParser.CHAR_LITERAL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def getRuleIndex(self):
            return EParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = EParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1998
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (EParser.SYMBOL_IDENTIFIER - 138)) | (1 << (EParser.TYPE_IDENTIFIER - 138)) | (1 << (EParser.VARIABLE_IDENTIFIER - 138)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_statementContext)
            super(EParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpStatement(self)


    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_statementContext)
            super(EParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpReturnStatement(self)



    def csharp_statement(self):

        localctx = EParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_csharp_statement)
        try:
            self.state = 2007
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2000
                self.match(EParser.RETURN)
                self.state = 2001 
                localctx.exp = self.csharp_expression(0)
                self.state = 2002
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2004 
                localctx.exp = self.csharp_expression(0)
                self.state = 2005
                self.match(EParser.SEMI)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPrimaryExpression(self)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpSelectorExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 348
        self.enterRecursionRule(localctx, 348, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2010 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2016
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2012
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2013 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2018
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_primary_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_primary_expressionContext, self).copyFrom(ctx)



    class CSharpLiteralExpressionContext(Csharp_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_primary_expressionContext)
            super(EParser.CSharpLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_literal_expressionContext
            self.copyFrom(ctx)

        def csharp_literal_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpLiteralExpression(self)


    class CSharpParenthesisExpressionContext(Csharp_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_primary_expressionContext)
            super(EParser.CSharpParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_parenthesis_expressionContext
            self.copyFrom(ctx)

        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpParenthesisExpression(self)


    class CSharpIdentifierExpressionContext(Csharp_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_primary_expressionContext)
            super(EParser.CSharpIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIdentifierExpression(self)



    def csharp_primary_expression(self):

        localctx = EParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_csharp_primary_expression)
        try:
            self.state = 2022
            token = self._input.LA(1)
            if token in [EParser.LPAR]:
                localctx = EParser.CSharpParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2019 
                localctx.exp = self.csharp_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2020 
                localctx.exp = self.csharp_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2021 
                localctx.exp = self.csharp_literal_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpItemExpression(self)


    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpMethodExpression(self)



    def csharp_selector_expression(self):

        localctx = EParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_csharp_selector_expression)
        try:
            self.state = 2027
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2024
                self.match(EParser.DOT)
                self.state = 2025 
                localctx.exp = self.csharp_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2026 
                localctx.exp = self.csharp_item_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(EParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = EParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2029 
            localctx.name = self.csharp_identifier()
            self.state = 2030
            self.match(EParser.LPAR)
            self.state = 2032
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (EParser.BOOLEAN_LITERAL - 134)) | (1 << (EParser.CHAR_LITERAL - 134)) | (1 << (EParser.SYMBOL_IDENTIFIER - 134)) | (1 << (EParser.TYPE_IDENTIFIER - 134)) | (1 << (EParser.VARIABLE_IDENTIFIER - 134)) | (1 << (EParser.TEXT_LITERAL - 134)) | (1 << (EParser.INTEGER_LITERAL - 134)) | (1 << (EParser.DECIMAL_LITERAL - 134)))) != 0):
                self.state = 2031 
                localctx.args = self.csharp_arguments(0)


            self.state = 2034
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_argumentsContext)
            super(EParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_argumentsContext)
            super(EParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(EParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 356
        self.enterRecursionRule(localctx, 356, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2037 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2044
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2039
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2040
                    self.match(EParser.COMMA)
                    self.state = 2041 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2046
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = EParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2047
            self.match(EParser.LBRAK)
            self.state = 2048 
            localctx.exp = self.csharp_expression(0)
            self.state = 2049
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = EParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2051
            self.match(EParser.LPAR)
            self.state = 2052 
            localctx.exp = self.csharp_expression(0)
            self.state = 2053
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpChildIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 362
        self.enterRecursionRule(localctx, 362, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2056 
            localctx.name = self.csharp_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2063
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2058
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2059
                    self.match(EParser.DOT)
                    self.state = 2060 
                    localctx.name = self.csharp_identifier() 
                self.state = 2065
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = EParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_csharp_literal_expression)
        try:
            self.state = 2071
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2066
                self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2067
                self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2068
                self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2069
                self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2070
                self.match(EParser.CHAR_LITERAL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = EParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2073
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (EParser.SYMBOL_IDENTIFIER - 138)) | (1 << (EParser.TYPE_IDENTIFIER - 138)) | (1 << (EParser.VARIABLE_IDENTIFIER - 138)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.native_category_mapping_list_sempred
        self._predicates[32] = self.else_if_statement_list_sempred
        self._predicates[37] = self.expression_sempred
        self._predicates[38] = self.unresolved_expression_sempred
        self._predicates[39] = self.unresolved_selector_sempred
        self._predicates[41] = self.invocation_trailer_sempred
        self._predicates[42] = self.instance_expression_sempred
        self._predicates[43] = self.instance_selector_sempred
        self._predicates[51] = self.argument_assignment_list_sempred
        self._predicates[52] = self.with_argument_assignment_list_sempred
        self._predicates[55] = self.child_instance_sempred
        self._predicates[63] = self.declarations_sempred
        self._predicates[67] = self.native_symbol_list_sempred
        self._predicates[68] = self.category_symbol_list_sempred
        self._predicates[69] = self.symbol_list_sempred
        self._predicates[73] = self.expression_list_sempred
        self._predicates[75] = self.typedef_sempred
        self._predicates[82] = self.type_identifier_list_sempred
        self._predicates[88] = self.argument_list_sempred
        self._predicates[94] = self.any_type_sempred
        self._predicates[95] = self.category_method_declaration_list_sempred
        self._predicates[100] = self.module_token_sempred
        self._predicates[103] = self.variable_identifier_list_sempred
        self._predicates[105] = self.native_statement_list_sempred
        self._predicates[109] = self.statement_list_sempred
        self._predicates[110] = self.switch_case_statement_list_sempred
        self._predicates[111] = self.catch_statement_list_sempred
        self._predicates[114] = self.literal_list_literal_sempred
        self._predicates[122] = self.expression_tuple_sempred
        self._predicates[123] = self.dict_entry_list_sempred
        self._predicates[127] = self.assignable_instance_sempred
        self._predicates[128] = self.is_expression_sempred
        self._predicates[130] = self.key_token_sempred
        self._predicates[131] = self.value_token_sempred
        self._predicates[132] = self.symbols_token_sempred
        self._predicates[139] = self.javascript_expression_sempred
        self._predicates[143] = self.javascript_arguments_sempred
        self._predicates[146] = self.javascript_identifier_expression_sempred
        self._predicates[150] = self.python_expression_sempred
        self._predicates[155] = self.python_ordinal_argument_list_sempred
        self._predicates[156] = self.python_named_argument_list_sempred
        self._predicates[158] = self.python_identifier_expression_sempred
        self._predicates[162] = self.java_expression_sempred
        self._predicates[166] = self.java_arguments_sempred
        self._predicates[169] = self.java_identifier_expression_sempred
        self._predicates[170] = self.java_class_identifier_expression_sempred
        self._predicates[174] = self.csharp_expression_sempred
        self._predicates[178] = self.csharp_arguments_sempred
        self._predicates[181] = self.csharp_identifier_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def native_category_mapping_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 19)
         

    def unresolved_expression_sempred(self, localctx, predIndex):
            if predIndex == 28:
                return self.precpred(self._ctx, 1)
         

    def unresolved_selector_sempred(self, localctx, predIndex):
            if predIndex == 29:
                return self.wasNot(EParser.WS)
         

    def invocation_trailer_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.willBe(EParser.LF)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.wasNot(EParser.WS)
         

            if predIndex == 33:
                return self.wasNot(EParser.WS)
         

            if predIndex == 34:
                return self.wasNot(EParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.was(EParser.WS)
         

    def with_argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.wasNot(EParser.WS)
         

            if predIndex == 38:
                return self.wasNot(EParser.WS)
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def category_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.willBeAOrAn()
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.precpred(self._ctx, 1)
         

    def javascript_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 78:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 79:
                return self.precpred(self._ctx, 1)
         



