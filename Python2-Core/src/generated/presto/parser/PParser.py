# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .PParserListener import PParserListener
else:
    from PParserListener import PParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u0097\u07ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\t\u00b6\4\u00b7\t\u00b7\3\2\3\2\3\2\3\2\3\2\3\2\5\2")
        buf.write(u"\u0175\n\2\3\2\5\2\u0178\n\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write(u"\3\4\3\5\3\5\3\5\5\5\u0191\n\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\5\6\u019e\n\6\3\6\3\6\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01ab\n\7\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\5\7\u01b2\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\5\b\u01bf\n\b\3\b\3\b\3\t\3\t\3\n\3")
        buf.write(u"\n\3\n\3\n\5\n\u01c9\n\n\3\n\3\n\3\n\5\n\u01ce\n\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\5\13\u01dd\n\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write(u"\u01fd\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\5\17\u020a\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\7\21\u021f\n\21\f\21\16\21\u0222\13")
        buf.write(u"\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u022b\n\23")
        buf.write(u"\3\23\3\23\3\23\5\23\u0230\n\23\3\24\3\24\3\24\3\24\5")
        buf.write(u"\24\u0236\n\24\3\24\3\24\3\24\5\24\u023b\n\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u0247")
        buf.write(u"\n\25\3\25\3\25\3\25\5\25\u024c\n\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u025a")
        buf.write(u"\n\26\3\26\3\26\5\26\u025e\n\26\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\5\27\u026f\n\27\3\30\3\30\3\30\5\30\u0274\n\30\3\30")
        buf.write(u"\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u027d\n\31\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\7\32\u0284\n\32\f\32\16\32\u0287\13")
        buf.write(u"\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u028f\n\33\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\5\36\u02ac\n\36\3\36\3\36\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\5\37\u02bf\n\37\3 \3 \3 \3 \5 \u02c5")
        buf.write(u"\n \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write(u"\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write(u"#\5#\u02e7\n#\3#\3#\3#\3#\3#\3#\3#\5#\u02f0\n#\3$\3$")
        buf.write(u"\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7")
        buf.write(u"$\u0305\n$\f$\16$\u0308\13$\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write(u"&\3&\3&\5&\u0315\n&\3&\3&\3&\3&\3&\3&\3&\5&\u031e\n&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3&\5&\u0327\n&\3&\3&\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\5\'\u033e\n\'\3(\3(\5(\u0342\n(\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0356")
        buf.write(u"\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\7)\u03b6\n)\f)\16)\u03b9\13)\3")
        buf.write(u"*\3*\3+\3+\3+\3+\3+\7+\u03c2\n+\f+\16+\u03c5\13+\3,\3")
        buf.write(u",\3,\3,\3,\3,\5,\u03cd\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\5-\u03dc\n-\3.\3.\3/\3/\3/\5/\u03e3\n/\3")
        buf.write(u"/\3/\3\60\3\60\3\60\3\60\3\60\5\60\u03ec\n\60\3\60\3")
        buf.write(u"\60\3\60\7\60\u03f1\n\60\f\60\16\60\u03f4\13\60\3\61")
        buf.write(u"\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0412\n\65\3\65\3")
        buf.write(u"\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\5\67\u0422\n\67\38\38\38\38\39\79\u0429\n")
        buf.write(u"9\f9\169\u042c\139\3:\6:\u042f\n:\r:\16:\u0430\3;\6;")
        buf.write(u"\u0434\n;\r;\16;\u0435\3;\3;\3<\7<\u043b\n<\f<\16<\u043e")
        buf.write(u"\13<\3<\3<\3=\3=\3>\5>\u0445\n>\3>\3>\3>\3?\3?\3?\3?")
        buf.write(u"\3?\3?\3?\7?\u0451\n?\f?\16?\u0454\13?\3@\3@\3@\3@\3")
        buf.write(u"@\5@\u045b\n@\3A\3A\3B\3B\5B\u0461\nB\3C\3C\3C\3C\3C")
        buf.write(u"\3C\3C\7C\u046a\nC\fC\16C\u046d\13C\3D\3D\3D\3D\3D\3")
        buf.write(u"D\3D\7D\u0476\nD\fD\16D\u0479\13D\3E\3E\3E\3E\3E\3E\7")
        buf.write(u"E\u0481\nE\fE\16E\u0484\13E\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write(u"F\3F\5F\u0490\nF\3G\3G\5G\u0494\nG\3G\3G\3H\3H\5H\u049a")
        buf.write(u"\nH\3H\3H\3I\3I\3I\3I\3I\3I\7I\u04a4\nI\fI\16I\u04a7")
        buf.write(u"\13I\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K")
        buf.write(u"\3K\7K\u04ba\nK\fK\16K\u04bd\13K\3L\3L\5L\u04c1\nL\3")
        buf.write(u"M\3M\3M\3M\3M\3M\3M\3M\3M\3M\5M\u04cd\nM\3N\3N\3O\3O")
        buf.write(u"\3P\3P\3Q\3Q\3Q\5Q\u04d8\nQ\3R\3R\3R\3R\3R\3R\7R\u04e0")
        buf.write(u"\nR\fR\16R\u04e3\13R\3S\3S\5S\u04e7\nS\3T\3T\3T\5T\u04ec")
        buf.write(u"\nT\3U\3U\3V\3V\3W\3W\3X\3X\3X\3X\3X\3X\7X\u04fa\nX\f")
        buf.write(u"X\16X\u04fd\13X\3Y\3Y\5Y\u0501\nY\3Z\3Z\5Z\u0505\nZ\3")
        buf.write(u"[\3[\3[\5[\u050a\n[\3\\\3\\\3\\\3]\3]\5]\u0511\n]\3^")
        buf.write(u"\3^\3^\3^\3^\3^\3^\3^\3^\7^\u051c\n^\f^\16^\u051f\13")
        buf.write(u"^\3_\3_\3_\3_\3_\3_\3_\7_\u0528\n_\f_\16_\u052b\13_\3")
        buf.write(u"`\3`\3`\3`\5`\u0531\n`\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a")
        buf.write(u"\5a\u053d\na\3b\3b\5b\u0541\nb\3c\3c\3c\3c\3c\3c\7c\u0549")
        buf.write(u"\nc\fc\16c\u054c\13c\3d\3d\3d\3e\3e\5e\u0553\ne\3f\3")
        buf.write(u"f\3f\3f\5f\u0559\nf\3f\3f\3f\7f\u055e\nf\ff\16f\u0561")
        buf.write(u"\13f\3f\3f\5f\u0565\nf\3g\3g\3g\3g\3g\3g\7g\u056d\ng")
        buf.write(u"\fg\16g\u0570\13g\3h\3h\3h\5h\u0575\nh\3i\3i\3i\3i\3")
        buf.write(u"i\3i\3i\7i\u057e\ni\fi\16i\u0581\13i\3j\3j\3j\3j\3j\3")
        buf.write(u"j\3j\3j\3j\3j\5j\u058d\nj\3k\3k\5k\u0591\nk\3k\5k\u0594")
        buf.write(u"\nk\3l\3l\5l\u0598\nl\3l\5l\u059b\nl\3m\3m\3m\3m\3m\3")
        buf.write(u"m\3m\7m\u05a4\nm\fm\16m\u05a7\13m\3n\3n\3n\3n\3n\3n\3")
        buf.write(u"n\7n\u05b0\nn\fn\16n\u05b3\13n\3o\3o\3o\3o\3o\3o\3o\7")
        buf.write(u"o\u05bc\no\fo\16o\u05bf\13o\3p\3p\3p\3p\3p\3p\3p\3p\3")
        buf.write(u"p\3p\3p\3p\3p\3p\5p\u05cf\np\3q\3q\3q\3q\3q\3q\3q\3q")
        buf.write(u"\3q\3q\3q\3q\3q\5q\u05de\nq\3r\3r\3r\3r\3r\3r\7r\u05e6")
        buf.write(u"\nr\fr\16r\u05e9\13r\3s\3s\3s\3s\5s\u05ef\ns\3t\3t\3")
        buf.write(u"u\3u\3u\3u\3v\3v\5v\u05f9\nv\3w\3w\3w\3w\3w\5w\u0600")
        buf.write(u"\nw\3x\3x\5x\u0604\nx\3x\3x\3y\3y\5y\u060a\ny\3y\3y\3")
        buf.write(u"z\3z\3z\3z\3z\3z\7z\u0614\nz\fz\16z\u0617\13z\3{\3{\3")
        buf.write(u"{\3{\3{\3{\7{\u061f\n{\f{\16{\u0622\13{\3|\3|\3|\3|\3")
        buf.write(u"}\3}\3}\3}\3}\3}\3}\3}\3}\5}\u0631\n}\3~\3~\3~\3~\3\177")
        buf.write(u"\3\177\3\177\3\177\3\177\7\177\u063c\n\177\f\177\16\177")
        buf.write(u"\u063f\13\177\3\u0080\3\u0080\3\u0080\3\u0080\5\u0080")
        buf.write(u"\u0645\n\u0080\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081")
        buf.write(u"\3\u0081\5\u0081\u064d\n\u0081\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0084\3\u0084\3\u0084\3\u0085")
        buf.write(u"\3\u0085\3\u0086\3\u0086\3\u0087\3\u0087\3\u0088\3\u0088")
        buf.write(u"\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008a\3\u008a\5\u008a\u0669\n\u008a\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\7\u008b\u0670\n\u008b\f\u008b")
        buf.write(u"\16\u008b\u0673\13\u008b\3\u008c\3\u008c\3\u008c\5\u008c")
        buf.write(u"\u0678\n\u008c\3\u008d\3\u008d\3\u008d\5\u008d\u067d")
        buf.write(u"\n\u008d\3\u008e\3\u008e\3\u008e\5\u008e\u0682\n\u008e")
        buf.write(u"\3\u008e\3\u008e\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u008f\7\u008f\u068c\n\u008f\f\u008f\16\u008f\u068f")
        buf.write(u"\13\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\7\u0092\u069f\n\u0092\f\u0092\16\u0092\u06a2")
        buf.write(u"\13\u0092\3\u0093\3\u0093\3\u0093\3\u0093\3\u0093\5\u0093")
        buf.write(u"\u06a9\n\u0093\3\u0094\3\u0094\3\u0095\3\u0095\3\u0095")
        buf.write(u"\5\u0095\u06b0\n\u0095\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write(u"\3\u0096\7\u0096\u06b7\n\u0096\f\u0096\16\u0096\u06ba")
        buf.write(u"\13\u0096\3\u0097\3\u0097\3\u0097\3\u0097\5\u0097\u06c0")
        buf.write(u"\n\u0097\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write(u"\5\u0098\u06c8\n\u0098\3\u0099\3\u0099\3\u0099\5\u0099")
        buf.write(u"\u06cd\n\u0099\3\u0099\3\u0099\3\u009a\3\u009a\3\u009a")
        buf.write(u"\3\u009a\3\u009a\3\u009a\5\u009a\u06d7\n\u009a\3\u009b")
        buf.write(u"\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\7\u009b\u06df")
        buf.write(u"\n\u009b\f\u009b\16\u009b\u06e2\13\u009b\3\u009c\3\u009c")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c")
        buf.write(u"\3\u009c\3\u009c\7\u009c\u06ef\n\u009c\f\u009c\16\u009c")
        buf.write(u"\u06f2\13\u009c\3\u009d\3\u009d\3\u009d\3\u009d\3\u009e")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\7\u009e\u06fe")
        buf.write(u"\n\u009e\f\u009e\16\u009e\u0701\13\u009e\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u009f\5\u009f\u0708\n\u009f\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write(u"\3\u00a1\5\u00a1\u0713\n\u00a1\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\3\u00a2\7\u00a2\u071a\n\u00a2\f\u00a2\16\u00a2")
        buf.write(u"\u071d\13\u00a2\3\u00a3\3\u00a3\3\u00a3\5\u00a3\u0722")
        buf.write(u"\n\u00a3\3\u00a4\3\u00a4\3\u00a4\5\u00a4\u0727\n\u00a4")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u072c\n\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\7\u00a6\u0736\n\u00a6\f\u00a6\16\u00a6\u0739\13\u00a6")
        buf.write(u"\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\7\u00a9\u0749\n\u00a9\f\u00a9\16\u00a9\u074c\13\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\7\u00aa")
        buf.write(u"\u0754\n\u00aa\f\u00aa\16\u00aa\u0757\13\u00aa\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u075e\n\u00ab")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write(u"\3\u00ad\3\u00ad\5\u00ad\u0769\n\u00ad\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\7\u00ae\u0770\n\u00ae\f\u00ae")
        buf.write(u"\16\u00ae\u0773\13\u00ae\3\u00af\3\u00af\3\u00af\5\u00af")
        buf.write(u"\u0778\n\u00af\3\u00b0\3\u00b0\3\u00b0\5\u00b0\u077d")
        buf.write(u"\n\u00b0\3\u00b1\3\u00b1\3\u00b1\5\u00b1\u0782\n\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\7\u00b2\u078c\n\u00b2\f\u00b2\16\u00b2\u078f")
        buf.write(u"\13\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\7\u00b5\u079f\n\u00b5\f\u00b5\16\u00b5\u07a2")
        buf.write(u"\13\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\5\u00b6")
        buf.write(u"\u07a9\n\u00b6\3\u00b7\3\u00b7\3\u00b7\2) \62FPT^|\u0084")
        buf.write(u"\u0086\u0088\u0090\u0094\u00a2\u00ae\u00ba\u00bc\u00cc")
        buf.write(u"\u00d0\u00d8\u00da\u00dc\u00e2\u00f2\u00f4\u00fc\u0114")
        buf.write(u"\u011c\u0122\u012a\u0134\u0136\u013a\u0142\u014a\u0150")
        buf.write(u"\u0152\u015a\u0162\u0168\u00b8\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV")
        buf.write(u"XZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write(u"\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write(u"\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae")
        buf.write(u"\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0")
        buf.write(u"\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2")
        buf.write(u"\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4")
        buf.write(u"\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6")
        buf.write(u"\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108")
        buf.write(u"\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118\u011a")
        buf.write(u"\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a\u012c")
        buf.write(u"\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c\u013e")
        buf.write(u"\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e\u0150")
        buf.write(u"\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160\u0162")
        buf.write(u"\u0164\u0166\u0168\u016a\u016c\2\b\3\2KL\3\2\"#\4\2z")
        buf.write(u"z\177\177\4\2\'\'hh\6\2\64<uu\u0087\u0087\u008c\u008e")
        buf.write(u"\4\2\64<\u008c\u008e\u07fb\2\u016e\3\2\2\2\4\u017f\3")
        buf.write(u"\2\2\2\6\u0189\3\2\2\2\b\u018d\3\2\2\2\n\u0194\3\2\2")
        buf.write(u"\2\f\u01a1\3\2\2\2\16\u01b5\3\2\2\2\20\u01c2\3\2\2\2")
        buf.write(u"\22\u01c4\3\2\2\2\24\u01d4\3\2\2\2\26\u01e3\3\2\2\2\30")
        buf.write(u"\u01ed\3\2\2\2\32\u01f7\3\2\2\2\34\u0204\3\2\2\2\36\u0211")
        buf.write(u"\3\2\2\2 \u0217\3\2\2\2\"\u0223\3\2\2\2$\u0225\3\2\2")
        buf.write(u"\2&\u0231\3\2\2\2(\u0241\3\2\2\2*\u0252\3\2\2\2,\u026e")
        buf.write(u"\3\2\2\2.\u0270\3\2\2\2\60\u027c\3\2\2\2\62\u027e\3\2")
        buf.write(u"\2\2\64\u028e\3\2\2\2\66\u0290\3\2\2\28\u0297\3\2\2\2")
        buf.write(u":\u029e\3\2\2\2<\u02be\3\2\2\2>\u02c0\3\2\2\2@\u02cd")
        buf.write(u"\3\2\2\2B\u02d6\3\2\2\2D\u02dd\3\2\2\2F\u02f1\3\2\2\2")
        buf.write(u"H\u0309\3\2\2\2J\u030c\3\2\2\2L\u033d\3\2\2\2N\u033f")
        buf.write(u"\3\2\2\2P\u0355\3\2\2\2R\u03ba\3\2\2\2T\u03bc\3\2\2\2")
        buf.write(u"V\u03cc\3\2\2\2X\u03db\3\2\2\2Z\u03dd\3\2\2\2\\\u03df")
        buf.write(u"\3\2\2\2^\u03eb\3\2\2\2`\u03f5\3\2\2\2b\u03f9\3\2\2\2")
        buf.write(u"d\u03fd\3\2\2\2f\u0402\3\2\2\2h\u0409\3\2\2\2j\u0415")
        buf.write(u"\3\2\2\2l\u0421\3\2\2\2n\u0423\3\2\2\2p\u042a\3\2\2\2")
        buf.write(u"r\u042e\3\2\2\2t\u0433\3\2\2\2v\u043c\3\2\2\2x\u0441")
        buf.write(u"\3\2\2\2z\u0444\3\2\2\2|\u0449\3\2\2\2~\u045a\3\2\2\2")
        buf.write(u"\u0080\u045c\3\2\2\2\u0082\u0460\3\2\2\2\u0084\u0462")
        buf.write(u"\3\2\2\2\u0086\u046e\3\2\2\2\u0088\u047a\3\2\2\2\u008a")
        buf.write(u"\u048f\3\2\2\2\u008c\u0491\3\2\2\2\u008e\u0497\3\2\2")
        buf.write(u"\2\u0090\u049d\3\2\2\2\u0092\u04a8\3\2\2\2\u0094\u04ae")
        buf.write(u"\3\2\2\2\u0096\u04c0\3\2\2\2\u0098\u04cc\3\2\2\2\u009a")
        buf.write(u"\u04ce\3\2\2\2\u009c\u04d0\3\2\2\2\u009e\u04d2\3\2\2")
        buf.write(u"\2\u00a0\u04d7\3\2\2\2\u00a2\u04d9\3\2\2\2\u00a4\u04e6")
        buf.write(u"\3\2\2\2\u00a6\u04eb\3\2\2\2\u00a8\u04ed\3\2\2\2\u00aa")
        buf.write(u"\u04ef\3\2\2\2\u00ac\u04f1\3\2\2\2\u00ae\u04f3\3\2\2")
        buf.write(u"\2\u00b0\u0500\3\2\2\2\u00b2\u0504\3\2\2\2\u00b4\u0506")
        buf.write(u"\3\2\2\2\u00b6\u050b\3\2\2\2\u00b8\u0510\3\2\2\2\u00ba")
        buf.write(u"\u0512\3\2\2\2\u00bc\u0520\3\2\2\2\u00be\u0530\3\2\2")
        buf.write(u"\2\u00c0\u053c\3\2\2\2\u00c2\u053e\3\2\2\2\u00c4\u0542")
        buf.write(u"\3\2\2\2\u00c6\u054d\3\2\2\2\u00c8\u0550\3\2\2\2\u00ca")
        buf.write(u"\u0554\3\2\2\2\u00cc\u0566\3\2\2\2\u00ce\u0574\3\2\2")
        buf.write(u"\2\u00d0\u0576\3\2\2\2\u00d2\u058c\3\2\2\2\u00d4\u058e")
        buf.write(u"\3\2\2\2\u00d6\u0595\3\2\2\2\u00d8\u059c\3\2\2\2\u00da")
        buf.write(u"\u05a8\3\2\2\2\u00dc\u05b4\3\2\2\2\u00de\u05ce\3\2\2")
        buf.write(u"\2\u00e0\u05dd\3\2\2\2\u00e2\u05df\3\2\2\2\u00e4\u05ee")
        buf.write(u"\3\2\2\2\u00e6\u05f0\3\2\2\2\u00e8\u05f2\3\2\2\2\u00ea")
        buf.write(u"\u05f8\3\2\2\2\u00ec\u05ff\3\2\2\2\u00ee\u0601\3\2\2")
        buf.write(u"\2\u00f0\u0607\3\2\2\2\u00f2\u060d\3\2\2\2\u00f4\u0618")
        buf.write(u"\3\2\2\2\u00f6\u0623\3\2\2\2\u00f8\u0630\3\2\2\2\u00fa")
        buf.write(u"\u0632\3\2\2\2\u00fc\u0636\3\2\2\2\u00fe\u0644\3\2\2")
        buf.write(u"\2\u0100\u064c\3\2\2\2\u0102\u064e\3\2\2\2\u0104\u0651")
        buf.write(u"\3\2\2\2\u0106\u0654\3\2\2\2\u0108\u0657\3\2\2\2\u010a")
        buf.write(u"\u0659\3\2\2\2\u010c\u065b\3\2\2\2\u010e\u065d\3\2\2")
        buf.write(u"\2\u0110\u065f\3\2\2\2\u0112\u0668\3\2\2\2\u0114\u066a")
        buf.write(u"\3\2\2\2\u0116\u0677\3\2\2\2\u0118\u067c\3\2\2\2\u011a")
        buf.write(u"\u067e\3\2\2\2\u011c\u0685\3\2\2\2\u011e\u0690\3\2\2")
        buf.write(u"\2\u0120\u0694\3\2\2\2\u0122\u0698\3\2\2\2\u0124\u06a8")
        buf.write(u"\3\2\2\2\u0126\u06aa\3\2\2\2\u0128\u06af\3\2\2\2\u012a")
        buf.write(u"\u06b1\3\2\2\2\u012c\u06bf\3\2\2\2\u012e\u06c7\3\2\2")
        buf.write(u"\2\u0130\u06c9\3\2\2\2\u0132\u06d6\3\2\2\2\u0134\u06d8")
        buf.write(u"\3\2\2\2\u0136\u06e3\3\2\2\2\u0138\u06f3\3\2\2\2\u013a")
        buf.write(u"\u06f7\3\2\2\2\u013c\u0707\3\2\2\2\u013e\u0709\3\2\2")
        buf.write(u"\2\u0140\u0712\3\2\2\2\u0142\u0714\3\2\2\2\u0144\u0721")
        buf.write(u"\3\2\2\2\u0146\u0726\3\2\2\2\u0148\u0728\3\2\2\2\u014a")
        buf.write(u"\u072f\3\2\2\2\u014c\u073a\3\2\2\2\u014e\u073e\3\2\2")
        buf.write(u"\2\u0150\u0742\3\2\2\2\u0152\u074d\3\2\2\2\u0154\u075d")
        buf.write(u"\3\2\2\2\u0156\u075f\3\2\2\2\u0158\u0768\3\2\2\2\u015a")
        buf.write(u"\u076a\3\2\2\2\u015c\u0777\3\2\2\2\u015e\u077c\3\2\2")
        buf.write(u"\2\u0160\u077e\3\2\2\2\u0162\u0785\3\2\2\2\u0164\u0790")
        buf.write(u"\3\2\2\2\u0166\u0794\3\2\2\2\u0168\u0798\3\2\2\2\u016a")
        buf.write(u"\u07a8\3\2\2\2\u016c\u07aa\3\2\2\2\u016e\u016f\7V\2\2")
        buf.write(u"\u016f\u0170\5\u00aaV\2\u0170\u0177\7\25\2\2\u0171\u0174")
        buf.write(u"\5\u00aaV\2\u0172\u0173\7\22\2\2\u0173\u0175\5\"\22\2")
        buf.write(u"\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0178")
        buf.write(u"\3\2\2\2\u0176\u0178\5\"\22\2\u0177\u0171\3\2\2\2\u0177")
        buf.write(u"\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\7\26\2")
        buf.write(u"\2\u017a\u017b\7\20\2\2\u017b\u017c\5t;\2\u017c\u017d")
        buf.write(u"\5\u0086D\2\u017d\u017e\5v<\2\u017e\3\3\2\2\2\u017f\u0180")
        buf.write(u"\7V\2\2\u0180\u0181\5\u00aaV\2\u0181\u0182\7\25\2\2\u0182")
        buf.write(u"\u0183\5\u0098M\2\u0183\u0184\7\26\2\2\u0184\u0185\7")
        buf.write(u"\20\2\2\u0185\u0186\5t;\2\u0186\u0187\5\u0084C\2\u0187")
        buf.write(u"\u0188\5v<\2\u0188\5\3\2\2\2\u0189\u018a\5\u00acW\2\u018a")
        buf.write(u"\u018b\7-\2\2\u018b\u018c\5P)\2\u018c\7\3\2\2\2\u018d")
        buf.write(u"\u018e\5\u00acW\2\u018e\u0190\7\25\2\2\u018f\u0191\5")
        buf.write(u"^\60\2\u0190\u018f\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write(u"\u0192\3\2\2\2\u0192\u0193\7\26\2\2\u0193\t\3\2\2\2\u0194")
        buf.write(u"\u0195\7F\2\2\u0195\u0196\5\u00a8U\2\u0196\u0197\7\25")
        buf.write(u"\2\2\u0197\u0198\5\u0094K\2\u0198\u0199\7\26\2\2\u0199")
        buf.write(u"\u019a\7\20\2\2\u019a\u019d\5t;\2\u019b\u019e\5\u008a")
        buf.write(u"F\2\u019c\u019e\7s\2\2\u019d\u019b\3\2\2\2\u019d\u019c")
        buf.write(u"\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\5v<\2\u01a0")
        buf.write(u"\13\3\2\2\2\u01a1\u01a2\t\2\2\2\u01a2\u01a3\5\u00aaV")
        buf.write(u"\2\u01a3\u01aa\7\25\2\2\u01a4\u01ab\5\20\t\2\u01a5\u01ab")
        buf.write(u"\5\"\22\2\u01a6\u01a7\5\20\t\2\u01a7\u01a8\7\22\2\2\u01a8")
        buf.write(u"\u01a9\5\"\22\2\u01a9\u01ab\3\2\2\2\u01aa\u01a4\3\2\2")
        buf.write(u"\2\u01aa\u01a5\3\2\2\2\u01aa\u01a6\3\2\2\2\u01ab\u01ac")
        buf.write(u"\3\2\2\2\u01ac\u01ad\7\26\2\2\u01ad\u01ae\7\20\2\2\u01ae")
        buf.write(u"\u01b1\5t;\2\u01af\u01b2\5\u00bc_\2\u01b0\u01b2\7s\2")
        buf.write(u"\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write(u"\3\2\2\2\u01b3\u01b4\5v<\2\u01b4\r\3\2\2\2\u01b5\u01b6")
        buf.write(u"\7|\2\2\u01b6\u01b7\5\u00aaV\2\u01b7\u01b8\7\25\2\2\u01b8")
        buf.write(u"\u01b9\5\"\22\2\u01b9\u01ba\7\26\2\2\u01ba\u01bb\7\20")
        buf.write(u"\2\2\u01bb\u01be\5t;\2\u01bc\u01bf\5\u00bc_\2\u01bd\u01bf")
        buf.write(u"\7s\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write(u"\u01c0\3\2\2\2\u01c0\u01c1\5v<\2\u01c1\17\3\2\2\2\u01c2")
        buf.write(u"\u01c3\5\u00a2R\2\u01c3\21\3\2\2\2\u01c4\u01c5\7O\2\2")
        buf.write(u"\u01c5\u01c6\5\u00a4S\2\u01c6\u01c8\7\25\2\2\u01c7\u01c9")
        buf.write(u"\5\u00aeX\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write(u"\u01ca\3\2\2\2\u01ca\u01cd\7\26\2\2\u01cb\u01cc\7\63")
        buf.write(u"\2\2\u01cc\u01ce\5\u0094K\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write(u"\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\7\20\2")
        buf.write(u"\2\u01d0\u01d1\5t;\2\u01d1\u01d2\5\u00d8m\2\u01d2\u01d3")
        buf.write(u"\5v<\2\u01d3\23\3\2\2\2\u01d4\u01d5\7O\2\2\u01d5\u01d6")
        buf.write(u"\7p\2\2\u01d6\u01d7\5\u0100\u0081\2\u01d7\u01d8\7\25")
        buf.write(u"\2\2\u01d8\u01d9\5\u00b2Z\2\u01d9\u01dc\7\26\2\2\u01da")
        buf.write(u"\u01db\7\63\2\2\u01db\u01dd\5\u0094K\2\u01dc\u01da\3")
        buf.write(u"\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write(u"\u01df\7\20\2\2\u01df\u01e0\5t;\2\u01e0\u01e1\5\u00d8")
        buf.write(u"m\2\u01e1\u01e2\5v<\2\u01e2\25\3\2\2\2\u01e3\u01e4\7")
        buf.write(u"O\2\2\u01e4\u01e5\5\u00a8U\2\u01e5\u01e6\7{\2\2\u01e6")
        buf.write(u"\u01e7\7\25\2\2\u01e7\u01e8\7\26\2\2\u01e8\u01e9\7\20")
        buf.write(u"\2\2\u01e9\u01ea\5t;\2\u01ea\u01eb\5\u00d8m\2\u01eb\u01ec")
        buf.write(u"\5v<\2\u01ec\27\3\2\2\2\u01ed\u01ee\7O\2\2\u01ee\u01ef")
        buf.write(u"\5\u00a8U\2\u01ef\u01f0\7_\2\2\u01f0\u01f1\7\25\2\2\u01f1")
        buf.write(u"\u01f2\7\26\2\2\u01f2\u01f3\7\20\2\2\u01f3\u01f4\5t;")
        buf.write(u"\2\u01f4\u01f5\5\u00d8m\2\u01f5\u01f6\5v<\2\u01f6\31")
        buf.write(u"\3\2\2\2\u01f7\u01f8\7i\2\2\u01f8\u01f9\t\2\2\2\u01f9")
        buf.write(u"\u01fa\5\u00aaV\2\u01fa\u01fc\7\25\2\2\u01fb\u01fd\5")
        buf.write(u"\"\22\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write(u"\u01fe\3\2\2\2\u01fe\u01ff\7\26\2\2\u01ff\u0200\7\20")
        buf.write(u"\2\2\u0200\u0201\5t;\2\u0201\u0202\5\36\20\2\u0202\u0203")
        buf.write(u"\5v<\2\u0203\33\3\2\2\2\u0204\u0205\7i\2\2\u0205\u0206")
        buf.write(u"\7w\2\2\u0206\u0207\5\u00aaV\2\u0207\u0209\7\25\2\2\u0208")
        buf.write(u"\u020a\5\"\22\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2")
        buf.write(u"\2\u020a\u020b\3\2\2\2\u020b\u020c\7\26\2\2\u020c\u020d")
        buf.write(u"\7\20\2\2\u020d\u020e\5t;\2\u020e\u020f\5\36\20\2\u020f")
        buf.write(u"\u0210\5v<\2\u0210\35\3\2\2\2\u0211\u0212\7d\2\2\u0212")
        buf.write(u"\u0213\7\20\2\2\u0213\u0214\5t;\2\u0214\u0215\5 \21\2")
        buf.write(u"\u0215\u0216\5v<\2\u0216\37\3\2\2\2\u0217\u0218\b\21")
        buf.write(u"\1\2\u0218\u0219\5\u00c0a\2\u0219\u0220\3\2\2\2\u021a")
        buf.write(u"\u021b\f\3\2\2\u021b\u021c\5r:\2\u021c\u021d\5\u00c0")
        buf.write(u"a\2\u021d\u021f\3\2\2\2\u021e\u021a\3\2\2\2\u021f\u0222")
        buf.write(u"\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221")
        buf.write(u"!\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0224\5\u00ccg\2")
        buf.write(u"\u0224#\3\2\2\2\u0225\u0226\7@\2\2\u0226\u0227\7O\2\2")
        buf.write(u"\u0227\u0228\5\u00a4S\2\u0228\u022a\7\25\2\2\u0229\u022b")
        buf.write(u"\5\u00aeX\2\u022a\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b")
        buf.write(u"\u022c\3\2\2\2\u022c\u022f\7\26\2\2\u022d\u022e\7\63")
        buf.write(u"\2\2\u022e\u0230\5\u0094K\2\u022f\u022d\3\2\2\2\u022f")
        buf.write(u"\u0230\3\2\2\2\u0230%\3\2\2\2\u0231\u0232\7O\2\2\u0232")
        buf.write(u"\u0233\5\u00a4S\2\u0233\u0235\7\25\2\2\u0234\u0236\5")
        buf.write(u"\u00aeX\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write(u"\u0237\3\2\2\2\u0237\u023a\7\26\2\2\u0238\u0239\7\63")
        buf.write(u"\2\2\u0239\u023b\5\u0094K\2\u023a\u0238\3\2\2\2\u023a")
        buf.write(u"\u023b\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\7\20\2")
        buf.write(u"\2\u023d\u023e\5t;\2\u023e\u023f\5\u00d8m\2\u023f\u0240")
        buf.write(u"\5v<\2\u0240\'\3\2\2\2\u0241\u0242\7O\2\2\u0242\u0243")
        buf.write(u"\7i\2\2\u0243\u0244\5\u00a4S\2\u0244\u0246\7\25\2\2\u0245")
        buf.write(u"\u0247\5\u00aeX\2\u0246\u0245\3\2\2\2\u0246\u0247\3\2")
        buf.write(u"\2\2\u0247\u0248\3\2\2\2\u0248\u024b\7\26\2\2\u0249\u024a")
        buf.write(u"\7\63\2\2\u024a\u024c\5\u0094K\2\u024b\u0249\3\2\2\2")
        buf.write(u"\u024b\u024c\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e")
        buf.write(u"\7\20\2\2\u024e\u024f\5t;\2\u024f\u0250\5\u00d0i\2\u0250")
        buf.write(u"\u0251\5v<\2\u0251)\3\2\2\2\u0252\u0253\5\u00a8U\2\u0253")
        buf.write(u"\u0254\7\20\2\2\u0254\u0259\5\u00b8]\2\u0255\u0256\7")
        buf.write(u"\25\2\2\u0256\u0257\5\"\22\2\u0257\u0258\7\26\2\2\u0258")
        buf.write(u"\u025a\3\2\2\2\u0259\u0255\3\2\2\2\u0259\u025a\3\2\2")
        buf.write(u"\2\u025a\u025d\3\2\2\2\u025b\u025c\7-\2\2\u025c\u025e")
        buf.write(u"\5\u00eav\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write(u"+\3\2\2\2\u025f\u026f\5.\30\2\u0260\u026f\5j\66\2\u0261")
        buf.write(u"\u026f\5n8\2\u0262\u026f\5N(\2\u0263\u026f\5D#\2\u0264")
        buf.write(u"\u026f\5:\36\2\u0265\u026f\5> \2\u0266\u026f\5B\"\2\u0267")
        buf.write(u"\u026f\5@!\2\u0268\u026f\5H%\2\u0269\u026f\5J&\2\u026a")
        buf.write(u"\u026f\5d\63\2\u026b\u026f\5\66\34\2\u026c\u026f\58\35")
        buf.write(u"\2\u026d\u026f\5&\24\2\u026e\u025f\3\2\2\2\u026e\u0260")
        buf.write(u"\3\2\2\2\u026e\u0261\3\2\2\2\u026e\u0262\3\2\2\2\u026e")
        buf.write(u"\u0263\3\2\2\2\u026e\u0264\3\2\2\2\u026e\u0265\3\2\2")
        buf.write(u"\2\u026e\u0266\3\2\2\2\u026e\u0267\3\2\2\2\u026e\u0268")
        buf.write(u"\3\2\2\2\u026e\u0269\3\2\2\2\u026e\u026a\3\2\2\2\u026e")
        buf.write(u"\u026b\3\2\2\2\u026e\u026c\3\2\2\2\u026e\u026d\3\2\2")
        buf.write(u"\2\u026f-\3\2\2\2\u0270\u0271\5\60\31\2\u0271\u0273\7")
        buf.write(u"\25\2\2\u0272\u0274\5^\60\2\u0273\u0272\3\2\2\2\u0273")
        buf.write(u"\u0274\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0276\7\26\2")
        buf.write(u"\2\u0276/\3\2\2\2\u0277\u027d\5\u00a4S\2\u0278\u0279")
        buf.write(u"\5\62\32\2\u0279\u027a\7\24\2\2\u027a\u027b\5\u00a4S")
        buf.write(u"\2\u027b\u027d\3\2\2\2\u027c\u0277\3\2\2\2\u027c\u0278")
        buf.write(u"\3\2\2\2\u027d\61\3\2\2\2\u027e\u027f\b\32\1\2\u027f")
        buf.write(u"\u0280\5\u00a6T\2\u0280\u0285\3\2\2\2\u0281\u0282\f\3")
        buf.write(u"\2\2\u0282\u0284\5\64\33\2\u0283\u0281\3\2\2\2\u0284")
        buf.write(u"\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2")
        buf.write(u"\2\u0286\63\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289\7")
        buf.write(u"\24\2\2\u0289\u028f\5\u00a8U\2\u028a\u028b\7\27\2\2\u028b")
        buf.write(u"\u028c\5P)\2\u028c\u028d\7\30\2\2\u028d\u028f\3\2\2\2")
        buf.write(u"\u028e\u0288\3\2\2\2\u028e\u028a\3\2\2\2\u028f\65\3\2")
        buf.write(u"\2\2\u0290\u0291\7\u0083\2\2\u0291\u0292\5\u00fa~\2\u0292")
        buf.write(u"\u0293\7\20\2\2\u0293\u0294\5t;\2\u0294\u0295\5\u00d8")
        buf.write(u"m\2\u0295\u0296\5v<\2\u0296\67\3\2\2\2\u0297\u0298\7")
        buf.write(u"\u0083\2\2\u0298\u0299\5\u00aaV\2\u0299\u029a\7\20\2")
        buf.write(u"\2\u029a\u029b\5t;\2\u029b\u029c\5\u00d8m\2\u029c\u029d")
        buf.write(u"\5v<\2\u029d9\3\2\2\2\u029e\u029f\7~\2\2\u029f\u02a0")
        buf.write(u"\7n\2\2\u02a0\u02a1\5P)\2\u02a1\u02a2\7\20\2\2\u02a2")
        buf.write(u"\u02a3\5t;\2\u02a3\u02ab\5\u00dan\2\u02a4\u02a5\5r:\2")
        buf.write(u"\u02a5\u02a6\7r\2\2\u02a6\u02a7\7\20\2\2\u02a7\u02a8")
        buf.write(u"\5t;\2\u02a8\u02a9\5\u00d8m\2\u02a9\u02aa\5v<\2\u02aa")
        buf.write(u"\u02ac\3\2\2\2\u02ab\u02a4\3\2\2\2\u02ab\u02ac\3\2\2")
        buf.write(u"\2\u02ac\u02ad\3\2\2\2\u02ad\u02ae\5v<\2\u02ae;\3\2\2")
        buf.write(u"\2\u02af\u02b0\7\u0084\2\2\u02b0\u02b1\5\u00e0q\2\u02b1")
        buf.write(u"\u02b2\7\20\2\2\u02b2\u02b3\5t;\2\u02b3\u02b4\5\u00d8")
        buf.write(u"m\2\u02b4\u02b5\5v<\2\u02b5\u02bf\3\2\2\2\u02b6\u02b7")
        buf.write(u"\7\u0084\2\2\u02b7\u02b8\7a\2\2\u02b8\u02b9\5\u00dep")
        buf.write(u"\2\u02b9\u02ba\7\20\2\2\u02ba\u02bb\5t;\2\u02bb\u02bc")
        buf.write(u"\5\u00d8m\2\u02bc\u02bd\5v<\2\u02bd\u02bf\3\2\2\2\u02be")
        buf.write(u"\u02af\3\2\2\2\u02be\u02b6\3\2\2\2\u02bf=\3\2\2\2\u02c0")
        buf.write(u"\u02c1\7]\2\2\u02c1\u02c4\5\u00a8U\2\u02c2\u02c3\7\22")
        buf.write(u"\2\2\u02c3\u02c5\5\u00a8U\2\u02c4\u02c2\3\2\2\2\u02c4")
        buf.write(u"\u02c5\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c6\u02c7\7a\2\2")
        buf.write(u"\u02c7\u02c8\5P)\2\u02c8\u02c9\7\20\2\2\u02c9\u02ca\5")
        buf.write(u"t;\2\u02ca\u02cb\5\u00d8m\2\u02cb\u02cc\5v<\2\u02cc?")
        buf.write(u"\3\2\2\2\u02cd\u02ce\7R\2\2\u02ce\u02cf\7\20\2\2\u02cf")
        buf.write(u"\u02d0\5t;\2\u02d0\u02d1\5\u00d8m\2\u02d1\u02d2\5v<\2")
        buf.write(u"\u02d2\u02d3\5r:\2\u02d3\u02d4\7\u0086\2\2\u02d4\u02d5")
        buf.write(u"\5P)\2\u02d5A\3\2\2\2\u02d6\u02d7\7\u0086\2\2\u02d7\u02d8")
        buf.write(u"\5P)\2\u02d8\u02d9\7\20\2\2\u02d9\u02da\5t;\2\u02da\u02db")
        buf.write(u"\5\u00d8m\2\u02db\u02dc\5v<\2\u02dcC\3\2\2\2\u02dd\u02de")
        buf.write(u"\7`\2\2\u02de\u02df\5P)\2\u02df\u02e0\7\20\2\2\u02e0")
        buf.write(u"\u02e1\5t;\2\u02e1\u02e2\5\u00d8m\2\u02e2\u02e6\5v<\2")
        buf.write(u"\u02e3\u02e4\5r:\2\u02e4\u02e5\5F$\2\u02e5\u02e7\3\2")
        buf.write(u"\2\2\u02e6\u02e3\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u02ef")
        buf.write(u"\3\2\2\2\u02e8\u02e9\5r:\2\u02e9\u02ea\7U\2\2\u02ea\u02eb")
        buf.write(u"\7\20\2\2\u02eb\u02ec\5t;\2\u02ec\u02ed\5\u00d8m\2\u02ed")
        buf.write(u"\u02ee\5v<\2\u02ee\u02f0\3\2\2\2\u02ef\u02e8\3\2\2\2")
        buf.write(u"\u02ef\u02f0\3\2\2\2\u02f0E\3\2\2\2\u02f1\u02f2\b$\1")
        buf.write(u"\2\u02f2\u02f3\7U\2\2\u02f3\u02f4\7`\2\2\u02f4\u02f5")
        buf.write(u"\5P)\2\u02f5\u02f6\7\20\2\2\u02f6\u02f7\5t;\2\u02f7\u02f8")
        buf.write(u"\5\u00d8m\2\u02f8\u02f9\5v<\2\u02f9\u0306\3\2\2\2\u02fa")
        buf.write(u"\u02fb\f\3\2\2\u02fb\u02fc\5r:\2\u02fc\u02fd\7U\2\2\u02fd")
        buf.write(u"\u02fe\7`\2\2\u02fe\u02ff\5P)\2\u02ff\u0300\7\20\2\2")
        buf.write(u"\u0300\u0301\5t;\2\u0301\u0302\5\u00d8m\2\u0302\u0303")
        buf.write(u"\5v<\2\u0303\u0305\3\2\2\2\u0304\u02fa\3\2\2\2\u0305")
        buf.write(u"\u0308\3\2\2\2\u0306\u0304\3\2\2\2\u0306\u0307\3\2\2")
        buf.write(u"\2\u0307G\3\2\2\2\u0308\u0306\3\2\2\2\u0309\u030a\7t")
        buf.write(u"\2\2\u030a\u030b\5P)\2\u030bI\3\2\2\2\u030c\u030d\7\u0082")
        buf.write(u"\2\2\u030d\u030e\5\u00a8U\2\u030e\u030f\7\20\2\2\u030f")
        buf.write(u"\u0310\5t;\2\u0310\u0311\5\u00d8m\2\u0311\u0312\5v<\2")
        buf.write(u"\u0312\u0314\5p9\2\u0313\u0315\5\u00dco\2\u0314\u0313")
        buf.write(u"\3\2\2\2\u0314\u0315\3\2\2\2\u0315\u031d\3\2\2\2\u0316")
        buf.write(u"\u0317\7X\2\2\u0317\u0318\7\20\2\2\u0318\u0319\5t;\2")
        buf.write(u"\u0319\u031a\5\u00d8m\2\u031a\u031b\5v<\2\u031b\u031c")
        buf.write(u"\5p9\2\u031c\u031e\3\2\2\2\u031d\u0316\3\2\2\2\u031d")
        buf.write(u"\u031e\3\2\2\2\u031e\u0326\3\2\2\2\u031f\u0320\7\\\2")
        buf.write(u"\2\u0320\u0321\7\20\2\2\u0321\u0322\5t;\2\u0322\u0323")
        buf.write(u"\5\u00d8m\2\u0323\u0324\5v<\2\u0324\u0325\5p9\2\u0325")
        buf.write(u"\u0327\3\2\2\2\u0326\u031f\3\2\2\2\u0326\u0327\3\2\2")
        buf.write(u"\2\u0327\u0328\3\2\2\2\u0328\u0329\5p9\2\u0329K\3\2\2")
        buf.write(u"\2\u032a\u032b\7X\2\2\u032b\u032c\5\u00acW\2\u032c\u032d")
        buf.write(u"\7\20\2\2\u032d\u032e\5t;\2\u032e\u032f\5\u00d8m\2\u032f")
        buf.write(u"\u0330\5v<\2\u0330\u0331\5p9\2\u0331\u033e\3\2\2\2\u0332")
        buf.write(u"\u0333\7X\2\2\u0333\u0334\7a\2\2\u0334\u0335\7\27\2\2")
        buf.write(u"\u0335\u0336\5\u0088E\2\u0336\u0337\7\30\2\2\u0337\u0338")
        buf.write(u"\7\20\2\2\u0338\u0339\5t;\2\u0339\u033a\5\u00d8m\2\u033a")
        buf.write(u"\u033b\5v<\2\u033b\u033c\5p9\2\u033c\u033e\3\2\2\2\u033d")
        buf.write(u"\u032a\3\2\2\2\u033d\u0332\3\2\2\2\u033eM\3\2\2\2\u033f")
        buf.write(u"\u0341\7x\2\2\u0340\u0342\5P)\2\u0341\u0340\3\2\2\2\u0341")
        buf.write(u"\u0342\3\2\2\2\u0342O\3\2\2\2\u0343\u0344\b)\1\2\u0344")
        buf.write(u"\u0345\7#\2\2\u0345\u0356\5P)!\u0346\u0347\7k\2\2\u0347")
        buf.write(u"\u0356\5P) \u0348\u0356\5T+\2\u0349\u0356\5V,\2\u034a")
        buf.write(u"\u034b\7>\2\2\u034b\u034c\7\25\2\2\u034c\u034d\5P)\2")
        buf.write(u"\u034d\u034e\7\26\2\2\u034e\u0356\3\2\2\2\u034f\u0350")
        buf.write(u"\7Y\2\2\u0350\u0351\7\25\2\2\u0351\u0352\5\u00a8U\2\u0352")
        buf.write(u"\u0353\7\26\2\2\u0353\u0356\3\2\2\2\u0354\u0356\5R*\2")
        buf.write(u"\u0355\u0343\3\2\2\2\u0355\u0346\3\2\2\2\u0355\u0348")
        buf.write(u"\3\2\2\2\u0355\u0349\3\2\2\2\u0355\u034a\3\2\2\2\u0355")
        buf.write(u"\u034f\3\2\2\2\u0355\u0354\3\2\2\2\u0356\u03b7\3\2\2")
        buf.write(u"\2\u0357\u0358\f\37\2\2\u0358\u0359\5\u010a\u0086\2\u0359")
        buf.write(u"\u035a\5P) \u035a\u03b6\3\2\2\2\u035b\u035c\f\36\2\2")
        buf.write(u"\u035c\u035d\5\u010c\u0087\2\u035d\u035e\5P)\37\u035e")
        buf.write(u"\u03b6\3\2\2\2\u035f\u0360\f\35\2\2\u0360\u0361\5\u0110")
        buf.write(u"\u0089\2\u0361\u0362\5P)\36\u0362\u03b6\3\2\2\2\u0363")
        buf.write(u"\u0364\f\34\2\2\u0364\u0365\5\u010e\u0088\2\u0365\u0366")
        buf.write(u"\5P)\35\u0366\u03b6\3\2\2\2\u0367\u0368\f\33\2\2\u0368")
        buf.write(u"\u0369\t\3\2\2\u0369\u03b6\5P)\34\u036a\u036b\f\32\2")
        buf.write(u"\2\u036b\u036c\7*\2\2\u036c\u03b6\5P)\33\u036d\u036e")
        buf.write(u"\f\31\2\2\u036e\u036f\7+\2\2\u036f\u03b6\5P)\32\u0370")
        buf.write(u"\u0371\f\30\2\2\u0371\u0372\7(\2\2\u0372\u03b6\5P)\31")
        buf.write(u"\u0373\u0374\f\27\2\2\u0374\u0375\7)\2\2\u0375\u03b6")
        buf.write(u"\5P)\30\u0376\u0377\f\24\2\2\u0377\u0378\7/\2\2\u0378")
        buf.write(u"\u03b6\5P)\25\u0379\u037a\f\23\2\2\u037a\u037b\7.\2\2")
        buf.write(u"\u037b\u03b6\5P)\24\u037c\u037d\f\22\2\2\u037d\u037e")
        buf.write(u"\7\60\2\2\u037e\u03b6\5P)\23\u037f\u0380\f\21\2\2\u0380")
        buf.write(u"\u0381\7q\2\2\u0381\u03b6\5P)\22\u0382\u0383\f\20\2\2")
        buf.write(u"\u0383\u0384\7C\2\2\u0384\u03b6\5P)\21\u0385\u0386\f")
        buf.write(u"\17\2\2\u0386\u0387\7`\2\2\u0387\u0388\5P)\2\u0388\u0389")
        buf.write(u"\7U\2\2\u0389\u038a\5P)\20\u038a\u03b6\3\2\2\2\u038b")
        buf.write(u"\u038c\f\r\2\2\u038c\u038d\7a\2\2\u038d\u03b6\5P)\16")
        buf.write(u"\u038e\u038f\f\f\2\2\u038f\u0390\7N\2\2\u0390\u03b6\5")
        buf.write(u"P)\r\u0391\u0392\f\13\2\2\u0392\u0393\7N\2\2\u0393\u0394")
        buf.write(u"\7A\2\2\u0394\u03b6\5P)\f\u0395\u0396\f\n\2\2\u0396\u0397")
        buf.write(u"\7N\2\2\u0397\u0398\7D\2\2\u0398\u03b6\5P)\13\u0399\u039a")
        buf.write(u"\f\t\2\2\u039a\u039b\7k\2\2\u039b\u039c\7a\2\2\u039c")
        buf.write(u"\u03b6\5P)\n\u039d\u039e\f\b\2\2\u039e\u039f\7k\2\2\u039f")
        buf.write(u"\u03a0\7N\2\2\u03a0\u03b6\5P)\t\u03a1\u03a2\f\7\2\2\u03a2")
        buf.write(u"\u03a3\7k\2\2\u03a3\u03a4\7N\2\2\u03a4\u03a5\7A\2\2\u03a5")
        buf.write(u"\u03b6\5P)\b\u03a6\u03a7\f\6\2\2\u03a7\u03a8\7k\2\2\u03a8")
        buf.write(u"\u03a9\7N\2\2\u03a9\u03aa\7D\2\2\u03aa\u03b6\5P)\7\u03ab")
        buf.write(u"\u03ac\f\26\2\2\u03ac\u03ad\7c\2\2\u03ad\u03ae\7k\2\2")
        buf.write(u"\u03ae\u03b6\5\u00fe\u0080\2\u03af\u03b0\f\25\2\2\u03b0")
        buf.write(u"\u03b1\7c\2\2\u03b1\u03b6\5\u00fe\u0080\2\u03b2\u03b3")
        buf.write(u"\f\16\2\2\u03b3\u03b4\7E\2\2\u03b4\u03b6\5\u00b8]\2\u03b5")
        buf.write(u"\u0357\3\2\2\2\u03b5\u035b\3\2\2\2\u03b5\u035f\3\2\2")
        buf.write(u"\2\u03b5\u0363\3\2\2\2\u03b5\u0367\3\2\2\2\u03b5\u036a")
        buf.write(u"\3\2\2\2\u03b5\u036d\3\2\2\2\u03b5\u0370\3\2\2\2\u03b5")
        buf.write(u"\u0373\3\2\2\2\u03b5\u0376\3\2\2\2\u03b5\u0379\3\2\2")
        buf.write(u"\2\u03b5\u037c\3\2\2\2\u03b5\u037f\3\2\2\2\u03b5\u0382")
        buf.write(u"\3\2\2\2\u03b5\u0385\3\2\2\2\u03b5\u038b\3\2\2\2\u03b5")
        buf.write(u"\u038e\3\2\2\2\u03b5\u0391\3\2\2\2\u03b5\u0395\3\2\2")
        buf.write(u"\2\u03b5\u0399\3\2\2\2\u03b5\u039d\3\2\2\2\u03b5\u03a1")
        buf.write(u"\3\2\2\2\u03b5\u03a6\3\2\2\2\u03b5\u03ab\3\2\2\2\u03b5")
        buf.write(u"\u03af\3\2\2\2\u03b5\u03b2\3\2\2\2\u03b6\u03b9\3\2\2")
        buf.write(u"\2\u03b7\u03b5\3\2\2\2\u03b7\u03b8\3\2\2\2\u03b8Q\3\2")
        buf.write(u"\2\2\u03b9\u03b7\3\2\2\2\u03ba\u03bb\5\u00aaV\2\u03bb")
        buf.write(u"S\3\2\2\2\u03bc\u03bd\b+\1\2\u03bd\u03be\5\u00e4s\2\u03be")
        buf.write(u"\u03c3\3\2\2\2\u03bf\u03c0\f\3\2\2\u03c0\u03c2\5X-\2")
        buf.write(u"\u03c1\u03bf\3\2\2\2\u03c2\u03c5\3\2\2\2\u03c3\u03c1")
        buf.write(u"\3\2\2\2\u03c3\u03c4\3\2\2\2\u03c4U\3\2\2\2\u03c5\u03c3")
        buf.write(u"\3\2\2\2\u03c6\u03cd\5Z.\2\u03c7\u03cd\5\\/\2\u03c8\u03cd")
        buf.write(u"\5f\64\2\u03c9\u03cd\5b\62\2\u03ca\u03cd\5h\65\2\u03cb")
        buf.write(u"\u03cd\5.\30\2\u03cc\u03c6\3\2\2\2\u03cc\u03c7\3\2\2")
        buf.write(u"\2\u03cc\u03c8\3\2\2\2\u03cc\u03c9\3\2\2\2\u03cc\u03ca")
        buf.write(u"\3\2\2\2\u03cc\u03cb\3\2\2\2\u03cdW\3\2\2\2\u03ce\u03cf")
        buf.write(u"\6- \3\u03cf\u03d0\7\24\2\2\u03d0\u03dc\5\u00a8U\2\u03d1")
        buf.write(u"\u03d2\6-!\3\u03d2\u03d3\7\27\2\2\u03d3\u03d4\5\u00f8")
        buf.write(u"}\2\u03d4\u03d5\7\30\2\2\u03d5\u03dc\3\2\2\2\u03d6\u03d7")
        buf.write(u"\6-\"\3\u03d7\u03d8\7\27\2\2\u03d8\u03d9\5P)\2\u03d9")
        buf.write(u"\u03da\7\30\2\2\u03da\u03dc\3\2\2\2\u03db\u03ce\3\2\2")
        buf.write(u"\2\u03db\u03d1\3\2\2\2\u03db\u03d6\3\2\2\2\u03dcY\3\2")
        buf.write(u"\2\2\u03dd\u03de\5\u009eP\2\u03de[\3\2\2\2\u03df\u03e0")
        buf.write(u"\5\u009aN\2\u03e0\u03e2\7\25\2\2\u03e1\u03e3\5^\60\2")
        buf.write(u"\u03e2\u03e1\3\2\2\2\u03e2\u03e3\3\2\2\2\u03e3\u03e4")
        buf.write(u"\3\2\2\2\u03e4\u03e5\7\26\2\2\u03e5]\3\2\2\2\u03e6\u03e7")
        buf.write(u"\b\60\1\2\u03e7\u03e8\5P)\2\u03e8\u03e9\6\60#\3\u03e9")
        buf.write(u"\u03ec\3\2\2\2\u03ea\u03ec\5`\61\2\u03eb\u03e6\3\2\2")
        buf.write(u"\2\u03eb\u03ea\3\2\2\2\u03ec\u03f2\3\2\2\2\u03ed\u03ee")
        buf.write(u"\f\3\2\2\u03ee\u03ef\7\22\2\2\u03ef\u03f1\5`\61\2\u03f0")
        buf.write(u"\u03ed\3\2\2\2\u03f1\u03f4\3\2\2\2\u03f2\u03f0\3\2\2")
        buf.write(u"\2\u03f2\u03f3\3\2\2\2\u03f3_\3\2\2\2\u03f4\u03f2\3\2")
        buf.write(u"\2\2\u03f5\u03f6\5\u00a8U\2\u03f6\u03f7\5\u0108\u0085")
        buf.write(u"\2\u03f7\u03f8\5P)\2\u03f8a\3\2\2\2\u03f9\u03fa\7u\2")
        buf.write(u"\2\u03fa\u03fb\7^\2\2\u03fb\u03fc\5P)\2\u03fcc\3\2\2")
        buf.write(u"\2\u03fd\u03fe\7\u0087\2\2\u03fe\u03ff\5P)\2\u03ff\u0400")
        buf.write(u"\7\u0081\2\2\u0400\u0401\5P)\2\u0401e\3\2\2\2\u0402\u0403")
        buf.write(u"\7[\2\2\u0403\u0404\5\u00a8U\2\u0404\u0405\7^\2\2\u0405")
        buf.write(u"\u0406\5P)\2\u0406\u0407\7\u0085\2\2\u0407\u0408\5P)")
        buf.write(u"\2\u0408g\3\2\2\2\u0409\u040a\7}\2\2\u040a\u040b\7\25")
        buf.write(u"\2\2\u040b\u0411\5T+\2\u040c\u040d\7\22\2\2\u040d\u040e")
        buf.write(u"\5\u0102\u0082\2\u040e\u040f\7-\2\2\u040f\u0410\5T+\2")
        buf.write(u"\u0410\u0412\3\2\2\2\u0411\u040c\3\2\2\2\u0411\u0412")
        buf.write(u"\3\2\2\2\u0412\u0413\3\2\2\2\u0413\u0414\7\26\2\2\u0414")
        buf.write(u"i\3\2\2\2\u0415\u0416\5\u00fc\177\2\u0416\u0417\5\u0108")
        buf.write(u"\u0085\2\u0417\u0418\5P)\2\u0418k\3\2\2\2\u0419\u041a")
        buf.write(u"\6\67%\3\u041a\u041b\7\24\2\2\u041b\u0422\5\u00a8U\2")
        buf.write(u"\u041c\u041d\6\67&\3\u041d\u041e\7\27\2\2\u041e\u041f")
        buf.write(u"\5P)\2\u041f\u0420\7\30\2\2\u0420\u0422\3\2\2\2\u0421")
        buf.write(u"\u0419\3\2\2\2\u0421\u041c\3\2\2\2\u0422m\3\2\2\2\u0423")
        buf.write(u"\u0424\5\u00ccg\2\u0424\u0425\5\u0108\u0085\2\u0425\u0426")
        buf.write(u"\5P)\2\u0426o\3\2\2\2\u0427\u0429\7\7\2\2\u0428\u0427")
        buf.write(u"\3\2\2\2\u0429\u042c\3\2\2\2\u042a\u0428\3\2\2\2\u042a")
        buf.write(u"\u042b\3\2\2\2\u042bq\3\2\2\2\u042c\u042a\3\2\2\2\u042d")
        buf.write(u"\u042f\7\7\2\2\u042e\u042d\3\2\2\2\u042f\u0430\3\2\2")
        buf.write(u"\2\u0430\u042e\3\2\2\2\u0430\u0431\3\2\2\2\u0431s\3\2")
        buf.write(u"\2\2\u0432\u0434\7\7\2\2\u0433\u0432\3\2\2\2\u0434\u0435")
        buf.write(u"\3\2\2\2\u0435\u0433\3\2\2\2\u0435\u0436\3\2\2\2\u0436")
        buf.write(u"\u0437\3\2\2\2\u0437\u0438\7\3\2\2\u0438u\3\2\2\2\u0439")
        buf.write(u"\u043b\7\7\2\2\u043a\u0439\3\2\2\2\u043b\u043e\3\2\2")
        buf.write(u"\2\u043c\u043a\3\2\2\2\u043c\u043d\3\2\2\2\u043d\u043f")
        buf.write(u"\3\2\2\2\u043e\u043c\3\2\2\2\u043f\u0440\7\4\2\2\u0440")
        buf.write(u"w\3\2\2\2\u0441\u0442\7j\2\2\u0442y\3\2\2\2\u0443\u0445")
        buf.write(u"\5|?\2\u0444\u0443\3\2\2\2\u0444\u0445\3\2\2\2\u0445")
        buf.write(u"\u0446\3\2\2\2\u0446\u0447\5p9\2\u0447\u0448\7\2\2\3")
        buf.write(u"\u0448{\3\2\2\2\u0449\u044a\b?\1\2\u044a\u044b\5~@\2")
        buf.write(u"\u044b\u0452\3\2\2\2\u044c\u044d\f\3\2\2\u044d\u044e")
        buf.write(u"\5r:\2\u044e\u044f\5~@\2\u044f\u0451\3\2\2\2\u0450\u044c")
        buf.write(u"\3\2\2\2\u0451\u0454\3\2\2\2\u0452\u0450\3\2\2\2\u0452")
        buf.write(u"\u0453\3\2\2\2\u0453}\3\2\2\2\u0454\u0452\3\2\2\2\u0455")
        buf.write(u"\u045b\5\n\6\2\u0456\u045b\5\u00a0Q\2\u0457\u045b\5\u0080")
        buf.write(u"A\2\u0458\u045b\5\u0082B\2\u0459\u045b\5\u00ceh\2\u045a")
        buf.write(u"\u0455\3\2\2\2\u045a\u0456\3\2\2\2\u045a\u0457\3\2\2")
        buf.write(u"\2\u045a\u0458\3\2\2\2\u045a\u0459\3\2\2\2\u045b\177")
        buf.write(u"\3\2\2\2\u045c\u045d\5\34\17\2\u045d\u0081\3\2\2\2\u045e")
        buf.write(u"\u0461\5\2\2\2\u045f\u0461\5\4\3\2\u0460\u045e\3\2\2")
        buf.write(u"\2\u0460\u045f\3\2\2\2\u0461\u0083\3\2\2\2\u0462\u0463")
        buf.write(u"\bC\1\2\u0463\u0464\5\6\4\2\u0464\u046b\3\2\2\2\u0465")
        buf.write(u"\u0466\f\3\2\2\u0466\u0467\5r:\2\u0467\u0468\5\6\4\2")
        buf.write(u"\u0468\u046a\3\2\2\2\u0469\u0465\3\2\2\2\u046a\u046d")
        buf.write(u"\3\2\2\2\u046b\u0469\3\2\2\2\u046b\u046c\3\2\2\2\u046c")
        buf.write(u"\u0085\3\2\2\2\u046d\u046b\3\2\2\2\u046e\u046f\bD\1\2")
        buf.write(u"\u046f\u0470\5\b\5\2\u0470\u0477\3\2\2\2\u0471\u0472")
        buf.write(u"\f\3\2\2\u0472\u0473\5r:\2\u0473\u0474\5\b\5\2\u0474")
        buf.write(u"\u0476\3\2\2\2\u0475\u0471\3\2\2\2\u0476\u0479\3\2\2")
        buf.write(u"\2\u0477\u0475\3\2\2\2\u0477\u0478\3\2\2\2\u0478\u0087")
        buf.write(u"\3\2\2\2\u0479\u0477\3\2\2\2\u047a\u047b\bE\1\2\u047b")
        buf.write(u"\u047c\5\u00acW\2\u047c\u0482\3\2\2\2\u047d\u047e\f\3")
        buf.write(u"\2\2\u047e\u047f\7\22\2\2\u047f\u0481\5\u00acW\2\u0480")
        buf.write(u"\u047d\3\2\2\2\u0481\u0484\3\2\2\2\u0482\u0480\3\2\2")
        buf.write(u"\2\u0482\u0483\3\2\2\2\u0483\u0089\3\2\2\2\u0484\u0482")
        buf.write(u"\3\2\2\2\u0485\u0486\7a\2\2\u0486\u0490\5\u008cG\2\u0487")
        buf.write(u"\u0488\7a\2\2\u0488\u0490\5\u008eH\2\u0489\u048a\7a\2")
        buf.write(u"\2\u048a\u0490\5\u0092J\2\u048b\u048c\7e\2\2\u048c\u0490")
        buf.write(u"\7\u008f\2\2\u048d\u048e\7e\2\2\u048e\u0490\5P)\2\u048f")
        buf.write(u"\u0485\3\2\2\2\u048f\u0487\3\2\2\2\u048f\u0489\3\2\2")
        buf.write(u"\2\u048f\u048b\3\2\2\2\u048f\u048d\3\2\2\2\u0490\u008b")
        buf.write(u"\3\2\2\2\u0491\u0493\7\27\2\2\u0492\u0494\5\u0090I\2")
        buf.write(u"\u0493\u0492\3\2\2\2\u0493\u0494\3\2\2\2\u0494\u0495")
        buf.write(u"\3\2\2\2\u0495\u0496\7\30\2\2\u0496\u008d\3\2\2\2\u0497")
        buf.write(u"\u0499\7*\2\2\u0498\u049a\5\u0090I\2\u0499\u0498\3\2")
        buf.write(u"\2\2\u0499\u049a\3\2\2\2\u049a\u049b\3\2\2\2\u049b\u049c")
        buf.write(u"\7(\2\2\u049c\u008f\3\2\2\2\u049d\u049e\bI\1\2\u049e")
        buf.write(u"\u049f\5P)\2\u049f\u04a5\3\2\2\2\u04a0\u04a1\f\3\2\2")
        buf.write(u"\u04a1\u04a2\7\22\2\2\u04a2\u04a4\5P)\2\u04a3\u04a0\3")
        buf.write(u"\2\2\2\u04a4\u04a7\3\2\2\2\u04a5\u04a3\3\2\2\2\u04a5")
        buf.write(u"\u04a6\3\2\2\2\u04a6\u0091\3\2\2\2\u04a7\u04a5\3\2\2")
        buf.write(u"\2\u04a8\u04a9\7\27\2\2\u04a9\u04aa\5P)\2\u04aa\u04ab")
        buf.write(u"\7\23\2\2\u04ab\u04ac\5P)\2\u04ac\u04ad\7\30\2\2\u04ad")
        buf.write(u"\u0093\3\2\2\2\u04ae\u04af\bK\1\2\u04af\u04b0\5\u0096")
        buf.write(u"L\2\u04b0\u04bb\3\2\2\2\u04b1\u04b2\f\5\2\2\u04b2\u04ba")
        buf.write(u"\7,\2\2\u04b3\u04b4\f\4\2\2\u04b4\u04b5\7\27\2\2\u04b5")
        buf.write(u"\u04ba\7\30\2\2\u04b6\u04b7\f\3\2\2\u04b7\u04b8\7\31")
        buf.write(u"\2\2\u04b8\u04ba\7\32\2\2\u04b9\u04b1\3\2\2\2\u04b9\u04b3")
        buf.write(u"\3\2\2\2\u04b9\u04b6\3\2\2\2\u04ba\u04bd\3\2\2\2\u04bb")
        buf.write(u"\u04b9\3\2\2\2\u04bb\u04bc\3\2\2\2\u04bc\u0095\3\2\2")
        buf.write(u"\2\u04bd\u04bb\3\2\2\2\u04be\u04c1\5\u0098M\2\u04bf\u04c1")
        buf.write(u"\5\u009aN\2\u04c0\u04be\3\2\2\2\u04c0\u04bf\3\2\2\2\u04c1")
        buf.write(u"\u0097\3\2\2\2\u04c2\u04cd\7\64\2\2\u04c3\u04cd\7\65")
        buf.write(u"\2\2\u04c4\u04cd\7\66\2\2\u04c5\u04cd\7\67\2\2\u04c6")
        buf.write(u"\u04cd\78\2\2\u04c7\u04cd\79\2\2\u04c8\u04cd\7;\2\2\u04c9")
        buf.write(u"\u04cd\7:\2\2\u04ca\u04cd\7<\2\2\u04cb\u04cd\7>\2\2\u04cc")
        buf.write(u"\u04c2\3\2\2\2\u04cc\u04c3\3\2\2\2\u04cc\u04c4\3\2\2")
        buf.write(u"\2\u04cc\u04c5\3\2\2\2\u04cc\u04c6\3\2\2\2\u04cc\u04c7")
        buf.write(u"\3\2\2\2\u04cc\u04c8\3\2\2\2\u04cc\u04c9\3\2\2\2\u04cc")
        buf.write(u"\u04ca\3\2\2\2\u04cc\u04cb\3\2\2\2\u04cd\u0099\3\2\2")
        buf.write(u"\2\u04ce\u04cf\7\u008d\2\2\u04cf\u009b\3\2\2\2\u04d0")
        buf.write(u"\u04d1\7>\2\2\u04d1\u009d\3\2\2\2\u04d2\u04d3\7?\2\2")
        buf.write(u"\u04d3\u009f\3\2\2\2\u04d4\u04d8\5\f\7\2\u04d5\u04d8")
        buf.write(u"\5\32\16\2\u04d6\u04d8\5\16\b\2\u04d7\u04d4\3\2\2\2\u04d7")
        buf.write(u"\u04d5\3\2\2\2\u04d7\u04d6\3\2\2\2\u04d8\u00a1\3\2\2")
        buf.write(u"\2\u04d9\u04da\bR\1\2\u04da\u04db\5\u00aaV\2\u04db\u04e1")
        buf.write(u"\3\2\2\2\u04dc\u04dd\f\3\2\2\u04dd\u04de\7\22\2\2\u04de")
        buf.write(u"\u04e0\5\u00aaV\2\u04df\u04dc\3\2\2\2\u04e0\u04e3\3\2")
        buf.write(u"\2\2\u04e1\u04df\3\2\2\2\u04e1\u04e2\3\2\2\2\u04e2\u00a3")
        buf.write(u"\3\2\2\2\u04e3\u04e1\3\2\2\2\u04e4\u04e7\5\u00a8U\2\u04e5")
        buf.write(u"\u04e7\5\u00aaV\2\u04e6\u04e4\3\2\2\2\u04e6\u04e5\3\2")
        buf.write(u"\2\2\u04e7\u00a5\3\2\2\2\u04e8\u04ec\5\u00a8U\2\u04e9")
        buf.write(u"\u04ec\5\u00aaV\2\u04ea\u04ec\5\u00acW\2\u04eb\u04e8")
        buf.write(u"\3\2\2\2\u04eb\u04e9\3\2\2\2\u04eb\u04ea\3\2\2\2\u04ec")
        buf.write(u"\u00a7\3\2\2\2\u04ed\u04ee\7\u008e\2\2\u04ee\u00a9\3")
        buf.write(u"\2\2\2\u04ef\u04f0\7\u008d\2\2\u04f0\u00ab\3\2\2\2\u04f1")
        buf.write(u"\u04f2\7\u008c\2\2\u04f2\u00ad\3\2\2\2\u04f3\u04f4\b")
        buf.write(u"X\1\2\u04f4\u04f5\5\u00b0Y\2\u04f5\u04fb\3\2\2\2\u04f6")
        buf.write(u"\u04f7\f\3\2\2\u04f7\u04f8\7\22\2\2\u04f8\u04fa\5\u00b0")
        buf.write(u"Y\2\u04f9\u04f6\3\2\2\2\u04fa\u04fd\3\2\2\2\u04fb\u04f9")
        buf.write(u"\3\2\2\2\u04fb\u04fc\3\2\2\2\u04fc\u00af\3\2\2\2\u04fd")
        buf.write(u"\u04fb\3\2\2\2\u04fe\u0501\5\u00b6\\\2\u04ff\u0501\5")
        buf.write(u"\u00b2Z\2\u0500\u04fe\3\2\2\2\u0500\u04ff\3\2\2\2\u0501")
        buf.write(u"\u00b1\3\2\2\2\u0502\u0505\5\u00b4[\2\u0503\u0505\5*")
        buf.write(u"\26\2\u0504\u0502\3\2\2\2\u0504\u0503\3\2\2\2\u0505\u00b3")
        buf.write(u"\3\2\2\2\u0506\u0509\5\u00a8U\2\u0507\u0508\7-\2\2\u0508")
        buf.write(u"\u050a\5\u00eav\2\u0509\u0507\3\2\2\2\u0509\u050a\3\2")
        buf.write(u"\2\2\u050a\u00b5\3\2\2\2\u050b\u050c\5\u009cO\2\u050c")
        buf.write(u"\u050d\5\u00a8U\2\u050d\u00b7\3\2\2\2\u050e\u0511\5\u0094")
        buf.write(u"K\2\u050f\u0511\5\u00ba^\2\u0510\u050e\3\2\2\2\u0510")
        buf.write(u"\u050f\3\2\2\2\u0511\u00b9\3\2\2\2\u0512\u0513\b^\1\2")
        buf.write(u"\u0513\u0514\7D\2\2\u0514\u051d\3\2\2\2\u0515\u0516\f")
        buf.write(u"\4\2\2\u0516\u0517\7\27\2\2\u0517\u051c\7\30\2\2\u0518")
        buf.write(u"\u0519\f\3\2\2\u0519\u051a\7\31\2\2\u051a\u051c\7\32")
        buf.write(u"\2\2\u051b\u0515\3\2\2\2\u051b\u0518\3\2\2\2\u051c\u051f")
        buf.write(u"\3\2\2\2\u051d\u051b\3\2\2\2\u051d\u051e\3\2\2\2\u051e")
        buf.write(u"\u00bb\3\2\2\2\u051f\u051d\3\2\2\2\u0520\u0521\b_\1\2")
        buf.write(u"\u0521\u0522\5\u00be`\2\u0522\u0529\3\2\2\2\u0523\u0524")
        buf.write(u"\f\3\2\2\u0524\u0525\5r:\2\u0525\u0526\5\u00be`\2\u0526")
        buf.write(u"\u0528\3\2\2\2\u0527\u0523\3\2\2\2\u0528\u052b\3\2\2")
        buf.write(u"\2\u0529\u0527\3\2\2\2\u0529\u052a\3\2\2\2\u052a\u00bd")
        buf.write(u"\3\2\2\2\u052b\u0529\3\2\2\2\u052c\u0531\5\26\f\2\u052d")
        buf.write(u"\u0531\5\30\r\2\u052e\u0531\5\22\n\2\u052f\u0531\5\24")
        buf.write(u"\13\2\u0530\u052c\3\2\2\2\u0530\u052d\3\2\2\2\u0530\u052e")
        buf.write(u"\3\2\2\2\u0530\u052f\3\2\2\2\u0531\u00bf\3\2\2\2\u0532")
        buf.write(u"\u0533\7\n\2\2\u0533\u053d\5\u0152\u00aa\2\u0534\u0535")
        buf.write(u"\7\13\2\2\u0535\u053d\5\u0168\u00b5\2\u0536\u0537\7\f")
        buf.write(u"\2\2\u0537\u053d\5\u00c2b\2\u0538\u0539\7\r\2\2\u0539")
        buf.write(u"\u053d\5\u00c2b\2\u053a\u053b\7\16\2\2\u053b\u053d\5")
        buf.write(u"\u00c8e\2\u053c\u0532\3\2\2\2\u053c\u0534\3\2\2\2\u053c")
        buf.write(u"\u0536\3\2\2\2\u053c\u0538\3\2\2\2\u053c\u053a\3\2\2")
        buf.write(u"\2\u053d\u00c1\3\2\2\2\u053e\u0540\5\u00a6T\2\u053f\u0541")
        buf.write(u"\5\u00c4c\2\u0540\u053f\3\2\2\2\u0540\u0541\3\2\2\2\u0541")
        buf.write(u"\u00c3\3\2\2\2\u0542\u0543\7^\2\2\u0543\u0544\5\u00c6")
        buf.write(u"d\2\u0544\u0545\7\20\2\2\u0545\u054a\5\u00a6T\2\u0546")
        buf.write(u"\u0547\7\24\2\2\u0547\u0549\5\u00a6T\2\u0548\u0546\3")
        buf.write(u"\2\2\2\u0549\u054c\3\2\2\2\u054a\u0548\3\2\2\2\u054a")
        buf.write(u"\u054b\3\2\2\2\u054b\u00c5\3\2\2\2\u054c\u054a\3\2\2")
        buf.write(u"\2\u054d\u054e\7\u008e\2\2\u054e\u054f\6d\64\3\u054f")
        buf.write(u"\u00c7\3\2\2\2\u0550\u0552\5\u00a6T\2\u0551\u0553\5\u00ca")
        buf.write(u"f\2\u0552\u0551\3\2\2\2\u0552\u0553\3\2\2\2\u0553\u00c9")
        buf.write(u"\3\2\2\2\u0554\u0555\7^\2\2\u0555\u0556\5\u00c6d\2\u0556")
        buf.write(u"\u0558\7\20\2\2\u0557\u0559\7%\2\2\u0558\u0557\3\2\2")
        buf.write(u"\2\u0558\u0559\3\2\2\2\u0559\u055a\3\2\2\2\u055a\u055f")
        buf.write(u"\5\u00a6T\2\u055b\u055c\7%\2\2\u055c\u055e\5\u00a6T\2")
        buf.write(u"\u055d\u055b\3\2\2\2\u055e\u0561\3\2\2\2\u055f\u055d")
        buf.write(u"\3\2\2\2\u055f\u0560\3\2\2\2\u0560\u0564\3\2\2\2\u0561")
        buf.write(u"\u055f\3\2\2\2\u0562\u0563\7\24\2\2\u0563\u0565\5\u00a6")
        buf.write(u"T\2\u0564\u0562\3\2\2\2\u0564\u0565\3\2\2\2\u0565\u00cb")
        buf.write(u"\3\2\2\2\u0566\u0567\bg\1\2\u0567\u0568\5\u00a8U\2\u0568")
        buf.write(u"\u056e\3\2\2\2\u0569\u056a\f\3\2\2\u056a\u056b\7\22\2")
        buf.write(u"\2\u056b\u056d\5\u00a8U\2\u056c\u0569\3\2\2\2\u056d\u0570")
        buf.write(u"\3\2\2\2\u056e\u056c\3\2\2\2\u056e\u056f\3\2\2\2\u056f")
        buf.write(u"\u00cd\3\2\2\2\u0570\u056e\3\2\2\2\u0571\u0575\5$\23")
        buf.write(u"\2\u0572\u0575\5&\24\2\u0573\u0575\5(\25\2\u0574\u0571")
        buf.write(u"\3\2\2\2\u0574\u0572\3\2\2\2\u0574\u0573\3\2\2\2\u0575")
        buf.write(u"\u00cf\3\2\2\2\u0576\u0577\bi\1\2\u0577\u0578\5\u00d2")
        buf.write(u"j\2\u0578\u057f\3\2\2\2\u0579\u057a\f\3\2\2\u057a\u057b")
        buf.write(u"\5r:\2\u057b\u057c\5\u00d2j\2\u057c\u057e\3\2\2\2\u057d")
        buf.write(u"\u0579\3\2\2\2\u057e\u0581\3\2\2\2\u057f\u057d\3\2\2")
        buf.write(u"\2\u057f\u0580\3\2\2\2\u0580\u00d1\3\2\2\2\u0581\u057f")
        buf.write(u"\3\2\2\2\u0582\u0583\7\n\2\2\u0583\u058d\5\u0140\u00a1")
        buf.write(u"\2\u0584\u0585\7\13\2\2\u0585\u058d\5\u0158\u00ad\2\u0586")
        buf.write(u"\u0587\7\f\2\2\u0587\u058d\5\u00d4k\2\u0588\u0589\7\r")
        buf.write(u"\2\2\u0589\u058d\5\u00d4k\2\u058a\u058b\7\16\2\2\u058b")
        buf.write(u"\u058d\5\u00d6l\2\u058c\u0582\3\2\2\2\u058c\u0584\3\2")
        buf.write(u"\2\2\u058c\u0586\3\2\2\2\u058c\u0588\3\2\2\2\u058c\u058a")
        buf.write(u"\3\2\2\2\u058d\u00d3\3\2\2\2\u058e\u0590\5\u0128\u0095")
        buf.write(u"\2\u058f\u0591\7\21\2\2\u0590\u058f\3\2\2\2\u0590\u0591")
        buf.write(u"\3\2\2\2\u0591\u0593\3\2\2\2\u0592\u0594\5\u00c4c\2\u0593")
        buf.write(u"\u0592\3\2\2\2\u0593\u0594\3\2\2\2\u0594\u00d5\3\2\2")
        buf.write(u"\2\u0595\u0597\5\u0112\u008a\2\u0596\u0598\7\21\2\2\u0597")
        buf.write(u"\u0596\3\2\2\2\u0597\u0598\3\2\2\2\u0598\u059a\3\2\2")
        buf.write(u"\2\u0599\u059b\5\u00caf\2\u059a\u0599\3\2\2\2\u059a\u059b")
        buf.write(u"\3\2\2\2\u059b\u00d7\3\2\2\2\u059c\u059d\bm\1\2\u059d")
        buf.write(u"\u059e\5,\27\2\u059e\u05a5\3\2\2\2\u059f\u05a0\f\3\2")
        buf.write(u"\2\u05a0\u05a1\5r:\2\u05a1\u05a2\5,\27\2\u05a2\u05a4")
        buf.write(u"\3\2\2\2\u05a3\u059f\3\2\2\2\u05a4\u05a7\3\2\2\2\u05a5")
        buf.write(u"\u05a3\3\2\2\2\u05a5\u05a6\3\2\2\2\u05a6\u00d9\3\2\2")
        buf.write(u"\2\u05a7\u05a5\3\2\2\2\u05a8\u05a9\bn\1\2\u05a9\u05aa")
        buf.write(u"\5<\37\2\u05aa\u05b1\3\2\2\2\u05ab\u05ac\f\3\2\2\u05ac")
        buf.write(u"\u05ad\5r:\2\u05ad\u05ae\5<\37\2\u05ae\u05b0\3\2\2\2")
        buf.write(u"\u05af\u05ab\3\2\2\2\u05b0\u05b3\3\2\2\2\u05b1\u05af")
        buf.write(u"\3\2\2\2\u05b1\u05b2\3\2\2\2\u05b2\u00db\3\2\2\2\u05b3")
        buf.write(u"\u05b1\3\2\2\2\u05b4\u05b5\bo\1\2\u05b5\u05b6\5L\'\2")
        buf.write(u"\u05b6\u05bd\3\2\2\2\u05b7\u05b8\f\3\2\2\u05b8\u05b9")
        buf.write(u"\5r:\2\u05b9\u05ba\5L\'\2\u05ba\u05bc\3\2\2\2\u05bb\u05b7")
        buf.write(u"\3\2\2\2\u05bc\u05bf\3\2\2\2\u05bd\u05bb\3\2\2\2\u05bd")
        buf.write(u"\u05be\3\2\2\2\u05be\u00dd\3\2\2\2\u05bf\u05bd\3\2\2")
        buf.write(u"\2\u05c0\u05c1\7\27\2\2\u05c1\u05c2\5\u00e0q\2\u05c2")
        buf.write(u"\u05c3\7\23\2\2\u05c3\u05c4\5\u00e0q\2\u05c4\u05c5\7")
        buf.write(u"\30\2\2\u05c5\u05cf\3\2\2\2\u05c6\u05c7\7\27\2\2\u05c7")
        buf.write(u"\u05c8\5\u00e2r\2\u05c8\u05c9\7\30\2\2\u05c9\u05cf\3")
        buf.write(u"\2\2\2\u05ca\u05cb\7*\2\2\u05cb\u05cc\5\u00e2r\2\u05cc")
        buf.write(u"\u05cd\7(\2\2\u05cd\u05cf\3\2\2\2\u05ce\u05c0\3\2\2\2")
        buf.write(u"\u05ce\u05c6\3\2\2\2\u05ce\u05ca\3\2\2\2\u05cf\u00df")
        buf.write(u"\3\2\2\2\u05d0\u05de\7\u008a\2\2\u05d1\u05de\7\u008b")
        buf.write(u"\2\2\u05d2\u05de\7\u0090\2\2\u05d3\u05de\7\u0091\2\2")
        buf.write(u"\u05d4\u05de\7\u0089\2\2\u05d5\u05de\7\u0095\2\2\u05d6")
        buf.write(u"\u05de\7\u0094\2\2\u05d7\u05de\7\u008f\2\2\u05d8\u05de")
        buf.write(u"\7\u0092\2\2\u05d9\u05de\7\u0093\2\2\u05da\u05de\7\u0088")
        buf.write(u"\2\2\u05db\u05de\7\u0096\2\2\u05dc\u05de\5x=\2\u05dd")
        buf.write(u"\u05d0\3\2\2\2\u05dd\u05d1\3\2\2\2\u05dd\u05d2\3\2\2")
        buf.write(u"\2\u05dd\u05d3\3\2\2\2\u05dd\u05d4\3\2\2\2\u05dd\u05d5")
        buf.write(u"\3\2\2\2\u05dd\u05d6\3\2\2\2\u05dd\u05d7\3\2\2\2\u05dd")
        buf.write(u"\u05d8\3\2\2\2\u05dd\u05d9\3\2\2\2\u05dd\u05da\3\2\2")
        buf.write(u"\2\u05dd\u05db\3\2\2\2\u05dd\u05dc\3\2\2\2\u05de\u00e1")
        buf.write(u"\3\2\2\2\u05df\u05e0\br\1\2\u05e0\u05e1\5\u00e0q\2\u05e1")
        buf.write(u"\u05e7\3\2\2\2\u05e2\u05e3\f\3\2\2\u05e3\u05e4\7\22\2")
        buf.write(u"\2\u05e4\u05e6\5\u00e0q\2\u05e5\u05e2\3\2\2\2\u05e6\u05e9")
        buf.write(u"\3\2\2\2\u05e7\u05e5\3\2\2\2\u05e7\u05e8\3\2\2\2\u05e8")
        buf.write(u"\u00e3\3\2\2\2\u05e9\u05e7\3\2\2\2\u05ea\u05ef\5\u00e8")
        buf.write(u"u\2\u05eb\u05ef\5\u00eav\2\u05ec\u05ef\5\u00a6T\2\u05ed")
        buf.write(u"\u05ef\5\u00e6t\2\u05ee\u05ea\3\2\2\2\u05ee\u05eb\3\2")
        buf.write(u"\2\2\u05ee\u05ec\3\2\2\2\u05ee\u05ed\3\2\2\2\u05ef\u00e5")
        buf.write(u"\3\2\2\2\u05f0\u05f1\t\4\2\2\u05f1\u00e7\3\2\2\2\u05f2")
        buf.write(u"\u05f3\7\25\2\2\u05f3\u05f4\5P)\2\u05f4\u05f5\7\26\2")
        buf.write(u"\2\u05f5\u00e9\3\2\2\2\u05f6\u05f9\5\u00e0q\2\u05f7\u05f9")
        buf.write(u"\5\u00ecw\2\u05f8\u05f6\3\2\2\2\u05f8\u05f7\3\2\2\2\u05f9")
        buf.write(u"\u00eb\3\2\2\2\u05fa\u0600\5\u0092J\2\u05fb\u0600\5\u008c")
        buf.write(u"G\2\u05fc\u0600\5\u008eH\2\u05fd\u0600\5\u00f0y\2\u05fe")
        buf.write(u"\u0600\5\u00eex\2\u05ff\u05fa\3\2\2\2\u05ff\u05fb\3\2")
        buf.write(u"\2\2\u05ff\u05fc\3\2\2\2\u05ff\u05fd\3\2\2\2\u05ff\u05fe")
        buf.write(u"\3\2\2\2\u0600\u00ed\3\2\2\2\u0601\u0603\7\25\2\2\u0602")
        buf.write(u"\u0604\5\u00f2z\2\u0603\u0602\3\2\2\2\u0603\u0604\3\2")
        buf.write(u"\2\2\u0604\u0605\3\2\2\2\u0605\u0606\7\26\2\2\u0606\u00ef")
        buf.write(u"\3\2\2\2\u0607\u0609\7\31\2\2\u0608\u060a\5\u00f4{\2")
        buf.write(u"\u0609\u0608\3\2\2\2\u0609\u060a\3\2\2\2\u060a\u060b")
        buf.write(u"\3\2\2\2\u060b\u060c\7\32\2\2\u060c\u00f1\3\2\2\2\u060d")
        buf.write(u"\u060e\bz\1\2\u060e\u060f\5P)\2\u060f\u0615\3\2\2\2\u0610")
        buf.write(u"\u0611\f\3\2\2\u0611\u0612\7\22\2\2\u0612\u0614\5P)\2")
        buf.write(u"\u0613\u0610\3\2\2\2\u0614\u0617\3\2\2\2\u0615\u0613")
        buf.write(u"\3\2\2\2\u0615\u0616\3\2\2\2\u0616\u00f3\3\2\2\2\u0617")
        buf.write(u"\u0615\3\2\2\2\u0618\u0619\b{\1\2\u0619\u061a\5\u00f6")
        buf.write(u"|\2\u061a\u0620\3\2\2\2\u061b\u061c\f\3\2\2\u061c\u061d")
        buf.write(u"\7\22\2\2\u061d\u061f\5\u00f6|\2\u061e\u061b\3\2\2\2")
        buf.write(u"\u061f\u0622\3\2\2\2\u0620\u061e\3\2\2\2\u0620\u0621")
        buf.write(u"\3\2\2\2\u0621\u00f5\3\2\2\2\u0622\u0620\3\2\2\2\u0623")
        buf.write(u"\u0624\5P)\2\u0624\u0625\7\20\2\2\u0625\u0626\5P)\2\u0626")
        buf.write(u"\u00f7\3\2\2\2\u0627\u0628\5P)\2\u0628\u0629\7\20\2\2")
        buf.write(u"\u0629\u062a\5P)\2\u062a\u0631\3\2\2\2\u062b\u062c\5")
        buf.write(u"P)\2\u062c\u062d\7\20\2\2\u062d\u0631\3\2\2\2\u062e\u062f")
        buf.write(u"\7\20\2\2\u062f\u0631\5P)\2\u0630\u0627\3\2\2\2\u0630")
        buf.write(u"\u062b\3\2\2\2\u0630\u062e\3\2\2\2\u0631\u00f9\3\2\2")
        buf.write(u"\2\u0632\u0633\5\u00a8U\2\u0633\u0634\5\u0108\u0085\2")
        buf.write(u"\u0634\u0635\5P)\2\u0635\u00fb\3\2\2\2\u0636\u0637\b")
        buf.write(u"\177\1\2\u0637\u0638\5\u00a8U\2\u0638\u063d\3\2\2\2\u0639")
        buf.write(u"\u063a\f\3\2\2\u063a\u063c\5l\67\2\u063b\u0639\3\2\2")
        buf.write(u"\2\u063c\u063f\3\2\2\2\u063d\u063b\3\2\2\2\u063d\u063e")
        buf.write(u"\3\2\2\2\u063e\u00fd\3\2\2\2\u063f\u063d\3\2\2\2\u0640")
        buf.write(u"\u0641\6\u0080>\3\u0641\u0642\7\u008e\2\2\u0642\u0645")
        buf.write(u"\5\u00b8]\2\u0643\u0645\5P)\2\u0644\u0640\3\2\2\2\u0644")
        buf.write(u"\u0643\3\2\2\2\u0645\u00ff\3\2\2\2\u0646\u064d\7\"\2")
        buf.write(u"\2\u0647\u064d\7#\2\2\u0648\u064d\5\u010a\u0086\2\u0649")
        buf.write(u"\u064d\5\u010c\u0087\2\u064a\u064d\5\u010e\u0088\2\u064b")
        buf.write(u"\u064d\5\u0110\u0089\2\u064c\u0646\3\2\2\2\u064c\u0647")
        buf.write(u"\3\2\2\2\u064c\u0648\3\2\2\2\u064c\u0649\3\2\2\2\u064c")
        buf.write(u"\u064a\3\2\2\2\u064c\u064b\3\2\2\2\u064d\u0101\3\2\2")
        buf.write(u"\2\u064e\u064f\7\u008e\2\2\u064f\u0650\6\u0082?\3\u0650")
        buf.write(u"\u0103\3\2\2\2\u0651\u0652\7\u008e\2\2\u0652\u0653\6")
        buf.write(u"\u0083@\3\u0653\u0105\3\2\2\2\u0654\u0655\7\u008e\2\2")
        buf.write(u"\u0655\u0656\6\u0084A\3\u0656\u0107\3\2\2\2\u0657\u0658")
        buf.write(u"\7-\2\2\u0658\u0109\3\2\2\2\u0659\u065a\7$\2\2\u065a")
        buf.write(u"\u010b\3\2\2\2\u065b\u065c\7%\2\2\u065c\u010d\3\2\2\2")
        buf.write(u"\u065d\u065e\7&\2\2\u065e\u010f\3\2\2\2\u065f\u0660\t")
        buf.write(u"\5\2\2\u0660\u0111\3\2\2\2\u0661\u0662\7x\2\2\u0662\u0663")
        buf.write(u"\5\u0114\u008b\2\u0663\u0664\7\21\2\2\u0664\u0669\3\2")
        buf.write(u"\2\2\u0665\u0666\5\u0114\u008b\2\u0666\u0667\7\21\2\2")
        buf.write(u"\u0667\u0669\3\2\2\2\u0668\u0661\3\2\2\2\u0668\u0665")
        buf.write(u"\3\2\2\2\u0669\u0113\3\2\2\2\u066a\u066b\b\u008b\1\2")
        buf.write(u"\u066b\u066c\5\u0116\u008c\2\u066c\u0671\3\2\2\2\u066d")
        buf.write(u"\u066e\f\3\2\2\u066e\u0670\5\u0118\u008d\2\u066f\u066d")
        buf.write(u"\3\2\2\2\u0670\u0673\3\2\2\2\u0671\u066f\3\2\2\2\u0671")
        buf.write(u"\u0672\3\2\2\2\u0672\u0115\3\2\2\2\u0673\u0671\3\2\2")
        buf.write(u"\2\u0674\u0678\5\u0120\u0091\2\u0675\u0678\5\u0122\u0092")
        buf.write(u"\2\u0676\u0678\5\u0124\u0093\2\u0677\u0674\3\2\2\2\u0677")
        buf.write(u"\u0675\3\2\2\2\u0677\u0676\3\2\2\2\u0678\u0117\3\2\2")
        buf.write(u"\2\u0679\u067a\7\24\2\2\u067a\u067d\5\u011a\u008e\2\u067b")
        buf.write(u"\u067d\5\u011e\u0090\2\u067c\u0679\3\2\2\2\u067c\u067b")
        buf.write(u"\3\2\2\2\u067d\u0119\3\2\2\2\u067e\u067f\5\u0126\u0094")
        buf.write(u"\2\u067f\u0681\7\25\2\2\u0680\u0682\5\u011c\u008f\2\u0681")
        buf.write(u"\u0680\3\2\2\2\u0681\u0682\3\2\2\2\u0682\u0683\3\2\2")
        buf.write(u"\2\u0683\u0684\7\26\2\2\u0684\u011b\3\2\2\2\u0685\u0686")
        buf.write(u"\b\u008f\1\2\u0686\u0687\5\u0114\u008b\2\u0687\u068d")
        buf.write(u"\3\2\2\2\u0688\u0689\f\3\2\2\u0689\u068a\7\22\2\2\u068a")
        buf.write(u"\u068c\5\u0114\u008b\2\u068b\u0688\3\2\2\2\u068c\u068f")
        buf.write(u"\3\2\2\2\u068d\u068b\3\2\2\2\u068d\u068e\3\2\2\2\u068e")
        buf.write(u"\u011d\3\2\2\2\u068f\u068d\3\2\2\2\u0690\u0691\7\27\2")
        buf.write(u"\2\u0691\u0692\5\u0114\u008b\2\u0692\u0693\7\30\2\2\u0693")
        buf.write(u"\u011f\3\2\2\2\u0694\u0695\7\25\2\2\u0695\u0696\5\u0114")
        buf.write(u"\u008b\2\u0696\u0697\7\26\2\2\u0697\u0121\3\2\2\2\u0698")
        buf.write(u"\u0699\b\u0092\1\2\u0699\u069a\5\u0126\u0094\2\u069a")
        buf.write(u"\u06a0\3\2\2\2\u069b\u069c\f\3\2\2\u069c\u069d\7\24\2")
        buf.write(u"\2\u069d\u069f\5\u0126\u0094\2\u069e\u069b\3\2\2\2\u069f")
        buf.write(u"\u06a2\3\2\2\2\u06a0\u069e\3\2\2\2\u06a0\u06a1\3\2\2")
        buf.write(u"\2\u06a1\u0123\3\2\2\2\u06a2\u06a0\3\2\2\2\u06a3\u06a9")
        buf.write(u"\7\u0090\2\2\u06a4\u06a9\7\u0092\2\2\u06a5\u06a9\7\u008f")
        buf.write(u"\2\2\u06a6\u06a9\7\u0088\2\2\u06a7\u06a9\7\u0089\2\2")
        buf.write(u"\u06a8\u06a3\3\2\2\2\u06a8\u06a4\3\2\2\2\u06a8\u06a5")
        buf.write(u"\3\2\2\2\u06a8\u06a6\3\2\2\2\u06a8\u06a7\3\2\2\2\u06a9")
        buf.write(u"\u0125\3\2\2\2\u06aa\u06ab\t\6\2\2\u06ab\u0127\3\2\2")
        buf.write(u"\2\u06ac\u06ad\7x\2\2\u06ad\u06b0\5\u012a\u0096\2\u06ae")
        buf.write(u"\u06b0\5\u012a\u0096\2\u06af\u06ac\3\2\2\2\u06af\u06ae")
        buf.write(u"\3\2\2\2\u06b0\u0129\3\2\2\2\u06b1\u06b2\b\u0096\1\2")
        buf.write(u"\u06b2\u06b3\5\u012c\u0097\2\u06b3\u06b8\3\2\2\2\u06b4")
        buf.write(u"\u06b5\f\3\2\2\u06b5\u06b7\5\u012e\u0098\2\u06b6\u06b4")
        buf.write(u"\3\2\2\2\u06b7\u06ba\3\2\2\2\u06b8\u06b6\3\2\2\2\u06b8")
        buf.write(u"\u06b9\3\2\2\2\u06b9\u012b\3\2\2\2\u06ba\u06b8\3\2\2")
        buf.write(u"\2\u06bb\u06c0\5\u0138\u009d\2\u06bc\u06c0\5\u013a\u009e")
        buf.write(u"\2\u06bd\u06c0\5\u013c\u009f\2\u06be\u06c0\5\u0130\u0099")
        buf.write(u"\2\u06bf\u06bb\3\2\2\2\u06bf\u06bc\3\2\2\2\u06bf\u06bd")
        buf.write(u"\3\2\2\2\u06bf\u06be\3\2\2\2\u06c0\u012d\3\2\2\2\u06c1")
        buf.write(u"\u06c2\7\24\2\2\u06c2\u06c8\5\u0130\u0099\2\u06c3\u06c4")
        buf.write(u"\7\27\2\2\u06c4\u06c5\5\u012a\u0096\2\u06c5\u06c6\7\30")
        buf.write(u"\2\2\u06c6\u06c8\3\2\2\2\u06c7\u06c1\3\2\2\2\u06c7\u06c3")
        buf.write(u"\3\2\2\2\u06c8\u012f\3\2\2\2\u06c9\u06ca\5\u013e\u00a0")
        buf.write(u"\2\u06ca\u06cc\7\25\2\2\u06cb\u06cd\5\u0132\u009a\2\u06cc")
        buf.write(u"\u06cb\3\2\2\2\u06cc\u06cd\3\2\2\2\u06cd\u06ce\3\2\2")
        buf.write(u"\2\u06ce\u06cf\7\26\2\2\u06cf\u0131\3\2\2\2\u06d0\u06d7")
        buf.write(u"\5\u0134\u009b\2\u06d1\u06d7\5\u0136\u009c\2\u06d2\u06d3")
        buf.write(u"\5\u0134\u009b\2\u06d3\u06d4\7\22\2\2\u06d4\u06d5\5\u0136")
        buf.write(u"\u009c\2\u06d5\u06d7\3\2\2\2\u06d6\u06d0\3\2\2\2\u06d6")
        buf.write(u"\u06d1\3\2\2\2\u06d6\u06d2\3\2\2\2\u06d7\u0133\3\2\2")
        buf.write(u"\2\u06d8\u06d9\b\u009b\1\2\u06d9\u06da\5\u012a\u0096")
        buf.write(u"\2\u06da\u06e0\3\2\2\2\u06db\u06dc\f\3\2\2\u06dc\u06dd")
        buf.write(u"\7\22\2\2\u06dd\u06df\5\u012a\u0096\2\u06de\u06db\3\2")
        buf.write(u"\2\2\u06df\u06e2\3\2\2\2\u06e0\u06de\3\2\2\2\u06e0\u06e1")
        buf.write(u"\3\2\2\2\u06e1\u0135\3\2\2\2\u06e2\u06e0\3\2\2\2\u06e3")
        buf.write(u"\u06e4\b\u009c\1\2\u06e4\u06e5\5\u013e\u00a0\2\u06e5")
        buf.write(u"\u06e6\7-\2\2\u06e6\u06e7\5\u012a\u0096\2\u06e7\u06f0")
        buf.write(u"\3\2\2\2\u06e8\u06e9\f\3\2\2\u06e9\u06ea\7\22\2\2\u06ea")
        buf.write(u"\u06eb\5\u013e\u00a0\2\u06eb\u06ec\7-\2\2\u06ec\u06ed")
        buf.write(u"\5\u012a\u0096\2\u06ed\u06ef\3\2\2\2\u06ee\u06e8\3\2")
        buf.write(u"\2\2\u06ef\u06f2\3\2\2\2\u06f0\u06ee\3\2\2\2\u06f0\u06f1")
        buf.write(u"\3\2\2\2\u06f1\u0137\3\2\2\2\u06f2\u06f0\3\2\2\2\u06f3")
        buf.write(u"\u06f4\7\25\2\2\u06f4\u06f5\5\u012a\u0096\2\u06f5\u06f6")
        buf.write(u"\7\26\2\2\u06f6\u0139\3\2\2\2\u06f7\u06f8\b\u009e\1\2")
        buf.write(u"\u06f8\u06f9\5\u013e\u00a0\2\u06f9\u06ff\3\2\2\2\u06fa")
        buf.write(u"\u06fb\f\3\2\2\u06fb\u06fc\7\24\2\2\u06fc\u06fe\5\u013e")
        buf.write(u"\u00a0\2\u06fd\u06fa\3\2\2\2\u06fe\u0701\3\2\2\2\u06ff")
        buf.write(u"\u06fd\3\2\2\2\u06ff\u0700\3\2\2\2\u0700\u013b\3\2\2")
        buf.write(u"\2\u0701\u06ff\3\2\2\2\u0702\u0708\7\u0090\2\2\u0703")
        buf.write(u"\u0708\7\u0092\2\2\u0704\u0708\7\u008f\2\2\u0705\u0708")
        buf.write(u"\7\u0088\2\2\u0706\u0708\7\u0089\2\2\u0707\u0702\3\2")
        buf.write(u"\2\2\u0707\u0703\3\2\2\2\u0707\u0704\3\2\2\2\u0707\u0705")
        buf.write(u"\3\2\2\2\u0707\u0706\3\2\2\2\u0708\u013d\3\2\2\2\u0709")
        buf.write(u"\u070a\t\7\2\2\u070a\u013f\3\2\2\2\u070b\u070c\7x\2\2")
        buf.write(u"\u070c\u070d\5\u0142\u00a2\2\u070d\u070e\7\21\2\2\u070e")
        buf.write(u"\u0713\3\2\2\2\u070f\u0710\5\u0142\u00a2\2\u0710\u0711")
        buf.write(u"\7\21\2\2\u0711\u0713\3\2\2\2\u0712\u070b\3\2\2\2\u0712")
        buf.write(u"\u070f\3\2\2\2\u0713\u0141\3\2\2\2\u0714\u0715\b\u00a2")
        buf.write(u"\1\2\u0715\u0716\5\u0144\u00a3\2\u0716\u071b\3\2\2\2")
        buf.write(u"\u0717\u0718\f\3\2\2\u0718\u071a\5\u0146\u00a4\2\u0719")
        buf.write(u"\u0717\3\2\2\2\u071a\u071d\3\2\2\2\u071b\u0719\3\2\2")
        buf.write(u"\2\u071b\u071c\3\2\2\2\u071c\u0143\3\2\2\2\u071d\u071b")
        buf.write(u"\3\2\2\2\u071e\u0722\5\u014e\u00a8\2\u071f\u0722\5\u0150")
        buf.write(u"\u00a9\2\u0720\u0722\5\u0154\u00ab\2\u0721\u071e\3\2")
        buf.write(u"\2\2\u0721\u071f\3\2\2\2\u0721\u0720\3\2\2\2\u0722\u0145")
        buf.write(u"\3\2\2\2\u0723\u0724\7\24\2\2\u0724\u0727\5\u0148\u00a5")
        buf.write(u"\2\u0725\u0727\5\u014c\u00a7\2\u0726\u0723\3\2\2\2\u0726")
        buf.write(u"\u0725\3\2\2\2\u0727\u0147\3\2\2\2\u0728\u0729\5\u0156")
        buf.write(u"\u00ac\2\u0729\u072b\7\25\2\2\u072a\u072c\5\u014a\u00a6")
        buf.write(u"\2\u072b\u072a\3\2\2\2\u072b\u072c\3\2\2\2\u072c\u072d")
        buf.write(u"\3\2\2\2\u072d\u072e\7\26\2\2\u072e\u0149\3\2\2\2\u072f")
        buf.write(u"\u0730\b\u00a6\1\2\u0730\u0731\5\u0142\u00a2\2\u0731")
        buf.write(u"\u0737\3\2\2\2\u0732\u0733\f\3\2\2\u0733\u0734\7\22\2")
        buf.write(u"\2\u0734\u0736\5\u0142\u00a2\2\u0735\u0732\3\2\2\2\u0736")
        buf.write(u"\u0739\3\2\2\2\u0737\u0735\3\2\2\2\u0737\u0738\3\2\2")
        buf.write(u"\2\u0738\u014b\3\2\2\2\u0739\u0737\3\2\2\2\u073a\u073b")
        buf.write(u"\7\27\2\2\u073b\u073c\5\u0142\u00a2\2\u073c\u073d\7\30")
        buf.write(u"\2\2\u073d\u014d\3\2\2\2\u073e\u073f\7\25\2\2\u073f\u0740")
        buf.write(u"\5\u0142\u00a2\2\u0740\u0741\7\26\2\2\u0741\u014f\3\2")
        buf.write(u"\2\2\u0742\u0743\b\u00a9\1\2\u0743\u0744\5\u0156\u00ac")
        buf.write(u"\2\u0744\u074a\3\2\2\2\u0745\u0746\f\3\2\2\u0746\u0747")
        buf.write(u"\7\24\2\2\u0747\u0749\5\u0156\u00ac\2\u0748\u0745\3\2")
        buf.write(u"\2\2\u0749\u074c\3\2\2\2\u074a\u0748\3\2\2\2\u074a\u074b")
        buf.write(u"\3\2\2\2\u074b\u0151\3\2\2\2\u074c\u074a\3\2\2\2\u074d")
        buf.write(u"\u074e\b\u00aa\1\2\u074e\u074f\5\u0150\u00a9\2\u074f")
        buf.write(u"\u0755\3\2\2\2\u0750\u0751\f\3\2\2\u0751\u0752\7\35\2")
        buf.write(u"\2\u0752\u0754\7\u008d\2\2\u0753\u0750\3\2\2\2\u0754")
        buf.write(u"\u0757\3\2\2\2\u0755\u0753\3\2\2\2\u0755\u0756\3\2\2")
        buf.write(u"\2\u0756\u0153\3\2\2\2\u0757\u0755\3\2\2\2\u0758\u075e")
        buf.write(u"\7\u0090\2\2\u0759\u075e\7\u0092\2\2\u075a\u075e\7\u008f")
        buf.write(u"\2\2\u075b\u075e\7\u0088\2\2\u075c\u075e\7\u0089\2\2")
        buf.write(u"\u075d\u0758\3\2\2\2\u075d\u0759\3\2\2\2\u075d\u075a")
        buf.write(u"\3\2\2\2\u075d\u075b\3\2\2\2\u075d\u075c\3\2\2\2\u075e")
        buf.write(u"\u0155\3\2\2\2\u075f\u0760\t\7\2\2\u0760\u0157\3\2\2")
        buf.write(u"\2\u0761\u0762\7x\2\2\u0762\u0763\5\u015a\u00ae\2\u0763")
        buf.write(u"\u0764\7\21\2\2\u0764\u0769\3\2\2\2\u0765\u0766\5\u015a")
        buf.write(u"\u00ae\2\u0766\u0767\7\21\2\2\u0767\u0769\3\2\2\2\u0768")
        buf.write(u"\u0761\3\2\2\2\u0768\u0765\3\2\2\2\u0769\u0159\3\2\2")
        buf.write(u"\2\u076a\u076b\b\u00ae\1\2\u076b\u076c\5\u015c\u00af")
        buf.write(u"\2\u076c\u0771\3\2\2\2\u076d\u076e\f\3\2\2\u076e\u0770")
        buf.write(u"\5\u015e\u00b0\2\u076f\u076d\3\2\2\2\u0770\u0773\3\2")
        buf.write(u"\2\2\u0771\u076f\3\2\2\2\u0771\u0772\3\2\2\2\u0772\u015b")
        buf.write(u"\3\2\2\2\u0773\u0771\3\2\2\2\u0774\u0778\5\u0166\u00b4")
        buf.write(u"\2\u0775\u0778\5\u0168\u00b5\2\u0776\u0778\5\u016a\u00b6")
        buf.write(u"\2\u0777\u0774\3\2\2\2\u0777\u0775\3\2\2\2\u0777\u0776")
        buf.write(u"\3\2\2\2\u0778\u015d\3\2\2\2\u0779\u077a\7\24\2\2\u077a")
        buf.write(u"\u077d\5\u0160\u00b1\2\u077b\u077d\5\u0164\u00b3\2\u077c")
        buf.write(u"\u0779\3\2\2\2\u077c\u077b\3\2\2\2\u077d\u015f\3\2\2")
        buf.write(u"\2\u077e\u077f\5\u016c\u00b7\2\u077f\u0781\7\25\2\2\u0780")
        buf.write(u"\u0782\5\u0162\u00b2\2\u0781\u0780\3\2\2\2\u0781\u0782")
        buf.write(u"\3\2\2\2\u0782\u0783\3\2\2\2\u0783\u0784\7\26\2\2\u0784")
        buf.write(u"\u0161\3\2\2\2\u0785\u0786\b\u00b2\1\2\u0786\u0787\5")
        buf.write(u"\u015a\u00ae\2\u0787\u078d\3\2\2\2\u0788\u0789\f\3\2")
        buf.write(u"\2\u0789\u078a\7\22\2\2\u078a\u078c\5\u015a\u00ae\2\u078b")
        buf.write(u"\u0788\3\2\2\2\u078c\u078f\3\2\2\2\u078d\u078b\3\2\2")
        buf.write(u"\2\u078d\u078e\3\2\2\2\u078e\u0163\3\2\2\2\u078f\u078d")
        buf.write(u"\3\2\2\2\u0790\u0791\7\27\2\2\u0791\u0792\5\u015a\u00ae")
        buf.write(u"\2\u0792\u0793\7\30\2\2\u0793\u0165\3\2\2\2\u0794\u0795")
        buf.write(u"\7\25\2\2\u0795\u0796\5\u015a\u00ae\2\u0796\u0797\7\26")
        buf.write(u"\2\2\u0797\u0167\3\2\2\2\u0798\u0799\b\u00b5\1\2\u0799")
        buf.write(u"\u079a\5\u016c\u00b7\2\u079a\u07a0\3\2\2\2\u079b\u079c")
        buf.write(u"\f\3\2\2\u079c\u079d\7\24\2\2\u079d\u079f\5\u016c\u00b7")
        buf.write(u"\2\u079e\u079b\3\2\2\2\u079f\u07a2\3\2\2\2\u07a0\u079e")
        buf.write(u"\3\2\2\2\u07a0\u07a1\3\2\2\2\u07a1\u0169\3\2\2\2\u07a2")
        buf.write(u"\u07a0\3\2\2\2\u07a3\u07a9\7\u0090\2\2\u07a4\u07a9\7")
        buf.write(u"\u0092\2\2\u07a5\u07a9\7\u008f\2\2\u07a6\u07a9\7\u0088")
        buf.write(u"\2\2\u07a7\u07a9\7\u0089\2\2\u07a8\u07a3\3\2\2\2\u07a8")
        buf.write(u"\u07a4\3\2\2\2\u07a8\u07a5\3\2\2\2\u07a8\u07a6\3\2\2")
        buf.write(u"\2\u07a8\u07a7\3\2\2\2\u07a9\u016b\3\2\2\2\u07aa\u07ab")
        buf.write(u"\t\7\2\2\u07ab\u016d\3\2\2\2\u0095\u0174\u0177\u0190")
        buf.write(u"\u019d\u01aa\u01b1\u01be\u01c8\u01cd\u01dc\u01fc\u0209")
        buf.write(u"\u0220\u022a\u022f\u0235\u023a\u0246\u024b\u0259\u025d")
        buf.write(u"\u026e\u0273\u027c\u0285\u028e\u02ab\u02be\u02c4\u02e6")
        buf.write(u"\u02ef\u0306\u0314\u031d\u0326\u033d\u0341\u0355\u03b5")
        buf.write(u"\u03b7\u03c3\u03cc\u03db\u03e2\u03eb\u03f2\u0411\u0421")
        buf.write(u"\u042a\u0430\u0435\u043c\u0444\u0452\u045a\u0460\u046b")
        buf.write(u"\u0477\u0482\u048f\u0493\u0499\u04a5\u04b9\u04bb\u04c0")
        buf.write(u"\u04cc\u04d7\u04e1\u04e6\u04eb\u04fb\u0500\u0504\u0509")
        buf.write(u"\u0510\u051b\u051d\u0529\u0530\u053c\u0540\u054a\u0552")
        buf.write(u"\u0558\u055f\u0564\u056e\u0574\u057f\u058c\u0590\u0593")
        buf.write(u"\u0597\u059a\u05a5\u05b1\u05bd\u05ce\u05dd\u05e7\u05ee")
        buf.write(u"\u05f8\u05ff\u0603\u0609\u0615\u0620\u0630\u063d\u0644")
        buf.write(u"\u064c\u0668\u0671\u0677\u067c\u0681\u068d\u06a0\u06a8")
        buf.write(u"\u06af\u06b8\u06bf\u06c7\u06cc\u06d6\u06e0\u06f0\u06ff")
        buf.write(u"\u0707\u0712\u071b\u0721\u0726\u072b\u0737\u074a\u0755")
        buf.write(u"\u075d\u0768\u0771\u0777\u077c\u0781\u078d\u07a0\u07a8")
        return buf.getvalue()
		

class PParser ( AbstractParser ):

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
    RULE_typed_argument = 20
    RULE_statement = 21
    RULE_method_call = 22
    RULE_method_selector = 23
    RULE_callable_parent = 24
    RULE_callable_selector = 25
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
    RULE_closure_expression = 40
    RULE_instance_expression = 41
    RULE_method_expression = 42
    RULE_instance_selector = 43
    RULE_document_expression = 44
    RULE_constructor_expression = 45
    RULE_argument_assignment_list = 46
    RULE_argument_assignment = 47
    RULE_read_expression = 48
    RULE_write_statement = 49
    RULE_fetch_expression = 50
    RULE_sorted_expression = 51
    RULE_assign_instance_statement = 52
    RULE_child_instance = 53
    RULE_assign_tuple_statement = 54
    RULE_lfs = 55
    RULE_lfp = 56
    RULE_indent = 57
    RULE_dedent = 58
    RULE_null_literal = 59
    RULE_declaration_list = 60
    RULE_declarations = 61
    RULE_declaration = 62
    RULE_resource_declaration = 63
    RULE_enum_declaration = 64
    RULE_native_symbol_list = 65
    RULE_category_symbol_list = 66
    RULE_symbol_list = 67
    RULE_attribute_constraint = 68
    RULE_list_literal = 69
    RULE_set_literal = 70
    RULE_expression_list = 71
    RULE_range_literal = 72
    RULE_typedef = 73
    RULE_primary_type = 74
    RULE_native_type = 75
    RULE_category_type = 76
    RULE_code_type = 77
    RULE_document_type = 78
    RULE_category_declaration = 79
    RULE_type_identifier_list = 80
    RULE_method_identifier = 81
    RULE_identifier = 82
    RULE_variable_identifier = 83
    RULE_type_identifier = 84
    RULE_symbol_identifier = 85
    RULE_argument_list = 86
    RULE_argument = 87
    RULE_operator_argument = 88
    RULE_named_argument = 89
    RULE_code_argument = 90
    RULE_category_or_any_type = 91
    RULE_any_type = 92
    RULE_category_method_declaration_list = 93
    RULE_category_method_declaration = 94
    RULE_native_category_mapping = 95
    RULE_python_category_mapping = 96
    RULE_python_module = 97
    RULE_module_token = 98
    RULE_javascript_category_mapping = 99
    RULE_javascript_module = 100
    RULE_variable_identifier_list = 101
    RULE_method_declaration = 102
    RULE_native_statement_list = 103
    RULE_native_statement = 104
    RULE_python_native_statement = 105
    RULE_javascript_native_statement = 106
    RULE_statement_list = 107
    RULE_switch_case_statement_list = 108
    RULE_catch_statement_list = 109
    RULE_literal_collection = 110
    RULE_atomic_literal = 111
    RULE_literal_list_literal = 112
    RULE_selectable_expression = 113
    RULE_this_expression = 114
    RULE_parenthesis_expression = 115
    RULE_literal_expression = 116
    RULE_collection_literal = 117
    RULE_tuple_literal = 118
    RULE_dict_literal = 119
    RULE_expression_tuple = 120
    RULE_dict_entry_list = 121
    RULE_dict_entry = 122
    RULE_slice_arguments = 123
    RULE_assign_variable_statement = 124
    RULE_assignable_instance = 125
    RULE_is_expression = 126
    RULE_operator = 127
    RULE_key_token = 128
    RULE_value_token = 129
    RULE_symbols_token = 130
    RULE_assign = 131
    RULE_multiply = 132
    RULE_divide = 133
    RULE_idivide = 134
    RULE_modulo = 135
    RULE_javascript_statement = 136
    RULE_javascript_expression = 137
    RULE_javascript_primary_expression = 138
    RULE_javascript_selector_expression = 139
    RULE_javascript_method_expression = 140
    RULE_javascript_arguments = 141
    RULE_javascript_item_expression = 142
    RULE_javascript_parenthesis_expression = 143
    RULE_javascript_identifier_expression = 144
    RULE_javascript_literal_expression = 145
    RULE_javascript_identifier = 146
    RULE_python_statement = 147
    RULE_python_expression = 148
    RULE_python_primary_expression = 149
    RULE_python_selector_expression = 150
    RULE_python_method_expression = 151
    RULE_python_argument_list = 152
    RULE_python_ordinal_argument_list = 153
    RULE_python_named_argument_list = 154
    RULE_python_parenthesis_expression = 155
    RULE_python_identifier_expression = 156
    RULE_python_literal_expression = 157
    RULE_python_identifier = 158
    RULE_java_statement = 159
    RULE_java_expression = 160
    RULE_java_primary_expression = 161
    RULE_java_selector_expression = 162
    RULE_java_method_expression = 163
    RULE_java_arguments = 164
    RULE_java_item_expression = 165
    RULE_java_parenthesis_expression = 166
    RULE_java_identifier_expression = 167
    RULE_java_class_identifier_expression = 168
    RULE_java_literal_expression = 169
    RULE_java_identifier = 170
    RULE_csharp_statement = 171
    RULE_csharp_expression = 172
    RULE_csharp_primary_expression = 173
    RULE_csharp_selector_expression = 174
    RULE_csharp_method_expression = 175
    RULE_csharp_arguments = 176
    RULE_csharp_item_expression = 177
    RULE_csharp_parenthesis_expression = 178
    RULE_csharp_identifier_expression = 179
    RULE_csharp_literal_expression = 180
    RULE_csharp_identifier = 181

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"member_method_declaration", u"operator_method_declaration", 
                   u"setter_method_declaration", u"getter_method_declaration", 
                   u"native_category_declaration", u"native_resource_declaration", 
                   u"native_category_mappings", u"native_category_mapping_list", 
                   u"attribute_list", u"abstract_method_declaration", u"concrete_method_declaration", 
                   u"native_method_declaration", u"typed_argument", u"statement", 
                   u"method_call", u"method_selector", u"callable_parent", 
                   u"callable_selector", u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"return_statement", u"expression", 
                   u"closure_expression", u"instance_expression", u"method_expression", 
                   u"instance_selector", u"document_expression", u"constructor_expression", 
                   u"argument_assignment_list", u"argument_assignment", 
                   u"read_expression", u"write_statement", u"fetch_expression", 
                   u"sorted_expression", u"assign_instance_statement", u"child_instance", 
                   u"assign_tuple_statement", u"lfs", u"lfp", u"indent", 
                   u"dedent", u"null_literal", u"declaration_list", u"declarations", 
                   u"declaration", u"resource_declaration", u"enum_declaration", 
                   u"native_symbol_list", u"category_symbol_list", u"symbol_list", 
                   u"attribute_constraint", u"list_literal", u"set_literal", 
                   u"expression_list", u"range_literal", u"typedef", u"primary_type", 
                   u"native_type", u"category_type", u"code_type", u"document_type", 
                   u"category_declaration", u"type_identifier_list", u"method_identifier", 
                   u"identifier", u"variable_identifier", u"type_identifier", 
                   u"symbol_identifier", u"argument_list", u"argument", 
                   u"operator_argument", u"named_argument", u"code_argument", 
                   u"category_or_any_type", u"any_type", u"category_method_declaration_list", 
                   u"category_method_declaration", u"native_category_mapping", 
                   u"python_category_mapping", u"python_module", u"module_token", 
                   u"javascript_category_mapping", u"javascript_module", 
                   u"variable_identifier_list", u"method_declaration", u"native_statement_list", 
                   u"native_statement", u"python_native_statement", u"javascript_native_statement", 
                   u"statement_list", u"switch_case_statement_list", u"catch_statement_list", 
                   u"literal_collection", u"atomic_literal", u"literal_list_literal", 
                   u"selectable_expression", u"this_expression", u"parenthesis_expression", 
                   u"literal_expression", u"collection_literal", u"tuple_literal", 
                   u"dict_literal", u"expression_tuple", u"dict_entry_list", 
                   u"dict_entry", u"slice_arguments", u"assign_variable_statement", 
                   u"assignable_instance", u"is_expression", u"operator", 
                   u"key_token", u"value_token", u"symbols_token", u"assign", 
                   u"multiply", u"divide", u"idivide", u"modulo", u"javascript_statement", 
                   u"javascript_expression", u"javascript_primary_expression", 
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
                   u"java_primary_expression", u"java_selector_expression", 
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
        super(PParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.symbols = None # Category_symbol_listContext

        def ENUM(self):
            return self.getToken(PParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(PParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(PParser.Category_symbol_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(PParser.Attribute_listContext,0)


        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)

        def getRuleIndex(self):
            return PParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = PParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(PParser.ENUM)
            self.state = 365 
            localctx.name = self.type_identifier()
            self.state = 366
            self.match(PParser.LPAR)
            self.state = 373
            token = self._input.LA(1)
            if token in [PParser.TYPE_IDENTIFIER]:
                self.state = 367 
                localctx.derived = self.type_identifier()
                self.state = 370
                _la = self._input.LA(1)
                if _la==PParser.COMMA:
                    self.state = 368
                    self.match(PParser.COMMA)
                    self.state = 369 
                    localctx.attrs = self.attribute_list()



            elif token in [PParser.VARIABLE_IDENTIFIER]:
                self.state = 372 
                localctx.attrs = self.attribute_list()

            else:
                raise NoViableAltException(self)

            self.state = 375
            self.match(PParser.RPAR)
            self.state = 376
            self.match(PParser.COLON)
            self.state = 377 
            self.indent()
            self.state = 378 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 379 
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
            super(PParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUM(self):
            return self.getToken(PParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(PParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(PParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = PParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(PParser.ENUM)
            self.state = 382 
            localctx.name = self.type_identifier()
            self.state = 383
            self.match(PParser.LPAR)
            self.state = 384 
            localctx.typ = self.native_type()
            self.state = 385
            self.match(PParser.RPAR)
            self.state = 386
            self.match(PParser.COLON)
            self.state = 387 
            self.indent()
            self.state = 388 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 389 
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
            super(PParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(PParser.EQ, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_native_symbol

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = PParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391 
            localctx.name = self.symbol_identifier()
            self.state = 392
            self.match(PParser.EQ)
            self.state = 393 
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
            super(PParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(PParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_category_symbol

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = PParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395 
            localctx.name = self.symbol_identifier()
            self.state = 396
            self.match(PParser.LPAR)
            self.state = 398
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 397 
                localctx.args = self.argument_assignment_list(0)


            self.state = 400
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext

        def ATTR(self):
            return self.getToken(PParser.ATTR, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def PASS(self):
            return self.getToken(PParser.PASS, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(PParser.Attribute_constraintContext,0)


        def getRuleIndex(self):
            return PParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = PParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(PParser.ATTR)
            self.state = 403 
            localctx.name = self.variable_identifier()
            self.state = 404
            self.match(PParser.LPAR)
            self.state = 405 
            localctx.typ = self.typedef(0)
            self.state = 406
            self.match(PParser.RPAR)
            self.state = 407
            self.match(PParser.COLON)
            self.state = 408 
            self.indent()
            self.state = 411
            token = self._input.LA(1)
            if token in [PParser.IN, PParser.MATCHING]:
                self.state = 409 
                localctx.match = self.attribute_constraint()

            elif token in [PParser.PASS]:
                self.state = 410
                self.match(PParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 413 
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
            super(PParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Category_method_declaration_listContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(PParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(PParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)

        def PASS(self):
            return self.getToken(PParser.PASS, 0)

        def derived_list(self):
            return self.getTypedRuleContext(PParser.Derived_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(PParser.Attribute_listContext,0)


        def category_method_declaration_list(self):
            return self.getTypedRuleContext(PParser.Category_method_declaration_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = PParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not(_la==PParser.CATEGORY or _la==PParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 416 
            localctx.name = self.type_identifier()
            self.state = 417
            self.match(PParser.LPAR)
            self.state = 424
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 418 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 419 
                localctx.attrs = self.attribute_list()
                pass

            elif la_ == 3:
                self.state = 420 
                localctx.derived = self.derived_list()
                self.state = 421
                self.match(PParser.COMMA)
                self.state = 422 
                localctx.attrs = self.attribute_list()
                pass


            self.state = 426
            self.match(PParser.RPAR)
            self.state = 427
            self.match(PParser.COLON)
            self.state = 428 
            self.indent()
            self.state = 431
            token = self._input.LA(1)
            if token in [PParser.DEF]:
                self.state = 429 
                localctx.methods = self.category_method_declaration_list(0)

            elif token in [PParser.PASS]:
                self.state = 430
                self.match(PParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 433 
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
            super(PParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Category_method_declaration_listContext

        def SINGLETON(self):
            return self.getToken(PParser.SINGLETON, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(PParser.Attribute_listContext,0)


        def PASS(self):
            return self.getToken(PParser.PASS, 0)

        def category_method_declaration_list(self):
            return self.getTypedRuleContext(PParser.Category_method_declaration_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = PParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(PParser.SINGLETON)
            self.state = 436 
            localctx.name = self.type_identifier()
            self.state = 437
            self.match(PParser.LPAR)
            self.state = 438 
            localctx.attrs = self.attribute_list()
            self.state = 439
            self.match(PParser.RPAR)
            self.state = 440
            self.match(PParser.COLON)
            self.state = 441 
            self.indent()
            self.state = 444
            token = self._input.LA(1)
            if token in [PParser.DEF]:
                self.state = 442 
                localctx.methods = self.category_method_declaration_list(0)

            elif token in [PParser.PASS]:
                self.state = 443
                self.match(PParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 446 
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
            super(PParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Type_identifier_listContext

        def type_identifier_list(self):
            return self.getTypedRuleContext(PParser.Type_identifier_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_derived_list

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDerived_list(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDerived_list(self)




    def derived_list(self):

        localctx = PParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448 
            localctx.items = self.type_identifier_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(PParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(PParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(PParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def getRuleIndex(self):
            return PParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = PParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_member_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(PParser.DEF)
            self.state = 451 
            localctx.name = self.method_identifier()
            self.state = 452
            self.match(PParser.LPAR)
            self.state = 454
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 453 
                localctx.args = self.argument_list(0)


            self.state = 456
            self.match(PParser.RPAR)
            self.state = 459
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 457
                self.match(PParser.RARROW)
                self.state = 458 
                localctx.typ = self.typedef(0)


            self.state = 461
            self.match(PParser.COLON)
            self.state = 462 
            self.indent()
            self.state = 463 
            localctx.stmts = self.statement_list(0)
            self.state = 464 
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
            super(PParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def OPERATOR(self):
            return self.getToken(PParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(PParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(PParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(PParser.RARROW, 0)

        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def getRuleIndex(self):
            return PParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = PParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(PParser.DEF)
            self.state = 467
            self.match(PParser.OPERATOR)
            self.state = 468 
            localctx.op = self.operator()
            self.state = 469
            self.match(PParser.LPAR)
            self.state = 470 
            localctx.arg = self.operator_argument()
            self.state = 471
            self.match(PParser.RPAR)
            self.state = 474
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 472
                self.match(PParser.RARROW)
                self.state = 473 
                localctx.typ = self.typedef(0)


            self.state = 476
            self.match(PParser.COLON)
            self.state = 477 
            self.indent()
            self.state = 478 
            localctx.stmts = self.statement_list(0)
            self.state = 479 
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
            super(PParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def SETTER(self):
            return self.getToken(PParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = PParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(PParser.DEF)
            self.state = 482 
            localctx.name = self.variable_identifier()
            self.state = 483
            self.match(PParser.SETTER)
            self.state = 484
            self.match(PParser.LPAR)
            self.state = 485
            self.match(PParser.RPAR)
            self.state = 486
            self.match(PParser.COLON)
            self.state = 487 
            self.indent()
            self.state = 488 
            localctx.stmts = self.statement_list(0)
            self.state = 489 
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
            super(PParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def GETTER(self):
            return self.getToken(PParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = PParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(PParser.DEF)
            self.state = 492 
            localctx.name = self.variable_identifier()
            self.state = 493
            self.match(PParser.GETTER)
            self.state = 494
            self.match(PParser.LPAR)
            self.state = 495
            self.match(PParser.RPAR)
            self.state = 496
            self.match(PParser.COLON)
            self.state = 497 
            self.indent()
            self.state = 498 
            localctx.stmts = self.statement_list(0)
            self.state = 499 
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
            super(PParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.mappings = None # Native_category_mappingsContext

        def NATIVE(self):
            return self.getToken(PParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(PParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(PParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def native_category_mappings(self):
            return self.getTypedRuleContext(PParser.Native_category_mappingsContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(PParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = PParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(PParser.NATIVE)
            self.state = 502
            _la = self._input.LA(1)
            if not(_la==PParser.CATEGORY or _la==PParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 503 
            localctx.name = self.type_identifier()
            self.state = 504
            self.match(PParser.LPAR)
            self.state = 506
            _la = self._input.LA(1)
            if _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 505 
                localctx.attrs = self.attribute_list()


            self.state = 508
            self.match(PParser.RPAR)
            self.state = 509
            self.match(PParser.COLON)
            self.state = 510 
            self.indent()
            self.state = 511 
            localctx.mappings = self.native_category_mappings()
            self.state = 512 
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
            super(PParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.mappings = None # Native_category_mappingsContext

        def NATIVE(self):
            return self.getToken(PParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(PParser.RESOURCE, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def native_category_mappings(self):
            return self.getTypedRuleContext(PParser.Native_category_mappingsContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(PParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = PParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(PParser.NATIVE)
            self.state = 515
            self.match(PParser.RESOURCE)
            self.state = 516 
            localctx.name = self.type_identifier()
            self.state = 517
            self.match(PParser.LPAR)
            self.state = 519
            _la = self._input.LA(1)
            if _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 518 
                localctx.attrs = self.attribute_list()


            self.state = 521
            self.match(PParser.RPAR)
            self.state = 522
            self.match(PParser.COLON)
            self.state = 523 
            self.indent()
            self.state = 524 
            localctx.mappings = self.native_category_mappings()
            self.state = 525 
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
            super(PParser.Native_category_mappingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_mapping_listContext

        def MAPPINGS(self):
            return self.getToken(PParser.MAPPINGS, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def native_category_mapping_list(self):
            return self.getTypedRuleContext(PParser.Native_category_mapping_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_native_category_mappings

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNative_category_mappings(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNative_category_mappings(self)




    def native_category_mappings(self):

        localctx = PParser.Native_category_mappingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_category_mappings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(PParser.MAPPINGS)
            self.state = 528
            self.match(PParser.COLON)
            self.state = 529 
            self.indent()
            self.state = 530 
            localctx.items = self.native_category_mapping_list(0)
            self.state = 531 
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
            super(PParser.Native_category_mapping_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_native_category_mapping_list

     
        def copyFrom(self, ctx):
            super(PParser.Native_category_mapping_listContext, self).copyFrom(ctx)


    class NativeCategoryMappingListContext(Native_category_mapping_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mapping_listContext)
            super(PParser.NativeCategoryMappingListContext, self).__init__(parser)
            self.item = None # Native_category_mappingContext
            self.copyFrom(ctx)

        def native_category_mapping(self):
            return self.getTypedRuleContext(PParser.Native_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeCategoryMappingList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeCategoryMappingList(self)


    class NativeCategoryMappingListItemContext(Native_category_mapping_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mapping_listContext)
            super(PParser.NativeCategoryMappingListItemContext, self).__init__(parser)
            self.items = None # Native_category_mapping_listContext
            self.item = None # Native_category_mappingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def native_category_mapping_list(self):
            return self.getTypedRuleContext(PParser.Native_category_mapping_listContext,0)

        def native_category_mapping(self):
            return self.getTypedRuleContext(PParser.Native_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeCategoryMappingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeCategoryMappingListItem(self)



    def native_category_mapping_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Native_category_mapping_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_native_category_mapping_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.NativeCategoryMappingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 534 
            localctx.item = self.native_category_mapping()
            self._ctx.stop = self._input.LT(-1)
            self.state = 542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.NativeCategoryMappingListItemContext(self, PParser.Native_category_mapping_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_mapping_list)
                    self.state = 536
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 537 
                    self.lfp()
                    self.state = 538 
                    localctx.item = self.native_category_mapping() 
                self.state = 544
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext

        def variable_identifier_list(self):
            return self.getTypedRuleContext(PParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_attribute_list

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAttribute_list(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAttribute_list(self)




    def attribute_list(self):

        localctx = PParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attribute_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545 
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
            super(PParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext

        def ABSTRACT(self):
            return self.getToken(PParser.ABSTRACT, 0)

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(PParser.Method_identifierContext,0)


        def RARROW(self):
            return self.getToken(PParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(PParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def getRuleIndex(self):
            return PParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = PParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(PParser.ABSTRACT)
            self.state = 548
            self.match(PParser.DEF)
            self.state = 549 
            localctx.name = self.method_identifier()
            self.state = 550
            self.match(PParser.LPAR)
            self.state = 552
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 551 
                localctx.args = self.argument_list(0)


            self.state = 554
            self.match(PParser.RPAR)
            self.state = 557
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 555
                self.match(PParser.RARROW)
                self.state = 556 
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
            super(PParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(PParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(PParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(PParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def getRuleIndex(self):
            return PParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = PParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(PParser.DEF)
            self.state = 560 
            localctx.name = self.method_identifier()
            self.state = 561
            self.match(PParser.LPAR)
            self.state = 563
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 562 
                localctx.args = self.argument_list(0)


            self.state = 565
            self.match(PParser.RPAR)
            self.state = 568
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 566
                self.match(PParser.RARROW)
                self.state = 567 
                localctx.typ = self.typedef(0)


            self.state = 570
            self.match(PParser.COLON)
            self.state = 571 
            self.indent()
            self.state = 572 
            localctx.stmts = self.statement_list(0)
            self.state = 573 
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
            super(PParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def NATIVE(self):
            return self.getToken(PParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(PParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(PParser.Native_statement_listContext,0)


        def RARROW(self):
            return self.getToken(PParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(PParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def getRuleIndex(self):
            return PParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = PParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.match(PParser.DEF)
            self.state = 576
            self.match(PParser.NATIVE)
            self.state = 577 
            localctx.name = self.method_identifier()
            self.state = 578
            self.match(PParser.LPAR)
            self.state = 580
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 579 
                localctx.args = self.argument_list(0)


            self.state = 582
            self.match(PParser.RPAR)
            self.state = 585
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 583
                self.match(PParser.RARROW)
                self.state = 584 
                localctx.typ = self.typedef(0)


            self.state = 587
            self.match(PParser.COLON)
            self.state = 588 
            self.indent()
            self.state = 589 
            localctx.stmts = self.native_statement_list(0)
            self.state = 590 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_listContext
            self.value = None # Literal_expressionContext

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(PParser.Category_or_any_typeContext,0)


        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def EQ(self):
            return self.getToken(PParser.EQ, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(PParser.Attribute_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(PParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_typed_argument

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = PParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592 
            localctx.name = self.variable_identifier()
            self.state = 593
            self.match(PParser.COLON)
            self.state = 594 
            localctx.typ = self.category_or_any_type()
            self.state = 599
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 595
                self.match(PParser.LPAR)
                self.state = 596 
                localctx.attrs = self.attribute_list()
                self.state = 597
                self.match(PParser.RPAR)


            self.state = 603
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 601
                self.match(PParser.EQ)
                self.state = 602 
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
            super(PParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(PParser.StatementContext, self).copyFrom(ctx)



    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(PParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssignInstanceStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(PParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWithResourceStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(PParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssignTupleStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(PParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(PParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWhileStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(PParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitClosureStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(PParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodCallStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(PParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWithSingletonStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(PParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitReturnStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(PParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDoWhileStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(PParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(PParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSwitchStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(PParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRaiseStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(PParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitForEachStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a PParser.StatementContext)
            super(PParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(PParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTryStatement(self)



    def statement(self):

        localctx = PParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 620
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = PParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 605 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = PParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 606 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = PParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 607 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = PParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 608 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 5:
                localctx = PParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 609 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 6:
                localctx = PParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 610 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 7:
                localctx = PParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 611 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 8:
                localctx = PParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 612 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 9:
                localctx = PParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 613 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 10:
                localctx = PParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 614 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 11:
                localctx = PParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 615 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 12:
                localctx = PParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 616 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 13:
                localctx = PParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 617 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 14:
                localctx = PParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 618 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 15:
                localctx = PParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 619 
                localctx.decl = self.concrete_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(PParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(PParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_method_call

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = PParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622 
            localctx.method = self.method_selector()
            self.state = 623
            self.match(PParser.LPAR)
            self.state = 625
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 624 
                localctx.args = self.argument_assignment_list(0)


            self.state = 627
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(PParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_selectorContext)
            super(PParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(PParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodName(self)


    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_selectorContext)
            super(PParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(PParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(PParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodParent(self)



    def method_selector(self):

        localctx = PParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_selector)
        try:
            self.state = 634
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = PParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 629 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = PParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 630 
                localctx.parent = self.callable_parent(0)
                self.state = 631
                self.match(PParser.DOT)
                self.state = 632 
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
            super(PParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(PParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a PParser.Callable_parentContext)
            super(PParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(PParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCallableRoot(self)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a PParser.Callable_parentContext)
            super(PParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(PParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(PParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCallableSelector(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 637 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 643
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CallableSelectorContext(self, PParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 639
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 640 
                    localctx.select = self.callable_selector() 
                self.state = 645
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(PParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Callable_selectorContext)
            super(PParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Callable_selectorContext)
            super(PParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = PParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_callable_selector)
        try:
            self.state = 652
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.match(PParser.DOT)
                self.state = 647 
                localctx.name = self.variable_identifier()

            elif token in [PParser.LBRAK]:
                localctx = PParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 648
                self.match(PParser.LBRAK)
                self.state = 649 
                localctx.exp = self.expression(0)
                self.state = 650
                self.match(PParser.RBRAK)

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
            super(PParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(PParser.WITH, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(PParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = PParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(PParser.WITH)
            self.state = 655 
            localctx.stmt = self.assign_variable_statement()
            self.state = 656
            self.match(PParser.COLON)
            self.state = 657 
            self.indent()
            self.state = 658 
            localctx.stmts = self.statement_list(0)
            self.state = 659 
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
            super(PParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(PParser.WITH, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = PParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(PParser.WITH)
            self.state = 662 
            localctx.typ = self.type_identifier()
            self.state = 663
            self.match(PParser.COLON)
            self.state = 664 
            self.indent()
            self.state = 665 
            localctx.stmts = self.statement_list(0)
            self.state = 666 
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
            super(PParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(PParser.SWITCH, 0)

        def ON(self):
            return self.getToken(PParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(PParser.COLON)
            else:
                return self.getToken(PParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.IndentContext)
            else:
                return self.getTypedRuleContext(PParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.DedentContext)
            else:
                return self.getTypedRuleContext(PParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(PParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(PParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_switch_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = PParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(PParser.SWITCH)
            self.state = 669
            self.match(PParser.ON)
            self.state = 670 
            localctx.exp = self.expression(0)
            self.state = 671
            self.match(PParser.COLON)
            self.state = 672 
            self.indent()
            self.state = 673 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 681
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 674 
                self.lfp()
                self.state = 675
                self.match(PParser.OTHERWISE)
                self.state = 676
                self.match(PParser.COLON)
                self.state = 677 
                self.indent()
                self.state = 678 
                localctx.stmts = self.statement_list(0)
                self.state = 679 
                self.dedent()


            self.state = 683 
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
            super(PParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(PParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Switch_case_statementContext)
            super(PParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(PParser.WHEN, 0)
        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(PParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Switch_case_statementContext)
            super(PParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(PParser.WHEN, 0)
        def IN(self):
            return self.getToken(PParser.IN, 0)
        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(PParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = PParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_switch_case_statement)
        try:
            self.state = 700
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = PParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                self.match(PParser.WHEN)
                self.state = 686 
                localctx.exp = self.atomic_literal()
                self.state = 687
                self.match(PParser.COLON)
                self.state = 688 
                self.indent()
                self.state = 689 
                localctx.stmts = self.statement_list(0)
                self.state = 690 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = PParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                self.match(PParser.WHEN)
                self.state = 693
                self.match(PParser.IN)
                self.state = 694 
                localctx.exp = self.literal_collection()
                self.state = 695
                self.match(PParser.COLON)
                self.state = 696 
                self.indent()
                self.state = 697 
                localctx.stmts = self.statement_list(0)
                self.state = 698 
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
            super(PParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(PParser.FOR, 0)

        def IN(self):
            return self.getToken(PParser.IN, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(PParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)

        def getRuleIndex(self):
            return PParser.RULE_for_each_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = PParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.match(PParser.FOR)
            self.state = 703 
            localctx.name1 = self.variable_identifier()
            self.state = 706
            _la = self._input.LA(1)
            if _la==PParser.COMMA:
                self.state = 704
                self.match(PParser.COMMA)
                self.state = 705 
                localctx.name2 = self.variable_identifier()


            self.state = 708
            self.match(PParser.IN)
            self.state = 709 
            localctx.source = self.expression(0)
            self.state = 710
            self.match(PParser.COLON)
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

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(PParser.DO, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(PParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_do_while_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = PParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
            self.match(PParser.DO)
            self.state = 716
            self.match(PParser.COLON)
            self.state = 717 
            self.indent()
            self.state = 718 
            localctx.stmts = self.statement_list(0)
            self.state = 719 
            self.dedent()
            self.state = 720 
            self.lfp()
            self.state = 721
            self.match(PParser.WHILE)
            self.state = 722 
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
            super(PParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(PParser.WHILE, 0)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_while_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = PParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(PParser.WHILE)
            self.state = 725 
            localctx.exp = self.expression(0)
            self.state = 726
            self.match(PParser.COLON)
            self.state = 727 
            self.indent()
            self.state = 728 
            localctx.stmts = self.statement_list(0)
            self.state = 729 
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
            super(PParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(PParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(PParser.COLON)
            else:
                return self.getToken(PParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.IndentContext)
            else:
                return self.getTypedRuleContext(PParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.DedentContext)
            else:
                return self.getTypedRuleContext(PParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(PParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.LfpContext)
            else:
                return self.getTypedRuleContext(PParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(PParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(PParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_if_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = PParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 731
            self.match(PParser.IF)
            self.state = 732 
            localctx.exp = self.expression(0)
            self.state = 733
            self.match(PParser.COLON)
            self.state = 734 
            self.indent()
            self.state = 735 
            localctx.stmts = self.statement_list(0)
            self.state = 736 
            self.dedent()
            self.state = 740
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 737 
                self.lfp()
                self.state = 738 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 749
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 742 
                self.lfp()
                self.state = 743
                self.match(PParser.ELSE)
                self.state = 744
                self.match(PParser.COLON)
                self.state = 745 
                self.indent()
                self.state = 746 
                localctx.elseStmts = self.statement_list(0)
                self.state = 747 
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
            super(PParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(PParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Else_if_statement_listContext)
            super(PParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(PParser.ELSE, 0)
        def IF(self):
            return self.getToken(PParser.IF, 0)
        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Else_if_statement_listContext)
            super(PParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(PParser.ELSE, 0)
        def IF(self):
            return self.getToken(PParser.IF, 0)
        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(PParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 752
            self.match(PParser.ELSE)
            self.state = 753
            self.match(PParser.IF)
            self.state = 754 
            localctx.exp = self.expression(0)
            self.state = 755
            self.match(PParser.COLON)
            self.state = 756 
            self.indent()
            self.state = 757 
            localctx.stmts = self.statement_list(0)
            self.state = 758 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 772
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ElseIfStatementListItemContext(self, PParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 760
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 761 
                    self.lfp()
                    self.state = 762
                    self.match(PParser.ELSE)
                    self.state = 763
                    self.match(PParser.IF)
                    self.state = 764 
                    localctx.exp = self.expression(0)
                    self.state = 765
                    self.match(PParser.COLON)
                    self.state = 766 
                    self.indent()
                    self.state = 767 
                    localctx.stmts = self.statement_list(0)
                    self.state = 768 
                    self.dedent() 
                self.state = 774
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(PParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_raise_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = PParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.match(PParser.RAISE)
            self.state = 776 
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
            super(PParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(PParser.TRY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(PParser.COLON)
            else:
                return self.getToken(PParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.IndentContext)
            else:
                return self.getTypedRuleContext(PParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.DedentContext)
            else:
                return self.getTypedRuleContext(PParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.LfsContext)
            else:
                return self.getTypedRuleContext(PParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(PParser.Statement_listContext,i)


        def EXCEPT(self):
            return self.getToken(PParser.EXCEPT, 0)

        def FINALLY(self):
            return self.getToken(PParser.FINALLY, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(PParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_try_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = PParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778
            self.match(PParser.TRY)
            self.state = 779 
            localctx.name = self.variable_identifier()
            self.state = 780
            self.match(PParser.COLON)
            self.state = 781 
            self.indent()
            self.state = 782 
            localctx.stmts = self.statement_list(0)
            self.state = 783 
            self.dedent()
            self.state = 784 
            self.lfs()
            self.state = 786
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 785 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 795
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 788
                self.match(PParser.EXCEPT)
                self.state = 789
                self.match(PParser.COLON)
                self.state = 790 
                self.indent()
                self.state = 791 
                localctx.anyStmts = self.statement_list(0)
                self.state = 792 
                self.dedent()
                self.state = 793 
                self.lfs()


            self.state = 804
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 797
                self.match(PParser.FINALLY)
                self.state = 798
                self.match(PParser.COLON)
                self.state = 799 
                self.indent()
                self.state = 800 
                localctx.finalStmts = self.statement_list(0)
                self.state = 801 
                self.dedent()
                self.state = 802 
                self.lfs()


            self.state = 806 
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
            super(PParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(PParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Catch_statementContext)
            super(PParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(PParser.EXCEPT, 0)
        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(PParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Catch_statementContext)
            super(PParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(PParser.EXCEPT, 0)
        def IN(self):
            return self.getToken(PParser.IN, 0)
        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(PParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(PParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(PParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(PParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = PParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_catch_statement)
        try:
            self.state = 827
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = PParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 808
                self.match(PParser.EXCEPT)
                self.state = 809 
                localctx.name = self.symbol_identifier()
                self.state = 810
                self.match(PParser.COLON)
                self.state = 811 
                self.indent()
                self.state = 812 
                localctx.stmts = self.statement_list(0)
                self.state = 813 
                self.dedent()
                self.state = 814 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = PParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 816
                self.match(PParser.EXCEPT)
                self.state = 817
                self.match(PParser.IN)
                self.state = 818
                self.match(PParser.LBRAK)
                self.state = 819 
                localctx.exp = self.symbol_list(0)
                self.state = 820
                self.match(PParser.RBRAK)
                self.state = 821
                self.match(PParser.COLON)
                self.state = 822 
                self.indent()
                self.state = 823 
                localctx.stmts = self.statement_list(0)
                self.state = 824 
                self.dedent()
                self.state = 825 
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
            super(PParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(PParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_return_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = PParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(PParser.RETURN)
            self.state = 831
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 830 
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
            super(PParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(PParser.ExpressionContext, self).copyFrom(ctx)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(PParser.IF, 0)
        def ELSE(self):
            return self.getToken(PParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTernaryExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(PParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitClosureExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(PParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOrExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(PParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitEqualsExpression(self)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(PParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIntDivideExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(PParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(PParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNotContainsAnyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(PParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRoughlyEqualsExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(PParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitContainsExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(PParser.CODE, 0)
        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCodeExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(PParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(PParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitInExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(PParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(PParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCastExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(PParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitInstanceExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNotExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(PParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(PParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitGreaterThanExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(PParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(PParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAddExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(PParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitModuloExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(PParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(PParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(PParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNotContainsAllExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(PParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLessThanOrEqualExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(PParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMultiplyExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(PParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAndExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(PParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDivideExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(PParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitExecuteExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(PParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(PParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitContainsAllExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(PParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLessThanExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PParser.NOT, 0)
        def IN(self):
            return self.getToken(PParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNotInExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(PParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNotContainsExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(PParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(PParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitContainsAnyExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(PParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(PParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(PParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMinusExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a PParser.ExpressionContext)
            super(PParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(PParser.IS, 0)
        def NOT(self):
            return self.getToken(PParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(PParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIsNotExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 851
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = PParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 834
                self.match(PParser.MINUS)
                self.state = 835 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 2:
                localctx = PParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 836
                self.match(PParser.NOT)
                self.state = 837 
                localctx.exp = self.expression(30)
                pass

            elif la_ == 3:
                localctx = PParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 838 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = PParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 839 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = PParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 840
                self.match(PParser.CODE)
                self.state = 841
                self.match(PParser.LPAR)
                self.state = 842 
                localctx.exp = self.expression(0)
                self.state = 843
                self.match(PParser.RPAR)
                pass

            elif la_ == 6:
                localctx = PParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 845
                self.match(PParser.EXECUTE)
                self.state = 846
                self.match(PParser.LPAR)
                self.state = 847 
                localctx.name = self.variable_identifier()
                self.state = 848
                self.match(PParser.RPAR)
                pass

            elif la_ == 7:
                localctx = PParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 850 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 949
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 947
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = PParser.MultiplyExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 853
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 854 
                        self.multiply()
                        self.state = 855 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 2:
                        localctx = PParser.DivideExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 857
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 858 
                        self.divide()
                        self.state = 859 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 3:
                        localctx = PParser.ModuloExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 861
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 862 
                        self.modulo()
                        self.state = 863 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 4:
                        localctx = PParser.IntDivideExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 865
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 866 
                        self.idivide()
                        self.state = 867 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 5:
                        localctx = PParser.AddExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 869
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 870
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PParser.PLUS or _la==PParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 871 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 6:
                        localctx = PParser.LessThanExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 872
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 873
                        self.match(PParser.LT)
                        self.state = 874 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 7:
                        localctx = PParser.LessThanOrEqualExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 875
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 876
                        self.match(PParser.LTE)
                        self.state = 877 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 8:
                        localctx = PParser.GreaterThanExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 878
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 879
                        self.match(PParser.GT)
                        self.state = 880 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 9:
                        localctx = PParser.GreaterThanOrEqualExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 881
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 882
                        self.match(PParser.GTE)
                        self.state = 883 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 10:
                        localctx = PParser.EqualsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 884
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 885
                        self.match(PParser.EQ2)
                        self.state = 886 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 11:
                        localctx = PParser.NotEqualsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 887
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 888
                        self.match(PParser.XEQ)
                        self.state = 889 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 12:
                        localctx = PParser.RoughlyEqualsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 890
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 891
                        self.match(PParser.TEQ)
                        self.state = 892 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 13:
                        localctx = PParser.OrExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 893
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 894
                        self.match(PParser.OR)
                        self.state = 895 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 14:
                        localctx = PParser.AndExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 896
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 897
                        self.match(PParser.AND)
                        self.state = 898 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 15:
                        localctx = PParser.TernaryExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 899
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 900
                        self.match(PParser.IF)
                        self.state = 901 
                        localctx.test = self.expression(0)
                        self.state = 902
                        self.match(PParser.ELSE)
                        self.state = 903 
                        localctx.ifFalse = self.expression(14)
                        pass

                    elif la_ == 16:
                        localctx = PParser.InExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 905
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 906
                        self.match(PParser.IN)
                        self.state = 907 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 17:
                        localctx = PParser.ContainsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 908
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 909
                        self.match(PParser.CONTAINS)
                        self.state = 910 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 18:
                        localctx = PParser.ContainsAllExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 911
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 912
                        self.match(PParser.CONTAINS)
                        self.state = 913
                        self.match(PParser.ALL)
                        self.state = 914 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 19:
                        localctx = PParser.ContainsAnyExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 915
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 916
                        self.match(PParser.CONTAINS)
                        self.state = 917
                        self.match(PParser.ANY)
                        self.state = 918 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 20:
                        localctx = PParser.NotInExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 919
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 920
                        self.match(PParser.NOT)
                        self.state = 921
                        self.match(PParser.IN)
                        self.state = 922 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 21:
                        localctx = PParser.NotContainsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 923
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 924
                        self.match(PParser.NOT)
                        self.state = 925
                        self.match(PParser.CONTAINS)
                        self.state = 926 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 22:
                        localctx = PParser.NotContainsAllExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 927
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 928
                        self.match(PParser.NOT)
                        self.state = 929
                        self.match(PParser.CONTAINS)
                        self.state = 930
                        self.match(PParser.ALL)
                        self.state = 931 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 23:
                        localctx = PParser.NotContainsAnyExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 932
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 933
                        self.match(PParser.NOT)
                        self.state = 934
                        self.match(PParser.CONTAINS)
                        self.state = 935
                        self.match(PParser.ANY)
                        self.state = 936 
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 24:
                        localctx = PParser.IsNotExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 937
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 938
                        self.match(PParser.IS)
                        self.state = 939
                        self.match(PParser.NOT)
                        self.state = 940 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 25:
                        localctx = PParser.IsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 941
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 942
                        self.match(PParser.IS)
                        self.state = 943 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = PParser.CastExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 944
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 945
                        self.match(PParser.AS)
                        self.state = 946 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 951
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return PParser.RULE_closure_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = PParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 952 
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
            super(PParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(PParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Instance_expressionContext)
            super(PParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(PParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSelectableExpression(self)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Instance_expressionContext)
            super(PParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(PParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(PParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSelectorExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 955 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 961
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.SelectorExpressionContext(self, PParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 957
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 958 
                    localctx.selector = self.instance_selector() 
                self.state = 963
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_method_expression

     
        def copyFrom(self, ctx):
            super(PParser.Method_expressionContext, self).copyFrom(ctx)



    class MethodCallExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_expressionContext)
            super(PParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(PParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodCallExpression(self)


    class SortedExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_expressionContext)
            super(PParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(PParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSortedExpression(self)


    class ReadExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_expressionContext)
            super(PParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(PParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitReadExpression(self)


    class FetchExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_expressionContext)
            super(PParser.FetchExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_expressionContext
            self.copyFrom(ctx)

        def fetch_expression(self):
            return self.getTypedRuleContext(PParser.Fetch_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterFetchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitFetchExpression(self)


    class ConstructorExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_expressionContext)
            super(PParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(PParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitConstructorExpression(self)


    class DocumentExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_expressionContext)
            super(PParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(PParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDocumentExpression(self)



    def method_expression(self):

        localctx = PParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_expression)
        try:
            self.state = 970
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = PParser.DocumentExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 964 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 2:
                localctx = PParser.ConstructorExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 965 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 3:
                localctx = PParser.FetchExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 966 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 4:
                localctx = PParser.ReadExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 967 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 5:
                localctx = PParser.SortedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 968 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 6:
                localctx = PParser.MethodCallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 969 
                localctx.exp = self.method_call()
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
            super(PParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(PParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Instance_selectorContext)
            super(PParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(PParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Instance_selectorContext)
            super(PParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a PParser.Instance_selectorContext)
            super(PParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = PParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_instance_selector)
        try:
            self.state = 985
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = PParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 972
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 973
                self.match(PParser.DOT)
                self.state = 974 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = PParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 975
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 976
                self.match(PParser.LBRAK)
                self.state = 977 
                localctx.xslice = self.slice_arguments()
                self.state = 978
                self.match(PParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = PParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 980
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 981
                self.match(PParser.LBRAK)
                self.state = 982 
                localctx.exp = self.expression(0)
                self.state = 983
                self.match(PParser.RBRAK)
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
            super(PParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def document_type(self):
            return self.getTypedRuleContext(PParser.Document_typeContext,0)


        def getRuleIndex(self):
            return PParser.RULE_document_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = PParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 987 
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
            super(PParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def category_type(self):
            return self.getTypedRuleContext(PParser.Category_typeContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(PParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_constructor_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterConstructor_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitConstructor_expression(self)




    def constructor_expression(self):

        localctx = PParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 989 
            localctx.typ = self.category_type()
            self.state = 990
            self.match(PParser.LPAR)
            self.state = 992
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 991 
                localctx.args = self.argument_assignment_list(0)


            self.state = 994
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(PParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Argument_assignment_listContext)
            super(PParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Argument_assignment_listContext)
            super(PParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(PParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Argument_assignment_listContext)
            super(PParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(PParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(PParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1001
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                localctx = PParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 997 
                localctx.exp = self.expression(0)
                self.state = 998
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = PParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1000 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1008
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ArgumentAssignmentListItemContext(self, PParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1003
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1004
                    self.match(PParser.COMMA)
                    self.state = 1005 
                    localctx.item = self.argument_assignment() 
                self.state = 1010
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(PParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = PParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1011 
            localctx.name = self.variable_identifier()
            self.state = 1012 
            self.assign()
            self.state = 1013 
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
            super(PParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(PParser.READ, 0)

        def FROM(self):
            return self.getToken(PParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = PParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1015
            self.match(PParser.READ)
            self.state = 1016
            self.match(PParser.FROM)
            self.state = 1017 
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
            super(PParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(PParser.WRITE, 0)

        def TO(self):
            return self.getToken(PParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PParser.RULE_write_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = PParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1019
            self.match(PParser.WRITE)
            self.state = 1020 
            localctx.what = self.expression(0)
            self.state = 1021
            self.match(PParser.TO)
            self.state = 1022 
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
            super(PParser.Fetch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext

        def FETCH(self):
            return self.getToken(PParser.FETCH, 0)

        def FROM(self):
            return self.getToken(PParser.FROM, 0)

        def WHERE(self):
            return self.getToken(PParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PParser.RULE_fetch_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterFetch_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitFetch_expression(self)




    def fetch_expression(self):

        localctx = PParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_fetch_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1024
            self.match(PParser.FETCH)
            self.state = 1025 
            localctx.name = self.variable_identifier()
            self.state = 1026
            self.match(PParser.FROM)
            self.state = 1027 
            localctx.source = self.expression(0)
            self.state = 1028
            self.match(PParser.WHERE)
            self.state = 1029 
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
            super(PParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(PParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(PParser.Instance_expressionContext,i)


        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(PParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(PParser.EQ, 0)

        def getRuleIndex(self):
            return PParser.RULE_sorted_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = PParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1031
            self.match(PParser.SORTED)
            self.state = 1032
            self.match(PParser.LPAR)
            self.state = 1033 
            localctx.source = self.instance_expression(0)
            self.state = 1039
            _la = self._input.LA(1)
            if _la==PParser.COMMA:
                self.state = 1034
                self.match(PParser.COMMA)
                self.state = 1035 
                self.key_token()
                self.state = 1036
                self.match(PParser.EQ)
                self.state = 1037 
                localctx.key = self.instance_expression(0)


            self.state = 1041
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(PParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(PParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = PParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1043 
            localctx.inst = self.assignable_instance(0)
            self.state = 1044 
            self.assign()
            self.state = 1045 
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
            super(PParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(PParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a PParser.Child_instanceContext)
            super(PParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a PParser.Child_instanceContext)
            super(PParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = PParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_child_instance)
        try:
            self.state = 1055
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = PParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1047
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1048
                self.match(PParser.DOT)
                self.state = 1049 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = PParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1050
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1051
                self.match(PParser.LBRAK)
                self.state = 1052 
                localctx.exp = self.expression(0)
                self.state = 1053
                self.match(PParser.RBRAK)
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
            super(PParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(PParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(PParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = PParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1057 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1058 
            self.assign()
            self.state = 1059 
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
            super(PParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(PParser.LF)
            else:
                return self.getToken(PParser.LF, i)

        def getRuleIndex(self):
            return PParser.RULE_lfs

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = PParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1064
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1061
                    self.match(PParser.LF) 
                self.state = 1066
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(PParser.LF)
            else:
                return self.getToken(PParser.LF, i)

        def getRuleIndex(self):
            return PParser.RULE_lfp

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = PParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1068 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1067
                self.match(PParser.LF)
                self.state = 1070 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PParser.LF):
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
            super(PParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(PParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(PParser.LF)
            else:
                return self.getToken(PParser.LF, i)

        def getRuleIndex(self):
            return PParser.RULE_indent

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = PParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1073 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1072
                self.match(PParser.LF)
                self.state = 1075 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PParser.LF):
                    break

            self.state = 1077
            self.match(PParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(PParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(PParser.LF)
            else:
                return self.getToken(PParser.LF, i)

        def getRuleIndex(self):
            return PParser.RULE_dedent

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = PParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1082
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PParser.LF:
                self.state = 1079
                self.match(PParser.LF)
                self.state = 1084
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1085
            self.match(PParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(PParser.NONE, 0)

        def getRuleIndex(self):
            return PParser.RULE_null_literal

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = PParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1087
            self.match(PParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(PParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Declaration_listContext)
            super(PParser.FullDeclarationListContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(PParser.LfsContext,0)

        def EOF(self):
            return self.getToken(PParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(PParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = PParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = PParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1090
            _la = self._input.LA(1)
            if ((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (PParser.ABSTRACT - 62)) | (1 << (PParser.ATTR - 62)) | (1 << (PParser.CATEGORY - 62)) | (1 << (PParser.CLASS - 62)) | (1 << (PParser.DEF - 62)) | (1 << (PParser.ENUM - 62)) | (1 << (PParser.NATIVE - 62)) | (1 << (PParser.SINGLETON - 62)))) != 0):
                self.state = 1089 
                localctx.items = self.declarations(0)


            self.state = 1092 
            self.lfs()
            self.state = 1093
            self.match(PParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_declarations

     
        def copyFrom(self, ctx):
            super(PParser.DeclarationsContext, self).copyFrom(ctx)


    class DeclarationListContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationsContext)
            super(PParser.DeclarationListContext, self).__init__(parser)
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(PParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDeclarationList(self)


    class DeclarationListItemContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationsContext)
            super(PParser.DeclarationListItemContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def declarations(self):
            return self.getTypedRuleContext(PParser.DeclarationsContext,0)

        def declaration(self):
            return self.getTypedRuleContext(PParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDeclarationListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDeclarationListItem(self)



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1096 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.DeclarationListItemContext(self, PParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1098
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1099 
                    self.lfp()
                    self.state = 1100 
                    localctx.item = self.declaration() 
                self.state = 1106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_declaration

     
        def copyFrom(self, ctx):
            super(PParser.DeclarationContext, self).copyFrom(ctx)



    class CategoryDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationContext)
            super(PParser.CategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Category_declarationContext
            self.copyFrom(ctx)

        def category_declaration(self):
            return self.getTypedRuleContext(PParser.Category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategoryDeclaration(self)


    class ResourceDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationContext)
            super(PParser.ResourceDeclarationContext, self).__init__(parser)
            self.decl = None # Resource_declarationContext
            self.copyFrom(ctx)

        def resource_declaration(self):
            return self.getTypedRuleContext(PParser.Resource_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterResourceDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitResourceDeclaration(self)


    class AttributeDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationContext)
            super(PParser.AttributeDeclarationContext, self).__init__(parser)
            self.decl = None # Attribute_declarationContext
            self.copyFrom(ctx)

        def attribute_declaration(self):
            return self.getTypedRuleContext(PParser.Attribute_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAttributeDeclaration(self)


    class MethodDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationContext)
            super(PParser.MethodDeclarationContext, self).__init__(parser)
            self.decl = None # Method_declarationContext
            self.copyFrom(ctx)

        def method_declaration(self):
            return self.getTypedRuleContext(PParser.Method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodDeclaration(self)


    class EnumDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a PParser.DeclarationContext)
            super(PParser.EnumDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_declarationContext
            self.copyFrom(ctx)

        def enum_declaration(self):
            return self.getTypedRuleContext(PParser.Enum_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitEnumDeclaration(self)



    def declaration(self):

        localctx = PParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_declaration)
        try:
            self.state = 1112
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = PParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1107 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1108 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = PParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1109 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = PParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1110 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = PParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1111 
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
            super(PParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.decl = None # Native_resource_declarationContext

        def native_resource_declaration(self):
            return self.getTypedRuleContext(PParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return PParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = PParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1114 
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
            super(PParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_enum_declaration

     
        def copyFrom(self, ctx):
            super(PParser.Enum_declarationContext, self).copyFrom(ctx)



    class EnumNativeDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Enum_declarationContext)
            super(PParser.EnumNativeDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_native_declarationContext
            self.copyFrom(ctx)

        def enum_native_declaration(self):
            return self.getTypedRuleContext(PParser.Enum_native_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterEnumNativeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitEnumNativeDeclaration(self)


    class EnumCategoryDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Enum_declarationContext)
            super(PParser.EnumCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_category_declarationContext
            self.copyFrom(ctx)

        def enum_category_declaration(self):
            return self.getTypedRuleContext(PParser.Enum_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterEnumCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitEnumCategoryDeclaration(self)



    def enum_declaration(self):

        localctx = PParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_enum_declaration)
        try:
            self.state = 1118
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = PParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1116 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1117 
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
            super(PParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_native_symbol_list

     
        def copyFrom(self, ctx):
            super(PParser.Native_symbol_listContext, self).copyFrom(ctx)


    class NativeSymbolListContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_symbol_listContext)
            super(PParser.NativeSymbolListContext, self).__init__(parser)
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def native_symbol(self):
            return self.getTypedRuleContext(PParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeSymbolList(self)


    class NativeSymbolListItemContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_symbol_listContext)
            super(PParser.NativeSymbolListItemContext, self).__init__(parser)
            self.items = None # Native_symbol_listContext
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def native_symbol_list(self):
            return self.getTypedRuleContext(PParser.Native_symbol_listContext,0)

        def native_symbol(self):
            return self.getTypedRuleContext(PParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeSymbolListItem(self)



    def native_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Native_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1121 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.NativeSymbolListItemContext(self, PParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1123
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1124 
                    self.lfp()
                    self.state = 1125 
                    localctx.item = self.native_symbol() 
                self.state = 1131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_category_symbol_list

     
        def copyFrom(self, ctx):
            super(PParser.Category_symbol_listContext, self).copyFrom(ctx)


    class CategorySymbolListItemContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_symbol_listContext)
            super(PParser.CategorySymbolListItemContext, self).__init__(parser)
            self.items = None # Category_symbol_listContext
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def category_symbol_list(self):
            return self.getTypedRuleContext(PParser.Category_symbol_listContext,0)

        def category_symbol(self):
            return self.getTypedRuleContext(PParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategorySymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategorySymbolListItem(self)


    class CategorySymbolListContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_symbol_listContext)
            super(PParser.CategorySymbolListContext, self).__init__(parser)
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def category_symbol(self):
            return self.getTypedRuleContext(PParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategorySymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategorySymbolList(self)



    def category_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Category_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1133 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CategorySymbolListItemContext(self, PParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1135
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1136 
                    self.lfp()
                    self.state = 1137 
                    localctx.item = self.category_symbol() 
                self.state = 1143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_symbol_list

     
        def copyFrom(self, ctx):
            super(PParser.Symbol_listContext, self).copyFrom(ctx)


    class SymbolListContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Symbol_listContext)
            super(PParser.SymbolListContext, self).__init__(parser)
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSymbolList(self)


    class SymbolListItemContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Symbol_listContext)
            super(PParser.SymbolListItemContext, self).__init__(parser)
            self.items = None # Symbol_listContext
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(PParser.Symbol_listContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSymbolListItem(self)



    def symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1145 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.SymbolListItemContext(self, PParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1147
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1148
                    self.match(PParser.COMMA)
                    self.state = 1149 
                    localctx.item = self.symbol_identifier() 
                self.state = 1154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(PParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a PParser.Attribute_constraintContext)
            super(PParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(PParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMatchingExpression(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a PParser.Attribute_constraintContext)
            super(PParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(PParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(PParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a PParser.Attribute_constraintContext)
            super(PParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(PParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(PParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMatchingRange(self)


    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a PParser.Attribute_constraintContext)
            super(PParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(PParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(PParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a PParser.Attribute_constraintContext)
            super(PParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(PParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMatchingPattern(self)



    def attribute_constraint(self):

        localctx = PParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_attribute_constraint)
        try:
            self.state = 1165
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = PParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1155
                self.match(PParser.IN)
                self.state = 1156 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = PParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1157
                self.match(PParser.IN)
                self.state = 1158 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = PParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1159
                self.match(PParser.IN)
                self.state = 1160 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = PParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1161
                self.match(PParser.MATCHING)
                self.state = 1162
                localctx.text = self.match(PParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = PParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1163
                self.match(PParser.MATCHING)
                self.state = 1164 
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
            super(PParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)

        def expression_list(self):
            return self.getTypedRuleContext(PParser.Expression_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_list_literal

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = PParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1167
            self.match(PParser.LBRAK)
            self.state = 1169
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1168 
                localctx.items = self.expression_list(0)


            self.state = 1171
            self.match(PParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LT(self):
            return self.getToken(PParser.LT, 0)

        def GT(self):
            return self.getToken(PParser.GT, 0)

        def expression_list(self):
            return self.getTypedRuleContext(PParser.Expression_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_set_literal

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = PParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1173
            self.match(PParser.LT)
            self.state = 1175
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1174 
                localctx.items = self.expression_list(0)


            self.state = 1177
            self.match(PParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_expression_list

     
        def copyFrom(self, ctx):
            super(PParser.Expression_listContext, self).copyFrom(ctx)


    class ValueListItemContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Expression_listContext)
            super(PParser.ValueListItemContext, self).__init__(parser)
            self.items = None # Expression_listContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def expression_list(self):
            return self.getTypedRuleContext(PParser.Expression_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterValueListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitValueListItem(self)


    class ValueListContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Expression_listContext)
            super(PParser.ValueListContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitValueList(self)



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1180 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ValueListItemContext(self, PParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1182
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1183
                    self.match(PParser.COMMA)
                    self.state = 1184 
                    localctx.item = self.expression(0) 
                self.state = 1189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(PParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PParser.RULE_range_literal

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = PParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1190
            self.match(PParser.LBRAK)
            self.state = 1191 
            localctx.low = self.expression(0)
            self.state = 1192
            self.match(PParser.RANGE)
            self.state = 1193 
            localctx.high = self.expression(0)
            self.state = 1194
            self.match(PParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(PParser.TypedefContext, self).copyFrom(ctx)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a PParser.TypedefContext)
            super(PParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitListType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a PParser.TypedefContext)
            super(PParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(PParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPrimaryType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a PParser.TypedefContext)
            super(PParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(PParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(PParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDictType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a PParser.TypedefContext)
            super(PParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(PParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSetType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1197 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1207
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        localctx = PParser.SetTypeContext(self, PParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1199
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1200
                        self.match(PParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = PParser.ListTypeContext(self, PParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1201
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1202
                        self.match(PParser.LBRAK)
                        self.state = 1203
                        self.match(PParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = PParser.DictTypeContext(self, PParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1204
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1205
                        self.match(PParser.LCURL)
                        self.state = 1206
                        self.match(PParser.RCURL)
                        pass

             
                self.state = 1211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(PParser.Primary_typeContext, self).copyFrom(ctx)



    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Primary_typeContext)
            super(PParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(PParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategoryType(self)


    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Primary_typeContext)
            super(PParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(PParser.Native_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeType(self)



    def primary_type(self):

        localctx = PParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_primary_type)
        try:
            self.state = 1214
            token = self._input.LA(1)
            if token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.CODE]:
                localctx = PParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1212 
                localctx.n = self.native_type()

            elif token in [PParser.TYPE_IDENTIFIER]:
                localctx = PParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1213 
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
            super(PParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(PParser.Native_typeContext, self).copyFrom(ctx)



    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.DateTimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(PParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDateTimeType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.TimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(PParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTimeType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.TextTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(PParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTextType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.CodeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(PParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCodeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.IntegerTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(PParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIntegerType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.DecimalTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(PParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDecimalType(self)


    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.PeriodTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(PParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPeriodType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.DateTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(PParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDateType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.CharacterTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(PParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCharacterType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_typeContext)
            super(PParser.BooleanTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(PParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitBooleanType(self)



    def native_type(self):

        localctx = PParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_native_type)
        try:
            self.state = 1226
            token = self._input.LA(1)
            if token in [PParser.BOOLEAN]:
                localctx = PParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1216
                localctx.t1 = self.match(PParser.BOOLEAN)

            elif token in [PParser.CHARACTER]:
                localctx = PParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1217
                localctx.t1 = self.match(PParser.CHARACTER)

            elif token in [PParser.TEXT]:
                localctx = PParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1218
                localctx.t1 = self.match(PParser.TEXT)

            elif token in [PParser.INTEGER]:
                localctx = PParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1219
                localctx.t1 = self.match(PParser.INTEGER)

            elif token in [PParser.DECIMAL]:
                localctx = PParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1220
                localctx.t1 = self.match(PParser.DECIMAL)

            elif token in [PParser.DATE]:
                localctx = PParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1221
                localctx.t1 = self.match(PParser.DATE)

            elif token in [PParser.DATETIME]:
                localctx = PParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1222
                localctx.t1 = self.match(PParser.DATETIME)

            elif token in [PParser.TIME]:
                localctx = PParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1223
                localctx.t1 = self.match(PParser.TIME)

            elif token in [PParser.PERIOD]:
                localctx = PParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1224
                localctx.t1 = self.match(PParser.PERIOD)

            elif token in [PParser.CODE]:
                localctx = PParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1225
                localctx.t1 = self.match(PParser.CODE)

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
            super(PParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_category_type

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = PParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1228
            localctx.t1 = self.match(PParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(PParser.CODE, 0)

        def getRuleIndex(self):
            return PParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = PParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1230
            localctx.t1 = self.match(PParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Document_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def DOCUMENT(self):
            return self.getToken(PParser.DOCUMENT, 0)

        def getRuleIndex(self):
            return PParser.RULE_document_type

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDocument_type(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDocument_type(self)




    def document_type(self):

        localctx = PParser.Document_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1232
            localctx.t1 = self.match(PParser.DOCUMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(PParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_declarationContext)
            super(PParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(PParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_declarationContext)
            super(PParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(PParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_declarationContext)
            super(PParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(PParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = PParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_category_declaration)
        try:
            self.state = 1237
            token = self._input.LA(1)
            if token in [PParser.CATEGORY, PParser.CLASS]:
                localctx = PParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1234 
                localctx.decl = self.concrete_category_declaration()

            elif token in [PParser.NATIVE]:
                localctx = PParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1235 
                localctx.decl = self.native_category_declaration()

            elif token in [PParser.SINGLETON]:
                localctx = PParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1236 
                localctx.decl = self.singleton_category_declaration()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_type_identifier_list

     
        def copyFrom(self, ctx):
            super(PParser.Type_identifier_listContext, self).copyFrom(ctx)


    class TypeIdentifierListItemContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Type_identifier_listContext)
            super(PParser.TypeIdentifierListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(PParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTypeIdentifierListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTypeIdentifierListItem(self)


    class TypeIdentifierListContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Type_identifier_listContext)
            super(PParser.TypeIdentifierListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTypeIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTypeIdentifierList(self)



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 160
        self.enterRecursionRule(localctx, 160, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1240 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.TypeIdentifierListItemContext(self, PParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1242
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1243
                    self.match(PParser.COMMA)
                    self.state = 1244 
                    localctx.item = self.type_identifier() 
                self.state = 1249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_method_identifier

     
        def copyFrom(self, ctx):
            super(PParser.Method_identifierContext, self).copyFrom(ctx)



    class MethodVariableIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_identifierContext)
            super(PParser.MethodVariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodVariableIdentifier(self)


    class MethodTypeIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_identifierContext)
            super(PParser.MethodTypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMethodTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMethodTypeIdentifier(self)



    def method_identifier(self):

        localctx = PParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_method_identifier)
        try:
            self.state = 1252
            token = self._input.LA(1)
            if token in [PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1250 
                localctx.name = self.variable_identifier()

            elif token in [PParser.TYPE_IDENTIFIER]:
                localctx = PParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1251 
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
            super(PParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(PParser.IdentifierContext, self).copyFrom(ctx)



    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a PParser.IdentifierContext)
            super(PParser.SymbolIdentifierContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a PParser.IdentifierContext)
            super(PParser.VariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitVariableIdentifier(self)


    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a PParser.IdentifierContext)
            super(PParser.TypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(PParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTypeIdentifier(self)



    def identifier(self):

        localctx = PParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_identifier)
        try:
            self.state = 1257
            token = self._input.LA(1)
            if token in [PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1254 
                localctx.name = self.variable_identifier()

            elif token in [PParser.TYPE_IDENTIFIER]:
                localctx = PParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1255 
                localctx.name = self.type_identifier()

            elif token in [PParser.SYMBOL_IDENTIFIER]:
                localctx = PParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1256 
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
            super(PParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = PParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259
            self.match(PParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = PParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1261
            self.match(PParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(PParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = PParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1263
            self.match(PParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_argument_list

     
        def copyFrom(self, ctx):
            super(PParser.Argument_listContext, self).copyFrom(ctx)


    class ArgumentListItemContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Argument_listContext)
            super(PParser.ArgumentListItemContext, self).__init__(parser)
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def argument_list(self):
            return self.getTypedRuleContext(PParser.Argument_listContext,0)

        def argument(self):
            return self.getTypedRuleContext(PParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitArgumentListItem(self)


    class ArgumentListContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Argument_listContext)
            super(PParser.ArgumentListContext, self).__init__(parser)
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(PParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitArgumentList(self)



    def argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 172
        self.enterRecursionRule(localctx, 172, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1266 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ArgumentListItemContext(self, PParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1268
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1269
                    self.match(PParser.COMMA)
                    self.state = 1270 
                    localctx.item = self.argument() 
                self.state = 1275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(PParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a PParser.ArgumentContext)
            super(PParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(PParser.Operator_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a PParser.ArgumentContext)
            super(PParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(PParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = PParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_argument)
        try:
            self.state = 1278
            token = self._input.LA(1)
            if token in [PParser.CODE]:
                localctx = PParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1276 
                localctx.arg = self.code_argument()

            elif token in [PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1277 
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
            super(PParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_operator_argument

     
        def copyFrom(self, ctx):
            super(PParser.Operator_argumentContext, self).copyFrom(ctx)



    class NamedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a PParser.Operator_argumentContext)
            super(PParser.NamedArgumentContext, self).__init__(parser)
            self.arg = None # Named_argumentContext
            self.copyFrom(ctx)

        def named_argument(self):
            return self.getTypedRuleContext(PParser.Named_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNamedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNamedArgument(self)


    class TypedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a PParser.Operator_argumentContext)
            super(PParser.TypedArgumentContext, self).__init__(parser)
            self.arg = None # Typed_argumentContext
            self.copyFrom(ctx)

        def typed_argument(self):
            return self.getTypedRuleContext(PParser.Typed_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTypedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTypedArgument(self)



    def operator_argument(self):

        localctx = PParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_operator_argument)
        try:
            self.state = 1282
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                localctx = PParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1280 
                localctx.arg = self.named_argument()
                pass

            elif la_ == 2:
                localctx = PParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1281 
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
            super(PParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(PParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(PParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_named_argument

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = PParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1284 
            localctx.name = self.variable_identifier()
            self.state = 1287
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.state = 1285
                self.match(PParser.EQ)
                self.state = 1286 
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
            super(PParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(PParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return PParser.RULE_code_argument

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = PParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1289 
            self.code_type()
            self.state = 1290 
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
            super(PParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_category_or_any_type

     
        def copyFrom(self, ctx):
            super(PParser.Category_or_any_typeContext, self).copyFrom(ctx)



    class AnyArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_or_any_typeContext)
            super(PParser.AnyArgumentTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(PParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAnyArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAnyArgumentType(self)


    class CategoryArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_or_any_typeContext)
            super(PParser.CategoryArgumentTypeContext, self).__init__(parser)
            self.typ = None # TypedefContext
            self.copyFrom(ctx)

        def typedef(self):
            return self.getTypedRuleContext(PParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategoryArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategoryArgumentType(self)



    def category_or_any_type(self):

        localctx = PParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_category_or_any_type)
        try:
            self.state = 1294
            token = self._input.LA(1)
            if token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.CODE, PParser.TYPE_IDENTIFIER]:
                localctx = PParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1292 
                localctx.typ = self.typedef(0)

            elif token in [PParser.ANY]:
                localctx = PParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1293 
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
            super(PParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(PParser.Any_typeContext, self).copyFrom(ctx)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Any_typeContext)
            super(PParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(PParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAnyType(self)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Any_typeContext)
            super(PParser.AnyListTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def any_type(self):
            return self.getTypedRuleContext(PParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAnyListType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a PParser.Any_typeContext)
            super(PParser.AnyDictTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(PParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(PParser.RCURL, 0)
        def any_type(self):
            return self.getTypedRuleContext(PParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 184
        self.enterRecursionRule(localctx, 184, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1297
            self.match(PParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1305
                    la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                    if la_ == 1:
                        localctx = PParser.AnyListTypeContext(self, PParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1299
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1300
                        self.match(PParser.LBRAK)
                        self.state = 1301
                        self.match(PParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = PParser.AnyDictTypeContext(self, PParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1302
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1303
                        self.match(PParser.LCURL)
                        self.state = 1304
                        self.match(PParser.RCURL)
                        pass

             
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

    class Category_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Category_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_category_method_declaration_list

     
        def copyFrom(self, ctx):
            super(PParser.Category_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListContext(Category_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_method_declaration_listContext)
            super(PParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Category_method_declarationContext
            self.copyFrom(ctx)

        def category_method_declaration(self):
            return self.getTypedRuleContext(PParser.Category_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategoryMethodList(self)


    class CategoryMethodListItemContext(Category_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_method_declaration_listContext)
            super(PParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Category_method_declaration_listContext
            self.item = None # Category_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def category_method_declaration_list(self):
            return self.getTypedRuleContext(PParser.Category_method_declaration_listContext,0)

        def category_method_declaration(self):
            return self.getTypedRuleContext(PParser.Category_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCategoryMethodListItem(self)



    def category_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Category_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 186
        self.enterRecursionRule(localctx, 186, self.RULE_category_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1311 
            localctx.item = self.category_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CategoryMethodListItemContext(self, PParser.Category_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_method_declaration_list)
                    self.state = 1313
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1314 
                    self.lfp()
                    self.state = 1315 
                    localctx.item = self.category_method_declaration() 
                self.state = 1321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Category_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_category_method_declaration

     
        def copyFrom(self, ctx):
            super(PParser.Category_method_declarationContext, self).copyFrom(ctx)



    class GetterMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_method_declarationContext)
            super(PParser.GetterMethodContext, self).__init__(parser)
            self.decl = None # Getter_method_declarationContext
            self.copyFrom(ctx)

        def getter_method_declaration(self):
            return self.getTypedRuleContext(PParser.Getter_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterGetterMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitGetterMethod(self)


    class MemberMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_method_declarationContext)
            super(PParser.MemberMethodContext, self).__init__(parser)
            self.decl = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(PParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMemberMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMemberMethod(self)


    class SetterMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_method_declarationContext)
            super(PParser.SetterMethodContext, self).__init__(parser)
            self.decl = None # Setter_method_declarationContext
            self.copyFrom(ctx)

        def setter_method_declaration(self):
            return self.getTypedRuleContext(PParser.Setter_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSetterMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSetterMethod(self)


    class OperatorMethodContext(Category_method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Category_method_declarationContext)
            super(PParser.OperatorMethodContext, self).__init__(parser)
            self.decl = None # Operator_method_declarationContext
            self.copyFrom(ctx)

        def operator_method_declaration(self):
            return self.getTypedRuleContext(PParser.Operator_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorMethod(self)



    def category_method_declaration(self):

        localctx = PParser.Category_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_category_method_declaration)
        try:
            self.state = 1326
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = PParser.SetterMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1322 
                localctx.decl = self.setter_method_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.GetterMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1323 
                localctx.decl = self.getter_method_declaration()
                pass

            elif la_ == 3:
                localctx = PParser.MemberMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1324 
                localctx.decl = self.member_method_declaration()
                pass

            elif la_ == 4:
                localctx = PParser.OperatorMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1325 
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
            super(PParser.Native_category_mappingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_native_category_mapping

     
        def copyFrom(self, ctx):
            super(PParser.Native_category_mappingContext, self).copyFrom(ctx)



    class CSharpCategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mappingContext)
            super(PParser.CSharpCategoryMappingContext, self).__init__(parser)
            self.mapping = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(PParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpCategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpCategoryMapping(self)


    class JavaCategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mappingContext)
            super(PParser.JavaCategoryMappingContext, self).__init__(parser)
            self.mapping = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(PParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaCategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaCategoryMapping(self)


    class JavaScriptCategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mappingContext)
            super(PParser.JavaScriptCategoryMappingContext, self).__init__(parser)
            self.mapping = None # Javascript_category_mappingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(PParser.JAVASCRIPT, 0)
        def javascript_category_mapping(self):
            return self.getTypedRuleContext(PParser.Javascript_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaScriptCategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaScriptCategoryMapping(self)


    class Python3CategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mappingContext)
            super(PParser.Python3CategoryMappingContext, self).__init__(parser)
            self.mapping = None # Python_category_mappingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(PParser.PYTHON3, 0)
        def python_category_mapping(self):
            return self.getTypedRuleContext(PParser.Python_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython3CategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython3CategoryMapping(self)


    class Python2CategoryMappingContext(Native_category_mappingContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_category_mappingContext)
            super(PParser.Python2CategoryMappingContext, self).__init__(parser)
            self.mapping = None # Python_category_mappingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(PParser.PYTHON2, 0)
        def python_category_mapping(self):
            return self.getTypedRuleContext(PParser.Python_category_mappingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython2CategoryMapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython2CategoryMapping(self)



    def native_category_mapping(self):

        localctx = PParser.Native_category_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_native_category_mapping)
        try:
            self.state = 1338
            token = self._input.LA(1)
            if token in [PParser.JAVA]:
                localctx = PParser.JavaCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1328
                self.match(PParser.JAVA)
                self.state = 1329 
                localctx.mapping = self.java_class_identifier_expression(0)

            elif token in [PParser.CSHARP]:
                localctx = PParser.CSharpCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1330
                self.match(PParser.CSHARP)
                self.state = 1331 
                localctx.mapping = self.csharp_identifier_expression(0)

            elif token in [PParser.PYTHON2]:
                localctx = PParser.Python2CategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1332
                self.match(PParser.PYTHON2)
                self.state = 1333 
                localctx.mapping = self.python_category_mapping()

            elif token in [PParser.PYTHON3]:
                localctx = PParser.Python3CategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1334
                self.match(PParser.PYTHON3)
                self.state = 1335 
                localctx.mapping = self.python_category_mapping()

            elif token in [PParser.JAVASCRIPT]:
                localctx = PParser.JavaScriptCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1336
                self.match(PParser.JAVASCRIPT)
                self.state = 1337 
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
            super(PParser.Python_category_mappingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(PParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(PParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return PParser.RULE_python_category_mapping

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython_category_mapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython_category_mapping(self)




    def python_category_mapping(self):

        localctx = PParser.Python_category_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_python_category_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1340 
            localctx.id_ = self.identifier()
            self.state = 1342
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.state = 1341 
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
            super(PParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(PParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(PParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(PParser.DOT)
            else:
                return self.getToken(PParser.DOT, i)

        def getRuleIndex(self):
            return PParser.RULE_python_module

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = PParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1344
            self.match(PParser.FROM)
            self.state = 1345 
            self.module_token()
            self.state = 1346
            self.match(PParser.COLON)
            self.state = 1347 
            self.identifier()
            self.state = 1352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1348
                    self.match(PParser.DOT)
                    self.state = 1349 
                    self.identifier() 
                self.state = 1354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = PParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1355
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1356
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
            super(PParser.Javascript_category_mappingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(PParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(PParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return PParser.RULE_javascript_category_mapping

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_category_mapping(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_category_mapping(self)




    def javascript_category_mapping(self):

        localctx = PParser.Javascript_category_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_javascript_category_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1358 
            localctx.id_ = self.identifier()
            self.state = 1360
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 1359 
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
            super(PParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(PParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(PParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PParser.IdentifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(PParser.SLASH)
            else:
                return self.getToken(PParser.SLASH, i)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)

        def getRuleIndex(self):
            return PParser.RULE_javascript_module

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = PParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1362
            self.match(PParser.FROM)
            self.state = 1363 
            self.module_token()
            self.state = 1364
            self.match(PParser.COLON)
            self.state = 1366
            _la = self._input.LA(1)
            if _la==PParser.SLASH:
                self.state = 1365
                self.match(PParser.SLASH)


            self.state = 1368 
            self.identifier()
            self.state = 1373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1369
                    self.match(PParser.SLASH)
                    self.state = 1370 
                    self.identifier() 
                self.state = 1375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

            self.state = 1378
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.state = 1376
                self.match(PParser.DOT)
                self.state = 1377 
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
            super(PParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_variable_identifier_list

     
        def copyFrom(self, ctx):
            super(PParser.Variable_identifier_listContext, self).copyFrom(ctx)


    class VariableListContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Variable_identifier_listContext)
            super(PParser.VariableListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterVariableList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitVariableList(self)


    class VariableListItemContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Variable_identifier_listContext)
            super(PParser.VariableListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(PParser.Variable_identifier_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterVariableListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitVariableListItem(self)



    def variable_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Variable_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 202
        self.enterRecursionRule(localctx, 202, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1381 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.VariableListItemContext(self, PParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1383
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1384
                    self.match(PParser.COMMA)
                    self.state = 1385 
                    localctx.item = self.variable_identifier() 
                self.state = 1390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_method_declaration

     
        def copyFrom(self, ctx):
            super(PParser.Method_declarationContext, self).copyFrom(ctx)



    class ConcreteMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_declarationContext)
            super(PParser.ConcreteMethodContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(PParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterConcreteMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitConcreteMethod(self)


    class AbstractMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_declarationContext)
            super(PParser.AbstractMethodContext, self).__init__(parser)
            self.decl = None # Abstract_method_declarationContext
            self.copyFrom(ctx)

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(PParser.Abstract_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAbstractMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAbstractMethod(self)


    class NativeMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_declarationContext)
            super(PParser.NativeMethodContext, self).__init__(parser)
            self.decl = None # Native_method_declarationContext
            self.copyFrom(ctx)

        def native_method_declaration(self):
            return self.getTypedRuleContext(PParser.Native_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeMethod(self)



    def method_declaration(self):

        localctx = PParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_method_declaration)
        try:
            self.state = 1394
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                localctx = PParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1391 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1392 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = PParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1393 
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
            super(PParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_native_statement_list

     
        def copyFrom(self, ctx):
            super(PParser.Native_statement_listContext, self).copyFrom(ctx)


    class NativeStatementListContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statement_listContext)
            super(PParser.NativeStatementListContext, self).__init__(parser)
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def native_statement(self):
            return self.getTypedRuleContext(PParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeStatementList(self)


    class NativeStatementListItemContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statement_listContext)
            super(PParser.NativeStatementListItemContext, self).__init__(parser)
            self.items = None # Native_statement_listContext
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def native_statement_list(self):
            return self.getTypedRuleContext(PParser.Native_statement_listContext,0)

        def native_statement(self):
            return self.getTypedRuleContext(PParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNativeStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNativeStatementListItem(self)



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 206
        self.enterRecursionRule(localctx, 206, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1397 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.NativeStatementListItemContext(self, PParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1399
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1400 
                    self.lfp()
                    self.state = 1401 
                    localctx.item = self.native_statement() 
                self.state = 1407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(PParser.Native_statementContext, self).copyFrom(ctx)



    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statementContext)
            super(PParser.Python2NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(PParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(PParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython2NativeStatement(self)


    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statementContext)
            super(PParser.CSharpNativeStatementContext, self).__init__(parser)
            self.stmt = None # Csharp_statementContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(PParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(PParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statementContext)
            super(PParser.JavaNativeStatementContext, self).__init__(parser)
            self.stmt = None # Java_statementContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(PParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(PParser.Java_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statementContext)
            super(PParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.stmt = None # Javascript_native_statementContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(PParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(PParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaScriptNativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Native_statementContext)
            super(PParser.Python3NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(PParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(PParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = PParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_statement)
        try:
            self.state = 1418
            token = self._input.LA(1)
            if token in [PParser.JAVA]:
                localctx = PParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1408
                self.match(PParser.JAVA)
                self.state = 1409 
                localctx.stmt = self.java_statement()

            elif token in [PParser.CSHARP]:
                localctx = PParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1410
                self.match(PParser.CSHARP)
                self.state = 1411 
                localctx.stmt = self.csharp_statement()

            elif token in [PParser.PYTHON2]:
                localctx = PParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1412
                self.match(PParser.PYTHON2)
                self.state = 1413 
                localctx.stmt = self.python_native_statement()

            elif token in [PParser.PYTHON3]:
                localctx = PParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1414
                self.match(PParser.PYTHON3)
                self.state = 1415 
                localctx.stmt = self.python_native_statement()

            elif token in [PParser.JAVASCRIPT]:
                localctx = PParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1416
                self.match(PParser.JAVASCRIPT)
                self.state = 1417 
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
            super(PParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Python_statementContext
            self.module = None # Python_moduleContext

        def python_statement(self):
            return self.getTypedRuleContext(PParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(PParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return PParser.RULE_python_native_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = PParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1420 
            localctx.stmt = self.python_statement()
            self.state = 1422
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.state = 1421
                self.match(PParser.SEMI)


            self.state = 1425
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 1424 
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
            super(PParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Javascript_statementContext
            self.module = None # Javascript_moduleContext

        def javascript_statement(self):
            return self.getTypedRuleContext(PParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(PParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return PParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = PParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1427 
            localctx.stmt = self.javascript_statement()
            self.state = 1429
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 1428
                self.match(PParser.SEMI)


            self.state = 1432
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.state = 1431 
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
            super(PParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_statement_list

     
        def copyFrom(self, ctx):
            super(PParser.Statement_listContext, self).copyFrom(ctx)


    class StatementListItemContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Statement_listContext)
            super(PParser.StatementListItemContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)

        def statement(self):
            return self.getTypedRuleContext(PParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitStatementListItem(self)


    class StatementListContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Statement_listContext)
            super(PParser.StatementListContext, self).__init__(parser)
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(PParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitStatementList(self)



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 214
        self.enterRecursionRule(localctx, 214, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1435 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,95,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.StatementListItemContext(self, PParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1437
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1438 
                    self.lfp()
                    self.state = 1439 
                    localctx.item = self.statement() 
                self.state = 1445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,95,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_switch_case_statement_list

     
        def copyFrom(self, ctx):
            super(PParser.Switch_case_statement_listContext, self).copyFrom(ctx)


    class SwitchCaseStatementListItemContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Switch_case_statement_listContext)
            super(PParser.SwitchCaseStatementListItemContext, self).__init__(parser)
            self.items = None # Switch_case_statement_listContext
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def switch_case_statement_list(self):
            return self.getTypedRuleContext(PParser.Switch_case_statement_listContext,0)

        def switch_case_statement(self):
            return self.getTypedRuleContext(PParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSwitchCaseStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSwitchCaseStatementListItem(self)


    class SwitchCaseStatementListContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Switch_case_statement_listContext)
            super(PParser.SwitchCaseStatementListContext, self).__init__(parser)
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def switch_case_statement(self):
            return self.getTypedRuleContext(PParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSwitchCaseStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSwitchCaseStatementList(self)



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 216
        self.enterRecursionRule(localctx, 216, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1447 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.SwitchCaseStatementListItemContext(self, PParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1449
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1450 
                    self.lfp()
                    self.state = 1451 
                    localctx.item = self.switch_case_statement() 
                self.state = 1457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_catch_statement_list

     
        def copyFrom(self, ctx):
            super(PParser.Catch_statement_listContext, self).copyFrom(ctx)


    class CatchStatementListContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Catch_statement_listContext)
            super(PParser.CatchStatementListContext, self).__init__(parser)
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def catch_statement(self):
            return self.getTypedRuleContext(PParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCatchStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCatchStatementList(self)


    class CatchStatementListItemContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Catch_statement_listContext)
            super(PParser.CatchStatementListItemContext, self).__init__(parser)
            self.items = None # Catch_statement_listContext
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(PParser.Catch_statement_listContext,0)

        def catch_statement(self):
            return self.getTypedRuleContext(PParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCatchStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCatchStatementListItem(self)



    def catch_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Catch_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 218
        self.enterRecursionRule(localctx, 218, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1459 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1467
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CatchStatementListItemContext(self, PParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1461
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1462 
                    self.lfp()
                    self.state = 1463 
                    localctx.item = self.catch_statement() 
                self.state = 1469
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(PParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_collectionContext)
            super(PParser.LiteralSetLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(PParser.LT, 0)
        def GT(self):
            return self.getToken(PParser.GT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(PParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLiteralSetLiteral(self)


    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_collectionContext)
            super(PParser.LiteralListLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(PParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_collectionContext)
            super(PParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(PParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(PParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLiteralRangeLiteral(self)



    def literal_collection(self):

        localctx = PParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_literal_collection)
        try:
            self.state = 1484
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                localctx = PParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1470
                self.match(PParser.LBRAK)
                self.state = 1471 
                localctx.low = self.atomic_literal()
                self.state = 1472
                self.match(PParser.RANGE)
                self.state = 1473 
                localctx.high = self.atomic_literal()
                self.state = 1474
                self.match(PParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = PParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1476
                self.match(PParser.LBRAK)
                self.state = 1477 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1478
                self.match(PParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = PParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1480
                self.match(PParser.LT)
                self.state = 1481 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1482
                self.match(PParser.GT)
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
            super(PParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(PParser.Atomic_literalContext, self).copyFrom(ctx)



    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(PParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPeriodLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(PParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitNullLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTextLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(PParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitHexadecimalLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(PParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCharacterLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(PParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDateLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(PParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTimeLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(PParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(PParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIntegerLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(PParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDecimalLiteral(self)


    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(PParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(PParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDateTimeLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Atomic_literalContext)
            super(PParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(PParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitBooleanLiteral(self)



    def atomic_literal(self):

        localctx = PParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_atomic_literal)
        try:
            self.state = 1499
            token = self._input.LA(1)
            if token in [PParser.MIN_INTEGER]:
                localctx = PParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1486
                localctx.t = self.match(PParser.MIN_INTEGER)

            elif token in [PParser.MAX_INTEGER]:
                localctx = PParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1487
                localctx.t = self.match(PParser.MAX_INTEGER)

            elif token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1488
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.HEXA_LITERAL]:
                localctx = PParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1489
                localctx.t = self.match(PParser.HEXA_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1490
                localctx.t = self.match(PParser.CHAR_LITERAL)

            elif token in [PParser.DATE_LITERAL]:
                localctx = PParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1491
                localctx.t = self.match(PParser.DATE_LITERAL)

            elif token in [PParser.TIME_LITERAL]:
                localctx = PParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1492
                localctx.t = self.match(PParser.TIME_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1493
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1494
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.DATETIME_LITERAL]:
                localctx = PParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1495
                localctx.t = self.match(PParser.DATETIME_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1496
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.PERIOD_LITERAL]:
                localctx = PParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1497
                localctx.t = self.match(PParser.PERIOD_LITERAL)

            elif token in [PParser.NONE]:
                localctx = PParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1498 
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
            super(PParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_literal_list_literal

     
        def copyFrom(self, ctx):
            super(PParser.Literal_list_literalContext, self).copyFrom(ctx)


    class LiteralListContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_list_literalContext)
            super(PParser.LiteralListContext, self).__init__(parser)
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(PParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLiteralList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLiteralList(self)


    class LiteralListItemContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_list_literalContext)
            super(PParser.LiteralListItemContext, self).__init__(parser)
            self.items = None # Literal_list_literalContext
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(PParser.Literal_list_literalContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(PParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLiteralListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLiteralListItem(self)



    def literal_list_literal(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Literal_list_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1502 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1509
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.LiteralListItemContext(self, PParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1504
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1505
                    self.match(PParser.COMMA)
                    self.state = 1506 
                    localctx.item = self.atomic_literal() 
                self.state = 1511
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(PParser.Selectable_expressionContext, self).copyFrom(ctx)



    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Selectable_expressionContext)
            super(PParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(PParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIdentifierExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Selectable_expressionContext)
            super(PParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(PParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Selectable_expressionContext)
            super(PParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(PParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitLiteralExpression(self)


    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Selectable_expressionContext)
            super(PParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(PParser.This_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitThisExpression(self)



    def selectable_expression(self):

        localctx = PParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_selectable_expression)
        try:
            self.state = 1516
            la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
            if la_ == 1:
                localctx = PParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1512 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = PParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1513 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = PParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1514 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = PParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1515 
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
            super(PParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(PParser.SELF, 0)

        def THIS(self):
            return self.getToken(PParser.THIS, 0)

        def getRuleIndex(self):
            return PParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = PParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1518
            _la = self._input.LA(1)
            if not(_la==PParser.SELF or _la==PParser.THIS):
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
            super(PParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = PParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1520
            self.match(PParser.LPAR)
            self.state = 1521 
            localctx.exp = self.expression(0)
            self.state = 1522
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_literal_expression

     
        def copyFrom(self, ctx):
            super(PParser.Literal_expressionContext, self).copyFrom(ctx)



    class CollectionLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_expressionContext)
            super(PParser.CollectionLiteralContext, self).__init__(parser)
            self.exp = None # Collection_literalContext
            self.copyFrom(ctx)

        def collection_literal(self):
            return self.getTypedRuleContext(PParser.Collection_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCollectionLiteral(self)


    class AtomicLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Literal_expressionContext)
            super(PParser.AtomicLiteralContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(PParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAtomicLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAtomicLiteral(self)



    def literal_expression(self):

        localctx = PParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_literal_expression)
        try:
            self.state = 1526
            token = self._input.LA(1)
            if token in [PParser.NONE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.MIN_INTEGER, PParser.MAX_INTEGER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.HEXA_LITERAL, PParser.DECIMAL_LITERAL, PParser.DATETIME_LITERAL, PParser.TIME_LITERAL, PParser.DATE_LITERAL, PParser.PERIOD_LITERAL]:
                localctx = PParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1524 
                localctx.exp = self.atomic_literal()

            elif token in [PParser.LPAR, PParser.LBRAK, PParser.LCURL, PParser.LT]:
                localctx = PParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1525 
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
            super(PParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_collection_literal

     
        def copyFrom(self, ctx):
            super(PParser.Collection_literalContext, self).copyFrom(ctx)



    class TupleLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Collection_literalContext)
            super(PParser.TupleLiteralContext, self).__init__(parser)
            self.exp = None # Tuple_literalContext
            self.copyFrom(ctx)

        def tuple_literal(self):
            return self.getTypedRuleContext(PParser.Tuple_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTupleLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTupleLiteral(self)


    class ListLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Collection_literalContext)
            super(PParser.ListLiteralContext, self).__init__(parser)
            self.exp = None # List_literalContext
            self.copyFrom(ctx)

        def list_literal(self):
            return self.getTypedRuleContext(PParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitListLiteral(self)


    class DictLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Collection_literalContext)
            super(PParser.DictLiteralContext, self).__init__(parser)
            self.exp = None # Dict_literalContext
            self.copyFrom(ctx)

        def dict_literal(self):
            return self.getTypedRuleContext(PParser.Dict_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDictLiteral(self)


    class RangeLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Collection_literalContext)
            super(PParser.RangeLiteralContext, self).__init__(parser)
            self.exp = None # Range_literalContext
            self.copyFrom(ctx)

        def range_literal(self):
            return self.getTypedRuleContext(PParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRangeLiteral(self)


    class SetLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a PParser.Collection_literalContext)
            super(PParser.SetLiteralContext, self).__init__(parser)
            self.exp = None # Set_literalContext
            self.copyFrom(ctx)

        def set_literal(self):
            return self.getTypedRuleContext(PParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSetLiteral(self)



    def collection_literal(self):

        localctx = PParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_collection_literal)
        try:
            self.state = 1533
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                localctx = PParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1528 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = PParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1529 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = PParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1530 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = PParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1531 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = PParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1532 
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
            super(PParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_tupleContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(PParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return PParser.RULE_tuple_literal

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = PParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1535
            self.match(PParser.LPAR)
            self.state = 1537
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1536 
                localctx.items = self.expression_tuple(0)


            self.state = 1539
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Dict_entry_listContext

        def LCURL(self):
            return self.getToken(PParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(PParser.RCURL, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(PParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_dict_literal

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = PParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1541
            self.match(PParser.LCURL)
            self.state = 1543
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1542 
                localctx.items = self.dict_entry_list(0)


            self.state = 1545
            self.match(PParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_expression_tuple

     
        def copyFrom(self, ctx):
            super(PParser.Expression_tupleContext, self).copyFrom(ctx)


    class ValueTupleItemContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a PParser.Expression_tupleContext)
            super(PParser.ValueTupleItemContext, self).__init__(parser)
            self.items = None # Expression_tupleContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def expression_tuple(self):
            return self.getTypedRuleContext(PParser.Expression_tupleContext,0)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterValueTupleItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitValueTupleItem(self)


    class ValueTupleContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a PParser.Expression_tupleContext)
            super(PParser.ValueTupleContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterValueTuple(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitValueTuple(self)



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 240
        self.enterRecursionRule(localctx, 240, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1548 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ValueTupleItemContext(self, PParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1550
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1551
                    self.match(PParser.COMMA)
                    self.state = 1552 
                    localctx.item = self.expression(0) 
                self.state = 1557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_dict_entry_list

     
        def copyFrom(self, ctx):
            super(PParser.Dict_entry_listContext, self).copyFrom(ctx)


    class DictEntryListContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Dict_entry_listContext)
            super(PParser.DictEntryListContext, self).__init__(parser)
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def dict_entry(self):
            return self.getTypedRuleContext(PParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDictEntryList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDictEntryList(self)


    class DictEntryListItemContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Dict_entry_listContext)
            super(PParser.DictEntryListItemContext, self).__init__(parser)
            self.items = None # Dict_entry_listContext
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def dict_entry_list(self):
            return self.getTypedRuleContext(PParser.Dict_entry_listContext,0)

        def dict_entry(self):
            return self.getTypedRuleContext(PParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDictEntryListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDictEntryListItem(self)



    def dict_entry_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Dict_entry_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 242
        self.enterRecursionRule(localctx, 242, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1559 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.DictEntryListItemContext(self, PParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1561
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1562
                    self.match(PParser.COMMA)
                    self.state = 1563 
                    localctx.item = self.dict_entry() 
                self.state = 1568
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,107,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(PParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PParser.RULE_dict_entry

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = PParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569 
            localctx.key = self.expression(0)
            self.state = 1570
            self.match(PParser.COLON)
            self.state = 1571 
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
            super(PParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(PParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Slice_argumentsContext)
            super(PParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSliceFirstAndLast(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Slice_argumentsContext)
            super(PParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSliceFirstOnly(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Slice_argumentsContext)
            super(PParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(PParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSliceLastOnly(self)



    def slice_arguments(self):

        localctx = PParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_slice_arguments)
        try:
            self.state = 1582
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                localctx = PParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1573 
                localctx.first = self.expression(0)
                self.state = 1574
                self.match(PParser.COLON)
                self.state = 1575 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = PParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1577 
                localctx.first = self.expression(0)
                self.state = 1578
                self.match(PParser.COLON)
                pass

            elif la_ == 3:
                localctx = PParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1580
                self.match(PParser.COLON)
                self.state = 1581 
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
            super(PParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(PParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = PParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1584 
            localctx.name = self.variable_identifier()
            self.state = 1585 
            self.assign()
            self.state = 1586 
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
            super(PParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(PParser.Assignable_instanceContext, self).copyFrom(ctx)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a PParser.Assignable_instanceContext)
            super(PParser.RootInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(PParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitRootInstance(self)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a PParser.Assignable_instanceContext)
            super(PParser.ChildInstanceContext, self).__init__(parser)
            self.parent = None # Assignable_instanceContext
            self.child = None # Child_instanceContext
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(PParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(PParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitChildInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 250
        self.enterRecursionRule(localctx, 250, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1589 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1595
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,109,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ChildInstanceContext(self, PParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1591
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1592 
                    localctx.child = self.child_instance() 
                self.state = 1597
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(PParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Is_expressionContext)
            super(PParser.IsATypeExpressionContext, self).__init__(parser)
            self.typ = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(PParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Is_expressionContext)
            super(PParser.IsOtherExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = PParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_is_expression)
        try:
            self.state = 1602
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = PParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1598
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1599
                self.match(PParser.VARIABLE_IDENTIFIER)
                self.state = 1600 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = PParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1601 
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
            super(PParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(PParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a PParser.OperatorContext)
            super(PParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(PParser.PLUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a PParser.OperatorContext)
            super(PParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(PParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorModulo(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a PParser.OperatorContext)
            super(PParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(PParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a PParser.OperatorContext)
            super(PParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(PParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a PParser.OperatorContext)
            super(PParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(PParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a PParser.OperatorContext)
            super(PParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(PParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitOperatorMinus(self)



    def operator(self):

        localctx = PParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_operator)
        try:
            self.state = 1610
            token = self._input.LA(1)
            if token in [PParser.PLUS]:
                localctx = PParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1604
                self.match(PParser.PLUS)

            elif token in [PParser.MINUS]:
                localctx = PParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1605
                self.match(PParser.MINUS)

            elif token in [PParser.STAR]:
                localctx = PParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1606 
                self.multiply()

            elif token in [PParser.SLASH]:
                localctx = PParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1607 
                self.divide()

            elif token in [PParser.BSLASH]:
                localctx = PParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1608 
                self.idivide()

            elif token in [PParser.PERCENT, PParser.MODULO]:
                localctx = PParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1609 
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
            super(PParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = PParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1612
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1613
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
            super(PParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = PParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1615
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1616
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
            super(PParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return PParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = PParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1618
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1619
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
            super(PParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(PParser.EQ, 0)

        def getRuleIndex(self):
            return PParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = PParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1621
            self.match(PParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(PParser.STAR, 0)

        def getRuleIndex(self):
            return PParser.RULE_multiply

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = PParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1623
            self.match(PParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(PParser.SLASH, 0)

        def getRuleIndex(self):
            return PParser.RULE_divide

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = PParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1625
            self.match(PParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(PParser.BSLASH, 0)

        def getRuleIndex(self):
            return PParser.RULE_idivide

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = PParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1627
            self.match(PParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(PParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(PParser.MODULO, 0)

        def getRuleIndex(self):
            return PParser.RULE_modulo

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = PParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1629
            _la = self._input.LA(1)
            if not(_la==PParser.PERCENT or _la==PParser.MODULO):
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
            super(PParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_statementContext)
            super(PParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(PParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptReturnStatement(self)


    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_statementContext)
            super(PParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptStatement(self)



    def javascript_statement(self):

        localctx = PParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_javascript_statement)
        try:
            self.state = 1638
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1631
                self.match(PParser.RETURN)
                self.state = 1632 
                localctx.exp = self.javascript_expression(0)
                self.state = 1633
                self.match(PParser.SEMI)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.WRITE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1635 
                localctx.exp = self.javascript_expression(0)
                self.state = 1636
                self.match(PParser.SEMI)

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
            super(PParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_expressionContext)
            super(PParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptPrimaryExpression(self)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_expressionContext)
            super(PParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptSelectorExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 274
        self.enterRecursionRule(localctx, 274, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1641 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1647
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,113,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavascriptSelectorExpressionContext(self, PParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1643
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1644 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1649
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,113,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_primary_expression

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_primary_expressionContext, self).copyFrom(ctx)



    class JavascriptParenthesisExpressionContext(Javascript_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_primary_expressionContext)
            super(PParser.JavascriptParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_parenthesis_expressionContext
            self.copyFrom(ctx)

        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptParenthesisExpression(self)


    class JavascriptLiteralExpressionContext(Javascript_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_primary_expressionContext)
            super(PParser.JavascriptLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_literal_expressionContext
            self.copyFrom(ctx)

        def javascript_literal_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptLiteralExpression(self)


    class JavascriptIdentifierExpressionContext(Javascript_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_primary_expressionContext)
            super(PParser.JavascriptIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_identifier_expressionContext
            self.copyFrom(ctx)

        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptIdentifierExpression(self)



    def javascript_primary_expression(self):

        localctx = PParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_javascript_primary_expression)
        try:
            self.state = 1653
            token = self._input.LA(1)
            if token in [PParser.LPAR]:
                localctx = PParser.JavascriptParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1650 
                localctx.exp = self.javascript_parenthesis_expression()

            elif token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.WRITE, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.JavascriptIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1651 
                localctx.exp = self.javascript_identifier_expression(0)

            elif token in [PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavascriptLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1652 
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
            super(PParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavascriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_selector_expressionContext)
            super(PParser.JavascriptMethodExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptMethodExpression(self)


    class JavascriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_selector_expressionContext)
            super(PParser.JavascriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptItemExpression(self)



    def javascript_selector_expression(self):

        localctx = PParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_javascript_selector_expression)
        try:
            self.state = 1658
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.JavascriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1655
                self.match(PParser.DOT)
                self.state = 1656 
                localctx.exp = self.javascript_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.JavascriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1657 
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
            super(PParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(PParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(PParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return PParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = PParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1660 
            localctx.name = self.javascript_identifier()
            self.state = 1661
            self.match(PParser.LPAR)
            self.state = 1663
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (PParser.READ - 115)) | (1 << (PParser.WRITE - 115)) | (1 << (PParser.BOOLEAN_LITERAL - 115)) | (1 << (PParser.CHAR_LITERAL - 115)) | (1 << (PParser.SYMBOL_IDENTIFIER - 115)) | (1 << (PParser.TYPE_IDENTIFIER - 115)) | (1 << (PParser.VARIABLE_IDENTIFIER - 115)) | (1 << (PParser.TEXT_LITERAL - 115)) | (1 << (PParser.INTEGER_LITERAL - 115)) | (1 << (PParser.DECIMAL_LITERAL - 115)))) != 0):
                self.state = 1662 
                localctx.args = self.javascript_arguments(0)


            self.state = 1665
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_argumentsContext)
            super(PParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(PParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptArgumentListItem(self)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_argumentsContext)
            super(PParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptArgumentList(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 282
        self.enterRecursionRule(localctx, 282, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1668 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1675
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavascriptArgumentListItemContext(self, PParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1670
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1671
                    self.match(PParser.COMMA)
                    self.state = 1672 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1677
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = PParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1678
            self.match(PParser.LBRAK)
            self.state = 1679 
            localctx.exp = self.javascript_expression(0)
            self.state = 1680
            self.match(PParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = PParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1682
            self.match(PParser.LPAR)
            self.state = 1683 
            localctx.exp = self.javascript_expression(0)
            self.state = 1684
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_identifier_expression

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_identifier_expressionContext, self).copyFrom(ctx)


    class JavascriptIdentifierContext(Javascript_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_identifier_expressionContext)
            super(PParser.JavascriptIdentifierContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def javascript_identifier(self):
            return self.getTypedRuleContext(PParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptIdentifier(self)


    class JavascriptChildIdentifierContext(Javascript_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_identifier_expressionContext)
            super(PParser.JavascriptChildIdentifierContext, self).__init__(parser)
            self.parent = None # Javascript_identifier_expressionContext
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Javascript_identifier_expressionContext,0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(PParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptChildIdentifier(self)



    def javascript_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Javascript_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 288
        self.enterRecursionRule(localctx, 288, self.RULE_javascript_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavascriptIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1687 
            localctx.name = self.javascript_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1694
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavascriptChildIdentifierContext(self, PParser.Javascript_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_identifier_expression)
                    self.state = 1689
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1690
                    self.match(PParser.DOT)
                    self.state = 1691 
                    localctx.name = self.javascript_identifier() 
                self.state = 1696
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(PParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_literal_expressionContext)
            super(PParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(PParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptDecimalLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_literal_expressionContext)
            super(PParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(PParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_literal_expressionContext)
            super(PParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(PParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_literal_expressionContext)
            super(PParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(PParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Javascript_literal_expressionContext)
            super(PParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascriptTextLiteral(self)



    def javascript_literal_expression(self):

        localctx = PParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_javascript_literal_expression)
        try:
            self.state = 1702
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1697
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1698
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1699
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1700
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1701
                localctx.t = self.match(PParser.CHAR_LITERAL)

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
            super(PParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(PParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(PParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(PParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(PParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(PParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(PParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(PParser.DATE, 0)

        def TIME(self):
            return self.getToken(PParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(PParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(PParser.PERIOD, 0)

        def READ(self):
            return self.getToken(PParser.READ, 0)

        def WRITE(self):
            return self.getToken(PParser.WRITE, 0)

        def getRuleIndex(self):
            return PParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = PParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1704
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (PParser.READ - 115)) | (1 << (PParser.WRITE - 115)) | (1 << (PParser.SYMBOL_IDENTIFIER - 115)) | (1 << (PParser.TYPE_IDENTIFIER - 115)) | (1 << (PParser.VARIABLE_IDENTIFIER - 115)))) != 0)):
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
            super(PParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(PParser.Python_statementContext, self).copyFrom(ctx)



    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_statementContext)
            super(PParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(PParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonReturnStatement(self)


    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_statementContext)
            super(PParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonStatement(self)



    def python_statement(self):

        localctx = PParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_python_statement)
        try:
            self.state = 1709
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1706
                self.match(PParser.RETURN)
                self.state = 1707 
                localctx.exp = self.python_expression(0)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1708 
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
            super(PParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(PParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_expressionContext)
            super(PParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(PParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonPrimaryExpression(self)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_expressionContext)
            super(PParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(PParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonSelectorExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 296
        self.enterRecursionRule(localctx, 296, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1712 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1718
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonSelectorExpressionContext(self, PParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1714
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1715 
                    localctx.child = self.python_selector_expression() 
                self.state = 1720
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(PParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_primary_expressionContext)
            super(PParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_primary_expressionContext)
            super(PParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(PParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonGlobalMethodExpression(self)


    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_primary_expressionContext)
            super(PParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(PParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_primary_expressionContext)
            super(PParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(PParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonLiteralExpression(self)



    def python_primary_expression(self):

        localctx = PParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_python_primary_expression)
        try:
            self.state = 1725
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                localctx = PParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1721 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = PParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1722 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = PParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1723 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = PParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1724 
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
            super(PParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(PParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_selector_expressionContext)
            super(PParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonItemExpression(self)


    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_selector_expressionContext)
            super(PParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(PParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonMethodExpression(self)



    def python_selector_expression(self):

        localctx = PParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_python_selector_expression)
        try:
            self.state = 1733
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1727
                self.match(PParser.DOT)
                self.state = 1728 
                localctx.exp = self.python_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1729
                self.match(PParser.LBRAK)
                self.state = 1730 
                localctx.exp = self.python_expression(0)
                self.state = 1731
                self.match(PParser.RBRAK)

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
            super(PParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(PParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return PParser.RULE_python_method_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = PParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1735 
            localctx.name = self.python_identifier()
            self.state = 1736
            self.match(PParser.LPAR)
            self.state = 1738
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (PParser.BOOLEAN_LITERAL - 134)) | (1 << (PParser.CHAR_LITERAL - 134)) | (1 << (PParser.SYMBOL_IDENTIFIER - 134)) | (1 << (PParser.TYPE_IDENTIFIER - 134)) | (1 << (PParser.VARIABLE_IDENTIFIER - 134)) | (1 << (PParser.TEXT_LITERAL - 134)) | (1 << (PParser.INTEGER_LITERAL - 134)) | (1 << (PParser.DECIMAL_LITERAL - 134)))) != 0):
                self.state = 1737 
                localctx.args = self.python_argument_list()


            self.state = 1740
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(PParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_argument_listContext)
            super(PParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_argument_listContext)
            super(PParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonArgumentList(self)


    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_argument_listContext)
            super(PParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)



    def python_argument_list(self):

        localctx = PParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_python_argument_list)
        try:
            self.state = 1748
            la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
            if la_ == 1:
                localctx = PParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1742 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = PParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1743 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = PParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1744 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1745
                self.match(PParser.COMMA)
                self.state = 1746 
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
            super(PParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(PParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_ordinal_argument_listContext)
            super(PParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_ordinal_argument_listContext)
            super(PParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonOrdinalArgumentList(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 306
        self.enterRecursionRule(localctx, 306, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1751 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1758
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonOrdinalArgumentListItemContext(self, PParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1753
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1754
                    self.match(PParser.COMMA)
                    self.state = 1755 
                    localctx.item = self.python_expression(0) 
                self.state = 1760
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(PParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_named_argument_listContext)
            super(PParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def EQ(self):
            return self.getToken(PParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(PParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(PParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonNamedArgumentListItem(self)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_named_argument_listContext)
            super(PParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(PParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(PParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonNamedArgumentList(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 308
        self.enterRecursionRule(localctx, 308, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1762 
            localctx.name = self.python_identifier()
            self.state = 1763
            self.match(PParser.EQ)
            self.state = 1764 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1774
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonNamedArgumentListItemContext(self, PParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1766
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1767
                    self.match(PParser.COMMA)
                    self.state = 1768 
                    localctx.name = self.python_identifier()
                    self.state = 1769
                    self.match(PParser.EQ)
                    self.state = 1770 
                    localctx.exp = self.python_expression(0) 
                self.state = 1776
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(PParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = PParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1777
            self.match(PParser.LPAR)
            self.state = 1778 
            localctx.exp = self.python_expression(0)
            self.state = 1779
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(PParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_identifier_expressionContext)
            super(PParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(PParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_identifier_expressionContext)
            super(PParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(PParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 312
        self.enterRecursionRule(localctx, 312, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1782 
            localctx.name = self.python_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1789
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonChildIdentifierContext(self, PParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1784
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1785
                    self.match(PParser.DOT)
                    self.state = 1786 
                    localctx.name = self.python_identifier() 
                self.state = 1791
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(PParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_literal_expressionContext)
            super(PParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(PParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_literal_expressionContext)
            super(PParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_literal_expressionContext)
            super(PParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(PParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_literal_expressionContext)
            super(PParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(PParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonDecimalLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Python_literal_expressionContext)
            super(PParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(PParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPythonBooleanLiteral(self)



    def python_literal_expression(self):

        localctx = PParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_python_literal_expression)
        try:
            self.state = 1797
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1792
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1793
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1794
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1795
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1796
                localctx.t = self.match(PParser.CHAR_LITERAL)

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
            super(PParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(PParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(PParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(PParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(PParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(PParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(PParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(PParser.DATE, 0)

        def TIME(self):
            return self.getToken(PParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(PParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(PParser.PERIOD, 0)

        def getRuleIndex(self):
            return PParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = PParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1799
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (PParser.SYMBOL_IDENTIFIER - 138)) | (1 << (PParser.TYPE_IDENTIFIER - 138)) | (1 << (PParser.VARIABLE_IDENTIFIER - 138)))) != 0)):
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
            super(PParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(PParser.Java_statementContext, self).copyFrom(ctx)



    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_statementContext)
            super(PParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaStatement(self)


    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_statementContext)
            super(PParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(PParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaReturnStatement(self)



    def java_statement(self):

        localctx = PParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_java_statement)
        try:
            self.state = 1808
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1801
                self.match(PParser.RETURN)
                self.state = 1802 
                localctx.exp = self.java_expression(0)
                self.state = 1803
                self.match(PParser.SEMI)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1805 
                localctx.exp = self.java_expression(0)
                self.state = 1806
                self.match(PParser.SEMI)

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
            super(PParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(PParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_expressionContext)
            super(PParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(PParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaPrimaryExpression(self)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_expressionContext)
            super(PParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(PParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaSelectorExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1811 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1817
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,131,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaSelectorExpressionContext(self, PParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 1813
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1814 
                    localctx.child = self.java_selector_expression() 
                self.state = 1819
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,131,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_primary_expression

     
        def copyFrom(self, ctx):
            super(PParser.Java_primary_expressionContext, self).copyFrom(ctx)



    class JavaIdentifierExpressionContext(Java_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_primary_expressionContext)
            super(PParser.JavaIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaIdentifierExpression(self)


    class JavaLiteralExpressionContext(Java_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_primary_expressionContext)
            super(PParser.JavaLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Java_literal_expressionContext
            self.copyFrom(ctx)

        def java_literal_expression(self):
            return self.getTypedRuleContext(PParser.Java_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaLiteralExpression(self)


    class JavaParenthesisExpressionContext(Java_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_primary_expressionContext)
            super(PParser.JavaParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Java_parenthesis_expressionContext
            self.copyFrom(ctx)

        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(PParser.Java_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaParenthesisExpression(self)



    def java_primary_expression(self):

        localctx = PParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_java_primary_expression)
        try:
            self.state = 1823
            token = self._input.LA(1)
            if token in [PParser.LPAR]:
                localctx = PParser.JavaParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1820 
                localctx.exp = self.java_parenthesis_expression()

            elif token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.JavaIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1821 
                localctx.exp = self.java_identifier_expression(0)

            elif token in [PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavaLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1822 
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
            super(PParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(PParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_selector_expressionContext)
            super(PParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(PParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_selector_expressionContext)
            super(PParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(PParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = PParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_java_selector_expression)
        try:
            self.state = 1828
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1825
                self.match(PParser.DOT)
                self.state = 1826 
                localctx.exp = self.java_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1827 
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
            super(PParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(PParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(PParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return PParser.RULE_java_method_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = PParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1830 
            localctx.name = self.java_identifier()
            self.state = 1831
            self.match(PParser.LPAR)
            self.state = 1833
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (PParser.BOOLEAN_LITERAL - 134)) | (1 << (PParser.CHAR_LITERAL - 134)) | (1 << (PParser.SYMBOL_IDENTIFIER - 134)) | (1 << (PParser.TYPE_IDENTIFIER - 134)) | (1 << (PParser.VARIABLE_IDENTIFIER - 134)) | (1 << (PParser.TEXT_LITERAL - 134)) | (1 << (PParser.INTEGER_LITERAL - 134)) | (1 << (PParser.DECIMAL_LITERAL - 134)))) != 0):
                self.state = 1832 
                localctx.args = self.java_arguments(0)


            self.state = 1835
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(PParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_argumentsContext)
            super(PParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaArgumentList(self)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_argumentsContext)
            super(PParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(PParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaArgumentListItem(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 328
        self.enterRecursionRule(localctx, 328, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1838 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1845
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,135,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaArgumentListItemContext(self, PParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 1840
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1841
                    self.match(PParser.COMMA)
                    self.state = 1842 
                    localctx.item = self.java_expression(0) 
                self.state = 1847
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,135,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_java_item_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = PParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1848
            self.match(PParser.LBRAK)
            self.state = 1849 
            localctx.exp = self.java_expression(0)
            self.state = 1850
            self.match(PParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(PParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = PParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1852
            self.match(PParser.LPAR)
            self.state = 1853 
            localctx.exp = self.java_expression(0)
            self.state = 1854
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(PParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_identifier_expressionContext)
            super(PParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(PParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_identifier_expressionContext)
            super(PParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(PParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1857 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1864
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,136,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaChildIdentifierContext(self, PParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 1859
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1860
                    self.match(PParser.DOT)
                    self.state = 1861 
                    localctx.name = self.java_identifier() 
                self.state = 1866
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,136,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(PParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_class_identifier_expressionContext)
            super(PParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def DOLLAR(self):
            return self.getToken(PParser.DOLLAR, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Java_class_identifier_expressionContext,0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaChildClassIdentifier(self)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_class_identifier_expressionContext)
            super(PParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 336
        self.enterRecursionRule(localctx, 336, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1868 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1875
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaChildClassIdentifierContext(self, PParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 1870
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1871
                    self.match(PParser.DOLLAR)
                    self.state = 1872
                    localctx.name = self.match(PParser.TYPE_IDENTIFIER) 
                self.state = 1877
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(PParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_literal_expressionContext)
            super(PParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(PParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_literal_expressionContext)
            super(PParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(PParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_literal_expressionContext)
            super(PParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(PParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_literal_expressionContext)
            super(PParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(PParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaDecimalLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Java_literal_expressionContext)
            super(PParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJavaTextLiteral(self)



    def java_literal_expression(self):

        localctx = PParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_java_literal_expression)
        try:
            self.state = 1883
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1878
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1879
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1880
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1881
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1882
                localctx.t = self.match(PParser.CHAR_LITERAL)

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
            super(PParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(PParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(PParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(PParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(PParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(PParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(PParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(PParser.DATE, 0)

        def TIME(self):
            return self.getToken(PParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(PParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(PParser.PERIOD, 0)

        def getRuleIndex(self):
            return PParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = PParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1885
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (PParser.SYMBOL_IDENTIFIER - 138)) | (1 << (PParser.TYPE_IDENTIFIER - 138)) | (1 << (PParser.VARIABLE_IDENTIFIER - 138)))) != 0)):
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
            super(PParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_statementContext)
            super(PParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpStatement(self)


    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_statementContext)
            super(PParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(PParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(PParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpReturnStatement(self)



    def csharp_statement(self):

        localctx = PParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_csharp_statement)
        try:
            self.state = 1894
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1887
                self.match(PParser.RETURN)
                self.state = 1888 
                localctx.exp = self.csharp_expression(0)
                self.state = 1889
                self.match(PParser.SEMI)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1891 
                localctx.exp = self.csharp_expression(0)
                self.state = 1892
                self.match(PParser.SEMI)

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
            super(PParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_expressionContext)
            super(PParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpPrimaryExpression(self)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_expressionContext)
            super(PParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpSelectorExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1897 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1903
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CSharpSelectorExpressionContext(self, PParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 1899
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1900 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 1905
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_primary_expression

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_primary_expressionContext, self).copyFrom(ctx)



    class CSharpLiteralExpressionContext(Csharp_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_primary_expressionContext)
            super(PParser.CSharpLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_literal_expressionContext
            self.copyFrom(ctx)

        def csharp_literal_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpLiteralExpression(self)


    class CSharpParenthesisExpressionContext(Csharp_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_primary_expressionContext)
            super(PParser.CSharpParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_parenthesis_expressionContext
            self.copyFrom(ctx)

        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpParenthesisExpression(self)


    class CSharpIdentifierExpressionContext(Csharp_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_primary_expressionContext)
            super(PParser.CSharpIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpIdentifierExpression(self)



    def csharp_primary_expression(self):

        localctx = PParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_csharp_primary_expression)
        try:
            self.state = 1909
            token = self._input.LA(1)
            if token in [PParser.LPAR]:
                localctx = PParser.CSharpParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1906 
                localctx.exp = self.csharp_parenthesis_expression()

            elif token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.CSharpIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1907 
                localctx.exp = self.csharp_identifier_expression(0)

            elif token in [PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.CSharpLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1908 
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
            super(PParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_selector_expressionContext)
            super(PParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpItemExpression(self)


    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_selector_expressionContext)
            super(PParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpMethodExpression(self)



    def csharp_selector_expression(self):

        localctx = PParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_csharp_selector_expression)
        try:
            self.state = 1914
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1911
                self.match(PParser.DOT)
                self.state = 1912 
                localctx.exp = self.csharp_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1913 
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
            super(PParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(PParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(PParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return PParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = PParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1916 
            localctx.name = self.csharp_identifier()
            self.state = 1917
            self.match(PParser.LPAR)
            self.state = 1919
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (PParser.BOOLEAN_LITERAL - 134)) | (1 << (PParser.CHAR_LITERAL - 134)) | (1 << (PParser.SYMBOL_IDENTIFIER - 134)) | (1 << (PParser.TYPE_IDENTIFIER - 134)) | (1 << (PParser.VARIABLE_IDENTIFIER - 134)) | (1 << (PParser.TEXT_LITERAL - 134)) | (1 << (PParser.INTEGER_LITERAL - 134)) | (1 << (PParser.DECIMAL_LITERAL - 134)))) != 0):
                self.state = 1918 
                localctx.args = self.csharp_arguments(0)


            self.state = 1921
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_argumentsContext)
            super(PParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_argumentsContext)
            super(PParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(PParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(PParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1924 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1931
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,144,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CSharpArgumentListItemContext(self, PParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 1926
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1927
                    self.match(PParser.COMMA)
                    self.state = 1928 
                    localctx.item = self.csharp_expression(0) 
                self.state = 1933
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,144,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(PParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(PParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = PParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1934
            self.match(PParser.LBRAK)
            self.state = 1935 
            localctx.exp = self.csharp_expression(0)
            self.state = 1936
            self.match(PParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = PParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1938
            self.match(PParser.LPAR)
            self.state = 1939 
            localctx.exp = self.csharp_expression(0)
            self.state = 1940
            self.match(PParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_identifier_expressionContext)
            super(PParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(PParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_identifier_expressionContext)
            super(PParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(PParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(PParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(PParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpChildIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CSharpIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1943 
            localctx.name = self.csharp_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1950
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CSharpChildIdentifierContext(self, PParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 1945
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1946
                    self.match(PParser.DOT)
                    self.state = 1947 
                    localctx.name = self.csharp_identifier() 
                self.state = 1952
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(PParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_literal_expressionContext)
            super(PParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(PParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_literal_expressionContext)
            super(PParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(PParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_literal_expressionContext)
            super(PParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(PParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_literal_expressionContext)
            super(PParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(PParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a PParser.Csharp_literal_expressionContext)
            super(PParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = PParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_csharp_literal_expression)
        try:
            self.state = 1958
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1953
                self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1954
                self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1955
                self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1956
                self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1957
                self.match(PParser.CHAR_LITERAL)

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
            super(PParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(PParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(PParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(PParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(PParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(PParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(PParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(PParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(PParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(PParser.DATE, 0)

        def TIME(self):
            return self.getToken(PParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(PParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(PParser.PERIOD, 0)

        def getRuleIndex(self):
            return PParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = PParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1960
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (PParser.SYMBOL_IDENTIFIER - 138)) | (1 << (PParser.TYPE_IDENTIFIER - 138)) | (1 << (PParser.VARIABLE_IDENTIFIER - 138)))) != 0)):
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
        self._predicates[24] = self.callable_parent_sempred
        self._predicates[34] = self.else_if_statement_list_sempred
        self._predicates[39] = self.expression_sempred
        self._predicates[41] = self.instance_expression_sempred
        self._predicates[43] = self.instance_selector_sempred
        self._predicates[46] = self.argument_assignment_list_sempred
        self._predicates[53] = self.child_instance_sempred
        self._predicates[61] = self.declarations_sempred
        self._predicates[65] = self.native_symbol_list_sempred
        self._predicates[66] = self.category_symbol_list_sempred
        self._predicates[67] = self.symbol_list_sempred
        self._predicates[71] = self.expression_list_sempred
        self._predicates[73] = self.typedef_sempred
        self._predicates[80] = self.type_identifier_list_sempred
        self._predicates[86] = self.argument_list_sempred
        self._predicates[92] = self.any_type_sempred
        self._predicates[93] = self.category_method_declaration_list_sempred
        self._predicates[98] = self.module_token_sempred
        self._predicates[101] = self.variable_identifier_list_sempred
        self._predicates[103] = self.native_statement_list_sempred
        self._predicates[107] = self.statement_list_sempred
        self._predicates[108] = self.switch_case_statement_list_sempred
        self._predicates[109] = self.catch_statement_list_sempred
        self._predicates[112] = self.literal_list_literal_sempred
        self._predicates[120] = self.expression_tuple_sempred
        self._predicates[121] = self.dict_entry_list_sempred
        self._predicates[125] = self.assignable_instance_sempred
        self._predicates[126] = self.is_expression_sempred
        self._predicates[128] = self.key_token_sempred
        self._predicates[129] = self.value_token_sempred
        self._predicates[130] = self.symbols_token_sempred
        self._predicates[137] = self.javascript_expression_sempred
        self._predicates[141] = self.javascript_arguments_sempred
        self._predicates[144] = self.javascript_identifier_expression_sempred
        self._predicates[148] = self.python_expression_sempred
        self._predicates[153] = self.python_ordinal_argument_list_sempred
        self._predicates[154] = self.python_named_argument_list_sempred
        self._predicates[156] = self.python_identifier_expression_sempred
        self._predicates[160] = self.java_expression_sempred
        self._predicates[164] = self.java_arguments_sempred
        self._predicates[167] = self.java_identifier_expression_sempred
        self._predicates[168] = self.java_class_identifier_expression_sempred
        self._predicates[172] = self.csharp_expression_sempred
        self._predicates[176] = self.csharp_arguments_sempred
        self._predicates[179] = self.csharp_identifier_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def native_category_mapping_list_sempred(self, localctx, predIndex):
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
                return self.wasNot(PParser.WS)
         

            if predIndex == 31:
                return self.wasNot(PParser.WS)
         

            if predIndex == 32:
                return self.wasNot(PParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 34:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.wasNot(PParser.WS)
         

            if predIndex == 36:
                return self.wasNot(PParser.WS)
         

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
         

    def category_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.willBeAOrAn()
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         

    def javascript_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         



