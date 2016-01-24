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
        buf.write(u"\u00a7\u08d3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc\t\u00bc\4\u00bd")
        buf.write(u"\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf\4\u00c0\t\u00c0")
        buf.write(u"\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3\t\u00c3\4\u00c4")
        buf.write(u"\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6\4\u00c7\t\u00c7")
        buf.write(u"\4\u00c8\t\u00c8\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0197\n")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\5\2\u019e\n\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u01bc")
        buf.write(u"\n\5\3\6\3\6\3\6\3\6\5\6\u01c2\n\6\3\6\3\6\3\6\5\6\u01c7")
        buf.write(u"\n\6\3\7\3\7\3\7\3\7\5\7\u01cd\n\7\3\7\3\7\5\7\u01d1")
        buf.write(u"\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01dc\n")
        buf.write(u"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01e5\n\7\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01f4")
        buf.write(u"\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01fd\n\b\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\5\t\u0204\n\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\5\n\u020e\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u022c\n\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0237\n\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0245")
        buf.write(u"\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\5\16\u0253\n\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0261\n\16\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\7\20\u0273\n\20\f\20\16\20\u0276")
        buf.write(u"\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0280")
        buf.write(u"\n\21\5\21\u0282\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write(u"\22\5\22\u028b\n\22\3\22\3\22\5\22\u028f\n\22\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\5\23\u0297\n\23\3\23\3\23\5\23")
        buf.write(u"\u029b\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\5\24\u02aa\n\24\3\24\3\24\5\24")
        buf.write(u"\u02ae\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u02c9\n\25\3\26\3")
        buf.write(u"\26\3\27\3\27\3\27\5\27\u02d0\n\27\3\30\3\30\3\30\5\30")
        buf.write(u"\u02d5\n\30\3\30\3\30\5\30\u02d9\n\30\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\5\31\u02ec\n\31\3\32\3\32\3\32\3\33")
        buf.write(u"\3\33\5\33\u02f3\n\33\3\33\5\33\u02f6\n\33\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0317\n")
        buf.write(u"\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u032a\n\37\3")
        buf.write(u" \3 \3 \3 \3 \5 \u0331\n \3 \3 \3 \3 \3 \3 \3 \3!\3!")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#")
        buf.write(u"\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0353\n#\3#\3#\3#\3#\3#\3")
        buf.write(u"#\3#\5#\u035c\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$")
        buf.write(u"\3$\3$\3$\3$\3$\3$\3$\7$\u0371\n$\f$\16$\u0374\13$\3")
        buf.write(u"%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0383\n&\3&")
        buf.write(u"\3&\3&\5&\u0388\n&\3&\3&\3&\3&\3&\3&\5&\u0390\n&\3&\3")
        buf.write(u"&\3&\3&\3&\3&\3&\5&\u0399\n&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\5\'\u03b0\n\'\3(\3(\5(\u03b4\n(\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\5)\u03d0\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\7)\u0437\n)\f)\16)\u043a\13)\3*\3*\3*\3")
        buf.write(u"*\3*\7*\u0441\n*\f*\16*\u0444\13*\3+\3+\3+\3+\3,\3,\3")
        buf.write(u",\3,\3,\3-\3-\3.\3.\3.\3.\3.\7.\u0456\n.\f.\16.\u0459")
        buf.write(u"\13.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0468")
        buf.write(u"\n/\3\60\3\60\3\61\3\61\3\61\3\61\5\61\u0470\n\61\3\61")
        buf.write(u"\3\61\3\61\5\61\u0475\n\61\5\61\u0477\n\61\3\61\3\61")
        buf.write(u"\3\61\3\61\5\61\u047d\n\61\5\61\u047f\n\61\5\61\u0481")
        buf.write(u"\n\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write(u"\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\3\65\5\65\u049b\n\65\3\65\3\65\3\65\3")
        buf.write(u"\65\3\65\5\65\u04a2\n\65\3\65\5\65\u04a5\n\65\3\65\3")
        buf.write(u"\65\3\65\3\65\5\65\u04ab\n\65\3\65\3\65\5\65\u04af\n")
        buf.write(u"\65\3\65\3\65\3\65\5\65\u04b4\n\65\5\65\u04b6\n\65\3")
        buf.write(u"\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u04bf\n\66\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\5\67\u04c6\n\67\5\67\u04c8\n\67")
        buf.write(u"\3\67\3\67\3\67\5\67\u04cd\n\67\5\67\u04cf\n\67\38\3")
        buf.write(u"8\38\38\38\38\38\78\u04d8\n8\f8\168\u04db\138\39\39\3")
        buf.write(u"9\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\5;\u04ed\n;")
        buf.write(u"\3<\3<\3<\3<\3=\7=\u04f4\n=\f=\16=\u04f7\13=\3>\6>\u04fa")
        buf.write(u"\n>\r>\16>\u04fb\3?\6?\u04ff\n?\r?\16?\u0500\3?\3?\3")
        buf.write(u"@\7@\u0506\n@\f@\16@\u0509\13@\3@\3@\3A\3A\3B\5B\u0510")
        buf.write(u"\nB\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\7C\u051c\nC\fC\16C")
        buf.write(u"\u051f\13C\3D\3D\3D\7D\u0524\nD\fD\16D\u0527\13D\3D\3")
        buf.write(u"D\3D\3D\3D\5D\u052e\nD\3E\3E\3F\3F\5F\u0534\nF\3G\3G")
        buf.write(u"\3G\3G\3G\3G\3G\7G\u053d\nG\fG\16G\u0540\13G\3H\3H\3")
        buf.write(u"H\3H\3H\3H\3H\7H\u0549\nH\fH\16H\u054c\13H\3I\3I\3I\3")
        buf.write(u"I\3I\3I\7I\u0554\nI\fI\16I\u0557\13I\3J\3J\3J\3J\3J\3")
        buf.write(u"J\3J\3J\3J\3J\5J\u0563\nJ\3K\3K\5K\u0567\nK\3K\3K\3L")
        buf.write(u"\3L\5L\u056d\nL\3L\3L\3M\3M\3M\3M\3M\3M\7M\u0577\nM\f")
        buf.write(u"M\16M\u057a\13M\3N\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3")
        buf.write(u"O\3O\3O\3O\3O\7O\u058d\nO\fO\16O\u0590\13O\3P\3P\5P\u0594")
        buf.write(u"\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u05a4")
        buf.write(u"\nQ\3R\3R\3S\5S\u05a9\nS\3S\3S\3T\3T\3U\3U\3U\5U\u05b2")
        buf.write(u"\nU\3V\3V\3V\3V\3V\3V\7V\u05ba\nV\fV\16V\u05bd\13V\3")
        buf.write(u"W\3W\5W\u05c1\nW\3X\3X\3X\5X\u05c6\nX\3Y\3Y\3Z\3Z\3[")
        buf.write(u"\3[\3\\\3\\\3\\\3\\\3\\\3\\\7\\\u05d4\n\\\f\\\16\\\u05d7")
        buf.write(u"\13\\\3]\3]\5]\u05db\n]\3]\5]\u05de\n]\3^\3^\5^\u05e2")
        buf.write(u"\n^\3_\3_\3_\5_\u05e7\n_\3`\3`\3`\3a\3a\5a\u05ee\na\3")
        buf.write(u"b\3b\3b\3b\3b\3b\3b\3b\3b\7b\u05f9\nb\fb\16b\u05fc\13")
        buf.write(u"b\3c\3c\3c\3c\3c\3c\3c\7c\u0605\nc\fc\16c\u0608\13c\3")
        buf.write(u"d\3d\3d\3d\3d\5d\u060f\nd\3e\3e\3e\3e\3e\3e\3e\7e\u0618")
        buf.write(u"\ne\fe\16e\u061b\13e\3f\3f\5f\u061f\nf\3g\3g\3g\3g\3")
        buf.write(u"g\3g\3g\3g\3g\3g\5g\u062b\ng\3h\3h\5h\u062f\nh\3i\3i")
        buf.write(u"\3i\3i\3i\3i\7i\u0637\ni\fi\16i\u063a\13i\3j\3j\3j\3")
        buf.write(u"k\3k\5k\u0641\nk\3l\3l\3l\3l\5l\u0647\nl\3l\3l\3l\7l")
        buf.write(u"\u064c\nl\fl\16l\u064f\13l\3l\3l\5l\u0653\nl\3m\3m\3")
        buf.write(u"m\3m\3m\3m\7m\u065b\nm\fm\16m\u065e\13m\3n\3n\3n\3n\5")
        buf.write(u"n\u0664\nn\3o\3o\3p\3p\3p\3p\3p\3p\3p\7p\u066f\np\fp")
        buf.write(u"\16p\u0672\13p\3q\3q\3q\3q\3q\3q\3q\3q\3q\3q\5q\u067e")
        buf.write(u"\nq\3r\3r\5r\u0682\nr\3r\5r\u0685\nr\3s\3s\5s\u0689\n")
        buf.write(u"s\3s\5s\u068c\ns\3t\3t\3t\3t\3t\3t\3t\7t\u0695\nt\ft")
        buf.write(u"\16t\u0698\13t\3u\3u\3u\3u\3u\3u\3u\7u\u06a1\nu\fu\16")
        buf.write(u"u\u06a4\13u\3v\3v\3v\3v\3v\3v\3v\7v\u06ad\nv\fv\16v\u06b0")
        buf.write(u"\13v\3w\3w\3w\3w\3w\3w\3w\7w\u06b9\nw\fw\16w\u06bc\13")
        buf.write(u"w\3x\3x\3x\3x\3x\3x\3x\3x\3x\3x\3x\3x\3x\3x\5x\u06cc")
        buf.write(u"\nx\3y\3y\3y\3y\3y\3y\3y\3y\3y\3y\3y\3y\3y\5y\u06db\n")
        buf.write(u"y\3z\3z\3z\3z\3z\3z\7z\u06e3\nz\fz\16z\u06e6\13z\3{\3")
        buf.write(u"{\3{\3{\5{\u06ec\n{\3|\3|\3}\3}\3}\3}\3~\3~\5~\u06f6")
        buf.write(u"\n~\3\177\3\177\3\177\3\177\3\177\5\177\u06fd\n\177\3")
        buf.write(u"\u0080\3\u0080\5\u0080\u0701\n\u0080\3\u0080\3\u0080")
        buf.write(u"\3\u0081\3\u0081\5\u0081\u0707\n\u0081\3\u0081\3\u0081")
        buf.write(u"\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\7\u0082")
        buf.write(u"\u0711\n\u0082\f\u0082\16\u0082\u0714\13\u0082\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\7\u0083\u071c")
        buf.write(u"\n\u0083\f\u0083\16\u0083\u071f\13\u0083\3\u0084\3\u0084")
        buf.write(u"\3\u0084\3\u0084\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\3\u0085\5\u0085\u072e\n\u0085")
        buf.write(u"\3\u0086\3\u0086\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0087\7\u0087\u0739\n\u0087\f\u0087\16\u0087")
        buf.write(u"\u073c\13\u0087\3\u0088\3\u0088\3\u0088\3\u0088\5\u0088")
        buf.write(u"\u0742\n\u0088\3\u0089\3\u0089\3\u0089\7\u0089\u0747")
        buf.write(u"\n\u0089\f\u0089\16\u0089\u074a\13\u0089\3\u008a\3\u008a")
        buf.write(u"\3\u008a\7\u008a\u074f\n\u008a\f\u008a\16\u008a\u0752")
        buf.write(u"\13\u008a\3\u008a\5\u008a\u0755\n\u008a\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b\u075d\n\u008b")
        buf.write(u"\3\u008c\3\u008c\3\u008c\3\u008d\3\u008d\3\u008d\3\u008e")
        buf.write(u"\3\u008e\3\u008e\3\u008f\3\u008f\3\u008f\3\u0090\3\u0090")
        buf.write(u"\3\u0091\3\u0091\3\u0092\3\u0092\3\u0093\3\u0093\3\u0094")
        buf.write(u"\3\u0094\3\u0095\3\u0095\3\u0095\3\u0095\3\u0095\3\u0095")
        buf.write(u"\3\u0095\5\u0095\u077c\n\u0095\3\u0096\3\u0096\3\u0096")
        buf.write(u"\3\u0096\3\u0096\7\u0096\u0783\n\u0096\f\u0096\16\u0096")
        buf.write(u"\u0786\13\u0096\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097")
        buf.write(u"\3\u0097\3\u0097\5\u0097\u078f\n\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0099\3\u0099\3\u0099\3\u009a\3\u009a\3\u009a\3\u009a")
        buf.write(u"\3\u009a\5\u009a\u079b\n\u009a\3\u009b\3\u009b\3\u009b")
        buf.write(u"\5\u009b\u07a0\n\u009b\3\u009b\3\u009b\3\u009c\3\u009c")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\7\u009c\u07aa\n\u009c")
        buf.write(u"\f\u009c\16\u009c\u07ad\13\u009c\3\u009d\3\u009d\3\u009d")
        buf.write(u"\3\u009d\3\u009e\3\u009e\3\u009e\3\u009e\3\u009f\3\u009f")
        buf.write(u"\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u07be")
        buf.write(u"\n\u00a0\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a2\5\u00a2")
        buf.write(u"\u07c5\n\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\7\u00a3\u07cc\n\u00a3\f\u00a3\16\u00a3\u07cf\13\u00a3")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a4\3\u00a4\5\u00a4\u07d5\n\u00a4")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\5\u00a5")
        buf.write(u"\u07dd\n\u00a5\3\u00a6\3\u00a6\3\u00a6\5\u00a6\u07e2")
        buf.write(u"\n\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a7\5\u00a7\u07ec\n\u00a7\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\3\u00a8\7\u00a8\u07f4\n\u00a8")
        buf.write(u"\f\u00a8\16\u00a8\u07f7\13\u00a8\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\7\u00a9\u0804\n\u00a9\f\u00a9\16\u00a9\u0807")
        buf.write(u"\13\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\5\u00ab\u0810\n\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\7\u00ab\u0815\n\u00ab\f\u00ab\16\u00ab\u0818\13\u00ab")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\5\u00ac\u081f")
        buf.write(u"\n\u00ac\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u082a\n\u00ae\3\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00af\3\u00af\7\u00af\u0831\n\u00af")
        buf.write(u"\f\u00af\16\u00af\u0834\13\u00af\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\5\u00b0\u083b\n\u00b0\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3\5\u00b3")
        buf.write(u"\u0845\n\u00b3\3\u00b4\3\u00b4\3\u00b4\5\u00b4\u084a")
        buf.write(u"\n\u00b4\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\7\u00b5\u0854\n\u00b5\f\u00b5\16\u00b5")
        buf.write(u"\u0857\13\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\7\u00b8\u0867\n\u00b8\f\u00b8\16\u00b8")
        buf.write(u"\u086a\13\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write(u"\7\u00b9\u0871\n\u00b9\f\u00b9\16\u00b9\u0874\13\u00b9")
        buf.write(u"\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\5\u00ba\u087b")
        buf.write(u"\n\u00ba\3\u00bb\3\u00bb\3\u00bc\3\u00bc\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bc\5\u00bc\u0886\n\u00bc\3\u00bd")
        buf.write(u"\3\u00bd\3\u00bd\3\u00bd\3\u00bd\7\u00bd\u088d\n\u00bd")
        buf.write(u"\f\u00bd\16\u00bd\u0890\13\u00bd\3\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00be\3\u00be\5\u00be\u0897\n\u00be\3\u00bf\3\u00bf")
        buf.write(u"\3\u00c0\3\u00c0\3\u00c0\3\u00c1\3\u00c1\3\u00c1\5\u00c1")
        buf.write(u"\u08a1\n\u00c1\3\u00c2\3\u00c2\3\u00c2\5\u00c2\u08a6")
        buf.write(u"\n\u00c2\3\u00c2\3\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write(u"\3\u00c3\3\u00c3\7\u00c3\u08b0\n\u00c3\f\u00c3\16\u00c3")
        buf.write(u"\u08b3\13\u00c3\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c5")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c6\3\u00c6\3\u00c6\5\u00c6")
        buf.write(u"\u08c0\n\u00c6\3\u00c6\3\u00c6\3\u00c6\7\u00c6\u08c5")
        buf.write(u"\n\u00c6\f\u00c6\16\u00c6\u08c8\13\u00c6\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c7\3\u00c7\5\u00c7\u08cf\n\u00c7\3\u00c8")
        buf.write(u"\3\u00c8\3\u00c8\2*\36FPRZn\u0084\u008c\u008e\u0090\u0098")
        buf.write(u"\u009c\u00aa\u00b6\u00c2\u00c4\u00c8\u00d8\u00de\u00e6")
        buf.write(u"\u00e8\u00ea\u00ec\u00f2\u0102\u0104\u010c\u012a\u0136")
        buf.write(u"\u0144\u014e\u0150\u0154\u015c\u0168\u016e\u0170\u0178")
        buf.write(u"\u0184\u018a\u00c9\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write(u"\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl")
        buf.write(u"nprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write(u"\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0")
        buf.write(u"\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2")
        buf.write(u"\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4")
        buf.write(u"\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6")
        buf.write(u"\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8")
        buf.write(u"\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa")
        buf.write(u"\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c")
        buf.write(u"\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e")
        buf.write(u"\u0120\u0122\u0124\u0126\u0128\u012a\u012c\u012e\u0130")
        buf.write(u"\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142")
        buf.write(u"\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154")
        buf.write(u"\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166")
        buf.write(u"\u0168\u016a\u016c\u016e\u0170\u0172\u0174\u0176\u0178")
        buf.write(u"\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a")
        buf.write(u"\u018c\u018e\2\n\3\2\"#\4\2\u0085\u0085\u008d\u008d\4")
        buf.write(u"\2IIXX\4\2\'\'oo\b\2\64<\177\177\u008c\u008c\u0096\u0096")
        buf.write(u"\u009b\u009d\u009f\u009f\b\2\64<\177\177\u0085\u0085")
        buf.write(u"\u008c\u008d\u0096\u0096\u009b\u009d\7\2\64<\177\177")
        buf.write(u"\u008c\u008c\u0096\u0096\u009b\u009f\7\2\64<\177\177")
        buf.write(u"\u008c\u008c\u0096\u0096\u009b\u009d\u094a\2\u0190\3")
        buf.write(u"\2\2\2\4\u01a5\3\2\2\2\6\u01b1\3\2\2\2\b\u01b7\3\2\2")
        buf.write(u"\2\n\u01bd\3\2\2\2\f\u01c8\3\2\2\2\16\u01e6\3\2\2\2\20")
        buf.write(u"\u0203\3\2\2\2\22\u0205\3\2\2\2\24\u0215\3\2\2\2\26\u021e")
        buf.write(u"\3\2\2\2\30\u0227\3\2\2\2\32\u0246\3\2\2\2\34\u0262\3")
        buf.write(u"\2\2\2\36\u026b\3\2\2\2 \u0281\3\2\2\2\"\u0283\3\2\2")
        buf.write(u"\2$\u0290\3\2\2\2&\u02a2\3\2\2\2(\u02b5\3\2\2\2*\u02ca")
        buf.write(u"\3\2\2\2,\u02cc\3\2\2\2.\u02d1\3\2\2\2\60\u02eb\3\2\2")
        buf.write(u"\2\62\u02ed\3\2\2\2\64\u02f5\3\2\2\2\66\u02f7\3\2\2\2")
        buf.write(u"8\u0300\3\2\2\2:\u0309\3\2\2\2<\u0329\3\2\2\2>\u032b")
        buf.write(u"\3\2\2\2@\u0339\3\2\2\2B\u0342\3\2\2\2D\u0349\3\2\2\2")
        buf.write(u"F\u035d\3\2\2\2H\u0375\3\2\2\2J\u0378\3\2\2\2L\u03af")
        buf.write(u"\3\2\2\2N\u03b1\3\2\2\2P\u03cf\3\2\2\2R\u043b\3\2\2\2")
        buf.write(u"T\u0445\3\2\2\2V\u0449\3\2\2\2X\u044e\3\2\2\2Z\u0450")
        buf.write(u"\3\2\2\2\\\u0467\3\2\2\2^\u0469\3\2\2\2`\u0480\3\2\2")
        buf.write(u"\2b\u0482\3\2\2\2d\u0486\3\2\2\2f\u048b\3\2\2\2h\u04b5")
        buf.write(u"\3\2\2\2j\u04b7\3\2\2\2l\u04ce\3\2\2\2n\u04d0\3\2\2\2")
        buf.write(u"p\u04dc\3\2\2\2r\u04e0\3\2\2\2t\u04ec\3\2\2\2v\u04ee")
        buf.write(u"\3\2\2\2x\u04f5\3\2\2\2z\u04f9\3\2\2\2|\u04fe\3\2\2\2")
        buf.write(u"~\u0507\3\2\2\2\u0080\u050c\3\2\2\2\u0082\u050f\3\2\2")
        buf.write(u"\2\u0084\u0514\3\2\2\2\u0086\u0525\3\2\2\2\u0088\u052f")
        buf.write(u"\3\2\2\2\u008a\u0533\3\2\2\2\u008c\u0535\3\2\2\2\u008e")
        buf.write(u"\u0541\3\2\2\2\u0090\u054d\3\2\2\2\u0092\u0562\3\2\2")
        buf.write(u"\2\u0094\u0564\3\2\2\2\u0096\u056a\3\2\2\2\u0098\u0570")
        buf.write(u"\3\2\2\2\u009a\u057b\3\2\2\2\u009c\u0581\3\2\2\2\u009e")
        buf.write(u"\u0593\3\2\2\2\u00a0\u05a3\3\2\2\2\u00a2\u05a5\3\2\2")
        buf.write(u"\2\u00a4\u05a8\3\2\2\2\u00a6\u05ac\3\2\2\2\u00a8\u05b1")
        buf.write(u"\3\2\2\2\u00aa\u05b3\3\2\2\2\u00ac\u05c0\3\2\2\2\u00ae")
        buf.write(u"\u05c5\3\2\2\2\u00b0\u05c7\3\2\2\2\u00b2\u05c9\3\2\2")
        buf.write(u"\2\u00b4\u05cb\3\2\2\2\u00b6\u05cd\3\2\2\2\u00b8\u05dd")
        buf.write(u"\3\2\2\2\u00ba\u05e1\3\2\2\2\u00bc\u05e3\3\2\2\2\u00be")
        buf.write(u"\u05e8\3\2\2\2\u00c0\u05ed\3\2\2\2\u00c2\u05ef\3\2\2")
        buf.write(u"\2\u00c4\u05fd\3\2\2\2\u00c6\u060e\3\2\2\2\u00c8\u0610")
        buf.write(u"\3\2\2\2\u00ca\u061e\3\2\2\2\u00cc\u062a\3\2\2\2\u00ce")
        buf.write(u"\u062c\3\2\2\2\u00d0\u0630\3\2\2\2\u00d2\u063b\3\2\2")
        buf.write(u"\2\u00d4\u063e\3\2\2\2\u00d6\u0642\3\2\2\2\u00d8\u0654")
        buf.write(u"\3\2\2\2\u00da\u0663\3\2\2\2\u00dc\u0665\3\2\2\2\u00de")
        buf.write(u"\u0667\3\2\2\2\u00e0\u067d\3\2\2\2\u00e2\u067f\3\2\2")
        buf.write(u"\2\u00e4\u0686\3\2\2\2\u00e6\u068d\3\2\2\2\u00e8\u0699")
        buf.write(u"\3\2\2\2\u00ea\u06a5\3\2\2\2\u00ec\u06b1\3\2\2\2\u00ee")
        buf.write(u"\u06cb\3\2\2\2\u00f0\u06da\3\2\2\2\u00f2\u06dc\3\2\2")
        buf.write(u"\2\u00f4\u06eb\3\2\2\2\u00f6\u06ed\3\2\2\2\u00f8\u06ef")
        buf.write(u"\3\2\2\2\u00fa\u06f5\3\2\2\2\u00fc\u06fc\3\2\2\2\u00fe")
        buf.write(u"\u06fe\3\2\2\2\u0100\u0704\3\2\2\2\u0102\u070a\3\2\2")
        buf.write(u"\2\u0104\u0715\3\2\2\2\u0106\u0720\3\2\2\2\u0108\u072d")
        buf.write(u"\3\2\2\2\u010a\u072f\3\2\2\2\u010c\u0733\3\2\2\2\u010e")
        buf.write(u"\u0741\3\2\2\2\u0110\u0743\3\2\2\2\u0112\u074b\3\2\2")
        buf.write(u"\2\u0114\u075c\3\2\2\2\u0116\u075e\3\2\2\2\u0118\u0761")
        buf.write(u"\3\2\2\2\u011a\u0764\3\2\2\2\u011c\u0767\3\2\2\2\u011e")
        buf.write(u"\u076a\3\2\2\2\u0120\u076c\3\2\2\2\u0122\u076e\3\2\2")
        buf.write(u"\2\u0124\u0770\3\2\2\2\u0126\u0772\3\2\2\2\u0128\u077b")
        buf.write(u"\3\2\2\2\u012a\u077d\3\2\2\2\u012c\u078e\3\2\2\2\u012e")
        buf.write(u"\u0790\3\2\2\2\u0130\u0792\3\2\2\2\u0132\u079a\3\2\2")
        buf.write(u"\2\u0134\u079c\3\2\2\2\u0136\u07a3\3\2\2\2\u0138\u07ae")
        buf.write(u"\3\2\2\2\u013a\u07b2\3\2\2\2\u013c\u07b6\3\2\2\2\u013e")
        buf.write(u"\u07bd\3\2\2\2\u0140\u07bf\3\2\2\2\u0142\u07c4\3\2\2")
        buf.write(u"\2\u0144\u07c6\3\2\2\2\u0146\u07d4\3\2\2\2\u0148\u07dc")
        buf.write(u"\3\2\2\2\u014a\u07de\3\2\2\2\u014c\u07eb\3\2\2\2\u014e")
        buf.write(u"\u07ed\3\2\2\2\u0150\u07f8\3\2\2\2\u0152\u0808\3\2\2")
        buf.write(u"\2\u0154\u080f\3\2\2\2\u0156\u081e\3\2\2\2\u0158\u0820")
        buf.write(u"\3\2\2\2\u015a\u0829\3\2\2\2\u015c\u082b\3\2\2\2\u015e")
        buf.write(u"\u083a\3\2\2\2\u0160\u083c\3\2\2\2\u0162\u083e\3\2\2")
        buf.write(u"\2\u0164\u0844\3\2\2\2\u0166\u0846\3\2\2\2\u0168\u084d")
        buf.write(u"\3\2\2\2\u016a\u0858\3\2\2\2\u016c\u085c\3\2\2\2\u016e")
        buf.write(u"\u0860\3\2\2\2\u0170\u086b\3\2\2\2\u0172\u087a\3\2\2")
        buf.write(u"\2\u0174\u087c\3\2\2\2\u0176\u0885\3\2\2\2\u0178\u0887")
        buf.write(u"\3\2\2\2\u017a\u0896\3\2\2\2\u017c\u0898\3\2\2\2\u017e")
        buf.write(u"\u089a\3\2\2\2\u0180\u08a0\3\2\2\2\u0182\u08a2\3\2\2")
        buf.write(u"\2\u0184\u08a9\3\2\2\2\u0186\u08b4\3\2\2\2\u0188\u08b8")
        buf.write(u"\3\2\2\2\u018a\u08bf\3\2\2\2\u018c\u08ce\3\2\2\2\u018e")
        buf.write(u"\u08d0\3\2\2\2\u0190\u0191\7W\2\2\u0191\u0192\5\u00b2")
        buf.write(u"Z\2\u0192\u0193\7H\2\2\u0193\u0196\7^\2\2\u0194\u0197")
        buf.write(u"\7Q\2\2\u0195\u0197\5\u00b2Z\2\u0196\u0194\3\2\2\2\u0196")
        buf.write(u"\u0195\3\2\2\2\u0197\u019d\3\2\2\2\u0198\u0199\5 \21")
        buf.write(u"\2\u0199\u019a\7\23\2\2\u019a\u019b\7F\2\2\u019b\u019e")
        buf.write(u"\3\2\2\2\u019c\u019e\7\u0092\2\2\u019d\u0198\3\2\2\2")
        buf.write(u"\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0")
        buf.write(u"\5\u011c\u008f\2\u01a0\u01a1\7\21\2\2\u01a1\u01a2\5|")
        buf.write(u"?\2\u01a2\u01a3\5\u008eH\2\u01a3\u01a4\5~@\2\u01a4\3")
        buf.write(u"\3\2\2\2\u01a5\u01a6\7W\2\2\u01a6\u01a7\5\u00b2Z\2\u01a7")
        buf.write(u"\u01a8\7H\2\2\u01a8\u01a9\7^\2\2\u01a9\u01aa\5\u00a0")
        buf.write(u"Q\2\u01aa\u01ab\7\u0092\2\2\u01ab\u01ac\5\u011c\u008f")
        buf.write(u"\2\u01ac\u01ad\7\21\2\2\u01ad\u01ae\5|?\2\u01ae\u01af")
        buf.write(u"\5\u008cG\2\u01af\u01b0\5~@\2\u01b0\5\3\2\2\2\u01b1\u01b2")
        buf.write(u"\5\u00b4[\2\u01b2\u01b3\7\u0092\2\2\u01b3\u01b4\5P)\2")
        buf.write(u"\u01b4\u01b5\7H\2\2\u01b5\u01b6\5\u011a\u008e\2\u01b6")
        buf.write(u"\7\3\2\2\2\u01b7\u01b8\5\u00b4[\2\u01b8\u01bb\5n8\2\u01b9")
        buf.write(u"\u01ba\7F\2\2\u01ba\u01bc\5p9\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write(u"\u01bc\3\2\2\2\u01bc\t\3\2\2\2\u01bd\u01be\7W\2\2\u01be")
        buf.write(u"\u01bf\5\u00b0Y\2\u01bf\u01c1\7H\2\2\u01c0\u01c2\7\u0089")
        buf.write(u"\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3")
        buf.write(u"\3\2\2\2\u01c3\u01c4\5\u009cO\2\u01c4\u01c6\7K\2\2\u01c5")
        buf.write(u"\u01c7\5\u0092J\2\u01c6\u01c5\3\2\2\2\u01c6\u01c7\3\2")
        buf.write(u"\2\2\u01c7\13\3\2\2\2\u01c8\u01c9\7W\2\2\u01c9\u01ca")
        buf.write(u"\5\u00b2Z\2\u01ca\u01cc\7H\2\2\u01cb\u01cd\7\u0089\2")
        buf.write(u"\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0")
        buf.write(u"\3\2\2\2\u01ce\u01d1\7Q\2\2\u01cf\u01d1\5\20\t\2\u01d0")
        buf.write(u"\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01e4\3\2\2")
        buf.write(u"\2\u01d2\u01db\5 \21\2\u01d3\u01d4\7\23\2\2\u01d4\u01d5")
        buf.write(u"\7F\2\2\u01d5\u01d6\7n\2\2\u01d6\u01d7\7\21\2\2\u01d7")
        buf.write(u"\u01d8\5|?\2\u01d8\u01d9\5\u00c4c\2\u01d9\u01da\5~@\2")
        buf.write(u"\u01da\u01dc\3\2\2\2\u01db\u01d3\3\2\2\2\u01db\u01dc")
        buf.write(u"\3\2\2\2\u01dc\u01e5\3\2\2\2\u01dd\u01de\7\u0092\2\2")
        buf.write(u"\u01de\u01df\7n\2\2\u01df\u01e0\7\21\2\2\u01e0\u01e1")
        buf.write(u"\5|?\2\u01e1\u01e2\5\u00c4c\2\u01e2\u01e3\5~@\2\u01e3")
        buf.write(u"\u01e5\3\2\2\2\u01e4\u01d2\3\2\2\2\u01e4\u01dd\3\2\2")
        buf.write(u"\2\u01e4\u01e5\3\2\2\2\u01e5\r\3\2\2\2\u01e6\u01e7\7")
        buf.write(u"W\2\2\u01e7\u01e8\5\u00b2Z\2\u01e8\u01e9\7H\2\2\u01e9")
        buf.write(u"\u01fc\7\u0087\2\2\u01ea\u01f3\5 \21\2\u01eb\u01ec\7")
        buf.write(u"\23\2\2\u01ec\u01ed\7F\2\2\u01ed\u01ee\7n\2\2\u01ee\u01ef")
        buf.write(u"\7\21\2\2\u01ef\u01f0\5|?\2\u01f0\u01f1\5\u00c4c\2\u01f1")
        buf.write(u"\u01f2\5~@\2\u01f2\u01f4\3\2\2\2\u01f3\u01eb\3\2\2\2")
        buf.write(u"\u01f3\u01f4\3\2\2\2\u01f4\u01fd\3\2\2\2\u01f5\u01f6")
        buf.write(u"\7\u0092\2\2\u01f6\u01f7\7n\2\2\u01f7\u01f8\7\21\2\2")
        buf.write(u"\u01f8\u01f9\5|?\2\u01f9\u01fa\5\u00c4c\2\u01fa\u01fb")
        buf.write(u"\5~@\2\u01fb\u01fd\3\2\2\2\u01fc\u01ea\3\2\2\2\u01fc")
        buf.write(u"\u01f5\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\17\3\2\2\2\u01fe")
        buf.write(u"\u0204\5\u00aaV\2\u01ff\u0200\5\u00aaV\2\u0200\u0201")
        buf.write(u"\7F\2\2\u0201\u0202\5\u00b2Z\2\u0202\u0204\3\2\2\2\u0203")
        buf.write(u"\u01fe\3\2\2\2\u0203\u01ff\3\2\2\2\u0204\21\3\2\2\2\u0205")
        buf.write(u"\u0206\7W\2\2\u0206\u0207\5\u0114\u008b\2\u0207\u0208")
        buf.write(u"\7H\2\2\u0208\u0209\7y\2\2\u0209\u020a\7\u0080\2\2\u020a")
        buf.write(u"\u020d\5\u00ba^\2\u020b\u020c\7\u0083\2\2\u020c\u020e")
        buf.write(u"\5\u009cO\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e")
        buf.write(u"\u020f\3\2\2\2\u020f\u0210\7Z\2\2\u0210\u0211\7\21\2")
        buf.write(u"\2\u0211\u0212\5|?\2\u0212\u0213\5\u00e6t\2\u0213\u0214")
        buf.write(u"\5~@\2\u0214\23\3\2\2\2\u0215\u0216\7W\2\2\u0216\u0217")
        buf.write(u"\5\u00b0Y\2\u0217\u0218\7\u0086\2\2\u0218\u0219\7Z\2")
        buf.write(u"\2\u0219\u021a\7\21\2\2\u021a\u021b\5|?\2\u021b\u021c")
        buf.write(u"\5\u00e6t\2\u021c\u021d\5~@\2\u021d\25\3\2\2\2\u021e")
        buf.write(u"\u021f\7W\2\2\u021f\u0220\5\u00b0Y\2\u0220\u0221\7g\2")
        buf.write(u"\2\u0221\u0222\7Z\2\2\u0222\u0223\7\21\2\2\u0223\u0224")
        buf.write(u"\5|?\2\u0224\u0225\5\u00e6t\2\u0225\u0226\5~@\2\u0226")
        buf.write(u"\27\3\2\2\2\u0227\u0228\7W\2\2\u0228\u0229\5\u00b2Z\2")
        buf.write(u"\u0229\u022b\7H\2\2\u022a\u022c\7\u0089\2\2\u022b\u022a")
        buf.write(u"\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write(u"\u022e\7q\2\2\u022e\u0236\7Q\2\2\u022f\u0230\5 \21\2")
        buf.write(u"\u0230\u0231\7\23\2\2\u0231\u0232\7F\2\2\u0232\u0233")
        buf.write(u"\7M\2\2\u0233\u0237\3\2\2\2\u0234\u0235\7\u0092\2\2\u0235")
        buf.write(u"\u0237\7M\2\2\u0236\u022f\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write(u"\u0237\u0238\3\2\2\2\u0238\u0239\7\21\2\2\u0239\u023a")
        buf.write(u"\5|?\2\u023a\u023b\5\34\17\2\u023b\u0244\5~@\2\u023c")
        buf.write(u"\u023d\5z>\2\u023d\u023e\7F\2\2\u023e\u023f\7n\2\2\u023f")
        buf.write(u"\u0240\7\21\2\2\u0240\u0241\5|?\2\u0241\u0242\5\u00c8")
        buf.write(u"e\2\u0242\u0243\5~@\2\u0243\u0245\3\2\2\2\u0244\u023c")
        buf.write(u"\3\2\2\2\u0244\u0245\3\2\2\2\u0245\31\3\2\2\2\u0246\u0247")
        buf.write(u"\7W\2\2\u0247\u0248\5\u00b2Z\2\u0248\u0249\7H\2\2\u0249")
        buf.write(u"\u024a\7q\2\2\u024a\u0252\7\u0081\2\2\u024b\u024c\5 ")
        buf.write(u"\21\2\u024c\u024d\7\23\2\2\u024d\u024e\7F\2\2\u024e\u024f")
        buf.write(u"\7M\2\2\u024f\u0253\3\2\2\2\u0250\u0251\7\u0092\2\2\u0251")
        buf.write(u"\u0253\7M\2\2\u0252\u024b\3\2\2\2\u0252\u0250\3\2\2\2")
        buf.write(u"\u0253\u0254\3\2\2\2\u0254\u0255\7\21\2\2\u0255\u0256")
        buf.write(u"\5|?\2\u0256\u0257\5\34\17\2\u0257\u0260\5~@\2\u0258")
        buf.write(u"\u0259\5z>\2\u0259\u025a\7F\2\2\u025a\u025b\7n\2\2\u025b")
        buf.write(u"\u025c\7\21\2\2\u025c\u025d\5|?\2\u025d\u025e\5\u00c8")
        buf.write(u"e\2\u025e\u025f\5~@\2\u025f\u0261\3\2\2\2\u0260\u0258")
        buf.write(u"\3\2\2\2\u0260\u0261\3\2\2\2\u0261\33\3\2\2\2\u0262\u0263")
        buf.write(u"\7W\2\2\u0263\u0264\7Q\2\2\u0264\u0265\7M\2\2\u0265\u0266")
        buf.write(u"\7H\2\2\u0266\u0267\7\21\2\2\u0267\u0268\5|?\2\u0268")
        buf.write(u"\u0269\5\36\20\2\u0269\u026a\5~@\2\u026a\35\3\2\2\2\u026b")
        buf.write(u"\u026c\b\20\1\2\u026c\u026d\5\u00ccg\2\u026d\u0274\3")
        buf.write(u"\2\2\2\u026e\u026f\f\3\2\2\u026f\u0270\5z>\2\u0270\u0271")
        buf.write(u"\5\u00ccg\2\u0271\u0273\3\2\2\2\u0272\u026e\3\2\2\2\u0273")
        buf.write(u"\u0276\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0275\3\2\2")
        buf.write(u"\2\u0275\37\3\2\2\2\u0276\u0274\3\2\2\2\u0277\u0278\7")
        buf.write(u"\u0092\2\2\u0278\u0279\7K\2\2\u0279\u0282\5\u00b0Y\2")
        buf.write(u"\u027a\u027b\7\u0092\2\2\u027b\u027c\7L\2\2\u027c\u027f")
        buf.write(u"\5\u00d8m\2\u027d\u027e\7F\2\2\u027e\u0280\5\u00b0Y\2")
        buf.write(u"\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0282")
        buf.write(u"\3\2\2\2\u0281\u0277\3\2\2\2\u0281\u027a\3\2\2\2\u0282")
        buf.write(u"!\3\2\2\2\u0283\u0284\7W\2\2\u0284\u0285\5\u00acW\2\u0285")
        buf.write(u"\u0286\7H\2\2\u0286\u0287\7C\2\2\u0287\u028a\7m\2\2\u0288")
        buf.write(u"\u0289\7\u0080\2\2\u0289\u028b\5,\27\2\u028a\u0288\3")
        buf.write(u"\2\2\2\u028a\u028b\3\2\2\2\u028b\u028e\3\2\2\2\u028c")
        buf.write(u"\u028d\7\u0083\2\2\u028d\u028f\5\u009cO\2\u028e\u028c")
        buf.write(u"\3\2\2\2\u028e\u028f\3\2\2\2\u028f#\3\2\2\2\u0290\u0291")
        buf.write(u"\7W\2\2\u0291\u0292\5\u00acW\2\u0292\u0293\7H\2\2\u0293")
        buf.write(u"\u0296\7m\2\2\u0294\u0295\7\u0080\2\2\u0295\u0297\5,")
        buf.write(u"\27\2\u0296\u0294\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u029a")
        buf.write(u"\3\2\2\2\u0298\u0299\7\u0083\2\2\u0299\u029b\5\u009c")
        buf.write(u"O\2\u029a\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029c")
        buf.write(u"\3\2\2\2\u029c\u029d\7Z\2\2\u029d\u029e\7\21\2\2\u029e")
        buf.write(u"\u029f\5|?\2\u029f\u02a0\5\u00e6t\2\u02a0\u02a1\5~@\2")
        buf.write(u"\u02a1%\3\2\2\2\u02a2\u02a3\7W\2\2\u02a3\u02a4\5\u00ac")
        buf.write(u"W\2\u02a4\u02a5\7H\2\2\u02a5\u02a6\7q\2\2\u02a6\u02a9")
        buf.write(u"\7m\2\2\u02a7\u02a8\7\u0080\2\2\u02a8\u02aa\5,\27\2\u02a9")
        buf.write(u"\u02a7\3\2\2\2\u02a9\u02aa\3\2\2\2\u02aa\u02ad\3\2\2")
        buf.write(u"\2\u02ab\u02ac\7\u0083\2\2\u02ac\u02ae\5\u00c0a\2\u02ad")
        buf.write(u"\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02af\3\2\2")
        buf.write(u"\2\u02af\u02b0\7Z\2\2\u02b0\u02b1\7\21\2\2\u02b1\u02b2")
        buf.write(u"\5|?\2\u02b2\u02b3\5\u00dep\2\u02b3\u02b4\5~@\2\u02b4")
        buf.write(u"\'\3\2\2\2\u02b5\u02b6\7W\2\2\u02b6\u02b7\7\u00a0\2\2")
        buf.write(u"\u02b7\u02b8\7H\2\2\u02b8\u02b9\7\u008c\2\2\u02b9\u02ba")
        buf.write(u"\7m\2\2\u02ba\u02bb\7Z\2\2\u02bb\u02bc\7\21\2\2\u02bc")
        buf.write(u"\u02bd\5|?\2\u02bd\u02be\5\u00e6t\2\u02be\u02bf\5~@\2")
        buf.write(u"\u02bf\u02c0\5z>\2\u02c0\u02c1\7F\2\2\u02c1\u02c8\7\u0091")
        buf.write(u"\2\2\u02c2\u02c3\7\21\2\2\u02c3\u02c4\5|?\2\u02c4\u02c5")
        buf.write(u"\5\u00e8u\2\u02c5\u02c6\5~@\2\u02c6\u02c9\3\2\2\2\u02c7")
        buf.write(u"\u02c9\5\u00b4[\2\u02c8\u02c2\3\2\2\2\u02c8\u02c7\3\2")
        buf.write(u"\2\2\u02c9)\3\2\2\2\u02ca\u02cb\5P)\2\u02cb+\3\2\2\2")
        buf.write(u"\u02cc\u02cf\5\u00b6\\\2\u02cd\u02ce\7F\2\2\u02ce\u02d0")
        buf.write(u"\5\u00b8]\2\u02cf\u02cd\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0")
        buf.write(u"-\3\2\2\2\u02d1\u02d2\5\u00c0a\2\u02d2\u02d4\5\u00b0")
        buf.write(u"Y\2\u02d3\u02d5\5 \21\2\u02d4\u02d3\3\2\2\2\u02d4\u02d5")
        buf.write(u"\3\2\2\2\u02d5\u02d8\3\2\2\2\u02d6\u02d7\7-\2\2\u02d7")
        buf.write(u"\u02d9\5\u00fa~\2\u02d8\u02d6\3\2\2\2\u02d8\u02d9\3\2")
        buf.write(u"\2\2\u02d9/\3\2\2\2\u02da\u02ec\5r:\2\u02db\u02ec\5\64")
        buf.write(u"\33\2\u02dc\u02ec\5v<\2\u02dd\u02ec\5\62\32\2\u02de\u02ec")
        buf.write(u"\5N(\2\u02df\u02ec\5D#\2\u02e0\u02ec\5:\36\2\u02e1\u02ec")
        buf.write(u"\5> \2\u02e2\u02ec\5B\"\2\u02e3\u02ec\5@!\2\u02e4\u02ec")
        buf.write(u"\5H%\2\u02e5\u02ec\5J&\2\u02e6\u02ec\5d\63\2\u02e7\u02ec")
        buf.write(u"\5\66\34\2\u02e8\u02ec\58\35\2\u02e9\u02ec\5$\23\2\u02ea")
        buf.write(u"\u02ec\5\u00dco\2\u02eb\u02da\3\2\2\2\u02eb\u02db\3\2")
        buf.write(u"\2\2\u02eb\u02dc\3\2\2\2\u02eb\u02dd\3\2\2\2\u02eb\u02de")
        buf.write(u"\3\2\2\2\u02eb\u02df\3\2\2\2\u02eb\u02e0\3\2\2\2\u02eb")
        buf.write(u"\u02e1\3\2\2\2\u02eb\u02e2\3\2\2\2\u02eb\u02e3\3\2\2")
        buf.write(u"\2\u02eb\u02e4\3\2\2\2\u02eb\u02e5\3\2\2\2\u02eb\u02e6")
        buf.write(u"\3\2\2\2\u02eb\u02e7\3\2\2\2\u02eb\u02e8\3\2\2\2\u02eb")
        buf.write(u"\u02e9\3\2\2\2\u02eb\u02ea\3\2\2\2\u02ec\61\3\2\2\2\u02ed")
        buf.write(u"\u02ee\7\u008a\2\2\u02ee\u02ef\5\u0098M\2\u02ef\63\3")
        buf.write(u"\2\2\2\u02f0\u02f2\5R*\2\u02f1\u02f3\5l\67\2\u02f2\u02f1")
        buf.write(u"\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u02f6\3\2\2\2\u02f4")
        buf.write(u"\u02f6\5V,\2\u02f5\u02f0\3\2\2\2\u02f5\u02f4\3\2\2\2")
        buf.write(u"\u02f6\65\3\2\2\2\u02f7\u02f8\7\u0092\2\2\u02f8\u02f9")
        buf.write(u"\5\u010a\u0086\2\u02f9\u02fa\7\23\2\2\u02fa\u02fb\7Y")
        buf.write(u"\2\2\u02fb\u02fc\7\21\2\2\u02fc\u02fd\5|?\2\u02fd\u02fe")
        buf.write(u"\5\u00e6t\2\u02fe\u02ff\5~@\2\u02ff\67\3\2\2\2\u0300")
        buf.write(u"\u0301\7\u0092\2\2\u0301\u0302\5\u00b2Z\2\u0302\u0303")
        buf.write(u"\7\23\2\2\u0303\u0304\7Y\2\2\u0304\u0305\7\21\2\2\u0305")
        buf.write(u"\u0306\5|?\2\u0306\u0307\5\u00e6t\2\u0307\u0308\5~@\2")
        buf.write(u"\u03089\3\2\2\2\u0309\u030a\7\u008b\2\2\u030a\u030b\7")
        buf.write(u"v\2\2\u030b\u030c\5P)\2\u030c\u030d\7\21\2\2\u030d\u030e")
        buf.write(u"\5|?\2\u030e\u0316\5\u00eav\2\u030f\u0310\5z>\2\u0310")
        buf.write(u"\u0311\7|\2\2\u0311\u0312\7\21\2\2\u0312\u0313\5|?\2")
        buf.write(u"\u0313\u0314\5\u00e6t\2\u0314\u0315\5~@\2\u0315\u0317")
        buf.write(u"\3\2\2\2\u0316\u030f\3\2\2\2\u0316\u0317\3\2\2\2\u0317")
        buf.write(u"\u0318\3\2\2\2\u0318\u0319\5~@\2\u0319;\3\2\2\2\u031a")
        buf.write(u"\u031b\7\u0093\2\2\u031b\u031c\5\u00f0y\2\u031c\u031d")
        buf.write(u"\7\21\2\2\u031d\u031e\5|?\2\u031e\u031f\5\u00e6t\2\u031f")
        buf.write(u"\u0320\5~@\2\u0320\u032a\3\2\2\2\u0321\u0322\7\u0093")
        buf.write(u"\2\2\u0322\u0323\7i\2\2\u0323\u0324\5\u00eex\2\u0324")
        buf.write(u"\u0325\7\21\2\2\u0325\u0326\5|?\2\u0326\u0327\5\u00e6")
        buf.write(u"t\2\u0327\u0328\5~@\2\u0328\u032a\3\2\2\2\u0329\u031a")
        buf.write(u"\3\2\2\2\u0329\u0321\3\2\2\2\u032a=\3\2\2\2\u032b\u032c")
        buf.write(u"\7e\2\2\u032c\u032d\7[\2\2\u032d\u0330\5\u00b0Y\2\u032e")
        buf.write(u"\u032f\7\23\2\2\u032f\u0331\5\u00b0Y\2\u0330\u032e\3")
        buf.write(u"\2\2\2\u0330\u0331\3\2\2\2\u0331\u0332\3\2\2\2\u0332")
        buf.write(u"\u0333\7i\2\2\u0333\u0334\5P)\2\u0334\u0335\7\21\2\2")
        buf.write(u"\u0335\u0336\5|?\2\u0336\u0337\5\u00e6t\2\u0337\u0338")
        buf.write(u"\5~@\2\u0338?\3\2\2\2\u0339\u033a\7Y\2\2\u033a\u033b")
        buf.write(u"\7\21\2\2\u033b\u033c\5|?\2\u033c\u033d\5\u00e6t\2\u033d")
        buf.write(u"\u033e\5~@\2\u033e\u033f\5z>\2\u033f\u0340\7\u0095\2")
        buf.write(u"\2\u0340\u0341\5P)\2\u0341A\3\2\2\2\u0342\u0343\7\u0095")
        buf.write(u"\2\2\u0343\u0344\5P)\2\u0344\u0345\7\21\2\2\u0345\u0346")
        buf.write(u"\5|?\2\u0346\u0347\5\u00e6t\2\u0347\u0348\5~@\2\u0348")
        buf.write(u"C\3\2\2\2\u0349\u034a\7h\2\2\u034a\u034b\5P)\2\u034b")
        buf.write(u"\u034c\7\21\2\2\u034c\u034d\5|?\2\u034d\u034e\5\u00e6")
        buf.write(u"t\2\u034e\u0352\5~@\2\u034f\u0350\5z>\2\u0350\u0351\5")
        buf.write(u"F$\2\u0351\u0353\3\2\2\2\u0352\u034f\3\2\2\2\u0352\u0353")
        buf.write(u"\3\2\2\2\u0353\u035b\3\2\2\2\u0354\u0355\5z>\2\u0355")
        buf.write(u"\u0356\7\\\2\2\u0356\u0357\7\21\2\2\u0357\u0358\5|?\2")
        buf.write(u"\u0358\u0359\5\u00e6t\2\u0359\u035a\5~@\2\u035a\u035c")
        buf.write(u"\3\2\2\2\u035b\u0354\3\2\2\2\u035b\u035c\3\2\2\2\u035c")
        buf.write(u"E\3\2\2\2\u035d\u035e\b$\1\2\u035e\u035f\7\\\2\2\u035f")
        buf.write(u"\u0360\7h\2\2\u0360\u0361\5P)\2\u0361\u0362\7\21\2\2")
        buf.write(u"\u0362\u0363\5|?\2\u0363\u0364\5\u00e6t\2\u0364\u0365")
        buf.write(u"\5~@\2\u0365\u0372\3\2\2\2\u0366\u0367\f\3\2\2\u0367")
        buf.write(u"\u0368\5z>\2\u0368\u0369\7\\\2\2\u0369\u036a\7h\2\2\u036a")
        buf.write(u"\u036b\5P)\2\u036b\u036c\7\21\2\2\u036c\u036d\5|?\2\u036d")
        buf.write(u"\u036e\5\u00e6t\2\u036e\u036f\5~@\2\u036f\u0371\3\2\2")
        buf.write(u"\2\u0370\u0366\3\2\2\2\u0371\u0374\3\2\2\2\u0372\u0370")
        buf.write(u"\3\2\2\2\u0372\u0373\3\2\2\2\u0373G\3\2\2\2\u0374\u0372")
        buf.write(u"\3\2\2\2\u0375\u0376\7~\2\2\u0376\u0377\5P)\2\u0377I")
        buf.write(u"\3\2\2\2\u0378\u0379\7\u008b\2\2\u0379\u037a\7v\2\2\u037a")
        buf.write(u"\u037b\5\u00b0Y\2\u037b\u037c\7Z\2\2\u037c\u037d\7\21")
        buf.write(u"\2\2\u037d\u037e\5|?\2\u037e\u037f\5\u00e6t\2\u037f\u0380")
        buf.write(u"\5~@\2\u0380\u0382\5x=\2\u0381\u0383\5\u00ecw\2\u0382")
        buf.write(u"\u0381\3\2\2\2\u0382\u0383\3\2\2\2\u0383\u038f\3\2\2")
        buf.write(u"\2\u0384\u0388\7|\2\2\u0385\u0386\7\u0093\2\2\u0386\u0388")
        buf.write(u"\7G\2\2\u0387\u0384\3\2\2\2\u0387\u0385\3\2\2\2\u0388")
        buf.write(u"\u0389\3\2\2\2\u0389\u038a\7\21\2\2\u038a\u038b\5|?\2")
        buf.write(u"\u038b\u038c\5\u00e6t\2\u038c\u038d\5~@\2\u038d\u038e")
        buf.write(u"\5x=\2\u038e\u0390\3\2\2\2\u038f\u0387\3\2\2\2\u038f")
        buf.write(u"\u0390\3\2\2\2\u0390\u0398\3\2\2\2\u0391\u0392\7E\2\2")
        buf.write(u"\u0392\u0393\7\21\2\2\u0393\u0394\5|?\2\u0394\u0395\5")
        buf.write(u"\u00e6t\2\u0395\u0396\5~@\2\u0396\u0397\5x=\2\u0397\u0399")
        buf.write(u"\3\2\2\2\u0398\u0391\3\2\2\2\u0398\u0399\3\2\2\2\u0399")
        buf.write(u"\u039a\3\2\2\2\u039a\u039b\5x=\2\u039bK\3\2\2\2\u039c")
        buf.write(u"\u039d\7\u0093\2\2\u039d\u039e\5\u00b4[\2\u039e\u039f")
        buf.write(u"\7\21\2\2\u039f\u03a0\5|?\2\u03a0\u03a1\5\u00e6t\2\u03a1")
        buf.write(u"\u03a2\5~@\2\u03a2\u03a3\5x=\2\u03a3\u03b0\3\2\2\2\u03a4")
        buf.write(u"\u03a5\7\u0093\2\2\u03a5\u03a6\7i\2\2\u03a6\u03a7\7\30")
        buf.write(u"\2\2\u03a7\u03a8\5\u0090I\2\u03a8\u03a9\7\31\2\2\u03a9")
        buf.write(u"\u03aa\7\21\2\2\u03aa\u03ab\5|?\2\u03ab\u03ac\5\u00e6")
        buf.write(u"t\2\u03ac\u03ad\5~@\2\u03ad\u03ae\5x=\2\u03ae\u03b0\3")
        buf.write(u"\2\2\2\u03af\u039c\3\2\2\2\u03af\u03a4\3\2\2\2\u03b0")
        buf.write(u"M\3\2\2\2\u03b1\u03b3\7\u0082\2\2\u03b2\u03b4\5P)\2\u03b3")
        buf.write(u"\u03b2\3\2\2\2\u03b3\u03b4\3\2\2\2\u03b4O\3\2\2\2\u03b5")
        buf.write(u"\u03b6\b)\1\2\u03b6\u03b7\7#\2\2\u03b7\u03d0\5P))\u03b8")
        buf.write(u"\u03b9\7s\2\2\u03b9\u03d0\5P)(\u03ba\u03bb\7>\2\2\u03bb")
        buf.write(u"\u03bc\7\21\2\2\u03bc\u03d0\5P)\r\u03bd\u03d0\5Z.\2\u03be")
        buf.write(u"\u03d0\5R*\2\u03bf\u03c0\5R*\2\u03c0\u03c1\5l\67\2\u03c1")
        buf.write(u"\u03d0\3\2\2\2\u03c2\u03c3\7`\2\2\u03c3\u03c4\7\21\2")
        buf.write(u"\2\u03c4\u03d0\5\u00b0Y\2\u03c5\u03c6\7=\2\2\u03c6\u03c7")
        buf.write(u"\7\21\2\2\u03c7\u03d0\5\u00acW\2\u03c8\u03d0\5^\60\2")
        buf.write(u"\u03c9\u03d0\5`\61\2\u03ca\u03d0\5h\65\2\u03cb\u03d0")
        buf.write(u"\5b\62\2\u03cc\u03d0\5j\66\2\u03cd\u03d0\5f\64\2\u03ce")
        buf.write(u"\u03d0\5V,\2\u03cf\u03b5\3\2\2\2\u03cf\u03b8\3\2\2\2")
        buf.write(u"\u03cf\u03ba\3\2\2\2\u03cf\u03bd\3\2\2\2\u03cf\u03be")
        buf.write(u"\3\2\2\2\u03cf\u03bf\3\2\2\2\u03cf\u03c2\3\2\2\2\u03cf")
        buf.write(u"\u03c5\3\2\2\2\u03cf\u03c8\3\2\2\2\u03cf\u03c9\3\2\2")
        buf.write(u"\2\u03cf\u03ca\3\2\2\2\u03cf\u03cb\3\2\2\2\u03cf\u03cc")
        buf.write(u"\3\2\2\2\u03cf\u03cd\3\2\2\2\u03cf\u03ce\3\2\2\2\u03d0")
        buf.write(u"\u0438\3\2\2\2\u03d1\u03d2\f\'\2\2\u03d2\u03d3\5\u0120")
        buf.write(u"\u0091\2\u03d3\u03d4\5P)(\u03d4\u0437\3\2\2\2\u03d5\u03d6")
        buf.write(u"\f&\2\2\u03d6\u03d7\5\u0122\u0092\2\u03d7\u03d8\5P)\'")
        buf.write(u"\u03d8\u0437\3\2\2\2\u03d9\u03da\f%\2\2\u03da\u03db\5")
        buf.write(u"\u0126\u0094\2\u03db\u03dc\5P)&\u03dc\u0437\3\2\2\2\u03dd")
        buf.write(u"\u03de\f$\2\2\u03de\u03df\5\u0124\u0093\2\u03df\u03e0")
        buf.write(u"\5P)%\u03e0\u0437\3\2\2\2\u03e1\u03e2\f#\2\2\u03e2\u03e3")
        buf.write(u"\t\2\2\2\u03e3\u0437\5P)$\u03e4\u03e5\f\"\2\2\u03e5\u03e6")
        buf.write(u"\7*\2\2\u03e6\u0437\5P)#\u03e7\u03e8\f!\2\2\u03e8\u03e9")
        buf.write(u"\7+\2\2\u03e9\u0437\5P)\"\u03ea\u03eb\f \2\2\u03eb\u03ec")
        buf.write(u"\7(\2\2\u03ec\u0437\5P)!\u03ed\u03ee\f\37\2\2\u03ee\u03ef")
        buf.write(u"\7)\2\2\u03ef\u0437\5P) \u03f0\u03f1\f\34\2\2\u03f1\u03f2")
        buf.write(u"\7-\2\2\u03f2\u0437\5P)\35\u03f3\u03f4\f\33\2\2\u03f4")
        buf.write(u"\u03f5\7,\2\2\u03f5\u0437\5P)\34\u03f6\u03f7\f\32\2\2")
        buf.write(u"\u03f7\u03f8\7\61\2\2\u03f8\u0437\5P)\33\u03f9\u03fa")
        buf.write(u"\f\31\2\2\u03fa\u03fb\7z\2\2\u03fb\u0437\5P)\32\u03fc")
        buf.write(u"\u03fd\f\30\2\2\u03fd\u03fe\7F\2\2\u03fe\u0437\5P)\31")
        buf.write(u"\u03ff\u0400\f\27\2\2\u0400\u0401\7h\2\2\u0401\u0402")
        buf.write(u"\5P)\2\u0402\u0403\7\\\2\2\u0403\u0404\5P)\30\u0404\u0437")
        buf.write(u"\3\2\2\2\u0405\u0406\f\25\2\2\u0406\u0407\7i\2\2\u0407")
        buf.write(u"\u0437\5P)\26\u0408\u0409\f\24\2\2\u0409\u040a\7T\2\2")
        buf.write(u"\u040a\u0437\5P)\25\u040b\u040c\f\23\2\2\u040c\u040d")
        buf.write(u"\7T\2\2\u040d\u040e\7D\2\2\u040e\u0437\5P)\24\u040f\u0410")
        buf.write(u"\f\22\2\2\u0410\u0411\7T\2\2\u0411\u0412\7G\2\2\u0412")
        buf.write(u"\u0437\5P)\23\u0413\u0414\f\21\2\2\u0414\u0415\7s\2\2")
        buf.write(u"\u0415\u0416\7i\2\2\u0416\u0437\5P)\22\u0417\u0418\f")
        buf.write(u"\20\2\2\u0418\u0419\7s\2\2\u0419\u041a\7T\2\2\u041a\u0437")
        buf.write(u"\5P)\21\u041b\u041c\f\17\2\2\u041c\u041d\7s\2\2\u041d")
        buf.write(u"\u041e\7T\2\2\u041e\u041f\7D\2\2\u041f\u0437\5P)\20\u0420")
        buf.write(u"\u0421\f\16\2\2\u0421\u0422\7s\2\2\u0422\u0423\7T\2\2")
        buf.write(u"\u0423\u0424\7G\2\2\u0424\u0437\5P)\17\u0425\u0426\f")
        buf.write(u"\3\2\2\u0426\u0427\7e\2\2\u0427\u0428\7[\2\2\u0428\u0429")
        buf.write(u"\5\u00b0Y\2\u0429\u042a\7i\2\2\u042a\u042b\5P)\4\u042b")
        buf.write(u"\u0437\3\2\2\2\u042c\u042d\f\36\2\2\u042d\u042e\7k\2")
        buf.write(u"\2\u042e\u042f\7s\2\2\u042f\u0437\5\u010e\u0088\2\u0430")
        buf.write(u"\u0431\f\35\2\2\u0431\u0432\7k\2\2\u0432\u0437\5\u010e")
        buf.write(u"\u0088\2\u0433\u0434\f\26\2\2\u0434\u0435\7H\2\2\u0435")
        buf.write(u"\u0437\5\u00c0a\2\u0436\u03d1\3\2\2\2\u0436\u03d5\3\2")
        buf.write(u"\2\2\u0436\u03d9\3\2\2\2\u0436\u03dd\3\2\2\2\u0436\u03e1")
        buf.write(u"\3\2\2\2\u0436\u03e4\3\2\2\2\u0436\u03e7\3\2\2\2\u0436")
        buf.write(u"\u03ea\3\2\2\2\u0436\u03ed\3\2\2\2\u0436\u03f0\3\2\2")
        buf.write(u"\2\u0436\u03f3\3\2\2\2\u0436\u03f6\3\2\2\2\u0436\u03f9")
        buf.write(u"\3\2\2\2\u0436\u03fc\3\2\2\2\u0436\u03ff\3\2\2\2\u0436")
        buf.write(u"\u0405\3\2\2\2\u0436\u0408\3\2\2\2\u0436\u040b\3\2\2")
        buf.write(u"\2\u0436\u040f\3\2\2\2\u0436\u0413\3\2\2\2\u0436\u0417")
        buf.write(u"\3\2\2\2\u0436\u041b\3\2\2\2\u0436\u0420\3\2\2\2\u0436")
        buf.write(u"\u0425\3\2\2\2\u0436\u042c\3\2\2\2\u0436\u0430\3\2\2")
        buf.write(u"\2\u0436\u0433\3\2\2\2\u0437\u043a\3\2\2\2\u0438\u0436")
        buf.write(u"\3\2\2\2\u0438\u0439\3\2\2\2\u0439Q\3\2\2\2\u043a\u0438")
        buf.write(u"\3\2\2\2\u043b\u043c\b*\1\2\u043c\u043d\5\u00aeX\2\u043d")
        buf.write(u"\u0442\3\2\2\2\u043e\u043f\f\3\2\2\u043f\u0441\5T+\2")
        buf.write(u"\u0440\u043e\3\2\2\2\u0441\u0444\3\2\2\2\u0442\u0440")
        buf.write(u"\3\2\2\2\u0442\u0443\3\2\2\2\u0443S\3\2\2\2\u0444\u0442")
        buf.write(u"\3\2\2\2\u0445\u0446\6+ \3\u0446\u0447\7\25\2\2\u0447")
        buf.write(u"\u0448\5\u00aeX\2\u0448U\3\2\2\2\u0449\u044a\7j\2\2\u044a")
        buf.write(u"\u044b\7\21\2\2\u044b\u044c\5\u00b0Y\2\u044c\u044d\5")
        buf.write(u"X-\2\u044dW\3\2\2\2\u044e\u044f\6-!\3\u044fY\3\2\2\2")
        buf.write(u"\u0450\u0451\b.\1\2\u0451\u0452\5\u00f4{\2\u0452\u0457")
        buf.write(u"\3\2\2\2\u0453\u0454\f\3\2\2\u0454\u0456\5\\/\2\u0455")
        buf.write(u"\u0453\3\2\2\2\u0456\u0459\3\2\2\2\u0457\u0455\3\2\2")
        buf.write(u"\2\u0457\u0458\3\2\2\2\u0458[\3\2\2\2\u0459\u0457\3\2")
        buf.write(u"\2\2\u045a\u045b\6/#\3\u045b\u045c\7\25\2\2\u045c\u0468")
        buf.write(u"\5\u00b0Y\2\u045d\u045e\6/$\3\u045e\u045f\7\30\2\2\u045f")
        buf.write(u"\u0460\5\u0108\u0085\2\u0460\u0461\7\31\2\2\u0461\u0468")
        buf.write(u"\3\2\2\2\u0462\u0463\6/%\3\u0463\u0464\7\30\2\2\u0464")
        buf.write(u"\u0465\5P)\2\u0465\u0466\7\31\2\2\u0466\u0468\3\2\2\2")
        buf.write(u"\u0467\u045a\3\2\2\2\u0467\u045d\3\2\2\2\u0467\u0462")
        buf.write(u"\3\2\2\2\u0468]\3\2\2\2\u0469\u046a\7?\2\2\u046a_\3\2")
        buf.write(u"\2\2\u046b\u046c\5\u00a4S\2\u046c\u046d\7f\2\2\u046d")
        buf.write(u"\u0476\5P)\2\u046e\u0470\7\23\2\2\u046f\u046e\3\2\2\2")
        buf.write(u"\u046f\u0470\3\2\2\2\u0470\u0471\3\2\2\2\u0471\u0474")
        buf.write(u"\5n8\2\u0472\u0473\7F\2\2\u0473\u0475\5p9\2\u0474\u0472")
        buf.write(u"\3\2\2\2\u0474\u0475\3\2\2\2\u0475\u0477\3\2\2\2\u0476")
        buf.write(u"\u046f\3\2\2\2\u0476\u0477\3\2\2\2\u0477\u0481\3\2\2")
        buf.write(u"\2\u0478\u047e\5\u00a4S\2\u0479\u047c\5n8\2\u047a\u047b")
        buf.write(u"\7F\2\2\u047b\u047d\5p9\2\u047c\u047a\3\2\2\2\u047c\u047d")
        buf.write(u"\3\2\2\2\u047d\u047f\3\2\2\2\u047e\u0479\3\2\2\2\u047e")
        buf.write(u"\u047f\3\2\2\2\u047f\u0481\3\2\2\2\u0480\u046b\3\2\2")
        buf.write(u"\2\u0480\u0478\3\2\2\2\u0481a\3\2\2\2\u0482\u0483\7\177")
        buf.write(u"\2\2\u0483\u0484\7f\2\2\u0484\u0485\5P)\2\u0485c\3\2")
        buf.write(u"\2\2\u0486\u0487\7\u0096\2\2\u0487\u0488\5P)\2\u0488")
        buf.write(u"\u0489\7\u008f\2\2\u0489\u048a\5P)\2\u048ae\3\2\2\2\u048b")
        buf.write(u"\u048c\5R*\2\u048c\u048d\7#\2\2\u048d\u048e\5P)\2\u048e")
        buf.write(u"g\3\2\2\2\u048f\u0490\7c\2\2\u0490\u0491\7G\2\2\u0491")
        buf.write(u"\u0492\5\u00b0Y\2\u0492\u0493\7f\2\2\u0493\u0494\5P)")
        buf.write(u"\2\u0494\u0495\7\u0094\2\2\u0495\u0496\5P)\2\u0496\u04b6")
        buf.write(u"\3\2\2\2\u0497\u0498\7c\2\2\u0498\u049a\7w\2\2\u0499")
        buf.write(u"\u049b\5\u00a4S\2\u049a\u0499\3\2\2\2\u049a\u049b\3\2")
        buf.write(u"\2\2\u049b\u049c\3\2\2\2\u049c\u049d\7\u0094\2\2\u049d")
        buf.write(u"\u04b6\5P)\2\u049e\u04aa\7c\2\2\u049f\u04a1\7D\2\2\u04a0")
        buf.write(u"\u04a2\5\u00a4S\2\u04a1\u04a0\3\2\2\2\u04a1\u04a2\3\2")
        buf.write(u"\2\2\u04a2\u04ab\3\2\2\2\u04a3\u04a5\5\u00a4S\2\u04a4")
        buf.write(u"\u04a3\3\2\2\2\u04a4\u04a5\3\2\2\2\u04a5\u04a6\3\2\2")
        buf.write(u"\2\u04a6\u04a7\5P)\2\u04a7\u04a8\7\u008f\2\2\u04a8\u04a9")
        buf.write(u"\5P)\2\u04a9\u04ab\3\2\2\2\u04aa\u049f\3\2\2\2\u04aa")
        buf.write(u"\u04a4\3\2\2\2\u04ab\u04ae\3\2\2\2\u04ac\u04ad\7\u0094")
        buf.write(u"\2\2\u04ad\u04af\5P)\2\u04ae\u04ac\3\2\2\2\u04ae\u04af")
        buf.write(u"\3\2\2\2\u04af\u04b3\3\2\2\2\u04b0\u04b1\7{\2\2\u04b1")
        buf.write(u"\u04b2\7N\2\2\u04b2\u04b4\5\u0110\u0089\2\u04b3\u04b0")
        buf.write(u"\3\2\2\2\u04b3\u04b4\3\2\2\2\u04b4\u04b6\3\2\2\2\u04b5")
        buf.write(u"\u048f\3\2\2\2\u04b5\u0497\3\2\2\2\u04b5\u049e\3\2\2")
        buf.write(u"\2\u04b6i\3\2\2\2\u04b7\u04b8\7\u0088\2\2\u04b8\u04be")
        buf.write(u"\5Z.\2\u04b9\u04ba\7\u0092\2\2\u04ba\u04bb\5Z.\2\u04bb")
        buf.write(u"\u04bc\7H\2\2\u04bc\u04bd\5\u0118\u008d\2\u04bd\u04bf")
        buf.write(u"\3\2\2\2\u04be\u04b9\3\2\2\2\u04be\u04bf\3\2\2\2\u04bf")
        buf.write(u"k\3\2\2\2\u04c0\u04c1\6\67&\3\u04c1\u04c7\5P)\2\u04c2")
        buf.write(u"\u04c5\5n8\2\u04c3\u04c4\7F\2\2\u04c4\u04c6\5p9\2\u04c5")
        buf.write(u"\u04c3\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6\u04c8\3\2\2")
        buf.write(u"\2\u04c7\u04c2\3\2\2\2\u04c7\u04c8\3\2\2\2\u04c8\u04cf")
        buf.write(u"\3\2\2\2\u04c9\u04cc\5n8\2\u04ca\u04cb\7F\2\2\u04cb\u04cd")
        buf.write(u"\5p9\2\u04cc\u04ca\3\2\2\2\u04cc\u04cd\3\2\2\2\u04cd")
        buf.write(u"\u04cf\3\2\2\2\u04ce\u04c0\3\2\2\2\u04ce\u04c9\3\2\2")
        buf.write(u"\2\u04cfm\3\2\2\2\u04d0\u04d1\b8\1\2\u04d1\u04d2\7\u0092")
        buf.write(u"\2\2\u04d2\u04d3\5p9\2\u04d3\u04d9\3\2\2\2\u04d4\u04d5")
        buf.write(u"\f\3\2\2\u04d5\u04d6\7\23\2\2\u04d6\u04d8\5p9\2\u04d7")
        buf.write(u"\u04d4\3\2\2\2\u04d8\u04db\3\2\2\2\u04d9\u04d7\3\2\2")
        buf.write(u"\2\u04d9\u04da\3\2\2\2\u04dao\3\2\2\2\u04db\u04d9\3\2")
        buf.write(u"\2\2\u04dc\u04dd\5P)\2\u04dd\u04de\7H\2\2\u04de\u04df")
        buf.write(u"\5\u00b0Y\2\u04dfq\3\2\2\2\u04e0\u04e1\5\u010c\u0087")
        buf.write(u"\2\u04e1\u04e2\5\u011e\u0090\2\u04e2\u04e3\5P)\2\u04e3")
        buf.write(u"s\3\2\2\2\u04e4\u04e5\6;(\3\u04e5\u04e6\7\25\2\2\u04e6")
        buf.write(u"\u04ed\5\u00b0Y\2\u04e7\u04e8\6;)\3\u04e8\u04e9\7\30")
        buf.write(u"\2\2\u04e9\u04ea\5P)\2\u04ea\u04eb\7\31\2\2\u04eb\u04ed")
        buf.write(u"\3\2\2\2\u04ec\u04e4\3\2\2\2\u04ec\u04e7\3\2\2\2\u04ed")
        buf.write(u"u\3\2\2\2\u04ee\u04ef\5\u00d8m\2\u04ef\u04f0\5\u011e")
        buf.write(u"\u0090\2\u04f0\u04f1\5P)\2\u04f1w\3\2\2\2\u04f2\u04f4")
        buf.write(u"\7\7\2\2\u04f3\u04f2\3\2\2\2\u04f4\u04f7\3\2\2\2\u04f5")
        buf.write(u"\u04f3\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6y\3\2\2\2\u04f7")
        buf.write(u"\u04f5\3\2\2\2\u04f8\u04fa\7\7\2\2\u04f9\u04f8\3\2\2")
        buf.write(u"\2\u04fa\u04fb\3\2\2\2\u04fb\u04f9\3\2\2\2\u04fb\u04fc")
        buf.write(u"\3\2\2\2\u04fc{\3\2\2\2\u04fd\u04ff\7\7\2\2\u04fe\u04fd")
        buf.write(u"\3\2\2\2\u04ff\u0500\3\2\2\2\u0500\u04fe\3\2\2\2\u0500")
        buf.write(u"\u0501\3\2\2\2\u0501\u0502\3\2\2\2\u0502\u0503\7\3\2")
        buf.write(u"\2\u0503}\3\2\2\2\u0504\u0506\7\7\2\2\u0505\u0504\3\2")
        buf.write(u"\2\2\u0506\u0509\3\2\2\2\u0507\u0505\3\2\2\2\u0507\u0508")
        buf.write(u"\3\2\2\2\u0508\u050a\3\2\2\2\u0509\u0507\3\2\2\2\u050a")
        buf.write(u"\u050b\7\4\2\2\u050b\177\3\2\2\2\u050c\u050d\7t\2\2\u050d")
        buf.write(u"\u0081\3\2\2\2\u050e\u0510\5\u0084C\2\u050f\u050e\3\2")
        buf.write(u"\2\2\u050f\u0510\3\2\2\2\u0510\u0511\3\2\2\2\u0511\u0512")
        buf.write(u"\5x=\2\u0512\u0513\7\2\2\3\u0513\u0083\3\2\2\2\u0514")
        buf.write(u"\u0515\bC\1\2\u0515\u0516\5\u0086D\2\u0516\u051d\3\2")
        buf.write(u"\2\2\u0517\u0518\f\3\2\2\u0518\u0519\5z>\2\u0519\u051a")
        buf.write(u"\5\u0086D\2\u051a\u051c\3\2\2\2\u051b\u0517\3\2\2\2\u051c")
        buf.write(u"\u051f\3\2\2\2\u051d\u051b\3\2\2\2\u051d\u051e\3\2\2")
        buf.write(u"\2\u051e\u0085\3\2\2\2\u051f\u051d\3\2\2\2\u0520\u0521")
        buf.write(u"\5\u00dco\2\u0521\u0522\5z>\2\u0522\u0524\3\2\2\2\u0523")
        buf.write(u"\u0520\3\2\2\2\u0524\u0527\3\2\2\2\u0525\u0523\3\2\2")
        buf.write(u"\2\u0525\u0526\3\2\2\2\u0526\u052d\3\2\2\2\u0527\u0525")
        buf.write(u"\3\2\2\2\u0528\u052e\5\n\6\2\u0529\u052e\5\u00a8U\2\u052a")
        buf.write(u"\u052e\5\u0088E\2\u052b\u052e\5\u008aF\2\u052c\u052e")
        buf.write(u"\5\u00dan\2\u052d\u0528\3\2\2\2\u052d\u0529\3\2\2\2\u052d")
        buf.write(u"\u052a\3\2\2\2\u052d\u052b\3\2\2\2\u052d\u052c\3\2\2")
        buf.write(u"\2\u052e\u0087\3\2\2\2\u052f\u0530\5\32\16\2\u0530\u0089")
        buf.write(u"\3\2\2\2\u0531\u0534\5\2\2\2\u0532\u0534\5\4\3\2\u0533")
        buf.write(u"\u0531\3\2\2\2\u0533\u0532\3\2\2\2\u0534\u008b\3\2\2")
        buf.write(u"\2\u0535\u0536\bG\1\2\u0536\u0537\5\6\4\2\u0537\u053e")
        buf.write(u"\3\2\2\2\u0538\u0539\f\3\2\2\u0539\u053a\5z>\2\u053a")
        buf.write(u"\u053b\5\6\4\2\u053b\u053d\3\2\2\2\u053c\u0538\3\2\2")
        buf.write(u"\2\u053d\u0540\3\2\2\2\u053e\u053c\3\2\2\2\u053e\u053f")
        buf.write(u"\3\2\2\2\u053f\u008d\3\2\2\2\u0540\u053e\3\2\2\2\u0541")
        buf.write(u"\u0542\bH\1\2\u0542\u0543\5\b\5\2\u0543\u054a\3\2\2\2")
        buf.write(u"\u0544\u0545\f\3\2\2\u0545\u0546\5z>\2\u0546\u0547\5")
        buf.write(u"\b\5\2\u0547\u0549\3\2\2\2\u0548\u0544\3\2\2\2\u0549")
        buf.write(u"\u054c\3\2\2\2\u054a\u0548\3\2\2\2\u054a\u054b\3\2\2")
        buf.write(u"\2\u054b\u008f\3\2\2\2\u054c\u054a\3\2\2\2\u054d\u054e")
        buf.write(u"\bI\1\2\u054e\u054f\5\u00b4[\2\u054f\u0555\3\2\2\2\u0550")
        buf.write(u"\u0551\f\3\2\2\u0551\u0552\7\23\2\2\u0552\u0554\5\u00b4")
        buf.write(u"[\2\u0553\u0550\3\2\2\2\u0554\u0557\3\2\2\2\u0555\u0553")
        buf.write(u"\3\2\2\2\u0555\u0556\3\2\2\2\u0556\u0091\3\2\2\2\u0557")
        buf.write(u"\u0555\3\2\2\2\u0558\u0559\7i\2\2\u0559\u0563\5\u0094")
        buf.write(u"K\2\u055a\u055b\7i\2\2\u055b\u0563\5\u0096L\2\u055c\u055d")
        buf.write(u"\7i\2\2\u055d\u0563\5\u009aN\2\u055e\u055f\7l\2\2\u055f")
        buf.write(u"\u0563\7\u00a0\2\2\u0560\u0561\7l\2\2\u0561\u0563\5P")
        buf.write(u")\2\u0562\u0558\3\2\2\2\u0562\u055a\3\2\2\2\u0562\u055c")
        buf.write(u"\3\2\2\2\u0562\u055e\3\2\2\2\u0562\u0560\3\2\2\2\u0563")
        buf.write(u"\u0093\3\2\2\2\u0564\u0566\7\30\2\2\u0565\u0567\5\u0098")
        buf.write(u"M\2\u0566\u0565\3\2\2\2\u0566\u0567\3\2\2\2\u0567\u0568")
        buf.write(u"\3\2\2\2\u0568\u0569\7\31\2\2\u0569\u0095\3\2\2\2\u056a")
        buf.write(u"\u056c\7*\2\2\u056b\u056d\5\u0098M\2\u056c\u056b\3\2")
        buf.write(u"\2\2\u056c\u056d\3\2\2\2\u056d\u056e\3\2\2\2\u056e\u056f")
        buf.write(u"\7(\2\2\u056f\u0097\3\2\2\2\u0570\u0571\bM\1\2\u0571")
        buf.write(u"\u0572\5P)\2\u0572\u0578\3\2\2\2\u0573\u0574\f\3\2\2")
        buf.write(u"\u0574\u0575\7\23\2\2\u0575\u0577\5P)\2\u0576\u0573\3")
        buf.write(u"\2\2\2\u0577\u057a\3\2\2\2\u0578\u0576\3\2\2\2\u0578")
        buf.write(u"\u0579\3\2\2\2\u0579\u0099\3\2\2\2\u057a\u0578\3\2\2")
        buf.write(u"\2\u057b\u057c\7\30\2\2\u057c\u057d\5P)\2\u057d\u057e")
        buf.write(u"\7\24\2\2\u057e\u057f\5P)\2\u057f\u0580\7\31\2\2\u0580")
        buf.write(u"\u009b\3\2\2\2\u0581\u0582\bO\1\2\u0582\u0583\5\u009e")
        buf.write(u"P\2\u0583\u058e\3\2\2\2\u0584\u0585\f\5\2\2\u0585\u058d")
        buf.write(u"\7,\2\2\u0586\u0587\f\4\2\2\u0587\u0588\7\30\2\2\u0588")
        buf.write(u"\u058d\7\31\2\2\u0589\u058a\f\3\2\2\u058a\u058b\7\32")
        buf.write(u"\2\2\u058b\u058d\7\33\2\2\u058c\u0584\3\2\2\2\u058c\u0586")
        buf.write(u"\3\2\2\2\u058c\u0589\3\2\2\2\u058d\u0590\3\2\2\2\u058e")
        buf.write(u"\u058c\3\2\2\2\u058e\u058f\3\2\2\2\u058f\u009d\3\2\2")
        buf.write(u"\2\u0590\u058e\3\2\2\2\u0591\u0594\5\u00a0Q\2\u0592\u0594")
        buf.write(u"\5\u00a2R\2\u0593\u0591\3\2\2\2\u0593\u0592\3\2\2\2\u0594")
        buf.write(u"\u009f\3\2\2\2\u0595\u05a4\7\64\2\2\u0596\u05a4\7\65")
        buf.write(u"\2\2\u0597\u05a4\7\66\2\2\u0598\u05a4\7A\2\2\u0599\u05a4")
        buf.write(u"\7\67\2\2\u059a\u05a4\78\2\2\u059b\u05a4\7?\2\2\u059c")
        buf.write(u"\u05a4\79\2\2\u059d\u05a4\7;\2\2\u059e\u05a4\7:\2\2\u059f")
        buf.write(u"\u05a4\7<\2\2\u05a0\u05a4\7>\2\2\u05a1\u05a4\7@\2\2\u05a2")
        buf.write(u"\u05a4\7B\2\2\u05a3\u0595\3\2\2\2\u05a3\u0596\3\2\2\2")
        buf.write(u"\u05a3\u0597\3\2\2\2\u05a3\u0598\3\2\2\2\u05a3\u0599")
        buf.write(u"\3\2\2\2\u05a3\u059a\3\2\2\2\u05a3\u059b\3\2\2\2\u05a3")
        buf.write(u"\u059c\3\2\2\2\u05a3\u059d\3\2\2\2\u05a3\u059e\3\2\2")
        buf.write(u"\2\u05a3\u059f\3\2\2\2\u05a3\u05a0\3\2\2\2\u05a3\u05a1")
        buf.write(u"\3\2\2\2\u05a3\u05a2\3\2\2\2\u05a4\u00a1\3\2\2\2\u05a5")
        buf.write(u"\u05a6\7\u009c\2\2\u05a6\u00a3\3\2\2\2\u05a7\u05a9\7")
        buf.write(u"p\2\2\u05a8\u05a7\3\2\2\2\u05a8\u05a9\3\2\2\2\u05a9\u05aa")
        buf.write(u"\3\2\2\2\u05aa\u05ab\5\u00a2R\2\u05ab\u00a5\3\2\2\2\u05ac")
        buf.write(u"\u05ad\7>\2\2\u05ad\u00a7\3\2\2\2\u05ae\u05b2\5\f\7\2")
        buf.write(u"\u05af\u05b2\5\30\r\2\u05b0\u05b2\5\16\b\2\u05b1\u05ae")
        buf.write(u"\3\2\2\2\u05b1\u05af\3\2\2\2\u05b1\u05b0\3\2\2\2\u05b2")
        buf.write(u"\u00a9\3\2\2\2\u05b3\u05b4\bV\1\2\u05b4\u05b5\5\u00b2")
        buf.write(u"Z\2\u05b5\u05bb\3\2\2\2\u05b6\u05b7\f\3\2\2\u05b7\u05b8")
        buf.write(u"\7\23\2\2\u05b8\u05ba\5\u00b2Z\2\u05b9\u05b6\3\2\2\2")
        buf.write(u"\u05ba\u05bd\3\2\2\2\u05bb\u05b9\3\2\2\2\u05bb\u05bc")
        buf.write(u"\3\2\2\2\u05bc\u00ab\3\2\2\2\u05bd\u05bb\3\2\2\2\u05be")
        buf.write(u"\u05c1\5\u00b0Y\2\u05bf\u05c1\5\u00b2Z\2\u05c0\u05be")
        buf.write(u"\3\2\2\2\u05c0\u05bf\3\2\2\2\u05c1\u00ad\3\2\2\2\u05c2")
        buf.write(u"\u05c6\5\u00b0Y\2\u05c3\u05c6\5\u00b2Z\2\u05c4\u05c6")
        buf.write(u"\5\u00b4[\2\u05c5\u05c2\3\2\2\2\u05c5\u05c3\3\2\2\2\u05c5")
        buf.write(u"\u05c4\3\2\2\2\u05c6\u00af\3\2\2\2\u05c7\u05c8\7\u009d")
        buf.write(u"\2\2\u05c8\u00b1\3\2\2\2\u05c9\u05ca\7\u009c\2\2\u05ca")
        buf.write(u"\u00b3\3\2\2\2\u05cb\u05cc\7\u009b\2\2\u05cc\u00b5\3")
        buf.write(u"\2\2\2\u05cd\u05ce\b\\\1\2\u05ce\u05cf\5\u00b8]\2\u05cf")
        buf.write(u"\u05d5\3\2\2\2\u05d0\u05d1\f\3\2\2\u05d1\u05d2\7\23\2")
        buf.write(u"\2\u05d2\u05d4\5\u00b8]\2\u05d3\u05d0\3\2\2\2\u05d4\u05d7")
        buf.write(u"\3\2\2\2\u05d5\u05d3\3\2\2\2\u05d5\u05d6\3\2\2\2\u05d6")
        buf.write(u"\u00b7\3\2\2\2\u05d7\u05d5\3\2\2\2\u05d8\u05de\5\u00be")
        buf.write(u"`\2\u05d9\u05db\7p\2\2\u05da\u05d9\3\2\2\2\u05da\u05db")
        buf.write(u"\3\2\2\2\u05db\u05dc\3\2\2\2\u05dc\u05de\5\u00ba^\2\u05dd")
        buf.write(u"\u05d8\3\2\2\2\u05dd\u05da\3\2\2\2\u05de\u00b9\3\2\2")
        buf.write(u"\2\u05df\u05e2\5\u00bc_\2\u05e0\u05e2\5.\30\2\u05e1\u05df")
        buf.write(u"\3\2\2\2\u05e1\u05e0\3\2\2\2\u05e2\u00bb\3\2\2\2\u05e3")
        buf.write(u"\u05e6\5\u00b0Y\2\u05e4\u05e5\7-\2\2\u05e5\u05e7\5\u00fa")
        buf.write(u"~\2\u05e6\u05e4\3\2\2\2\u05e6\u05e7\3\2\2\2\u05e7\u00bd")
        buf.write(u"\3\2\2\2\u05e8\u05e9\5\u00a6T\2\u05e9\u05ea\5\u00b0Y")
        buf.write(u"\2\u05ea\u00bf\3\2\2\2\u05eb\u05ee\5\u009cO\2\u05ec\u05ee")
        buf.write(u"\5\u00c2b\2\u05ed\u05eb\3\2\2\2\u05ed\u05ec\3\2\2\2\u05ee")
        buf.write(u"\u00c1\3\2\2\2\u05ef\u05f0\bb\1\2\u05f0\u05f1\7G\2\2")
        buf.write(u"\u05f1\u05fa\3\2\2\2\u05f2\u05f3\f\4\2\2\u05f3\u05f4")
        buf.write(u"\7\30\2\2\u05f4\u05f9\7\31\2\2\u05f5\u05f6\f\3\2\2\u05f6")
        buf.write(u"\u05f7\7\32\2\2\u05f7\u05f9\7\33\2\2\u05f8\u05f2\3\2")
        buf.write(u"\2\2\u05f8\u05f5\3\2\2\2\u05f9\u05fc\3\2\2\2\u05fa\u05f8")
        buf.write(u"\3\2\2\2\u05fa\u05fb\3\2\2\2\u05fb\u00c3\3\2\2\2\u05fc")
        buf.write(u"\u05fa\3\2\2\2\u05fd\u05fe\bc\1\2\u05fe\u05ff\5\u00c6")
        buf.write(u"d\2\u05ff\u0606\3\2\2\2\u0600\u0601\f\3\2\2\u0601\u0602")
        buf.write(u"\5z>\2\u0602\u0603\5\u00c6d\2\u0603\u0605\3\2\2\2\u0604")
        buf.write(u"\u0600\3\2\2\2\u0605\u0608\3\2\2\2\u0606\u0604\3\2\2")
        buf.write(u"\2\u0606\u0607\3\2\2\2\u0607\u00c5\3\2\2\2\u0608\u0606")
        buf.write(u"\3\2\2\2\u0609\u060f\5\24\13\2\u060a\u060f\5\26\f\2\u060b")
        buf.write(u"\u060f\5$\23\2\u060c\u060f\5\"\22\2\u060d\u060f\5\22")
        buf.write(u"\n\2\u060e\u0609\3\2\2\2\u060e\u060a\3\2\2\2\u060e\u060b")
        buf.write(u"\3\2\2\2\u060e\u060c\3\2\2\2\u060e\u060d\3\2\2\2\u060f")
        buf.write(u"\u00c7\3\2\2\2\u0610\u0611\be\1\2\u0611\u0612\5\u00ca")
        buf.write(u"f\2\u0612\u0619\3\2\2\2\u0613\u0614\f\3\2\2\u0614\u0615")
        buf.write(u"\5z>\2\u0615\u0616\5\u00caf\2\u0616\u0618\3\2\2\2\u0617")
        buf.write(u"\u0613\3\2\2\2\u0618\u061b\3\2\2\2\u0619\u0617\3\2\2")
        buf.write(u"\2\u0619\u061a\3\2\2\2\u061a\u00c9\3\2\2\2\u061b\u0619")
        buf.write(u"\3\2\2\2\u061c\u061f\5\u00c6d\2\u061d\u061f\5&\24\2\u061e")
        buf.write(u"\u061c\3\2\2\2\u061e\u061d\3\2\2\2\u061f\u00cb\3\2\2")
        buf.write(u"\2\u0620\u0621\7\13\2\2\u0621\u062b\5\u0170\u00b9\2\u0622")
        buf.write(u"\u0623\7\f\2\2\u0623\u062b\5\u018a\u00c6\2\u0624\u0625")
        buf.write(u"\7\r\2\2\u0625\u062b\5\u00ceh\2\u0626\u0627\7\16\2\2")
        buf.write(u"\u0627\u062b\5\u00ceh\2\u0628\u0629\7\17\2\2\u0629\u062b")
        buf.write(u"\5\u00d4k\2\u062a\u0620\3\2\2\2\u062a\u0622\3\2\2\2\u062a")
        buf.write(u"\u0624\3\2\2\2\u062a\u0626\3\2\2\2\u062a\u0628\3\2\2")
        buf.write(u"\2\u062b\u00cd\3\2\2\2\u062c\u062e\5\u00aeX\2\u062d\u062f")
        buf.write(u"\5\u00d0i\2\u062e\u062d\3\2\2\2\u062e\u062f\3\2\2\2\u062f")
        buf.write(u"\u00cf\3\2\2\2\u0630\u0631\7f\2\2\u0631\u0632\5\u00d2")
        buf.write(u"j\2\u0632\u0633\7\21\2\2\u0633\u0638\5\u00aeX\2\u0634")
        buf.write(u"\u0635\7\25\2\2\u0635\u0637\5\u00aeX\2\u0636\u0634\3")
        buf.write(u"\2\2\2\u0637\u063a\3\2\2\2\u0638\u0636\3\2\2\2\u0638")
        buf.write(u"\u0639\3\2\2\2\u0639\u00d1\3\2\2\2\u063a\u0638\3\2\2")
        buf.write(u"\2\u063b\u063c\7\u009d\2\2\u063c\u063d\6j8\3\u063d\u00d3")
        buf.write(u"\3\2\2\2\u063e\u0640\5\u00aeX\2\u063f\u0641\5\u00d6l")
        buf.write(u"\2\u0640\u063f\3\2\2\2\u0640\u0641\3\2\2\2\u0641\u00d5")
        buf.write(u"\3\2\2\2\u0642\u0643\7f\2\2\u0643\u0644\5\u00d2j\2\u0644")
        buf.write(u"\u0646\7\21\2\2\u0645\u0647\7%\2\2\u0646\u0645\3\2\2")
        buf.write(u"\2\u0646\u0647\3\2\2\2\u0647\u0648\3\2\2\2\u0648\u064d")
        buf.write(u"\5\u0140\u00a1\2\u0649\u064a\7%\2\2\u064a\u064c\5\u0140")
        buf.write(u"\u00a1\2\u064b\u0649\3\2\2\2\u064c\u064f\3\2\2\2\u064d")
        buf.write(u"\u064b\3\2\2\2\u064d\u064e\3\2\2\2\u064e\u0652\3\2\2")
        buf.write(u"\2\u064f\u064d\3\2\2\2\u0650\u0651\7\25\2\2\u0651\u0653")
        buf.write(u"\5\u0140\u00a1\2\u0652\u0650\3\2\2\2\u0652\u0653\3\2")
        buf.write(u"\2\2\u0653\u00d7\3\2\2\2\u0654\u0655\bm\1\2\u0655\u0656")
        buf.write(u"\5\u00b0Y\2\u0656\u065c\3\2\2\2\u0657\u0658\f\3\2\2\u0658")
        buf.write(u"\u0659\7\23\2\2\u0659\u065b\5\u00b0Y\2\u065a\u0657\3")
        buf.write(u"\2\2\2\u065b\u065e\3\2\2\2\u065c\u065a\3\2\2\2\u065c")
        buf.write(u"\u065d\3\2\2\2\u065d\u00d9\3\2\2\2\u065e\u065c\3\2\2")
        buf.write(u"\2\u065f\u0664\5\"\22\2\u0660\u0664\5$\23\2\u0661\u0664")
        buf.write(u"\5&\24\2\u0662\u0664\5(\25\2\u0663\u065f\3\2\2\2\u0663")
        buf.write(u"\u0660\3\2\2\2\u0663\u0661\3\2\2\2\u0663\u0662\3\2\2")
        buf.write(u"\2\u0664\u00db\3\2\2\2\u0665\u0666\7\n\2\2\u0666\u00dd")
        buf.write(u"\3\2\2\2\u0667\u0668\bp\1\2\u0668\u0669\5\u00e0q\2\u0669")
        buf.write(u"\u0670\3\2\2\2\u066a\u066b\f\3\2\2\u066b\u066c\5z>\2")
        buf.write(u"\u066c\u066d\5\u00e0q\2\u066d\u066f\3\2\2\2\u066e\u066a")
        buf.write(u"\3\2\2\2\u066f\u0672\3\2\2\2\u0670\u066e\3\2\2\2\u0670")
        buf.write(u"\u0671\3\2\2\2\u0671\u00df\3\2\2\2\u0672\u0670\3\2\2")
        buf.write(u"\2\u0673\u0674\7\13\2\2\u0674\u067e\5\u015a\u00ae\2\u0675")
        buf.write(u"\u0676\7\f\2\2\u0676\u067e\5\u0176\u00bc\2\u0677\u0678")
        buf.write(u"\7\r\2\2\u0678\u067e\5\u00e2r\2\u0679\u067a\7\16\2\2")
        buf.write(u"\u067a\u067e\5\u00e2r\2\u067b\u067c\7\17\2\2\u067c\u067e")
        buf.write(u"\5\u00e4s\2\u067d\u0673\3\2\2\2\u067d\u0675\3\2\2\2\u067d")
        buf.write(u"\u0677\3\2\2\2\u067d\u0679\3\2\2\2\u067d\u067b\3\2\2")
        buf.write(u"\2\u067e\u00e1\3\2\2\2\u067f\u0681\5\u0142\u00a2\2\u0680")
        buf.write(u"\u0682\7\22\2\2\u0681\u0680\3\2\2\2\u0681\u0682\3\2\2")
        buf.write(u"\2\u0682\u0684\3\2\2\2\u0683\u0685\5\u00d0i\2\u0684\u0683")
        buf.write(u"\3\2\2\2\u0684\u0685\3\2\2\2\u0685\u00e3\3\2\2\2\u0686")
        buf.write(u"\u0688\5\u0128\u0095\2\u0687\u0689\7\22\2\2\u0688\u0687")
        buf.write(u"\3\2\2\2\u0688\u0689\3\2\2\2\u0689\u068b\3\2\2\2\u068a")
        buf.write(u"\u068c\5\u00d6l\2\u068b\u068a\3\2\2\2\u068b\u068c\3\2")
        buf.write(u"\2\2\u068c\u00e5\3\2\2\2\u068d\u068e\bt\1\2\u068e\u068f")
        buf.write(u"\5\60\31\2\u068f\u0696\3\2\2\2\u0690\u0691\f\3\2\2\u0691")
        buf.write(u"\u0692\5z>\2\u0692\u0693\5\60\31\2\u0693\u0695\3\2\2")
        buf.write(u"\2\u0694\u0690\3\2\2\2\u0695\u0698\3\2\2\2\u0696\u0694")
        buf.write(u"\3\2\2\2\u0696\u0697\3\2\2\2\u0697\u00e7\3\2\2\2\u0698")
        buf.write(u"\u0696\3\2\2\2\u0699\u069a\bu\1\2\u069a\u069b\5*\26\2")
        buf.write(u"\u069b\u06a2\3\2\2\2\u069c\u069d\f\3\2\2\u069d\u069e")
        buf.write(u"\5z>\2\u069e\u069f\5*\26\2\u069f\u06a1\3\2\2\2\u06a0")
        buf.write(u"\u069c\3\2\2\2\u06a1\u06a4\3\2\2\2\u06a2\u06a0\3\2\2")
        buf.write(u"\2\u06a2\u06a3\3\2\2\2\u06a3\u00e9\3\2\2\2\u06a4\u06a2")
        buf.write(u"\3\2\2\2\u06a5\u06a6\bv\1\2\u06a6\u06a7\5<\37\2\u06a7")
        buf.write(u"\u06ae\3\2\2\2\u06a8\u06a9\f\3\2\2\u06a9\u06aa\5z>\2")
        buf.write(u"\u06aa\u06ab\5<\37\2\u06ab\u06ad\3\2\2\2\u06ac\u06a8")
        buf.write(u"\3\2\2\2\u06ad\u06b0\3\2\2\2\u06ae\u06ac\3\2\2\2\u06ae")
        buf.write(u"\u06af\3\2\2\2\u06af\u00eb\3\2\2\2\u06b0\u06ae\3\2\2")
        buf.write(u"\2\u06b1\u06b2\bw\1\2\u06b2\u06b3\5L\'\2\u06b3\u06ba")
        buf.write(u"\3\2\2\2\u06b4\u06b5\f\3\2\2\u06b5\u06b6\5z>\2\u06b6")
        buf.write(u"\u06b7\5L\'\2\u06b7\u06b9\3\2\2\2\u06b8\u06b4\3\2\2\2")
        buf.write(u"\u06b9\u06bc\3\2\2\2\u06ba\u06b8\3\2\2\2\u06ba\u06bb")
        buf.write(u"\3\2\2\2\u06bb\u00ed\3\2\2\2\u06bc\u06ba\3\2\2\2\u06bd")
        buf.write(u"\u06be\7\30\2\2\u06be\u06bf\5\u00f0y\2\u06bf\u06c0\7")
        buf.write(u"\24\2\2\u06c0\u06c1\5\u00f0y\2\u06c1\u06c2\7\31\2\2\u06c2")
        buf.write(u"\u06cc\3\2\2\2\u06c3\u06c4\7\30\2\2\u06c4\u06c5\5\u00f2")
        buf.write(u"z\2\u06c5\u06c6\7\31\2\2\u06c6\u06cc\3\2\2\2\u06c7\u06c8")
        buf.write(u"\7*\2\2\u06c8\u06c9\5\u00f2z\2\u06c9\u06ca\7(\2\2\u06ca")
        buf.write(u"\u06cc\3\2\2\2\u06cb\u06bd\3\2\2\2\u06cb\u06c3\3\2\2")
        buf.write(u"\2\u06cb\u06c7\3\2\2\2\u06cc\u00ef\3\2\2\2\u06cd\u06db")
        buf.write(u"\7\u0099\2\2\u06ce\u06db\7\u009a\2\2\u06cf\u06db\7\u00a1")
        buf.write(u"\2\2\u06d0\u06db\7\u00a2\2\2\u06d1\u06db\7\u0098\2\2")
        buf.write(u"\u06d2\u06db\7\u00a6\2\2\u06d3\u06db\7\u00a5\2\2\u06d4")
        buf.write(u"\u06db\7\u00a0\2\2\u06d5\u06db\7\u00a3\2\2\u06d6\u06db")
        buf.write(u"\7\u00a4\2\2\u06d7\u06db\7\u0097\2\2\u06d8\u06db\7\u00a7")
        buf.write(u"\2\2\u06d9\u06db\5\u0080A\2\u06da\u06cd\3\2\2\2\u06da")
        buf.write(u"\u06ce\3\2\2\2\u06da\u06cf\3\2\2\2\u06da\u06d0\3\2\2")
        buf.write(u"\2\u06da\u06d1\3\2\2\2\u06da\u06d2\3\2\2\2\u06da\u06d3")
        buf.write(u"\3\2\2\2\u06da\u06d4\3\2\2\2\u06da\u06d5\3\2\2\2\u06da")
        buf.write(u"\u06d6\3\2\2\2\u06da\u06d7\3\2\2\2\u06da\u06d8\3\2\2")
        buf.write(u"\2\u06da\u06d9\3\2\2\2\u06db\u00f1\3\2\2\2\u06dc\u06dd")
        buf.write(u"\bz\1\2\u06dd\u06de\5\u00f0y\2\u06de\u06e4\3\2\2\2\u06df")
        buf.write(u"\u06e0\f\3\2\2\u06e0\u06e1\7\23\2\2\u06e1\u06e3\5\u00f0")
        buf.write(u"y\2\u06e2\u06df\3\2\2\2\u06e3\u06e6\3\2\2\2\u06e4\u06e2")
        buf.write(u"\3\2\2\2\u06e4\u06e5\3\2\2\2\u06e5\u00f3\3\2\2\2\u06e6")
        buf.write(u"\u06e4\3\2\2\2\u06e7\u06ec\5\u00f8}\2\u06e8\u06ec\5\u00fa")
        buf.write(u"~\2\u06e9\u06ec\5\u00aeX\2\u06ea\u06ec\5\u00f6|\2\u06eb")
        buf.write(u"\u06e7\3\2\2\2\u06eb\u06e8\3\2\2\2\u06eb\u06e9\3\2\2")
        buf.write(u"\2\u06eb\u06ea\3\2\2\2\u06ec\u00f5\3\2\2\2\u06ed\u06ee")
        buf.write(u"\t\3\2\2\u06ee\u00f7\3\2\2\2\u06ef\u06f0\7\26\2\2\u06f0")
        buf.write(u"\u06f1\5P)\2\u06f1\u06f2\7\27\2\2\u06f2\u00f9\3\2\2\2")
        buf.write(u"\u06f3\u06f6\5\u00f0y\2\u06f4\u06f6\5\u00fc\177\2\u06f5")
        buf.write(u"\u06f3\3\2\2\2\u06f5\u06f4\3\2\2\2\u06f6\u00fb\3\2\2")
        buf.write(u"\2\u06f7\u06fd\5\u009aN\2\u06f8\u06fd\5\u0094K\2\u06f9")
        buf.write(u"\u06fd\5\u0096L\2\u06fa\u06fd\5\u0100\u0081\2\u06fb\u06fd")
        buf.write(u"\5\u00fe\u0080\2\u06fc\u06f7\3\2\2\2\u06fc\u06f8\3\2")
        buf.write(u"\2\2\u06fc\u06f9\3\2\2\2\u06fc\u06fa\3\2\2\2\u06fc\u06fb")
        buf.write(u"\3\2\2\2\u06fd\u00fd\3\2\2\2\u06fe\u0700\7\26\2\2\u06ff")
        buf.write(u"\u0701\5\u0102\u0082\2\u0700\u06ff\3\2\2\2\u0700\u0701")
        buf.write(u"\3\2\2\2\u0701\u0702\3\2\2\2\u0702\u0703\7\27\2\2\u0703")
        buf.write(u"\u00ff\3\2\2\2\u0704\u0706\7\32\2\2\u0705\u0707\5\u0104")
        buf.write(u"\u0083\2\u0706\u0705\3\2\2\2\u0706\u0707\3\2\2\2\u0707")
        buf.write(u"\u0708\3\2\2\2\u0708\u0709\7\33\2\2\u0709\u0101\3\2\2")
        buf.write(u"\2\u070a\u070b\b\u0082\1\2\u070b\u070c\5P)\2\u070c\u0712")
        buf.write(u"\3\2\2\2\u070d\u070e\f\3\2\2\u070e\u070f\7\23\2\2\u070f")
        buf.write(u"\u0711\5P)\2\u0710\u070d\3\2\2\2\u0711\u0714\3\2\2\2")
        buf.write(u"\u0712\u0710\3\2\2\2\u0712\u0713\3\2\2\2\u0713\u0103")
        buf.write(u"\3\2\2\2\u0714\u0712\3\2\2\2\u0715\u0716\b\u0083\1\2")
        buf.write(u"\u0716\u0717\5\u0106\u0084\2\u0717\u071d\3\2\2\2\u0718")
        buf.write(u"\u0719\f\3\2\2\u0719\u071a\7\23\2\2\u071a\u071c\5\u0106")
        buf.write(u"\u0084\2\u071b\u0718\3\2\2\2\u071c\u071f\3\2\2\2\u071d")
        buf.write(u"\u071b\3\2\2\2\u071d\u071e\3\2\2\2\u071e\u0105\3\2\2")
        buf.write(u"\2\u071f\u071d\3\2\2\2\u0720\u0721\5P)\2\u0721\u0722")
        buf.write(u"\7\21\2\2\u0722\u0723\5P)\2\u0723\u0107\3\2\2\2\u0724")
        buf.write(u"\u0725\5P)\2\u0725\u0726\7\21\2\2\u0726\u0727\5P)\2\u0727")
        buf.write(u"\u072e\3\2\2\2\u0728\u0729\5P)\2\u0729\u072a\7\21\2\2")
        buf.write(u"\u072a\u072e\3\2\2\2\u072b\u072c\7\21\2\2\u072c\u072e")
        buf.write(u"\5P)\2\u072d\u0724\3\2\2\2\u072d\u0728\3\2\2\2\u072d")
        buf.write(u"\u072b\3\2\2\2\u072e\u0109\3\2\2\2\u072f\u0730\5\u00b0")
        buf.write(u"Y\2\u0730\u0731\5\u011e\u0090\2\u0731\u0732\5P)\2\u0732")
        buf.write(u"\u010b\3\2\2\2\u0733\u0734\b\u0087\1\2\u0734\u0735\5")
        buf.write(u"\u00b0Y\2\u0735\u073a\3\2\2\2\u0736\u0737\f\3\2\2\u0737")
        buf.write(u"\u0739\5t;\2\u0738\u0736\3\2\2\2\u0739\u073c\3\2\2\2")
        buf.write(u"\u073a\u0738\3\2\2\2\u073a\u073b\3\2\2\2\u073b\u010d")
        buf.write(u"\3\2\2\2\u073c\u073a\3\2\2\2\u073d\u073e\6\u0088C\3\u073e")
        buf.write(u"\u073f\7\u009d\2\2\u073f\u0742\5\u00c0a\2\u0740\u0742")
        buf.write(u"\5P)\2\u0741\u073d\3\2\2\2\u0741\u0740\3\2\2\2\u0742")
        buf.write(u"\u010f\3\2\2\2\u0743\u0748\5\u0112\u008a\2\u0744\u0745")
        buf.write(u"\7\23\2\2\u0745\u0747\5\u0112\u008a\2\u0746\u0744\3\2")
        buf.write(u"\2\2\u0747\u074a\3\2\2\2\u0748\u0746\3\2\2\2\u0748\u0749")
        buf.write(u"\3\2\2\2\u0749\u0111\3\2\2\2\u074a\u0748\3\2\2\2\u074b")
        buf.write(u"\u0750\5\u00b0Y\2\u074c\u074d\7\25\2\2\u074d\u074f\5")
        buf.write(u"\u00b0Y\2\u074e\u074c\3\2\2\2\u074f\u0752\3\2\2\2\u0750")
        buf.write(u"\u074e\3\2\2\2\u0750\u0751\3\2\2\2\u0751\u0754\3\2\2")
        buf.write(u"\2\u0752\u0750\3\2\2\2\u0753\u0755\t\4\2\2\u0754\u0753")
        buf.write(u"\3\2\2\2\u0754\u0755\3\2\2\2\u0755\u0113\3\2\2\2\u0756")
        buf.write(u"\u075d\7\"\2\2\u0757\u075d\7#\2\2\u0758\u075d\5\u0120")
        buf.write(u"\u0091\2\u0759\u075d\5\u0122\u0092\2\u075a\u075d\5\u0124")
        buf.write(u"\u0093\2\u075b\u075d\5\u0126\u0094\2\u075c\u0756\3\2")
        buf.write(u"\2\2\u075c\u0757\3\2\2\2\u075c\u0758\3\2\2\2\u075c\u0759")
        buf.write(u"\3\2\2\2\u075c\u075a\3\2\2\2\u075c\u075b\3\2\2\2\u075d")
        buf.write(u"\u0115\3\2\2\2\u075e\u075f\7\u009d\2\2\u075f\u0760\6")
        buf.write(u"\u008cD\3\u0760\u0117\3\2\2\2\u0761\u0762\7\u009d\2\2")
        buf.write(u"\u0762\u0763\6\u008dE\3\u0763\u0119\3\2\2\2\u0764\u0765")
        buf.write(u"\7\u009d\2\2\u0765\u0766\6\u008eF\3\u0766\u011b\3\2\2")
        buf.write(u"\2\u0767\u0768\7\u009d\2\2\u0768\u0769\6\u008fG\3\u0769")
        buf.write(u"\u011d\3\2\2\2\u076a\u076b\7-\2\2\u076b\u011f\3\2\2\2")
        buf.write(u"\u076c\u076d\7$\2\2\u076d\u0121\3\2\2\2\u076e\u076f\7")
        buf.write(u"%\2\2\u076f\u0123\3\2\2\2\u0770\u0771\7&\2\2\u0771\u0125")
        buf.write(u"\3\2\2\2\u0772\u0773\t\5\2\2\u0773\u0127\3\2\2\2\u0774")
        buf.write(u"\u0775\7\u0082\2\2\u0775\u0776\5\u012a\u0096\2\u0776")
        buf.write(u"\u0777\7\22\2\2\u0777\u077c\3\2\2\2\u0778\u0779\5\u012a")
        buf.write(u"\u0096\2\u0779\u077a\7\22\2\2\u077a\u077c\3\2\2\2\u077b")
        buf.write(u"\u0774\3\2\2\2\u077b\u0778\3\2\2\2\u077c\u0129\3\2\2")
        buf.write(u"\2\u077d\u077e\b\u0096\1\2\u077e\u077f\5\u012c\u0097")
        buf.write(u"\2\u077f\u0784\3\2\2\2\u0780\u0781\f\3\2\2\u0781\u0783")
        buf.write(u"\5\u0132\u009a\2\u0782\u0780\3\2\2\2\u0783\u0786\3\2")
        buf.write(u"\2\2\u0784\u0782\3\2\2\2\u0784\u0785\3\2\2\2\u0785\u012b")
        buf.write(u"\3\2\2\2\u0786\u0784\3\2\2\2\u0787\u078f\5\u012e\u0098")
        buf.write(u"\2\u0788\u078f\5\u0130\u0099\2\u0789\u078f\5\u013a\u009e")
        buf.write(u"\2\u078a\u078f\5\u013c\u009f\2\u078b\u078f\5\u013e\u00a0")
        buf.write(u"\2\u078c\u078f\5\u0134\u009b\2\u078d\u078f\5\u0138\u009d")
        buf.write(u"\2\u078e\u0787\3\2\2\2\u078e\u0788\3\2\2\2\u078e\u0789")
        buf.write(u"\3\2\2\2\u078e\u078a\3\2\2\2\u078e\u078b\3\2\2\2\u078e")
        buf.write(u"\u078c\3\2\2\2\u078e\u078d\3\2\2\2\u078f\u012d\3\2\2")
        buf.write(u"\2\u0790\u0791\5\u00f6|\2\u0791\u012f\3\2\2\2\u0792\u0793")
        buf.write(u"\5\u0116\u008c\2\u0793\u0794\5\u0134\u009b\2\u0794\u0131")
        buf.write(u"\3\2\2\2\u0795\u0796\7\25\2\2\u0796\u079b\5\u0134\u009b")
        buf.write(u"\2\u0797\u0798\7\25\2\2\u0798\u079b\5\u0140\u00a1\2\u0799")
        buf.write(u"\u079b\5\u0138\u009d\2\u079a\u0795\3\2\2\2\u079a\u0797")
        buf.write(u"\3\2\2\2\u079a\u0799\3\2\2\2\u079b\u0133\3\2\2\2\u079c")
        buf.write(u"\u079d\5\u0140\u00a1\2\u079d\u079f\7\26\2\2\u079e\u07a0")
        buf.write(u"\5\u0136\u009c\2\u079f\u079e\3\2\2\2\u079f\u07a0\3\2")
        buf.write(u"\2\2\u07a0\u07a1\3\2\2\2\u07a1\u07a2\7\27\2\2\u07a2\u0135")
        buf.write(u"\3\2\2\2\u07a3\u07a4\b\u009c\1\2\u07a4\u07a5\5\u012a")
        buf.write(u"\u0096\2\u07a5\u07ab\3\2\2\2\u07a6\u07a7\f\3\2\2\u07a7")
        buf.write(u"\u07a8\7\23\2\2\u07a8\u07aa\5\u012a\u0096\2\u07a9\u07a6")
        buf.write(u"\3\2\2\2\u07aa\u07ad\3\2\2\2\u07ab\u07a9\3\2\2\2\u07ab")
        buf.write(u"\u07ac\3\2\2\2\u07ac\u0137\3\2\2\2\u07ad\u07ab\3\2\2")
        buf.write(u"\2\u07ae\u07af\7\30\2\2\u07af\u07b0\5\u012a\u0096\2\u07b0")
        buf.write(u"\u07b1\7\31\2\2\u07b1\u0139\3\2\2\2\u07b2\u07b3\7\26")
        buf.write(u"\2\2\u07b3\u07b4\5\u012a\u0096\2\u07b4\u07b5\7\27\2\2")
        buf.write(u"\u07b5\u013b\3\2\2\2\u07b6\u07b7\5\u0140\u00a1\2\u07b7")
        buf.write(u"\u013d\3\2\2\2\u07b8\u07be\7\u00a1\2\2\u07b9\u07be\7")
        buf.write(u"\u00a3\2\2\u07ba\u07be\7\u00a0\2\2\u07bb\u07be\7\u0097")
        buf.write(u"\2\2\u07bc\u07be\7\u0098\2\2\u07bd\u07b8\3\2\2\2\u07bd")
        buf.write(u"\u07b9\3\2\2\2\u07bd\u07ba\3\2\2\2\u07bd\u07bb\3\2\2")
        buf.write(u"\2\u07bd\u07bc\3\2\2\2\u07be\u013f\3\2\2\2\u07bf\u07c0")
        buf.write(u"\t\6\2\2\u07c0\u0141\3\2\2\2\u07c1\u07c2\7\u0082\2\2")
        buf.write(u"\u07c2\u07c5\5\u0144\u00a3\2\u07c3\u07c5\5\u0144\u00a3")
        buf.write(u"\2\u07c4\u07c1\3\2\2\2\u07c4\u07c3\3\2\2\2\u07c5\u0143")
        buf.write(u"\3\2\2\2\u07c6\u07c7\b\u00a3\1\2\u07c7\u07c8\5\u0146")
        buf.write(u"\u00a4\2\u07c8\u07cd\3\2\2\2\u07c9\u07ca\f\3\2\2\u07ca")
        buf.write(u"\u07cc\5\u0148\u00a5\2\u07cb\u07c9\3\2\2\2\u07cc\u07cf")
        buf.write(u"\3\2\2\2\u07cd\u07cb\3\2\2\2\u07cd\u07ce\3\2\2\2\u07ce")
        buf.write(u"\u0145\3\2\2\2\u07cf\u07cd\3\2\2\2\u07d0\u07d5\5\u0152")
        buf.write(u"\u00aa\2\u07d1\u07d5\5\u0154\u00ab\2\u07d2\u07d5\5\u0156")
        buf.write(u"\u00ac\2\u07d3\u07d5\5\u014a\u00a6\2\u07d4\u07d0\3\2")
        buf.write(u"\2\2\u07d4\u07d1\3\2\2\2\u07d4\u07d2\3\2\2\2\u07d4\u07d3")
        buf.write(u"\3\2\2\2\u07d5\u0147\3\2\2\2\u07d6\u07d7\7\25\2\2\u07d7")
        buf.write(u"\u07dd\5\u014a\u00a6\2\u07d8\u07d9\7\30\2\2\u07d9\u07da")
        buf.write(u"\5\u0144\u00a3\2\u07da\u07db\7\31\2\2\u07db\u07dd\3\2")
        buf.write(u"\2\2\u07dc\u07d6\3\2\2\2\u07dc\u07d8\3\2\2\2\u07dd\u0149")
        buf.write(u"\3\2\2\2\u07de\u07df\5\u0158\u00ad\2\u07df\u07e1\7\26")
        buf.write(u"\2\2\u07e0\u07e2\5\u014c\u00a7\2\u07e1\u07e0\3\2\2\2")
        buf.write(u"\u07e1\u07e2\3\2\2\2\u07e2\u07e3\3\2\2\2\u07e3\u07e4")
        buf.write(u"\7\27\2\2\u07e4\u014b\3\2\2\2\u07e5\u07ec\5\u014e\u00a8")
        buf.write(u"\2\u07e6\u07ec\5\u0150\u00a9\2\u07e7\u07e8\5\u014e\u00a8")
        buf.write(u"\2\u07e8\u07e9\7\23\2\2\u07e9\u07ea\5\u0150\u00a9\2\u07ea")
        buf.write(u"\u07ec\3\2\2\2\u07eb\u07e5\3\2\2\2\u07eb\u07e6\3\2\2")
        buf.write(u"\2\u07eb\u07e7\3\2\2\2\u07ec\u014d\3\2\2\2\u07ed\u07ee")
        buf.write(u"\b\u00a8\1\2\u07ee\u07ef\5\u0144\u00a3\2\u07ef\u07f5")
        buf.write(u"\3\2\2\2\u07f0\u07f1\f\3\2\2\u07f1\u07f2\7\23\2\2\u07f2")
        buf.write(u"\u07f4\5\u0144\u00a3\2\u07f3\u07f0\3\2\2\2\u07f4\u07f7")
        buf.write(u"\3\2\2\2\u07f5\u07f3\3\2\2\2\u07f5\u07f6\3\2\2\2\u07f6")
        buf.write(u"\u014f\3\2\2\2\u07f7\u07f5\3\2\2\2\u07f8\u07f9\b\u00a9")
        buf.write(u"\1\2\u07f9\u07fa\5\u0158\u00ad\2\u07fa\u07fb\7-\2\2\u07fb")
        buf.write(u"\u07fc\5\u0144\u00a3\2\u07fc\u0805\3\2\2\2\u07fd\u07fe")
        buf.write(u"\f\3\2\2\u07fe\u07ff\7\23\2\2\u07ff\u0800\5\u0158\u00ad")
        buf.write(u"\2\u0800\u0801\7-\2\2\u0801\u0802\5\u0144\u00a3\2\u0802")
        buf.write(u"\u0804\3\2\2\2\u0803\u07fd\3\2\2\2\u0804\u0807\3\2\2")
        buf.write(u"\2\u0805\u0803\3\2\2\2\u0805\u0806\3\2\2\2\u0806\u0151")
        buf.write(u"\3\2\2\2\u0807\u0805\3\2\2\2\u0808\u0809\7\26\2\2\u0809")
        buf.write(u"\u080a\5\u0144\u00a3\2\u080a\u080b\7\27\2\2\u080b\u0153")
        buf.write(u"\3\2\2\2\u080c\u080d\b\u00ab\1\2\u080d\u0810\7\u009f")
        buf.write(u"\2\2\u080e\u0810\5\u0158\u00ad\2\u080f\u080c\3\2\2\2")
        buf.write(u"\u080f\u080e\3\2\2\2\u0810\u0816\3\2\2\2\u0811\u0812")
        buf.write(u"\f\3\2\2\u0812\u0813\7\25\2\2\u0813\u0815\5\u0158\u00ad")
        buf.write(u"\2\u0814\u0811\3\2\2\2\u0815\u0818\3\2\2\2\u0816\u0814")
        buf.write(u"\3\2\2\2\u0816\u0817\3\2\2\2\u0817\u0155\3\2\2\2\u0818")
        buf.write(u"\u0816\3\2\2\2\u0819\u081f\7\u00a1\2\2\u081a\u081f\7")
        buf.write(u"\u00a3\2\2\u081b\u081f\7\u00a0\2\2\u081c\u081f\7\u0097")
        buf.write(u"\2\2\u081d\u081f\7\u0098\2\2\u081e\u0819\3\2\2\2\u081e")
        buf.write(u"\u081a\3\2\2\2\u081e\u081b\3\2\2\2\u081e\u081c\3\2\2")
        buf.write(u"\2\u081e\u081d\3\2\2\2\u081f\u0157\3\2\2\2\u0820\u0821")
        buf.write(u"\t\7\2\2\u0821\u0159\3\2\2\2\u0822\u0823\7\u0082\2\2")
        buf.write(u"\u0823\u0824\5\u015c\u00af\2\u0824\u0825\7\22\2\2\u0825")
        buf.write(u"\u082a\3\2\2\2\u0826\u0827\5\u015c\u00af\2\u0827\u0828")
        buf.write(u"\7\22\2\2\u0828\u082a\3\2\2\2\u0829\u0822\3\2\2\2\u0829")
        buf.write(u"\u0826\3\2\2\2\u082a\u015b\3\2\2\2\u082b\u082c\b\u00af")
        buf.write(u"\1\2\u082c\u082d\5\u015e\u00b0\2\u082d\u0832\3\2\2\2")
        buf.write(u"\u082e\u082f\f\3\2\2\u082f\u0831\5\u0164\u00b3\2\u0830")
        buf.write(u"\u082e\3\2\2\2\u0831\u0834\3\2\2\2\u0832\u0830\3\2\2")
        buf.write(u"\2\u0832\u0833\3\2\2\2\u0833\u015d\3\2\2\2\u0834\u0832")
        buf.write(u"\3\2\2\2\u0835\u083b\5\u0160\u00b1\2\u0836\u083b\5\u0162")
        buf.write(u"\u00b2\2\u0837\u083b\5\u016c\u00b7\2\u0838\u083b\5\u016e")
        buf.write(u"\u00b8\2\u0839\u083b\5\u0172\u00ba\2\u083a\u0835\3\2")
        buf.write(u"\2\2\u083a\u0836\3\2\2\2\u083a\u0837\3\2\2\2\u083a\u0838")
        buf.write(u"\3\2\2\2\u083a\u0839\3\2\2\2\u083b\u015f\3\2\2\2\u083c")
        buf.write(u"\u083d\5\u00f6|\2\u083d\u0161\3\2\2\2\u083e\u083f\5\u0116")
        buf.write(u"\u008c\2\u083f\u0840\5\u0166\u00b4\2\u0840\u0163\3\2")
        buf.write(u"\2\2\u0841\u0842\7\25\2\2\u0842\u0845\5\u0166\u00b4\2")
        buf.write(u"\u0843\u0845\5\u016a\u00b6\2\u0844\u0841\3\2\2\2\u0844")
        buf.write(u"\u0843\3\2\2\2\u0845\u0165\3\2\2\2\u0846\u0847\5\u0174")
        buf.write(u"\u00bb\2\u0847\u0849\7\26\2\2\u0848\u084a\5\u0168\u00b5")
        buf.write(u"\2\u0849\u0848\3\2\2\2\u0849\u084a\3\2\2\2\u084a\u084b")
        buf.write(u"\3\2\2\2\u084b\u084c\7\27\2\2\u084c\u0167\3\2\2\2\u084d")
        buf.write(u"\u084e\b\u00b5\1\2\u084e\u084f\5\u015c\u00af\2\u084f")
        buf.write(u"\u0855\3\2\2\2\u0850\u0851\f\3\2\2\u0851\u0852\7\23\2")
        buf.write(u"\2\u0852\u0854\5\u015c\u00af\2\u0853\u0850\3\2\2\2\u0854")
        buf.write(u"\u0857\3\2\2\2\u0855\u0853\3\2\2\2\u0855\u0856\3\2\2")
        buf.write(u"\2\u0856\u0169\3\2\2\2\u0857\u0855\3\2\2\2\u0858\u0859")
        buf.write(u"\7\30\2\2\u0859\u085a\5\u015c\u00af\2\u085a\u085b\7\31")
        buf.write(u"\2\2\u085b\u016b\3\2\2\2\u085c\u085d\7\26\2\2\u085d\u085e")
        buf.write(u"\5\u015c\u00af\2\u085e\u085f\7\27\2\2\u085f\u016d\3\2")
        buf.write(u"\2\2\u0860\u0861\b\u00b8\1\2\u0861\u0862\5\u0174\u00bb")
        buf.write(u"\2\u0862\u0868\3\2\2\2\u0863\u0864\f\3\2\2\u0864\u0865")
        buf.write(u"\7\25\2\2\u0865\u0867\5\u0174\u00bb\2\u0866\u0863\3\2")
        buf.write(u"\2\2\u0867\u086a\3\2\2\2\u0868\u0866\3\2\2\2\u0868\u0869")
        buf.write(u"\3\2\2\2\u0869\u016f\3\2\2\2\u086a\u0868\3\2\2\2\u086b")
        buf.write(u"\u086c\b\u00b9\1\2\u086c\u086d\5\u016e\u00b8\2\u086d")
        buf.write(u"\u0872\3\2\2\2\u086e\u086f\f\3\2\2\u086f\u0871\7\u009f")
        buf.write(u"\2\2\u0870\u086e\3\2\2\2\u0871\u0874\3\2\2\2\u0872\u0870")
        buf.write(u"\3\2\2\2\u0872\u0873\3\2\2\2\u0873\u0171\3\2\2\2\u0874")
        buf.write(u"\u0872\3\2\2\2\u0875\u087b\7\u00a1\2\2\u0876\u087b\7")
        buf.write(u"\u00a3\2\2\u0877\u087b\7\u00a0\2\2\u0878\u087b\7\u0097")
        buf.write(u"\2\2\u0879\u087b\7\u0098\2\2\u087a\u0875\3\2\2\2\u087a")
        buf.write(u"\u0876\3\2\2\2\u087a\u0877\3\2\2\2\u087a\u0878\3\2\2")
        buf.write(u"\2\u087a\u0879\3\2\2\2\u087b\u0173\3\2\2\2\u087c\u087d")
        buf.write(u"\t\b\2\2\u087d\u0175\3\2\2\2\u087e\u087f\7\u0082\2\2")
        buf.write(u"\u087f\u0880\5\u0178\u00bd\2\u0880\u0881\7\22\2\2\u0881")
        buf.write(u"\u0886\3\2\2\2\u0882\u0883\5\u0178\u00bd\2\u0883\u0884")
        buf.write(u"\7\22\2\2\u0884\u0886\3\2\2\2\u0885\u087e\3\2\2\2\u0885")
        buf.write(u"\u0882\3\2\2\2\u0886\u0177\3\2\2\2\u0887\u0888\b\u00bd")
        buf.write(u"\1\2\u0888\u0889\5\u017a\u00be\2\u0889\u088e\3\2\2\2")
        buf.write(u"\u088a\u088b\f\3\2\2\u088b\u088d\5\u0180\u00c1\2\u088c")
        buf.write(u"\u088a\3\2\2\2\u088d\u0890\3\2\2\2\u088e\u088c\3\2\2")
        buf.write(u"\2\u088e\u088f\3\2\2\2\u088f\u0179\3\2\2\2\u0890\u088e")
        buf.write(u"\3\2\2\2\u0891\u0897\5\u017c\u00bf\2\u0892\u0897\5\u017e")
        buf.write(u"\u00c0\2\u0893\u0897\5\u0188\u00c5\2\u0894\u0897\5\u018a")
        buf.write(u"\u00c6\2\u0895\u0897\5\u018c\u00c7\2\u0896\u0891\3\2")
        buf.write(u"\2\2\u0896\u0892\3\2\2\2\u0896\u0893\3\2\2\2\u0896\u0894")
        buf.write(u"\3\2\2\2\u0896\u0895\3\2\2\2\u0897\u017b\3\2\2\2\u0898")
        buf.write(u"\u0899\5\u00f6|\2\u0899\u017d\3\2\2\2\u089a\u089b\5\u0116")
        buf.write(u"\u008c\2\u089b\u089c\5\u0182\u00c2\2\u089c\u017f\3\2")
        buf.write(u"\2\2\u089d\u089e\7\25\2\2\u089e\u08a1\5\u0182\u00c2\2")
        buf.write(u"\u089f\u08a1\5\u0186\u00c4\2\u08a0\u089d\3\2\2\2\u08a0")
        buf.write(u"\u089f\3\2\2\2\u08a1\u0181\3\2\2\2\u08a2\u08a3\5\u018e")
        buf.write(u"\u00c8\2\u08a3\u08a5\7\26\2\2\u08a4\u08a6\5\u0184\u00c3")
        buf.write(u"\2\u08a5\u08a4\3\2\2\2\u08a5\u08a6\3\2\2\2\u08a6\u08a7")
        buf.write(u"\3\2\2\2\u08a7\u08a8\7\27\2\2\u08a8\u0183\3\2\2\2\u08a9")
        buf.write(u"\u08aa\b\u00c3\1\2\u08aa\u08ab\5\u0178\u00bd\2\u08ab")
        buf.write(u"\u08b1\3\2\2\2\u08ac\u08ad\f\3\2\2\u08ad\u08ae\7\23\2")
        buf.write(u"\2\u08ae\u08b0\5\u0178\u00bd\2\u08af\u08ac\3\2\2\2\u08b0")
        buf.write(u"\u08b3\3\2\2\2\u08b1\u08af\3\2\2\2\u08b1\u08b2\3\2\2")
        buf.write(u"\2\u08b2\u0185\3\2\2\2\u08b3\u08b1\3\2\2\2\u08b4\u08b5")
        buf.write(u"\7\30\2\2\u08b5\u08b6\5\u0178\u00bd\2\u08b6\u08b7\7\31")
        buf.write(u"\2\2\u08b7\u0187\3\2\2\2\u08b8\u08b9\7\26\2\2\u08b9\u08ba")
        buf.write(u"\5\u0178\u00bd\2\u08ba\u08bb\7\27\2\2\u08bb\u0189\3\2")
        buf.write(u"\2\2\u08bc\u08bd\b\u00c6\1\2\u08bd\u08c0\7\u009f\2\2")
        buf.write(u"\u08be\u08c0\5\u018e\u00c8\2\u08bf\u08bc\3\2\2\2\u08bf")
        buf.write(u"\u08be\3\2\2\2\u08c0\u08c6\3\2\2\2\u08c1\u08c2\f\3\2")
        buf.write(u"\2\u08c2\u08c3\7\25\2\2\u08c3\u08c5\5\u018e\u00c8\2\u08c4")
        buf.write(u"\u08c1\3\2\2\2\u08c5\u08c8\3\2\2\2\u08c6\u08c4\3\2\2")
        buf.write(u"\2\u08c6\u08c7\3\2\2\2\u08c7\u018b\3\2\2\2\u08c8\u08c6")
        buf.write(u"\3\2\2\2\u08c9\u08cf\7\u00a1\2\2\u08ca\u08cf\7\u00a3")
        buf.write(u"\2\2\u08cb\u08cf\7\u00a0\2\2\u08cc\u08cf\7\u0097\2\2")
        buf.write(u"\u08cd\u08cf\7\u0098\2\2\u08ce\u08c9\3\2\2\2\u08ce\u08ca")
        buf.write(u"\3\2\2\2\u08ce\u08cb\3\2\2\2\u08ce\u08cc\3\2\2\2\u08ce")
        buf.write(u"\u08cd\3\2\2\2\u08cf\u018d\3\2\2\2\u08d0\u08d1\t\t\2")
        buf.write(u"\2\u08d1\u018f\3\2\2\2\u00b7\u0196\u019d\u01bb\u01c1")
        buf.write(u"\u01c6\u01cc\u01d0\u01db\u01e4\u01f3\u01fc\u0203\u020d")
        buf.write(u"\u022b\u0236\u0244\u0252\u0260\u0274\u027f\u0281\u028a")
        buf.write(u"\u028e\u0296\u029a\u02a9\u02ad\u02c8\u02cf\u02d4\u02d8")
        buf.write(u"\u02eb\u02f2\u02f5\u0316\u0329\u0330\u0352\u035b\u0372")
        buf.write(u"\u0382\u0387\u038f\u0398\u03af\u03b3\u03cf\u0436\u0438")
        buf.write(u"\u0442\u0457\u0467\u046f\u0474\u0476\u047c\u047e\u0480")
        buf.write(u"\u049a\u04a1\u04a4\u04aa\u04ae\u04b3\u04b5\u04be\u04c5")
        buf.write(u"\u04c7\u04cc\u04ce\u04d9\u04ec\u04f5\u04fb\u0500\u0507")
        buf.write(u"\u050f\u051d\u0525\u052d\u0533\u053e\u054a\u0555\u0562")
        buf.write(u"\u0566\u056c\u0578\u058c\u058e\u0593\u05a3\u05a8\u05b1")
        buf.write(u"\u05bb\u05c0\u05c5\u05d5\u05da\u05dd\u05e1\u05e6\u05ed")
        buf.write(u"\u05f8\u05fa\u0606\u060e\u0619\u061e\u062a\u062e\u0638")
        buf.write(u"\u0640\u0646\u064d\u0652\u065c\u0663\u0670\u067d\u0681")
        buf.write(u"\u0684\u0688\u068b\u0696\u06a2\u06ae\u06ba\u06cb\u06da")
        buf.write(u"\u06e4\u06eb\u06f5\u06fc\u0700\u0706\u0712\u071d\u072d")
        buf.write(u"\u073a\u0741\u0748\u0750\u0754\u075c\u077b\u0784\u078e")
        buf.write(u"\u079a\u079f\u07ab\u07bd\u07c4\u07cd\u07d4\u07dc\u07e1")
        buf.write(u"\u07eb\u07f5\u0805\u080f\u0816\u081e\u0829\u0832\u083a")
        buf.write(u"\u0844\u0849\u0855\u0868\u0872\u087a\u0885\u088e\u0896")
        buf.write(u"\u08a0\u08a5\u08b1\u08bf\u08c6\u08ce")
        return buf.getvalue()
		

class EParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"<INVALID>", 
                     u"'Java:'", u"'C#:'", u"'Python2:'", u"'Python3:'", 
                     u"'JavaScript:'", u"'Swift:'", u"':'", u"';'", u"','", 
                     u"'..'", u"'.'", u"'('", u"')'", u"'['", u"']'", u"'{'", 
                     u"'}'", u"'?'", u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", 
                     u"'+'", u"'-'", u"'*'", u"'/'", u"'\\'", u"'%'", u"'>'", 
                     u"'>='", u"'<'", u"'<='", u"'<>'", u"'='", u"'!='", 
                     u"'=='", u"'~='", u"'~'", u"'<-'", u"'->'", u"'Boolean'", 
                     u"'Character'", u"'Text'", u"'Integer'", u"'Decimal'", 
                     u"'Date'", u"'Time'", u"'DateTime'", u"'Period'", u"'Method'", 
                     u"'Code'", u"'Document'", u"'Blob'", u"'Image'", u"'UUID'", 
                     u"'abstract'", u"'all'", u"'always'", u"'and'", u"'any'", 
                     u"'as'", u"<INVALID>", u"'attr'", u"'attribute'", u"'attributes'", 
                     u"'bindings'", u"'by'", u"'case'", u"'catch'", u"'category'", 
                     u"'class'", u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"<INVALID>", u"'do'", u"'doing'", u"'each'", 
                     u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
                     u"'methods'", u"'modulo'", u"'mutable'", u"'native'", 
                     u"'None'", u"'not'", u"<INVALID>", u"'null'", u"'on'", 
                     u"'one'", u"'open'", u"'operator'", u"'or'", u"'order'", 
                     u"'otherwise'", u"'pass'", u"'raise'", u"'read'", u"'receiving'", 
                     u"'resource'", u"'return'", u"'returning'", u"'rows'", 
                     u"'self'", u"'setter'", u"'singleton'", u"'sorted'", 
                     u"'storable'", u"'store'", u"'switch'", u"'test'", 
                     u"'this'", u"'throw'", u"'to'", u"'try'", u"'verifying'", 
                     u"'with'", u"'when'", u"'where'", u"'while'", u"'write'", 
                     u"<INVALID>", u"<INVALID>", u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"INDENT", u"DEDENT", u"LF_TAB", u"LF_MORE", 
                      u"LF", u"TAB", u"WS", u"COMMENT", u"JAVA", u"CSHARP", 
                      u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", 
                      u"SEMI", u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", 
                      u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", u"QMARK", 
                      u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", 
                      u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", 
                      u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", u"ABSTRACT", 
                      u"ALL", u"ALWAYS", u"AND", u"ANY", u"AS", u"ASC", 
                      u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", u"BINDINGS", 
                      u"BY", u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DESC", 
                      u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FINALLY", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INVOKE", u"IS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", u"OPERATOR", 
                      u"OR", u"ORDER", u"OTHERWISE", u"PASS", u"RAISE", 
                      u"READ", u"RECEIVING", u"RESOURCE", u"RETURN", u"RETURNING", 
                      u"ROWS", u"SELF", u"SETTER", u"SINGLETON", u"SORTED", 
                      u"STORABLE", u"STORE", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"VERIFYING", u"WITH", u"WHEN", 
                      u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"INTEGER_LITERAL", 
                      u"HEXA_LITERAL", u"DECIMAL_LITERAL", u"DATETIME_LITERAL", 
                      u"TIME_LITERAL", u"DATE_LITERAL", u"PERIOD_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_concrete_category_declaration = 5
    RULE_singleton_category_declaration = 6
    RULE_derived_list = 7
    RULE_operator_method_declaration = 8
    RULE_setter_method_declaration = 9
    RULE_getter_method_declaration = 10
    RULE_native_category_declaration = 11
    RULE_native_resource_declaration = 12
    RULE_native_category_bindings = 13
    RULE_native_category_binding_list = 14
    RULE_attribute_list = 15
    RULE_abstract_method_declaration = 16
    RULE_concrete_method_declaration = 17
    RULE_native_method_declaration = 18
    RULE_test_method_declaration = 19
    RULE_assertion = 20
    RULE_full_argument_list = 21
    RULE_typed_argument = 22
    RULE_statement = 23
    RULE_store_statement = 24
    RULE_method_call_statement = 25
    RULE_with_resource_statement = 26
    RULE_with_singleton_statement = 27
    RULE_switch_statement = 28
    RULE_switch_case_statement = 29
    RULE_for_each_statement = 30
    RULE_do_while_statement = 31
    RULE_while_statement = 32
    RULE_if_statement = 33
    RULE_else_if_statement_list = 34
    RULE_raise_statement = 35
    RULE_try_statement = 36
    RULE_catch_statement = 37
    RULE_return_statement = 38
    RULE_expression = 39
    RULE_unresolved_expression = 40
    RULE_unresolved_selector = 41
    RULE_invocation_expression = 42
    RULE_invocation_trailer = 43
    RULE_instance_expression = 44
    RULE_instance_selector = 45
    RULE_document_expression = 46
    RULE_constructor_expression = 47
    RULE_read_expression = 48
    RULE_write_statement = 49
    RULE_ambiguous_expression = 50
    RULE_fetch_expression = 51
    RULE_sorted_expression = 52
    RULE_argument_assignment_list = 53
    RULE_with_argument_assignment_list = 54
    RULE_argument_assignment = 55
    RULE_assign_instance_statement = 56
    RULE_child_instance = 57
    RULE_assign_tuple_statement = 58
    RULE_lfs = 59
    RULE_lfp = 60
    RULE_indent = 61
    RULE_dedent = 62
    RULE_null_literal = 63
    RULE_declaration_list = 64
    RULE_declarations = 65
    RULE_declaration = 66
    RULE_resource_declaration = 67
    RULE_enum_declaration = 68
    RULE_native_symbol_list = 69
    RULE_category_symbol_list = 70
    RULE_symbol_list = 71
    RULE_attribute_constraint = 72
    RULE_list_literal = 73
    RULE_set_literal = 74
    RULE_expression_list = 75
    RULE_range_literal = 76
    RULE_typedef = 77
    RULE_primary_type = 78
    RULE_native_type = 79
    RULE_category_type = 80
    RULE_mutable_category_type = 81
    RULE_code_type = 82
    RULE_category_declaration = 83
    RULE_type_identifier_list = 84
    RULE_method_identifier = 85
    RULE_identifier = 86
    RULE_variable_identifier = 87
    RULE_type_identifier = 88
    RULE_symbol_identifier = 89
    RULE_argument_list = 90
    RULE_argument = 91
    RULE_operator_argument = 92
    RULE_named_argument = 93
    RULE_code_argument = 94
    RULE_category_or_any_type = 95
    RULE_any_type = 96
    RULE_member_method_declaration_list = 97
    RULE_member_method_declaration = 98
    RULE_native_member_method_declaration_list = 99
    RULE_native_member_method_declaration = 100
    RULE_native_category_binding = 101
    RULE_python_category_binding = 102
    RULE_python_module = 103
    RULE_module_token = 104
    RULE_javascript_category_binding = 105
    RULE_javascript_module = 106
    RULE_variable_identifier_list = 107
    RULE_method_declaration = 108
    RULE_comment_statement = 109
    RULE_native_statement_list = 110
    RULE_native_statement = 111
    RULE_python_native_statement = 112
    RULE_javascript_native_statement = 113
    RULE_statement_list = 114
    RULE_assertion_list = 115
    RULE_switch_case_statement_list = 116
    RULE_catch_statement_list = 117
    RULE_literal_collection = 118
    RULE_atomic_literal = 119
    RULE_literal_list_literal = 120
    RULE_selectable_expression = 121
    RULE_this_expression = 122
    RULE_parenthesis_expression = 123
    RULE_literal_expression = 124
    RULE_collection_literal = 125
    RULE_tuple_literal = 126
    RULE_dict_literal = 127
    RULE_expression_tuple = 128
    RULE_dict_entry_list = 129
    RULE_dict_entry = 130
    RULE_slice_arguments = 131
    RULE_assign_variable_statement = 132
    RULE_assignable_instance = 133
    RULE_is_expression = 134
    RULE_order_by_list = 135
    RULE_order_by = 136
    RULE_operator = 137
    RULE_new_token = 138
    RULE_key_token = 139
    RULE_value_token = 140
    RULE_symbols_token = 141
    RULE_assign = 142
    RULE_multiply = 143
    RULE_divide = 144
    RULE_idivide = 145
    RULE_modulo = 146
    RULE_javascript_statement = 147
    RULE_javascript_expression = 148
    RULE_javascript_primary_expression = 149
    RULE_javascript_this_expression = 150
    RULE_javascript_new_expression = 151
    RULE_javascript_selector_expression = 152
    RULE_javascript_method_expression = 153
    RULE_javascript_arguments = 154
    RULE_javascript_item_expression = 155
    RULE_javascript_parenthesis_expression = 156
    RULE_javascript_identifier_expression = 157
    RULE_javascript_literal_expression = 158
    RULE_javascript_identifier = 159
    RULE_python_statement = 160
    RULE_python_expression = 161
    RULE_python_primary_expression = 162
    RULE_python_selector_expression = 163
    RULE_python_method_expression = 164
    RULE_python_argument_list = 165
    RULE_python_ordinal_argument_list = 166
    RULE_python_named_argument_list = 167
    RULE_python_parenthesis_expression = 168
    RULE_python_identifier_expression = 169
    RULE_python_literal_expression = 170
    RULE_python_identifier = 171
    RULE_java_statement = 172
    RULE_java_expression = 173
    RULE_java_primary_expression = 174
    RULE_java_this_expression = 175
    RULE_java_new_expression = 176
    RULE_java_selector_expression = 177
    RULE_java_method_expression = 178
    RULE_java_arguments = 179
    RULE_java_item_expression = 180
    RULE_java_parenthesis_expression = 181
    RULE_java_identifier_expression = 182
    RULE_java_class_identifier_expression = 183
    RULE_java_literal_expression = 184
    RULE_java_identifier = 185
    RULE_csharp_statement = 186
    RULE_csharp_expression = 187
    RULE_csharp_primary_expression = 188
    RULE_csharp_this_expression = 189
    RULE_csharp_new_expression = 190
    RULE_csharp_selector_expression = 191
    RULE_csharp_method_expression = 192
    RULE_csharp_arguments = 193
    RULE_csharp_item_expression = 194
    RULE_csharp_parenthesis_expression = 195
    RULE_csharp_identifier_expression = 196
    RULE_csharp_literal_expression = 197
    RULE_csharp_identifier = 198

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"getter_method_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"full_argument_list", 
                   u"typed_argument", u"statement", u"store_statement", 
                   u"method_call_statement", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"return_statement", 
                   u"expression", u"unresolved_expression", u"unresolved_selector", 
                   u"invocation_expression", u"invocation_trailer", u"instance_expression", 
                   u"instance_selector", u"document_expression", u"constructor_expression", 
                   u"read_expression", u"write_statement", u"ambiguous_expression", 
                   u"fetch_expression", u"sorted_expression", u"argument_assignment_list", 
                   u"with_argument_assignment_list", u"argument_assignment", 
                   u"assign_instance_statement", u"child_instance", u"assign_tuple_statement", 
                   u"lfs", u"lfp", u"indent", u"dedent", u"null_literal", 
                   u"declaration_list", u"declarations", u"declaration", 
                   u"resource_declaration", u"enum_declaration", u"native_symbol_list", 
                   u"category_symbol_list", u"symbol_list", u"attribute_constraint", 
                   u"list_literal", u"set_literal", u"expression_list", 
                   u"range_literal", u"typedef", u"primary_type", u"native_type", 
                   u"category_type", u"mutable_category_type", u"code_type", 
                   u"category_declaration", u"type_identifier_list", u"method_identifier", 
                   u"identifier", u"variable_identifier", u"type_identifier", 
                   u"symbol_identifier", u"argument_list", u"argument", 
                   u"operator_argument", u"named_argument", u"code_argument", 
                   u"category_or_any_type", u"any_type", u"member_method_declaration_list", 
                   u"member_method_declaration", u"native_member_method_declaration_list", 
                   u"native_member_method_declaration", u"native_category_binding", 
                   u"python_category_binding", u"python_module", u"module_token", 
                   u"javascript_category_binding", u"javascript_module", 
                   u"variable_identifier_list", u"method_declaration", u"comment_statement", 
                   u"native_statement_list", u"native_statement", u"python_native_statement", 
                   u"javascript_native_statement", u"statement_list", u"assertion_list", 
                   u"switch_case_statement_list", u"catch_statement_list", 
                   u"literal_collection", u"atomic_literal", u"literal_list_literal", 
                   u"selectable_expression", u"this_expression", u"parenthesis_expression", 
                   u"literal_expression", u"collection_literal", u"tuple_literal", 
                   u"dict_literal", u"expression_tuple", u"dict_entry_list", 
                   u"dict_entry", u"slice_arguments", u"assign_variable_statement", 
                   u"assignable_instance", u"is_expression", u"order_by_list", 
                   u"order_by", u"operator", u"new_token", u"key_token", 
                   u"value_token", u"symbols_token", u"assign", u"multiply", 
                   u"divide", u"idivide", u"modulo", u"javascript_statement", 
                   u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_new_expression", 
                   u"javascript_selector_expression", u"javascript_method_expression", 
                   u"javascript_arguments", u"javascript_item_expression", 
                   u"javascript_parenthesis_expression", u"javascript_identifier_expression", 
                   u"javascript_literal_expression", u"javascript_identifier", 
                   u"python_statement", u"python_expression", u"python_primary_expression", 
                   u"python_selector_expression", u"python_method_expression", 
                   u"python_argument_list", u"python_ordinal_argument_list", 
                   u"python_named_argument_list", u"python_parenthesis_expression", 
                   u"python_identifier_expression", u"python_literal_expression", 
                   u"python_identifier", u"java_statement", u"java_expression", 
                   u"java_primary_expression", u"java_this_expression", 
                   u"java_new_expression", u"java_selector_expression", 
                   u"java_method_expression", u"java_arguments", u"java_item_expression", 
                   u"java_parenthesis_expression", u"java_identifier_expression", 
                   u"java_class_identifier_expression", u"java_literal_expression", 
                   u"java_identifier", u"csharp_statement", u"csharp_expression", 
                   u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_new_expression", u"csharp_selector_expression", 
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
    COMMENT=8
    JAVA=9
    CSHARP=10
    PYTHON2=11
    PYTHON3=12
    JAVASCRIPT=13
    SWIFT=14
    COLON=15
    SEMI=16
    COMMA=17
    RANGE=18
    DOT=19
    LPAR=20
    RPAR=21
    LBRAK=22
    RBRAK=23
    LCURL=24
    RCURL=25
    QMARK=26
    XMARK=27
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
    BLOB=62
    IMAGE=63
    UUID=64
    ABSTRACT=65
    ALL=66
    ALWAYS=67
    AND=68
    ANY=69
    AS=70
    ASC=71
    ATTR=72
    ATTRIBUTE=73
    ATTRIBUTES=74
    BINDINGS=75
    BY=76
    CASE=77
    CATCH=78
    CATEGORY=79
    CLASS=80
    CLOSE=81
    CONTAINS=82
    DEF=83
    DEFAULT=84
    DEFINE=85
    DESC=86
    DO=87
    DOING=88
    EACH=89
    ELSE=90
    ENUM=91
    ENUMERATED=92
    EXCEPT=93
    EXECUTE=94
    EXPECTING=95
    EXTENDS=96
    FETCH=97
    FINALLY=98
    FOR=99
    FROM=100
    GETTER=101
    IF=102
    IN=103
    INVOKE=104
    IS=105
    MATCHING=106
    METHOD=107
    METHODS=108
    MODULO=109
    MUTABLE=110
    NATIVE=111
    NONE=112
    NOT=113
    NOTHING=114
    NULL=115
    ON=116
    ONE=117
    OPEN=118
    OPERATOR=119
    OR=120
    ORDER=121
    OTHERWISE=122
    PASS=123
    RAISE=124
    READ=125
    RECEIVING=126
    RESOURCE=127
    RETURN=128
    RETURNING=129
    ROWS=130
    SELF=131
    SETTER=132
    SINGLETON=133
    SORTED=134
    STORABLE=135
    STORE=136
    SWITCH=137
    TEST=138
    THIS=139
    THROW=140
    TO=141
    TRY=142
    VERIFYING=143
    WITH=144
    WHEN=145
    WHERE=146
    WHILE=147
    WRITE=148
    BOOLEAN_LITERAL=149
    CHAR_LITERAL=150
    MIN_INTEGER=151
    MAX_INTEGER=152
    SYMBOL_IDENTIFIER=153
    TYPE_IDENTIFIER=154
    VARIABLE_IDENTIFIER=155
    NATIVE_IDENTIFIER=156
    DOLLAR_IDENTIFIER=157
    TEXT_LITERAL=158
    INTEGER_LITERAL=159
    HEXA_LITERAL=160
    DECIMAL_LITERAL=161
    DATETIME_LITERAL=162
    TIME_LITERAL=163
    DATE_LITERAL=164
    PERIOD_LITERAL=165

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

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

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

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

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
            self.state = 398
            self.match(EParser.DEFINE)
            self.state = 399 
            localctx.name = self.type_identifier()
            self.state = 400
            self.match(EParser.AS)
            self.state = 401
            self.match(EParser.ENUMERATED)
            self.state = 404
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 402
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 403 
                localctx.derived = self.type_identifier()

            else:
                raise NoViableAltException(self)

            self.state = 411
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 406 
                localctx.attrs = self.attribute_list()
                self.state = 407
                self.match(EParser.COMMA)
                self.state = 408
                self.match(EParser.AND)
                pass

            elif la_ == 2:
                self.state = 410
                self.match(EParser.WITH)
                pass


            self.state = 413 
            self.symbols_token()
            self.state = 414
            self.match(EParser.COLON)
            self.state = 415 
            self.indent()
            self.state = 416 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 417 
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

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

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
            self.state = 419
            self.match(EParser.DEFINE)
            self.state = 420 
            localctx.name = self.type_identifier()
            self.state = 421
            self.match(EParser.AS)
            self.state = 422
            self.match(EParser.ENUMERATED)
            self.state = 423 
            localctx.typ = self.native_type()
            self.state = 424
            self.match(EParser.WITH)
            self.state = 425 
            self.symbols_token()
            self.state = 426
            self.match(EParser.COLON)
            self.state = 427 
            self.indent()
            self.state = 428 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 429 
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
            self.state = 431 
            localctx.name = self.symbol_identifier()
            self.state = 432
            self.match(EParser.WITH)
            self.state = 433 
            localctx.exp = self.expression(0)
            self.state = 434
            self.match(EParser.AS)
            self.state = 435 
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
            self.state = 437 
            localctx.name = self.symbol_identifier()
            self.state = 438 
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 441
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 439
                self.match(EParser.AND)
                self.state = 440 
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

        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(EParser.DEFINE)
            self.state = 444 
            localctx.name = self.variable_identifier()
            self.state = 445
            self.match(EParser.AS)
            self.state = 447
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 446
                self.match(EParser.STORABLE)


            self.state = 449 
            localctx.typ = self.typedef(0)
            self.state = 450
            self.match(EParser.ATTRIBUTE)
            self.state = 452
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 451 
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
            self.methods = None # Member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(EParser.Derived_listContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(EParser.DEFINE)
            self.state = 455 
            localctx.name = self.type_identifier()
            self.state = 456
            self.match(EParser.AS)
            self.state = 458
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 457
                self.match(EParser.STORABLE)


            self.state = 462
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 460
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 461 
                localctx.derived = self.derived_list()

            else:
                raise NoViableAltException(self)

            self.state = 482
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 464 
                localctx.attrs = self.attribute_list()
                self.state = 473
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 465
                    self.match(EParser.COMMA)
                    self.state = 466
                    self.match(EParser.AND)
                    self.state = 467
                    self.match(EParser.METHODS)
                    self.state = 468
                    self.match(EParser.COLON)
                    self.state = 469 
                    self.indent()
                    self.state = 470 
                    localctx.methods = self.member_method_declaration_list(0)
                    self.state = 471 
                    self.dedent()



            elif la_ == 2:
                self.state = 475
                self.match(EParser.WITH)
                self.state = 476
                self.match(EParser.METHODS)
                self.state = 477
                self.match(EParser.COLON)
                self.state = 478 
                self.indent()
                self.state = 479 
                localctx.methods = self.member_method_declaration_list(0)
                self.state = 480 
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
            self.methods = None # Member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SINGLETON(self):
            return self.getToken(EParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)


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
            self.state = 484
            self.match(EParser.DEFINE)
            self.state = 485 
            localctx.name = self.type_identifier()
            self.state = 486
            self.match(EParser.AS)
            self.state = 487
            self.match(EParser.SINGLETON)
            self.state = 506
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 488 
                localctx.attrs = self.attribute_list()
                self.state = 497
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 489
                    self.match(EParser.COMMA)
                    self.state = 490
                    self.match(EParser.AND)
                    self.state = 491
                    self.match(EParser.METHODS)
                    self.state = 492
                    self.match(EParser.COLON)
                    self.state = 493 
                    self.indent()
                    self.state = 494 
                    localctx.methods = self.member_method_declaration_list(0)
                    self.state = 495 
                    self.dedent()



            elif la_ == 2:
                self.state = 499
                self.match(EParser.WITH)
                self.state = 500
                self.match(EParser.METHODS)
                self.state = 501
                self.match(EParser.COLON)
                self.state = 502 
                self.indent()
                self.state = 503 
                localctx.methods = self.member_method_declaration_list(0)
                self.state = 504 
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



    def derived_list(self):

        localctx = EParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.state = 513
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 508 
                localctx.items = self.type_identifier_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 509 
                localctx.items = self.type_identifier_list(0)
                self.state = 510
                self.match(EParser.AND)
                self.state = 511 
                localctx.item = self.type_identifier()
                pass


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

        def OPERATOR(self):
            return self.getToken(EParser.OPERATOR, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

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
        self.enterRule(localctx, 16, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(EParser.DEFINE)
            self.state = 516 
            localctx.op = self.operator()
            self.state = 517
            self.match(EParser.AS)
            self.state = 518
            self.match(EParser.OPERATOR)
            self.state = 519
            self.match(EParser.RECEIVING)
            self.state = 520 
            localctx.arg = self.operator_argument()
            self.state = 523
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 521
                self.match(EParser.RETURNING)
                self.state = 522 
                localctx.typ = self.typedef(0)


            self.state = 525
            self.match(EParser.DOING)
            self.state = 526
            self.match(EParser.COLON)
            self.state = 527 
            self.indent()
            self.state = 528 
            localctx.stmts = self.statement_list(0)
            self.state = 529 
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
        self.enterRule(localctx, 18, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(EParser.DEFINE)
            self.state = 532 
            localctx.name = self.variable_identifier()
            self.state = 533
            self.match(EParser.SETTER)
            self.state = 534
            self.match(EParser.DOING)
            self.state = 535
            self.match(EParser.COLON)
            self.state = 536 
            self.indent()
            self.state = 537 
            localctx.stmts = self.statement_list(0)
            self.state = 538 
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
        self.enterRule(localctx, 20, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(EParser.DEFINE)
            self.state = 541 
            localctx.name = self.variable_identifier()
            self.state = 542
            self.match(EParser.GETTER)
            self.state = 543
            self.match(EParser.DOING)
            self.state = 544
            self.match(EParser.COLON)
            self.state = 545 
            self.indent()
            self.state = 546 
            localctx.stmts = self.statement_list(0)
            self.state = 547 
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
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

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


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingsContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(EParser.AND)
            else:
                return self.getToken(EParser.AND, i)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


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
        self.enterRule(localctx, 22, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(EParser.DEFINE)
            self.state = 550 
            localctx.name = self.type_identifier()
            self.state = 551
            self.match(EParser.AS)
            self.state = 553
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 552
                self.match(EParser.STORABLE)


            self.state = 555
            self.match(EParser.NATIVE)
            self.state = 556
            self.match(EParser.CATEGORY)
            self.state = 564
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 557 
                localctx.attrs = self.attribute_list()
                self.state = 558
                self.match(EParser.COMMA)
                self.state = 559
                self.match(EParser.AND)
                self.state = 560
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 562
                self.match(EParser.WITH)
                self.state = 563
                self.match(EParser.BINDINGS)
                pass


            self.state = 566
            self.match(EParser.COLON)
            self.state = 567 
            self.indent()
            self.state = 568 
            localctx.bindings = self.native_category_bindings()
            self.state = 569 
            self.dedent()
            self.state = 578
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 570 
                self.lfp()
                self.state = 571
                self.match(EParser.AND)
                self.state = 572
                self.match(EParser.METHODS)
                self.state = 573
                self.match(EParser.COLON)
                self.state = 574 
                self.indent()
                self.state = 575 
                localctx.methods = self.native_member_method_declaration_list(0)
                self.state = 576 
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
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(EParser.RESOURCE, 0)

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


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingsContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(EParser.AND)
            else:
                return self.getToken(EParser.AND, i)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)


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
        self.enterRule(localctx, 24, self.RULE_native_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(EParser.DEFINE)
            self.state = 581 
            localctx.name = self.type_identifier()
            self.state = 582
            self.match(EParser.AS)
            self.state = 583
            self.match(EParser.NATIVE)
            self.state = 584
            self.match(EParser.RESOURCE)
            self.state = 592
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 585 
                localctx.attrs = self.attribute_list()
                self.state = 586
                self.match(EParser.COMMA)
                self.state = 587
                self.match(EParser.AND)
                self.state = 588
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 590
                self.match(EParser.WITH)
                self.state = 591
                self.match(EParser.BINDINGS)
                pass


            self.state = 594
            self.match(EParser.COLON)
            self.state = 595 
            self.indent()
            self.state = 596 
            localctx.bindings = self.native_category_bindings()
            self.state = 597 
            self.dedent()
            self.state = 606
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 598 
                self.lfp()
                self.state = 599
                self.match(EParser.AND)
                self.state = 600
                self.match(EParser.METHODS)
                self.state = 601
                self.match(EParser.COLON)
                self.state = 602 
                self.indent()
                self.state = 603 
                localctx.methods = self.native_member_method_declaration_list(0)
                self.state = 604 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def native_category_binding_list(self):
            return self.getTypedRuleContext(EParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = EParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(EParser.DEFINE)
            self.state = 609
            self.match(EParser.CATEGORY)
            self.state = 610
            self.match(EParser.BINDINGS)
            self.state = 611
            self.match(EParser.AS)
            self.state = 612
            self.match(EParser.COLON)
            self.state = 613 
            self.indent()
            self.state = 614 
            localctx.items = self.native_category_binding_list(0)
            self.state = 615 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(EParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 618 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 626
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryBindingListItemContext(self, EParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 620
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 621 
                    self.lfp()
                    self.state = 622 
                    localctx.item = self.native_category_binding() 
                self.state = 628
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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



    class AttributeListContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeList(self)


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



    def attribute_list(self):

        localctx = EParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attribute_list)
        try:
            self.state = 639
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(EParser.WITH)
                self.state = 630
                self.match(EParser.ATTRIBUTE)
                self.state = 631 
                localctx.item = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 632
                self.match(EParser.WITH)
                self.state = 633
                self.match(EParser.ATTRIBUTES)
                self.state = 634 
                localctx.items = self.variable_identifier_list(0)
                self.state = 637
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 635
                    self.match(EParser.AND)
                    self.state = 636 
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
        self.enterRule(localctx, 32, self.RULE_abstract_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(EParser.DEFINE)
            self.state = 642 
            localctx.name = self.method_identifier()
            self.state = 643
            self.match(EParser.AS)
            self.state = 644
            self.match(EParser.ABSTRACT)
            self.state = 645
            self.match(EParser.METHOD)
            self.state = 648
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 646
                self.match(EParser.RECEIVING)
                self.state = 647 
                localctx.args = self.full_argument_list()


            self.state = 652
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 650
                self.match(EParser.RETURNING)
                self.state = 651 
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

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

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
        self.enterRule(localctx, 34, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(EParser.DEFINE)
            self.state = 655 
            localctx.name = self.method_identifier()
            self.state = 656
            self.match(EParser.AS)
            self.state = 657
            self.match(EParser.METHOD)
            self.state = 660
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 658
                self.match(EParser.RECEIVING)
                self.state = 659 
                localctx.args = self.full_argument_list()


            self.state = 664
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 662
                self.match(EParser.RETURNING)
                self.state = 663 
                localctx.typ = self.typedef(0)


            self.state = 666
            self.match(EParser.DOING)
            self.state = 667
            self.match(EParser.COLON)
            self.state = 668 
            self.indent()
            self.state = 669 
            localctx.stmts = self.statement_list(0)
            self.state = 670 
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
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

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


        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


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
        self.enterRule(localctx, 36, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.match(EParser.DEFINE)
            self.state = 673 
            localctx.name = self.method_identifier()
            self.state = 674
            self.match(EParser.AS)
            self.state = 675
            self.match(EParser.NATIVE)
            self.state = 676
            self.match(EParser.METHOD)
            self.state = 679
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 677
                self.match(EParser.RECEIVING)
                self.state = 678 
                localctx.args = self.full_argument_list()


            self.state = 683
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 681
                self.match(EParser.RETURNING)
                self.state = 682 
                localctx.typ = self.category_or_any_type()


            self.state = 685
            self.match(EParser.DOING)
            self.state = 686
            self.match(EParser.COLON)
            self.state = 687 
            self.indent()
            self.state = 688 
            localctx.stmts = self.native_statement_list(0)
            self.state = 689 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

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


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def VERIFYING(self):
            return self.getToken(EParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(EParser.Assertion_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = EParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(EParser.DEFINE)
            self.state = 692
            localctx.name = self.match(EParser.TEXT_LITERAL)
            self.state = 693
            self.match(EParser.AS)
            self.state = 694
            self.match(EParser.TEST)
            self.state = 695
            self.match(EParser.METHOD)
            self.state = 696
            self.match(EParser.DOING)
            self.state = 697
            self.match(EParser.COLON)
            self.state = 698 
            self.indent()
            self.state = 699 
            localctx.stmts = self.statement_list(0)
            self.state = 700 
            self.dedent()
            self.state = 701 
            self.lfp()
            self.state = 702
            self.match(EParser.AND)
            self.state = 703
            self.match(EParser.VERIFYING)
            self.state = 710
            token = self._input.LA(1)
            if token in [EParser.COLON]:
                self.state = 704
                self.match(EParser.COLON)
                self.state = 705 
                self.indent()
                self.state = 706 
                localctx.exps = self.assertion_list(0)
                self.state = 707 
                self.dedent()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                self.state = 709 
                localctx.error = self.symbol_identifier()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssertionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assertion

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = EParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712 
            localctx.exp = self.expression(0)
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
        self.enterRule(localctx, 42, self.RULE_full_argument_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714 
            localctx.items = self.argument_list(0)
            self.state = 717
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 715
                self.match(EParser.AND)
                self.state = 716 
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
        self.enterRule(localctx, 44, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719 
            localctx.typ = self.category_or_any_type()
            self.state = 720 
            localctx.name = self.variable_identifier()
            self.state = 722
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 721 
                localctx.attrs = self.attribute_list()


            self.state = 726
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 724
                self.match(EParser.EQ)
                self.state = 725 
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



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(EParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(EParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStoreStatement(self)


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



    def statement(self):

        localctx = EParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 745
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 728 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 729 
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 730 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 731 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 732 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 6:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 733 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 7:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 734 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 8:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 735 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 9:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 736 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 10:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 737 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 11:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 738 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 12:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 739 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 13:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 740 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 14:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 741 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 15:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 742 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 16:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 743 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 17:
                localctx = EParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 744 
                localctx.decl = self.comment_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exps = None # Expression_listContext

        def STORE(self):
            return self.getToken(EParser.STORE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_store_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = EParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_store_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 747
            self.match(EParser.STORE)
            self.state = 748 
            localctx.exps = self.expression_list(0)
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



    def method_call_statement(self):

        localctx = EParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_call_statement)
        try:
            self.state = 755
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 750 
                localctx.exp = self.unresolved_expression(0)
                self.state = 752
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 751 
                    localctx.args = self.argument_assignment_list()



            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 754 
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
        self.enterRule(localctx, 52, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.match(EParser.WITH)
            self.state = 758 
            localctx.stmt = self.assign_variable_statement()
            self.state = 759
            self.match(EParser.COMMA)
            self.state = 760
            self.match(EParser.DO)
            self.state = 761
            self.match(EParser.COLON)
            self.state = 762 
            self.indent()
            self.state = 763 
            localctx.stmts = self.statement_list(0)
            self.state = 764 
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
        self.enterRule(localctx, 54, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 766
            self.match(EParser.WITH)
            self.state = 767 
            localctx.typ = self.type_identifier()
            self.state = 768
            self.match(EParser.COMMA)
            self.state = 769
            self.match(EParser.DO)
            self.state = 770
            self.match(EParser.COLON)
            self.state = 771 
            self.indent()
            self.state = 772 
            localctx.stmts = self.statement_list(0)
            self.state = 773 
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
        self.enterRule(localctx, 56, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.match(EParser.SWITCH)
            self.state = 776
            self.match(EParser.ON)
            self.state = 777 
            localctx.exp = self.expression(0)
            self.state = 778
            self.match(EParser.COLON)
            self.state = 779 
            self.indent()
            self.state = 780 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 788
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 781 
                self.lfp()
                self.state = 782
                self.match(EParser.OTHERWISE)
                self.state = 783
                self.match(EParser.COLON)
                self.state = 784 
                self.indent()
                self.state = 785 
                localctx.stmts = self.statement_list(0)
                self.state = 786 
                self.dedent()


            self.state = 790 
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
        self.enterRule(localctx, 58, self.RULE_switch_case_statement)
        try:
            self.state = 807
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 792
                self.match(EParser.WHEN)
                self.state = 793 
                localctx.exp = self.atomic_literal()
                self.state = 794
                self.match(EParser.COLON)
                self.state = 795 
                self.indent()
                self.state = 796 
                localctx.stmts = self.statement_list(0)
                self.state = 797 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 799
                self.match(EParser.WHEN)
                self.state = 800
                self.match(EParser.IN)
                self.state = 801 
                localctx.exp = self.literal_collection()
                self.state = 802
                self.match(EParser.COLON)
                self.state = 803 
                self.indent()
                self.state = 804 
                localctx.stmts = self.statement_list(0)
                self.state = 805 
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
        self.enterRule(localctx, 60, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self.match(EParser.FOR)
            self.state = 810
            self.match(EParser.EACH)
            self.state = 811 
            localctx.name1 = self.variable_identifier()
            self.state = 814
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 812
                self.match(EParser.COMMA)
                self.state = 813 
                localctx.name2 = self.variable_identifier()


            self.state = 816
            self.match(EParser.IN)
            self.state = 817 
            localctx.source = self.expression(0)
            self.state = 818
            self.match(EParser.COLON)
            self.state = 819 
            self.indent()
            self.state = 820 
            localctx.stmts = self.statement_list(0)
            self.state = 821 
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
        self.enterRule(localctx, 62, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 823
            self.match(EParser.DO)
            self.state = 824
            self.match(EParser.COLON)
            self.state = 825 
            self.indent()
            self.state = 826 
            localctx.stmts = self.statement_list(0)
            self.state = 827 
            self.dedent()
            self.state = 828 
            self.lfp()
            self.state = 829
            self.match(EParser.WHILE)
            self.state = 830 
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
        self.enterRule(localctx, 64, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 832
            self.match(EParser.WHILE)
            self.state = 833 
            localctx.exp = self.expression(0)
            self.state = 834
            self.match(EParser.COLON)
            self.state = 835 
            self.indent()
            self.state = 836 
            localctx.stmts = self.statement_list(0)
            self.state = 837 
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
        self.enterRule(localctx, 66, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 839
            self.match(EParser.IF)
            self.state = 840 
            localctx.exp = self.expression(0)
            self.state = 841
            self.match(EParser.COLON)
            self.state = 842 
            self.indent()
            self.state = 843 
            localctx.stmts = self.statement_list(0)
            self.state = 844 
            self.dedent()
            self.state = 848
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 845 
                self.lfp()
                self.state = 846 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 857
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 850 
                self.lfp()
                self.state = 851
                self.match(EParser.ELSE)
                self.state = 852
                self.match(EParser.COLON)
                self.state = 853 
                self.indent()
                self.state = 854 
                localctx.elseStmts = self.statement_list(0)
                self.state = 855 
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 860
            self.match(EParser.ELSE)
            self.state = 861
            self.match(EParser.IF)
            self.state = 862 
            localctx.exp = self.expression(0)
            self.state = 863
            self.match(EParser.COLON)
            self.state = 864 
            self.indent()
            self.state = 865 
            localctx.stmts = self.statement_list(0)
            self.state = 866 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 880
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 868
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 869 
                    self.lfp()
                    self.state = 870
                    self.match(EParser.ELSE)
                    self.state = 871
                    self.match(EParser.IF)
                    self.state = 872 
                    localctx.exp = self.expression(0)
                    self.state = 873
                    self.match(EParser.COLON)
                    self.state = 874 
                    self.indent()
                    self.state = 875 
                    localctx.stmts = self.statement_list(0)
                    self.state = 876 
                    self.dedent() 
                self.state = 882
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 883
            self.match(EParser.RAISE)
            self.state = 884 
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
        self.enterRule(localctx, 72, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 886
            self.match(EParser.SWITCH)
            self.state = 887
            self.match(EParser.ON)
            self.state = 888 
            localctx.name = self.variable_identifier()
            self.state = 889
            self.match(EParser.DOING)
            self.state = 890
            self.match(EParser.COLON)
            self.state = 891 
            self.indent()
            self.state = 892 
            localctx.stmts = self.statement_list(0)
            self.state = 893 
            self.dedent()
            self.state = 894 
            self.lfs()
            self.state = 896
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 895 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 909
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 901
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 898
                    self.match(EParser.OTHERWISE)

                elif token in [EParser.WHEN]:
                    self.state = 899
                    self.match(EParser.WHEN)
                    self.state = 900
                    self.match(EParser.ANY)

                else:
                    raise NoViableAltException(self)

                self.state = 903
                self.match(EParser.COLON)
                self.state = 904 
                self.indent()
                self.state = 905 
                localctx.anyStmts = self.statement_list(0)
                self.state = 906 
                self.dedent()
                self.state = 907 
                self.lfs()


            self.state = 918
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 911
                self.match(EParser.ALWAYS)
                self.state = 912
                self.match(EParser.COLON)
                self.state = 913 
                self.indent()
                self.state = 914 
                localctx.finalStmts = self.statement_list(0)
                self.state = 915 
                self.dedent()
                self.state = 916 
                self.lfs()


            self.state = 920 
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
        self.enterRule(localctx, 74, self.RULE_catch_statement)
        try:
            self.state = 941
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 922
                self.match(EParser.WHEN)
                self.state = 923 
                localctx.name = self.symbol_identifier()
                self.state = 924
                self.match(EParser.COLON)
                self.state = 925 
                self.indent()
                self.state = 926 
                localctx.stmts = self.statement_list(0)
                self.state = 927 
                self.dedent()
                self.state = 928 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 930
                self.match(EParser.WHEN)
                self.state = 931
                self.match(EParser.IN)
                self.state = 932
                self.match(EParser.LBRAK)
                self.state = 933 
                localctx.exp = self.symbol_list(0)
                self.state = 934
                self.match(EParser.RBRAK)
                self.state = 935
                self.match(EParser.COLON)
                self.state = 936 
                self.indent()
                self.state = 937 
                localctx.stmts = self.statement_list(0)
                self.state = 938 
                self.dedent()
                self.state = 939 
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
        self.enterRule(localctx, 76, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 943
            self.match(EParser.RETURN)
            self.state = 945
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 944 
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


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(EParser.FOR, 0)
        def EACH(self):
            return self.getToken(EParser.EACH, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIteratorExpression(self)


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



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 973
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 948
                self.match(EParser.MINUS)
                self.state = 949 
                localctx.exp = self.expression(39)
                pass

            elif la_ == 2:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 950
                self.match(EParser.NOT)
                self.state = 951 
                localctx.exp = self.expression(38)
                pass

            elif la_ == 3:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 952
                self.match(EParser.CODE)
                self.state = 953
                self.match(EParser.COLON)
                self.state = 954 
                localctx.exp = self.expression(11)
                pass

            elif la_ == 4:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 955 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 956 
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 6:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 957 
                localctx.exp = self.unresolved_expression(0)
                self.state = 958 
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 960
                self.match(EParser.EXECUTE)
                self.state = 961
                self.match(EParser.COLON)
                self.state = 962 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 963
                self.match(EParser.METHOD_T)
                self.state = 964
                self.match(EParser.COLON)
                self.state = 965 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 966 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 10:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 967 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 11:
                localctx = EParser.FetchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 968 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 12:
                localctx = EParser.ReadExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 969 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 13:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 970 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 14:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 971 
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 15:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 972 
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1078
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1076
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 975
                        if not self.precpred(self._ctx, 37):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 37)")
                        self.state = 976 
                        self.multiply()
                        self.state = 977 
                        localctx.right = self.expression(38)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 979
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 980 
                        self.divide()
                        self.state = 981 
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 983
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 984 
                        self.modulo()
                        self.state = 985 
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 987
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 988 
                        self.idivide()
                        self.state = 989 
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 991
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 992
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 993 
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 994
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 995
                        self.match(EParser.LT)
                        self.state = 996 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 997
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 998
                        self.match(EParser.LTE)
                        self.state = 999 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1000
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1001
                        self.match(EParser.GT)
                        self.state = 1002 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1003
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1004
                        self.match(EParser.GTE)
                        self.state = 1005 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1006
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1007
                        self.match(EParser.EQ)
                        self.state = 1008 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1009
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1010
                        self.match(EParser.LTGT)
                        self.state = 1011 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1012
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1013
                        self.match(EParser.TILDE)
                        self.state = 1014 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 13:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1015
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1016
                        self.match(EParser.OR)
                        self.state = 1017 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 14:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1018
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1019
                        self.match(EParser.AND)
                        self.state = 1020 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 15:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1021
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1022
                        self.match(EParser.IF)
                        self.state = 1023 
                        localctx.test = self.expression(0)
                        self.state = 1024
                        self.match(EParser.ELSE)
                        self.state = 1025 
                        localctx.ifFalse = self.expression(22)
                        pass

                    elif la_ == 16:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1027
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1028
                        self.match(EParser.IN)
                        self.state = 1029 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 17:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1030
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1031
                        self.match(EParser.CONTAINS)
                        self.state = 1032 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 18:
                        localctx = EParser.ContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1033
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1034
                        self.match(EParser.CONTAINS)
                        self.state = 1035
                        self.match(EParser.ALL)
                        self.state = 1036 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 19:
                        localctx = EParser.ContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1037
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1038
                        self.match(EParser.CONTAINS)
                        self.state = 1039
                        self.match(EParser.ANY)
                        self.state = 1040 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1041
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1042
                        self.match(EParser.NOT)
                        self.state = 1043
                        self.match(EParser.IN)
                        self.state = 1044 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1045
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1046
                        self.match(EParser.NOT)
                        self.state = 1047
                        self.match(EParser.CONTAINS)
                        self.state = 1048 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1049
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1050
                        self.match(EParser.NOT)
                        self.state = 1051
                        self.match(EParser.CONTAINS)
                        self.state = 1052
                        self.match(EParser.ALL)
                        self.state = 1053 
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 23:
                        localctx = EParser.NotContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1054
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1055
                        self.match(EParser.NOT)
                        self.state = 1056
                        self.match(EParser.CONTAINS)
                        self.state = 1057
                        self.match(EParser.ANY)
                        self.state = 1058 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 24:
                        localctx = EParser.IteratorExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1059
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1060
                        self.match(EParser.FOR)
                        self.state = 1061
                        self.match(EParser.EACH)
                        self.state = 1062 
                        localctx.name = self.variable_identifier()
                        self.state = 1063
                        self.match(EParser.IN)
                        self.state = 1064 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1066
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1067
                        self.match(EParser.IS)
                        self.state = 1068
                        self.match(EParser.NOT)
                        self.state = 1069 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1070
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1071
                        self.match(EParser.IS)
                        self.state = 1072 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1073
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1074
                        self.match(EParser.AS)
                        self.state = 1075 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1080
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1082 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1088
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1084
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1085 
                    localctx.selector = self.unresolved_selector() 
                self.state = 1090
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1091
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1092
            self.match(EParser.DOT)
            self.state = 1093 
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
        self.enterRule(localctx, 84, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1095
            self.match(EParser.INVOKE)
            self.state = 1096
            self.match(EParser.COLON)
            self.state = 1097 
            localctx.name = self.variable_identifier()
            self.state = 1098 
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
        self.enterRule(localctx, 86, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1100
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



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1103 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1105
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1106 
                    localctx.selector = self.instance_selector() 
                self.state = 1111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_instance_selector)
        try:
            self.state = 1125
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1112
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1113
                self.match(EParser.DOT)
                self.state = 1114 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1115
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1116
                self.match(EParser.LBRAK)
                self.state = 1117 
                localctx.xslice = self.slice_arguments()
                self.state = 1118
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1120
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1121
                self.match(EParser.LBRAK)
                self.state = 1122 
                localctx.exp = self.expression(0)
                self.state = 1123
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

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

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
        self.enterRule(localctx, 92, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1127
            self.match(EParser.DOCUMENT)
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



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.firstArg = None # ExpressionContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)

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


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)

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



    def constructor_expression(self):

        localctx = EParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1150
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1129 
                localctx.typ = self.mutable_category_type()
                self.state = 1130
                self.match(EParser.FROM)
                self.state = 1131 
                localctx.firstArg = self.expression(0)
                self.state = 1140
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 1133
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1132
                        self.match(EParser.COMMA)


                    self.state = 1135 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1138
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        self.state = 1136
                        self.match(EParser.AND)
                        self.state = 1137 
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1142 
                localctx.typ = self.mutable_category_type()
                self.state = 1148
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 1143 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1146
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        self.state = 1144
                        self.match(EParser.AND)
                        self.state = 1145 
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
        self.enterRule(localctx, 96, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152
            self.match(EParser.READ)
            self.state = 1153
            self.match(EParser.FROM)
            self.state = 1154 
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
        self.enterRule(localctx, 98, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156
            self.match(EParser.WRITE)
            self.state = 1157 
            localctx.what = self.expression(0)
            self.state = 1158
            self.match(EParser.TO)
            self.state = 1159 
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
        self.enterRule(localctx, 100, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1161 
            localctx.method = self.unresolved_expression(0)
            self.state = 1162
            self.match(EParser.MINUS)
            self.state = 1163 
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


        def getRuleIndex(self):
            return EParser.RULE_fetch_expression

     
        def copyFrom(self, ctx):
            super(EParser.Fetch_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_expressionContext)
            super(EParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)
        def ONE(self):
            return self.getToken(EParser.ONE, 0)
        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchOne(self)


    class FetchListContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_expressionContext)
            super(EParser.FetchListContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

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


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchList(self)


    class FetchAllContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_expressionContext)
            super(EParser.FetchAllContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.xfilter = None # ExpressionContext
            self.xorder = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)
        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)
        def ORDER(self):
            return self.getToken(EParser.ORDER, 0)
        def BY(self):
            return self.getToken(EParser.BY, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def TO(self):
            return self.getToken(EParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def order_by_list(self):
            return self.getTypedRuleContext(EParser.Order_by_listContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchAll(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchAll(self)



    def fetch_expression(self):

        localctx = EParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fetch_expression)
        self._la = 0 # Token type
        try:
            self.state = 1203
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                localctx = EParser.FetchListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1165
                self.match(EParser.FETCH)
                self.state = 1166
                self.match(EParser.ANY)
                self.state = 1167 
                localctx.name = self.variable_identifier()
                self.state = 1168
                self.match(EParser.FROM)
                self.state = 1169 
                localctx.source = self.expression(0)
                self.state = 1170
                self.match(EParser.WHERE)
                self.state = 1171 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1173
                self.match(EParser.FETCH)
                self.state = 1174
                self.match(EParser.ONE)

                self.state = 1176
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE or _la==EParser.TYPE_IDENTIFIER:
                    self.state = 1175 
                    localctx.typ = self.mutable_category_type()


                self.state = 1178
                self.match(EParser.WHERE)
                self.state = 1179 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.FetchAllContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1180
                self.match(EParser.FETCH)
                self.state = 1192
                token = self._input.LA(1)
                if token in [EParser.ALL]:
                    self.state = 1181
                    self.match(EParser.ALL)
                    self.state = 1183
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        self.state = 1182 
                        localctx.typ = self.mutable_category_type()



                elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.MINUS, EParser.LT, EParser.METHOD_T, EParser.CODE, EParser.DOCUMENT, EParser.EXECUTE, EParser.FETCH, EParser.INVOKE, EParser.MUTABLE, EParser.NOT, EParser.NOTHING, EParser.READ, EParser.SELF, EParser.SORTED, EParser.THIS, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                    self.state = 1186
                    la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                    if la_ == 1:
                        self.state = 1185 
                        localctx.typ = self.mutable_category_type()


                    self.state = 1188 
                    localctx.xstart = self.expression(0)
                    self.state = 1189
                    self.match(EParser.TO)
                    self.state = 1190 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1196
                la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
                if la_ == 1:
                    self.state = 1194
                    self.match(EParser.WHERE)
                    self.state = 1195 
                    localctx.xfilter = self.expression(0)


                self.state = 1201
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 1198
                    self.match(EParser.ORDER)
                    self.state = 1199
                    self.match(EParser.BY)
                    self.state = 1200 
                    localctx.xorder = self.order_by_list()


                pass


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
        self.enterRule(localctx, 104, self.RULE_sorted_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self.match(EParser.SORTED)
            self.state = 1206 
            localctx.source = self.instance_expression(0)
            self.state = 1212
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 1207
                self.match(EParser.WITH)
                self.state = 1208 
                localctx.key = self.instance_expression(0)
                self.state = 1209
                self.match(EParser.AS)
                self.state = 1210 
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
        self.enterRule(localctx, 106, self.RULE_argument_assignment_list)
        try:
            self.state = 1228
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1214
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1215 
                localctx.exp = self.expression(0)
                self.state = 1221
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 1216 
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1219
                    la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                    if la_ == 1:
                        self.state = 1217
                        self.match(EParser.AND)
                        self.state = 1218 
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1223 
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1226
                la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                if la_ == 1:
                    self.state = 1224
                    self.match(EParser.AND)
                    self.state = 1225 
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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1231
            self.match(EParser.WITH)
            self.state = 1232 
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1234
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1235
                    self.match(EParser.COMMA)
                    self.state = 1236 
                    localctx.item = self.argument_assignment() 
                self.state = 1241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

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
        self.enterRule(localctx, 110, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1242 
            localctx.exp = self.expression(0)
            self.state = 1243
            self.match(EParser.AS)
            self.state = 1244 
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
        self.enterRule(localctx, 112, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1246 
            localctx.inst = self.assignable_instance(0)
            self.state = 1247 
            self.assign()
            self.state = 1248 
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
        self.enterRule(localctx, 114, self.RULE_child_instance)
        try:
            self.state = 1258
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1250
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1251
                self.match(EParser.DOT)
                self.state = 1252 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1253
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1254
                self.match(EParser.LBRAK)
                self.state = 1255 
                localctx.exp = self.expression(0)
                self.state = 1256
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
        self.enterRule(localctx, 116, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1260 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1261 
            self.assign()
            self.state = 1262 
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
        self.enterRule(localctx, 118, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1264
                    self.match(EParser.LF) 
                self.state = 1269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

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
        self.enterRule(localctx, 120, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1271 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1270
                self.match(EParser.LF)
                self.state = 1273 
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
        self.enterRule(localctx, 122, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1276 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1275
                self.match(EParser.LF)
                self.state = 1278 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1280
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
        self.enterRule(localctx, 124, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1282
                self.match(EParser.LF)
                self.state = 1287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1288
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
        self.enterRule(localctx, 126, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1290
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
        self.enterRule(localctx, 128, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1293
            _la = self._input.LA(1)
            if _la==EParser.COMMENT or _la==EParser.DEFINE:
                self.state = 1292 
                localctx.items = self.declarations(0)


            self.state = 1295 
            self.lfs()
            self.state = 1296
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



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1299 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DeclarationListItemContext(self, EParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1301
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1302 
                    self.lfp()
                    self.state = 1303 
                    localctx.item = self.declaration() 
                self.state = 1309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

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

        def attribute_declaration(self):
            return self.getTypedRuleContext(EParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(EParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(EParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(EParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = EParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMENT:
                self.state = 1310 
                self.comment_statement()
                self.state = 1311 
                self.lfp()
                self.state = 1317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1323
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.state = 1318 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1319 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1320 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1321 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1322 
                self.method_declaration()
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
        self.enterRule(localctx, 134, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1325 
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



    def enum_declaration(self):

        localctx = EParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_enum_declaration)
        try:
            self.state = 1329
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = EParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1327 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1328 
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
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1332 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeSymbolListItemContext(self, EParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1334
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1335 
                    self.lfp()
                    self.state = 1336 
                    localctx.item = self.native_symbol() 
                self.state = 1342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1344 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategorySymbolListItemContext(self, EParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1346
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1347 
                    self.lfp()
                    self.state = 1348 
                    localctx.item = self.category_symbol() 
                self.state = 1354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

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
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1356 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SymbolListItemContext(self, EParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1358
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1359
                    self.match(EParser.COMMA)
                    self.state = 1360 
                    localctx.item = self.symbol_identifier() 
                self.state = 1365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

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



    def attribute_constraint(self):

        localctx = EParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_attribute_constraint)
        try:
            self.state = 1376
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1366
                self.match(EParser.IN)
                self.state = 1367 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1368
                self.match(EParser.IN)
                self.state = 1369 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1370
                self.match(EParser.IN)
                self.state = 1371 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1372
                self.match(EParser.MATCHING)
                self.state = 1373
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1374
                self.match(EParser.MATCHING)
                self.state = 1375 
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
        self.enterRule(localctx, 146, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1378
            self.match(EParser.LBRAK)
            self.state = 1380
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (EParser.EXECUTE - 94)) | (1 << (EParser.FETCH - 94)) | (1 << (EParser.INVOKE - 94)) | (1 << (EParser.MUTABLE - 94)) | (1 << (EParser.NOT - 94)) | (1 << (EParser.NOTHING - 94)) | (1 << (EParser.READ - 94)) | (1 << (EParser.SELF - 94)) | (1 << (EParser.SORTED - 94)) | (1 << (EParser.THIS - 94)) | (1 << (EParser.BOOLEAN_LITERAL - 94)) | (1 << (EParser.CHAR_LITERAL - 94)) | (1 << (EParser.MIN_INTEGER - 94)) | (1 << (EParser.MAX_INTEGER - 94)) | (1 << (EParser.SYMBOL_IDENTIFIER - 94)) | (1 << (EParser.TYPE_IDENTIFIER - 94)) | (1 << (EParser.VARIABLE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (EParser.TEXT_LITERAL - 158)) | (1 << (EParser.INTEGER_LITERAL - 158)) | (1 << (EParser.HEXA_LITERAL - 158)) | (1 << (EParser.DECIMAL_LITERAL - 158)) | (1 << (EParser.DATETIME_LITERAL - 158)) | (1 << (EParser.TIME_LITERAL - 158)) | (1 << (EParser.DATE_LITERAL - 158)) | (1 << (EParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1379 
                localctx.items = self.expression_list(0)


            self.state = 1382
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
        self.enterRule(localctx, 148, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1384
            self.match(EParser.LT)
            self.state = 1386
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (EParser.EXECUTE - 94)) | (1 << (EParser.FETCH - 94)) | (1 << (EParser.INVOKE - 94)) | (1 << (EParser.MUTABLE - 94)) | (1 << (EParser.NOT - 94)) | (1 << (EParser.NOTHING - 94)) | (1 << (EParser.READ - 94)) | (1 << (EParser.SELF - 94)) | (1 << (EParser.SORTED - 94)) | (1 << (EParser.THIS - 94)) | (1 << (EParser.BOOLEAN_LITERAL - 94)) | (1 << (EParser.CHAR_LITERAL - 94)) | (1 << (EParser.MIN_INTEGER - 94)) | (1 << (EParser.MAX_INTEGER - 94)) | (1 << (EParser.SYMBOL_IDENTIFIER - 94)) | (1 << (EParser.TYPE_IDENTIFIER - 94)) | (1 << (EParser.VARIABLE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (EParser.TEXT_LITERAL - 158)) | (1 << (EParser.INTEGER_LITERAL - 158)) | (1 << (EParser.HEXA_LITERAL - 158)) | (1 << (EParser.DECIMAL_LITERAL - 158)) | (1 << (EParser.DATETIME_LITERAL - 158)) | (1 << (EParser.TIME_LITERAL - 158)) | (1 << (EParser.DATE_LITERAL - 158)) | (1 << (EParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1385 
                localctx.items = self.expression_list(0)


            self.state = 1388
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



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1391 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueListItemContext(self, EParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1393
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1394
                    self.match(EParser.COMMA)
                    self.state = 1395 
                    localctx.item = self.expression(0) 
                self.state = 1400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

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
        self.enterRule(localctx, 152, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
            self.match(EParser.LBRAK)
            self.state = 1402 
            localctx.low = self.expression(0)
            self.state = 1403
            self.match(EParser.RANGE)
            self.state = 1404 
            localctx.high = self.expression(0)
            self.state = 1405
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



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 154
        self.enterRecursionRule(localctx, 154, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1408 
            localctx.p = self.primary_type()
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
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1410
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1411
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1412
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1413
                        self.match(EParser.LBRAK)
                        self.state = 1414
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
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

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(EParser.Primary_typeContext, self).copyFrom(ctx)



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



    def primary_type(self):

        localctx = EParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_primary_type)
        try:
            self.state = 1425
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1423 
                localctx.n = self.native_type()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1424 
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



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(EParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_native_type)
        try:
            self.state = 1441
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1427
                self.match(EParser.BOOLEAN)

            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1428
                self.match(EParser.CHARACTER)

            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1429
                self.match(EParser.TEXT)

            elif token in [EParser.IMAGE]:
                localctx = EParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1430
                self.match(EParser.IMAGE)

            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1431
                self.match(EParser.INTEGER)

            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1432
                self.match(EParser.DECIMAL)

            elif token in [EParser.DOCUMENT]:
                localctx = EParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1433
                self.match(EParser.DOCUMENT)

            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1434
                self.match(EParser.DATE)

            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1435
                self.match(EParser.DATETIME)

            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1436
                self.match(EParser.TIME)

            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1437
                self.match(EParser.PERIOD)

            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1438
                self.match(EParser.CODE)

            elif token in [EParser.BLOB]:
                localctx = EParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1439
                self.match(EParser.BLOB)

            elif token in [EParser.UUID]:
                localctx = EParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1440
                self.match(EParser.UUID)

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
        self.enterRule(localctx, 160, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1443
            localctx.t1 = self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def getRuleIndex(self):
            return EParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = EParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1446
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1445
                self.match(EParser.MUTABLE)


            self.state = 1448 
            self.category_type()
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
        self.enterRule(localctx, 164, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1450
            localctx.t1 = self.match(EParser.CODE)
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
        self.enterRule(localctx, 166, self.RULE_category_declaration)
        try:
            self.state = 1455
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1452 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1453 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1454 
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



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 168
        self.enterRecursionRule(localctx, 168, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1458 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.TypeIdentifierListItemContext(self, EParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1460
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1461
                    self.match(EParser.COMMA)
                    self.state = 1462 
                    localctx.item = self.type_identifier() 
                self.state = 1467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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
        self.enterRule(localctx, 170, self.RULE_method_identifier)
        try:
            self.state = 1470
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1468 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1469 
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



    def identifier(self):

        localctx = EParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_identifier)
        try:
            self.state = 1475
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1472 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1473 
                localctx.name = self.type_identifier()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1474 
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
        self.enterRule(localctx, 174, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1477
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
        self.enterRule(localctx, 176, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
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
        self.enterRule(localctx, 178, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1481
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
        _startState = 180
        self.enterRecursionRule(localctx, 180, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1484 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentListItemContext(self, EParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1486
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1487
                    self.match(EParser.COMMA)
                    self.state = 1488 
                    localctx.item = self.argument() 
                self.state = 1493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

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

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

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
        self.enterRule(localctx, 182, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1499
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1494 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1496
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1495
                    self.match(EParser.MUTABLE)


                self.state = 1498 
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



    def operator_argument(self):

        localctx = EParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_operator_argument)
        try:
            self.state = 1503
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1501 
                localctx.arg = self.named_argument()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1502 
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
        self.enterRule(localctx, 186, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1505 
            localctx.name = self.variable_identifier()
            self.state = 1508
            la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
            if la_ == 1:
                self.state = 1506
                self.match(EParser.EQ)
                self.state = 1507 
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
        self.enterRule(localctx, 188, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1510 
            self.code_type()
            self.state = 1511 
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
        self.enterRule(localctx, 190, self.RULE_category_or_any_type)
        try:
            self.state = 1515
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1513 
                localctx.typ = self.typedef(0)

            elif token in [EParser.ANY]:
                localctx = EParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1514 
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
        _startState = 192
        self.enterRecursionRule(localctx, 192, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1518
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1528
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,104,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1526
                    la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1520
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1521
                        self.match(EParser.LBRAK)
                        self.state = 1522
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1523
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1524
                        self.match(EParser.LCURL)
                        self.state = 1525
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1530
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Member_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListItemContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Member_method_declaration_listContext)
            super(EParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryMethodListItem(self)


    class CategoryMethodListContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Member_method_declaration_listContext)
            super(EParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryMethodList(self)



    def member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 194
        self.enterRecursionRule(localctx, 194, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1532 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1540
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,105,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategoryMethodListItemContext(self, EParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1534
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1535 
                    self.lfp()
                    self.state = 1536 
                    localctx.item = self.member_method_declaration() 
                self.state = 1542
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,105,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(EParser.Operator_method_declarationContext,0)


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
        self.enterRule(localctx, 196, self.RULE_member_method_declaration)
        try:
            self.state = 1548
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1543 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1544 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1545 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1546 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1547 
                self.operator_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_member_method_declaration_listContext, self).copyFrom(ctx)


    class NativeCategoryMethodListContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_member_method_declaration_listContext)
            super(EParser.NativeCategoryMethodListContext, self).__init__(parser)
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryMethodList(self)


    class NativeCategoryMethodListItemContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_member_method_declaration_listContext)
            super(EParser.NativeCategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Native_member_method_declaration_listContext
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryMethodListItem(self)



    def native_member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 198
        self.enterRecursionRule(localctx, 198, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1551 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1559
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryMethodListItemContext(self, EParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1553
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1554 
                    self.lfp()
                    self.state = 1555 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1561
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,107,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = EParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_native_member_method_declaration)
        try:
            self.state = 1564
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1562 
                self.member_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1563 
                self.native_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(EParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(EParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(EParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = EParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_native_category_binding)
        try:
            self.state = 1576
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1566
                self.match(EParser.JAVA)
                self.state = 1567 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1568
                self.match(EParser.CSHARP)
                self.state = 1569 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1570
                self.match(EParser.PYTHON2)
                self.state = 1571 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1572
                self.match(EParser.PYTHON3)
                self.state = 1573 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1574
                self.match(EParser.JAVASCRIPT)
                self.state = 1575 
                localctx.binding = self.javascript_category_binding()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_category_binding

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = EParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1578 
            localctx.id_ = self.identifier()
            self.state = 1580
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 1579 
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
        self.enterRule(localctx, 206, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1582
            self.match(EParser.FROM)
            self.state = 1583 
            self.module_token()
            self.state = 1584
            self.match(EParser.COLON)
            self.state = 1585 
            self.identifier()
            self.state = 1590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1586
                    self.match(EParser.DOT)
                    self.state = 1587 
                    self.identifier() 
                self.state = 1592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

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
        self.enterRule(localctx, 208, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1593
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1594
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

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = EParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1596 
            localctx.id_ = self.identifier()
            self.state = 1598
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.state = 1597 
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

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Javascript_identifierContext,i)


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
        self.enterRule(localctx, 212, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1600
            self.match(EParser.FROM)
            self.state = 1601 
            self.module_token()
            self.state = 1602
            self.match(EParser.COLON)
            self.state = 1604
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1603
                self.match(EParser.SLASH)


            self.state = 1606 
            self.javascript_identifier()
            self.state = 1611
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1607
                    self.match(EParser.SLASH)
                    self.state = 1608 
                    self.javascript_identifier() 
                self.state = 1613
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

            self.state = 1616
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                self.state = 1614
                self.match(EParser.DOT)
                self.state = 1615 
                self.javascript_identifier()


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
        _startState = 214
        self.enterRecursionRule(localctx, 214, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1619 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1626
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.VariableListItemContext(self, EParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1621
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1622
                    self.match(EParser.COMMA)
                    self.state = 1623 
                    localctx.item = self.variable_identifier() 
                self.state = 1628
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

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


    class TestMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.TestMethodContext, self).__init__(parser)
            self.decl = None # Test_method_declarationContext
            self.copyFrom(ctx)

        def test_method_declaration(self):
            return self.getTypedRuleContext(EParser.Test_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTestMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTestMethod(self)



    def method_declaration(self):

        localctx = EParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_method_declaration)
        try:
            self.state = 1633
            la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
            if la_ == 1:
                localctx = EParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1629 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1630 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1631 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1632 
                localctx.decl = self.test_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comment_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(EParser.COMMENT, 0)

        def getRuleIndex(self):
            return EParser.RULE_comment_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = EParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1635
            self.match(EParser.COMMENT)
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



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 220
        self.enterRecursionRule(localctx, 220, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1638 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1646
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeStatementListItemContext(self, EParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1640
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1641 
                    self.lfp()
                    self.state = 1642 
                    localctx.item = self.native_statement() 
                self.state = 1648
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

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
        self.enterRule(localctx, 222, self.RULE_native_statement)
        try:
            self.state = 1659
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1649
                self.match(EParser.JAVA)
                self.state = 1650 
                localctx.stmt = self.java_statement()

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1651
                self.match(EParser.CSHARP)
                self.state = 1652 
                localctx.stmt = self.csharp_statement()

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1653
                self.match(EParser.PYTHON2)
                self.state = 1654 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1655
                self.match(EParser.PYTHON3)
                self.state = 1656 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1657
                self.match(EParser.JAVASCRIPT)
                self.state = 1658 
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
        self.enterRule(localctx, 224, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1661 
            localctx.stmt = self.python_statement()
            self.state = 1663
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.state = 1662
                self.match(EParser.SEMI)


            self.state = 1666
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                self.state = 1665 
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
        self.enterRule(localctx, 226, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1668 
            localctx.stmt = self.javascript_statement()
            self.state = 1670
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.state = 1669
                self.match(EParser.SEMI)


            self.state = 1673
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.state = 1672 
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



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1676 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1684
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,124,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.StatementListItemContext(self, EParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1678
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1679 
                    self.lfp()
                    self.state = 1680 
                    localctx.item = self.statement() 
                self.state = 1686
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,124,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_assertion_list

     
        def copyFrom(self, ctx):
            super(EParser.Assertion_listContext, self).copyFrom(ctx)


    class AssertionListContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Assertion_listContext)
            super(EParser.AssertionListContext, self).__init__(parser)
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def assertion(self):
            return self.getTypedRuleContext(EParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertionList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertionList(self)


    class AssertionListItemContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Assertion_listContext)
            super(EParser.AssertionListItemContext, self).__init__(parser)
            self.items = None # Assertion_listContext
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def assertion_list(self):
            return self.getTypedRuleContext(EParser.Assertion_listContext,0)

        def assertion(self):
            return self.getTypedRuleContext(EParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertionListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertionListItem(self)



    def assertion_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assertion_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 230
        self.enterRecursionRule(localctx, 230, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1688 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1696
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.AssertionListItemContext(self, EParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1690
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1691 
                    self.lfp()
                    self.state = 1692 
                    localctx.item = self.assertion() 
                self.state = 1698
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

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



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 232
        self.enterRecursionRule(localctx, 232, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1700 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1708
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SwitchCaseStatementListItemContext(self, EParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1702
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1703 
                    self.lfp()
                    self.state = 1704 
                    localctx.item = self.switch_case_statement() 
                self.state = 1710
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

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
        _startState = 234
        self.enterRecursionRule(localctx, 234, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1712 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1720
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CatchStatementListItemContext(self, EParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1714
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1715 
                    self.lfp()
                    self.state = 1716 
                    localctx.item = self.catch_statement() 
                self.state = 1722
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

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



    def literal_collection(self):

        localctx = EParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_literal_collection)
        try:
            self.state = 1737
            la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1723
                self.match(EParser.LBRAK)
                self.state = 1724 
                localctx.low = self.atomic_literal()
                self.state = 1725
                self.match(EParser.RANGE)
                self.state = 1726 
                localctx.high = self.atomic_literal()
                self.state = 1727
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1729
                self.match(EParser.LBRAK)
                self.state = 1730 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1731
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1733
                self.match(EParser.LT)
                self.state = 1734 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1735
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



    def atomic_literal(self):

        localctx = EParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_atomic_literal)
        try:
            self.state = 1752
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1739
                localctx.t = self.match(EParser.MIN_INTEGER)

            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1740
                localctx.t = self.match(EParser.MAX_INTEGER)

            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1741
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1742
                localctx.t = self.match(EParser.HEXA_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1743
                localctx.t = self.match(EParser.CHAR_LITERAL)

            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1744
                localctx.t = self.match(EParser.DATE_LITERAL)

            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1745
                localctx.t = self.match(EParser.TIME_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1746
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1747
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1748
                localctx.t = self.match(EParser.DATETIME_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1749
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1750
                localctx.t = self.match(EParser.PERIOD_LITERAL)

            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1751 
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
        _startState = 240
        self.enterRecursionRule(localctx, 240, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1755 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1762
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.LiteralListItemContext(self, EParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1757
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1758
                    self.match(EParser.COMMA)
                    self.state = 1759 
                    localctx.item = self.atomic_literal() 
                self.state = 1764
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

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



    def selectable_expression(self):

        localctx = EParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_selectable_expression)
        try:
            self.state = 1769
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1765 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1766 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1767 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1768 
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
        self.enterRule(localctx, 244, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1771
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
        self.enterRule(localctx, 246, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1773
            self.match(EParser.LPAR)
            self.state = 1774 
            localctx.exp = self.expression(0)
            self.state = 1775
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
        self.enterRule(localctx, 248, self.RULE_literal_expression)
        try:
            self.state = 1779
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                localctx = EParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1777 
                localctx.exp = self.atomic_literal()

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT]:
                localctx = EParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1778 
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



    def collection_literal(self):

        localctx = EParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_collection_literal)
        try:
            self.state = 1786
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                localctx = EParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1781 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = EParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1782 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = EParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1783 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = EParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1784 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = EParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1785 
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
        self.enterRule(localctx, 252, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1788
            self.match(EParser.LPAR)
            self.state = 1790
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (EParser.EXECUTE - 94)) | (1 << (EParser.FETCH - 94)) | (1 << (EParser.INVOKE - 94)) | (1 << (EParser.MUTABLE - 94)) | (1 << (EParser.NOT - 94)) | (1 << (EParser.NOTHING - 94)) | (1 << (EParser.READ - 94)) | (1 << (EParser.SELF - 94)) | (1 << (EParser.SORTED - 94)) | (1 << (EParser.THIS - 94)) | (1 << (EParser.BOOLEAN_LITERAL - 94)) | (1 << (EParser.CHAR_LITERAL - 94)) | (1 << (EParser.MIN_INTEGER - 94)) | (1 << (EParser.MAX_INTEGER - 94)) | (1 << (EParser.SYMBOL_IDENTIFIER - 94)) | (1 << (EParser.TYPE_IDENTIFIER - 94)) | (1 << (EParser.VARIABLE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (EParser.TEXT_LITERAL - 158)) | (1 << (EParser.INTEGER_LITERAL - 158)) | (1 << (EParser.HEXA_LITERAL - 158)) | (1 << (EParser.DECIMAL_LITERAL - 158)) | (1 << (EParser.DATETIME_LITERAL - 158)) | (1 << (EParser.TIME_LITERAL - 158)) | (1 << (EParser.DATE_LITERAL - 158)) | (1 << (EParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1789 
                localctx.items = self.expression_tuple(0)


            self.state = 1792
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
        self.enterRule(localctx, 254, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1794
            self.match(EParser.LCURL)
            self.state = 1796
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (EParser.EXECUTE - 94)) | (1 << (EParser.FETCH - 94)) | (1 << (EParser.INVOKE - 94)) | (1 << (EParser.MUTABLE - 94)) | (1 << (EParser.NOT - 94)) | (1 << (EParser.NOTHING - 94)) | (1 << (EParser.READ - 94)) | (1 << (EParser.SELF - 94)) | (1 << (EParser.SORTED - 94)) | (1 << (EParser.THIS - 94)) | (1 << (EParser.BOOLEAN_LITERAL - 94)) | (1 << (EParser.CHAR_LITERAL - 94)) | (1 << (EParser.MIN_INTEGER - 94)) | (1 << (EParser.MAX_INTEGER - 94)) | (1 << (EParser.SYMBOL_IDENTIFIER - 94)) | (1 << (EParser.TYPE_IDENTIFIER - 94)) | (1 << (EParser.VARIABLE_IDENTIFIER - 94)))) != 0) or ((((_la - 158)) & ~0x3f) == 0 and ((1 << (_la - 158)) & ((1 << (EParser.TEXT_LITERAL - 158)) | (1 << (EParser.INTEGER_LITERAL - 158)) | (1 << (EParser.HEXA_LITERAL - 158)) | (1 << (EParser.DECIMAL_LITERAL - 158)) | (1 << (EParser.DATETIME_LITERAL - 158)) | (1 << (EParser.TIME_LITERAL - 158)) | (1 << (EParser.DATE_LITERAL - 158)) | (1 << (EParser.PERIOD_LITERAL - 158)))) != 0):
                self.state = 1795 
                localctx.items = self.dict_entry_list(0)


            self.state = 1798
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



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 256
        self.enterRecursionRule(localctx, 256, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1801 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1808
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,136,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueTupleItemContext(self, EParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1803
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1804
                    self.match(EParser.COMMA)
                    self.state = 1805 
                    localctx.item = self.expression(0) 
                self.state = 1810
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,136,self._ctx)

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
        _startState = 258
        self.enterRecursionRule(localctx, 258, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1812 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1819
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DictEntryListItemContext(self, EParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1814
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1815
                    self.match(EParser.COMMA)
                    self.state = 1816 
                    localctx.item = self.dict_entry() 
                self.state = 1821
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

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
        self.enterRule(localctx, 260, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1822 
            localctx.key = self.expression(0)
            self.state = 1823
            self.match(EParser.COLON)
            self.state = 1824 
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



    def slice_arguments(self):

        localctx = EParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_slice_arguments)
        try:
            self.state = 1835
            la_ = self._interp.adaptivePredict(self._input,138,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1826 
                localctx.first = self.expression(0)
                self.state = 1827
                self.match(EParser.COLON)
                self.state = 1828 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1830 
                localctx.first = self.expression(0)
                self.state = 1831
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1833
                self.match(EParser.COLON)
                self.state = 1834 
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
        self.enterRule(localctx, 264, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1837 
            localctx.name = self.variable_identifier()
            self.state = 1838 
            self.assign()
            self.state = 1839 
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



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 266
        self.enterRecursionRule(localctx, 266, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1842 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1848
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1844
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1845 
                    localctx.child = self.child_instance() 
                self.state = 1850
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

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
        self.enterRule(localctx, 268, self.RULE_is_expression)
        try:
            self.state = 1855
            la_ = self._interp.adaptivePredict(self._input,140,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1851
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1852
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1853 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1854 
                localctx.exp = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_by_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Order_byContext)
            else:
                return self.getTypedRuleContext(EParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_order_by_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = EParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1857 
            self.order_by()
            self.state = 1862
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1858
                    self.match(EParser.COMMA)
                    self.state = 1859 
                    self.order_by() 
                self.state = 1864
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,141,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(EParser.DOT)
            else:
                return self.getToken(EParser.DOT, i)

        def ASC(self):
            return self.getToken(EParser.ASC, 0)

        def DESC(self):
            return self.getToken(EParser.DESC, 0)

        def getRuleIndex(self):
            return EParser.RULE_order_by

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = EParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1865 
            self.variable_identifier()
            self.state = 1870
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,142,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1866
                    self.match(EParser.DOT)
                    self.state = 1867 
                    self.variable_identifier() 
                self.state = 1872
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,142,self._ctx)

            self.state = 1874
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                self.state = 1873
                _la = self._input.LA(1)
                if not(_la==EParser.ASC or _la==EParser.DESC):
                    self._errHandler.recoverInline(self)
                self.consume()


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



    def operator(self):

        localctx = EParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_operator)
        try:
            self.state = 1882
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1876
                self.match(EParser.PLUS)

            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1877
                self.match(EParser.MINUS)

            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1878 
                self.multiply()

            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1879 
                self.divide()

            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1880 
                self.idivide()

            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1881 
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

    class New_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = EParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1885
            if not self.isText(localctx.i1,"new"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"new\")")
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
        self.enterRule(localctx, 278, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1887
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1888
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
        self.enterRule(localctx, 280, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1890
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1891
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
        self.enterRule(localctx, 282, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1893
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1894
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
        self.enterRule(localctx, 284, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1896
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
        self.enterRule(localctx, 286, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1898
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
        self.enterRule(localctx, 288, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1900
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
        self.enterRule(localctx, 290, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1902
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
        self.enterRule(localctx, 292, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1904
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



    def javascript_statement(self):

        localctx = EParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_javascript_statement)
        try:
            self.state = 1913
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1906
                self.match(EParser.RETURN)
                self.state = 1907 
                localctx.exp = self.javascript_expression(0)
                self.state = 1908
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1910 
                localctx.exp = self.javascript_expression(0)
                self.state = 1911
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



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 296
        self.enterRecursionRule(localctx, 296, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1916 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1922
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1918
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1919 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1924
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

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

        def javascript_this_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = EParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_javascript_primary_expression)
        try:
            self.state = 1932
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1925 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1926 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1927 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1928 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1929 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1930 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1931 
                self.javascript_item_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = EParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1934 
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = EParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1936 
            self.new_token()
            self.state = 1937 
            self.javascript_method_expression()
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



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = EParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_javascript_selector_expression)
        try:
            self.state = 1944
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                localctx = EParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1939
                self.match(EParser.DOT)
                self.state = 1940 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = EParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1941
                self.match(EParser.DOT)
                self.state = 1942 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = EParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1943 
                localctx.exp = self.javascript_item_expression()
                pass


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
        self.enterRule(localctx, 306, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946 
            localctx.name = self.javascript_identifier()
            self.state = 1947
            self.match(EParser.LPAR)
            self.state = 1949
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.SELF - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.THIS - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.BOOLEAN_LITERAL - 125)) | (1 << (EParser.CHAR_LITERAL - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)) | (1 << (EParser.DOLLAR_IDENTIFIER - 125)) | (1 << (EParser.TEXT_LITERAL - 125)) | (1 << (EParser.INTEGER_LITERAL - 125)) | (1 << (EParser.DECIMAL_LITERAL - 125)))) != 0):
                self.state = 1948 
                localctx.args = self.javascript_arguments(0)


            self.state = 1951
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



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 308
        self.enterRecursionRule(localctx, 308, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1954 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1961
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1956
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1957
                    self.match(EParser.COMMA)
                    self.state = 1958 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1963
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

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
        self.enterRule(localctx, 310, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1964
            self.match(EParser.LBRAK)
            self.state = 1965 
            localctx.exp = self.javascript_expression(0)
            self.state = 1966
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
        self.enterRule(localctx, 312, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1968
            self.match(EParser.LPAR)
            self.state = 1969 
            localctx.exp = self.javascript_expression(0)
            self.state = 1970
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
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = EParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1972 
            localctx.name = self.javascript_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



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



    def javascript_literal_expression(self):

        localctx = EParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_literal_expression)
        try:
            self.state = 1979
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1974
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1975
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1976
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1977
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1978
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

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

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

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

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
        self.enterRule(localctx, 318, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1981
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)) | (1 << (EParser.DOLLAR_IDENTIFIER - 125)))) != 0)):
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



    def python_statement(self):

        localctx = EParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_python_statement)
        try:
            self.state = 1986
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1983
                self.match(EParser.RETURN)
                self.state = 1984 
                localctx.exp = self.python_expression(0)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1985 
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



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1989 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1995
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,153,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1991
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1992 
                    localctx.child = self.python_selector_expression() 
                self.state = 1997
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

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



    def python_primary_expression(self):

        localctx = EParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_python_primary_expression)
        try:
            self.state = 2002
            la_ = self._interp.adaptivePredict(self._input,154,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1998 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1999 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2000 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2001 
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



    def python_selector_expression(self):

        localctx = EParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_python_selector_expression)
        try:
            self.state = 2010
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2004
                self.match(EParser.DOT)
                self.state = 2005 
                localctx.exp = self.python_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2006
                self.match(EParser.LBRAK)
                self.state = 2007 
                localctx.exp = self.python_expression(0)
                self.state = 2008
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
        self.enterRule(localctx, 328, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2012 
            localctx.name = self.python_identifier()
            self.state = 2013
            self.match(EParser.LPAR)
            self.state = 2015
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.SELF - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.THIS - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.BOOLEAN_LITERAL - 125)) | (1 << (EParser.CHAR_LITERAL - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)) | (1 << (EParser.DOLLAR_IDENTIFIER - 125)) | (1 << (EParser.TEXT_LITERAL - 125)) | (1 << (EParser.INTEGER_LITERAL - 125)) | (1 << (EParser.DECIMAL_LITERAL - 125)))) != 0):
                self.state = 2014 
                localctx.args = self.python_argument_list()


            self.state = 2017
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



    def python_argument_list(self):

        localctx = EParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_python_argument_list)
        try:
            self.state = 2025
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2019 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2020 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2021 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2022
                self.match(EParser.COMMA)
                self.state = 2023 
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



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 332
        self.enterRecursionRule(localctx, 332, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2028 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2035
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2030
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2031
                    self.match(EParser.COMMA)
                    self.state = 2032 
                    localctx.item = self.python_expression(0) 
                self.state = 2037
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

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



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2039 
            localctx.name = self.python_identifier()
            self.state = 2040
            self.match(EParser.EQ)
            self.state = 2041 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2051
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,159,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2043
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2044
                    self.match(EParser.COMMA)
                    self.state = 2045 
                    localctx.name = self.python_identifier()
                    self.state = 2046
                    self.match(EParser.EQ)
                    self.state = 2047 
                    localctx.exp = self.python_expression(0) 
                self.state = 2053
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,159,self._ctx)

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
        self.enterRule(localctx, 336, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2054
            self.match(EParser.LPAR)
            self.state = 2055 
            localctx.exp = self.python_expression(0)
            self.state = 2056
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


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPromptoIdentifier(self)


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
        _startState = 338
        self.enterRecursionRule(localctx, 338, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2061
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2059
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2060 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2068
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2063
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2064
                    self.match(EParser.DOT)
                    self.state = 2065 
                    localctx.name = self.python_identifier() 
                self.state = 2070
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

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



    def python_literal_expression(self):

        localctx = EParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_python_literal_expression)
        try:
            self.state = 2076
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2071
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2072
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2073
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2074
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2075
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

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

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
        self.enterRule(localctx, 342, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2078
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.SELF - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.THIS - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)))) != 0)):
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



    def java_statement(self):

        localctx = EParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_java_statement)
        try:
            self.state = 2087
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2080
                self.match(EParser.RETURN)
                self.state = 2081 
                localctx.exp = self.java_expression(0)
                self.state = 2082
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2084 
                localctx.exp = self.java_expression(0)
                self.state = 2085
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



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 346
        self.enterRecursionRule(localctx, 346, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2090 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2096
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,164,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2092
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2093 
                    localctx.child = self.java_selector_expression() 
                self.state = 2098
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,164,self._ctx)

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

        def java_this_expression(self):
            return self.getTypedRuleContext(EParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(EParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(EParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = EParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_java_primary_expression)
        try:
            self.state = 2104
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2099 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2100 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2101 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2102 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2103 
                self.java_literal_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = EParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2106 
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(EParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = EParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2108 
            self.new_token()
            self.state = 2109 
            self.java_method_expression()
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
        self.enterRule(localctx, 354, self.RULE_java_selector_expression)
        try:
            self.state = 2114
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2111
                self.match(EParser.DOT)
                self.state = 2112 
                localctx.exp = self.java_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2113 
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
        self.enterRule(localctx, 356, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2116 
            localctx.name = self.java_identifier()
            self.state = 2117
            self.match(EParser.LPAR)
            self.state = 2119
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.SELF - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.THIS - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.BOOLEAN_LITERAL - 125)) | (1 << (EParser.CHAR_LITERAL - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)) | (1 << (EParser.NATIVE_IDENTIFIER - 125)) | (1 << (EParser.DOLLAR_IDENTIFIER - 125)) | (1 << (EParser.TEXT_LITERAL - 125)) | (1 << (EParser.INTEGER_LITERAL - 125)) | (1 << (EParser.DECIMAL_LITERAL - 125)))) != 0):
                self.state = 2118 
                localctx.args = self.java_arguments(0)


            self.state = 2121
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



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2124 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,168,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2126
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2127
                    self.match(EParser.COMMA)
                    self.state = 2128 
                    localctx.item = self.java_expression(0) 
                self.state = 2133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

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
        self.enterRule(localctx, 360, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2134
            self.match(EParser.LBRAK)
            self.state = 2135 
            localctx.exp = self.java_expression(0)
            self.state = 2136
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
        self.enterRule(localctx, 362, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2138
            self.match(EParser.LPAR)
            self.state = 2139 
            localctx.exp = self.java_expression(0)
            self.state = 2140
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
        _startState = 364
        self.enterRecursionRule(localctx, 364, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2143 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,169,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2145
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2146
                    self.match(EParser.DOT)
                    self.state = 2147 
                    localctx.name = self.java_identifier() 
                self.state = 2152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,169,self._ctx)

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


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 366
        self.enterRecursionRule(localctx, 366, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2154 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,170,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2156
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2157
                    localctx.name = self.match(EParser.DOLLAR_IDENTIFIER) 
                self.state = 2162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,170,self._ctx)

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



    def java_literal_expression(self):

        localctx = EParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_literal_expression)
        try:
            self.state = 2168
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2163
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2164
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2165
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2166
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2167
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

        def NATIVE_IDENTIFIER(self):
            return self.getToken(EParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

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

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

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
        self.enterRule(localctx, 370, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)) | (1 << (EParser.NATIVE_IDENTIFIER - 125)) | (1 << (EParser.DOLLAR_IDENTIFIER - 125)))) != 0)):
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



    def csharp_statement(self):

        localctx = EParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_csharp_statement)
        try:
            self.state = 2179
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2172
                self.match(EParser.RETURN)
                self.state = 2173 
                localctx.exp = self.csharp_expression(0)
                self.state = 2174
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2176 
                localctx.exp = self.csharp_expression(0)
                self.state = 2177
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



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 374
        self.enterRecursionRule(localctx, 374, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2182 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,173,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2184
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2185 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,173,self._ctx)

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

        def csharp_this_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = EParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_csharp_primary_expression)
        try:
            self.state = 2196
            la_ = self._interp.adaptivePredict(self._input,174,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2191 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2192 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2193 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2194 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2195 
                self.csharp_literal_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = EParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2198 
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = EParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2200 
            self.new_token()
            self.state = 2201 
            self.csharp_method_expression()
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



    def csharp_selector_expression(self):

        localctx = EParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_csharp_selector_expression)
        try:
            self.state = 2206
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2203
                self.match(EParser.DOT)
                self.state = 2204 
                localctx.exp = self.csharp_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2205 
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
        self.enterRule(localctx, 384, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2208 
            localctx.name = self.csharp_identifier()
            self.state = 2209
            self.match(EParser.LPAR)
            self.state = 2211
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.SELF - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.THIS - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.BOOLEAN_LITERAL - 125)) | (1 << (EParser.CHAR_LITERAL - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)) | (1 << (EParser.DOLLAR_IDENTIFIER - 125)) | (1 << (EParser.TEXT_LITERAL - 125)) | (1 << (EParser.INTEGER_LITERAL - 125)) | (1 << (EParser.DECIMAL_LITERAL - 125)))) != 0):
                self.state = 2210 
                localctx.args = self.csharp_arguments(0)


            self.state = 2213
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
        _startState = 386
        self.enterRecursionRule(localctx, 386, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2216 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2218
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2219
                    self.match(EParser.COMMA)
                    self.state = 2220 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

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
        self.enterRule(localctx, 388, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2226
            self.match(EParser.LBRAK)
            self.state = 2227 
            localctx.exp = self.csharp_expression(0)
            self.state = 2228
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
        self.enterRule(localctx, 390, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2230
            self.match(EParser.LPAR)
            self.state = 2231 
            localctx.exp = self.csharp_expression(0)
            self.state = 2232
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


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 392
        self.enterRecursionRule(localctx, 392, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2237
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2235
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2236 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,179,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2239
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2240
                    self.match(EParser.DOT)
                    self.state = 2241 
                    localctx.name = self.csharp_identifier() 
                self.state = 2246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,179,self._ctx)

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
        self.enterRule(localctx, 394, self.RULE_csharp_literal_expression)
        try:
            self.state = 2252
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2247
                self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2248
                self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2249
                self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2250
                self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2251
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

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

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
        self.enterRule(localctx, 396, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (EParser.READ - 125)) | (1 << (EParser.TEST - 125)) | (1 << (EParser.WRITE - 125)) | (1 << (EParser.SYMBOL_IDENTIFIER - 125)) | (1 << (EParser.TYPE_IDENTIFIER - 125)) | (1 << (EParser.VARIABLE_IDENTIFIER - 125)))) != 0)):
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
        self._predicates[14] = self.native_category_binding_list_sempred
        self._predicates[34] = self.else_if_statement_list_sempred
        self._predicates[39] = self.expression_sempred
        self._predicates[40] = self.unresolved_expression_sempred
        self._predicates[41] = self.unresolved_selector_sempred
        self._predicates[43] = self.invocation_trailer_sempred
        self._predicates[44] = self.instance_expression_sempred
        self._predicates[45] = self.instance_selector_sempred
        self._predicates[53] = self.argument_assignment_list_sempred
        self._predicates[54] = self.with_argument_assignment_list_sempred
        self._predicates[57] = self.child_instance_sempred
        self._predicates[65] = self.declarations_sempred
        self._predicates[69] = self.native_symbol_list_sempred
        self._predicates[70] = self.category_symbol_list_sempred
        self._predicates[71] = self.symbol_list_sempred
        self._predicates[75] = self.expression_list_sempred
        self._predicates[77] = self.typedef_sempred
        self._predicates[84] = self.type_identifier_list_sempred
        self._predicates[90] = self.argument_list_sempred
        self._predicates[96] = self.any_type_sempred
        self._predicates[97] = self.member_method_declaration_list_sempred
        self._predicates[99] = self.native_member_method_declaration_list_sempred
        self._predicates[104] = self.module_token_sempred
        self._predicates[107] = self.variable_identifier_list_sempred
        self._predicates[110] = self.native_statement_list_sempred
        self._predicates[114] = self.statement_list_sempred
        self._predicates[115] = self.assertion_list_sempred
        self._predicates[116] = self.switch_case_statement_list_sempred
        self._predicates[117] = self.catch_statement_list_sempred
        self._predicates[120] = self.literal_list_literal_sempred
        self._predicates[128] = self.expression_tuple_sempred
        self._predicates[129] = self.dict_entry_list_sempred
        self._predicates[133] = self.assignable_instance_sempred
        self._predicates[134] = self.is_expression_sempred
        self._predicates[138] = self.new_token_sempred
        self._predicates[139] = self.key_token_sempred
        self._predicates[140] = self.value_token_sempred
        self._predicates[141] = self.symbols_token_sempred
        self._predicates[148] = self.javascript_expression_sempred
        self._predicates[154] = self.javascript_arguments_sempred
        self._predicates[161] = self.python_expression_sempred
        self._predicates[166] = self.python_ordinal_argument_list_sempred
        self._predicates[167] = self.python_named_argument_list_sempred
        self._predicates[169] = self.python_identifier_expression_sempred
        self._predicates[173] = self.java_expression_sempred
        self._predicates[179] = self.java_arguments_sempred
        self._predicates[182] = self.java_identifier_expression_sempred
        self._predicates[183] = self.java_class_identifier_expression_sempred
        self._predicates[187] = self.csharp_expression_sempred
        self._predicates[193] = self.csharp_arguments_sempred
        self._predicates[196] = self.csharp_identifier_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 37)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 20)
         

    def unresolved_expression_sempred(self, localctx, predIndex):
            if predIndex == 29:
                return self.precpred(self._ctx, 1)
         

    def unresolved_selector_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.wasNot(EParser.WS)
         

    def invocation_trailer_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.willBe(EParser.LF)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.wasNot(EParser.WS)
         

            if predIndex == 34:
                return self.wasNot(EParser.WS)
         

            if predIndex == 35:
                return self.wasNot(EParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.was(EParser.WS)
         

    def with_argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.wasNot(EParser.WS)
         

            if predIndex == 39:
                return self.wasNot(EParser.WS)
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 46:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def assertion_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 78:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 79:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 80:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 81:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 82:
                return self.precpred(self._ctx, 1)
         



