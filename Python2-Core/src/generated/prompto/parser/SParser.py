# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .SParserListener import SParserListener
else:
    from SParserListener import SParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00a0\u0825\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0187\n\2\3\2\5\2\u018a")
        buf.write(u"\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u01a3")
        buf.write(u"\n\5\3\5\3\5\3\6\5\6\u01a8\n\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\5\6\u01b3\n\6\3\6\3\6\3\7\5\7\u01b8\n")
        buf.write(u"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01c3\n\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\5\7\u01ca\n\7\3\7\3\7\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01d7\n\b\3\b\3\b\3\t")
        buf.write(u"\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u01e5\n\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\r\5\r\u0201\n\r\3\r\3\r\3\r\3\r\3\r\5\r\u0208\n")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0211\n\r\3\r\3\r")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\5\16\u021a\n\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\5\16\u0223\n\16\3\16\3\16\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\7\20\u0236\n\20\f\20\16\20\u0239\13")
        buf.write(u"\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u0242\n\22")
        buf.write(u"\3\22\3\22\3\22\5\22\u0247\n\22\3\23\3\23\3\23\3\23\5")
        buf.write(u"\23\u024d\n\23\3\23\3\23\3\23\5\23\u0252\n\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u025e")
        buf.write(u"\n\24\3\24\3\24\3\24\5\24\u0263\n\24\3\24\3\24\3\24\3")
        buf.write(u"\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u027b\n")
        buf.write(u"\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write(u"\u0286\n\27\3\27\3\27\5\27\u028a\n\27\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\3\30\5\30\u029d\n\30\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\32\3\32\3\32\5\32\u02a7\n\32\3\32\3\32\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\5\33\u02b0\n\33\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\7\34\u02b7\n\34\f\34\16\34\u02ba\13\34\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\5\35\u02c2\n\35\3\36\3\36\3\36\3")
        buf.write(u"\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u02df\n \3")
        buf.write(u" \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!")
        buf.write(u"\u02f2\n!\3\"\3\"\3\"\3\"\5\"\u02f8\n\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write(u"$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u031a\n%\3%")
        buf.write(u"\3%\3%\3%\3%\3%\3%\5%\u0323\n%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write(u"&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u0338\n&\f&\16")
        buf.write(u"&\u033b\13&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0348")
        buf.write(u"\n(\3(\3(\3(\3(\3(\3(\3(\5(\u0351\n(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\5(\u035a\n(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0371\n)\3*\3*\5*\u0375")
        buf.write(u"\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\5+\u0389\n+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\7+\u03e9\n+\f+\16")
        buf.write(u"+\u03ec\13+\3,\3,\3-\3-\3-\3-\3-\7-\u03f5\n-\f-\16-\u03f8")
        buf.write(u"\13-\3.\3.\3.\3.\3.\3.\5.\u0400\n.\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\5/\u040f\n/\3\60\3\60\3\61\5\61")
        buf.write(u"\u0414\n\61\3\61\3\61\3\61\5\61\u0419\n\61\3\61\3\61")
        buf.write(u"\3\62\3\62\3\62\3\62\3\62\5\62\u0422\n\62\3\62\3\62\3")
        buf.write(u"\62\7\62\u0427\n\62\f\62\16\62\u042a\13\62\3\63\3\63")
        buf.write(u"\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3")
        buf.write(u"\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write(u"\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5")
        buf.write(u"\66\u044d\n\66\3\66\3\66\3\66\3\66\3\66\5\66\u0454\n")
        buf.write(u"\66\5\66\u0456\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\5\67\u0460\n\67\3\67\3\67\38\38\38\38\39\39\39")
        buf.write(u"\39\39\39\39\39\59\u0470\n9\3:\3:\3:\3:\3;\7;\u0477\n")
        buf.write(u";\f;\16;\u047a\13;\3<\6<\u047d\n<\r<\16<\u047e\3=\6=")
        buf.write(u"\u0482\n=\r=\16=\u0483\3=\3=\3>\7>\u0489\n>\f>\16>\u048c")
        buf.write(u"\13>\3>\3>\3?\3?\3@\5@\u0493\n@\3@\3@\3@\3A\3A\3A\3A")
        buf.write(u"\3A\3A\3A\7A\u049f\nA\fA\16A\u04a2\13A\3B\3B\3B\3B\3")
        buf.write(u"B\5B\u04a9\nB\3C\3C\3D\3D\5D\u04af\nD\3E\3E\3E\3E\3E")
        buf.write(u"\3E\3E\7E\u04b8\nE\fE\16E\u04bb\13E\3F\3F\3F\3F\3F\3")
        buf.write(u"F\3F\7F\u04c4\nF\fF\16F\u04c7\13F\3G\3G\3G\3G\3G\3G\7")
        buf.write(u"G\u04cf\nG\fG\16G\u04d2\13G\3H\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write(u"H\3H\5H\u04de\nH\3I\3I\5I\u04e2\nI\3I\3I\3J\3J\5J\u04e8")
        buf.write(u"\nJ\3J\3J\3K\3K\3K\3K\3K\3K\7K\u04f2\nK\fK\16K\u04f5")
        buf.write(u"\13K\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M")
        buf.write(u"\3M\7M\u0508\nM\fM\16M\u050b\13M\3N\3N\5N\u050f\nN\3")
        buf.write(u"O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u051b\nO\3P\3P\3Q\3Q")
        buf.write(u"\3R\3R\3S\3S\3S\5S\u0526\nS\3T\3T\3T\3T\3T\3T\7T\u052e")
        buf.write(u"\nT\fT\16T\u0531\13T\3U\3U\5U\u0535\nU\3V\3V\3V\5V\u053a")
        buf.write(u"\nV\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\7Z\u0548\nZ\f")
        buf.write(u"Z\16Z\u054b\13Z\3[\3[\5[\u054f\n[\3[\5[\u0552\n[\3\\")
        buf.write(u"\3\\\5\\\u0556\n\\\3]\3]\3]\5]\u055b\n]\3^\3^\3^\3_\3")
        buf.write(u"_\5_\u0562\n_\3`\3`\3`\3`\3`\3`\3`\3`\3`\7`\u056d\n`")
        buf.write(u"\f`\16`\u0570\13`\3a\3a\3a\3a\3a\3a\3a\7a\u0579\na\f")
        buf.write(u"a\16a\u057c\13a\3b\3b\3b\3b\3b\5b\u0583\nb\3c\3c\3c\3")
        buf.write(u"c\3c\3c\3c\7c\u058c\nc\fc\16c\u058f\13c\3d\3d\5d\u0593")
        buf.write(u"\nd\3e\3e\3e\3e\3e\3e\3e\3e\3e\3e\5e\u059f\ne\3f\3f\5")
        buf.write(u"f\u05a3\nf\3g\3g\3g\3g\3g\3g\7g\u05ab\ng\fg\16g\u05ae")
        buf.write(u"\13g\3h\3h\3h\3i\3i\5i\u05b5\ni\3j\3j\3j\3j\5j\u05bb")
        buf.write(u"\nj\3j\3j\3j\7j\u05c0\nj\fj\16j\u05c3\13j\3j\3j\5j\u05c7")
        buf.write(u"\nj\3k\3k\3k\3k\3k\3k\7k\u05cf\nk\fk\16k\u05d2\13k\3")
        buf.write(u"l\3l\3l\3l\5l\u05d8\nl\3m\3m\3n\3n\3n\3n\3n\3n\3n\7n")
        buf.write(u"\u05e3\nn\fn\16n\u05e6\13n\3o\3o\3o\3o\3o\3o\3o\3o\3")
        buf.write(u"o\3o\5o\u05f2\no\3p\3p\5p\u05f6\np\3p\5p\u05f9\np\3q")
        buf.write(u"\3q\5q\u05fd\nq\3q\5q\u0600\nq\3r\3r\3r\3r\3r\3r\3r\7")
        buf.write(u"r\u0609\nr\fr\16r\u060c\13r\3s\3s\3s\3s\3s\3s\3s\7s\u0615")
        buf.write(u"\ns\fs\16s\u0618\13s\3t\3t\3t\3t\3t\3t\3t\7t\u0621\n")
        buf.write(u"t\ft\16t\u0624\13t\3u\3u\3u\3u\3u\3u\3u\7u\u062d\nu\f")
        buf.write(u"u\16u\u0630\13u\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write(u"v\3v\5v\u0640\nv\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w")
        buf.write(u"\3w\5w\u064f\nw\3x\3x\3x\3x\3x\3x\7x\u0657\nx\fx\16x")
        buf.write(u"\u065a\13x\3y\3y\3y\3y\5y\u0660\ny\3z\3z\3{\3{\3{\3{")
        buf.write(u"\3|\3|\5|\u066a\n|\3}\3}\3}\3}\3}\5}\u0671\n}\3~\3~\5")
        buf.write(u"~\u0675\n~\3~\3~\3\177\3\177\5\177\u067b\n\177\3\177")
        buf.write(u"\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080")
        buf.write(u"\7\u0080\u0685\n\u0080\f\u0080\16\u0080\u0688\13\u0080")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\7\u0081")
        buf.write(u"\u0690\n\u0081\f\u0081\16\u0081\u0693\13\u0081\3\u0082")
        buf.write(u"\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083\u06a2")
        buf.write(u"\n\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\7\u0085\u06ad\n\u0085\f\u0085")
        buf.write(u"\16\u0085\u06b0\13\u0085\3\u0086\3\u0086\3\u0086\3\u0086")
        buf.write(u"\5\u0086\u06b6\n\u0086\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0087\5\u0087\u06be\n\u0087\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0089\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008b\3\u008b\3\u008c\3\u008c\3\u008d\3\u008d\3\u008e")
        buf.write(u"\3\u008e\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write(u"\3\u0090\3\u0090\3\u0090\5\u0090\u06da\n\u0090\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0091\3\u0091\7\u0091\u06e1\n\u0091")
        buf.write(u"\f\u0091\16\u0091\u06e4\13\u0091\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\3\u0092\3\u0092\5\u0092\u06ec\n\u0092\3\u0093")
        buf.write(u"\3\u0093\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\5\u0094")
        buf.write(u"\u06f5\n\u0094\3\u0095\3\u0095\3\u0095\5\u0095\u06fa")
        buf.write(u"\n\u0095\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write(u"\3\u0096\3\u0096\7\u0096\u0704\n\u0096\f\u0096\16\u0096")
        buf.write(u"\u0707\13\u0096\3\u0097\3\u0097\3\u0097\3\u0097\3\u0098")
        buf.write(u"\3\u0098\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a")
        buf.write(u"\3\u009a\3\u009a\3\u009a\5\u009a\u0718\n\u009a\3\u009b")
        buf.write(u"\3\u009b\3\u009c\3\u009c\3\u009c\5\u009c\u071f\n\u009c")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d\7\u009d\u0726")
        buf.write(u"\n\u009d\f\u009d\16\u009d\u0729\13\u009d\3\u009e\3\u009e")
        buf.write(u"\3\u009e\3\u009e\5\u009e\u072f\n\u009e\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u009f\3\u009f\5\u009f\u0737\n\u009f")
        buf.write(u"\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u073c\n\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write(u"\5\u00a1\u0746\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\3\u00a2\7\u00a2\u074e\n\u00a2\f\u00a2\16\u00a2")
        buf.write(u"\u0751\13\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\7\u00a3")
        buf.write(u"\u075e\n\u00a3\f\u00a3\16\u00a3\u0761\13\u00a3\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5\5\u00a5")
        buf.write(u"\u076a\n\u00a5\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u076f")
        buf.write(u"\n\u00a5\f\u00a5\16\u00a5\u0772\13\u00a5\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a6\3\u00a6\5\u00a6\u0779\n\u00a6\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\5\u00a8\u0784\n\u00a8\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\7\u00a9\u078b\n\u00a9\f\u00a9\16\u00a9")
        buf.write(u"\u078e\13\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa")
        buf.write(u"\u0794\n\u00aa\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\5\u00ac\u079b\n\u00ac\3\u00ad\3\u00ad\3\u00ad\5\u00ad")
        buf.write(u"\u07a0\n\u00ad\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\7\u00ae\u07aa\n\u00ae\f\u00ae")
        buf.write(u"\16\u00ae\u07ad\13\u00ae\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u07bd\n\u00b1\f\u00b1")
        buf.write(u"\16\u00b1\u07c0\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\7\u00b2\u07c7\n\u00b2\f\u00b2\16\u00b2\u07ca")
        buf.write(u"\13\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\5\u00b3")
        buf.write(u"\u07d1\n\u00b3\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u07dc\n\u00b5")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u07e3")
        buf.write(u"\n\u00b6\f\u00b6\16\u00b6\u07e6\13\u00b6\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\5\u00b7\u07ec\n\u00b7\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b9\3\u00b9\3\u00b9\5\u00b9\u07f3\n\u00b9\3\u00ba")
        buf.write(u"\3\u00ba\3\u00ba\5\u00ba\u07f8\n\u00ba\3\u00ba\3\u00ba")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb")
        buf.write(u"\u0802\n\u00bb\f\u00bb\16\u00bb\u0805\13\u00bb\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write(u"\3\u00be\3\u00be\3\u00be\5\u00be\u0812\n\u00be\3\u00be")
        buf.write(u"\3\u00be\3\u00be\7\u00be\u0817\n\u00be\f\u00be\16\u00be")
        buf.write(u"\u081a\13\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write(u"\5\u00bf\u0821\n\u00bf\3\u00c0\3\u00c0\3\u00c0\2*\36")
        buf.write(u"\66JTXb\u0080\u0088\u008a\u008c\u0094\u0098\u00a6\u00b2")
        buf.write(u"\u00be\u00c0\u00c4\u00d4\u00da\u00e2\u00e4\u00e6\u00e8")
        buf.write(u"\u00ee\u00fe\u0100\u0108\u0120\u012a\u0138\u0142\u0144")
        buf.write(u"\u0148\u0150\u015a\u0160\u0162\u016a\u0174\u017a\u00c1")
        buf.write(u"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write(u"\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write(u"\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write(u"\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6")
        buf.write(u"\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8")
        buf.write(u"\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca")
        buf.write(u"\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc")
        buf.write(u"\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee")
        buf.write(u"\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100")
        buf.write(u"\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112")
        buf.write(u"\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124")
        buf.write(u"\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136")
        buf.write(u"\u0138\u013a\u013c\u013e\u0140\u0142\u0144\u0146\u0148")
        buf.write(u"\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a")
        buf.write(u"\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c")
        buf.write(u"\u016e\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e")
        buf.write(u"\2\n\3\2LM\3\2\"#\4\2~~\u0086\u0086\4\2\'\'ii\b\2\64")
        buf.write(u"<xx\u0085\u0085\u008f\u008f\u0094\u0096\u0098\u0098\b")
        buf.write(u"\2\64<xx~~\u0085\u0086\u008f\u008f\u0094\u0096\7\2\64")
        buf.write(u"<xx\u0085\u0085\u008f\u008f\u0094\u0098\7\2\64<xx\u0085")
        buf.write(u"\u0085\u008f\u008f\u0094\u0096\u0882\2\u0180\3\2\2\2")
        buf.write(u"\4\u0191\3\2\2\2\6\u019b\3\2\2\2\b\u019f\3\2\2\2\n\u01a7")
        buf.write(u"\3\2\2\2\f\u01b7\3\2\2\2\16\u01cd\3\2\2\2\20\u01da\3")
        buf.write(u"\2\2\2\22\u01dc\3\2\2\2\24\u01eb\3\2\2\2\26\u01f5\3\2")
        buf.write(u"\2\2\30\u0200\3\2\2\2\32\u0214\3\2\2\2\34\u0226\3\2\2")
        buf.write(u"\2\36\u022e\3\2\2\2 \u023a\3\2\2\2\"\u023c\3\2\2\2$\u0248")
        buf.write(u"\3\2\2\2&\u0258\3\2\2\2(\u0269\3\2\2\2*\u027c\3\2\2\2")
        buf.write(u",\u027e\3\2\2\2.\u029c\3\2\2\2\60\u029e\3\2\2\2\62\u02a3")
        buf.write(u"\3\2\2\2\64\u02af\3\2\2\2\66\u02b1\3\2\2\28\u02c1\3\2")
        buf.write(u"\2\2:\u02c3\3\2\2\2<\u02ca\3\2\2\2>\u02d1\3\2\2\2@\u02f1")
        buf.write(u"\3\2\2\2B\u02f3\3\2\2\2D\u0300\3\2\2\2F\u0309\3\2\2\2")
        buf.write(u"H\u0310\3\2\2\2J\u0324\3\2\2\2L\u033c\3\2\2\2N\u033f")
        buf.write(u"\3\2\2\2P\u0370\3\2\2\2R\u0372\3\2\2\2T\u0388\3\2\2\2")
        buf.write(u"V\u03ed\3\2\2\2X\u03ef\3\2\2\2Z\u03ff\3\2\2\2\\\u040e")
        buf.write(u"\3\2\2\2^\u0410\3\2\2\2`\u0413\3\2\2\2b\u0421\3\2\2\2")
        buf.write(u"d\u042b\3\2\2\2f\u042f\3\2\2\2h\u0433\3\2\2\2j\u0455")
        buf.write(u"\3\2\2\2l\u0457\3\2\2\2n\u0463\3\2\2\2p\u046f\3\2\2\2")
        buf.write(u"r\u0471\3\2\2\2t\u0478\3\2\2\2v\u047c\3\2\2\2x\u0481")
        buf.write(u"\3\2\2\2z\u048a\3\2\2\2|\u048f\3\2\2\2~\u0492\3\2\2\2")
        buf.write(u"\u0080\u0497\3\2\2\2\u0082\u04a8\3\2\2\2\u0084\u04aa")
        buf.write(u"\3\2\2\2\u0086\u04ae\3\2\2\2\u0088\u04b0\3\2\2\2\u008a")
        buf.write(u"\u04bc\3\2\2\2\u008c\u04c8\3\2\2\2\u008e\u04dd\3\2\2")
        buf.write(u"\2\u0090\u04df\3\2\2\2\u0092\u04e5\3\2\2\2\u0094\u04eb")
        buf.write(u"\3\2\2\2\u0096\u04f6\3\2\2\2\u0098\u04fc\3\2\2\2\u009a")
        buf.write(u"\u050e\3\2\2\2\u009c\u051a\3\2\2\2\u009e\u051c\3\2\2")
        buf.write(u"\2\u00a0\u051e\3\2\2\2\u00a2\u0520\3\2\2\2\u00a4\u0525")
        buf.write(u"\3\2\2\2\u00a6\u0527\3\2\2\2\u00a8\u0534\3\2\2\2\u00aa")
        buf.write(u"\u0539\3\2\2\2\u00ac\u053b\3\2\2\2\u00ae\u053d\3\2\2")
        buf.write(u"\2\u00b0\u053f\3\2\2\2\u00b2\u0541\3\2\2\2\u00b4\u0551")
        buf.write(u"\3\2\2\2\u00b6\u0555\3\2\2\2\u00b8\u0557\3\2\2\2\u00ba")
        buf.write(u"\u055c\3\2\2\2\u00bc\u0561\3\2\2\2\u00be\u0563\3\2\2")
        buf.write(u"\2\u00c0\u0571\3\2\2\2\u00c2\u0582\3\2\2\2\u00c4\u0584")
        buf.write(u"\3\2\2\2\u00c6\u0592\3\2\2\2\u00c8\u059e\3\2\2\2\u00ca")
        buf.write(u"\u05a0\3\2\2\2\u00cc\u05a4\3\2\2\2\u00ce\u05af\3\2\2")
        buf.write(u"\2\u00d0\u05b2\3\2\2\2\u00d2\u05b6\3\2\2\2\u00d4\u05c8")
        buf.write(u"\3\2\2\2\u00d6\u05d7\3\2\2\2\u00d8\u05d9\3\2\2\2\u00da")
        buf.write(u"\u05db\3\2\2\2\u00dc\u05f1\3\2\2\2\u00de\u05f3\3\2\2")
        buf.write(u"\2\u00e0\u05fa\3\2\2\2\u00e2\u0601\3\2\2\2\u00e4\u060d")
        buf.write(u"\3\2\2\2\u00e6\u0619\3\2\2\2\u00e8\u0625\3\2\2\2\u00ea")
        buf.write(u"\u063f\3\2\2\2\u00ec\u064e\3\2\2\2\u00ee\u0650\3\2\2")
        buf.write(u"\2\u00f0\u065f\3\2\2\2\u00f2\u0661\3\2\2\2\u00f4\u0663")
        buf.write(u"\3\2\2\2\u00f6\u0669\3\2\2\2\u00f8\u0670\3\2\2\2\u00fa")
        buf.write(u"\u0672\3\2\2\2\u00fc\u0678\3\2\2\2\u00fe\u067e\3\2\2")
        buf.write(u"\2\u0100\u0689\3\2\2\2\u0102\u0694\3\2\2\2\u0104\u06a1")
        buf.write(u"\3\2\2\2\u0106\u06a3\3\2\2\2\u0108\u06a7\3\2\2\2\u010a")
        buf.write(u"\u06b5\3\2\2\2\u010c\u06bd\3\2\2\2\u010e\u06bf\3\2\2")
        buf.write(u"\2\u0110\u06c2\3\2\2\2\u0112\u06c5\3\2\2\2\u0114\u06c8")
        buf.write(u"\3\2\2\2\u0116\u06ca\3\2\2\2\u0118\u06cc\3\2\2\2\u011a")
        buf.write(u"\u06ce\3\2\2\2\u011c\u06d0\3\2\2\2\u011e\u06d9\3\2\2")
        buf.write(u"\2\u0120\u06db\3\2\2\2\u0122\u06eb\3\2\2\2\u0124\u06ed")
        buf.write(u"\3\2\2\2\u0126\u06f4\3\2\2\2\u0128\u06f6\3\2\2\2\u012a")
        buf.write(u"\u06fd\3\2\2\2\u012c\u0708\3\2\2\2\u012e\u070c\3\2\2")
        buf.write(u"\2\u0130\u0710\3\2\2\2\u0132\u0717\3\2\2\2\u0134\u0719")
        buf.write(u"\3\2\2\2\u0136\u071e\3\2\2\2\u0138\u0720\3\2\2\2\u013a")
        buf.write(u"\u072e\3\2\2\2\u013c\u0736\3\2\2\2\u013e\u0738\3\2\2")
        buf.write(u"\2\u0140\u0745\3\2\2\2\u0142\u0747\3\2\2\2\u0144\u0752")
        buf.write(u"\3\2\2\2\u0146\u0762\3\2\2\2\u0148\u0769\3\2\2\2\u014a")
        buf.write(u"\u0778\3\2\2\2\u014c\u077a\3\2\2\2\u014e\u0783\3\2\2")
        buf.write(u"\2\u0150\u0785\3\2\2\2\u0152\u0793\3\2\2\2\u0154\u0795")
        buf.write(u"\3\2\2\2\u0156\u079a\3\2\2\2\u0158\u079c\3\2\2\2\u015a")
        buf.write(u"\u07a3\3\2\2\2\u015c\u07ae\3\2\2\2\u015e\u07b2\3\2\2")
        buf.write(u"\2\u0160\u07b6\3\2\2\2\u0162\u07c1\3\2\2\2\u0164\u07d0")
        buf.write(u"\3\2\2\2\u0166\u07d2\3\2\2\2\u0168\u07db\3\2\2\2\u016a")
        buf.write(u"\u07dd\3\2\2\2\u016c\u07eb\3\2\2\2\u016e\u07ed\3\2\2")
        buf.write(u"\2\u0170\u07f2\3\2\2\2\u0172\u07f4\3\2\2\2\u0174\u07fb")
        buf.write(u"\3\2\2\2\u0176\u0806\3\2\2\2\u0178\u080a\3\2\2\2\u017a")
        buf.write(u"\u0811\3\2\2\2\u017c\u0820\3\2\2\2\u017e\u0822\3\2\2")
        buf.write(u"\2\u0180\u0181\7W\2\2\u0181\u0182\5\u00aeX\2\u0182\u0189")
        buf.write(u"\7\26\2\2\u0183\u0186\5\u00aeX\2\u0184\u0185\7\23\2\2")
        buf.write(u"\u0185\u0187\5 \21\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write(u"\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u018a\5 \21\2\u0189")
        buf.write(u"\u0183\3\2\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2")
        buf.write(u"\2\u018b\u018c\7\27\2\2\u018c\u018d\7\21\2\2\u018d\u018e")
        buf.write(u"\5x=\2\u018e\u018f\5\u008aF\2\u018f\u0190\5z>\2\u0190")
        buf.write(u"\3\3\2\2\2\u0191\u0192\7W\2\2\u0192\u0193\5\u00aeX\2")
        buf.write(u"\u0193\u0194\7\26\2\2\u0194\u0195\5\u009cO\2\u0195\u0196")
        buf.write(u"\7\27\2\2\u0196\u0197\7\21\2\2\u0197\u0198\5x=\2\u0198")
        buf.write(u"\u0199\5\u0088E\2\u0199\u019a\5z>\2\u019a\5\3\2\2\2\u019b")
        buf.write(u"\u019c\5\u00b0Y\2\u019c\u019d\7-\2\2\u019d\u019e\5T+")
        buf.write(u"\2\u019e\7\3\2\2\2\u019f\u01a0\5\u00b0Y\2\u01a0\u01a2")
        buf.write(u"\7\26\2\2\u01a1\u01a3\5b\62\2\u01a2\u01a1\3\2\2\2\u01a2")
        buf.write(u"\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\7\27\2")
        buf.write(u"\2\u01a5\t\3\2\2\2\u01a6\u01a8\7\u0082\2\2\u01a7\u01a6")
        buf.write(u"\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write(u"\u01aa\7F\2\2\u01aa\u01ab\5\u00acW\2\u01ab\u01ac\7\26")
        buf.write(u"\2\2\u01ac\u01ad\5\u0098M\2\u01ad\u01ae\7\27\2\2\u01ae")
        buf.write(u"\u01af\7\21\2\2\u01af\u01b2\5x=\2\u01b0\u01b3\5\u008e")
        buf.write(u"H\2\u01b1\u01b3\7v\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1")
        buf.write(u"\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\5z>\2\u01b5")
        buf.write(u"\13\3\2\2\2\u01b6\u01b8\7\u0082\2\2\u01b7\u01b6\3\2\2")
        buf.write(u"\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba")
        buf.write(u"\t\2\2\2\u01ba\u01bb\5\u00aeX\2\u01bb\u01c2\7\26\2\2")
        buf.write(u"\u01bc\u01c3\5\20\t\2\u01bd\u01c3\5 \21\2\u01be\u01bf")
        buf.write(u"\5\20\t\2\u01bf\u01c0\7\23\2\2\u01c0\u01c1\5 \21\2\u01c1")
        buf.write(u"\u01c3\3\2\2\2\u01c2\u01bc\3\2\2\2\u01c2\u01bd\3\2\2")
        buf.write(u"\2\u01c2\u01be\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5")
        buf.write(u"\7\27\2\2\u01c5\u01c6\7\21\2\2\u01c6\u01c9\5x=\2\u01c7")
        buf.write(u"\u01ca\5\u00c0a\2\u01c8\u01ca\7v\2\2\u01c9\u01c7\3\2")
        buf.write(u"\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc")
        buf.write(u"\5z>\2\u01cc\r\3\2\2\2\u01cd\u01ce\7\u0080\2\2\u01ce")
        buf.write(u"\u01cf\5\u00aeX\2\u01cf\u01d0\7\26\2\2\u01d0\u01d1\5")
        buf.write(u" \21\2\u01d1\u01d2\7\27\2\2\u01d2\u01d3\7\21\2\2\u01d3")
        buf.write(u"\u01d6\5x=\2\u01d4\u01d7\5\u00c0a\2\u01d5\u01d7\7v\2")
        buf.write(u"\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write(u"\3\2\2\2\u01d8\u01d9\5z>\2\u01d9\17\3\2\2\2\u01da\u01db")
        buf.write(u"\5\u00a6T\2\u01db\21\3\2\2\2\u01dc\u01dd\7P\2\2\u01dd")
        buf.write(u"\u01de\7s\2\2\u01de\u01df\5\u010c\u0087\2\u01df\u01e0")
        buf.write(u"\7\26\2\2\u01e0\u01e1\5\u00b6\\\2\u01e1\u01e4\7\27\2")
        buf.write(u"\2\u01e2\u01e3\7\63\2\2\u01e3\u01e5\5\u0098M\2\u01e4")
        buf.write(u"\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\3\2\2")
        buf.write(u"\2\u01e6\u01e7\7\21\2\2\u01e7\u01e8\5x=\2\u01e8\u01e9")
        buf.write(u"\5\u00e2r\2\u01e9\u01ea\5z>\2\u01ea\23\3\2\2\2\u01eb")
        buf.write(u"\u01ec\7P\2\2\u01ec\u01ed\5\u00acW\2\u01ed\u01ee\7\177")
        buf.write(u"\2\2\u01ee\u01ef\7\26\2\2\u01ef\u01f0\7\27\2\2\u01f0")
        buf.write(u"\u01f1\7\21\2\2\u01f1\u01f2\5x=\2\u01f2\u01f3\5\u00e2")
        buf.write(u"r\2\u01f3\u01f4\5z>\2\u01f4\25\3\2\2\2\u01f5\u01f6\7")
        buf.write(u"P\2\2\u01f6\u01f7\5\u00acW\2\u01f7\u01f8\7a\2\2\u01f8")
        buf.write(u"\u01f9\7\26\2\2\u01f9\u01fa\7\27\2\2\u01fa\u01fb\7\21")
        buf.write(u"\2\2\u01fb\u01fc\5x=\2\u01fc\u01fd\5\u00e2r\2\u01fd\u01fe")
        buf.write(u"\5z>\2\u01fe\27\3\2\2\2\u01ff\u0201\7\u0082\2\2\u0200")
        buf.write(u"\u01ff\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\3\2\2")
        buf.write(u"\2\u0202\u0203\7k\2\2\u0203\u0204\t\2\2\2\u0204\u0205")
        buf.write(u"\5\u00aeX\2\u0205\u0207\7\26\2\2\u0206\u0208\5 \21\2")
        buf.write(u"\u0207\u0206\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209")
        buf.write(u"\3\2\2\2\u0209\u020a\7\27\2\2\u020a\u020b\7\21\2\2\u020b")
        buf.write(u"\u020c\5x=\2\u020c\u0210\5\34\17\2\u020d\u020e\5v<\2")
        buf.write(u"\u020e\u020f\5\u00c4c\2\u020f\u0211\3\2\2\2\u0210\u020d")
        buf.write(u"\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write(u"\u0213\5z>\2\u0213\31\3\2\2\2\u0214\u0215\7k\2\2\u0215")
        buf.write(u"\u0216\7z\2\2\u0216\u0217\5\u00aeX\2\u0217\u0219\7\26")
        buf.write(u"\2\2\u0218\u021a\5 \21\2\u0219\u0218\3\2\2\2\u0219\u021a")
        buf.write(u"\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\7\27\2\2\u021c")
        buf.write(u"\u021d\7\21\2\2\u021d\u021e\5x=\2\u021e\u0222\5\34\17")
        buf.write(u"\2\u021f\u0220\5v<\2\u0220\u0221\5\u00c4c\2\u0221\u0223")
        buf.write(u"\3\2\2\2\u0222\u021f\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write(u"\u0224\3\2\2\2\u0224\u0225\5z>\2\u0225\33\3\2\2\2\u0226")
        buf.write(u"\u0227\7P\2\2\u0227\u0228\t\2\2\2\u0228\u0229\7I\2\2")
        buf.write(u"\u0229\u022a\7\21\2\2\u022a\u022b\5x=\2\u022b\u022c\5")
        buf.write(u"\36\20\2\u022c\u022d\5z>\2\u022d\35\3\2\2\2\u022e\u022f")
        buf.write(u"\b\20\1\2\u022f\u0230\5\u00c8e\2\u0230\u0237\3\2\2\2")
        buf.write(u"\u0231\u0232\f\3\2\2\u0232\u0233\5v<\2\u0233\u0234\5")
        buf.write(u"\u00c8e\2\u0234\u0236\3\2\2\2\u0235\u0231\3\2\2\2\u0236")
        buf.write(u"\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2")
        buf.write(u"\2\u0238\37\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\5")
        buf.write(u"\u00d4k\2\u023b!\3\2\2\2\u023c\u023d\7@\2\2\u023d\u023e")
        buf.write(u"\7P\2\2\u023e\u023f\5\u00a8U\2\u023f\u0241\7\26\2\2\u0240")
        buf.write(u"\u0242\5\u00b2Z\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2")
        buf.write(u"\2\2\u0242\u0243\3\2\2\2\u0243\u0246\7\27\2\2\u0244\u0245")
        buf.write(u"\7\63\2\2\u0245\u0247\5\u0098M\2\u0246\u0244\3\2\2\2")
        buf.write(u"\u0246\u0247\3\2\2\2\u0247#\3\2\2\2\u0248\u0249\7P\2")
        buf.write(u"\2\u0249\u024a\5\u00a8U\2\u024a\u024c\7\26\2\2\u024b")
        buf.write(u"\u024d\5\u00b2Z\2\u024c\u024b\3\2\2\2\u024c\u024d\3\2")
        buf.write(u"\2\2\u024d\u024e\3\2\2\2\u024e\u0251\7\27\2\2\u024f\u0250")
        buf.write(u"\7\63\2\2\u0250\u0252\5\u0098M\2\u0251\u024f\3\2\2\2")
        buf.write(u"\u0251\u0252\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0254")
        buf.write(u"\7\21\2\2\u0254\u0255\5x=\2\u0255\u0256\5\u00e2r\2\u0256")
        buf.write(u"\u0257\5z>\2\u0257%\3\2\2\2\u0258\u0259\7P\2\2\u0259")
        buf.write(u"\u025a\7k\2\2\u025a\u025b\5\u00a8U\2\u025b\u025d\7\26")
        buf.write(u"\2\2\u025c\u025e\5\u00b2Z\2\u025d\u025c\3\2\2\2\u025d")
        buf.write(u"\u025e\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0262\7\27\2")
        buf.write(u"\2\u0260\u0261\7\63\2\2\u0261\u0263\5\u00bc_\2\u0262")
        buf.write(u"\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\3\2\2")
        buf.write(u"\2\u0264\u0265\7\21\2\2\u0265\u0266\5x=\2\u0266\u0267")
        buf.write(u"\5\u00dan\2\u0267\u0268\5z>\2\u0268\'\3\2\2\2\u0269\u026a")
        buf.write(u"\7P\2\2\u026a\u026b\7\u0085\2\2\u026b\u026c\7\u0099\2")
        buf.write(u"\2\u026c\u026d\7\26\2\2\u026d\u026e\7\27\2\2\u026e\u026f")
        buf.write(u"\7\21\2\2\u026f\u0270\5x=\2\u0270\u0271\5\u00e2r\2\u0271")
        buf.write(u"\u0272\5z>\2\u0272\u0273\5v<\2\u0273\u0274\7\u008a\2")
        buf.write(u"\2\u0274\u027a\7\21\2\2\u0275\u0276\5x=\2\u0276\u0277")
        buf.write(u"\5\u00e4s\2\u0277\u0278\5z>\2\u0278\u027b\3\2\2\2\u0279")
        buf.write(u"\u027b\5\u00b0Y\2\u027a\u0275\3\2\2\2\u027a\u0279\3\2")
        buf.write(u"\2\2\u027b)\3\2\2\2\u027c\u027d\5T+\2\u027d+\3\2\2\2")
        buf.write(u"\u027e\u027f\5\u00acW\2\u027f\u0280\7\21\2\2\u0280\u0285")
        buf.write(u"\5\u00bc_\2\u0281\u0282\7\26\2\2\u0282\u0283\5 \21\2")
        buf.write(u"\u0283\u0284\7\27\2\2\u0284\u0286\3\2\2\2\u0285\u0281")
        buf.write(u"\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0289\3\2\2\2\u0287")
        buf.write(u"\u0288\7-\2\2\u0288\u028a\5\u00f6|\2\u0289\u0287\3\2")
        buf.write(u"\2\2\u0289\u028a\3\2\2\2\u028a-\3\2\2\2\u028b\u029d\5")
        buf.write(u"\62\32\2\u028c\u029d\5n8\2\u028d\u029d\5r:\2\u028e\u029d")
        buf.write(u"\5\60\31\2\u028f\u029d\5R*\2\u0290\u029d\5H%\2\u0291")
        buf.write(u"\u029d\5> \2\u0292\u029d\5B\"\2\u0293\u029d\5F$\2\u0294")
        buf.write(u"\u029d\5D#\2\u0295\u029d\5L\'\2\u0296\u029d\5N(\2\u0297")
        buf.write(u"\u029d\5h\65\2\u0298\u029d\5:\36\2\u0299\u029d\5<\37")
        buf.write(u"\2\u029a\u029d\5$\23\2\u029b\u029d\5\u00d8m\2\u029c\u028b")
        buf.write(u"\3\2\2\2\u029c\u028c\3\2\2\2\u029c\u028d\3\2\2\2\u029c")
        buf.write(u"\u028e\3\2\2\2\u029c\u028f\3\2\2\2\u029c\u0290\3\2\2")
        buf.write(u"\2\u029c\u0291\3\2\2\2\u029c\u0292\3\2\2\2\u029c\u0293")
        buf.write(u"\3\2\2\2\u029c\u0294\3\2\2\2\u029c\u0295\3\2\2\2\u029c")
        buf.write(u"\u0296\3\2\2\2\u029c\u0297\3\2\2\2\u029c\u0298\3\2\2")
        buf.write(u"\2\u029c\u0299\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029b")
        buf.write(u"\3\2\2\2\u029d/\3\2\2\2\u029e\u029f\7\u0083\2\2\u029f")
        buf.write(u"\u02a0\7\26\2\2\u02a0\u02a1\5\u0094K\2\u02a1\u02a2\7")
        buf.write(u"\27\2\2\u02a2\61\3\2\2\2\u02a3\u02a4\5\64\33\2\u02a4")
        buf.write(u"\u02a6\7\26\2\2\u02a5\u02a7\5b\62\2\u02a6\u02a5\3\2\2")
        buf.write(u"\2\u02a6\u02a7\3\2\2\2\u02a7\u02a8\3\2\2\2\u02a8\u02a9")
        buf.write(u"\7\27\2\2\u02a9\63\3\2\2\2\u02aa\u02b0\5\u00a8U\2\u02ab")
        buf.write(u"\u02ac\5\66\34\2\u02ac\u02ad\7\25\2\2\u02ad\u02ae\5\u00a8")
        buf.write(u"U\2\u02ae\u02b0\3\2\2\2\u02af\u02aa\3\2\2\2\u02af\u02ab")
        buf.write(u"\3\2\2\2\u02b0\65\3\2\2\2\u02b1\u02b2\b\34\1\2\u02b2")
        buf.write(u"\u02b3\5\u00aaV\2\u02b3\u02b8\3\2\2\2\u02b4\u02b5\f\3")
        buf.write(u"\2\2\u02b5\u02b7\58\35\2\u02b6\u02b4\3\2\2\2\u02b7\u02ba")
        buf.write(u"\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9")
        buf.write(u"\67\3\2\2\2\u02ba\u02b8\3\2\2\2\u02bb\u02bc\7\25\2\2")
        buf.write(u"\u02bc\u02c2\5\u00acW\2\u02bd\u02be\7\30\2\2\u02be\u02bf")
        buf.write(u"\5T+\2\u02bf\u02c0\7\31\2\2\u02c0\u02c2\3\2\2\2\u02c1")
        buf.write(u"\u02bb\3\2\2\2\u02c1\u02bd\3\2\2\2\u02c29\3\2\2\2\u02c3")
        buf.write(u"\u02c4\7\u008b\2\2\u02c4\u02c5\5\u0106\u0084\2\u02c5")
        buf.write(u"\u02c6\7\21\2\2\u02c6\u02c7\5x=\2\u02c7\u02c8\5\u00e2")
        buf.write(u"r\2\u02c8\u02c9\5z>\2\u02c9;\3\2\2\2\u02ca\u02cb\7\u008b")
        buf.write(u"\2\2\u02cb\u02cc\5\u00aeX\2\u02cc\u02cd\7\21\2\2\u02cd")
        buf.write(u"\u02ce\5x=\2\u02ce\u02cf\5\u00e2r\2\u02cf\u02d0\5z>\2")
        buf.write(u"\u02d0=\3\2\2\2\u02d1\u02d2\7\u0084\2\2\u02d2\u02d3\7")
        buf.write(u"p\2\2\u02d3\u02d4\5T+\2\u02d4\u02d5\7\21\2\2\u02d5\u02d6")
        buf.write(u"\5x=\2\u02d6\u02de\5\u00e6t\2\u02d7\u02d8\5v<\2\u02d8")
        buf.write(u"\u02d9\7u\2\2\u02d9\u02da\7\21\2\2\u02da\u02db\5x=\2")
        buf.write(u"\u02db\u02dc\5\u00e2r\2\u02dc\u02dd\5z>\2\u02dd\u02df")
        buf.write(u"\3\2\2\2\u02de\u02d7\3\2\2\2\u02de\u02df\3\2\2\2\u02df")
        buf.write(u"\u02e0\3\2\2\2\u02e0\u02e1\5z>\2\u02e1?\3\2\2\2\u02e2")
        buf.write(u"\u02e3\7\u008c\2\2\u02e3\u02e4\5\u00ecw\2\u02e4\u02e5")
        buf.write(u"\7\21\2\2\u02e5\u02e6\5x=\2\u02e6\u02e7\5\u00e2r\2\u02e7")
        buf.write(u"\u02e8\5z>\2\u02e8\u02f2\3\2\2\2\u02e9\u02ea\7\u008c")
        buf.write(u"\2\2\u02ea\u02eb\7c\2\2\u02eb\u02ec\5\u00eav\2\u02ec")
        buf.write(u"\u02ed\7\21\2\2\u02ed\u02ee\5x=\2\u02ee\u02ef\5\u00e2")
        buf.write(u"r\2\u02ef\u02f0\5z>\2\u02f0\u02f2\3\2\2\2\u02f1\u02e2")
        buf.write(u"\3\2\2\2\u02f1\u02e9\3\2\2\2\u02f2A\3\2\2\2\u02f3\u02f4")
        buf.write(u"\7_\2\2\u02f4\u02f7\5\u00acW\2\u02f5\u02f6\7\23\2\2\u02f6")
        buf.write(u"\u02f8\5\u00acW\2\u02f7\u02f5\3\2\2\2\u02f7\u02f8\3\2")
        buf.write(u"\2\2\u02f8\u02f9\3\2\2\2\u02f9\u02fa\7c\2\2\u02fa\u02fb")
        buf.write(u"\5T+\2\u02fb\u02fc\7\21\2\2\u02fc\u02fd\5x=\2\u02fd\u02fe")
        buf.write(u"\5\u00e2r\2\u02fe\u02ff\5z>\2\u02ffC\3\2\2\2\u0300\u0301")
        buf.write(u"\7S\2\2\u0301\u0302\7\21\2\2\u0302\u0303\5x=\2\u0303")
        buf.write(u"\u0304\5\u00e2r\2\u0304\u0305\5z>\2\u0305\u0306\5v<\2")
        buf.write(u"\u0306\u0307\7\u008e\2\2\u0307\u0308\5T+\2\u0308E\3\2")
        buf.write(u"\2\2\u0309\u030a\7\u008e\2\2\u030a\u030b\5T+\2\u030b")
        buf.write(u"\u030c\7\21\2\2\u030c\u030d\5x=\2\u030d\u030e\5\u00e2")
        buf.write(u"r\2\u030e\u030f\5z>\2\u030fG\3\2\2\2\u0310\u0311\7b\2")
        buf.write(u"\2\u0311\u0312\5T+\2\u0312\u0313\7\21\2\2\u0313\u0314")
        buf.write(u"\5x=\2\u0314\u0315\5\u00e2r\2\u0315\u0319\5z>\2\u0316")
        buf.write(u"\u0317\5v<\2\u0317\u0318\5J&\2\u0318\u031a\3\2\2\2\u0319")
        buf.write(u"\u0316\3\2\2\2\u0319\u031a\3\2\2\2\u031a\u0322\3\2\2")
        buf.write(u"\2\u031b\u031c\5v<\2\u031c\u031d\7V\2\2\u031d\u031e\7")
        buf.write(u"\21\2\2\u031e\u031f\5x=\2\u031f\u0320\5\u00e2r\2\u0320")
        buf.write(u"\u0321\5z>\2\u0321\u0323\3\2\2\2\u0322\u031b\3\2\2\2")
        buf.write(u"\u0322\u0323\3\2\2\2\u0323I\3\2\2\2\u0324\u0325\b&\1")
        buf.write(u"\2\u0325\u0326\7V\2\2\u0326\u0327\7b\2\2\u0327\u0328")
        buf.write(u"\5T+\2\u0328\u0329\7\21\2\2\u0329\u032a\5x=\2\u032a\u032b")
        buf.write(u"\5\u00e2r\2\u032b\u032c\5z>\2\u032c\u0339\3\2\2\2\u032d")
        buf.write(u"\u032e\f\3\2\2\u032e\u032f\5v<\2\u032f\u0330\7V\2\2\u0330")
        buf.write(u"\u0331\7b\2\2\u0331\u0332\5T+\2\u0332\u0333\7\21\2\2")
        buf.write(u"\u0333\u0334\5x=\2\u0334\u0335\5\u00e2r\2\u0335\u0336")
        buf.write(u"\5z>\2\u0336\u0338\3\2\2\2\u0337\u032d\3\2\2\2\u0338")
        buf.write(u"\u033b\3\2\2\2\u0339\u0337\3\2\2\2\u0339\u033a\3\2\2")
        buf.write(u"\2\u033aK\3\2\2\2\u033b\u0339\3\2\2\2\u033c\u033d\7w")
        buf.write(u"\2\2\u033d\u033e\5T+\2\u033eM\3\2\2\2\u033f\u0340\7\u0089")
        buf.write(u"\2\2\u0340\u0341\5\u00acW\2\u0341\u0342\7\21\2\2\u0342")
        buf.write(u"\u0343\5x=\2\u0343\u0344\5\u00e2r\2\u0344\u0345\5z>\2")
        buf.write(u"\u0345\u0347\5t;\2\u0346\u0348\5\u00e8u\2\u0347\u0346")
        buf.write(u"\3\2\2\2\u0347\u0348\3\2\2\2\u0348\u0350\3\2\2\2\u0349")
        buf.write(u"\u034a\7Y\2\2\u034a\u034b\7\21\2\2\u034b\u034c\5x=\2")
        buf.write(u"\u034c\u034d\5\u00e2r\2\u034d\u034e\5z>\2\u034e\u034f")
        buf.write(u"\5t;\2\u034f\u0351\3\2\2\2\u0350\u0349\3\2\2\2\u0350")
        buf.write(u"\u0351\3\2\2\2\u0351\u0359\3\2\2\2\u0352\u0353\7^\2\2")
        buf.write(u"\u0353\u0354\7\21\2\2\u0354\u0355\5x=\2\u0355\u0356\5")
        buf.write(u"\u00e2r\2\u0356\u0357\5z>\2\u0357\u0358\5t;\2\u0358\u035a")
        buf.write(u"\3\2\2\2\u0359\u0352\3\2\2\2\u0359\u035a\3\2\2\2\u035a")
        buf.write(u"\u035b\3\2\2\2\u035b\u035c\5t;\2\u035cO\3\2\2\2\u035d")
        buf.write(u"\u035e\7Y\2\2\u035e\u035f\5\u00b0Y\2\u035f\u0360\7\21")
        buf.write(u"\2\2\u0360\u0361\5x=\2\u0361\u0362\5\u00e2r\2\u0362\u0363")
        buf.write(u"\5z>\2\u0363\u0364\5t;\2\u0364\u0371\3\2\2\2\u0365\u0366")
        buf.write(u"\7Y\2\2\u0366\u0367\7c\2\2\u0367\u0368\7\30\2\2\u0368")
        buf.write(u"\u0369\5\u008cG\2\u0369\u036a\7\31\2\2\u036a\u036b\7")
        buf.write(u"\21\2\2\u036b\u036c\5x=\2\u036c\u036d\5\u00e2r\2\u036d")
        buf.write(u"\u036e\5z>\2\u036e\u036f\5t;\2\u036f\u0371\3\2\2\2\u0370")
        buf.write(u"\u035d\3\2\2\2\u0370\u0365\3\2\2\2\u0371Q\3\2\2\2\u0372")
        buf.write(u"\u0374\7{\2\2\u0373\u0375\5T+\2\u0374\u0373\3\2\2\2\u0374")
        buf.write(u"\u0375\3\2\2\2\u0375S\3\2\2\2\u0376\u0377\b+\1\2\u0377")
        buf.write(u"\u0378\7#\2\2\u0378\u0389\5T+!\u0379\u037a\7m\2\2\u037a")
        buf.write(u"\u0389\5T+ \u037b\u0389\5X-\2\u037c\u0389\5Z.\2\u037d")
        buf.write(u"\u037e\7>\2\2\u037e\u037f\7\26\2\2\u037f\u0380\5T+\2")
        buf.write(u"\u0380\u0381\7\27\2\2\u0381\u0389\3\2\2\2\u0382\u0383")
        buf.write(u"\7Z\2\2\u0383\u0384\7\26\2\2\u0384\u0385\5\u00acW\2\u0385")
        buf.write(u"\u0386\7\27\2\2\u0386\u0389\3\2\2\2\u0387\u0389\5V,\2")
        buf.write(u"\u0388\u0376\3\2\2\2\u0388\u0379\3\2\2\2\u0388\u037b")
        buf.write(u"\3\2\2\2\u0388\u037c\3\2\2\2\u0388\u037d\3\2\2\2\u0388")
        buf.write(u"\u0382\3\2\2\2\u0388\u0387\3\2\2\2\u0389\u03ea\3\2\2")
        buf.write(u"\2\u038a\u038b\f\37\2\2\u038b\u038c\5\u0116\u008c\2\u038c")
        buf.write(u"\u038d\5T+ \u038d\u03e9\3\2\2\2\u038e\u038f\f\36\2\2")
        buf.write(u"\u038f\u0390\5\u0118\u008d\2\u0390\u0391\5T+\37\u0391")
        buf.write(u"\u03e9\3\2\2\2\u0392\u0393\f\35\2\2\u0393\u0394\5\u011c")
        buf.write(u"\u008f\2\u0394\u0395\5T+\36\u0395\u03e9\3\2\2\2\u0396")
        buf.write(u"\u0397\f\34\2\2\u0397\u0398\5\u011a\u008e\2\u0398\u0399")
        buf.write(u"\5T+\35\u0399\u03e9\3\2\2\2\u039a\u039b\f\33\2\2\u039b")
        buf.write(u"\u039c\t\3\2\2\u039c\u03e9\5T+\34\u039d\u039e\f\32\2")
        buf.write(u"\2\u039e\u039f\7*\2\2\u039f\u03e9\5T+\33\u03a0\u03a1")
        buf.write(u"\f\31\2\2\u03a1\u03a2\7+\2\2\u03a2\u03e9\5T+\32\u03a3")
        buf.write(u"\u03a4\f\30\2\2\u03a4\u03a5\7(\2\2\u03a5\u03e9\5T+\31")
        buf.write(u"\u03a6\u03a7\f\27\2\2\u03a7\u03a8\7)\2\2\u03a8\u03e9")
        buf.write(u"\5T+\30\u03a9\u03aa\f\24\2\2\u03aa\u03ab\7/\2\2\u03ab")
        buf.write(u"\u03e9\5T+\25\u03ac\u03ad\f\23\2\2\u03ad\u03ae\7.\2\2")
        buf.write(u"\u03ae\u03e9\5T+\24\u03af\u03b0\f\22\2\2\u03b0\u03b1")
        buf.write(u"\7\60\2\2\u03b1\u03e9\5T+\23\u03b2\u03b3\f\21\2\2\u03b3")
        buf.write(u"\u03b4\7t\2\2\u03b4\u03e9\5T+\22\u03b5\u03b6\f\20\2\2")
        buf.write(u"\u03b6\u03b7\7C\2\2\u03b7\u03e9\5T+\21\u03b8\u03b9\f")
        buf.write(u"\17\2\2\u03b9\u03ba\7b\2\2\u03ba\u03bb\5T+\2\u03bb\u03bc")
        buf.write(u"\7V\2\2\u03bc\u03bd\5T+\20\u03bd\u03e9\3\2\2\2\u03be")
        buf.write(u"\u03bf\f\r\2\2\u03bf\u03c0\7c\2\2\u03c0\u03e9\5T+\16")
        buf.write(u"\u03c1\u03c2\f\f\2\2\u03c2\u03c3\7O\2\2\u03c3\u03e9\5")
        buf.write(u"T+\r\u03c4\u03c5\f\13\2\2\u03c5\u03c6\7O\2\2\u03c6\u03c7")
        buf.write(u"\7A\2\2\u03c7\u03e9\5T+\f\u03c8\u03c9\f\n\2\2\u03c9\u03ca")
        buf.write(u"\7O\2\2\u03ca\u03cb\7D\2\2\u03cb\u03e9\5T+\13\u03cc\u03cd")
        buf.write(u"\f\t\2\2\u03cd\u03ce\7m\2\2\u03ce\u03cf\7c\2\2\u03cf")
        buf.write(u"\u03e9\5T+\n\u03d0\u03d1\f\b\2\2\u03d1\u03d2\7m\2\2\u03d2")
        buf.write(u"\u03d3\7O\2\2\u03d3\u03e9\5T+\t\u03d4\u03d5\f\7\2\2\u03d5")
        buf.write(u"\u03d6\7m\2\2\u03d6\u03d7\7O\2\2\u03d7\u03d8\7A\2\2\u03d8")
        buf.write(u"\u03e9\5T+\b\u03d9\u03da\f\6\2\2\u03da\u03db\7m\2\2\u03db")
        buf.write(u"\u03dc\7O\2\2\u03dc\u03dd\7D\2\2\u03dd\u03e9\5T+\7\u03de")
        buf.write(u"\u03df\f\26\2\2\u03df\u03e0\7e\2\2\u03e0\u03e1\7m\2\2")
        buf.write(u"\u03e1\u03e9\5\u010a\u0086\2\u03e2\u03e3\f\25\2\2\u03e3")
        buf.write(u"\u03e4\7e\2\2\u03e4\u03e9\5\u010a\u0086\2\u03e5\u03e6")
        buf.write(u"\f\16\2\2\u03e6\u03e7\7E\2\2\u03e7\u03e9\5\u00bc_\2\u03e8")
        buf.write(u"\u038a\3\2\2\2\u03e8\u038e\3\2\2\2\u03e8\u0392\3\2\2")
        buf.write(u"\2\u03e8\u0396\3\2\2\2\u03e8\u039a\3\2\2\2\u03e8\u039d")
        buf.write(u"\3\2\2\2\u03e8\u03a0\3\2\2\2\u03e8\u03a3\3\2\2\2\u03e8")
        buf.write(u"\u03a6\3\2\2\2\u03e8\u03a9\3\2\2\2\u03e8\u03ac\3\2\2")
        buf.write(u"\2\u03e8\u03af\3\2\2\2\u03e8\u03b2\3\2\2\2\u03e8\u03b5")
        buf.write(u"\3\2\2\2\u03e8\u03b8\3\2\2\2\u03e8\u03be\3\2\2\2\u03e8")
        buf.write(u"\u03c1\3\2\2\2\u03e8\u03c4\3\2\2\2\u03e8\u03c8\3\2\2")
        buf.write(u"\2\u03e8\u03cc\3\2\2\2\u03e8\u03d0\3\2\2\2\u03e8\u03d4")
        buf.write(u"\3\2\2\2\u03e8\u03d9\3\2\2\2\u03e8\u03de\3\2\2\2\u03e8")
        buf.write(u"\u03e2\3\2\2\2\u03e8\u03e5\3\2\2\2\u03e9\u03ec\3\2\2")
        buf.write(u"\2\u03ea\u03e8\3\2\2\2\u03ea\u03eb\3\2\2\2\u03ebU\3\2")
        buf.write(u"\2\2\u03ec\u03ea\3\2\2\2\u03ed\u03ee\5\u00aeX\2\u03ee")
        buf.write(u"W\3\2\2\2\u03ef\u03f0\b-\1\2\u03f0\u03f1\5\u00f0y\2\u03f1")
        buf.write(u"\u03f6\3\2\2\2\u03f2\u03f3\f\3\2\2\u03f3\u03f5\5\\/\2")
        buf.write(u"\u03f4\u03f2\3\2\2\2\u03f5\u03f8\3\2\2\2\u03f6\u03f4")
        buf.write(u"\3\2\2\2\u03f6\u03f7\3\2\2\2\u03f7Y\3\2\2\2\u03f8\u03f6")
        buf.write(u"\3\2\2\2\u03f9\u0400\5^\60\2\u03fa\u0400\5j\66\2\u03fb")
        buf.write(u"\u0400\5f\64\2\u03fc\u0400\5l\67\2\u03fd\u0400\5\62\32")
        buf.write(u"\2\u03fe\u0400\5`\61\2\u03ff\u03f9\3\2\2\2\u03ff\u03fa")
        buf.write(u"\3\2\2\2\u03ff\u03fb\3\2\2\2\u03ff\u03fc\3\2\2\2\u03ff")
        buf.write(u"\u03fd\3\2\2\2\u03ff\u03fe\3\2\2\2\u0400[\3\2\2\2\u0401")
        buf.write(u"\u0402\6/ \3\u0402\u0403\7\25\2\2\u0403\u040f\5\u00ac")
        buf.write(u"W\2\u0404\u0405\6/!\3\u0405\u0406\7\30\2\2\u0406\u0407")
        buf.write(u"\5\u0104\u0083\2\u0407\u0408\7\31\2\2\u0408\u040f\3\2")
        buf.write(u"\2\2\u0409\u040a\6/\"\3\u040a\u040b\7\30\2\2\u040b\u040c")
        buf.write(u"\5T+\2\u040c\u040d\7\31\2\2\u040d\u040f\3\2\2\2\u040e")
        buf.write(u"\u0401\3\2\2\2\u040e\u0404\3\2\2\2\u040e\u0409\3\2\2")
        buf.write(u"\2\u040f]\3\2\2\2\u0410\u0411\5\u00a2R\2\u0411_\3\2\2")
        buf.write(u"\2\u0412\u0414\7j\2\2\u0413\u0412\3\2\2\2\u0413\u0414")
        buf.write(u"\3\2\2\2\u0414\u0415\3\2\2\2\u0415\u0416\5\u009eP\2\u0416")
        buf.write(u"\u0418\7\26\2\2\u0417\u0419\5b\62\2\u0418\u0417\3\2\2")
        buf.write(u"\2\u0418\u0419\3\2\2\2\u0419\u041a\3\2\2\2\u041a\u041b")
        buf.write(u"\7\27\2\2\u041ba\3\2\2\2\u041c\u041d\b\62\1\2\u041d\u041e")
        buf.write(u"\5T+\2\u041e\u041f\6\62#\3\u041f\u0422\3\2\2\2\u0420")
        buf.write(u"\u0422\5d\63\2\u0421\u041c\3\2\2\2\u0421\u0420\3\2\2")
        buf.write(u"\2\u0422\u0428\3\2\2\2\u0423\u0424\f\3\2\2\u0424\u0425")
        buf.write(u"\7\23\2\2\u0425\u0427\5d\63\2\u0426\u0423\3\2\2\2\u0427")
        buf.write(u"\u042a\3\2\2\2\u0428\u0426\3\2\2\2\u0428\u0429\3\2\2")
        buf.write(u"\2\u0429c\3\2\2\2\u042a\u0428\3\2\2\2\u042b\u042c\5\u00ac")
        buf.write(u"W\2\u042c\u042d\5\u0114\u008b\2\u042d\u042e\5T+\2\u042e")
        buf.write(u"e\3\2\2\2\u042f\u0430\7x\2\2\u0430\u0431\7`\2\2\u0431")
        buf.write(u"\u0432\5T+\2\u0432g\3\2\2\2\u0433\u0434\7\u008f\2\2\u0434")
        buf.write(u"\u0435\5T+\2\u0435\u0436\7\u0088\2\2\u0436\u0437\5T+")
        buf.write(u"\2\u0437i\3\2\2\2\u0438\u0439\7]\2\2\u0439\u043a\5\u00ac")
        buf.write(u"W\2\u043a\u043b\7`\2\2\u043b\u043c\5T+\2\u043c\u043d")
        buf.write(u"\7\u008d\2\2\u043d\u043e\5T+\2\u043e\u0456\3\2\2\2\u043f")
        buf.write(u"\u0440\7]\2\2\u0440\u0441\7q\2\2\u0441\u0442\5\u009e")
        buf.write(u"P\2\u0442\u0443\7\u008d\2\2\u0443\u0444\5T+\2\u0444\u0456")
        buf.write(u"\3\2\2\2\u0445\u044c\7]\2\2\u0446\u044d\7A\2\2\u0447")
        buf.write(u"\u0448\7}\2\2\u0448\u0449\5T+\2\u0449\u044a\7\u0088\2")
        buf.write(u"\2\u044a\u044b\5T+\2\u044b\u044d\3\2\2\2\u044c\u0446")
        buf.write(u"\3\2\2\2\u044c\u0447\3\2\2\2\u044d\u044e\3\2\2\2\u044e")
        buf.write(u"\u044f\7\26\2\2\u044f\u0450\5\u009eP\2\u0450\u0453\7")
        buf.write(u"\27\2\2\u0451\u0452\7\u008d\2\2\u0452\u0454\5T+\2\u0453")
        buf.write(u"\u0451\3\2\2\2\u0453\u0454\3\2\2\2\u0454\u0456\3\2\2")
        buf.write(u"\2\u0455\u0438\3\2\2\2\u0455\u043f\3\2\2\2\u0455\u0445")
        buf.write(u"\3\2\2\2\u0456k\3\2\2\2\u0457\u0458\7\u0081\2\2\u0458")
        buf.write(u"\u0459\7\26\2\2\u0459\u045f\5X-\2\u045a\u045b\7\23\2")
        buf.write(u"\2\u045b\u045c\5\u010e\u0088\2\u045c\u045d\7-\2\2\u045d")
        buf.write(u"\u045e\5X-\2\u045e\u0460\3\2\2\2\u045f\u045a\3\2\2\2")
        buf.write(u"\u045f\u0460\3\2\2\2\u0460\u0461\3\2\2\2\u0461\u0462")
        buf.write(u"\7\27\2\2\u0462m\3\2\2\2\u0463\u0464\5\u0108\u0085\2")
        buf.write(u"\u0464\u0465\5\u0114\u008b\2\u0465\u0466\5T+\2\u0466")
        buf.write(u"o\3\2\2\2\u0467\u0468\69%\3\u0468\u0469\7\25\2\2\u0469")
        buf.write(u"\u0470\5\u00acW\2\u046a\u046b\69&\3\u046b\u046c\7\30")
        buf.write(u"\2\2\u046c\u046d\5T+\2\u046d\u046e\7\31\2\2\u046e\u0470")
        buf.write(u"\3\2\2\2\u046f\u0467\3\2\2\2\u046f\u046a\3\2\2\2\u0470")
        buf.write(u"q\3\2\2\2\u0471\u0472\5\u00d4k\2\u0472\u0473\5\u0114")
        buf.write(u"\u008b\2\u0473\u0474\5T+\2\u0474s\3\2\2\2\u0475\u0477")
        buf.write(u"\7\7\2\2\u0476\u0475\3\2\2\2\u0477\u047a\3\2\2\2\u0478")
        buf.write(u"\u0476\3\2\2\2\u0478\u0479\3\2\2\2\u0479u\3\2\2\2\u047a")
        buf.write(u"\u0478\3\2\2\2\u047b\u047d\7\7\2\2\u047c\u047b\3\2\2")
        buf.write(u"\2\u047d\u047e\3\2\2\2\u047e\u047c\3\2\2\2\u047e\u047f")
        buf.write(u"\3\2\2\2\u047fw\3\2\2\2\u0480\u0482\7\7\2\2\u0481\u0480")
        buf.write(u"\3\2\2\2\u0482\u0483\3\2\2\2\u0483\u0481\3\2\2\2\u0483")
        buf.write(u"\u0484\3\2\2\2\u0484\u0485\3\2\2\2\u0485\u0486\7\3\2")
        buf.write(u"\2\u0486y\3\2\2\2\u0487\u0489\7\7\2\2\u0488\u0487\3\2")
        buf.write(u"\2\2\u0489\u048c\3\2\2\2\u048a\u0488\3\2\2\2\u048a\u048b")
        buf.write(u"\3\2\2\2\u048b\u048d\3\2\2\2\u048c\u048a\3\2\2\2\u048d")
        buf.write(u"\u048e\7\4\2\2\u048e{\3\2\2\2\u048f\u0490\7l\2\2\u0490")
        buf.write(u"}\3\2\2\2\u0491\u0493\5\u0080A\2\u0492\u0491\3\2\2\2")
        buf.write(u"\u0492\u0493\3\2\2\2\u0493\u0494\3\2\2\2\u0494\u0495")
        buf.write(u"\5t;\2\u0495\u0496\7\2\2\3\u0496\177\3\2\2\2\u0497\u0498")
        buf.write(u"\bA\1\2\u0498\u0499\5\u0082B\2\u0499\u04a0\3\2\2\2\u049a")
        buf.write(u"\u049b\f\3\2\2\u049b\u049c\5v<\2\u049c\u049d\5\u0082")
        buf.write(u"B\2\u049d\u049f\3\2\2\2\u049e\u049a\3\2\2\2\u049f\u04a2")
        buf.write(u"\3\2\2\2\u04a0\u049e\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1")
        buf.write(u"\u0081\3\2\2\2\u04a2\u04a0\3\2\2\2\u04a3\u04a9\5\n\6")
        buf.write(u"\2\u04a4\u04a9\5\u00a4S\2\u04a5\u04a9\5\u0084C\2\u04a6")
        buf.write(u"\u04a9\5\u0086D\2\u04a7\u04a9\5\u00d6l\2\u04a8\u04a3")
        buf.write(u"\3\2\2\2\u04a8\u04a4\3\2\2\2\u04a8\u04a5\3\2\2\2\u04a8")
        buf.write(u"\u04a6\3\2\2\2\u04a8\u04a7\3\2\2\2\u04a9\u0083\3\2\2")
        buf.write(u"\2\u04aa\u04ab\5\32\16\2\u04ab\u0085\3\2\2\2\u04ac\u04af")
        buf.write(u"\5\2\2\2\u04ad\u04af\5\4\3\2\u04ae\u04ac\3\2\2\2\u04ae")
        buf.write(u"\u04ad\3\2\2\2\u04af\u0087\3\2\2\2\u04b0\u04b1\bE\1\2")
        buf.write(u"\u04b1\u04b2\5\6\4\2\u04b2\u04b9\3\2\2\2\u04b3\u04b4")
        buf.write(u"\f\3\2\2\u04b4\u04b5\5v<\2\u04b5\u04b6\5\6\4\2\u04b6")
        buf.write(u"\u04b8\3\2\2\2\u04b7\u04b3\3\2\2\2\u04b8\u04bb\3\2\2")
        buf.write(u"\2\u04b9\u04b7\3\2\2\2\u04b9\u04ba\3\2\2\2\u04ba\u0089")
        buf.write(u"\3\2\2\2\u04bb\u04b9\3\2\2\2\u04bc\u04bd\bF\1\2\u04bd")
        buf.write(u"\u04be\5\b\5\2\u04be\u04c5\3\2\2\2\u04bf\u04c0\f\3\2")
        buf.write(u"\2\u04c0\u04c1\5v<\2\u04c1\u04c2\5\b\5\2\u04c2\u04c4")
        buf.write(u"\3\2\2\2\u04c3\u04bf\3\2\2\2\u04c4\u04c7\3\2\2\2\u04c5")
        buf.write(u"\u04c3\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6\u008b\3\2\2")
        buf.write(u"\2\u04c7\u04c5\3\2\2\2\u04c8\u04c9\bG\1\2\u04c9\u04ca")
        buf.write(u"\5\u00b0Y\2\u04ca\u04d0\3\2\2\2\u04cb\u04cc\f\3\2\2\u04cc")
        buf.write(u"\u04cd\7\23\2\2\u04cd\u04cf\5\u00b0Y\2\u04ce\u04cb\3")
        buf.write(u"\2\2\2\u04cf\u04d2\3\2\2\2\u04d0\u04ce\3\2\2\2\u04d0")
        buf.write(u"\u04d1\3\2\2\2\u04d1\u008d\3\2\2\2\u04d2\u04d0\3\2\2")
        buf.write(u"\2\u04d3\u04d4\7c\2\2\u04d4\u04de\5\u0090I\2\u04d5\u04d6")
        buf.write(u"\7c\2\2\u04d6\u04de\5\u0092J\2\u04d7\u04d8\7c\2\2\u04d8")
        buf.write(u"\u04de\5\u0096L\2\u04d9\u04da\7f\2\2\u04da\u04de\7\u0099")
        buf.write(u"\2\2\u04db\u04dc\7f\2\2\u04dc\u04de\5T+\2\u04dd\u04d3")
        buf.write(u"\3\2\2\2\u04dd\u04d5\3\2\2\2\u04dd\u04d7\3\2\2\2\u04dd")
        buf.write(u"\u04d9\3\2\2\2\u04dd\u04db\3\2\2\2\u04de\u008f\3\2\2")
        buf.write(u"\2\u04df\u04e1\7\30\2\2\u04e0\u04e2\5\u0094K\2\u04e1")
        buf.write(u"\u04e0\3\2\2\2\u04e1\u04e2\3\2\2\2\u04e2\u04e3\3\2\2")
        buf.write(u"\2\u04e3\u04e4\7\31\2\2\u04e4\u0091\3\2\2\2\u04e5\u04e7")
        buf.write(u"\7*\2\2\u04e6\u04e8\5\u0094K\2\u04e7\u04e6\3\2\2\2\u04e7")
        buf.write(u"\u04e8\3\2\2\2\u04e8\u04e9\3\2\2\2\u04e9\u04ea\7(\2\2")
        buf.write(u"\u04ea\u0093\3\2\2\2\u04eb\u04ec\bK\1\2\u04ec\u04ed\5")
        buf.write(u"T+\2\u04ed\u04f3\3\2\2\2\u04ee\u04ef\f\3\2\2\u04ef\u04f0")
        buf.write(u"\7\23\2\2\u04f0\u04f2\5T+\2\u04f1\u04ee\3\2\2\2\u04f2")
        buf.write(u"\u04f5\3\2\2\2\u04f3\u04f1\3\2\2\2\u04f3\u04f4\3\2\2")
        buf.write(u"\2\u04f4\u0095\3\2\2\2\u04f5\u04f3\3\2\2\2\u04f6\u04f7")
        buf.write(u"\7\30\2\2\u04f7\u04f8\5T+\2\u04f8\u04f9\7\24\2\2\u04f9")
        buf.write(u"\u04fa\5T+\2\u04fa\u04fb\7\31\2\2\u04fb\u0097\3\2\2\2")
        buf.write(u"\u04fc\u04fd\bM\1\2\u04fd\u04fe\5\u009aN\2\u04fe\u0509")
        buf.write(u"\3\2\2\2\u04ff\u0500\f\5\2\2\u0500\u0508\7,\2\2\u0501")
        buf.write(u"\u0502\f\4\2\2\u0502\u0503\7\30\2\2\u0503\u0508\7\31")
        buf.write(u"\2\2\u0504\u0505\f\3\2\2\u0505\u0506\7\32\2\2\u0506\u0508")
        buf.write(u"\7\33\2\2\u0507\u04ff\3\2\2\2\u0507\u0501\3\2\2\2\u0507")
        buf.write(u"\u0504\3\2\2\2\u0508\u050b\3\2\2\2\u0509\u0507\3\2\2")
        buf.write(u"\2\u0509\u050a\3\2\2\2\u050a\u0099\3\2\2\2\u050b\u0509")
        buf.write(u"\3\2\2\2\u050c\u050f\5\u009cO\2\u050d\u050f\5\u009eP")
        buf.write(u"\2\u050e\u050c\3\2\2\2\u050e\u050d\3\2\2\2\u050f\u009b")
        buf.write(u"\3\2\2\2\u0510\u051b\7\64\2\2\u0511\u051b\7\65\2\2\u0512")
        buf.write(u"\u051b\7\66\2\2\u0513\u051b\7\67\2\2\u0514\u051b\78\2")
        buf.write(u"\2\u0515\u051b\79\2\2\u0516\u051b\7;\2\2\u0517\u051b")
        buf.write(u"\7:\2\2\u0518\u051b\7<\2\2\u0519\u051b\7>\2\2\u051a\u0510")
        buf.write(u"\3\2\2\2\u051a\u0511\3\2\2\2\u051a\u0512\3\2\2\2\u051a")
        buf.write(u"\u0513\3\2\2\2\u051a\u0514\3\2\2\2\u051a\u0515\3\2\2")
        buf.write(u"\2\u051a\u0516\3\2\2\2\u051a\u0517\3\2\2\2\u051a\u0518")
        buf.write(u"\3\2\2\2\u051a\u0519\3\2\2\2\u051b\u009d\3\2\2\2\u051c")
        buf.write(u"\u051d\7\u0095\2\2\u051d\u009f\3\2\2\2\u051e\u051f\7")
        buf.write(u">\2\2\u051f\u00a1\3\2\2\2\u0520\u0521\7?\2\2\u0521\u00a3")
        buf.write(u"\3\2\2\2\u0522\u0526\5\f\7\2\u0523\u0526\5\30\r\2\u0524")
        buf.write(u"\u0526\5\16\b\2\u0525\u0522\3\2\2\2\u0525\u0523\3\2\2")
        buf.write(u"\2\u0525\u0524\3\2\2\2\u0526\u00a5\3\2\2\2\u0527\u0528")
        buf.write(u"\bT\1\2\u0528\u0529\5\u00aeX\2\u0529\u052f\3\2\2\2\u052a")
        buf.write(u"\u052b\f\3\2\2\u052b\u052c\7\23\2\2\u052c\u052e\5\u00ae")
        buf.write(u"X\2\u052d\u052a\3\2\2\2\u052e\u0531\3\2\2\2\u052f\u052d")
        buf.write(u"\3\2\2\2\u052f\u0530\3\2\2\2\u0530\u00a7\3\2\2\2\u0531")
        buf.write(u"\u052f\3\2\2\2\u0532\u0535\5\u00acW\2\u0533\u0535\5\u00ae")
        buf.write(u"X\2\u0534\u0532\3\2\2\2\u0534\u0533\3\2\2\2\u0535\u00a9")
        buf.write(u"\3\2\2\2\u0536\u053a\5\u00acW\2\u0537\u053a\5\u00aeX")
        buf.write(u"\2\u0538\u053a\5\u00b0Y\2\u0539\u0536\3\2\2\2\u0539\u0537")
        buf.write(u"\3\2\2\2\u0539\u0538\3\2\2\2\u053a\u00ab\3\2\2\2\u053b")
        buf.write(u"\u053c\7\u0096\2\2\u053c\u00ad\3\2\2\2\u053d\u053e\7")
        buf.write(u"\u0095\2\2\u053e\u00af\3\2\2\2\u053f\u0540\7\u0094\2")
        buf.write(u"\2\u0540\u00b1\3\2\2\2\u0541\u0542\bZ\1\2\u0542\u0543")
        buf.write(u"\5\u00b4[\2\u0543\u0549\3\2\2\2\u0544\u0545\f\3\2\2\u0545")
        buf.write(u"\u0546\7\23\2\2\u0546\u0548\5\u00b4[\2\u0547\u0544\3")
        buf.write(u"\2\2\2\u0548\u054b\3\2\2\2\u0549\u0547\3\2\2\2\u0549")
        buf.write(u"\u054a\3\2\2\2\u054a\u00b3\3\2\2\2\u054b\u0549\3\2\2")
        buf.write(u"\2\u054c\u0552\5\u00ba^\2\u054d\u054f\7j\2\2\u054e\u054d")
        buf.write(u"\3\2\2\2\u054e\u054f\3\2\2\2\u054f\u0550\3\2\2\2\u0550")
        buf.write(u"\u0552\5\u00b6\\\2\u0551\u054c\3\2\2\2\u0551\u054e\3")
        buf.write(u"\2\2\2\u0552\u00b5\3\2\2\2\u0553\u0556\5\u00b8]\2\u0554")
        buf.write(u"\u0556\5,\27\2\u0555\u0553\3\2\2\2\u0555\u0554\3\2\2")
        buf.write(u"\2\u0556\u00b7\3\2\2\2\u0557\u055a\5\u00acW\2\u0558\u0559")
        buf.write(u"\7-\2\2\u0559\u055b\5\u00f6|\2\u055a\u0558\3\2\2\2\u055a")
        buf.write(u"\u055b\3\2\2\2\u055b\u00b9\3\2\2\2\u055c\u055d\5\u00a0")
        buf.write(u"Q\2\u055d\u055e\5\u00acW\2\u055e\u00bb\3\2\2\2\u055f")
        buf.write(u"\u0562\5\u0098M\2\u0560\u0562\5\u00be`\2\u0561\u055f")
        buf.write(u"\3\2\2\2\u0561\u0560\3\2\2\2\u0562\u00bd\3\2\2\2\u0563")
        buf.write(u"\u0564\b`\1\2\u0564\u0565\7D\2\2\u0565\u056e\3\2\2\2")
        buf.write(u"\u0566\u0567\f\4\2\2\u0567\u0568\7\30\2\2\u0568\u056d")
        buf.write(u"\7\31\2\2\u0569\u056a\f\3\2\2\u056a\u056b\7\32\2\2\u056b")
        buf.write(u"\u056d\7\33\2\2\u056c\u0566\3\2\2\2\u056c\u0569\3\2\2")
        buf.write(u"\2\u056d\u0570\3\2\2\2\u056e\u056c\3\2\2\2\u056e\u056f")
        buf.write(u"\3\2\2\2\u056f\u00bf\3\2\2\2\u0570\u056e\3\2\2\2\u0571")
        buf.write(u"\u0572\ba\1\2\u0572\u0573\5\u00c2b\2\u0573\u057a\3\2")
        buf.write(u"\2\2\u0574\u0575\f\3\2\2\u0575\u0576\5v<\2\u0576\u0577")
        buf.write(u"\5\u00c2b\2\u0577\u0579\3\2\2\2\u0578\u0574\3\2\2\2\u0579")
        buf.write(u"\u057c\3\2\2\2\u057a\u0578\3\2\2\2\u057a\u057b\3\2\2")
        buf.write(u"\2\u057b\u00c1\3\2\2\2\u057c\u057a\3\2\2\2\u057d\u0583")
        buf.write(u"\5\24\13\2\u057e\u0583\5\26\f\2\u057f\u0583\5$\23\2\u0580")
        buf.write(u"\u0583\5\"\22\2\u0581\u0583\5\22\n\2\u0582\u057d\3\2")
        buf.write(u"\2\2\u0582\u057e\3\2\2\2\u0582\u057f\3\2\2\2\u0582\u0580")
        buf.write(u"\3\2\2\2\u0582\u0581\3\2\2\2\u0583\u00c3\3\2\2\2\u0584")
        buf.write(u"\u0585\bc\1\2\u0585\u0586\5\u00c6d\2\u0586\u058d\3\2")
        buf.write(u"\2\2\u0587\u0588\f\3\2\2\u0588\u0589\5v<\2\u0589\u058a")
        buf.write(u"\5\u00c6d\2\u058a\u058c\3\2\2\2\u058b\u0587\3\2\2\2\u058c")
        buf.write(u"\u058f\3\2\2\2\u058d\u058b\3\2\2\2\u058d\u058e\3\2\2")
        buf.write(u"\2\u058e\u00c5\3\2\2\2\u058f\u058d\3\2\2\2\u0590\u0593")
        buf.write(u"\5\u00c2b\2\u0591\u0593\5&\24\2\u0592\u0590\3\2\2\2\u0592")
        buf.write(u"\u0591\3\2\2\2\u0593\u00c7\3\2\2\2\u0594\u0595\7\13\2")
        buf.write(u"\2\u0595\u059f\5\u0162\u00b2\2\u0596\u0597\7\f\2\2\u0597")
        buf.write(u"\u059f\5\u017a\u00be\2\u0598\u0599\7\r\2\2\u0599\u059f")
        buf.write(u"\5\u00caf\2\u059a\u059b\7\16\2\2\u059b\u059f\5\u00ca")
        buf.write(u"f\2\u059c\u059d\7\17\2\2\u059d\u059f\5\u00d0i\2\u059e")
        buf.write(u"\u0594\3\2\2\2\u059e\u0596\3\2\2\2\u059e\u0598\3\2\2")
        buf.write(u"\2\u059e\u059a\3\2\2\2\u059e\u059c\3\2\2\2\u059f\u00c9")
        buf.write(u"\3\2\2\2\u05a0\u05a2\5\u00aaV\2\u05a1\u05a3\5\u00ccg")
        buf.write(u"\2\u05a2\u05a1\3\2\2\2\u05a2\u05a3\3\2\2\2\u05a3\u00cb")
        buf.write(u"\3\2\2\2\u05a4\u05a5\7`\2\2\u05a5\u05a6\5\u00ceh\2\u05a6")
        buf.write(u"\u05a7\7\21\2\2\u05a7\u05ac\5\u00aaV\2\u05a8\u05a9\7")
        buf.write(u"\25\2\2\u05a9\u05ab\5\u00aaV\2\u05aa\u05a8\3\2\2\2\u05ab")
        buf.write(u"\u05ae\3\2\2\2\u05ac\u05aa\3\2\2\2\u05ac\u05ad\3\2\2")
        buf.write(u"\2\u05ad\u00cd\3\2\2\2\u05ae\u05ac\3\2\2\2\u05af\u05b0")
        buf.write(u"\7\u0096\2\2\u05b0\u05b1\6h\65\3\u05b1\u00cf\3\2\2\2")
        buf.write(u"\u05b2\u05b4\5\u00aaV\2\u05b3\u05b5\5\u00d2j\2\u05b4")
        buf.write(u"\u05b3\3\2\2\2\u05b4\u05b5\3\2\2\2\u05b5\u00d1\3\2\2")
        buf.write(u"\2\u05b6\u05b7\7`\2\2\u05b7\u05b8\5\u00ceh\2\u05b8\u05ba")
        buf.write(u"\7\21\2\2\u05b9\u05bb\7%\2\2\u05ba\u05b9\3\2\2\2\u05ba")
        buf.write(u"\u05bb\3\2\2\2\u05bb\u05bc\3\2\2\2\u05bc\u05c1\5\u0134")
        buf.write(u"\u009b\2\u05bd\u05be\7%\2\2\u05be\u05c0\5\u0134\u009b")
        buf.write(u"\2\u05bf\u05bd\3\2\2\2\u05c0\u05c3\3\2\2\2\u05c1\u05bf")
        buf.write(u"\3\2\2\2\u05c1\u05c2\3\2\2\2\u05c2\u05c6\3\2\2\2\u05c3")
        buf.write(u"\u05c1\3\2\2\2\u05c4\u05c5\7\25\2\2\u05c5\u05c7\5\u0134")
        buf.write(u"\u009b\2\u05c6\u05c4\3\2\2\2\u05c6\u05c7\3\2\2\2\u05c7")
        buf.write(u"\u00d3\3\2\2\2\u05c8\u05c9\bk\1\2\u05c9\u05ca\5\u00ac")
        buf.write(u"W\2\u05ca\u05d0\3\2\2\2\u05cb\u05cc\f\3\2\2\u05cc\u05cd")
        buf.write(u"\7\23\2\2\u05cd\u05cf\5\u00acW\2\u05ce\u05cb\3\2\2\2")
        buf.write(u"\u05cf\u05d2\3\2\2\2\u05d0\u05ce\3\2\2\2\u05d0\u05d1")
        buf.write(u"\3\2\2\2\u05d1\u00d5\3\2\2\2\u05d2\u05d0\3\2\2\2\u05d3")
        buf.write(u"\u05d8\5\"\22\2\u05d4\u05d8\5$\23\2\u05d5\u05d8\5&\24")
        buf.write(u"\2\u05d6\u05d8\5(\25\2\u05d7\u05d3\3\2\2\2\u05d7\u05d4")
        buf.write(u"\3\2\2\2\u05d7\u05d5\3\2\2\2\u05d7\u05d6\3\2\2\2\u05d8")
        buf.write(u"\u00d7\3\2\2\2\u05d9\u05da\7\n\2\2\u05da\u00d9\3\2\2")
        buf.write(u"\2\u05db\u05dc\bn\1\2\u05dc\u05dd\5\u00dco\2\u05dd\u05e4")
        buf.write(u"\3\2\2\2\u05de\u05df\f\3\2\2\u05df\u05e0\5v<\2\u05e0")
        buf.write(u"\u05e1\5\u00dco\2\u05e1\u05e3\3\2\2\2\u05e2\u05de\3\2")
        buf.write(u"\2\2\u05e3\u05e6\3\2\2\2\u05e4\u05e2\3\2\2\2\u05e4\u05e5")
        buf.write(u"\3\2\2\2\u05e5\u00db\3\2\2\2\u05e6\u05e4\3\2\2\2\u05e7")
        buf.write(u"\u05e8\7\13\2\2\u05e8\u05f2\5\u014e\u00a8\2\u05e9\u05ea")
        buf.write(u"\7\f\2\2\u05ea\u05f2\5\u0168\u00b5\2\u05eb\u05ec\7\r")
        buf.write(u"\2\2\u05ec\u05f2\5\u00dep\2\u05ed\u05ee\7\16\2\2\u05ee")
        buf.write(u"\u05f2\5\u00dep\2\u05ef\u05f0\7\17\2\2\u05f0\u05f2\5")
        buf.write(u"\u00e0q\2\u05f1\u05e7\3\2\2\2\u05f1\u05e9\3\2\2\2\u05f1")
        buf.write(u"\u05eb\3\2\2\2\u05f1\u05ed\3\2\2\2\u05f1\u05ef\3\2\2")
        buf.write(u"\2\u05f2\u00dd\3\2\2\2\u05f3\u05f5\5\u0136\u009c\2\u05f4")
        buf.write(u"\u05f6\7\22\2\2\u05f5\u05f4\3\2\2\2\u05f5\u05f6\3\2\2")
        buf.write(u"\2\u05f6\u05f8\3\2\2\2\u05f7\u05f9\5\u00ccg\2\u05f8\u05f7")
        buf.write(u"\3\2\2\2\u05f8\u05f9\3\2\2\2\u05f9\u00df\3\2\2\2\u05fa")
        buf.write(u"\u05fc\5\u011e\u0090\2\u05fb\u05fd\7\22\2\2\u05fc\u05fb")
        buf.write(u"\3\2\2\2\u05fc\u05fd\3\2\2\2\u05fd\u05ff\3\2\2\2\u05fe")
        buf.write(u"\u0600\5\u00d2j\2\u05ff\u05fe\3\2\2\2\u05ff\u0600\3\2")
        buf.write(u"\2\2\u0600\u00e1\3\2\2\2\u0601\u0602\br\1\2\u0602\u0603")
        buf.write(u"\5.\30\2\u0603\u060a\3\2\2\2\u0604\u0605\f\3\2\2\u0605")
        buf.write(u"\u0606\5v<\2\u0606\u0607\5.\30\2\u0607\u0609\3\2\2\2")
        buf.write(u"\u0608\u0604\3\2\2\2\u0609\u060c\3\2\2\2\u060a\u0608")
        buf.write(u"\3\2\2\2\u060a\u060b\3\2\2\2\u060b\u00e3\3\2\2\2\u060c")
        buf.write(u"\u060a\3\2\2\2\u060d\u060e\bs\1\2\u060e\u060f\5*\26\2")
        buf.write(u"\u060f\u0616\3\2\2\2\u0610\u0611\f\3\2\2\u0611\u0612")
        buf.write(u"\5v<\2\u0612\u0613\5*\26\2\u0613\u0615\3\2\2\2\u0614")
        buf.write(u"\u0610\3\2\2\2\u0615\u0618\3\2\2\2\u0616\u0614\3\2\2")
        buf.write(u"\2\u0616\u0617\3\2\2\2\u0617\u00e5\3\2\2\2\u0618\u0616")
        buf.write(u"\3\2\2\2\u0619\u061a\bt\1\2\u061a\u061b\5@!\2\u061b\u0622")
        buf.write(u"\3\2\2\2\u061c\u061d\f\3\2\2\u061d\u061e\5v<\2\u061e")
        buf.write(u"\u061f\5@!\2\u061f\u0621\3\2\2\2\u0620\u061c\3\2\2\2")
        buf.write(u"\u0621\u0624\3\2\2\2\u0622\u0620\3\2\2\2\u0622\u0623")
        buf.write(u"\3\2\2\2\u0623\u00e7\3\2\2\2\u0624\u0622\3\2\2\2\u0625")
        buf.write(u"\u0626\bu\1\2\u0626\u0627\5P)\2\u0627\u062e\3\2\2\2\u0628")
        buf.write(u"\u0629\f\3\2\2\u0629\u062a\5v<\2\u062a\u062b\5P)\2\u062b")
        buf.write(u"\u062d\3\2\2\2\u062c\u0628\3\2\2\2\u062d\u0630\3\2\2")
        buf.write(u"\2\u062e\u062c\3\2\2\2\u062e\u062f\3\2\2\2\u062f\u00e9")
        buf.write(u"\3\2\2\2\u0630\u062e\3\2\2\2\u0631\u0632\7\30\2\2\u0632")
        buf.write(u"\u0633\5\u00ecw\2\u0633\u0634\7\24\2\2\u0634\u0635\5")
        buf.write(u"\u00ecw\2\u0635\u0636\7\31\2\2\u0636\u0640\3\2\2\2\u0637")
        buf.write(u"\u0638\7\30\2\2\u0638\u0639\5\u00eex\2\u0639\u063a\7")
        buf.write(u"\31\2\2\u063a\u0640\3\2\2\2\u063b\u063c\7*\2\2\u063c")
        buf.write(u"\u063d\5\u00eex\2\u063d\u063e\7(\2\2\u063e\u0640\3\2")
        buf.write(u"\2\2\u063f\u0631\3\2\2\2\u063f\u0637\3\2\2\2\u063f\u063b")
        buf.write(u"\3\2\2\2\u0640\u00eb\3\2\2\2\u0641\u064f\7\u0092\2\2")
        buf.write(u"\u0642\u064f\7\u0093\2\2\u0643\u064f\7\u009a\2\2\u0644")
        buf.write(u"\u064f\7\u009b\2\2\u0645\u064f\7\u0091\2\2\u0646\u064f")
        buf.write(u"\7\u009f\2\2\u0647\u064f\7\u009e\2\2\u0648\u064f\7\u0099")
        buf.write(u"\2\2\u0649\u064f\7\u009c\2\2\u064a\u064f\7\u009d\2\2")
        buf.write(u"\u064b\u064f\7\u0090\2\2\u064c\u064f\7\u00a0\2\2\u064d")
        buf.write(u"\u064f\5|?\2\u064e\u0641\3\2\2\2\u064e\u0642\3\2\2\2")
        buf.write(u"\u064e\u0643\3\2\2\2\u064e\u0644\3\2\2\2\u064e\u0645")
        buf.write(u"\3\2\2\2\u064e\u0646\3\2\2\2\u064e\u0647\3\2\2\2\u064e")
        buf.write(u"\u0648\3\2\2\2\u064e\u0649\3\2\2\2\u064e\u064a\3\2\2")
        buf.write(u"\2\u064e\u064b\3\2\2\2\u064e\u064c\3\2\2\2\u064e\u064d")
        buf.write(u"\3\2\2\2\u064f\u00ed\3\2\2\2\u0650\u0651\bx\1\2\u0651")
        buf.write(u"\u0652\5\u00ecw\2\u0652\u0658\3\2\2\2\u0653\u0654\f\3")
        buf.write(u"\2\2\u0654\u0655\7\23\2\2\u0655\u0657\5\u00ecw\2\u0656")
        buf.write(u"\u0653\3\2\2\2\u0657\u065a\3\2\2\2\u0658\u0656\3\2\2")
        buf.write(u"\2\u0658\u0659\3\2\2\2\u0659\u00ef\3\2\2\2\u065a\u0658")
        buf.write(u"\3\2\2\2\u065b\u0660\5\u00f4{\2\u065c\u0660\5\u00f6|")
        buf.write(u"\2\u065d\u0660\5\u00aaV\2\u065e\u0660\5\u00f2z\2\u065f")
        buf.write(u"\u065b\3\2\2\2\u065f\u065c\3\2\2\2\u065f\u065d\3\2\2")
        buf.write(u"\2\u065f\u065e\3\2\2\2\u0660\u00f1\3\2\2\2\u0661\u0662")
        buf.write(u"\t\4\2\2\u0662\u00f3\3\2\2\2\u0663\u0664\7\26\2\2\u0664")
        buf.write(u"\u0665\5T+\2\u0665\u0666\7\27\2\2\u0666\u00f5\3\2\2\2")
        buf.write(u"\u0667\u066a\5\u00ecw\2\u0668\u066a\5\u00f8}\2\u0669")
        buf.write(u"\u0667\3\2\2\2\u0669\u0668\3\2\2\2\u066a\u00f7\3\2\2")
        buf.write(u"\2\u066b\u0671\5\u0096L\2\u066c\u0671\5\u0090I\2\u066d")
        buf.write(u"\u0671\5\u0092J\2\u066e\u0671\5\u00fc\177\2\u066f\u0671")
        buf.write(u"\5\u00fa~\2\u0670\u066b\3\2\2\2\u0670\u066c\3\2\2\2\u0670")
        buf.write(u"\u066d\3\2\2\2\u0670\u066e\3\2\2\2\u0670\u066f\3\2\2")
        buf.write(u"\2\u0671\u00f9\3\2\2\2\u0672\u0674\7\26\2\2\u0673\u0675")
        buf.write(u"\5\u00fe\u0080\2\u0674\u0673\3\2\2\2\u0674\u0675\3\2")
        buf.write(u"\2\2\u0675\u0676\3\2\2\2\u0676\u0677\7\27\2\2\u0677\u00fb")
        buf.write(u"\3\2\2\2\u0678\u067a\7\32\2\2\u0679\u067b\5\u0100\u0081")
        buf.write(u"\2\u067a\u0679\3\2\2\2\u067a\u067b\3\2\2\2\u067b\u067c")
        buf.write(u"\3\2\2\2\u067c\u067d\7\33\2\2\u067d\u00fd\3\2\2\2\u067e")
        buf.write(u"\u067f\b\u0080\1\2\u067f\u0680\5T+\2\u0680\u0686\3\2")
        buf.write(u"\2\2\u0681\u0682\f\3\2\2\u0682\u0683\7\23\2\2\u0683\u0685")
        buf.write(u"\5T+\2\u0684\u0681\3\2\2\2\u0685\u0688\3\2\2\2\u0686")
        buf.write(u"\u0684\3\2\2\2\u0686\u0687\3\2\2\2\u0687\u00ff\3\2\2")
        buf.write(u"\2\u0688\u0686\3\2\2\2\u0689\u068a\b\u0081\1\2\u068a")
        buf.write(u"\u068b\5\u0102\u0082\2\u068b\u0691\3\2\2\2\u068c\u068d")
        buf.write(u"\f\3\2\2\u068d\u068e\7\23\2\2\u068e\u0690\5\u0102\u0082")
        buf.write(u"\2\u068f\u068c\3\2\2\2\u0690\u0693\3\2\2\2\u0691\u068f")
        buf.write(u"\3\2\2\2\u0691\u0692\3\2\2\2\u0692\u0101\3\2\2\2\u0693")
        buf.write(u"\u0691\3\2\2\2\u0694\u0695\5T+\2\u0695\u0696\7\21\2\2")
        buf.write(u"\u0696\u0697\5T+\2\u0697\u0103\3\2\2\2\u0698\u0699\5")
        buf.write(u"T+\2\u0699\u069a\7\21\2\2\u069a\u069b\5T+\2\u069b\u06a2")
        buf.write(u"\3\2\2\2\u069c\u069d\5T+\2\u069d\u069e\7\21\2\2\u069e")
        buf.write(u"\u06a2\3\2\2\2\u069f\u06a0\7\21\2\2\u06a0\u06a2\5T+\2")
        buf.write(u"\u06a1\u0698\3\2\2\2\u06a1\u069c\3\2\2\2\u06a1\u069f")
        buf.write(u"\3\2\2\2\u06a2\u0105\3\2\2\2\u06a3\u06a4\5\u00acW\2\u06a4")
        buf.write(u"\u06a5\5\u0114\u008b\2\u06a5\u06a6\5T+\2\u06a6\u0107")
        buf.write(u"\3\2\2\2\u06a7\u06a8\b\u0085\1\2\u06a8\u06a9\5\u00ac")
        buf.write(u"W\2\u06a9\u06ae\3\2\2\2\u06aa\u06ab\f\3\2\2\u06ab\u06ad")
        buf.write(u"\5p9\2\u06ac\u06aa\3\2\2\2\u06ad\u06b0\3\2\2\2\u06ae")
        buf.write(u"\u06ac\3\2\2\2\u06ae\u06af\3\2\2\2\u06af\u0109\3\2\2")
        buf.write(u"\2\u06b0\u06ae\3\2\2\2\u06b1\u06b2\6\u0086@\3\u06b2\u06b3")
        buf.write(u"\7\u0096\2\2\u06b3\u06b6\5\u00bc_\2\u06b4\u06b6\5T+\2")
        buf.write(u"\u06b5\u06b1\3\2\2\2\u06b5\u06b4\3\2\2\2\u06b6\u010b")
        buf.write(u"\3\2\2\2\u06b7\u06be\7\"\2\2\u06b8\u06be\7#\2\2\u06b9")
        buf.write(u"\u06be\5\u0116\u008c\2\u06ba\u06be\5\u0118\u008d\2\u06bb")
        buf.write(u"\u06be\5\u011a\u008e\2\u06bc\u06be\5\u011c\u008f\2\u06bd")
        buf.write(u"\u06b7\3\2\2\2\u06bd\u06b8\3\2\2\2\u06bd\u06b9\3\2\2")
        buf.write(u"\2\u06bd\u06ba\3\2\2\2\u06bd\u06bb\3\2\2\2\u06bd\u06bc")
        buf.write(u"\3\2\2\2\u06be\u010d\3\2\2\2\u06bf\u06c0\7\u0096\2\2")
        buf.write(u"\u06c0\u06c1\6\u0088A\3\u06c1\u010f\3\2\2\2\u06c2\u06c3")
        buf.write(u"\7\u0096\2\2\u06c3\u06c4\6\u0089B\3\u06c4\u0111\3\2\2")
        buf.write(u"\2\u06c5\u06c6\7\u0096\2\2\u06c6\u06c7\6\u008aC\3\u06c7")
        buf.write(u"\u0113\3\2\2\2\u06c8\u06c9\7-\2\2\u06c9\u0115\3\2\2\2")
        buf.write(u"\u06ca\u06cb\7$\2\2\u06cb\u0117\3\2\2\2\u06cc\u06cd\7")
        buf.write(u"%\2\2\u06cd\u0119\3\2\2\2\u06ce\u06cf\7&\2\2\u06cf\u011b")
        buf.write(u"\3\2\2\2\u06d0\u06d1\t\5\2\2\u06d1\u011d\3\2\2\2\u06d2")
        buf.write(u"\u06d3\7{\2\2\u06d3\u06d4\5\u0120\u0091\2\u06d4\u06d5")
        buf.write(u"\7\22\2\2\u06d5\u06da\3\2\2\2\u06d6\u06d7\5\u0120\u0091")
        buf.write(u"\2\u06d7\u06d8\7\22\2\2\u06d8\u06da\3\2\2\2\u06d9\u06d2")
        buf.write(u"\3\2\2\2\u06d9\u06d6\3\2\2\2\u06da\u011f\3\2\2\2\u06db")
        buf.write(u"\u06dc\b\u0091\1\2\u06dc\u06dd\5\u0122\u0092\2\u06dd")
        buf.write(u"\u06e2\3\2\2\2\u06de\u06df\f\3\2\2\u06df\u06e1\5\u0126")
        buf.write(u"\u0094\2\u06e0\u06de\3\2\2\2\u06e1\u06e4\3\2\2\2\u06e2")
        buf.write(u"\u06e0\3\2\2\2\u06e2\u06e3\3\2\2\2\u06e3\u0121\3\2\2")
        buf.write(u"\2\u06e4\u06e2\3\2\2\2\u06e5\u06ec\5\u0124\u0093\2\u06e6")
        buf.write(u"\u06ec\5\u012e\u0098\2\u06e7\u06ec\5\u0130\u0099\2\u06e8")
        buf.write(u"\u06ec\5\u0132\u009a\2\u06e9\u06ec\5\u0128\u0095\2\u06ea")
        buf.write(u"\u06ec\5\u012c\u0097\2\u06eb\u06e5\3\2\2\2\u06eb\u06e6")
        buf.write(u"\3\2\2\2\u06eb\u06e7\3\2\2\2\u06eb\u06e8\3\2\2\2\u06eb")
        buf.write(u"\u06e9\3\2\2\2\u06eb\u06ea\3\2\2\2\u06ec\u0123\3\2\2")
        buf.write(u"\2\u06ed\u06ee\5\u00f2z\2\u06ee\u0125\3\2\2\2\u06ef\u06f0")
        buf.write(u"\7\25\2\2\u06f0\u06f5\5\u0128\u0095\2\u06f1\u06f2\7\25")
        buf.write(u"\2\2\u06f2\u06f5\5\u0134\u009b\2\u06f3\u06f5\5\u012c")
        buf.write(u"\u0097\2\u06f4\u06ef\3\2\2\2\u06f4\u06f1\3\2\2\2\u06f4")
        buf.write(u"\u06f3\3\2\2\2\u06f5\u0127\3\2\2\2\u06f6\u06f7\5\u0134")
        buf.write(u"\u009b\2\u06f7\u06f9\7\26\2\2\u06f8\u06fa\5\u012a\u0096")
        buf.write(u"\2\u06f9\u06f8\3\2\2\2\u06f9\u06fa\3\2\2\2\u06fa\u06fb")
        buf.write(u"\3\2\2\2\u06fb\u06fc\7\27\2\2\u06fc\u0129\3\2\2\2\u06fd")
        buf.write(u"\u06fe\b\u0096\1\2\u06fe\u06ff\5\u0120\u0091\2\u06ff")
        buf.write(u"\u0705\3\2\2\2\u0700\u0701\f\3\2\2\u0701\u0702\7\23\2")
        buf.write(u"\2\u0702\u0704\5\u0120\u0091\2\u0703\u0700\3\2\2\2\u0704")
        buf.write(u"\u0707\3\2\2\2\u0705\u0703\3\2\2\2\u0705\u0706\3\2\2")
        buf.write(u"\2\u0706\u012b\3\2\2\2\u0707\u0705\3\2\2\2\u0708\u0709")
        buf.write(u"\7\30\2\2\u0709\u070a\5\u0120\u0091\2\u070a\u070b\7\31")
        buf.write(u"\2\2\u070b\u012d\3\2\2\2\u070c\u070d\7\26\2\2\u070d\u070e")
        buf.write(u"\5\u0120\u0091\2\u070e\u070f\7\27\2\2\u070f\u012f\3\2")
        buf.write(u"\2\2\u0710\u0711\5\u0134\u009b\2\u0711\u0131\3\2\2\2")
        buf.write(u"\u0712\u0718\7\u009a\2\2\u0713\u0718\7\u009c\2\2\u0714")
        buf.write(u"\u0718\7\u0099\2\2\u0715\u0718\7\u0090\2\2\u0716\u0718")
        buf.write(u"\7\u0091\2\2\u0717\u0712\3\2\2\2\u0717\u0713\3\2\2\2")
        buf.write(u"\u0717\u0714\3\2\2\2\u0717\u0715\3\2\2\2\u0717\u0716")
        buf.write(u"\3\2\2\2\u0718\u0133\3\2\2\2\u0719\u071a\t\6\2\2\u071a")
        buf.write(u"\u0135\3\2\2\2\u071b\u071c\7{\2\2\u071c\u071f\5\u0138")
        buf.write(u"\u009d\2\u071d\u071f\5\u0138\u009d\2\u071e\u071b\3\2")
        buf.write(u"\2\2\u071e\u071d\3\2\2\2\u071f\u0137\3\2\2\2\u0720\u0721")
        buf.write(u"\b\u009d\1\2\u0721\u0722\5\u013a\u009e\2\u0722\u0727")
        buf.write(u"\3\2\2\2\u0723\u0724\f\3\2\2\u0724\u0726\5\u013c\u009f")
        buf.write(u"\2\u0725\u0723\3\2\2\2\u0726\u0729\3\2\2\2\u0727\u0725")
        buf.write(u"\3\2\2\2\u0727\u0728\3\2\2\2\u0728\u0139\3\2\2\2\u0729")
        buf.write(u"\u0727\3\2\2\2\u072a\u072f\5\u0146\u00a4\2\u072b\u072f")
        buf.write(u"\5\u0148\u00a5\2\u072c\u072f\5\u014a\u00a6\2\u072d\u072f")
        buf.write(u"\5\u013e\u00a0\2\u072e\u072a\3\2\2\2\u072e\u072b\3\2")
        buf.write(u"\2\2\u072e\u072c\3\2\2\2\u072e\u072d\3\2\2\2\u072f\u013b")
        buf.write(u"\3\2\2\2\u0730\u0731\7\25\2\2\u0731\u0737\5\u013e\u00a0")
        buf.write(u"\2\u0732\u0733\7\30\2\2\u0733\u0734\5\u0138\u009d\2\u0734")
        buf.write(u"\u0735\7\31\2\2\u0735\u0737\3\2\2\2\u0736\u0730\3\2\2")
        buf.write(u"\2\u0736\u0732\3\2\2\2\u0737\u013d\3\2\2\2\u0738\u0739")
        buf.write(u"\5\u014c\u00a7\2\u0739\u073b\7\26\2\2\u073a\u073c\5\u0140")
        buf.write(u"\u00a1\2\u073b\u073a\3\2\2\2\u073b\u073c\3\2\2\2\u073c")
        buf.write(u"\u073d\3\2\2\2\u073d\u073e\7\27\2\2\u073e\u013f\3\2\2")
        buf.write(u"\2\u073f\u0746\5\u0142\u00a2\2\u0740\u0746\5\u0144\u00a3")
        buf.write(u"\2\u0741\u0742\5\u0142\u00a2\2\u0742\u0743\7\23\2\2\u0743")
        buf.write(u"\u0744\5\u0144\u00a3\2\u0744\u0746\3\2\2\2\u0745\u073f")
        buf.write(u"\3\2\2\2\u0745\u0740\3\2\2\2\u0745\u0741\3\2\2\2\u0746")
        buf.write(u"\u0141\3\2\2\2\u0747\u0748\b\u00a2\1\2\u0748\u0749\5")
        buf.write(u"\u0138\u009d\2\u0749\u074f\3\2\2\2\u074a\u074b\f\3\2")
        buf.write(u"\2\u074b\u074c\7\23\2\2\u074c\u074e\5\u0138\u009d\2\u074d")
        buf.write(u"\u074a\3\2\2\2\u074e\u0751\3\2\2\2\u074f\u074d\3\2\2")
        buf.write(u"\2\u074f\u0750\3\2\2\2\u0750\u0143\3\2\2\2\u0751\u074f")
        buf.write(u"\3\2\2\2\u0752\u0753\b\u00a3\1\2\u0753\u0754\5\u014c")
        buf.write(u"\u00a7\2\u0754\u0755\7-\2\2\u0755\u0756\5\u0138\u009d")
        buf.write(u"\2\u0756\u075f\3\2\2\2\u0757\u0758\f\3\2\2\u0758\u0759")
        buf.write(u"\7\23\2\2\u0759\u075a\5\u014c\u00a7\2\u075a\u075b\7-")
        buf.write(u"\2\2\u075b\u075c\5\u0138\u009d\2\u075c\u075e\3\2\2\2")
        buf.write(u"\u075d\u0757\3\2\2\2\u075e\u0761\3\2\2\2\u075f\u075d")
        buf.write(u"\3\2\2\2\u075f\u0760\3\2\2\2\u0760\u0145\3\2\2\2\u0761")
        buf.write(u"\u075f\3\2\2\2\u0762\u0763\7\26\2\2\u0763\u0764\5\u0138")
        buf.write(u"\u009d\2\u0764\u0765\7\27\2\2\u0765\u0147\3\2\2\2\u0766")
        buf.write(u"\u0767\b\u00a5\1\2\u0767\u076a\7\u0098\2\2\u0768\u076a")
        buf.write(u"\5\u014c\u00a7\2\u0769\u0766\3\2\2\2\u0769\u0768\3\2")
        buf.write(u"\2\2\u076a\u0770\3\2\2\2\u076b\u076c\f\3\2\2\u076c\u076d")
        buf.write(u"\7\25\2\2\u076d\u076f\5\u014c\u00a7\2\u076e\u076b\3\2")
        buf.write(u"\2\2\u076f\u0772\3\2\2\2\u0770\u076e\3\2\2\2\u0770\u0771")
        buf.write(u"\3\2\2\2\u0771\u0149\3\2\2\2\u0772\u0770\3\2\2\2\u0773")
        buf.write(u"\u0779\7\u009a\2\2\u0774\u0779\7\u009c\2\2\u0775\u0779")
        buf.write(u"\7\u0099\2\2\u0776\u0779\7\u0090\2\2\u0777\u0779\7\u0091")
        buf.write(u"\2\2\u0778\u0773\3\2\2\2\u0778\u0774\3\2\2\2\u0778\u0775")
        buf.write(u"\3\2\2\2\u0778\u0776\3\2\2\2\u0778\u0777\3\2\2\2\u0779")
        buf.write(u"\u014b\3\2\2\2\u077a\u077b\t\7\2\2\u077b\u014d\3\2\2")
        buf.write(u"\2\u077c\u077d\7{\2\2\u077d\u077e\5\u0150\u00a9\2\u077e")
        buf.write(u"\u077f\7\22\2\2\u077f\u0784\3\2\2\2\u0780\u0781\5\u0150")
        buf.write(u"\u00a9\2\u0781\u0782\7\22\2\2\u0782\u0784\3\2\2\2\u0783")
        buf.write(u"\u077c\3\2\2\2\u0783\u0780\3\2\2\2\u0784\u014f\3\2\2")
        buf.write(u"\2\u0785\u0786\b\u00a9\1\2\u0786\u0787\5\u0152\u00aa")
        buf.write(u"\2\u0787\u078c\3\2\2\2\u0788\u0789\f\3\2\2\u0789\u078b")
        buf.write(u"\5\u0156\u00ac\2\u078a\u0788\3\2\2\2\u078b\u078e\3\2")
        buf.write(u"\2\2\u078c\u078a\3\2\2\2\u078c\u078d\3\2\2\2\u078d\u0151")
        buf.write(u"\3\2\2\2\u078e\u078c\3\2\2\2\u078f\u0794\5\u0154\u00ab")
        buf.write(u"\2\u0790\u0794\5\u015e\u00b0\2\u0791\u0794\5\u0160\u00b1")
        buf.write(u"\2\u0792\u0794\5\u0164\u00b3\2\u0793\u078f\3\2\2\2\u0793")
        buf.write(u"\u0790\3\2\2\2\u0793\u0791\3\2\2\2\u0793\u0792\3\2\2")
        buf.write(u"\2\u0794\u0153\3\2\2\2\u0795\u0796\5\u00f2z\2\u0796\u0155")
        buf.write(u"\3\2\2\2\u0797\u0798\7\25\2\2\u0798\u079b\5\u0158\u00ad")
        buf.write(u"\2\u0799\u079b\5\u015c\u00af\2\u079a\u0797\3\2\2\2\u079a")
        buf.write(u"\u0799\3\2\2\2\u079b\u0157\3\2\2\2\u079c\u079d\5\u0166")
        buf.write(u"\u00b4\2\u079d\u079f\7\26\2\2\u079e\u07a0\5\u015a\u00ae")
        buf.write(u"\2\u079f\u079e\3\2\2\2\u079f\u07a0\3\2\2\2\u07a0\u07a1")
        buf.write(u"\3\2\2\2\u07a1\u07a2\7\27\2\2\u07a2\u0159\3\2\2\2\u07a3")
        buf.write(u"\u07a4\b\u00ae\1\2\u07a4\u07a5\5\u0150\u00a9\2\u07a5")
        buf.write(u"\u07ab\3\2\2\2\u07a6\u07a7\f\3\2\2\u07a7\u07a8\7\23\2")
        buf.write(u"\2\u07a8\u07aa\5\u0150\u00a9\2\u07a9\u07a6\3\2\2\2\u07aa")
        buf.write(u"\u07ad\3\2\2\2\u07ab\u07a9\3\2\2\2\u07ab\u07ac\3\2\2")
        buf.write(u"\2\u07ac\u015b\3\2\2\2\u07ad\u07ab\3\2\2\2\u07ae\u07af")
        buf.write(u"\7\30\2\2\u07af\u07b0\5\u0150\u00a9\2\u07b0\u07b1\7\31")
        buf.write(u"\2\2\u07b1\u015d\3\2\2\2\u07b2\u07b3\7\26\2\2\u07b3\u07b4")
        buf.write(u"\5\u0150\u00a9\2\u07b4\u07b5\7\27\2\2\u07b5\u015f\3\2")
        buf.write(u"\2\2\u07b6\u07b7\b\u00b1\1\2\u07b7\u07b8\5\u0166\u00b4")
        buf.write(u"\2\u07b8\u07be\3\2\2\2\u07b9\u07ba\f\3\2\2\u07ba\u07bb")
        buf.write(u"\7\25\2\2\u07bb\u07bd\5\u0166\u00b4\2\u07bc\u07b9\3\2")
        buf.write(u"\2\2\u07bd\u07c0\3\2\2\2\u07be\u07bc\3\2\2\2\u07be\u07bf")
        buf.write(u"\3\2\2\2\u07bf\u0161\3\2\2\2\u07c0\u07be\3\2\2\2\u07c1")
        buf.write(u"\u07c2\b\u00b2\1\2\u07c2\u07c3\5\u0160\u00b1\2\u07c3")
        buf.write(u"\u07c8\3\2\2\2\u07c4\u07c5\f\3\2\2\u07c5\u07c7\7\u0098")
        buf.write(u"\2\2\u07c6\u07c4\3\2\2\2\u07c7\u07ca\3\2\2\2\u07c8\u07c6")
        buf.write(u"\3\2\2\2\u07c8\u07c9\3\2\2\2\u07c9\u0163\3\2\2\2\u07ca")
        buf.write(u"\u07c8\3\2\2\2\u07cb\u07d1\7\u009a\2\2\u07cc\u07d1\7")
        buf.write(u"\u009c\2\2\u07cd\u07d1\7\u0099\2\2\u07ce\u07d1\7\u0090")
        buf.write(u"\2\2\u07cf\u07d1\7\u0091\2\2\u07d0\u07cb\3\2\2\2\u07d0")
        buf.write(u"\u07cc\3\2\2\2\u07d0\u07cd\3\2\2\2\u07d0\u07ce\3\2\2")
        buf.write(u"\2\u07d0\u07cf\3\2\2\2\u07d1\u0165\3\2\2\2\u07d2\u07d3")
        buf.write(u"\t\b\2\2\u07d3\u0167\3\2\2\2\u07d4\u07d5\7{\2\2\u07d5")
        buf.write(u"\u07d6\5\u016a\u00b6\2\u07d6\u07d7\7\22\2\2\u07d7\u07dc")
        buf.write(u"\3\2\2\2\u07d8\u07d9\5\u016a\u00b6\2\u07d9\u07da\7\22")
        buf.write(u"\2\2\u07da\u07dc\3\2\2\2\u07db\u07d4\3\2\2\2\u07db\u07d8")
        buf.write(u"\3\2\2\2\u07dc\u0169\3\2\2\2\u07dd\u07de\b\u00b6\1\2")
        buf.write(u"\u07de\u07df\5\u016c\u00b7\2\u07df\u07e4\3\2\2\2\u07e0")
        buf.write(u"\u07e1\f\3\2\2\u07e1\u07e3\5\u0170\u00b9\2\u07e2\u07e0")
        buf.write(u"\3\2\2\2\u07e3\u07e6\3\2\2\2\u07e4\u07e2\3\2\2\2\u07e4")
        buf.write(u"\u07e5\3\2\2\2\u07e5\u016b\3\2\2\2\u07e6\u07e4\3\2\2")
        buf.write(u"\2\u07e7\u07ec\5\u016e\u00b8\2\u07e8\u07ec\5\u0178\u00bd")
        buf.write(u"\2\u07e9\u07ec\5\u017a\u00be\2\u07ea\u07ec\5\u017c\u00bf")
        buf.write(u"\2\u07eb\u07e7\3\2\2\2\u07eb\u07e8\3\2\2\2\u07eb\u07e9")
        buf.write(u"\3\2\2\2\u07eb\u07ea\3\2\2\2\u07ec\u016d\3\2\2\2\u07ed")
        buf.write(u"\u07ee\5\u00f2z\2\u07ee\u016f\3\2\2\2\u07ef\u07f0\7\25")
        buf.write(u"\2\2\u07f0\u07f3\5\u0172\u00ba\2\u07f1\u07f3\5\u0176")
        buf.write(u"\u00bc\2\u07f2\u07ef\3\2\2\2\u07f2\u07f1\3\2\2\2\u07f3")
        buf.write(u"\u0171\3\2\2\2\u07f4\u07f5\5\u017e\u00c0\2\u07f5\u07f7")
        buf.write(u"\7\26\2\2\u07f6\u07f8\5\u0174\u00bb\2\u07f7\u07f6\3\2")
        buf.write(u"\2\2\u07f7\u07f8\3\2\2\2\u07f8\u07f9\3\2\2\2\u07f9\u07fa")
        buf.write(u"\7\27\2\2\u07fa\u0173\3\2\2\2\u07fb\u07fc\b\u00bb\1\2")
        buf.write(u"\u07fc\u07fd\5\u016a\u00b6\2\u07fd\u0803\3\2\2\2\u07fe")
        buf.write(u"\u07ff\f\3\2\2\u07ff\u0800\7\23\2\2\u0800\u0802\5\u016a")
        buf.write(u"\u00b6\2\u0801\u07fe\3\2\2\2\u0802\u0805\3\2\2\2\u0803")
        buf.write(u"\u0801\3\2\2\2\u0803\u0804\3\2\2\2\u0804\u0175\3\2\2")
        buf.write(u"\2\u0805\u0803\3\2\2\2\u0806\u0807\7\30\2\2\u0807\u0808")
        buf.write(u"\5\u016a\u00b6\2\u0808\u0809\7\31\2\2\u0809\u0177\3\2")
        buf.write(u"\2\2\u080a\u080b\7\26\2\2\u080b\u080c\5\u016a\u00b6\2")
        buf.write(u"\u080c\u080d\7\27\2\2\u080d\u0179\3\2\2\2\u080e\u080f")
        buf.write(u"\b\u00be\1\2\u080f\u0812\7\u0098\2\2\u0810\u0812\5\u017e")
        buf.write(u"\u00c0\2\u0811\u080e\3\2\2\2\u0811\u0810\3\2\2\2\u0812")
        buf.write(u"\u0818\3\2\2\2\u0813\u0814\f\3\2\2\u0814\u0815\7\25\2")
        buf.write(u"\2\u0815\u0817\5\u017e\u00c0\2\u0816\u0813\3\2\2\2\u0817")
        buf.write(u"\u081a\3\2\2\2\u0818\u0816\3\2\2\2\u0818\u0819\3\2\2")
        buf.write(u"\2\u0819\u017b\3\2\2\2\u081a\u0818\3\2\2\2\u081b\u0821")
        buf.write(u"\7\u009a\2\2\u081c\u0821\7\u009c\2\2\u081d\u0821\7\u0099")
        buf.write(u"\2\2\u081e\u0821\7\u0090\2\2\u081f\u0821\7\u0091\2\2")
        buf.write(u"\u0820\u081b\3\2\2\2\u0820\u081c\3\2\2\2\u0820\u081d")
        buf.write(u"\3\2\2\2\u0820\u081e\3\2\2\2\u0820\u081f\3\2\2\2\u0821")
        buf.write(u"\u017d\3\2\2\2\u0822\u0823\t\t\2\2\u0823\u017f\3\2\2")
        buf.write(u"\2\u00a2\u0186\u0189\u01a2\u01a7\u01b2\u01b7\u01c2\u01c9")
        buf.write(u"\u01d6\u01e4\u0200\u0207\u0210\u0219\u0222\u0237\u0241")
        buf.write(u"\u0246\u024c\u0251\u025d\u0262\u027a\u0285\u0289\u029c")
        buf.write(u"\u02a6\u02af\u02b8\u02c1\u02de\u02f1\u02f7\u0319\u0322")
        buf.write(u"\u0339\u0347\u0350\u0359\u0370\u0374\u0388\u03e8\u03ea")
        buf.write(u"\u03f6\u03ff\u040e\u0413\u0418\u0421\u0428\u044c\u0453")
        buf.write(u"\u0455\u045f\u046f\u0478\u047e\u0483\u048a\u0492\u04a0")
        buf.write(u"\u04a8\u04ae\u04b9\u04c5\u04d0\u04dd\u04e1\u04e7\u04f3")
        buf.write(u"\u0507\u0509\u050e\u051a\u0525\u052f\u0534\u0539\u0549")
        buf.write(u"\u054e\u0551\u0555\u055a\u0561\u056c\u056e\u057a\u0582")
        buf.write(u"\u058d\u0592\u059e\u05a2\u05ac\u05b4\u05ba\u05c1\u05c6")
        buf.write(u"\u05d0\u05d7\u05e4\u05f1\u05f5\u05f8\u05fc\u05ff\u060a")
        buf.write(u"\u0616\u0622\u062e\u063f\u064e\u0658\u065f\u0669\u0670")
        buf.write(u"\u0674\u067a\u0686\u0691\u06a1\u06ae\u06b5\u06bd\u06d9")
        buf.write(u"\u06e2\u06eb\u06f4\u06f9\u0705\u0717\u071e\u0727\u072e")
        buf.write(u"\u0736\u073b\u0745\u074f\u075f\u0769\u0770\u0778\u0783")
        buf.write(u"\u078c\u0793\u079a\u079f\u07ab\u07be\u07c8\u07d0\u07db")
        buf.write(u"\u07e4\u07eb\u07f2\u07f7\u0803\u0811\u0818\u0820")
        return buf.getvalue()
		

class SParser ( AbstractParser ):

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
                     u"'Code'", u"'Document'", u"'abstract'", u"'all'", 
                     u"'always'", u"'and'", u"'any'", u"'as'", u"'attr'", 
                     u"'attribute'", u"'attributes'", u"'bindings'", u"'case'", 
                     u"'catch'", u"'category'", u"'class'", u"'close'", 
                     u"'contains'", u"'def'", u"'default'", u"'define'", 
                     u"'do'", u"'doing'", u"'each'", u"'else'", u"'enum'", 
                     u"'enumerated'", u"'except'", u"'execute'", u"'expecting'", 
                     u"'extends'", u"'fetch'", u"'finally'", u"'for'", u"'from'", 
                     u"'getter'", u"'if'", u"'in'", u"'invoke'", u"'is'", 
                     u"'matching'", u"'method'", u"'methods'", u"'modulo'", 
                     u"'mutable'", u"'native'", u"'None'", u"'not'", u"<INVALID>", 
                     u"'null'", u"'on'", u"'one'", u"'open'", u"'operator'", 
                     u"'or'", u"'otherwise'", u"'pass'", u"'raise'", u"'read'", 
                     u"'receiving'", u"'resource'", u"'return'", u"'returning'", 
                     u"'rows'", u"'self'", u"'setter'", u"'singleton'", 
                     u"'sorted'", u"'storable'", u"'store'", u"'switch'", 
                     u"'test'", u"'this'", u"'throw'", u"'to'", u"'try'", 
                     u"'verifying'", u"'with'", u"'when'", u"'where'", u"'while'", 
                     u"'write'", u"<INVALID>", u"<INVALID>", u"'MIN_INTEGER'", 
                     u"'MAX_INTEGER'" ]

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
                      u"DOCUMENT", u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", 
                      u"ANY", u"AS", u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", 
                      u"BINDINGS", u"CASE", u"CATCH", u"CATEGORY", u"CLASS", 
                      u"CLOSE", u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", 
                      u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FINALLY", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INVOKE", u"IS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", u"OPERATOR", 
                      u"OR", u"OTHERWISE", u"PASS", u"RAISE", u"READ", u"RECEIVING", 
                      u"RESOURCE", u"RETURN", u"RETURNING", u"ROWS", u"SELF", 
                      u"SETTER", u"SINGLETON", u"SORTED", u"STORABLE", u"STORE", 
                      u"SWITCH", u"TEST", u"THIS", u"THROW", u"TO", u"TRY", 
                      u"VERIFYING", u"WITH", u"WHEN", u"WHERE", u"WHILE", 
                      u"WRITE", u"BOOLEAN_LITERAL", u"CHAR_LITERAL", u"MIN_INTEGER", 
                      u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", u"TYPE_IDENTIFIER", 
                      u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", u"DOLLAR_IDENTIFIER", 
                      u"TEXT_LITERAL", u"INTEGER_LITERAL", u"HEXA_LITERAL", 
                      u"DECIMAL_LITERAL", u"DATETIME_LITERAL", u"TIME_LITERAL", 
                      u"DATE_LITERAL", u"PERIOD_LITERAL" ]

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
    RULE_typed_argument = 21
    RULE_statement = 22
    RULE_store_statement = 23
    RULE_method_call = 24
    RULE_method_selector = 25
    RULE_callable_parent = 26
    RULE_callable_selector = 27
    RULE_with_resource_statement = 28
    RULE_with_singleton_statement = 29
    RULE_switch_statement = 30
    RULE_switch_case_statement = 31
    RULE_for_each_statement = 32
    RULE_do_while_statement = 33
    RULE_while_statement = 34
    RULE_if_statement = 35
    RULE_else_if_statement_list = 36
    RULE_raise_statement = 37
    RULE_try_statement = 38
    RULE_catch_statement = 39
    RULE_return_statement = 40
    RULE_expression = 41
    RULE_closure_expression = 42
    RULE_instance_expression = 43
    RULE_method_expression = 44
    RULE_instance_selector = 45
    RULE_document_expression = 46
    RULE_constructor_expression = 47
    RULE_argument_assignment_list = 48
    RULE_argument_assignment = 49
    RULE_read_expression = 50
    RULE_write_statement = 51
    RULE_fetch_expression = 52
    RULE_sorted_expression = 53
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
    RULE_member_method_declaration_list = 95
    RULE_member_method_declaration = 96
    RULE_native_member_method_declaration_list = 97
    RULE_native_member_method_declaration = 98
    RULE_native_category_binding = 99
    RULE_python_category_binding = 100
    RULE_python_module = 101
    RULE_module_token = 102
    RULE_javascript_category_binding = 103
    RULE_javascript_module = 104
    RULE_variable_identifier_list = 105
    RULE_method_declaration = 106
    RULE_comment_statement = 107
    RULE_native_statement_list = 108
    RULE_native_statement = 109
    RULE_python_native_statement = 110
    RULE_javascript_native_statement = 111
    RULE_statement_list = 112
    RULE_assertion_list = 113
    RULE_switch_case_statement_list = 114
    RULE_catch_statement_list = 115
    RULE_literal_collection = 116
    RULE_atomic_literal = 117
    RULE_literal_list_literal = 118
    RULE_selectable_expression = 119
    RULE_this_expression = 120
    RULE_parenthesis_expression = 121
    RULE_literal_expression = 122
    RULE_collection_literal = 123
    RULE_tuple_literal = 124
    RULE_dict_literal = 125
    RULE_expression_tuple = 126
    RULE_dict_entry_list = 127
    RULE_dict_entry = 128
    RULE_slice_arguments = 129
    RULE_assign_variable_statement = 130
    RULE_assignable_instance = 131
    RULE_is_expression = 132
    RULE_operator = 133
    RULE_key_token = 134
    RULE_value_token = 135
    RULE_symbols_token = 136
    RULE_assign = 137
    RULE_multiply = 138
    RULE_divide = 139
    RULE_idivide = 140
    RULE_modulo = 141
    RULE_javascript_statement = 142
    RULE_javascript_expression = 143
    RULE_javascript_primary_expression = 144
    RULE_javascript_this_expression = 145
    RULE_javascript_selector_expression = 146
    RULE_javascript_method_expression = 147
    RULE_javascript_arguments = 148
    RULE_javascript_item_expression = 149
    RULE_javascript_parenthesis_expression = 150
    RULE_javascript_identifier_expression = 151
    RULE_javascript_literal_expression = 152
    RULE_javascript_identifier = 153
    RULE_python_statement = 154
    RULE_python_expression = 155
    RULE_python_primary_expression = 156
    RULE_python_selector_expression = 157
    RULE_python_method_expression = 158
    RULE_python_argument_list = 159
    RULE_python_ordinal_argument_list = 160
    RULE_python_named_argument_list = 161
    RULE_python_parenthesis_expression = 162
    RULE_python_identifier_expression = 163
    RULE_python_literal_expression = 164
    RULE_python_identifier = 165
    RULE_java_statement = 166
    RULE_java_expression = 167
    RULE_java_primary_expression = 168
    RULE_java_this_expression = 169
    RULE_java_selector_expression = 170
    RULE_java_method_expression = 171
    RULE_java_arguments = 172
    RULE_java_item_expression = 173
    RULE_java_parenthesis_expression = 174
    RULE_java_identifier_expression = 175
    RULE_java_class_identifier_expression = 176
    RULE_java_literal_expression = 177
    RULE_java_identifier = 178
    RULE_csharp_statement = 179
    RULE_csharp_expression = 180
    RULE_csharp_primary_expression = 181
    RULE_csharp_this_expression = 182
    RULE_csharp_selector_expression = 183
    RULE_csharp_method_expression = 184
    RULE_csharp_arguments = 185
    RULE_csharp_item_expression = 186
    RULE_csharp_parenthesis_expression = 187
    RULE_csharp_identifier_expression = 188
    RULE_csharp_literal_expression = 189
    RULE_csharp_identifier = 190

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"getter_method_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"typed_argument", 
                   u"statement", u"store_statement", u"method_call", u"method_selector", 
                   u"callable_parent", u"callable_selector", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"return_statement", 
                   u"expression", u"closure_expression", u"instance_expression", 
                   u"method_expression", u"instance_selector", u"document_expression", 
                   u"constructor_expression", u"argument_assignment_list", 
                   u"argument_assignment", u"read_expression", u"write_statement", 
                   u"fetch_expression", u"sorted_expression", u"assign_instance_statement", 
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
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"module_token", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"method_declaration", 
                   u"comment_statement", u"native_statement_list", u"native_statement", 
                   u"python_native_statement", u"javascript_native_statement", 
                   u"statement_list", u"assertion_list", u"switch_case_statement_list", 
                   u"catch_statement_list", u"literal_collection", u"atomic_literal", 
                   u"literal_list_literal", u"selectable_expression", u"this_expression", 
                   u"parenthesis_expression", u"literal_expression", u"collection_literal", 
                   u"tuple_literal", u"dict_literal", u"expression_tuple", 
                   u"dict_entry_list", u"dict_entry", u"slice_arguments", 
                   u"assign_variable_statement", u"assignable_instance", 
                   u"is_expression", u"operator", u"key_token", u"value_token", 
                   u"symbols_token", u"assign", u"multiply", u"divide", 
                   u"idivide", u"modulo", u"javascript_statement", u"javascript_expression", 
                   u"javascript_primary_expression", u"javascript_this_expression", 
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
                   u"java_selector_expression", u"java_method_expression", 
                   u"java_arguments", u"java_item_expression", u"java_parenthesis_expression", 
                   u"java_identifier_expression", u"java_class_identifier_expression", 
                   u"java_literal_expression", u"java_identifier", u"csharp_statement", 
                   u"csharp_expression", u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_selector_expression", u"csharp_method_expression", 
                   u"csharp_arguments", u"csharp_item_expression", u"csharp_parenthesis_expression", 
                   u"csharp_identifier_expression", u"csharp_literal_expression", 
                   u"csharp_identifier" ]

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
    ABSTRACT=62
    ALL=63
    ALWAYS=64
    AND=65
    ANY=66
    AS=67
    ATTR=68
    ATTRIBUTE=69
    ATTRIBUTES=70
    BINDINGS=71
    CASE=72
    CATCH=73
    CATEGORY=74
    CLASS=75
    CLOSE=76
    CONTAINS=77
    DEF=78
    DEFAULT=79
    DEFINE=80
    DO=81
    DOING=82
    EACH=83
    ELSE=84
    ENUM=85
    ENUMERATED=86
    EXCEPT=87
    EXECUTE=88
    EXPECTING=89
    EXTENDS=90
    FETCH=91
    FINALLY=92
    FOR=93
    FROM=94
    GETTER=95
    IF=96
    IN=97
    INVOKE=98
    IS=99
    MATCHING=100
    METHOD=101
    METHODS=102
    MODULO=103
    MUTABLE=104
    NATIVE=105
    NONE=106
    NOT=107
    NOTHING=108
    NULL=109
    ON=110
    ONE=111
    OPEN=112
    OPERATOR=113
    OR=114
    OTHERWISE=115
    PASS=116
    RAISE=117
    READ=118
    RECEIVING=119
    RESOURCE=120
    RETURN=121
    RETURNING=122
    ROWS=123
    SELF=124
    SETTER=125
    SINGLETON=126
    SORTED=127
    STORABLE=128
    STORE=129
    SWITCH=130
    TEST=131
    THIS=132
    THROW=133
    TO=134
    TRY=135
    VERIFYING=136
    WITH=137
    WHEN=138
    WHERE=139
    WHILE=140
    WRITE=141
    BOOLEAN_LITERAL=142
    CHAR_LITERAL=143
    MIN_INTEGER=144
    MAX_INTEGER=145
    SYMBOL_IDENTIFIER=146
    TYPE_IDENTIFIER=147
    VARIABLE_IDENTIFIER=148
    NATIVE_IDENTIFIER=149
    DOLLAR_IDENTIFIER=150
    TEXT_LITERAL=151
    INTEGER_LITERAL=152
    HEXA_LITERAL=153
    DECIMAL_LITERAL=154
    DATETIME_LITERAL=155
    TIME_LITERAL=156
    DATE_LITERAL=157
    PERIOD_LITERAL=158

    def __init__(self, input):
        super(SParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.symbols = None # Category_symbol_listContext

        def ENUM(self):
            return self.getToken(SParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(SParser.Category_symbol_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def getRuleIndex(self):
            return SParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = SParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(SParser.ENUM)
            self.state = 383 
            localctx.name = self.type_identifier()
            self.state = 384
            self.match(SParser.LPAR)
            self.state = 391
            token = self._input.LA(1)
            if token in [SParser.TYPE_IDENTIFIER]:
                self.state = 385 
                localctx.derived = self.type_identifier()
                self.state = 388
                _la = self._input.LA(1)
                if _la==SParser.COMMA:
                    self.state = 386
                    self.match(SParser.COMMA)
                    self.state = 387 
                    localctx.attrs = self.attribute_list()



            elif token in [SParser.VARIABLE_IDENTIFIER]:
                self.state = 390 
                localctx.attrs = self.attribute_list()

            else:
                raise NoViableAltException(self)

            self.state = 393
            self.match(SParser.RPAR)
            self.state = 394
            self.match(SParser.COLON)
            self.state = 395 
            self.indent()
            self.state = 396 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 397 
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
            super(SParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUM(self):
            return self.getToken(SParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(SParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(SParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = SParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(SParser.ENUM)
            self.state = 400 
            localctx.name = self.type_identifier()
            self.state = 401
            self.match(SParser.LPAR)
            self.state = 402 
            localctx.typ = self.native_type()
            self.state = 403
            self.match(SParser.RPAR)
            self.state = 404
            self.match(SParser.COLON)
            self.state = 405 
            self.indent()
            self.state = 406 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 407 
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
            super(SParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_symbol

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = SParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409 
            localctx.name = self.symbol_identifier()
            self.state = 410
            self.match(SParser.EQ)
            self.state = 411 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_category_symbol

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = SParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413 
            localctx.name = self.symbol_identifier()
            self.state = 414
            self.match(SParser.LPAR)
            self.state = 416
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 415 
                localctx.args = self.argument_assignment_list(0)


            self.state = 418
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext

        def ATTR(self):
            return self.getToken(SParser.ATTR, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(SParser.Attribute_constraintContext,0)


        def getRuleIndex(self):
            return SParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = SParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 420
                self.match(SParser.STORABLE)


            self.state = 423
            self.match(SParser.ATTR)
            self.state = 424 
            localctx.name = self.variable_identifier()
            self.state = 425
            self.match(SParser.LPAR)
            self.state = 426 
            localctx.typ = self.typedef(0)
            self.state = 427
            self.match(SParser.RPAR)
            self.state = 428
            self.match(SParser.COLON)
            self.state = 429 
            self.indent()
            self.state = 432
            token = self._input.LA(1)
            if token in [SParser.IN, SParser.MATCHING]:
                self.state = 430 
                localctx.match = self.attribute_constraint()

            elif token in [SParser.PASS]:
                self.state = 431
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 434 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(SParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(SParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(SParser.Derived_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = SParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 436
                self.match(SParser.STORABLE)


            self.state = 439
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 440 
            localctx.name = self.type_identifier()
            self.state = 441
            self.match(SParser.LPAR)
            self.state = 448
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 442 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 443 
                localctx.attrs = self.attribute_list()
                pass

            elif la_ == 3:
                self.state = 444 
                localctx.derived = self.derived_list()
                self.state = 445
                self.match(SParser.COMMA)
                self.state = 446 
                localctx.attrs = self.attribute_list()
                pass


            self.state = 450
            self.match(SParser.RPAR)
            self.state = 451
            self.match(SParser.COLON)
            self.state = 452 
            self.indent()
            self.state = 455
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 453 
                localctx.methods = self.member_method_declaration_list(0)

            elif token in [SParser.PASS]:
                self.state = 454
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 457 
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
            super(SParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def SINGLETON(self):
            return self.getToken(SParser.SINGLETON, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = SParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(SParser.SINGLETON)
            self.state = 460 
            localctx.name = self.type_identifier()
            self.state = 461
            self.match(SParser.LPAR)
            self.state = 462 
            localctx.attrs = self.attribute_list()
            self.state = 463
            self.match(SParser.RPAR)
            self.state = 464
            self.match(SParser.COLON)
            self.state = 465 
            self.indent()
            self.state = 468
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 466 
                localctx.methods = self.member_method_declaration_list(0)

            elif token in [SParser.PASS]:
                self.state = 467
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 470 
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
            super(SParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Type_identifier_listContext

        def type_identifier_list(self):
            return self.getTypedRuleContext(SParser.Type_identifier_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_derived_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDerived_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDerived_list(self)




    def derived_list(self):

        localctx = SParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472 
            localctx.items = self.type_identifier_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def OPERATOR(self):
            return self.getToken(SParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(SParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(SParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def getRuleIndex(self):
            return SParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = SParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(SParser.DEF)
            self.state = 475
            self.match(SParser.OPERATOR)
            self.state = 476 
            localctx.op = self.operator()
            self.state = 477
            self.match(SParser.LPAR)
            self.state = 478 
            localctx.arg = self.operator_argument()
            self.state = 479
            self.match(SParser.RPAR)
            self.state = 482
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 480
                self.match(SParser.RARROW)
                self.state = 481 
                localctx.typ = self.typedef(0)


            self.state = 484
            self.match(SParser.COLON)
            self.state = 485 
            self.indent()
            self.state = 486 
            localctx.stmts = self.statement_list(0)
            self.state = 487 
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
            super(SParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def SETTER(self):
            return self.getToken(SParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = SParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(SParser.DEF)
            self.state = 490 
            localctx.name = self.variable_identifier()
            self.state = 491
            self.match(SParser.SETTER)
            self.state = 492
            self.match(SParser.LPAR)
            self.state = 493
            self.match(SParser.RPAR)
            self.state = 494
            self.match(SParser.COLON)
            self.state = 495 
            self.indent()
            self.state = 496 
            localctx.stmts = self.statement_list(0)
            self.state = 497 
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
            super(SParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def GETTER(self):
            return self.getToken(SParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = SParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(SParser.DEF)
            self.state = 500 
            localctx.name = self.variable_identifier()
            self.state = 501
            self.match(SParser.GETTER)
            self.state = 502
            self.match(SParser.LPAR)
            self.state = 503
            self.match(SParser.RPAR)
            self.state = 504
            self.match(SParser.COLON)
            self.state = 505 
            self.indent()
            self.state = 506 
            localctx.stmts = self.statement_list(0)
            self.state = 507 
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
            super(SParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(SParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(SParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = SParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 509
                self.match(SParser.STORABLE)


            self.state = 512
            self.match(SParser.NATIVE)
            self.state = 513
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 514 
            localctx.name = self.type_identifier()
            self.state = 515
            self.match(SParser.LPAR)
            self.state = 517
            _la = self._input.LA(1)
            if _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 516 
                localctx.attrs = self.attribute_list()


            self.state = 519
            self.match(SParser.RPAR)
            self.state = 520
            self.match(SParser.COLON)
            self.state = 521 
            self.indent()
            self.state = 522 
            localctx.bindings = self.native_category_bindings()
            self.state = 526
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 523 
                self.lfp()
                self.state = 524 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 528 
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
            super(SParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(SParser.RESOURCE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingsContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = SParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(SParser.NATIVE)
            self.state = 531
            self.match(SParser.RESOURCE)
            self.state = 532 
            localctx.name = self.type_identifier()
            self.state = 533
            self.match(SParser.LPAR)
            self.state = 535
            _la = self._input.LA(1)
            if _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 534 
                localctx.attrs = self.attribute_list()


            self.state = 537
            self.match(SParser.RPAR)
            self.state = 538
            self.match(SParser.COLON)
            self.state = 539 
            self.indent()
            self.state = 540 
            localctx.bindings = self.native_category_bindings()
            self.state = 544
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 541 
                self.lfp()
                self.state = 542 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 546 
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
            super(SParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def BINDINGS(self):
            return self.getToken(SParser.BINDINGS, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(SParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(SParser.CATEGORY, 0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(SParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = SParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(SParser.DEF)
            self.state = 549
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 550
            self.match(SParser.BINDINGS)
            self.state = 551
            self.match(SParser.COLON)
            self.state = 552 
            self.indent()
            self.state = 553 
            localctx.items = self.native_category_binding_list(0)
            self.state = 554 
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
            super(SParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_binding_listContext)
            super(SParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(SParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_binding_listContext)
            super(SParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 557 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 565
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryBindingListItemContext(self, SParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 559
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 560 
                    self.lfp()
                    self.state = 561 
                    localctx.item = self.native_category_binding() 
                self.state = 567
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext

        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_attribute_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_list(self)




    def attribute_list(self):

        localctx = SParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attribute_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568 
            localctx.items = self.variable_identifier_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext

        def ABSTRACT(self):
            return self.getToken(SParser.ABSTRACT, 0)

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def getRuleIndex(self):
            return SParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = SParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(SParser.ABSTRACT)
            self.state = 571
            self.match(SParser.DEF)
            self.state = 572 
            localctx.name = self.method_identifier()
            self.state = 573
            self.match(SParser.LPAR)
            self.state = 575
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 574 
                localctx.args = self.argument_list(0)


            self.state = 577
            self.match(SParser.RPAR)
            self.state = 580
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 578
                self.match(SParser.RARROW)
                self.state = 579 
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
            super(SParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def getRuleIndex(self):
            return SParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = SParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.match(SParser.DEF)
            self.state = 583 
            localctx.name = self.method_identifier()
            self.state = 584
            self.match(SParser.LPAR)
            self.state = 586
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 585 
                localctx.args = self.argument_list(0)


            self.state = 588
            self.match(SParser.RPAR)
            self.state = 591
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 589
                self.match(SParser.RARROW)
                self.state = 590 
                localctx.typ = self.typedef(0)


            self.state = 593
            self.match(SParser.COLON)
            self.state = 594 
            self.indent()
            self.state = 595 
            localctx.stmts = self.statement_list(0)
            self.state = 596 
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
            super(SParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = SParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(SParser.DEF)
            self.state = 599
            self.match(SParser.NATIVE)
            self.state = 600 
            localctx.name = self.method_identifier()
            self.state = 601
            self.match(SParser.LPAR)
            self.state = 603
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 602 
                localctx.args = self.argument_list(0)


            self.state = 605
            self.match(SParser.RPAR)
            self.state = 608
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 606
                self.match(SParser.RARROW)
                self.state = 607 
                localctx.typ = self.category_or_any_type()


            self.state = 610
            self.match(SParser.COLON)
            self.state = 611 
            self.indent()
            self.state = 612 
            localctx.stmts = self.native_statement_list(0)
            self.state = 613 
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
            super(SParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def VERIFYING(self):
            return self.getToken(SParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(SParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = SParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(SParser.DEF)
            self.state = 616
            self.match(SParser.TEST)
            self.state = 617
            localctx.name = self.match(SParser.TEXT_LITERAL)
            self.state = 618
            self.match(SParser.LPAR)
            self.state = 619
            self.match(SParser.RPAR)
            self.state = 620
            self.match(SParser.COLON)
            self.state = 621 
            self.indent()
            self.state = 622 
            localctx.stmts = self.statement_list(0)
            self.state = 623 
            self.dedent()
            self.state = 624 
            self.lfp()
            self.state = 625
            self.match(SParser.VERIFYING)
            self.state = 626
            self.match(SParser.COLON)
            self.state = 632
            token = self._input.LA(1)
            if token in [SParser.LF]:
                self.state = 627 
                self.indent()
                self.state = 628 
                localctx.exps = self.assertion_list(0)
                self.state = 629 
                self.dedent()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                self.state = 631 
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
            super(SParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assertion

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = SParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_listContext
            self.value = None # Literal_expressionContext

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(SParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_typed_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = SParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636 
            localctx.name = self.variable_identifier()
            self.state = 637
            self.match(SParser.COLON)
            self.state = 638 
            localctx.typ = self.category_or_any_type()
            self.state = 643
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 639
                self.match(SParser.LPAR)
                self.state = 640 
                localctx.attrs = self.attribute_list()
                self.state = 641
                self.match(SParser.RPAR)


            self.state = 647
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 645
                self.match(SParser.EQ)
                self.state = 646 
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
            super(SParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(SParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(SParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(SParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(SParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(SParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(SParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(SParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(SParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRaiseStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(SParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(SParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(SParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(SParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(SParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(SParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(SParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitClosureStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(SParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(SParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = SParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 666
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 649 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = SParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 650 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = SParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 651 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = SParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 652 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = SParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 653 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 6:
                localctx = SParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 654 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 7:
                localctx = SParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 655 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 8:
                localctx = SParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 656 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 9:
                localctx = SParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 657 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 10:
                localctx = SParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 658 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 11:
                localctx = SParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 659 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 12:
                localctx = SParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 660 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 13:
                localctx = SParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 661 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 14:
                localctx = SParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 662 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 15:
                localctx = SParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 663 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 16:
                localctx = SParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 664 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 17:
                localctx = SParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 665 
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
            super(SParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exps = None # Expression_listContext

        def STORE(self):
            return self.getToken(SParser.STORE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_store_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = SParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_store_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(SParser.STORE)
            self.state = 669
            self.match(SParser.LPAR)
            self.state = 670 
            localctx.exps = self.expression_list(0)
            self.state = 671
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(SParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_method_call

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = SParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673 
            localctx.method = self.method_selector()
            self.state = 674
            self.match(SParser.LPAR)
            self.state = 676
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 675 
                localctx.args = self.argument_assignment_list(0)


            self.state = 678
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(SParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_selectorContext)
            super(SParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(SParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_selectorContext)
            super(SParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = SParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_selector)
        try:
            self.state = 685
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 680 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 681 
                localctx.parent = self.callable_parent(0)
                self.state = 682
                self.match(SParser.DOT)
                self.state = 683 
                localctx.name = self.method_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Callable_parentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(SParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_parentContext)
            super(SParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(SParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(SParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_parentContext)
            super(SParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 688 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 694
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CallableSelectorContext(self, SParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 690
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 691 
                    localctx.select = self.callable_selector() 
                self.state = 696
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(SParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_selectorContext)
            super(SParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_selectorContext)
            super(SParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = SParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_callable_selector)
        try:
            self.state = 703
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 697
                self.match(SParser.DOT)
                self.state = 698 
                localctx.name = self.variable_identifier()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 699
                self.match(SParser.LBRAK)
                self.state = 700 
                localctx.exp = self.expression(0)
                self.state = 701
                self.match(SParser.RBRAK)

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
            super(SParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(SParser.WITH, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(SParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = SParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 705
            self.match(SParser.WITH)
            self.state = 706 
            localctx.stmt = self.assign_variable_statement()
            self.state = 707
            self.match(SParser.COLON)
            self.state = 708 
            self.indent()
            self.state = 709 
            localctx.stmts = self.statement_list(0)
            self.state = 710 
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
            super(SParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(SParser.WITH, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = SParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(SParser.WITH)
            self.state = 713 
            localctx.typ = self.type_identifier()
            self.state = 714
            self.match(SParser.COLON)
            self.state = 715 
            self.indent()
            self.state = 716 
            localctx.stmts = self.statement_list(0)
            self.state = 717 
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
            super(SParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(SParser.SWITCH, 0)

        def ON(self):
            return self.getToken(SParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(SParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(SParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_switch_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = SParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
            self.match(SParser.SWITCH)
            self.state = 720
            self.match(SParser.ON)
            self.state = 721 
            localctx.exp = self.expression(0)
            self.state = 722
            self.match(SParser.COLON)
            self.state = 723 
            self.indent()
            self.state = 724 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 732
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 725 
                self.lfp()
                self.state = 726
                self.match(SParser.OTHERWISE)
                self.state = 727
                self.match(SParser.COLON)
                self.state = 728 
                self.indent()
                self.state = 729 
                localctx.stmts = self.statement_list(0)
                self.state = 730 
                self.dedent()


            self.state = 734 
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
            super(SParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(SParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statementContext)
            super(SParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(SParser.WHEN, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statementContext)
            super(SParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(SParser.WHEN, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(SParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = SParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_case_statement)
        try:
            self.state = 751
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = SParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 736
                self.match(SParser.WHEN)
                self.state = 737 
                localctx.exp = self.atomic_literal()
                self.state = 738
                self.match(SParser.COLON)
                self.state = 739 
                self.indent()
                self.state = 740 
                localctx.stmts = self.statement_list(0)
                self.state = 741 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = SParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 743
                self.match(SParser.WHEN)
                self.state = 744
                self.match(SParser.IN)
                self.state = 745 
                localctx.exp = self.literal_collection()
                self.state = 746
                self.match(SParser.COLON)
                self.state = 747 
                self.indent()
                self.state = 748 
                localctx.stmts = self.statement_list(0)
                self.state = 749 
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
            super(SParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(SParser.FOR, 0)

        def IN(self):
            return self.getToken(SParser.IN, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def getRuleIndex(self):
            return SParser.RULE_for_each_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = SParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self.match(SParser.FOR)
            self.state = 754 
            localctx.name1 = self.variable_identifier()
            self.state = 757
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 755
                self.match(SParser.COMMA)
                self.state = 756 
                localctx.name2 = self.variable_identifier()


            self.state = 759
            self.match(SParser.IN)
            self.state = 760 
            localctx.source = self.expression(0)
            self.state = 761
            self.match(SParser.COLON)
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

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(SParser.DO, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(SParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_do_while_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = SParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 766
            self.match(SParser.DO)
            self.state = 767
            self.match(SParser.COLON)
            self.state = 768 
            self.indent()
            self.state = 769 
            localctx.stmts = self.statement_list(0)
            self.state = 770 
            self.dedent()
            self.state = 771 
            self.lfp()
            self.state = 772
            self.match(SParser.WHILE)
            self.state = 773 
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
            super(SParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(SParser.WHILE, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_while_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = SParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.match(SParser.WHILE)
            self.state = 776 
            localctx.exp = self.expression(0)
            self.state = 777
            self.match(SParser.COLON)
            self.state = 778 
            self.indent()
            self.state = 779 
            localctx.stmts = self.statement_list(0)
            self.state = 780 
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
            super(SParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(SParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(SParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(SParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_if_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = SParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.match(SParser.IF)
            self.state = 783 
            localctx.exp = self.expression(0)
            self.state = 784
            self.match(SParser.COLON)
            self.state = 785 
            self.indent()
            self.state = 786 
            localctx.stmts = self.statement_list(0)
            self.state = 787 
            self.dedent()
            self.state = 791
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 788 
                self.lfp()
                self.state = 789 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 800
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 793 
                self.lfp()
                self.state = 794
                self.match(SParser.ELSE)
                self.state = 795
                self.match(SParser.COLON)
                self.state = 796 
                self.indent()
                self.state = 797 
                localctx.elseStmts = self.statement_list(0)
                self.state = 798 
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
            super(SParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Else_if_statement_listContext)
            super(SParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)
        def IF(self):
            return self.getToken(SParser.IF, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Else_if_statement_listContext)
            super(SParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)
        def IF(self):
            return self.getToken(SParser.IF, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(SParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 803
            self.match(SParser.ELSE)
            self.state = 804
            self.match(SParser.IF)
            self.state = 805 
            localctx.exp = self.expression(0)
            self.state = 806
            self.match(SParser.COLON)
            self.state = 807 
            self.indent()
            self.state = 808 
            localctx.stmts = self.statement_list(0)
            self.state = 809 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 823
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ElseIfStatementListItemContext(self, SParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 811
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 812 
                    self.lfp()
                    self.state = 813
                    self.match(SParser.ELSE)
                    self.state = 814
                    self.match(SParser.IF)
                    self.state = 815 
                    localctx.exp = self.expression(0)
                    self.state = 816
                    self.match(SParser.COLON)
                    self.state = 817 
                    self.indent()
                    self.state = 818 
                    localctx.stmts = self.statement_list(0)
                    self.state = 819 
                    self.dedent() 
                self.state = 825
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(SParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_raise_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = SParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 826
            self.match(SParser.RAISE)
            self.state = 827 
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
            super(SParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(SParser.TRY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfsContext)
            else:
                return self.getTypedRuleContext(SParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(SParser.Statement_listContext,i)


        def EXCEPT(self):
            return self.getToken(SParser.EXCEPT, 0)

        def FINALLY(self):
            return self.getToken(SParser.FINALLY, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(SParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_try_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = SParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(SParser.TRY)
            self.state = 830 
            localctx.name = self.variable_identifier()
            self.state = 831
            self.match(SParser.COLON)
            self.state = 832 
            self.indent()
            self.state = 833 
            localctx.stmts = self.statement_list(0)
            self.state = 834 
            self.dedent()
            self.state = 835 
            self.lfs()
            self.state = 837
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 836 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 846
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 839
                self.match(SParser.EXCEPT)
                self.state = 840
                self.match(SParser.COLON)
                self.state = 841 
                self.indent()
                self.state = 842 
                localctx.anyStmts = self.statement_list(0)
                self.state = 843 
                self.dedent()
                self.state = 844 
                self.lfs()


            self.state = 855
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 848
                self.match(SParser.FINALLY)
                self.state = 849
                self.match(SParser.COLON)
                self.state = 850 
                self.indent()
                self.state = 851 
                localctx.finalStmts = self.statement_list(0)
                self.state = 852 
                self.dedent()
                self.state = 853 
                self.lfs()


            self.state = 857 
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
            super(SParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(SParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statementContext)
            super(SParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(SParser.EXCEPT, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(SParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statementContext)
            super(SParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(SParser.EXCEPT, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(SParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(SParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = SParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_catch_statement)
        try:
            self.state = 878
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = SParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 859
                self.match(SParser.EXCEPT)
                self.state = 860 
                localctx.name = self.symbol_identifier()
                self.state = 861
                self.match(SParser.COLON)
                self.state = 862 
                self.indent()
                self.state = 863 
                localctx.stmts = self.statement_list(0)
                self.state = 864 
                self.dedent()
                self.state = 865 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = SParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 867
                self.match(SParser.EXCEPT)
                self.state = 868
                self.match(SParser.IN)
                self.state = 869
                self.match(SParser.LBRAK)
                self.state = 870 
                localctx.exp = self.symbol_list(0)
                self.state = 871
                self.match(SParser.RBRAK)
                self.state = 872
                self.match(SParser.COLON)
                self.state = 873 
                self.indent()
                self.state = 874 
                localctx.stmts = self.statement_list(0)
                self.state = 875 
                self.dedent()
                self.state = 876 
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
            super(SParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_return_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = SParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 880
            self.match(SParser.RETURN)
            self.state = 882
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 881 
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
            super(SParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(SParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(SParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntDivideExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SParser.IF, 0)
        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTernaryExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(SParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitContainsAllExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(SParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitInExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(SParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitGreaterThanExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(SParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(SParser.CODE, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(SParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLessThanOrEqualExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(SParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAndExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(SParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitClosureExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(SParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotContainsAnyExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitContainsExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(SParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(SParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRoughlyEqualsExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(SParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(SParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(SParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotInExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(SParser.IS, 0)
        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(SParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(SParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(SParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(SParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(SParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAddExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(SParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotContainsAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(SParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitInstanceExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(SParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitContainsAnyExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(SParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(SParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(SParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(SParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 902
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = SParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 885
                self.match(SParser.MINUS)
                self.state = 886 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 2:
                localctx = SParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 887
                self.match(SParser.NOT)
                self.state = 888 
                localctx.exp = self.expression(30)
                pass

            elif la_ == 3:
                localctx = SParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 889 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = SParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 890 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = SParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 891
                self.match(SParser.CODE)
                self.state = 892
                self.match(SParser.LPAR)
                self.state = 893 
                localctx.exp = self.expression(0)
                self.state = 894
                self.match(SParser.RPAR)
                pass

            elif la_ == 6:
                localctx = SParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 896
                self.match(SParser.EXECUTE)
                self.state = 897
                self.match(SParser.LPAR)
                self.state = 898 
                localctx.name = self.variable_identifier()
                self.state = 899
                self.match(SParser.RPAR)
                pass

            elif la_ == 7:
                localctx = SParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 901 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1000
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 998
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = SParser.MultiplyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 904
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 905 
                        self.multiply()
                        self.state = 906 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 2:
                        localctx = SParser.DivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 908
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 909 
                        self.divide()
                        self.state = 910 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 3:
                        localctx = SParser.ModuloExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 912
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 913 
                        self.modulo()
                        self.state = 914 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 4:
                        localctx = SParser.IntDivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 916
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 917 
                        self.idivide()
                        self.state = 918 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 5:
                        localctx = SParser.AddExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 920
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 921
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SParser.PLUS or _la==SParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 922 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 6:
                        localctx = SParser.LessThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 923
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 924
                        self.match(SParser.LT)
                        self.state = 925 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 7:
                        localctx = SParser.LessThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 926
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 927
                        self.match(SParser.LTE)
                        self.state = 928 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 8:
                        localctx = SParser.GreaterThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 929
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 930
                        self.match(SParser.GT)
                        self.state = 931 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 9:
                        localctx = SParser.GreaterThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 932
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 933
                        self.match(SParser.GTE)
                        self.state = 934 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 10:
                        localctx = SParser.EqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 935
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 936
                        self.match(SParser.EQ2)
                        self.state = 937 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 11:
                        localctx = SParser.NotEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 938
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 939
                        self.match(SParser.XEQ)
                        self.state = 940 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 12:
                        localctx = SParser.RoughlyEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 941
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 942
                        self.match(SParser.TEQ)
                        self.state = 943 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 13:
                        localctx = SParser.OrExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 944
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 945
                        self.match(SParser.OR)
                        self.state = 946 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 14:
                        localctx = SParser.AndExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 947
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 948
                        self.match(SParser.AND)
                        self.state = 949 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 15:
                        localctx = SParser.TernaryExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 950
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 951
                        self.match(SParser.IF)
                        self.state = 952 
                        localctx.test = self.expression(0)
                        self.state = 953
                        self.match(SParser.ELSE)
                        self.state = 954 
                        localctx.ifFalse = self.expression(14)
                        pass

                    elif la_ == 16:
                        localctx = SParser.InExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 956
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 957
                        self.match(SParser.IN)
                        self.state = 958 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 17:
                        localctx = SParser.ContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 959
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 960
                        self.match(SParser.CONTAINS)
                        self.state = 961 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 18:
                        localctx = SParser.ContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 962
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 963
                        self.match(SParser.CONTAINS)
                        self.state = 964
                        self.match(SParser.ALL)
                        self.state = 965 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 19:
                        localctx = SParser.ContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 966
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 967
                        self.match(SParser.CONTAINS)
                        self.state = 968
                        self.match(SParser.ANY)
                        self.state = 969 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 20:
                        localctx = SParser.NotInExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 970
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 971
                        self.match(SParser.NOT)
                        self.state = 972
                        self.match(SParser.IN)
                        self.state = 973 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 21:
                        localctx = SParser.NotContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 974
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 975
                        self.match(SParser.NOT)
                        self.state = 976
                        self.match(SParser.CONTAINS)
                        self.state = 977 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 22:
                        localctx = SParser.NotContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 978
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 979
                        self.match(SParser.NOT)
                        self.state = 980
                        self.match(SParser.CONTAINS)
                        self.state = 981
                        self.match(SParser.ALL)
                        self.state = 982 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 23:
                        localctx = SParser.NotContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 983
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 984
                        self.match(SParser.NOT)
                        self.state = 985
                        self.match(SParser.CONTAINS)
                        self.state = 986
                        self.match(SParser.ANY)
                        self.state = 987 
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 24:
                        localctx = SParser.IsNotExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 988
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 989
                        self.match(SParser.IS)
                        self.state = 990
                        self.match(SParser.NOT)
                        self.state = 991 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 25:
                        localctx = SParser.IsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 992
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 993
                        self.match(SParser.IS)
                        self.state = 994 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = SParser.CastExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 995
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 996
                        self.match(SParser.AS)
                        self.state = 997 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1002
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_closure_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = SParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1003 
            localctx.name = self.type_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(SParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_expressionContext)
            super(SParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(SParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(SParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_expressionContext)
            super(SParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(SParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1006 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1012
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SelectorExpressionContext(self, SParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1008
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1009 
                    localctx.selector = self.instance_selector() 
                self.state = 1014
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_expression

     
        def copyFrom(self, ctx):
            super(SParser.Method_expressionContext, self).copyFrom(ctx)



    class ReadExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(SParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitReadExpression(self)


    class MethodCallExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(SParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodCallExpression(self)


    class FetchExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.FetchExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_expressionContext
            self.copyFrom(ctx)

        def fetch_expression(self):
            return self.getTypedRuleContext(SParser.Fetch_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchExpression(self)


    class ConstructorExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(SParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConstructorExpression(self)


    class DocumentExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(SParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocumentExpression(self)


    class SortedExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(SParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSortedExpression(self)



    def method_expression(self):

        localctx = SParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_expression)
        try:
            self.state = 1021
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = SParser.DocumentExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1015 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 2:
                localctx = SParser.FetchExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1016 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 3:
                localctx = SParser.ReadExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1017 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 4:
                localctx = SParser.SortedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1018 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 5:
                localctx = SParser.MethodCallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1019 
                localctx.exp = self.method_call()
                pass

            elif la_ == 6:
                localctx = SParser.ConstructorExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1020 
                localctx.exp = self.constructor_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(SParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_selectorContext)
            super(SParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(SParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_selectorContext)
            super(SParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_selectorContext)
            super(SParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = SParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_instance_selector)
        try:
            self.state = 1036
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1023
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1024
                self.match(SParser.DOT)
                self.state = 1025 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1026
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1027
                self.match(SParser.LBRAK)
                self.state = 1028 
                localctx.xslice = self.slice_arguments()
                self.state = 1029
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1031
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1032
                self.match(SParser.LBRAK)
                self.state = 1033 
                localctx.exp = self.expression(0)
                self.state = 1034
                self.match(SParser.RBRAK)
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
            super(SParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def document_type(self):
            return self.getTypedRuleContext(SParser.Document_typeContext,0)


        def getRuleIndex(self):
            return SParser.RULE_document_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = SParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1038 
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
            super(SParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_constructor_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConstructor_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConstructor_expression(self)




    def constructor_expression(self):

        localctx = SParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1041
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1040
                self.match(SParser.MUTABLE)


            self.state = 1043 
            localctx.typ = self.category_type()
            self.state = 1044
            self.match(SParser.LPAR)
            self.state = 1046
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 1045 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1048
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(SParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_assignment_listContext)
            super(SParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_assignment_listContext)
            super(SParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(SParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_assignment_listContext)
            super(SParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(SParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1055
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = SParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1051 
                localctx.exp = self.expression(0)
                self.state = 1052
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = SParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1054 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1062
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentAssignmentListItemContext(self, SParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1057
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1058
                    self.match(SParser.COMMA)
                    self.state = 1059 
                    localctx.item = self.argument_assignment() 
                self.state = 1064
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = SParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1065 
            localctx.name = self.variable_identifier()
            self.state = 1066 
            self.assign()
            self.state = 1067 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def FROM(self):
            return self.getToken(SParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = SParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1069
            self.match(SParser.READ)
            self.state = 1070
            self.match(SParser.FROM)
            self.state = 1071 
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
            super(SParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TO(self):
            return self.getToken(SParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SParser.RULE_write_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = SParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1073
            self.match(SParser.WRITE)
            self.state = 1074 
            localctx.what = self.expression(0)
            self.state = 1075
            self.match(SParser.TO)
            self.state = 1076 
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Fetch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_fetch_expression

     
        def copyFrom(self, ctx):
            super(SParser.Fetch_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_expressionContext)
            super(SParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def ONE(self):
            return self.getToken(SParser.ONE, 0)
        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)
        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchOne(self)


    class FetchListContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_expressionContext)
            super(SParser.FetchListContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def FROM(self):
            return self.getToken(SParser.FROM, 0)
        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchList(self)


    class FetchAllContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_expressionContext)
            super(SParser.FetchAllContext, self).__init__(parser)
            self.start = None # ExpressionContext
            self.end = None # ExpressionContext
            self.typ = None # Category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)

        def ALL(self):
            return self.getToken(SParser.ALL, 0)
        def ROWS(self):
            return self.getToken(SParser.ROWS, 0)
        def TO(self):
            return self.getToken(SParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)

        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchAll(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchAll(self)



    def fetch_expression(self):

        localctx = SParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_fetch_expression)
        try:
            self.state = 1107
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = SParser.FetchListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1078
                self.match(SParser.FETCH)
                self.state = 1079 
                localctx.name = self.variable_identifier()
                self.state = 1080
                self.match(SParser.FROM)
                self.state = 1081 
                localctx.source = self.expression(0)
                self.state = 1082
                self.match(SParser.WHERE)
                self.state = 1083 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1085
                self.match(SParser.FETCH)
                self.state = 1086
                self.match(SParser.ONE)
                self.state = 1087 
                localctx.typ = self.category_type()
                self.state = 1088
                self.match(SParser.WHERE)
                self.state = 1089 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.FetchAllContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1091
                self.match(SParser.FETCH)
                self.state = 1098
                token = self._input.LA(1)
                if token in [SParser.ALL]:
                    self.state = 1092
                    self.match(SParser.ALL)

                elif token in [SParser.ROWS]:
                    self.state = 1093
                    self.match(SParser.ROWS)
                    self.state = 1094 
                    localctx.start = self.expression(0)
                    self.state = 1095
                    self.match(SParser.TO)
                    self.state = 1096 
                    localctx.end = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1100
                self.match(SParser.LPAR)
                self.state = 1101 
                localctx.typ = self.category_type()
                self.state = 1102
                self.match(SParser.RPAR)
                self.state = 1105
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 1103
                    self.match(SParser.WHERE)
                    self.state = 1104 
                    localctx.xfilter = self.expression(0)


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
            super(SParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(SParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(SParser.Instance_expressionContext,i)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(SParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def getRuleIndex(self):
            return SParser.RULE_sorted_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = SParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1109
            self.match(SParser.SORTED)
            self.state = 1110
            self.match(SParser.LPAR)
            self.state = 1111 
            localctx.source = self.instance_expression(0)
            self.state = 1117
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 1112
                self.match(SParser.COMMA)
                self.state = 1113 
                self.key_token()
                self.state = 1114
                self.match(SParser.EQ)
                self.state = 1115 
                localctx.key = self.instance_expression(0)


            self.state = 1119
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(SParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = SParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1121 
            localctx.inst = self.assignable_instance(0)
            self.state = 1122 
            self.assign()
            self.state = 1123 
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
            super(SParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(SParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Child_instanceContext)
            super(SParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Child_instanceContext)
            super(SParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = SParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_child_instance)
        try:
            self.state = 1133
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1125
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1126
                self.match(SParser.DOT)
                self.state = 1127 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1128
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1129
                self.match(SParser.LBRAK)
                self.state = 1130 
                localctx.exp = self.expression(0)
                self.state = 1131
                self.match(SParser.RBRAK)
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
            super(SParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = SParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1135 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1136 
            self.assign()
            self.state = 1137 
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
            super(SParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_lfs

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = SParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1139
                    self.match(SParser.LF) 
                self.state = 1144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_lfp

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = SParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1145
                self.match(SParser.LF)
                self.state = 1148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SParser.LF):
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
            super(SParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(SParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_indent

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = SParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1151 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1150
                self.match(SParser.LF)
                self.state = 1153 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SParser.LF):
                    break

            self.state = 1155
            self.match(SParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(SParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_dedent

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = SParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.LF:
                self.state = 1157
                self.match(SParser.LF)
                self.state = 1162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1163
            self.match(SParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(SParser.NONE, 0)

        def getRuleIndex(self):
            return SParser.RULE_null_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = SParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1165
            self.match(SParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(SParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Declaration_listContext)
            super(SParser.FullDeclarationListContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(SParser.LfsContext,0)

        def EOF(self):
            return self.getToken(SParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(SParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = SParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = SParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1168
            _la = self._input.LA(1)
            if _la==SParser.ABSTRACT or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (SParser.ATTR - 68)) | (1 << (SParser.CATEGORY - 68)) | (1 << (SParser.CLASS - 68)) | (1 << (SParser.DEF - 68)) | (1 << (SParser.ENUM - 68)) | (1 << (SParser.NATIVE - 68)) | (1 << (SParser.SINGLETON - 68)) | (1 << (SParser.STORABLE - 68)))) != 0):
                self.state = 1167 
                localctx.items = self.declarations(0)


            self.state = 1170 
            self.lfs()
            self.state = 1171
            self.match(SParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_declarations

     
        def copyFrom(self, ctx):
            super(SParser.DeclarationsContext, self).copyFrom(ctx)


    class DeclarationListItemContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationsContext)
            super(SParser.DeclarationListItemContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def declarations(self):
            return self.getTypedRuleContext(SParser.DeclarationsContext,0)

        def declaration(self):
            return self.getTypedRuleContext(SParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclarationListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclarationListItem(self)


    class DeclarationListContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationsContext)
            super(SParser.DeclarationListContext, self).__init__(parser)
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(SParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclarationList(self)



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1174 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.DeclarationListItemContext(self, SParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1176
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1177 
                    self.lfp()
                    self.state = 1178 
                    localctx.item = self.declaration() 
                self.state = 1184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_declaration

     
        def copyFrom(self, ctx):
            super(SParser.DeclarationContext, self).copyFrom(ctx)



    class ResourceDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationContext)
            super(SParser.ResourceDeclarationContext, self).__init__(parser)
            self.decl = None # Resource_declarationContext
            self.copyFrom(ctx)

        def resource_declaration(self):
            return self.getTypedRuleContext(SParser.Resource_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterResourceDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitResourceDeclaration(self)


    class MethodDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationContext)
            super(SParser.MethodDeclarationContext, self).__init__(parser)
            self.decl = None # Method_declarationContext
            self.copyFrom(ctx)

        def method_declaration(self):
            return self.getTypedRuleContext(SParser.Method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodDeclaration(self)


    class CategoryDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationContext)
            super(SParser.CategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Category_declarationContext
            self.copyFrom(ctx)

        def category_declaration(self):
            return self.getTypedRuleContext(SParser.Category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryDeclaration(self)


    class AttributeDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationContext)
            super(SParser.AttributeDeclarationContext, self).__init__(parser)
            self.decl = None # Attribute_declarationContext
            self.copyFrom(ctx)

        def attribute_declaration(self):
            return self.getTypedRuleContext(SParser.Attribute_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttributeDeclaration(self)


    class EnumDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationContext)
            super(SParser.EnumDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_declarationContext
            self.copyFrom(ctx)

        def enum_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnumDeclaration(self)



    def declaration(self):

        localctx = SParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_declaration)
        try:
            self.state = 1190
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = SParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1185 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1186 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1187 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = SParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1188 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = SParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1189 
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
            super(SParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.decl = None # Native_resource_declarationContext

        def native_resource_declaration(self):
            return self.getTypedRuleContext(SParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = SParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1192 
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
            super(SParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_enum_declaration

     
        def copyFrom(self, ctx):
            super(SParser.Enum_declarationContext, self).copyFrom(ctx)



    class EnumCategoryDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Enum_declarationContext)
            super(SParser.EnumCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_category_declarationContext
            self.copyFrom(ctx)

        def enum_category_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnumCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnumCategoryDeclaration(self)


    class EnumNativeDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Enum_declarationContext)
            super(SParser.EnumNativeDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_native_declarationContext
            self.copyFrom(ctx)

        def enum_native_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_native_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnumNativeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnumNativeDeclaration(self)



    def enum_declaration(self):

        localctx = SParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_enum_declaration)
        try:
            self.state = 1196
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = SParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1194 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1195 
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
            super(SParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_symbol_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_symbol_listContext, self).copyFrom(ctx)


    class NativeSymbolListContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_symbol_listContext)
            super(SParser.NativeSymbolListContext, self).__init__(parser)
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def native_symbol(self):
            return self.getTypedRuleContext(SParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeSymbolList(self)


    class NativeSymbolListItemContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_symbol_listContext)
            super(SParser.NativeSymbolListItemContext, self).__init__(parser)
            self.items = None # Native_symbol_listContext
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_symbol_list(self):
            return self.getTypedRuleContext(SParser.Native_symbol_listContext,0)

        def native_symbol(self):
            return self.getTypedRuleContext(SParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeSymbolListItem(self)



    def native_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1199 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeSymbolListItemContext(self, SParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1201
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1202 
                    self.lfp()
                    self.state = 1203 
                    localctx.item = self.native_symbol() 
                self.state = 1209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_category_symbol_list

     
        def copyFrom(self, ctx):
            super(SParser.Category_symbol_listContext, self).copyFrom(ctx)


    class CategorySymbolListItemContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_symbol_listContext)
            super(SParser.CategorySymbolListItemContext, self).__init__(parser)
            self.items = None # Category_symbol_listContext
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def category_symbol_list(self):
            return self.getTypedRuleContext(SParser.Category_symbol_listContext,0)

        def category_symbol(self):
            return self.getTypedRuleContext(SParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategorySymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategorySymbolListItem(self)


    class CategorySymbolListContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_symbol_listContext)
            super(SParser.CategorySymbolListContext, self).__init__(parser)
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def category_symbol(self):
            return self.getTypedRuleContext(SParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategorySymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategorySymbolList(self)



    def category_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Category_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1211 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CategorySymbolListItemContext(self, SParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1213
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1214 
                    self.lfp()
                    self.state = 1215 
                    localctx.item = self.category_symbol() 
                self.state = 1221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_symbol_list

     
        def copyFrom(self, ctx):
            super(SParser.Symbol_listContext, self).copyFrom(ctx)


    class SymbolListContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Symbol_listContext)
            super(SParser.SymbolListContext, self).__init__(parser)
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbolList(self)


    class SymbolListItemContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Symbol_listContext)
            super(SParser.SymbolListItemContext, self).__init__(parser)
            self.items = None # Symbol_listContext
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(SParser.Symbol_listContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbolListItem(self)



    def symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1223 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SymbolListItemContext(self, SParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1225
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1226
                    self.match(SParser.COMMA)
                    self.state = 1227 
                    localctx.item = self.symbol_identifier() 
                self.state = 1232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(SParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(SParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(SParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(SParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(SParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(SParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = SParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_attribute_constraint)
        try:
            self.state = 1243
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                localctx = SParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1233
                self.match(SParser.IN)
                self.state = 1234 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = SParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1235
                self.match(SParser.IN)
                self.state = 1236 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = SParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1237
                self.match(SParser.IN)
                self.state = 1238 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = SParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1239
                self.match(SParser.MATCHING)
                self.state = 1240
                localctx.text = self.match(SParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = SParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1241
                self.match(SParser.MATCHING)
                self.state = 1242 
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
            super(SParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_list_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = SParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1245
            self.match(SParser.LBRAK)
            self.state = 1247
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 1246 
                localctx.items = self.expression_list(0)


            self.state = 1249
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LT(self):
            return self.getToken(SParser.LT, 0)

        def GT(self):
            return self.getToken(SParser.GT, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_set_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = SParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1251
            self.match(SParser.LT)
            self.state = 1253
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 1252 
                localctx.items = self.expression_list(0)


            self.state = 1255
            self.match(SParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_expression_list

     
        def copyFrom(self, ctx):
            super(SParser.Expression_listContext, self).copyFrom(ctx)


    class ValueListContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_listContext)
            super(SParser.ValueListContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueList(self)


    class ValueListItemContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_listContext)
            super(SParser.ValueListItemContext, self).__init__(parser)
            self.items = None # Expression_listContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueListItem(self)



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1258 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ValueListItemContext(self, SParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1260
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1261
                    self.match(SParser.COMMA)
                    self.state = 1262 
                    localctx.item = self.expression(0) 
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

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(SParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SParser.RULE_range_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = SParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1268
            self.match(SParser.LBRAK)
            self.state = 1269 
            localctx.low = self.expression(0)
            self.state = 1270
            self.match(SParser.RANGE)
            self.state = 1271 
            localctx.high = self.expression(0)
            self.state = 1272
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(SParser.TypedefContext, self).copyFrom(ctx)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(SParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(SParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1275 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1285
                    la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                    if la_ == 1:
                        localctx = SParser.SetTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1277
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1278
                        self.match(SParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = SParser.ListTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1279
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1280
                        self.match(SParser.LBRAK)
                        self.state = 1281
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = SParser.DictTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1282
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1283
                        self.match(SParser.LCURL)
                        self.state = 1284
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(SParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Primary_typeContext)
            super(SParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(SParser.Native_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Primary_typeContext)
            super(SParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = SParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_primary_type)
        try:
            self.state = 1292
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE]:
                localctx = SParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1290 
                localctx.n = self.native_type()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1291 
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
            super(SParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(SParser.Native_typeContext, self).copyFrom(ctx)



    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.IntegerTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntegerType(self)


    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.PeriodTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPeriodType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DateTimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateTimeType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.BooleanTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBooleanType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DecimalTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.CodeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(SParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.CharacterTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCharacterType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DateTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.TextTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTextType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.TimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTimeType(self)



    def native_type(self):

        localctx = SParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_native_type)
        try:
            self.state = 1304
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN]:
                localctx = SParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1294
                localctx.t1 = self.match(SParser.BOOLEAN)

            elif token in [SParser.CHARACTER]:
                localctx = SParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1295
                localctx.t1 = self.match(SParser.CHARACTER)

            elif token in [SParser.TEXT]:
                localctx = SParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1296
                localctx.t1 = self.match(SParser.TEXT)

            elif token in [SParser.INTEGER]:
                localctx = SParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1297
                localctx.t1 = self.match(SParser.INTEGER)

            elif token in [SParser.DECIMAL]:
                localctx = SParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1298
                localctx.t1 = self.match(SParser.DECIMAL)

            elif token in [SParser.DATE]:
                localctx = SParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1299
                localctx.t1 = self.match(SParser.DATE)

            elif token in [SParser.DATETIME]:
                localctx = SParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1300
                localctx.t1 = self.match(SParser.DATETIME)

            elif token in [SParser.TIME]:
                localctx = SParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1301
                localctx.t1 = self.match(SParser.TIME)

            elif token in [SParser.PERIOD]:
                localctx = SParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1302
                localctx.t1 = self.match(SParser.PERIOD)

            elif token in [SParser.CODE]:
                localctx = SParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1303
                localctx.t1 = self.match(SParser.CODE)

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
            super(SParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_category_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = SParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1306
            localctx.t1 = self.match(SParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(SParser.CODE, 0)

        def getRuleIndex(self):
            return SParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = SParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1308
            localctx.t1 = self.match(SParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Document_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def DOCUMENT(self):
            return self.getToken(SParser.DOCUMENT, 0)

        def getRuleIndex(self):
            return SParser.RULE_document_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocument_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocument_type(self)




    def document_type(self):

        localctx = SParser.Document_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1310
            localctx.t1 = self.match(SParser.DOCUMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(SParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_declarationContext)
            super(SParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_declarationContext)
            super(SParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(SParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_declarationContext)
            super(SParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(SParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = SParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_category_declaration)
        try:
            self.state = 1315
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                localctx = SParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1312 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1313 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1314 
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
            super(SParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_type_identifier_list

     
        def copyFrom(self, ctx):
            super(SParser.Type_identifier_listContext, self).copyFrom(ctx)


    class TypeIdentifierListContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Type_identifier_listContext)
            super(SParser.TypeIdentifierListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypeIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypeIdentifierList(self)


    class TypeIdentifierListItemContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Type_identifier_listContext)
            super(SParser.TypeIdentifierListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(SParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypeIdentifierListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypeIdentifierListItem(self)



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 164
        self.enterRecursionRule(localctx, 164, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1318 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.TypeIdentifierListItemContext(self, SParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1320
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1321
                    self.match(SParser.COMMA)
                    self.state = 1322 
                    localctx.item = self.type_identifier() 
                self.state = 1327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_identifier

     
        def copyFrom(self, ctx):
            super(SParser.Method_identifierContext, self).copyFrom(ctx)



    class MethodVariableIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_identifierContext)
            super(SParser.MethodVariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodVariableIdentifier(self)


    class MethodTypeIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_identifierContext)
            super(SParser.MethodTypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodTypeIdentifier(self)



    def method_identifier(self):

        localctx = SParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_method_identifier)
        try:
            self.state = 1330
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1328 
                localctx.name = self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1329 
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
            super(SParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(SParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.TypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.SymbolIdentifierContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.VariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = SParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_identifier)
        try:
            self.state = 1335
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1332 
                localctx.name = self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1333 
                localctx.name = self.type_identifier()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                localctx = SParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1334 
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
            super(SParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = SParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1337
            self.match(SParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = SParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1339
            self.match(SParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = SParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1341
            self.match(SParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Argument_listContext, self).copyFrom(ctx)


    class ArgumentListItemContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_listContext)
            super(SParser.ArgumentListItemContext, self).__init__(parser)
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)

        def argument(self):
            return self.getTypedRuleContext(SParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentListItem(self)


    class ArgumentListContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_listContext)
            super(SParser.ArgumentListContext, self).__init__(parser)
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(SParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentList(self)



    def argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 176
        self.enterRecursionRule(localctx, 176, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1344 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentListItemContext(self, SParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1346
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1347
                    self.match(SParser.COMMA)
                    self.state = 1348 
                    localctx.item = self.argument() 
                self.state = 1353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(SParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a SParser.ArgumentContext)
            super(SParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(SParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a SParser.ArgumentContext)
            super(SParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(SParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = SParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1359
            token = self._input.LA(1)
            if token in [SParser.CODE]:
                localctx = SParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1354 
                localctx.arg = self.code_argument()

            elif token in [SParser.MUTABLE, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1356
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE:
                    self.state = 1355
                    self.match(SParser.MUTABLE)


                self.state = 1358 
                localctx.arg = self.operator_argument()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_operator_argument

     
        def copyFrom(self, ctx):
            super(SParser.Operator_argumentContext, self).copyFrom(ctx)



    class TypedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a SParser.Operator_argumentContext)
            super(SParser.TypedArgumentContext, self).__init__(parser)
            self.arg = None # Typed_argumentContext
            self.copyFrom(ctx)

        def typed_argument(self):
            return self.getTypedRuleContext(SParser.Typed_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypedArgument(self)


    class NamedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a SParser.Operator_argumentContext)
            super(SParser.NamedArgumentContext, self).__init__(parser)
            self.arg = None # Named_argumentContext
            self.copyFrom(ctx)

        def named_argument(self):
            return self.getTypedRuleContext(SParser.Named_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNamedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNamedArgument(self)



    def operator_argument(self):

        localctx = SParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_operator_argument)
        try:
            self.state = 1363
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                localctx = SParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1361 
                localctx.arg = self.named_argument()
                pass

            elif la_ == 2:
                localctx = SParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1362 
                localctx.arg = self.typed_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Named_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(SParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_named_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = SParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1365 
            localctx.name = self.variable_identifier()
            self.state = 1368
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 1366
                self.match(SParser.EQ)
                self.state = 1367 
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
            super(SParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(SParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_code_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = SParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1370 
            self.code_type()
            self.state = 1371 
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
            super(SParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_category_or_any_type

     
        def copyFrom(self, ctx):
            super(SParser.Category_or_any_typeContext, self).copyFrom(ctx)



    class AnyArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_or_any_typeContext)
            super(SParser.AnyArgumentTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyArgumentType(self)


    class CategoryArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_or_any_typeContext)
            super(SParser.CategoryArgumentTypeContext, self).__init__(parser)
            self.typ = None # TypedefContext
            self.copyFrom(ctx)

        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryArgumentType(self)



    def category_or_any_type(self):

        localctx = SParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_category_or_any_type)
        try:
            self.state = 1375
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1373 
                localctx.typ = self.typedef(0)

            elif token in [SParser.ANY]:
                localctx = SParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1374 
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
            super(SParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(SParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyListTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(SParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyDictTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)
        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 188
        self.enterRecursionRule(localctx, 188, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1378
            self.match(SParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1386
                    la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
                    if la_ == 1:
                        localctx = SParser.AnyListTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1380
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1381
                        self.match(SParser.LBRAK)
                        self.state = 1382
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = SParser.AnyDictTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1383
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1384
                        self.match(SParser.LCURL)
                        self.state = 1385
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(SParser.Member_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListItemContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Member_method_declaration_listContext)
            super(SParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Member_method_declaration_listContext,0)

        def member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryMethodListItem(self)


    class CategoryMethodListContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Member_method_declaration_listContext)
            super(SParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryMethodList(self)



    def member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 190
        self.enterRecursionRule(localctx, 190, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1392 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CategoryMethodListItemContext(self, SParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1394
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1395 
                    self.lfp()
                    self.state = 1396 
                    localctx.item = self.member_method_declaration() 
                self.state = 1402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(SParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(SParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(SParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(SParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = SParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_member_method_declaration)
        try:
            self.state = 1408
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1403 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1404 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1405 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1406 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1407 
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
            super(SParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_member_method_declaration_listContext, self).copyFrom(ctx)


    class NativeCategoryMethodListContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_member_method_declaration_listContext)
            super(SParser.NativeCategoryMethodListContext, self).__init__(parser)
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryMethodList(self)


    class NativeCategoryMethodListItemContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_member_method_declaration_listContext)
            super(SParser.NativeCategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Native_member_method_declaration_listContext
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declaration_listContext,0)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryMethodListItem(self)



    def native_member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 194
        self.enterRecursionRule(localctx, 194, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1411 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryMethodListItemContext(self, SParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1413
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1414 
                    self.lfp()
                    self.state = 1415 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Member_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = SParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_native_member_method_declaration)
        try:
            self.state = 1424
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1422 
                self.member_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1423 
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
            super(SParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(SParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(SParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(SParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(SParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(SParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(SParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(SParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(SParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(SParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = SParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_native_category_binding)
        try:
            self.state = 1436
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1426
                self.match(SParser.JAVA)
                self.state = 1427 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1428
                self.match(SParser.CSHARP)
                self.state = 1429 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1430
                self.match(SParser.PYTHON2)
                self.state = 1431 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1432
                self.match(SParser.PYTHON3)
                self.state = 1433 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1434
                self.match(SParser.JAVASCRIPT)
                self.state = 1435 
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
            super(SParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(SParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_category_binding

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = SParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1438 
            localctx.id_ = self.identifier()
            self.state = 1440
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 1439 
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
            super(SParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(SParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(SParser.DOT)
            else:
                return self.getToken(SParser.DOT, i)

        def getRuleIndex(self):
            return SParser.RULE_python_module

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = SParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1442
            self.match(SParser.FROM)
            self.state = 1443 
            self.module_token()
            self.state = 1444
            self.match(SParser.COLON)
            self.state = 1445 
            self.identifier()
            self.state = 1450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1446
                    self.match(SParser.DOT)
                    self.state = 1447 
                    self.identifier() 
                self.state = 1452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = SParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1454
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
            super(SParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(SParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = SParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1456 
            localctx.id_ = self.identifier()
            self.state = 1458
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.state = 1457 
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
            super(SParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(SParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(SParser.SLASH)
            else:
                return self.getToken(SParser.SLASH, i)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)

        def getRuleIndex(self):
            return SParser.RULE_javascript_module

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = SParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1460
            self.match(SParser.FROM)
            self.state = 1461 
            self.module_token()
            self.state = 1462
            self.match(SParser.COLON)
            self.state = 1464
            _la = self._input.LA(1)
            if _la==SParser.SLASH:
                self.state = 1463
                self.match(SParser.SLASH)


            self.state = 1466 
            self.javascript_identifier()
            self.state = 1471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1467
                    self.match(SParser.SLASH)
                    self.state = 1468 
                    self.javascript_identifier() 
                self.state = 1473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

            self.state = 1476
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 1474
                self.match(SParser.DOT)
                self.state = 1475 
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
            super(SParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_variable_identifier_list

     
        def copyFrom(self, ctx):
            super(SParser.Variable_identifier_listContext, self).copyFrom(ctx)


    class VariableListContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Variable_identifier_listContext)
            super(SParser.VariableListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariableList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariableList(self)


    class VariableListItemContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Variable_identifier_listContext)
            super(SParser.VariableListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariableListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariableListItem(self)



    def variable_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Variable_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 210
        self.enterRecursionRule(localctx, 210, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1479 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,98,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.VariableListItemContext(self, SParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1481
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1482
                    self.match(SParser.COMMA)
                    self.state = 1483 
                    localctx.item = self.variable_identifier() 
                self.state = 1488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,98,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_declaration

     
        def copyFrom(self, ctx):
            super(SParser.Method_declarationContext, self).copyFrom(ctx)



    class NativeMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.NativeMethodContext, self).__init__(parser)
            self.decl = None # Native_method_declarationContext
            self.copyFrom(ctx)

        def native_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeMethod(self)


    class AbstractMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.AbstractMethodContext, self).__init__(parser)
            self.decl = None # Abstract_method_declarationContext
            self.copyFrom(ctx)

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(SParser.Abstract_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAbstractMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAbstractMethod(self)


    class ConcreteMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.ConcreteMethodContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcreteMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcreteMethod(self)


    class TestMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.TestMethodContext, self).__init__(parser)
            self.decl = None # Test_method_declarationContext
            self.copyFrom(ctx)

        def test_method_declaration(self):
            return self.getTypedRuleContext(SParser.Test_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTestMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTestMethod(self)



    def method_declaration(self):

        localctx = SParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_method_declaration)
        try:
            self.state = 1493
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                localctx = SParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1489 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1490 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1491 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = SParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1492 
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
            super(SParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(SParser.COMMENT, 0)

        def getRuleIndex(self):
            return SParser.RULE_comment_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = SParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1495
            self.match(SParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_statement_listContext, self).copyFrom(ctx)


    class NativeStatementListItemContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statement_listContext)
            super(SParser.NativeStatementListItemContext, self).__init__(parser)
            self.items = None # Native_statement_listContext
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)

        def native_statement(self):
            return self.getTypedRuleContext(SParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeStatementListItem(self)


    class NativeStatementListContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statement_listContext)
            super(SParser.NativeStatementListContext, self).__init__(parser)
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def native_statement(self):
            return self.getTypedRuleContext(SParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeStatementList(self)



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 216
        self.enterRecursionRule(localctx, 216, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1498 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1506
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeStatementListItemContext(self, SParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1500
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1501 
                    self.lfp()
                    self.state = 1502 
                    localctx.item = self.native_statement() 
                self.state = 1508
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(SParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.CSharpNativeStatementContext, self).__init__(parser)
            self.stmt = None # Csharp_statementContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(SParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(SParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.JavaNativeStatementContext, self).__init__(parser)
            self.stmt = None # Java_statementContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(SParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(SParser.Java_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.stmt = None # Javascript_native_statementContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(SParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(SParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.Python2NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(SParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(SParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.Python3NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(SParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(SParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = SParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_native_statement)
        try:
            self.state = 1519
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1509
                self.match(SParser.JAVA)
                self.state = 1510 
                localctx.stmt = self.java_statement()

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1511
                self.match(SParser.CSHARP)
                self.state = 1512 
                localctx.stmt = self.csharp_statement()

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1513
                self.match(SParser.PYTHON2)
                self.state = 1514 
                localctx.stmt = self.python_native_statement()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1515
                self.match(SParser.PYTHON3)
                self.state = 1516 
                localctx.stmt = self.python_native_statement()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1517
                self.match(SParser.JAVASCRIPT)
                self.state = 1518 
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
            super(SParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Python_statementContext
            self.module = None # Python_moduleContext

        def python_statement(self):
            return self.getTypedRuleContext(SParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(SParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_native_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = SParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1521 
            localctx.stmt = self.python_statement()
            self.state = 1523
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1522
                self.match(SParser.SEMI)


            self.state = 1526
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                self.state = 1525 
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
            super(SParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Javascript_statementContext
            self.module = None # Javascript_moduleContext

        def javascript_statement(self):
            return self.getTypedRuleContext(SParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(SParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = SParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1528 
            localctx.stmt = self.javascript_statement()
            self.state = 1530
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 1529
                self.match(SParser.SEMI)


            self.state = 1533
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 1532 
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
            super(SParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Statement_listContext, self).copyFrom(ctx)


    class StatementListContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Statement_listContext)
            super(SParser.StatementListContext, self).__init__(parser)
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(SParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStatementList(self)


    class StatementListItemContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Statement_listContext)
            super(SParser.StatementListItemContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)

        def statement(self):
            return self.getTypedRuleContext(SParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStatementListItem(self)



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1536 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.StatementListItemContext(self, SParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1538
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1539 
                    self.lfp()
                    self.state = 1540 
                    localctx.item = self.statement() 
                self.state = 1546
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_assertion_list

     
        def copyFrom(self, ctx):
            super(SParser.Assertion_listContext, self).copyFrom(ctx)


    class AssertionListContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Assertion_listContext)
            super(SParser.AssertionListContext, self).__init__(parser)
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def assertion(self):
            return self.getTypedRuleContext(SParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertionList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertionList(self)


    class AssertionListItemContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Assertion_listContext)
            super(SParser.AssertionListItemContext, self).__init__(parser)
            self.items = None # Assertion_listContext
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def assertion_list(self):
            return self.getTypedRuleContext(SParser.Assertion_listContext,0)

        def assertion(self):
            return self.getTypedRuleContext(SParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertionListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertionListItem(self)



    def assertion_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Assertion_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 226
        self.enterRecursionRule(localctx, 226, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1548 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1556
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.AssertionListItemContext(self, SParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1550
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1551 
                    self.lfp()
                    self.state = 1552 
                    localctx.item = self.assertion() 
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
            super(SParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_switch_case_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Switch_case_statement_listContext, self).copyFrom(ctx)


    class SwitchCaseStatementListContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statement_listContext)
            super(SParser.SwitchCaseStatementListContext, self).__init__(parser)
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def switch_case_statement(self):
            return self.getTypedRuleContext(SParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitchCaseStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitchCaseStatementList(self)


    class SwitchCaseStatementListItemContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statement_listContext)
            super(SParser.SwitchCaseStatementListItemContext, self).__init__(parser)
            self.items = None # Switch_case_statement_listContext
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def switch_case_statement_list(self):
            return self.getTypedRuleContext(SParser.Switch_case_statement_listContext,0)

        def switch_case_statement(self):
            return self.getTypedRuleContext(SParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitchCaseStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitchCaseStatementListItem(self)



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SwitchCaseStatementListContext(self, localctx)
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
                    localctx = SParser.SwitchCaseStatementListItemContext(self, SParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
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
            super(SParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_catch_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Catch_statement_listContext, self).copyFrom(ctx)


    class CatchStatementListContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statement_listContext)
            super(SParser.CatchStatementListContext, self).__init__(parser)
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def catch_statement(self):
            return self.getTypedRuleContext(SParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchStatementList(self)


    class CatchStatementListItemContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statement_listContext)
            super(SParser.CatchStatementListItemContext, self).__init__(parser)
            self.items = None # Catch_statement_listContext
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(SParser.Catch_statement_listContext,0)

        def catch_statement(self):
            return self.getTypedRuleContext(SParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchStatementListItem(self)



    def catch_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Catch_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 230
        self.enterRecursionRule(localctx, 230, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CatchStatementListContext(self, localctx)
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
                    localctx = SParser.CatchStatementListItemContext(self, SParser.Catch_statement_listContext(self, _parentctx, _parentState))
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
            super(SParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(SParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_collectionContext)
            super(SParser.LiteralListLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_collectionContext)
            super(SParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(SParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(SParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_collectionContext)
            super(SParser.LiteralSetLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(SParser.LT, 0)
        def GT(self):
            return self.getToken(SParser.GT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = SParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_literal_collection)
        try:
            self.state = 1597
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = SParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1583
                self.match(SParser.LBRAK)
                self.state = 1584 
                localctx.low = self.atomic_literal()
                self.state = 1585
                self.match(SParser.RANGE)
                self.state = 1586 
                localctx.high = self.atomic_literal()
                self.state = 1587
                self.match(SParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = SParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1589
                self.match(SParser.LBRAK)
                self.state = 1590 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1591
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1593
                self.match(SParser.LT)
                self.state = 1594 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1595
                self.match(SParser.GT)
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
            super(SParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(SParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(SParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(SParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBooleanLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(SParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitHexadecimalLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(SParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(SParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(SParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(SParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(SParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = SParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_atomic_literal)
        try:
            self.state = 1612
            token = self._input.LA(1)
            if token in [SParser.MIN_INTEGER]:
                localctx = SParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1599
                localctx.t = self.match(SParser.MIN_INTEGER)

            elif token in [SParser.MAX_INTEGER]:
                localctx = SParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1600
                localctx.t = self.match(SParser.MAX_INTEGER)

            elif token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1601
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.HEXA_LITERAL]:
                localctx = SParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1602
                localctx.t = self.match(SParser.HEXA_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1603
                localctx.t = self.match(SParser.CHAR_LITERAL)

            elif token in [SParser.DATE_LITERAL]:
                localctx = SParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1604
                localctx.t = self.match(SParser.DATE_LITERAL)

            elif token in [SParser.TIME_LITERAL]:
                localctx = SParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1605
                localctx.t = self.match(SParser.TIME_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1606
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1607
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.DATETIME_LITERAL]:
                localctx = SParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1608
                localctx.t = self.match(SParser.DATETIME_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1609
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.PERIOD_LITERAL]:
                localctx = SParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1610
                localctx.t = self.match(SParser.PERIOD_LITERAL)

            elif token in [SParser.NONE]:
                localctx = SParser.NullLiteralContext(self, localctx)
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
            super(SParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_literal_list_literal

     
        def copyFrom(self, ctx):
            super(SParser.Literal_list_literalContext, self).copyFrom(ctx)


    class LiteralListContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_list_literalContext)
            super(SParser.LiteralListContext, self).__init__(parser)
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralList(self)


    class LiteralListItemContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_list_literalContext)
            super(SParser.LiteralListItemContext, self).__init__(parser)
            self.items = None # Literal_list_literalContext
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralListItem(self)



    def literal_list_literal(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Literal_list_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 236
        self.enterRecursionRule(localctx, 236, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.LiteralListContext(self, localctx)
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
                    localctx = SParser.LiteralListItemContext(self, SParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1617
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1618
                    self.match(SParser.COMMA)
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
            super(SParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(SParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(SParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = SParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_selectable_expression)
        try:
            self.state = 1629
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                localctx = SParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1625 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1626 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = SParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1627 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = SParser.ThisExpressionContext(self, localctx)
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
            super(SParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(SParser.SELF, 0)

        def THIS(self):
            return self.getToken(SParser.THIS, 0)

        def getRuleIndex(self):
            return SParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = SParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631
            _la = self._input.LA(1)
            if not(_la==SParser.SELF or _la==SParser.THIS):
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
            super(SParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = SParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633
            self.match(SParser.LPAR)
            self.state = 1634 
            localctx.exp = self.expression(0)
            self.state = 1635
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Literal_expressionContext, self).copyFrom(ctx)



    class CollectionLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_expressionContext)
            super(SParser.CollectionLiteralContext, self).__init__(parser)
            self.exp = None # Collection_literalContext
            self.copyFrom(ctx)

        def collection_literal(self):
            return self.getTypedRuleContext(SParser.Collection_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCollectionLiteral(self)


    class AtomicLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_expressionContext)
            super(SParser.AtomicLiteralContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAtomicLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAtomicLiteral(self)



    def literal_expression(self):

        localctx = SParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_literal_expression)
        try:
            self.state = 1639
            token = self._input.LA(1)
            if token in [SParser.NONE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.MIN_INTEGER, SParser.MAX_INTEGER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.HEXA_LITERAL, SParser.DECIMAL_LITERAL, SParser.DATETIME_LITERAL, SParser.TIME_LITERAL, SParser.DATE_LITERAL, SParser.PERIOD_LITERAL]:
                localctx = SParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1637 
                localctx.exp = self.atomic_literal()

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.LCURL, SParser.LT]:
                localctx = SParser.CollectionLiteralContext(self, localctx)
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
            super(SParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_collection_literal

     
        def copyFrom(self, ctx):
            super(SParser.Collection_literalContext, self).copyFrom(ctx)



    class ListLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.ListLiteralContext, self).__init__(parser)
            self.exp = None # List_literalContext
            self.copyFrom(ctx)

        def list_literal(self):
            return self.getTypedRuleContext(SParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitListLiteral(self)


    class RangeLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.RangeLiteralContext, self).__init__(parser)
            self.exp = None # Range_literalContext
            self.copyFrom(ctx)

        def range_literal(self):
            return self.getTypedRuleContext(SParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRangeLiteral(self)


    class TupleLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.TupleLiteralContext, self).__init__(parser)
            self.exp = None # Tuple_literalContext
            self.copyFrom(ctx)

        def tuple_literal(self):
            return self.getTypedRuleContext(SParser.Tuple_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTupleLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTupleLiteral(self)


    class SetLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.SetLiteralContext, self).__init__(parser)
            self.exp = None # Set_literalContext
            self.copyFrom(ctx)

        def set_literal(self):
            return self.getTypedRuleContext(SParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSetLiteral(self)


    class DictLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.DictLiteralContext, self).__init__(parser)
            self.exp = None # Dict_literalContext
            self.copyFrom(ctx)

        def dict_literal(self):
            return self.getTypedRuleContext(SParser.Dict_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictLiteral(self)



    def collection_literal(self):

        localctx = SParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_collection_literal)
        try:
            self.state = 1646
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                localctx = SParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1641 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = SParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1642 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = SParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1643 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = SParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1644 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = SParser.TupleLiteralContext(self, localctx)
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
            super(SParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_tupleContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(SParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_tuple_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = SParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1648
            self.match(SParser.LPAR)
            self.state = 1650
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 1649 
                localctx.items = self.expression_tuple(0)


            self.state = 1652
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Dict_entry_listContext

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(SParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_dict_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = SParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1654
            self.match(SParser.LCURL)
            self.state = 1656
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (SParser.EXECUTE - 88)) | (1 << (SParser.FETCH - 88)) | (1 << (SParser.MUTABLE - 88)) | (1 << (SParser.NONE - 88)) | (1 << (SParser.NOT - 88)) | (1 << (SParser.READ - 88)) | (1 << (SParser.SELF - 88)) | (1 << (SParser.SORTED - 88)) | (1 << (SParser.THIS - 88)) | (1 << (SParser.BOOLEAN_LITERAL - 88)) | (1 << (SParser.CHAR_LITERAL - 88)) | (1 << (SParser.MIN_INTEGER - 88)) | (1 << (SParser.MAX_INTEGER - 88)) | (1 << (SParser.SYMBOL_IDENTIFIER - 88)) | (1 << (SParser.TYPE_IDENTIFIER - 88)) | (1 << (SParser.VARIABLE_IDENTIFIER - 88)) | (1 << (SParser.TEXT_LITERAL - 88)))) != 0) or ((((_la - 152)) & ~0x3f) == 0 and ((1 << (_la - 152)) & ((1 << (SParser.INTEGER_LITERAL - 152)) | (1 << (SParser.HEXA_LITERAL - 152)) | (1 << (SParser.DECIMAL_LITERAL - 152)) | (1 << (SParser.DATETIME_LITERAL - 152)) | (1 << (SParser.TIME_LITERAL - 152)) | (1 << (SParser.DATE_LITERAL - 152)) | (1 << (SParser.PERIOD_LITERAL - 152)))) != 0):
                self.state = 1655 
                localctx.items = self.dict_entry_list(0)


            self.state = 1658
            self.match(SParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_expression_tuple

     
        def copyFrom(self, ctx):
            super(SParser.Expression_tupleContext, self).copyFrom(ctx)


    class ValueTupleContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_tupleContext)
            super(SParser.ValueTupleContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueTuple(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueTuple(self)


    class ValueTupleItemContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_tupleContext)
            super(SParser.ValueTupleItemContext, self).__init__(parser)
            self.items = None # Expression_tupleContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def expression_tuple(self):
            return self.getTypedRuleContext(SParser.Expression_tupleContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueTupleItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueTupleItem(self)



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 252
        self.enterRecursionRule(localctx, 252, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ValueTupleContext(self, localctx)
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
                    localctx = SParser.ValueTupleItemContext(self, SParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1663
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1664
                    self.match(SParser.COMMA)
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
            super(SParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_dict_entry_list

     
        def copyFrom(self, ctx):
            super(SParser.Dict_entry_listContext, self).copyFrom(ctx)


    class DictEntryListContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Dict_entry_listContext)
            super(SParser.DictEntryListContext, self).__init__(parser)
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def dict_entry(self):
            return self.getTypedRuleContext(SParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictEntryList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictEntryList(self)


    class DictEntryListItemContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Dict_entry_listContext)
            super(SParser.DictEntryListItemContext, self).__init__(parser)
            self.items = None # Dict_entry_listContext
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def dict_entry_list(self):
            return self.getTypedRuleContext(SParser.Dict_entry_listContext,0)

        def dict_entry(self):
            return self.getTypedRuleContext(SParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictEntryListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictEntryListItem(self)



    def dict_entry_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Dict_entry_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 254
        self.enterRecursionRule(localctx, 254, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.DictEntryListContext(self, localctx)
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
                    localctx = SParser.DictEntryListItemContext(self, SParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1674
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1675
                    self.match(SParser.COMMA)
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
            super(SParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SParser.RULE_dict_entry

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = SParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1682 
            localctx.key = self.expression(0)
            self.state = 1683
            self.match(SParser.COLON)
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
            super(SParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Slice_argumentsContext)
            super(SParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Slice_argumentsContext)
            super(SParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Slice_argumentsContext)
            super(SParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = SParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_slice_arguments)
        try:
            self.state = 1695
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                localctx = SParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1686 
                localctx.first = self.expression(0)
                self.state = 1687
                self.match(SParser.COLON)
                self.state = 1688 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1690 
                localctx.first = self.expression(0)
                self.state = 1691
                self.match(SParser.COLON)
                pass

            elif la_ == 3:
                localctx = SParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1693
                self.match(SParser.COLON)
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
            super(SParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = SParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_assign_variable_statement)
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
            super(SParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(SParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Assignable_instanceContext)
            super(SParser.ChildInstanceContext, self).__init__(parser)
            self.parent = None # Assignable_instanceContext
            self.child = None # Child_instanceContext
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(SParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(SParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Assignable_instanceContext)
            super(SParser.RootInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 262
        self.enterRecursionRule(localctx, 262, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.RootInstanceContext(self, localctx)
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
                    localctx = SParser.ChildInstanceContext(self, SParser.Assignable_instanceContext(self, _parentctx, _parentState))
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
            super(SParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(SParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Is_expressionContext)
            super(SParser.IsATypeExpressionContext, self).__init__(parser)
            self.typ = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Is_expressionContext)
            super(SParser.IsOtherExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = SParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_is_expression)
        try:
            self.state = 1715
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                localctx = SParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1711
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1712
                self.match(SParser.VARIABLE_IDENTIFIER)
                self.state = 1713 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = SParser.IsOtherExpressionContext(self, localctx)
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
            super(SParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(SParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(SParser.PLUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(SParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(SParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(SParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(SParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = SParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_operator)
        try:
            self.state = 1723
            token = self._input.LA(1)
            if token in [SParser.PLUS]:
                localctx = SParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1717
                self.match(SParser.PLUS)

            elif token in [SParser.MINUS]:
                localctx = SParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1718
                self.match(SParser.MINUS)

            elif token in [SParser.STAR]:
                localctx = SParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1719 
                self.multiply()

            elif token in [SParser.SLASH]:
                localctx = SParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1720 
                self.divide()

            elif token in [SParser.BSLASH]:
                localctx = SParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1721 
                self.idivide()

            elif token in [SParser.PERCENT, SParser.MODULO]:
                localctx = SParser.OperatorModuloContext(self, localctx)
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
            super(SParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = SParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1725
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
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
            super(SParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = SParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1728
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
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
            super(SParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = SParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1731
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
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
            super(SParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def getRuleIndex(self):
            return SParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = SParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1734
            self.match(SParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(SParser.STAR, 0)

        def getRuleIndex(self):
            return SParser.RULE_multiply

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = SParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1736
            self.match(SParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(SParser.SLASH, 0)

        def getRuleIndex(self):
            return SParser.RULE_divide

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = SParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1738
            self.match(SParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(SParser.BSLASH, 0)

        def getRuleIndex(self):
            return SParser.RULE_idivide

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = SParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1740
            self.match(SParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(SParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(SParser.MODULO, 0)

        def getRuleIndex(self):
            return SParser.RULE_modulo

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = SParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1742
            _la = self._input.LA(1)
            if not(_la==SParser.PERCENT or _la==SParser.MODULO):
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
            super(SParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_statementContext)
            super(SParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_statementContext)
            super(SParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = SParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_javascript_statement)
        try:
            self.state = 1751
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1744
                self.match(SParser.RETURN)
                self.state = 1745 
                localctx.exp = self.javascript_expression(0)
                self.state = 1746
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1748 
                localctx.exp = self.javascript_expression(0)
                self.state = 1749
                self.match(SParser.SEMI)

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
            super(SParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_expressionContext)
            super(SParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_expressionContext)
            super(SParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 286
        self.enterRecursionRule(localctx, 286, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptPrimaryExpressionContext(self, localctx)
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
                    localctx = SParser.JavascriptSelectorExpressionContext(self, SParser.Javascript_expressionContext(self, _parentctx, _parentState))
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
            super(SParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_this_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = SParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_javascript_primary_expression)
        try:
            self.state = 1769
            la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1763 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1764 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1765 
                self.javascript_identifier_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1766 
                self.javascript_literal_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1767 
                self.javascript_method_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1768 
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
            super(SParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = SParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1771 
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_selector_expressionContext)
            super(SParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(SParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_selector_expressionContext)
            super(SParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_selector_expressionContext)
            super(SParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = SParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_javascript_selector_expression)
        try:
            self.state = 1778
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                localctx = SParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1773
                self.match(SParser.DOT)
                self.state = 1774 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = SParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1775
                self.match(SParser.DOT)
                self.state = 1776 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = SParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1777 
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
            super(SParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(SParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(SParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = SParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1780 
            localctx.name = self.javascript_identifier()
            self.state = 1781
            self.match(SParser.LPAR)
            self.state = 1783
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.SELF - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.THIS - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.BOOLEAN_LITERAL - 118)) | (1 << (SParser.CHAR_LITERAL - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)) | (1 << (SParser.DOLLAR_IDENTIFIER - 118)) | (1 << (SParser.TEXT_LITERAL - 118)) | (1 << (SParser.INTEGER_LITERAL - 118)) | (1 << (SParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 1782 
                localctx.args = self.javascript_arguments(0)


            self.state = 1785
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_argumentsContext)
            super(SParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_argumentsContext)
            super(SParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(SParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 296
        self.enterRecursionRule(localctx, 296, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1788 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1795
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptArgumentListItemContext(self, SParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1790
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1791
                    self.match(SParser.COMMA)
                    self.state = 1792 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1797
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
            super(SParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = SParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1798
            self.match(SParser.LBRAK)
            self.state = 1799 
            localctx.exp = self.javascript_expression(0)
            self.state = 1800
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = SParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1802
            self.match(SParser.LPAR)
            self.state = 1803 
            localctx.exp = self.javascript_expression(0)
            self.state = 1804
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(SParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = SParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1806 
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
            super(SParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = SParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_javascript_literal_expression)
        try:
            self.state = 1813
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1808
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1809
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1810
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1811
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1812
                localctx.t = self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def getRuleIndex(self):
            return SParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = SParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1815
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)) | (1 << (SParser.DOLLAR_IDENTIFIER - 118)))) != 0)):
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
            super(SParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(SParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_statementContext)
            super(SParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_statementContext)
            super(SParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = SParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_python_statement)
        try:
            self.state = 1820
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1817
                self.match(SParser.RETURN)
                self.state = 1818 
                localctx.exp = self.python_expression(0)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1819 
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
            super(SParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_expressionContext)
            super(SParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(SParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_expressionContext)
            super(SParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(SParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1823 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1829
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,132,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonSelectorExpressionContext(self, SParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1825
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1826 
                    localctx.child = self.python_selector_expression() 
                self.state = 1831
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,132,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(SParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(SParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = SParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_python_primary_expression)
        try:
            self.state = 1836
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1832 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1833 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1834 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = SParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1835 
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
            super(SParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_selector_expressionContext)
            super(SParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(SParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_selector_expressionContext)
            super(SParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = SParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_python_selector_expression)
        try:
            self.state = 1844
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1838
                self.match(SParser.DOT)
                self.state = 1839 
                localctx.exp = self.python_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1840
                self.match(SParser.LBRAK)
                self.state = 1841 
                localctx.exp = self.python_expression(0)
                self.state = 1842
                self.match(SParser.RBRAK)

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
            super(SParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = SParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1846 
            localctx.name = self.python_identifier()
            self.state = 1847
            self.match(SParser.LPAR)
            self.state = 1849
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.SELF - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.THIS - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.BOOLEAN_LITERAL - 118)) | (1 << (SParser.CHAR_LITERAL - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)) | (1 << (SParser.DOLLAR_IDENTIFIER - 118)) | (1 << (SParser.TEXT_LITERAL - 118)) | (1 << (SParser.INTEGER_LITERAL - 118)) | (1 << (SParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 1848 
                localctx.args = self.python_argument_list()


            self.state = 1851
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_argument_listContext)
            super(SParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_argument_listContext)
            super(SParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_argument_listContext)
            super(SParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = SParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_python_argument_list)
        try:
            self.state = 1859
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1853 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = SParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1854 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1855 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1856
                self.match(SParser.COMMA)
                self.state = 1857 
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
            super(SParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_ordinal_argument_listContext)
            super(SParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_ordinal_argument_listContext)
            super(SParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1862 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1869
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonOrdinalArgumentListItemContext(self, SParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1864
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1865
                    self.match(SParser.COMMA)
                    self.state = 1866 
                    localctx.item = self.python_expression(0) 
                self.state = 1871
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_named_argument_listContext)
            super(SParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(SParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_named_argument_listContext)
            super(SParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def EQ(self):
            return self.getToken(SParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1873 
            localctx.name = self.python_identifier()
            self.state = 1874
            self.match(SParser.EQ)
            self.state = 1875 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1885
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonNamedArgumentListItemContext(self, SParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1877
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1878
                    self.match(SParser.COMMA)
                    self.state = 1879 
                    localctx.name = self.python_identifier()
                    self.state = 1880
                    self.match(SParser.EQ)
                    self.state = 1881 
                    localctx.exp = self.python_expression(0) 
                self.state = 1887
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = SParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
            self.match(SParser.LPAR)
            self.state = 1889 
            localctx.exp = self.python_expression(0)
            self.state = 1890
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_identifier_expressionContext)
            super(SParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_identifier_expressionContext)
            super(SParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_identifier_expressionContext)
            super(SParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1895
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1893
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1894 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1902
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonChildIdentifierContext(self, SParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1897
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1898
                    self.match(SParser.DOT)
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
            super(SParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = SParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_python_literal_expression)
        try:
            self.state = 1910
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1905
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1906
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1907
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1908
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1909
                localctx.t = self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def SELF(self):
            return self.getToken(SParser.SELF, 0)

        def THIS(self):
            return self.getToken(SParser.THIS, 0)

        def getRuleIndex(self):
            return SParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = SParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1912
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.SELF - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.THIS - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)))) != 0)):
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
            super(SParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(SParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_statementContext)
            super(SParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_statementContext)
            super(SParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = SParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_java_statement)
        try:
            self.state = 1921
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1914
                self.match(SParser.RETURN)
                self.state = 1915 
                localctx.exp = self.java_expression(0)
                self.state = 1916
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.NATIVE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1918 
                localctx.exp = self.java_expression(0)
                self.state = 1919
                self.match(SParser.SEMI)

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
            super(SParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_expressionContext)
            super(SParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(SParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_expressionContext)
            super(SParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(SParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaPrimaryExpressionContext(self, localctx)
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
                    localctx = SParser.JavaSelectorExpressionContext(self, SParser.Java_expressionContext(self, _parentctx, _parentState))
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
            super(SParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(SParser.Java_this_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(SParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = SParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_java_primary_expression)
        try:
            self.state = 1937
            token = self._input.LA(1)
            if token in [SParser.SELF, SParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1933 
                self.java_this_expression()

            elif token in [SParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1934 
                self.java_parenthesis_expression()

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.TEST, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.NATIVE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1935 
                self.java_identifier_expression(0)

            elif token in [SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1936 
                self.java_literal_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = SParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1939 
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_selector_expressionContext)
            super(SParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(SParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_selector_expressionContext)
            super(SParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(SParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = SParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_java_selector_expression)
        try:
            self.state = 1944
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1941
                self.match(SParser.DOT)
                self.state = 1942 
                localctx.exp = self.java_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1943 
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
            super(SParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(SParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(SParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = SParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946 
            localctx.name = self.java_identifier()
            self.state = 1947
            self.match(SParser.LPAR)
            self.state = 1949
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.SELF - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.THIS - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.BOOLEAN_LITERAL - 118)) | (1 << (SParser.CHAR_LITERAL - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)) | (1 << (SParser.NATIVE_IDENTIFIER - 118)) | (1 << (SParser.DOLLAR_IDENTIFIER - 118)) | (1 << (SParser.TEXT_LITERAL - 118)) | (1 << (SParser.INTEGER_LITERAL - 118)) | (1 << (SParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 1948 
                localctx.args = self.java_arguments(0)


            self.state = 1951
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_argumentsContext)
            super(SParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(SParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_argumentsContext)
            super(SParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1954 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1961
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,147,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaArgumentListItemContext(self, SParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 1956
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1957
                    self.match(SParser.COMMA)
                    self.state = 1958 
                    localctx.item = self.java_expression(0) 
                self.state = 1963
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
            super(SParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_item_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = SParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1964
            self.match(SParser.LBRAK)
            self.state = 1965 
            localctx.exp = self.java_expression(0)
            self.state = 1966
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = SParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1968
            self.match(SParser.LPAR)
            self.state = 1969 
            localctx.exp = self.java_expression(0)
            self.state = 1970
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_identifier_expressionContext)
            super(SParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(SParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_identifier_expressionContext)
            super(SParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(SParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1973 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1980
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,148,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildIdentifierContext(self, SParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 1975
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1976
                    self.match(SParser.DOT)
                    self.state = 1977 
                    localctx.name = self.java_identifier() 
                self.state = 1982
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
            super(SParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_class_identifier_expressionContext)
            super(SParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_class_identifier_expressionContext)
            super(SParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1984 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1990
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,149,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildClassIdentifierContext(self, SParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 1986
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1987
                    localctx.name = self.match(SParser.DOLLAR_IDENTIFIER) 
                self.state = 1992
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
            super(SParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = SParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_java_literal_expression)
        try:
            self.state = 1998
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1993
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1994
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1995
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1996
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1997
                localctx.t = self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(SParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def getRuleIndex(self):
            return SParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = SParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2000
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)) | (1 << (SParser.NATIVE_IDENTIFIER - 118)) | (1 << (SParser.DOLLAR_IDENTIFIER - 118)))) != 0)):
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
            super(SParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_statementContext)
            super(SParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_statementContext)
            super(SParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = SParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_csharp_statement)
        try:
            self.state = 2009
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2002
                self.match(SParser.RETURN)
                self.state = 2003 
                localctx.exp = self.csharp_expression(0)
                self.state = 2004
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2006 
                localctx.exp = self.csharp_expression(0)
                self.state = 2007
                self.match(SParser.SEMI)

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
            super(SParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_expressionContext)
            super(SParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_expressionContext)
            super(SParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2012 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2018
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpSelectorExpressionContext(self, SParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2014
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2015 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2020
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
            super(SParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_this_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = SParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_csharp_primary_expression)
        try:
            self.state = 2025
            token = self._input.LA(1)
            if token in [SParser.SELF, SParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2021 
                self.csharp_this_expression()

            elif token in [SParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2022 
                self.csharp_parenthesis_expression()

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.TEST, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2023 
                self.csharp_identifier_expression(0)

            elif token in [SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2024 
                self.csharp_literal_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = SParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2027 
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_selector_expressionContext)
            super(SParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_selector_expressionContext)
            super(SParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = SParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_csharp_selector_expression)
        try:
            self.state = 2032
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2029
                self.match(SParser.DOT)
                self.state = 2030 
                localctx.exp = self.csharp_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2031 
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
            super(SParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(SParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(SParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = SParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2034 
            localctx.name = self.csharp_identifier()
            self.state = 2035
            self.match(SParser.LPAR)
            self.state = 2037
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.SELF - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.THIS - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.BOOLEAN_LITERAL - 118)) | (1 << (SParser.CHAR_LITERAL - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)) | (1 << (SParser.DOLLAR_IDENTIFIER - 118)) | (1 << (SParser.TEXT_LITERAL - 118)) | (1 << (SParser.INTEGER_LITERAL - 118)) | (1 << (SParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 2036 
                localctx.args = self.csharp_arguments(0)


            self.state = 2039
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_argumentsContext)
            super(SParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_argumentsContext)
            super(SParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(SParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2042 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2049
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpArgumentListItemContext(self, SParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2044
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2045
                    self.match(SParser.COMMA)
                    self.state = 2046 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2051
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
            super(SParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = SParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2052
            self.match(SParser.LBRAK)
            self.state = 2053 
            localctx.exp = self.csharp_expression(0)
            self.state = 2054
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = SParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2056
            self.match(SParser.LPAR)
            self.state = 2057 
            localctx.exp = self.csharp_expression(0)
            self.state = 2058
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_identifier_expressionContext)
            super(SParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(SParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_identifier_expressionContext)
            super(SParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(SParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_identifier_expressionContext)
            super(SParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2063
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2061
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.TEST, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2062 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2070
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpChildIdentifierContext(self, SParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2065
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2066
                    self.match(SParser.DOT)
                    self.state = 2067 
                    localctx.name = self.csharp_identifier() 
                self.state = 2072
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = SParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_csharp_literal_expression)
        try:
            self.state = 2078
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2073
                self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2074
                self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2075
                self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2076
                self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2077
                self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def getRuleIndex(self):
            return SParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = SParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2080
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SParser.READ - 118)) | (1 << (SParser.TEST - 118)) | (1 << (SParser.WRITE - 118)) | (1 << (SParser.SYMBOL_IDENTIFIER - 118)) | (1 << (SParser.TYPE_IDENTIFIER - 118)) | (1 << (SParser.VARIABLE_IDENTIFIER - 118)))) != 0)):
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
        self._predicates[26] = self.callable_parent_sempred
        self._predicates[36] = self.else_if_statement_list_sempred
        self._predicates[41] = self.expression_sempred
        self._predicates[43] = self.instance_expression_sempred
        self._predicates[45] = self.instance_selector_sempred
        self._predicates[48] = self.argument_assignment_list_sempred
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
        self._predicates[95] = self.member_method_declaration_list_sempred
        self._predicates[97] = self.native_member_method_declaration_list_sempred
        self._predicates[102] = self.module_token_sempred
        self._predicates[105] = self.variable_identifier_list_sempred
        self._predicates[108] = self.native_statement_list_sempred
        self._predicates[112] = self.statement_list_sempred
        self._predicates[113] = self.assertion_list_sempred
        self._predicates[114] = self.switch_case_statement_list_sempred
        self._predicates[115] = self.catch_statement_list_sempred
        self._predicates[118] = self.literal_list_literal_sempred
        self._predicates[126] = self.expression_tuple_sempred
        self._predicates[127] = self.dict_entry_list_sempred
        self._predicates[131] = self.assignable_instance_sempred
        self._predicates[132] = self.is_expression_sempred
        self._predicates[134] = self.key_token_sempred
        self._predicates[135] = self.value_token_sempred
        self._predicates[136] = self.symbols_token_sempred
        self._predicates[143] = self.javascript_expression_sempred
        self._predicates[148] = self.javascript_arguments_sempred
        self._predicates[155] = self.python_expression_sempred
        self._predicates[160] = self.python_ordinal_argument_list_sempred
        self._predicates[161] = self.python_named_argument_list_sempred
        self._predicates[163] = self.python_identifier_expression_sempred
        self._predicates[167] = self.java_expression_sempred
        self._predicates[172] = self.java_arguments_sempred
        self._predicates[175] = self.java_identifier_expression_sempred
        self._predicates[176] = self.java_class_identifier_expression_sempred
        self._predicates[180] = self.csharp_expression_sempred
        self._predicates[185] = self.csharp_arguments_sempred
        self._predicates[188] = self.csharp_identifier_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def callable_parent_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 12)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 29:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.wasNot(SParser.WS)
         

            if predIndex == 31:
                return self.wasNot(SParser.WS)
         

            if predIndex == 32:
                return self.wasNot(SParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 34:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.wasNot(SParser.WS)
         

            if predIndex == 36:
                return self.wasNot(SParser.WS)
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def assertion_list_sempred(self, localctx, predIndex):
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
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 78:
                return self.precpred(self._ctx, 1)
         



