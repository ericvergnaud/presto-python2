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
        buf.write(u"\u00a9\u08b5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca\t\u00ca\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\5\2\u019b\n\2\3\2\5\2\u019e\n\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u01b7\n")
        buf.write(u"\5\3\5\3\5\3\6\5\6\u01bc\n\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\3\6\5\6\u01c7\n\6\3\6\3\6\3\7\5\7\u01cc\n\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01d7\n\7\3")
        buf.write(u"\7\3\7\3\7\3\7\3\7\5\7\u01de\n\7\3\7\3\7\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01eb\n\b\3\b\3\b\3\t\3")
        buf.write(u"\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u01f9\n\n\3\n")
        buf.write(u"\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\f\3\f\3\f\5\f\u020d\n\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\16\3\16\3\16\5\16\u0224\n\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\17\5\17\u022f\n\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\5\17\u0236\n\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\5\17\u023f\n\17\3\17\3\17\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\5\20\u0248\n\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\5\20\u0251\n\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\7\22\u0264\n\22\f\22\16\22\u0267\13\22\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\5\23\u026e\n\23\3\23\3\23\3\23\5\23\u0273")
        buf.write(u"\n\23\3\24\3\24\3\24\3\24\5\24\u0279\n\24\3\24\3\24\3")
        buf.write(u"\24\5\24\u027e\n\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write(u"\5\25\u0287\n\25\3\25\3\25\3\25\5\25\u028c\n\25\3\25")
        buf.write(u"\3\25\3\25\5\25\u0291\n\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u02a9\n\26\3\27\3")
        buf.write(u"\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u02b4\n\30")
        buf.write(u"\3\30\3\30\5\30\u02b8\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\5\31\u02cb\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\5\32\u02e1\n\32\3\33\3\33\3\33\5\33\u02e6")
        buf.write(u"\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\5\34\u02ef\n")
        buf.write(u"\34\3\35\3\35\3\35\3\35\3\35\7\35\u02f6\n\35\f\35\16")
        buf.write(u"\35\u02f9\13\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0301")
        buf.write(u"\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write(u"\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u031e")
        buf.write(u"\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\5\"\u0331\n\"\3#\3#\3#\3#\5#\u0337\n")
        buf.write(u"#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%")
        buf.write(u"\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0359")
        buf.write(u"\n&\3&\3&\3&\3&\3&\3&\3&\5&\u0362\n&\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\7\'\u0377\n\'\f\'\16\'\u037a\13\'\3(\3(\3(\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\5)\u0387\n)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\5)\u0390\n)\3)\3)\3)\3)\3)\3)\3)\5)\u0399\n)\3)\3")
        buf.write(u")\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*")
        buf.write(u"\3*\3*\5*\u03b0\n*\3+\3+\5+\u03b4\n+\3,\3,\3,\3,\3,\3")
        buf.write(u",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u03c8\n,\3,")
        buf.write(u"\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(u",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write(u"\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(u",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write(u"\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(u",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\7,\u042e\n,\f,\16")
        buf.write(u",\u0431\13,\3-\3-\3.\3.\3.\3.\3.\7.\u043a\n.\f.\16.\u043d")
        buf.write(u"\13.\3/\3/\3/\3/\3/\3/\3/\5/\u0446\n/\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5")
        buf.write(u"\60\u0455\n\60\3\61\3\61\3\61\5\61\u045a\n\61\3\61\3")
        buf.write(u"\61\3\62\3\62\3\62\5\62\u0461\n\62\3\62\3\62\3\63\3\63")
        buf.write(u"\3\63\5\63\u0468\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\5\64\u0471\n\64\3\64\3\64\3\64\7\64\u0476\n\64\f")
        buf.write(u"\64\16\64\u0479\13\64\3\65\3\65\3\65\3\65\3\66\3\66\3")
        buf.write(u"\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\3")
        buf.write(u"8\38\38\38\58\u0492\n8\38\38\38\38\38\38\38\38\38\58")
        buf.write(u"\u049d\n8\38\38\58\u04a1\n8\38\38\38\58\u04a6\n8\38\3")
        buf.write(u"8\38\58\u04ab\n8\58\u04ad\n8\39\39\39\39\39\39\39\39")
        buf.write(u"\59\u04b7\n9\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(u";\5;\u04c7\n;\3<\3<\3<\3<\3=\7=\u04ce\n=\f=\16=\u04d1")
        buf.write(u"\13=\3>\6>\u04d4\n>\r>\16>\u04d5\3?\6?\u04d9\n?\r?\16")
        buf.write(u"?\u04da\3?\3?\3@\7@\u04e0\n@\f@\16@\u04e3\13@\3@\3@\3")
        buf.write(u"A\3A\3B\5B\u04ea\nB\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\7C")
        buf.write(u"\u04f6\nC\fC\16C\u04f9\13C\3D\3D\3D\7D\u04fe\nD\fD\16")
        buf.write(u"D\u0501\13D\3D\3D\3D\3D\3D\5D\u0508\nD\3E\3E\3F\3F\5")
        buf.write(u"F\u050e\nF\3G\3G\3G\3G\3G\3G\3G\7G\u0517\nG\fG\16G\u051a")
        buf.write(u"\13G\3H\3H\3H\3H\3H\3H\3H\7H\u0523\nH\fH\16H\u0526\13")
        buf.write(u"H\3I\3I\3I\3I\3I\3I\7I\u052e\nI\fI\16I\u0531\13I\3J\3")
        buf.write(u"J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u053d\nJ\3K\3K\5K\u0541")
        buf.write(u"\nK\3K\3K\3L\3L\5L\u0547\nL\3L\3L\3M\3M\3M\3M\3M\3M\7")
        buf.write(u"M\u0551\nM\fM\16M\u0554\13M\3N\3N\3N\3N\3N\3N\3O\3O\3")
        buf.write(u"O\3O\3O\3O\3O\3O\3O\3O\3O\7O\u0567\nO\fO\16O\u056a\13")
        buf.write(u"O\3P\3P\5P\u056e\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q")
        buf.write(u"\3Q\3Q\3Q\5Q\u057e\nQ\3R\3R\3S\5S\u0583\nS\3S\3S\3T\3")
        buf.write(u"T\3U\3U\3U\5U\u058c\nU\3V\3V\3V\3V\3V\3V\7V\u0594\nV")
        buf.write(u"\fV\16V\u0597\13V\3W\3W\5W\u059b\nW\3X\3X\3X\5X\u05a0")
        buf.write(u"\nX\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3]\3]\3]\3]\7]\u05b0")
        buf.write(u"\n]\f]\16]\u05b3\13]\3^\3^\5^\u05b7\n^\3^\5^\u05ba\n")
        buf.write(u"^\3_\3_\5_\u05be\n_\3`\3`\3`\5`\u05c3\n`\3a\3a\3a\3b")
        buf.write(u"\3b\5b\u05ca\nb\3c\3c\3c\3c\3c\3c\3c\3c\3c\7c\u05d5\n")
        buf.write(u"c\fc\16c\u05d8\13c\3d\3d\3d\3d\3d\3d\3d\7d\u05e1\nd\f")
        buf.write(u"d\16d\u05e4\13d\3e\3e\3e\3e\3e\5e\u05eb\ne\3f\3f\3f\3")
        buf.write(u"f\3f\3f\3f\7f\u05f4\nf\ff\16f\u05f7\13f\3g\3g\3g\5g\u05fc")
        buf.write(u"\ng\3h\3h\3h\3h\3h\3h\3h\3h\3h\3h\5h\u0608\nh\3i\3i\5")
        buf.write(u"i\u060c\ni\3j\3j\3j\3j\3j\3j\7j\u0614\nj\fj\16j\u0617")
        buf.write(u"\13j\3k\3k\3k\3l\3l\5l\u061e\nl\3m\3m\3m\3m\5m\u0624")
        buf.write(u"\nm\3m\3m\3m\7m\u0629\nm\fm\16m\u062c\13m\3m\3m\5m\u0630")
        buf.write(u"\nm\3n\3n\3n\7n\u0635\nn\fn\16n\u0638\13n\3o\3o\3o\7")
        buf.write(u"o\u063d\no\fo\16o\u0640\13o\3p\3p\3p\3p\5p\u0646\np\3")
        buf.write(u"q\3q\3r\3r\3r\3r\3r\3r\3r\7r\u0651\nr\fr\16r\u0654\13")
        buf.write(u"r\3s\3s\3s\3s\3s\3s\3s\3s\3s\3s\5s\u0660\ns\3t\3t\5t")
        buf.write(u"\u0664\nt\3t\5t\u0667\nt\3u\3u\5u\u066b\nu\3u\5u\u066e")
        buf.write(u"\nu\3v\3v\3v\3v\3v\3v\3v\7v\u0677\nv\fv\16v\u067a\13")
        buf.write(u"v\3w\3w\3w\3w\3w\3w\3w\7w\u0683\nw\fw\16w\u0686\13w\3")
        buf.write(u"x\3x\3x\3x\3x\3x\3x\7x\u068f\nx\fx\16x\u0692\13x\3y\3")
        buf.write(u"y\3y\3y\3y\3y\3y\7y\u069b\ny\fy\16y\u069e\13y\3z\3z\3")
        buf.write(u"z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\5z\u06ae\nz\3{\3{")
        buf.write(u"\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\5{\u06bd\n{\3|\3|\3")
        buf.write(u"|\3|\3|\3|\7|\u06c5\n|\f|\16|\u06c8\13|\3}\3}\3}\3}\5")
        buf.write(u"}\u06ce\n}\3~\3~\3\177\3\177\3\177\3\177\3\u0080\3\u0080")
        buf.write(u"\5\u0080\u06d8\n\u0080\3\u0081\3\u0081\3\u0081\3\u0081")
        buf.write(u"\3\u0081\5\u0081\u06df\n\u0081\3\u0082\3\u0082\5\u0082")
        buf.write(u"\u06e3\n\u0082\3\u0082\3\u0082\3\u0083\3\u0083\5\u0083")
        buf.write(u"\u06e9\n\u0083\3\u0083\3\u0083\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\3\u0084\3\u0084\7\u0084\u06f3\n\u0084\f\u0084")
        buf.write(u"\16\u0084\u06f6\13\u0084\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\7\u0085\u06fe\n\u0085\f\u0085\16\u0085")
        buf.write(u"\u0701\13\u0085\3\u0086\3\u0086\3\u0086\3\u0086\3\u0087")
        buf.write(u"\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\5\u0087\u0710\n\u0087\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\7\u0089")
        buf.write(u"\u071b\n\u0089\f\u0089\16\u0089\u071e\13\u0089\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\5\u008a\u0724\n\u008a\3\u008b")
        buf.write(u"\3\u008b\3\u008b\7\u008b\u0729\n\u008b\f\u008b\16\u008b")
        buf.write(u"\u072c\13\u008b\3\u008c\3\u008c\3\u008c\7\u008c\u0731")
        buf.write(u"\n\u008c\f\u008c\16\u008c\u0734\13\u008c\3\u008c\5\u008c")
        buf.write(u"\u0737\n\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write(u"\3\u008d\5\u008d\u073f\n\u008d\3\u008e\3\u008e\3\u008e")
        buf.write(u"\3\u008f\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0092\3\u0092\3\u0093\3\u0093\3\u0094")
        buf.write(u"\3\u0094\3\u0095\3\u0095\3\u0096\3\u0096\3\u0097\3\u0097")
        buf.write(u"\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097\5\u0097\u075e")
        buf.write(u"\n\u0097\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\7\u0098")
        buf.write(u"\u0765\n\u0098\f\u0098\16\u0098\u0768\13\u0098\3\u0099")
        buf.write(u"\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\5\u0099")
        buf.write(u"\u0771\n\u0099\3\u009a\3\u009a\3\u009b\3\u009b\3\u009b")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\5\u009c\u077d")
        buf.write(u"\n\u009c\3\u009d\3\u009d\3\u009d\5\u009d\u0782\n\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\7\u009e\u078c\n\u009e\f\u009e\16\u009e\u078f")
        buf.write(u"\13\u009e\3\u009f\3\u009f\3\u009f\3\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a0\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\3\u00a2\5\u00a2\u07a0\n\u00a2\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a4\5\u00a4\u07a7\n\u00a4\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u07ae\n\u00a5")
        buf.write(u"\f\u00a5\16\u00a5\u07b1\13\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\5\u00a6\u07b7\n\u00a6\3\u00a7\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a7\3\u00a7\5\u00a7\u07bf\n\u00a7\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a8\5\u00a8\u07c4\n\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\5\u00a9")
        buf.write(u"\u07ce\n\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write(u"\3\u00aa\7\u00aa\u07d6\n\u00aa\f\u00aa\16\u00aa\u07d9")
        buf.write(u"\13\u00aa\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\7\u00ab\u07e6")
        buf.write(u"\n\u00ab\f\u00ab\16\u00ab\u07e9\13\u00ab\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u07f2")
        buf.write(u"\n\u00ad\3\u00ad\3\u00ad\3\u00ad\7\u00ad\u07f7\n\u00ad")
        buf.write(u"\f\u00ad\16\u00ad\u07fa\13\u00ad\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\5\u00ae\u0801\n\u00ae\3\u00af\3\u00af")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\5\u00b0\u080c\n\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\7\u00b1\u0813\n\u00b1\f\u00b1\16\u00b1\u0816")
        buf.write(u"\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write(u"\u081d\n\u00b2\3\u00b3\3\u00b3\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u0827\n\u00b5\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\5\u00b6\u082c\n\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\7\u00b7")
        buf.write(u"\u0836\n\u00b7\f\u00b7\16\u00b7\u0839\13\u00b7\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\3\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write(u"\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\7\u00ba")
        buf.write(u"\u0849\n\u00ba\f\u00ba\16\u00ba\u084c\13\u00ba\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u0853\n\u00bb")
        buf.write(u"\f\u00bb\16\u00bb\u0856\13\u00bb\3\u00bc\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\5\u00bc\u085d\n\u00bc\3\u00bd\3\u00bd")
        buf.write(u"\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write(u"\5\u00be\u0868\n\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write(u"\3\u00bf\7\u00bf\u086f\n\u00bf\f\u00bf\16\u00bf\u0872")
        buf.write(u"\13\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0\5\u00c0")
        buf.write(u"\u0879\n\u00c0\3\u00c1\3\u00c1\3\u00c2\3\u00c2\3\u00c2")
        buf.write(u"\3\u00c3\3\u00c3\3\u00c3\5\u00c3\u0883\n\u00c3\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c4\5\u00c4\u0888\n\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\7\u00c5")
        buf.write(u"\u0892\n\u00c5\f\u00c5\16\u00c5\u0895\13\u00c5\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\3\u00c7\3\u00c7\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c8\3\u00c8\3\u00c8\5\u00c8\u08a2\n\u00c8\3\u00c8")
        buf.write(u"\3\u00c8\3\u00c8\7\u00c8\u08a7\n\u00c8\f\u00c8\16\u00c8")
        buf.write(u"\u08aa\13\u00c8\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9")
        buf.write(u"\5\u00c9\u08b1\n\u00c9\3\u00ca\3\u00ca\3\u00ca\2)\"8")
        buf.write(u"LVZf\u0084\u008c\u008e\u0090\u0098\u009c\u00aa\u00b8")
        buf.write(u"\u00c4\u00c6\u00ca\u00e2\u00ea\u00ec\u00ee\u00f0\u00f6")
        buf.write(u"\u0106\u0108\u0110\u012e\u013a\u0148\u0152\u0154\u0158")
        buf.write(u"\u0160\u016c\u0172\u0174\u017c\u0188\u018e\u00cb\2\4")
        buf.write(u"\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write(u"\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
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
        buf.write(u"\u0180\u0182\u0184\u0186\u0188\u018a\u018c\u018e\u0190")
        buf.write(u"\u0192\2\f\3\2QR\3\2\"#\4\2\u008b\u008b\u009f\u009f\4")
        buf.write(u"\2\u0087\u0087\u008f\u008f\4\2IIYY\4\2\'\'qq\b\2\64<")
        buf.write(u"\u0081\u0081\u008e\u008e\u0098\u0098\u009d\u009f\u00a1")
        buf.write(u"\u00a1\b\2\64<\u0081\u0081\u0087\u0087\u008e\u008f\u0098")
        buf.write(u"\u0098\u009d\u009f\7\2\64<\u0081\u0081\u008e\u008e\u0098")
        buf.write(u"\u0098\u009d\u00a1\7\2\64<\u0081\u0081\u008e\u008e\u0098")
        buf.write(u"\u0098\u009d\u009f\u0921\2\u0194\3\2\2\2\4\u01a5\3\2")
        buf.write(u"\2\2\6\u01af\3\2\2\2\b\u01b3\3\2\2\2\n\u01bb\3\2\2\2")
        buf.write(u"\f\u01cb\3\2\2\2\16\u01e1\3\2\2\2\20\u01ee\3\2\2\2\22")
        buf.write(u"\u01f0\3\2\2\2\24\u01ff\3\2\2\2\26\u0209\3\2\2\2\30\u0216")
        buf.write(u"\3\2\2\2\32\u0220\3\2\2\2\34\u022e\3\2\2\2\36\u0242\3")
        buf.write(u"\2\2\2 \u0254\3\2\2\2\"\u025c\3\2\2\2$\u0268\3\2\2\2")
        buf.write(u"&\u0274\3\2\2\2(\u0284\3\2\2\2*\u0297\3\2\2\2,\u02aa")
        buf.write(u"\3\2\2\2.\u02ac\3\2\2\2\60\u02ca\3\2\2\2\62\u02e0\3\2")
        buf.write(u"\2\2\64\u02e2\3\2\2\2\66\u02ee\3\2\2\28\u02f0\3\2\2\2")
        buf.write(u":\u0300\3\2\2\2<\u0302\3\2\2\2>\u0309\3\2\2\2@\u0310")
        buf.write(u"\3\2\2\2B\u0330\3\2\2\2D\u0332\3\2\2\2F\u033f\3\2\2\2")
        buf.write(u"H\u0348\3\2\2\2J\u034f\3\2\2\2L\u0363\3\2\2\2N\u037b")
        buf.write(u"\3\2\2\2P\u037e\3\2\2\2R\u03af\3\2\2\2T\u03b1\3\2\2\2")
        buf.write(u"V\u03c7\3\2\2\2X\u0432\3\2\2\2Z\u0434\3\2\2\2\\\u0445")
        buf.write(u"\3\2\2\2^\u0454\3\2\2\2`\u0456\3\2\2\2b\u045d\3\2\2\2")
        buf.write(u"d\u0464\3\2\2\2f\u0470\3\2\2\2h\u047a\3\2\2\2j\u047e")
        buf.write(u"\3\2\2\2l\u0482\3\2\2\2n\u04ac\3\2\2\2p\u04ae\3\2\2\2")
        buf.write(u"r\u04ba\3\2\2\2t\u04c6\3\2\2\2v\u04c8\3\2\2\2x\u04cf")
        buf.write(u"\3\2\2\2z\u04d3\3\2\2\2|\u04d8\3\2\2\2~\u04e1\3\2\2\2")
        buf.write(u"\u0080\u04e6\3\2\2\2\u0082\u04e9\3\2\2\2\u0084\u04ee")
        buf.write(u"\3\2\2\2\u0086\u04ff\3\2\2\2\u0088\u0509\3\2\2\2\u008a")
        buf.write(u"\u050d\3\2\2\2\u008c\u050f\3\2\2\2\u008e\u051b\3\2\2")
        buf.write(u"\2\u0090\u0527\3\2\2\2\u0092\u053c\3\2\2\2\u0094\u053e")
        buf.write(u"\3\2\2\2\u0096\u0544\3\2\2\2\u0098\u054a\3\2\2\2\u009a")
        buf.write(u"\u0555\3\2\2\2\u009c\u055b\3\2\2\2\u009e\u056d\3\2\2")
        buf.write(u"\2\u00a0\u057d\3\2\2\2\u00a2\u057f\3\2\2\2\u00a4\u0582")
        buf.write(u"\3\2\2\2\u00a6\u0586\3\2\2\2\u00a8\u058b\3\2\2\2\u00aa")
        buf.write(u"\u058d\3\2\2\2\u00ac\u059a\3\2\2\2\u00ae\u059f\3\2\2")
        buf.write(u"\2\u00b0\u05a1\3\2\2\2\u00b2\u05a3\3\2\2\2\u00b4\u05a5")
        buf.write(u"\3\2\2\2\u00b6\u05a7\3\2\2\2\u00b8\u05a9\3\2\2\2\u00ba")
        buf.write(u"\u05b9\3\2\2\2\u00bc\u05bd\3\2\2\2\u00be\u05bf\3\2\2")
        buf.write(u"\2\u00c0\u05c4\3\2\2\2\u00c2\u05c9\3\2\2\2\u00c4\u05cb")
        buf.write(u"\3\2\2\2\u00c6\u05d9\3\2\2\2\u00c8\u05ea\3\2\2\2\u00ca")
        buf.write(u"\u05ec\3\2\2\2\u00cc\u05fb\3\2\2\2\u00ce\u0607\3\2\2")
        buf.write(u"\2\u00d0\u0609\3\2\2\2\u00d2\u060d\3\2\2\2\u00d4\u0618")
        buf.write(u"\3\2\2\2\u00d6\u061b\3\2\2\2\u00d8\u061f\3\2\2\2\u00da")
        buf.write(u"\u0631\3\2\2\2\u00dc\u0639\3\2\2\2\u00de\u0645\3\2\2")
        buf.write(u"\2\u00e0\u0647\3\2\2\2\u00e2\u0649\3\2\2\2\u00e4\u065f")
        buf.write(u"\3\2\2\2\u00e6\u0661\3\2\2\2\u00e8\u0668\3\2\2\2\u00ea")
        buf.write(u"\u066f\3\2\2\2\u00ec\u067b\3\2\2\2\u00ee\u0687\3\2\2")
        buf.write(u"\2\u00f0\u0693\3\2\2\2\u00f2\u06ad\3\2\2\2\u00f4\u06bc")
        buf.write(u"\3\2\2\2\u00f6\u06be\3\2\2\2\u00f8\u06cd\3\2\2\2\u00fa")
        buf.write(u"\u06cf\3\2\2\2\u00fc\u06d1\3\2\2\2\u00fe\u06d7\3\2\2")
        buf.write(u"\2\u0100\u06de\3\2\2\2\u0102\u06e0\3\2\2\2\u0104\u06e6")
        buf.write(u"\3\2\2\2\u0106\u06ec\3\2\2\2\u0108\u06f7\3\2\2\2\u010a")
        buf.write(u"\u0702\3\2\2\2\u010c\u070f\3\2\2\2\u010e\u0711\3\2\2")
        buf.write(u"\2\u0110\u0715\3\2\2\2\u0112\u0723\3\2\2\2\u0114\u0725")
        buf.write(u"\3\2\2\2\u0116\u072d\3\2\2\2\u0118\u073e\3\2\2\2\u011a")
        buf.write(u"\u0740\3\2\2\2\u011c\u0743\3\2\2\2\u011e\u0746\3\2\2")
        buf.write(u"\2\u0120\u0749\3\2\2\2\u0122\u074c\3\2\2\2\u0124\u074e")
        buf.write(u"\3\2\2\2\u0126\u0750\3\2\2\2\u0128\u0752\3\2\2\2\u012a")
        buf.write(u"\u0754\3\2\2\2\u012c\u075d\3\2\2\2\u012e\u075f\3\2\2")
        buf.write(u"\2\u0130\u0770\3\2\2\2\u0132\u0772\3\2\2\2\u0134\u0774")
        buf.write(u"\3\2\2\2\u0136\u077c\3\2\2\2\u0138\u077e\3\2\2\2\u013a")
        buf.write(u"\u0785\3\2\2\2\u013c\u0790\3\2\2\2\u013e\u0794\3\2\2")
        buf.write(u"\2\u0140\u0798\3\2\2\2\u0142\u079f\3\2\2\2\u0144\u07a1")
        buf.write(u"\3\2\2\2\u0146\u07a6\3\2\2\2\u0148\u07a8\3\2\2\2\u014a")
        buf.write(u"\u07b6\3\2\2\2\u014c\u07be\3\2\2\2\u014e\u07c0\3\2\2")
        buf.write(u"\2\u0150\u07cd\3\2\2\2\u0152\u07cf\3\2\2\2\u0154\u07da")
        buf.write(u"\3\2\2\2\u0156\u07ea\3\2\2\2\u0158\u07f1\3\2\2\2\u015a")
        buf.write(u"\u0800\3\2\2\2\u015c\u0802\3\2\2\2\u015e\u080b\3\2\2")
        buf.write(u"\2\u0160\u080d\3\2\2\2\u0162\u081c\3\2\2\2\u0164\u081e")
        buf.write(u"\3\2\2\2\u0166\u0820\3\2\2\2\u0168\u0826\3\2\2\2\u016a")
        buf.write(u"\u0828\3\2\2\2\u016c\u082f\3\2\2\2\u016e\u083a\3\2\2")
        buf.write(u"\2\u0170\u083e\3\2\2\2\u0172\u0842\3\2\2\2\u0174\u084d")
        buf.write(u"\3\2\2\2\u0176\u085c\3\2\2\2\u0178\u085e\3\2\2\2\u017a")
        buf.write(u"\u0867\3\2\2\2\u017c\u0869\3\2\2\2\u017e\u0878\3\2\2")
        buf.write(u"\2\u0180\u087a\3\2\2\2\u0182\u087c\3\2\2\2\u0184\u0882")
        buf.write(u"\3\2\2\2\u0186\u0884\3\2\2\2\u0188\u088b\3\2\2\2\u018a")
        buf.write(u"\u0896\3\2\2\2\u018c\u089a\3\2\2\2\u018e\u08a1\3\2\2")
        buf.write(u"\2\u0190\u08b0\3\2\2\2\u0192\u08b2\3\2\2\2\u0194\u0195")
        buf.write(u"\7^\2\2\u0195\u0196\5\u00b4[\2\u0196\u019d\7\26\2\2\u0197")
        buf.write(u"\u019a\5\u00b4[\2\u0198\u0199\7\23\2\2\u0199\u019b\5")
        buf.write(u"\u00dco\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write(u"\u019e\3\2\2\2\u019c\u019e\5\u00dco\2\u019d\u0197\3\2")
        buf.write(u"\2\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0")
        buf.write(u"\7\27\2\2\u01a0\u01a1\7\21\2\2\u01a1\u01a2\5|?\2\u01a2")
        buf.write(u"\u01a3\5\u008eH\2\u01a3\u01a4\5~@\2\u01a4\3\3\2\2\2\u01a5")
        buf.write(u"\u01a6\7^\2\2\u01a6\u01a7\5\u00b4[\2\u01a7\u01a8\7\26")
        buf.write(u"\2\2\u01a8\u01a9\5\u00a0Q\2\u01a9\u01aa\7\27\2\2\u01aa")
        buf.write(u"\u01ab\7\21\2\2\u01ab\u01ac\5|?\2\u01ac\u01ad\5\u008c")
        buf.write(u"G\2\u01ad\u01ae\5~@\2\u01ae\5\3\2\2\2\u01af\u01b0\5\u00b6")
        buf.write(u"\\\2\u01b0\u01b1\7-\2\2\u01b1\u01b2\5V,\2\u01b2\7\3\2")
        buf.write(u"\2\2\u01b3\u01b4\5\u00b6\\\2\u01b4\u01b6\7\26\2\2\u01b5")
        buf.write(u"\u01b7\5f\64\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2")
        buf.write(u"\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\7\27\2\2\u01b9\t\3")
        buf.write(u"\2\2\2\u01ba\u01bc\7\u008b\2\2\u01bb\u01ba\3\2\2\2\u01bb")
        buf.write(u"\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\7J\2\2")
        buf.write(u"\u01be\u01bf\5\u00b2Z\2\u01bf\u01c0\7\26\2\2\u01c0\u01c1")
        buf.write(u"\5\u009cO\2\u01c1\u01c2\7\27\2\2\u01c2\u01c3\7\21\2\2")
        buf.write(u"\u01c3\u01c6\5|?\2\u01c4\u01c7\5\u0092J\2\u01c5\u01c7")
        buf.write(u"\7\177\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write(u"\u01c8\3\2\2\2\u01c8\u01c9\5~@\2\u01c9\13\3\2\2\2\u01ca")
        buf.write(u"\u01cc\7\u008b\2\2\u01cb\u01ca\3\2\2\2\u01cb\u01cc\3")
        buf.write(u"\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\t\2\2\2\u01ce")
        buf.write(u"\u01cf\5\u00b4[\2\u01cf\u01d6\7\26\2\2\u01d0\u01d7\5")
        buf.write(u"\20\t\2\u01d1\u01d7\5\u00dco\2\u01d2\u01d3\5\20\t\2\u01d3")
        buf.write(u"\u01d4\7\23\2\2\u01d4\u01d5\5\u00dco\2\u01d5\u01d7\3")
        buf.write(u"\2\2\2\u01d6\u01d0\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d6")
        buf.write(u"\u01d2\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\7\27\2")
        buf.write(u"\2\u01d9\u01da\7\21\2\2\u01da\u01dd\5|?\2\u01db\u01de")
        buf.write(u"\5\u00c6d\2\u01dc\u01de\7\177\2\2\u01dd\u01db\3\2\2\2")
        buf.write(u"\u01dd\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0")
        buf.write(u"\5~@\2\u01e0\r\3\2\2\2\u01e1\u01e2\7\u0089\2\2\u01e2")
        buf.write(u"\u01e3\5\u00b4[\2\u01e3\u01e4\7\26\2\2\u01e4\u01e5\5")
        buf.write(u"\u00dco\2\u01e5\u01e6\7\27\2\2\u01e6\u01e7\7\21\2\2\u01e7")
        buf.write(u"\u01ea\5|?\2\u01e8\u01eb\5\u00c6d\2\u01e9\u01eb\7\177")
        buf.write(u"\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec")
        buf.write(u"\3\2\2\2\u01ec\u01ed\5~@\2\u01ed\17\3\2\2\2\u01ee\u01ef")
        buf.write(u"\5\u00aaV\2\u01ef\21\3\2\2\2\u01f0\u01f1\7U\2\2\u01f1")
        buf.write(u"\u01f2\7{\2\2\u01f2\u01f3\5\u0118\u008d\2\u01f3\u01f4")
        buf.write(u"\7\26\2\2\u01f4\u01f5\5\u00bc_\2\u01f5\u01f8\7\27\2\2")
        buf.write(u"\u01f6\u01f7\7\63\2\2\u01f7\u01f9\5\u009cO\2\u01f8\u01f6")
        buf.write(u"\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write(u"\u01fb\7\21\2\2\u01fb\u01fc\5|?\2\u01fc\u01fd\5\u00ea")
        buf.write(u"v\2\u01fd\u01fe\5~@\2\u01fe\23\3\2\2\2\u01ff\u0200\7")
        buf.write(u"U\2\2\u0200\u0201\5\u00b0Y\2\u0201\u0202\7\u0088\2\2")
        buf.write(u"\u0202\u0203\7\26\2\2\u0203\u0204\7\27\2\2\u0204\u0205")
        buf.write(u"\7\21\2\2\u0205\u0206\5|?\2\u0206\u0207\5\u00eav\2\u0207")
        buf.write(u"\u0208\5~@\2\u0208\25\3\2\2\2\u0209\u020a\7U\2\2\u020a")
        buf.write(u"\u020c\5\u00b0Y\2\u020b\u020d\7s\2\2\u020c\u020b\3\2")
        buf.write(u"\2\2\u020c\u020d\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f")
        buf.write(u"\7\u0088\2\2\u020f\u0210\7\26\2\2\u0210\u0211\7\27\2")
        buf.write(u"\2\u0211\u0212\7\21\2\2\u0212\u0213\5|?\2\u0213\u0214")
        buf.write(u"\5\u00e2r\2\u0214\u0215\5~@\2\u0215\27\3\2\2\2\u0216")
        buf.write(u"\u0217\7U\2\2\u0217\u0218\5\u00b0Y\2\u0218\u0219\7h\2")
        buf.write(u"\2\u0219\u021a\7\26\2\2\u021a\u021b\7\27\2\2\u021b\u021c")
        buf.write(u"\7\21\2\2\u021c\u021d\5|?\2\u021d\u021e\5\u00eav\2\u021e")
        buf.write(u"\u021f\5~@\2\u021f\31\3\2\2\2\u0220\u0221\7U\2\2\u0221")
        buf.write(u"\u0223\5\u00b0Y\2\u0222\u0224\7s\2\2\u0223\u0222\3\2")
        buf.write(u"\2\2\u0223\u0224\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226")
        buf.write(u"\7h\2\2\u0226\u0227\7\26\2\2\u0227\u0228\7\27\2\2\u0228")
        buf.write(u"\u0229\7\21\2\2\u0229\u022a\5|?\2\u022a\u022b\5\u00e2")
        buf.write(u"r\2\u022b\u022c\5~@\2\u022c\33\3\2\2\2\u022d\u022f\7")
        buf.write(u"\u008b\2\2\u022e\u022d\3\2\2\2\u022e\u022f\3\2\2\2\u022f")
        buf.write(u"\u0230\3\2\2\2\u0230\u0231\7s\2\2\u0231\u0232\t\2\2\2")
        buf.write(u"\u0232\u0233\5\u00b4[\2\u0233\u0235\7\26\2\2\u0234\u0236")
        buf.write(u"\5\u00dco\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write(u"\u0237\3\2\2\2\u0237\u0238\7\27\2\2\u0238\u0239\7\21")
        buf.write(u"\2\2\u0239\u023a\5|?\2\u023a\u023e\5 \21\2\u023b\u023c")
        buf.write(u"\5z>\2\u023c\u023d\5\u00caf\2\u023d\u023f\3\2\2\2\u023e")
        buf.write(u"\u023b\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0240\3\2\2")
        buf.write(u"\2\u0240\u0241\5~@\2\u0241\35\3\2\2\2\u0242\u0243\7s")
        buf.write(u"\2\2\u0243\u0244\7\u0083\2\2\u0244\u0245\5\u00b4[\2\u0245")
        buf.write(u"\u0247\7\26\2\2\u0246\u0248\5\u00dco\2\u0247\u0246\3")
        buf.write(u"\2\2\2\u0247\u0248\3\2\2\2\u0248\u0249\3\2\2\2\u0249")
        buf.write(u"\u024a\7\27\2\2\u024a\u024b\7\21\2\2\u024b\u024c\5|?")
        buf.write(u"\2\u024c\u0250\5 \21\2\u024d\u024e\5z>\2\u024e\u024f")
        buf.write(u"\5\u00caf\2\u024f\u0251\3\2\2\2\u0250\u024d\3\2\2\2\u0250")
        buf.write(u"\u0251\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0253\5~@\2")
        buf.write(u"\u0253\37\3\2\2\2\u0254\u0255\7U\2\2\u0255\u0256\t\2")
        buf.write(u"\2\2\u0256\u0257\7M\2\2\u0257\u0258\7\21\2\2\u0258\u0259")
        buf.write(u"\5|?\2\u0259\u025a\5\"\22\2\u025a\u025b\5~@\2\u025b!")
        buf.write(u"\3\2\2\2\u025c\u025d\b\22\1\2\u025d\u025e\5\u00ceh\2")
        buf.write(u"\u025e\u0265\3\2\2\2\u025f\u0260\f\3\2\2\u0260\u0261")
        buf.write(u"\5z>\2\u0261\u0262\5\u00ceh\2\u0262\u0264\3\2\2\2\u0263")
        buf.write(u"\u025f\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263\3\2\2")
        buf.write(u"\2\u0265\u0266\3\2\2\2\u0266#\3\2\2\2\u0267\u0265\3\2")
        buf.write(u"\2\2\u0268\u0269\7C\2\2\u0269\u026a\7U\2\2\u026a\u026b")
        buf.write(u"\5\u00acW\2\u026b\u026d\7\26\2\2\u026c\u026e\5\u00b8")
        buf.write(u"]\2\u026d\u026c\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026f")
        buf.write(u"\3\2\2\2\u026f\u0272\7\27\2\2\u0270\u0271\7\63\2\2\u0271")
        buf.write(u"\u0273\5\u009cO\2\u0272\u0270\3\2\2\2\u0272\u0273\3\2")
        buf.write(u"\2\2\u0273%\3\2\2\2\u0274\u0275\7U\2\2\u0275\u0276\5")
        buf.write(u"\u00acW\2\u0276\u0278\7\26\2\2\u0277\u0279\5\u00b8]\2")
        buf.write(u"\u0278\u0277\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027a")
        buf.write(u"\3\2\2\2\u027a\u027d\7\27\2\2\u027b\u027c\7\63\2\2\u027c")
        buf.write(u"\u027e\5\u009cO\2\u027d\u027b\3\2\2\2\u027d\u027e\3\2")
        buf.write(u"\2\2\u027e\u027f\3\2\2\2\u027f\u0280\7\21\2\2\u0280\u0281")
        buf.write(u"\5|?\2\u0281\u0282\5\u00eav\2\u0282\u0283\5~@\2\u0283")
        buf.write(u"\'\3\2\2\2\u0284\u0286\7U\2\2\u0285\u0287\7s\2\2\u0286")
        buf.write(u"\u0285\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\3\2\2")
        buf.write(u"\2\u0288\u0289\5\u00acW\2\u0289\u028b\7\26\2\2\u028a")
        buf.write(u"\u028c\5\u00b8]\2\u028b\u028a\3\2\2\2\u028b\u028c\3\2")
        buf.write(u"\2\2\u028c\u028d\3\2\2\2\u028d\u0290\7\27\2\2\u028e\u028f")
        buf.write(u"\7\63\2\2\u028f\u0291\5\u00c2b\2\u0290\u028e\3\2\2\2")
        buf.write(u"\u0290\u0291\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0293")
        buf.write(u"\7\21\2\2\u0293\u0294\5|?\2\u0294\u0295\5\u00e2r\2\u0295")
        buf.write(u"\u0296\5~@\2\u0296)\3\2\2\2\u0297\u0298\7U\2\2\u0298")
        buf.write(u"\u0299\7\u008e\2\2\u0299\u029a\7\u00a2\2\2\u029a\u029b")
        buf.write(u"\7\26\2\2\u029b\u029c\7\27\2\2\u029c\u029d\7\21\2\2\u029d")
        buf.write(u"\u029e\5|?\2\u029e\u029f\5\u00eav\2\u029f\u02a0\5~@\2")
        buf.write(u"\u02a0\u02a1\5z>\2\u02a1\u02a2\7\u0093\2\2\u02a2\u02a8")
        buf.write(u"\7\21\2\2\u02a3\u02a4\5|?\2\u02a4\u02a5\5\u00ecw\2\u02a5")
        buf.write(u"\u02a6\5~@\2\u02a6\u02a9\3\2\2\2\u02a7\u02a9\5\u00b6")
        buf.write(u"\\\2\u02a8\u02a3\3\2\2\2\u02a8\u02a7\3\2\2\2\u02a9+\3")
        buf.write(u"\2\2\2\u02aa\u02ab\5V,\2\u02ab-\3\2\2\2\u02ac\u02ad\5")
        buf.write(u"\u00b0Y\2\u02ad\u02ae\7\21\2\2\u02ae\u02b3\5\u00c2b\2")
        buf.write(u"\u02af\u02b0\7\26\2\2\u02b0\u02b1\5\u00dco\2\u02b1\u02b2")
        buf.write(u"\7\27\2\2\u02b2\u02b4\3\2\2\2\u02b3\u02af\3\2\2\2\u02b3")
        buf.write(u"\u02b4\3\2\2\2\u02b4\u02b7\3\2\2\2\u02b5\u02b6\7-\2\2")
        buf.write(u"\u02b6\u02b8\5\u00fe\u0080\2\u02b7\u02b5\3\2\2\2\u02b7")
        buf.write(u"\u02b8\3\2\2\2\u02b8/\3\2\2\2\u02b9\u02cb\5\64\33\2\u02ba")
        buf.write(u"\u02cb\5r:\2\u02bb\u02cb\5v<\2\u02bc\u02cb\5\62\32\2")
        buf.write(u"\u02bd\u02cb\5T+\2\u02be\u02cb\5J&\2\u02bf\u02cb\5@!")
        buf.write(u"\2\u02c0\u02cb\5D#\2\u02c1\u02cb\5H%\2\u02c2\u02cb\5")
        buf.write(u"F$\2\u02c3\u02cb\5N(\2\u02c4\u02cb\5P)\2\u02c5\u02cb")
        buf.write(u"\5l\67\2\u02c6\u02cb\5<\37\2\u02c7\u02cb\5> \2\u02c8")
        buf.write(u"\u02cb\5&\24\2\u02c9\u02cb\5\u00e0q\2\u02ca\u02b9\3\2")
        buf.write(u"\2\2\u02ca\u02ba\3\2\2\2\u02ca\u02bb\3\2\2\2\u02ca\u02bc")
        buf.write(u"\3\2\2\2\u02ca\u02bd\3\2\2\2\u02ca\u02be\3\2\2\2\u02ca")
        buf.write(u"\u02bf\3\2\2\2\u02ca\u02c0\3\2\2\2\u02ca\u02c1\3\2\2")
        buf.write(u"\2\u02ca\u02c2\3\2\2\2\u02ca\u02c3\3\2\2\2\u02ca\u02c4")
        buf.write(u"\3\2\2\2\u02ca\u02c5\3\2\2\2\u02ca\u02c6\3\2\2\2\u02ca")
        buf.write(u"\u02c7\3\2\2\2\u02ca\u02c8\3\2\2\2\u02ca\u02c9\3\2\2")
        buf.write(u"\2\u02cb\61\3\2\2\2\u02cc\u02cd\7X\2\2\u02cd\u02ce\7")
        buf.write(u"\26\2\2\u02ce\u02cf\5\u0098M\2\u02cf\u02d0\7\27\2\2\u02d0")
        buf.write(u"\u02e1\3\2\2\2\u02d1\u02d2\7\u008c\2\2\u02d2\u02d3\7")
        buf.write(u"\26\2\2\u02d3\u02d4\5\u0098M\2\u02d4\u02d5\7\27\2\2\u02d5")
        buf.write(u"\u02e1\3\2\2\2\u02d6\u02d7\7X\2\2\u02d7\u02d8\7\26\2")
        buf.write(u"\2\u02d8\u02d9\5\u0098M\2\u02d9\u02da\7\27\2\2\u02da")
        buf.write(u"\u02db\7F\2\2\u02db\u02dc\7\u008c\2\2\u02dc\u02dd\7\26")
        buf.write(u"\2\2\u02dd\u02de\5\u0098M\2\u02de\u02df\7\27\2\2\u02df")
        buf.write(u"\u02e1\3\2\2\2\u02e0\u02cc\3\2\2\2\u02e0\u02d1\3\2\2")
        buf.write(u"\2\u02e0\u02d6\3\2\2\2\u02e1\63\3\2\2\2\u02e2\u02e3\5")
        buf.write(u"\66\34\2\u02e3\u02e5\7\26\2\2\u02e4\u02e6\5f\64\2\u02e5")
        buf.write(u"\u02e4\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6\u02e7\3\2\2")
        buf.write(u"\2\u02e7\u02e8\7\27\2\2\u02e8\65\3\2\2\2\u02e9\u02ef")
        buf.write(u"\5\u00acW\2\u02ea\u02eb\58\35\2\u02eb\u02ec\7\25\2\2")
        buf.write(u"\u02ec\u02ed\5\u00acW\2\u02ed\u02ef\3\2\2\2\u02ee\u02e9")
        buf.write(u"\3\2\2\2\u02ee\u02ea\3\2\2\2\u02ef\67\3\2\2\2\u02f0\u02f1")
        buf.write(u"\b\35\1\2\u02f1\u02f2\5\u00aeX\2\u02f2\u02f7\3\2\2\2")
        buf.write(u"\u02f3\u02f4\f\3\2\2\u02f4\u02f6\5:\36\2\u02f5\u02f3")
        buf.write(u"\3\2\2\2\u02f6\u02f9\3\2\2\2\u02f7\u02f5\3\2\2\2\u02f7")
        buf.write(u"\u02f8\3\2\2\2\u02f89\3\2\2\2\u02f9\u02f7\3\2\2\2\u02fa")
        buf.write(u"\u02fb\7\25\2\2\u02fb\u0301\5\u00b0Y\2\u02fc\u02fd\7")
        buf.write(u"\30\2\2\u02fd\u02fe\5V,\2\u02fe\u02ff\7\31\2\2\u02ff")
        buf.write(u"\u0301\3\2\2\2\u0300\u02fa\3\2\2\2\u0300\u02fc\3\2\2")
        buf.write(u"\2\u0301;\3\2\2\2\u0302\u0303\7\u0094\2\2\u0303\u0304")
        buf.write(u"\5\u010e\u0088\2\u0304\u0305\7\21\2\2\u0305\u0306\5|")
        buf.write(u"?\2\u0306\u0307\5\u00eav\2\u0307\u0308\5~@\2\u0308=\3")
        buf.write(u"\2\2\2\u0309\u030a\7\u0094\2\2\u030a\u030b\5\u00b4[\2")
        buf.write(u"\u030b\u030c\7\21\2\2\u030c\u030d\5|?\2\u030d\u030e\5")
        buf.write(u"\u00eav\2\u030e\u030f\5~@\2\u030f?\3\2\2\2\u0310\u0311")
        buf.write(u"\7\u008d\2\2\u0311\u0312\7x\2\2\u0312\u0313\5V,\2\u0313")
        buf.write(u"\u0314\7\21\2\2\u0314\u0315\5|?\2\u0315\u031d\5\u00ee")
        buf.write(u"x\2\u0316\u0317\5z>\2\u0317\u0318\7~\2\2\u0318\u0319")
        buf.write(u"\7\21\2\2\u0319\u031a\5|?\2\u031a\u031b\5\u00eav\2\u031b")
        buf.write(u"\u031c\5~@\2\u031c\u031e\3\2\2\2\u031d\u0316\3\2\2\2")
        buf.write(u"\u031d\u031e\3\2\2\2\u031e\u031f\3\2\2\2\u031f\u0320")
        buf.write(u"\5~@\2\u0320A\3\2\2\2\u0321\u0322\7\u0095\2\2\u0322\u0323")
        buf.write(u"\5\u00f4{\2\u0323\u0324\7\21\2\2\u0324\u0325\5|?\2\u0325")
        buf.write(u"\u0326\5\u00eav\2\u0326\u0327\5~@\2\u0327\u0331\3\2\2")
        buf.write(u"\2\u0328\u0329\7\u0095\2\2\u0329\u032a\7j\2\2\u032a\u032b")
        buf.write(u"\5\u00f2z\2\u032b\u032c\7\21\2\2\u032c\u032d\5|?\2\u032d")
        buf.write(u"\u032e\5\u00eav\2\u032e\u032f\5~@\2\u032f\u0331\3\2\2")
        buf.write(u"\2\u0330\u0321\3\2\2\2\u0330\u0328\3\2\2\2\u0331C\3\2")
        buf.write(u"\2\2\u0332\u0333\7f\2\2\u0333\u0336\5\u00b0Y\2\u0334")
        buf.write(u"\u0335\7\23\2\2\u0335\u0337\5\u00b0Y\2\u0336\u0334\3")
        buf.write(u"\2\2\2\u0336\u0337\3\2\2\2\u0337\u0338\3\2\2\2\u0338")
        buf.write(u"\u0339\7j\2\2\u0339\u033a\5V,\2\u033a\u033b\7\21\2\2")
        buf.write(u"\u033b\u033c\5|?\2\u033c\u033d\5\u00eav\2\u033d\u033e")
        buf.write(u"\5~@\2\u033eE\3\2\2\2\u033f\u0340\7Z\2\2\u0340\u0341")
        buf.write(u"\7\21\2\2\u0341\u0342\5|?\2\u0342\u0343\5\u00eav\2\u0343")
        buf.write(u"\u0344\5~@\2\u0344\u0345\5z>\2\u0345\u0346\7\u0097\2")
        buf.write(u"\2\u0346\u0347\5V,\2\u0347G\3\2\2\2\u0348\u0349\7\u0097")
        buf.write(u"\2\2\u0349\u034a\5V,\2\u034a\u034b\7\21\2\2\u034b\u034c")
        buf.write(u"\5|?\2\u034c\u034d\5\u00eav\2\u034d\u034e\5~@\2\u034e")
        buf.write(u"I\3\2\2\2\u034f\u0350\7i\2\2\u0350\u0351\5V,\2\u0351")
        buf.write(u"\u0352\7\21\2\2\u0352\u0353\5|?\2\u0353\u0354\5\u00ea")
        buf.write(u"v\2\u0354\u0358\5~@\2\u0355\u0356\5z>\2\u0356\u0357\5")
        buf.write(u"L\'\2\u0357\u0359\3\2\2\2\u0358\u0355\3\2\2\2\u0358\u0359")
        buf.write(u"\3\2\2\2\u0359\u0361\3\2\2\2\u035a\u035b\5z>\2\u035b")
        buf.write(u"\u035c\7]\2\2\u035c\u035d\7\21\2\2\u035d\u035e\5|?\2")
        buf.write(u"\u035e\u035f\5\u00eav\2\u035f\u0360\5~@\2\u0360\u0362")
        buf.write(u"\3\2\2\2\u0361\u035a\3\2\2\2\u0361\u0362\3\2\2\2\u0362")
        buf.write(u"K\3\2\2\2\u0363\u0364\b\'\1\2\u0364\u0365\7]\2\2\u0365")
        buf.write(u"\u0366\7i\2\2\u0366\u0367\5V,\2\u0367\u0368\7\21\2\2")
        buf.write(u"\u0368\u0369\5|?\2\u0369\u036a\5\u00eav\2\u036a\u036b")
        buf.write(u"\5~@\2\u036b\u0378\3\2\2\2\u036c\u036d\f\3\2\2\u036d")
        buf.write(u"\u036e\5z>\2\u036e\u036f\7]\2\2\u036f\u0370\7i\2\2\u0370")
        buf.write(u"\u0371\5V,\2\u0371\u0372\7\21\2\2\u0372\u0373\5|?\2\u0373")
        buf.write(u"\u0374\5\u00eav\2\u0374\u0375\5~@\2\u0375\u0377\3\2\2")
        buf.write(u"\2\u0376\u036c\3\2\2\2\u0377\u037a\3\2\2\2\u0378\u0376")
        buf.write(u"\3\2\2\2\u0378\u0379\3\2\2\2\u0379M\3\2\2\2\u037a\u0378")
        buf.write(u"\3\2\2\2\u037b\u037c\7\u0080\2\2\u037c\u037d\5V,\2\u037d")
        buf.write(u"O\3\2\2\2\u037e\u037f\7\u0092\2\2\u037f\u0380\5\u00b0")
        buf.write(u"Y\2\u0380\u0381\7\21\2\2\u0381\u0382\5|?\2\u0382\u0383")
        buf.write(u"\5\u00eav\2\u0383\u0384\5~@\2\u0384\u0386\5x=\2\u0385")
        buf.write(u"\u0387\5\u00f0y\2\u0386\u0385\3\2\2\2\u0386\u0387\3\2")
        buf.write(u"\2\2\u0387\u038f\3\2\2\2\u0388\u0389\7`\2\2\u0389\u038a")
        buf.write(u"\7\21\2\2\u038a\u038b\5|?\2\u038b\u038c\5\u00eav\2\u038c")
        buf.write(u"\u038d\5~@\2\u038d\u038e\5x=\2\u038e\u0390\3\2\2\2\u038f")
        buf.write(u"\u0388\3\2\2\2\u038f\u0390\3\2\2\2\u0390\u0398\3\2\2")
        buf.write(u"\2\u0391\u0392\7e\2\2\u0392\u0393\7\21\2\2\u0393\u0394")
        buf.write(u"\5|?\2\u0394\u0395\5\u00eav\2\u0395\u0396\5~@\2\u0396")
        buf.write(u"\u0397\5x=\2\u0397\u0399\3\2\2\2\u0398\u0391\3\2\2\2")
        buf.write(u"\u0398\u0399\3\2\2\2\u0399\u039a\3\2\2\2\u039a\u039b")
        buf.write(u"\5x=\2\u039bQ\3\2\2\2\u039c\u039d\7`\2\2\u039d\u039e")
        buf.write(u"\5\u00b6\\\2\u039e\u039f\7\21\2\2\u039f\u03a0\5|?\2\u03a0")
        buf.write(u"\u03a1\5\u00eav\2\u03a1\u03a2\5~@\2\u03a2\u03a3\5x=\2")
        buf.write(u"\u03a3\u03b0\3\2\2\2\u03a4\u03a5\7`\2\2\u03a5\u03a6\7")
        buf.write(u"j\2\2\u03a6\u03a7\7\30\2\2\u03a7\u03a8\5\u0090I\2\u03a8")
        buf.write(u"\u03a9\7\31\2\2\u03a9\u03aa\7\21\2\2\u03aa\u03ab\5|?")
        buf.write(u"\2\u03ab\u03ac\5\u00eav\2\u03ac\u03ad\5~@\2\u03ad\u03ae")
        buf.write(u"\5x=\2\u03ae\u03b0\3\2\2\2\u03af\u039c\3\2\2\2\u03af")
        buf.write(u"\u03a4\3\2\2\2\u03b0S\3\2\2\2\u03b1\u03b3\7\u0084\2\2")
        buf.write(u"\u03b2\u03b4\5V,\2\u03b3\u03b2\3\2\2\2\u03b3\u03b4\3")
        buf.write(u"\2\2\2\u03b4U\3\2\2\2\u03b5\u03b6\b,\1\2\u03b6\u03b7")
        buf.write(u"\7#\2\2\u03b7\u03c8\5V,\"\u03b8\u03b9\7u\2\2\u03b9\u03c8")
        buf.write(u"\5V,!\u03ba\u03c8\5Z.\2\u03bb\u03c8\5\\/\2\u03bc\u03bd")
        buf.write(u"\7>\2\2\u03bd\u03be\7\26\2\2\u03be\u03bf\5V,\2\u03bf")
        buf.write(u"\u03c0\7\27\2\2\u03c0\u03c8\3\2\2\2\u03c1\u03c2\7a\2")
        buf.write(u"\2\u03c2\u03c3\7\26\2\2\u03c3\u03c4\5\u00b0Y\2\u03c4")
        buf.write(u"\u03c5\7\27\2\2\u03c5\u03c8\3\2\2\2\u03c6\u03c8\5X-\2")
        buf.write(u"\u03c7\u03b5\3\2\2\2\u03c7\u03b8\3\2\2\2\u03c7\u03ba")
        buf.write(u"\3\2\2\2\u03c7\u03bb\3\2\2\2\u03c7\u03bc\3\2\2\2\u03c7")
        buf.write(u"\u03c1\3\2\2\2\u03c7\u03c6\3\2\2\2\u03c8\u042f\3\2\2")
        buf.write(u"\2\u03c9\u03ca\f \2\2\u03ca\u03cb\5\u0124\u0093\2\u03cb")
        buf.write(u"\u03cc\5V,!\u03cc\u042e\3\2\2\2\u03cd\u03ce\f\37\2\2")
        buf.write(u"\u03ce\u03cf\5\u0126\u0094\2\u03cf\u03d0\5V, \u03d0\u042e")
        buf.write(u"\3\2\2\2\u03d1\u03d2\f\36\2\2\u03d2\u03d3\5\u012a\u0096")
        buf.write(u"\2\u03d3\u03d4\5V,\37\u03d4\u042e\3\2\2\2\u03d5\u03d6")
        buf.write(u"\f\35\2\2\u03d6\u03d7\5\u0128\u0095\2\u03d7\u03d8\5V")
        buf.write(u",\36\u03d8\u042e\3\2\2\2\u03d9\u03da\f\34\2\2\u03da\u03db")
        buf.write(u"\t\3\2\2\u03db\u042e\5V,\35\u03dc\u03dd\f\33\2\2\u03dd")
        buf.write(u"\u03de\7*\2\2\u03de\u042e\5V,\34\u03df\u03e0\f\32\2\2")
        buf.write(u"\u03e0\u03e1\7+\2\2\u03e1\u042e\5V,\33\u03e2\u03e3\f")
        buf.write(u"\31\2\2\u03e3\u03e4\7(\2\2\u03e4\u042e\5V,\32\u03e5\u03e6")
        buf.write(u"\f\30\2\2\u03e6\u03e7\7)\2\2\u03e7\u042e\5V,\31\u03e8")
        buf.write(u"\u03e9\f\25\2\2\u03e9\u03ea\7/\2\2\u03ea\u042e\5V,\26")
        buf.write(u"\u03eb\u03ec\f\24\2\2\u03ec\u03ed\7.\2\2\u03ed\u042e")
        buf.write(u"\5V,\25\u03ee\u03ef\f\23\2\2\u03ef\u03f0\7\60\2\2\u03f0")
        buf.write(u"\u042e\5V,\24\u03f1\u03f2\f\22\2\2\u03f2\u03f3\7|\2\2")
        buf.write(u"\u03f3\u042e\5V,\23\u03f4\u03f5\f\21\2\2\u03f5\u03f6")
        buf.write(u"\7F\2\2\u03f6\u042e\5V,\22\u03f7\u03f8\f\20\2\2\u03f8")
        buf.write(u"\u03f9\7i\2\2\u03f9\u03fa\5V,\2\u03fa\u03fb\7]\2\2\u03fb")
        buf.write(u"\u03fc\5V,\21\u03fc\u042e\3\2\2\2\u03fd\u03fe\f\16\2")
        buf.write(u"\2\u03fe\u03ff\7j\2\2\u03ff\u042e\5V,\17\u0400\u0401")
        buf.write(u"\f\r\2\2\u0401\u0402\7T\2\2\u0402\u042e\5V,\16\u0403")
        buf.write(u"\u0404\f\f\2\2\u0404\u0405\7T\2\2\u0405\u0406\7D\2\2")
        buf.write(u"\u0406\u042e\5V,\r\u0407\u0408\f\13\2\2\u0408\u0409\7")
        buf.write(u"T\2\2\u0409\u040a\7G\2\2\u040a\u042e\5V,\f\u040b\u040c")
        buf.write(u"\f\n\2\2\u040c\u040d\7u\2\2\u040d\u040e\7j\2\2\u040e")
        buf.write(u"\u042e\5V,\13\u040f\u0410\f\t\2\2\u0410\u0411\7u\2\2")
        buf.write(u"\u0411\u0412\7T\2\2\u0412\u042e\5V,\n\u0413\u0414\f\b")
        buf.write(u"\2\2\u0414\u0415\7u\2\2\u0415\u0416\7T\2\2\u0416\u0417")
        buf.write(u"\7D\2\2\u0417\u042e\5V,\t\u0418\u0419\f\7\2\2\u0419\u041a")
        buf.write(u"\7u\2\2\u041a\u041b\7T\2\2\u041b\u041c\7G\2\2\u041c\u042e")
        buf.write(u"\5V,\b\u041d\u041e\f\3\2\2\u041e\u041f\7f\2\2\u041f\u0420")
        buf.write(u"\5\u00b0Y\2\u0420\u0421\7j\2\2\u0421\u0422\5V,\4\u0422")
        buf.write(u"\u042e\3\2\2\2\u0423\u0424\f\27\2\2\u0424\u0425\7m\2")
        buf.write(u"\2\u0425\u0426\7u\2\2\u0426\u042e\5\u0112\u008a\2\u0427")
        buf.write(u"\u0428\f\26\2\2\u0428\u0429\7m\2\2\u0429\u042e\5\u0112")
        buf.write(u"\u008a\2\u042a\u042b\f\17\2\2\u042b\u042c\7H\2\2\u042c")
        buf.write(u"\u042e\5\u00c2b\2\u042d\u03c9\3\2\2\2\u042d\u03cd\3\2")
        buf.write(u"\2\2\u042d\u03d1\3\2\2\2\u042d\u03d5\3\2\2\2\u042d\u03d9")
        buf.write(u"\3\2\2\2\u042d\u03dc\3\2\2\2\u042d\u03df\3\2\2\2\u042d")
        buf.write(u"\u03e2\3\2\2\2\u042d\u03e5\3\2\2\2\u042d\u03e8\3\2\2")
        buf.write(u"\2\u042d\u03eb\3\2\2\2\u042d\u03ee\3\2\2\2\u042d\u03f1")
        buf.write(u"\3\2\2\2\u042d\u03f4\3\2\2\2\u042d\u03f7\3\2\2\2\u042d")
        buf.write(u"\u03fd\3\2\2\2\u042d\u0400\3\2\2\2\u042d\u0403\3\2\2")
        buf.write(u"\2\u042d\u0407\3\2\2\2\u042d\u040b\3\2\2\2\u042d\u040f")
        buf.write(u"\3\2\2\2\u042d\u0413\3\2\2\2\u042d\u0418\3\2\2\2\u042d")
        buf.write(u"\u041d\3\2\2\2\u042d\u0423\3\2\2\2\u042d\u0427\3\2\2")
        buf.write(u"\2\u042d\u042a\3\2\2\2\u042e\u0431\3\2\2\2\u042f\u042d")
        buf.write(u"\3\2\2\2\u042f\u0430\3\2\2\2\u0430W\3\2\2\2\u0431\u042f")
        buf.write(u"\3\2\2\2\u0432\u0433\5\u00b4[\2\u0433Y\3\2\2\2\u0434")
        buf.write(u"\u0435\b.\1\2\u0435\u0436\5\u00f8}\2\u0436\u043b\3\2")
        buf.write(u"\2\2\u0437\u0438\f\3\2\2\u0438\u043a\5^\60\2\u0439\u0437")
        buf.write(u"\3\2\2\2\u043a\u043d\3\2\2\2\u043b\u0439\3\2\2\2\u043b")
        buf.write(u"\u043c\3\2\2\2\u043c[\3\2\2\2\u043d\u043b\3\2\2\2\u043e")
        buf.write(u"\u0446\5`\61\2\u043f\u0446\5b\62\2\u0440\u0446\5n8\2")
        buf.write(u"\u0441\u0446\5j\66\2\u0442\u0446\5p9\2\u0443\u0446\5")
        buf.write(u"\64\33\2\u0444\u0446\5d\63\2\u0445\u043e\3\2\2\2\u0445")
        buf.write(u"\u043f\3\2\2\2\u0445\u0440\3\2\2\2\u0445\u0441\3\2\2")
        buf.write(u"\2\u0445\u0442\3\2\2\2\u0445\u0443\3\2\2\2\u0445\u0444")
        buf.write(u"\3\2\2\2\u0446]\3\2\2\2\u0447\u0448\6\60!\3\u0448\u0449")
        buf.write(u"\7\25\2\2\u0449\u0455\5\u00b0Y\2\u044a\u044b\6\60\"\3")
        buf.write(u"\u044b\u044c\7\30\2\2\u044c\u044d\5\u010c\u0087\2\u044d")
        buf.write(u"\u044e\7\31\2\2\u044e\u0455\3\2\2\2\u044f\u0450\6\60")
        buf.write(u"#\3\u0450\u0451\7\30\2\2\u0451\u0452\5V,\2\u0452\u0453")
        buf.write(u"\7\31\2\2\u0453\u0455\3\2\2\2\u0454\u0447\3\2\2\2\u0454")
        buf.write(u"\u044a\3\2\2\2\u0454\u044f\3\2\2\2\u0455_\3\2\2\2\u0456")
        buf.write(u"\u0457\7@\2\2\u0457\u0459\7\26\2\2\u0458\u045a\5V,\2")
        buf.write(u"\u0459\u0458\3\2\2\2\u0459\u045a\3\2\2\2\u045a\u045b")
        buf.write(u"\3\2\2\2\u045b\u045c\7\27\2\2\u045ca\3\2\2\2\u045d\u045e")
        buf.write(u"\7?\2\2\u045e\u0460\7\26\2\2\u045f\u0461\5V,\2\u0460")
        buf.write(u"\u045f\3\2\2\2\u0460\u0461\3\2\2\2\u0461\u0462\3\2\2")
        buf.write(u"\2\u0462\u0463\7\27\2\2\u0463c\3\2\2\2\u0464\u0465\5")
        buf.write(u"\u00a4S\2\u0465\u0467\7\26\2\2\u0466\u0468\5f\64\2\u0467")
        buf.write(u"\u0466\3\2\2\2\u0467\u0468\3\2\2\2\u0468\u0469\3\2\2")
        buf.write(u"\2\u0469\u046a\7\27\2\2\u046ae\3\2\2\2\u046b\u046c\b")
        buf.write(u"\64\1\2\u046c\u046d\5V,\2\u046d\u046e\6\64$\3\u046e\u0471")
        buf.write(u"\3\2\2\2\u046f\u0471\5h\65\2\u0470\u046b\3\2\2\2\u0470")
        buf.write(u"\u046f\3\2\2\2\u0471\u0477\3\2\2\2\u0472\u0473\f\3\2")
        buf.write(u"\2\u0473\u0474\7\23\2\2\u0474\u0476\5h\65\2\u0475\u0472")
        buf.write(u"\3\2\2\2\u0476\u0479\3\2\2\2\u0477\u0475\3\2\2\2\u0477")
        buf.write(u"\u0478\3\2\2\2\u0478g\3\2\2\2\u0479\u0477\3\2\2\2\u047a")
        buf.write(u"\u047b\5\u00b0Y\2\u047b\u047c\5\u0122\u0092\2\u047c\u047d")
        buf.write(u"\5V,\2\u047di\3\2\2\2\u047e\u047f\7\u0081\2\2\u047f\u0480")
        buf.write(u"\7g\2\2\u0480\u0481\5V,\2\u0481k\3\2\2\2\u0482\u0483")
        buf.write(u"\7\u0098\2\2\u0483\u0484\5V,\2\u0484\u0485\7\u0091\2")
        buf.write(u"\2\u0485\u0486\5V,\2\u0486m\3\2\2\2\u0487\u0488\7d\2")
        buf.write(u"\2\u0488\u0489\5\u00b0Y\2\u0489\u048a\7g\2\2\u048a\u048b")
        buf.write(u"\5V,\2\u048b\u048c\7\u0096\2\2\u048c\u048d\5V,\2\u048d")
        buf.write(u"\u04ad\3\2\2\2\u048e\u048f\7d\2\2\u048f\u0491\7y\2\2")
        buf.write(u"\u0490\u0492\5\u00a4S\2\u0491\u0490\3\2\2\2\u0491\u0492")
        buf.write(u"\3\2\2\2\u0492\u0493\3\2\2\2\u0493\u0494\7\u0096\2\2")
        buf.write(u"\u0494\u04ad\5V,\2\u0495\u049c\7d\2\2\u0496\u049d\7D")
        buf.write(u"\2\2\u0497\u0498\7\u0086\2\2\u0498\u0499\5V,\2\u0499")
        buf.write(u"\u049a\7\u0091\2\2\u049a\u049b\5V,\2\u049b\u049d\3\2")
        buf.write(u"\2\2\u049c\u0496\3\2\2\2\u049c\u0497\3\2\2\2\u049d\u049e")
        buf.write(u"\3\2\2\2\u049e\u04a0\7\26\2\2\u049f\u04a1\5\u00a4S\2")
        buf.write(u"\u04a0\u049f\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1\u04a2")
        buf.write(u"\3\2\2\2\u04a2\u04a5\7\27\2\2\u04a3\u04a4\7\u0096\2\2")
        buf.write(u"\u04a4\u04a6\5V,\2\u04a5\u04a3\3\2\2\2\u04a5\u04a6\3")
        buf.write(u"\2\2\2\u04a6\u04aa\3\2\2\2\u04a7\u04a8\7}\2\2\u04a8\u04a9")
        buf.write(u"\7N\2\2\u04a9\u04ab\5\u0114\u008b\2\u04aa\u04a7\3\2\2")
        buf.write(u"\2\u04aa\u04ab\3\2\2\2\u04ab\u04ad\3\2\2\2\u04ac\u0487")
        buf.write(u"\3\2\2\2\u04ac\u048e\3\2\2\2\u04ac\u0495\3\2\2\2\u04ad")
        buf.write(u"o\3\2\2\2\u04ae\u04af\7\u008a\2\2\u04af\u04b0\7\26\2")
        buf.write(u"\2\u04b0\u04b6\5Z.\2\u04b1\u04b2\7\23\2\2\u04b2\u04b3")
        buf.write(u"\5\u011c\u008f\2\u04b3\u04b4\7-\2\2\u04b4\u04b5\5Z.\2")
        buf.write(u"\u04b5\u04b7\3\2\2\2\u04b6\u04b1\3\2\2\2\u04b6\u04b7")
        buf.write(u"\3\2\2\2\u04b7\u04b8\3\2\2\2\u04b8\u04b9\7\27\2\2\u04b9")
        buf.write(u"q\3\2\2\2\u04ba\u04bb\5\u0110\u0089\2\u04bb\u04bc\5\u0122")
        buf.write(u"\u0092\2\u04bc\u04bd\5V,\2\u04bds\3\2\2\2\u04be\u04bf")
        buf.write(u"\6;&\3\u04bf\u04c0\7\25\2\2\u04c0\u04c7\5\u00b0Y\2\u04c1")
        buf.write(u"\u04c2\6;\'\3\u04c2\u04c3\7\30\2\2\u04c3\u04c4\5V,\2")
        buf.write(u"\u04c4\u04c5\7\31\2\2\u04c5\u04c7\3\2\2\2\u04c6\u04be")
        buf.write(u"\3\2\2\2\u04c6\u04c1\3\2\2\2\u04c7u\3\2\2\2\u04c8\u04c9")
        buf.write(u"\5\u00dan\2\u04c9\u04ca\5\u0122\u0092\2\u04ca\u04cb\5")
        buf.write(u"V,\2\u04cbw\3\2\2\2\u04cc\u04ce\7\7\2\2\u04cd\u04cc\3")
        buf.write(u"\2\2\2\u04ce\u04d1\3\2\2\2\u04cf\u04cd\3\2\2\2\u04cf")
        buf.write(u"\u04d0\3\2\2\2\u04d0y\3\2\2\2\u04d1\u04cf\3\2\2\2\u04d2")
        buf.write(u"\u04d4\7\7\2\2\u04d3\u04d2\3\2\2\2\u04d4\u04d5\3\2\2")
        buf.write(u"\2\u04d5\u04d3\3\2\2\2\u04d5\u04d6\3\2\2\2\u04d6{\3\2")
        buf.write(u"\2\2\u04d7\u04d9\7\7\2\2\u04d8\u04d7\3\2\2\2\u04d9\u04da")
        buf.write(u"\3\2\2\2\u04da\u04d8\3\2\2\2\u04da\u04db\3\2\2\2\u04db")
        buf.write(u"\u04dc\3\2\2\2\u04dc\u04dd\7\3\2\2\u04dd}\3\2\2\2\u04de")
        buf.write(u"\u04e0\7\7\2\2\u04df\u04de\3\2\2\2\u04e0\u04e3\3\2\2")
        buf.write(u"\2\u04e1\u04df\3\2\2\2\u04e1\u04e2\3\2\2\2\u04e2\u04e4")
        buf.write(u"\3\2\2\2\u04e3\u04e1\3\2\2\2\u04e4\u04e5\7\4\2\2\u04e5")
        buf.write(u"\177\3\2\2\2\u04e6\u04e7\7t\2\2\u04e7\u0081\3\2\2\2\u04e8")
        buf.write(u"\u04ea\5\u0084C\2\u04e9\u04e8\3\2\2\2\u04e9\u04ea\3\2")
        buf.write(u"\2\2\u04ea\u04eb\3\2\2\2\u04eb\u04ec\5x=\2\u04ec\u04ed")
        buf.write(u"\7\2\2\3\u04ed\u0083\3\2\2\2\u04ee\u04ef\bC\1\2\u04ef")
        buf.write(u"\u04f0\5\u0086D\2\u04f0\u04f7\3\2\2\2\u04f1\u04f2\f\3")
        buf.write(u"\2\2\u04f2\u04f3\5z>\2\u04f3\u04f4\5\u0086D\2\u04f4\u04f6")
        buf.write(u"\3\2\2\2\u04f5\u04f1\3\2\2\2\u04f6\u04f9\3\2\2\2\u04f7")
        buf.write(u"\u04f5\3\2\2\2\u04f7\u04f8\3\2\2\2\u04f8\u0085\3\2\2")
        buf.write(u"\2\u04f9\u04f7\3\2\2\2\u04fa\u04fb\5\u00e0q\2\u04fb\u04fc")
        buf.write(u"\5z>\2\u04fc\u04fe\3\2\2\2\u04fd\u04fa\3\2\2\2\u04fe")
        buf.write(u"\u0501\3\2\2\2\u04ff\u04fd\3\2\2\2\u04ff\u0500\3\2\2")
        buf.write(u"\2\u0500\u0507\3\2\2\2\u0501\u04ff\3\2\2\2\u0502\u0508")
        buf.write(u"\5\n\6\2\u0503\u0508\5\u00a8U\2\u0504\u0508\5\u0088E")
        buf.write(u"\2\u0505\u0508\5\u008aF\2\u0506\u0508\5\u00dep\2\u0507")
        buf.write(u"\u0502\3\2\2\2\u0507\u0503\3\2\2\2\u0507\u0504\3\2\2")
        buf.write(u"\2\u0507\u0505\3\2\2\2\u0507\u0506\3\2\2\2\u0508\u0087")
        buf.write(u"\3\2\2\2\u0509\u050a\5\36\20\2\u050a\u0089\3\2\2\2\u050b")
        buf.write(u"\u050e\5\2\2\2\u050c\u050e\5\4\3\2\u050d\u050b\3\2\2")
        buf.write(u"\2\u050d\u050c\3\2\2\2\u050e\u008b\3\2\2\2\u050f\u0510")
        buf.write(u"\bG\1\2\u0510\u0511\5\6\4\2\u0511\u0518\3\2\2\2\u0512")
        buf.write(u"\u0513\f\3\2\2\u0513\u0514\5z>\2\u0514\u0515\5\6\4\2")
        buf.write(u"\u0515\u0517\3\2\2\2\u0516\u0512\3\2\2\2\u0517\u051a")
        buf.write(u"\3\2\2\2\u0518\u0516\3\2\2\2\u0518\u0519\3\2\2\2\u0519")
        buf.write(u"\u008d\3\2\2\2\u051a\u0518\3\2\2\2\u051b\u051c\bH\1\2")
        buf.write(u"\u051c\u051d\5\b\5\2\u051d\u0524\3\2\2\2\u051e\u051f")
        buf.write(u"\f\3\2\2\u051f\u0520\5z>\2\u0520\u0521\5\b\5\2\u0521")
        buf.write(u"\u0523\3\2\2\2\u0522\u051e\3\2\2\2\u0523\u0526\3\2\2")
        buf.write(u"\2\u0524\u0522\3\2\2\2\u0524\u0525\3\2\2\2\u0525\u008f")
        buf.write(u"\3\2\2\2\u0526\u0524\3\2\2\2\u0527\u0528\bI\1\2\u0528")
        buf.write(u"\u0529\5\u00b6\\\2\u0529\u052f\3\2\2\2\u052a\u052b\f")
        buf.write(u"\3\2\2\u052b\u052c\7\23\2\2\u052c\u052e\5\u00b6\\\2\u052d")
        buf.write(u"\u052a\3\2\2\2\u052e\u0531\3\2\2\2\u052f\u052d\3\2\2")
        buf.write(u"\2\u052f\u0530\3\2\2\2\u0530\u0091\3\2\2\2\u0531\u052f")
        buf.write(u"\3\2\2\2\u0532\u0533\7j\2\2\u0533\u053d\5\u0094K\2\u0534")
        buf.write(u"\u0535\7j\2\2\u0535\u053d\5\u0096L\2\u0536\u0537\7j\2")
        buf.write(u"\2\u0537\u053d\5\u009aN\2\u0538\u0539\7n\2\2\u0539\u053d")
        buf.write(u"\7\u00a2\2\2\u053a\u053b\7n\2\2\u053b\u053d\5V,\2\u053c")
        buf.write(u"\u0532\3\2\2\2\u053c\u0534\3\2\2\2\u053c\u0536\3\2\2")
        buf.write(u"\2\u053c\u0538\3\2\2\2\u053c\u053a\3\2\2\2\u053d\u0093")
        buf.write(u"\3\2\2\2\u053e\u0540\7\30\2\2\u053f\u0541\5\u0098M\2")
        buf.write(u"\u0540\u053f\3\2\2\2\u0540\u0541\3\2\2\2\u0541\u0542")
        buf.write(u"\3\2\2\2\u0542\u0543\7\31\2\2\u0543\u0095\3\2\2\2\u0544")
        buf.write(u"\u0546\7*\2\2\u0545\u0547\5\u0098M\2\u0546\u0545\3\2")
        buf.write(u"\2\2\u0546\u0547\3\2\2\2\u0547\u0548\3\2\2\2\u0548\u0549")
        buf.write(u"\7(\2\2\u0549\u0097\3\2\2\2\u054a\u054b\bM\1\2\u054b")
        buf.write(u"\u054c\5V,\2\u054c\u0552\3\2\2\2\u054d\u054e\f\3\2\2")
        buf.write(u"\u054e\u054f\7\23\2\2\u054f\u0551\5V,\2\u0550\u054d\3")
        buf.write(u"\2\2\2\u0551\u0554\3\2\2\2\u0552\u0550\3\2\2\2\u0552")
        buf.write(u"\u0553\3\2\2\2\u0553\u0099\3\2\2\2\u0554\u0552\3\2\2")
        buf.write(u"\2\u0555\u0556\7\30\2\2\u0556\u0557\5V,\2\u0557\u0558")
        buf.write(u"\7\24\2\2\u0558\u0559\5V,\2\u0559\u055a\7\31\2\2\u055a")
        buf.write(u"\u009b\3\2\2\2\u055b\u055c\bO\1\2\u055c\u055d\5\u009e")
        buf.write(u"P\2\u055d\u0568\3\2\2\2\u055e\u055f\f\5\2\2\u055f\u0567")
        buf.write(u"\7,\2\2\u0560\u0561\f\4\2\2\u0561\u0562\7\30\2\2\u0562")
        buf.write(u"\u0567\7\31\2\2\u0563\u0564\f\3\2\2\u0564\u0565\7\32")
        buf.write(u"\2\2\u0565\u0567\7\33\2\2\u0566\u055e\3\2\2\2\u0566\u0560")
        buf.write(u"\3\2\2\2\u0566\u0563\3\2\2\2\u0567\u056a\3\2\2\2\u0568")
        buf.write(u"\u0566\3\2\2\2\u0568\u0569\3\2\2\2\u0569\u009d\3\2\2")
        buf.write(u"\2\u056a\u0568\3\2\2\2\u056b\u056e\5\u00a0Q\2\u056c\u056e")
        buf.write(u"\5\u00a2R\2\u056d\u056b\3\2\2\2\u056d\u056c\3\2\2\2\u056e")
        buf.write(u"\u009f\3\2\2\2\u056f\u057e\7\64\2\2\u0570\u057e\7\65")
        buf.write(u"\2\2\u0571\u057e\7\66\2\2\u0572\u057e\7A\2\2\u0573\u057e")
        buf.write(u"\7\67\2\2\u0574\u057e\78\2\2\u0575\u057e\7?\2\2\u0576")
        buf.write(u"\u057e\79\2\2\u0577\u057e\7;\2\2\u0578\u057e\7:\2\2\u0579")
        buf.write(u"\u057e\7<\2\2\u057a\u057e\7>\2\2\u057b\u057e\7@\2\2\u057c")
        buf.write(u"\u057e\7B\2\2\u057d\u056f\3\2\2\2\u057d\u0570\3\2\2\2")
        buf.write(u"\u057d\u0571\3\2\2\2\u057d\u0572\3\2\2\2\u057d\u0573")
        buf.write(u"\3\2\2\2\u057d\u0574\3\2\2\2\u057d\u0575\3\2\2\2\u057d")
        buf.write(u"\u0576\3\2\2\2\u057d\u0577\3\2\2\2\u057d\u0578\3\2\2")
        buf.write(u"\2\u057d\u0579\3\2\2\2\u057d\u057a\3\2\2\2\u057d\u057b")
        buf.write(u"\3\2\2\2\u057d\u057c\3\2\2\2\u057e\u00a1\3\2\2\2\u057f")
        buf.write(u"\u0580\7\u009e\2\2\u0580\u00a3\3\2\2\2\u0581\u0583\7")
        buf.write(u"r\2\2\u0582\u0581\3\2\2\2\u0582\u0583\3\2\2\2\u0583\u0584")
        buf.write(u"\3\2\2\2\u0584\u0585\5\u00a2R\2\u0585\u00a5\3\2\2\2\u0586")
        buf.write(u"\u0587\7>\2\2\u0587\u00a7\3\2\2\2\u0588\u058c\5\f\7\2")
        buf.write(u"\u0589\u058c\5\34\17\2\u058a\u058c\5\16\b\2\u058b\u0588")
        buf.write(u"\3\2\2\2\u058b\u0589\3\2\2\2\u058b\u058a\3\2\2\2\u058c")
        buf.write(u"\u00a9\3\2\2\2\u058d\u058e\bV\1\2\u058e\u058f\5\u00b4")
        buf.write(u"[\2\u058f\u0595\3\2\2\2\u0590\u0591\f\3\2\2\u0591\u0592")
        buf.write(u"\7\23\2\2\u0592\u0594\5\u00b4[\2\u0593\u0590\3\2\2\2")
        buf.write(u"\u0594\u0597\3\2\2\2\u0595\u0593\3\2\2\2\u0595\u0596")
        buf.write(u"\3\2\2\2\u0596\u00ab\3\2\2\2\u0597\u0595\3\2\2\2\u0598")
        buf.write(u"\u059b\5\u00b0Y\2\u0599\u059b\5\u00b4[\2\u059a\u0598")
        buf.write(u"\3\2\2\2\u059a\u0599\3\2\2\2\u059b\u00ad\3\2\2\2\u059c")
        buf.write(u"\u05a0\5\u00b0Y\2\u059d\u05a0\5\u00b4[\2\u059e\u05a0")
        buf.write(u"\5\u00b6\\\2\u059f\u059c\3\2\2\2\u059f\u059d\3\2\2\2")
        buf.write(u"\u059f\u059e\3\2\2\2\u05a0\u00af\3\2\2\2\u05a1\u05a2")
        buf.write(u"\7\u009f\2\2\u05a2\u00b1\3\2\2\2\u05a3\u05a4\t\4\2\2")
        buf.write(u"\u05a4\u00b3\3\2\2\2\u05a5\u05a6\7\u009e\2\2\u05a6\u00b5")
        buf.write(u"\3\2\2\2\u05a7\u05a8\7\u009d\2\2\u05a8\u00b7\3\2\2\2")
        buf.write(u"\u05a9\u05aa\b]\1\2\u05aa\u05ab\5\u00ba^\2\u05ab\u05b1")
        buf.write(u"\3\2\2\2\u05ac\u05ad\f\3\2\2\u05ad\u05ae\7\23\2\2\u05ae")
        buf.write(u"\u05b0\5\u00ba^\2\u05af\u05ac\3\2\2\2\u05b0\u05b3\3\2")
        buf.write(u"\2\2\u05b1\u05af\3\2\2\2\u05b1\u05b2\3\2\2\2\u05b2\u00b9")
        buf.write(u"\3\2\2\2\u05b3\u05b1\3\2\2\2\u05b4\u05ba\5\u00c0a\2\u05b5")
        buf.write(u"\u05b7\7r\2\2\u05b6\u05b5\3\2\2\2\u05b6\u05b7\3\2\2\2")
        buf.write(u"\u05b7\u05b8\3\2\2\2\u05b8\u05ba\5\u00bc_\2\u05b9\u05b4")
        buf.write(u"\3\2\2\2\u05b9\u05b6\3\2\2\2\u05ba\u00bb\3\2\2\2\u05bb")
        buf.write(u"\u05be\5\u00be`\2\u05bc\u05be\5.\30\2\u05bd\u05bb\3\2")
        buf.write(u"\2\2\u05bd\u05bc\3\2\2\2\u05be\u00bd\3\2\2\2\u05bf\u05c2")
        buf.write(u"\5\u00b0Y\2\u05c0\u05c1\7-\2\2\u05c1\u05c3\5\u00fe\u0080")
        buf.write(u"\2\u05c2\u05c0\3\2\2\2\u05c2\u05c3\3\2\2\2\u05c3\u00bf")
        buf.write(u"\3\2\2\2\u05c4\u05c5\5\u00a6T\2\u05c5\u05c6\5\u00b0Y")
        buf.write(u"\2\u05c6\u00c1\3\2\2\2\u05c7\u05ca\5\u009cO\2\u05c8\u05ca")
        buf.write(u"\5\u00c4c\2\u05c9\u05c7\3\2\2\2\u05c9\u05c8\3\2\2\2\u05ca")
        buf.write(u"\u00c3\3\2\2\2\u05cb\u05cc\bc\1\2\u05cc\u05cd\7G\2\2")
        buf.write(u"\u05cd\u05d6\3\2\2\2\u05ce\u05cf\f\4\2\2\u05cf\u05d0")
        buf.write(u"\7\30\2\2\u05d0\u05d5\7\31\2\2\u05d1\u05d2\f\3\2\2\u05d2")
        buf.write(u"\u05d3\7\32\2\2\u05d3\u05d5\7\33\2\2\u05d4\u05ce\3\2")
        buf.write(u"\2\2\u05d4\u05d1\3\2\2\2\u05d5\u05d8\3\2\2\2\u05d6\u05d4")
        buf.write(u"\3\2\2\2\u05d6\u05d7\3\2\2\2\u05d7\u00c5\3\2\2\2\u05d8")
        buf.write(u"\u05d6\3\2\2\2\u05d9\u05da\bd\1\2\u05da\u05db\5\u00c8")
        buf.write(u"e\2\u05db\u05e2\3\2\2\2\u05dc\u05dd\f\3\2\2\u05dd\u05de")
        buf.write(u"\5z>\2\u05de\u05df\5\u00c8e\2\u05df\u05e1\3\2\2\2\u05e0")
        buf.write(u"\u05dc\3\2\2\2\u05e1\u05e4\3\2\2\2\u05e2\u05e0\3\2\2")
        buf.write(u"\2\u05e2\u05e3\3\2\2\2\u05e3\u00c7\3\2\2\2\u05e4\u05e2")
        buf.write(u"\3\2\2\2\u05e5\u05eb\5\24\13\2\u05e6\u05eb\5\30\r\2\u05e7")
        buf.write(u"\u05eb\5&\24\2\u05e8\u05eb\5$\23\2\u05e9\u05eb\5\22\n")
        buf.write(u"\2\u05ea\u05e5\3\2\2\2\u05ea\u05e6\3\2\2\2\u05ea\u05e7")
        buf.write(u"\3\2\2\2\u05ea\u05e8\3\2\2\2\u05ea\u05e9\3\2\2\2\u05eb")
        buf.write(u"\u00c9\3\2\2\2\u05ec\u05ed\bf\1\2\u05ed\u05ee\5\u00cc")
        buf.write(u"g\2\u05ee\u05f5\3\2\2\2\u05ef\u05f0\f\3\2\2\u05f0\u05f1")
        buf.write(u"\5z>\2\u05f1\u05f2\5\u00ccg\2\u05f2\u05f4\3\2\2\2\u05f3")
        buf.write(u"\u05ef\3\2\2\2\u05f4\u05f7\3\2\2\2\u05f5\u05f3\3\2\2")
        buf.write(u"\2\u05f5\u05f6\3\2\2\2\u05f6\u00cb\3\2\2\2\u05f7\u05f5")
        buf.write(u"\3\2\2\2\u05f8\u05fc\5\32\16\2\u05f9\u05fc\5\26\f\2\u05fa")
        buf.write(u"\u05fc\5(\25\2\u05fb\u05f8\3\2\2\2\u05fb\u05f9\3\2\2")
        buf.write(u"\2\u05fb\u05fa\3\2\2\2\u05fc\u00cd\3\2\2\2\u05fd\u05fe")
        buf.write(u"\7\13\2\2\u05fe\u0608\5\u0174\u00bb\2\u05ff\u0600\7\f")
        buf.write(u"\2\2\u0600\u0608\5\u018e\u00c8\2\u0601\u0602\7\r\2\2")
        buf.write(u"\u0602\u0608\5\u00d0i\2\u0603\u0604\7\16\2\2\u0604\u0608")
        buf.write(u"\5\u00d0i\2\u0605\u0606\7\17\2\2\u0606\u0608\5\u00d6")
        buf.write(u"l\2\u0607\u05fd\3\2\2\2\u0607\u05ff\3\2\2\2\u0607\u0601")
        buf.write(u"\3\2\2\2\u0607\u0603\3\2\2\2\u0607\u0605\3\2\2\2\u0608")
        buf.write(u"\u00cf\3\2\2\2\u0609\u060b\5\u00aeX\2\u060a\u060c\5\u00d2")
        buf.write(u"j\2\u060b\u060a\3\2\2\2\u060b\u060c\3\2\2\2\u060c\u00d1")
        buf.write(u"\3\2\2\2\u060d\u060e\7g\2\2\u060e\u060f\5\u00d4k\2\u060f")
        buf.write(u"\u0610\7\21\2\2\u0610\u0615\5\u00aeX\2\u0611\u0612\7")
        buf.write(u"\25\2\2\u0612\u0614\5\u00aeX\2\u0613\u0611\3\2\2\2\u0614")
        buf.write(u"\u0617\3\2\2\2\u0615\u0613\3\2\2\2\u0615\u0616\3\2\2")
        buf.write(u"\2\u0616\u00d3\3\2\2\2\u0617\u0615\3\2\2\2\u0618\u0619")
        buf.write(u"\7\u009f\2\2\u0619\u061a\6k\66\3\u061a\u00d5\3\2\2\2")
        buf.write(u"\u061b\u061d\5\u00aeX\2\u061c\u061e\5\u00d8m\2\u061d")
        buf.write(u"\u061c\3\2\2\2\u061d\u061e\3\2\2\2\u061e\u00d7\3\2\2")
        buf.write(u"\2\u061f\u0620\7g\2\2\u0620\u0621\5\u00d4k\2\u0621\u0623")
        buf.write(u"\7\21\2\2\u0622\u0624\7%\2\2\u0623\u0622\3\2\2\2\u0623")
        buf.write(u"\u0624\3\2\2\2\u0624\u0625\3\2\2\2\u0625\u062a\5\u0144")
        buf.write(u"\u00a3\2\u0626\u0627\7%\2\2\u0627\u0629\5\u0144\u00a3")
        buf.write(u"\2\u0628\u0626\3\2\2\2\u0629\u062c\3\2\2\2\u062a\u0628")
        buf.write(u"\3\2\2\2\u062a\u062b\3\2\2\2\u062b\u062f\3\2\2\2\u062c")
        buf.write(u"\u062a\3\2\2\2\u062d\u062e\7\25\2\2\u062e\u0630\5\u0144")
        buf.write(u"\u00a3\2\u062f\u062d\3\2\2\2\u062f\u0630\3\2\2\2\u0630")
        buf.write(u"\u00d9\3\2\2\2\u0631\u0636\5\u00b0Y\2\u0632\u0633\7\23")
        buf.write(u"\2\2\u0633\u0635\5\u00b0Y\2\u0634\u0632\3\2\2\2\u0635")
        buf.write(u"\u0638\3\2\2\2\u0636\u0634\3\2\2\2\u0636\u0637\3\2\2")
        buf.write(u"\2\u0637\u00db\3\2\2\2\u0638\u0636\3\2\2\2\u0639\u063e")
        buf.write(u"\5\u00b2Z\2\u063a\u063b\7\23\2\2\u063b\u063d\5\u00b2")
        buf.write(u"Z\2\u063c\u063a\3\2\2\2\u063d\u0640\3\2\2\2\u063e\u063c")
        buf.write(u"\3\2\2\2\u063e\u063f\3\2\2\2\u063f\u00dd\3\2\2\2\u0640")
        buf.write(u"\u063e\3\2\2\2\u0641\u0646\5$\23\2\u0642\u0646\5&\24")
        buf.write(u"\2\u0643\u0646\5(\25\2\u0644\u0646\5*\26\2\u0645\u0641")
        buf.write(u"\3\2\2\2\u0645\u0642\3\2\2\2\u0645\u0643\3\2\2\2\u0645")
        buf.write(u"\u0644\3\2\2\2\u0646\u00df\3\2\2\2\u0647\u0648\7\n\2")
        buf.write(u"\2\u0648\u00e1\3\2\2\2\u0649\u064a\br\1\2\u064a\u064b")
        buf.write(u"\5\u00e4s\2\u064b\u0652\3\2\2\2\u064c\u064d\f\3\2\2\u064d")
        buf.write(u"\u064e\5z>\2\u064e\u064f\5\u00e4s\2\u064f\u0651\3\2\2")
        buf.write(u"\2\u0650\u064c\3\2\2\2\u0651\u0654\3\2\2\2\u0652\u0650")
        buf.write(u"\3\2\2\2\u0652\u0653\3\2\2\2\u0653\u00e3\3\2\2\2\u0654")
        buf.write(u"\u0652\3\2\2\2\u0655\u0656\7\13\2\2\u0656\u0660\5\u015e")
        buf.write(u"\u00b0\2\u0657\u0658\7\f\2\2\u0658\u0660\5\u017a\u00be")
        buf.write(u"\2\u0659\u065a\7\r\2\2\u065a\u0660\5\u00e6t\2\u065b\u065c")
        buf.write(u"\7\16\2\2\u065c\u0660\5\u00e6t\2\u065d\u065e\7\17\2\2")
        buf.write(u"\u065e\u0660\5\u00e8u\2\u065f\u0655\3\2\2\2\u065f\u0657")
        buf.write(u"\3\2\2\2\u065f\u0659\3\2\2\2\u065f\u065b\3\2\2\2\u065f")
        buf.write(u"\u065d\3\2\2\2\u0660\u00e5\3\2\2\2\u0661\u0663\5\u0146")
        buf.write(u"\u00a4\2\u0662\u0664\7\22\2\2\u0663\u0662\3\2\2\2\u0663")
        buf.write(u"\u0664\3\2\2\2\u0664\u0666\3\2\2\2\u0665\u0667\5\u00d2")
        buf.write(u"j\2\u0666\u0665\3\2\2\2\u0666\u0667\3\2\2\2\u0667\u00e7")
        buf.write(u"\3\2\2\2\u0668\u066a\5\u012c\u0097\2\u0669\u066b\7\22")
        buf.write(u"\2\2\u066a\u0669\3\2\2\2\u066a\u066b\3\2\2\2\u066b\u066d")
        buf.write(u"\3\2\2\2\u066c\u066e\5\u00d8m\2\u066d\u066c\3\2\2\2\u066d")
        buf.write(u"\u066e\3\2\2\2\u066e\u00e9\3\2\2\2\u066f\u0670\bv\1\2")
        buf.write(u"\u0670\u0671\5\60\31\2\u0671\u0678\3\2\2\2\u0672\u0673")
        buf.write(u"\f\3\2\2\u0673\u0674\5z>\2\u0674\u0675\5\60\31\2\u0675")
        buf.write(u"\u0677\3\2\2\2\u0676\u0672\3\2\2\2\u0677\u067a\3\2\2")
        buf.write(u"\2\u0678\u0676\3\2\2\2\u0678\u0679\3\2\2\2\u0679\u00eb")
        buf.write(u"\3\2\2\2\u067a\u0678\3\2\2\2\u067b\u067c\bw\1\2\u067c")
        buf.write(u"\u067d\5,\27\2\u067d\u0684\3\2\2\2\u067e\u067f\f\3\2")
        buf.write(u"\2\u067f\u0680\5z>\2\u0680\u0681\5,\27\2\u0681\u0683")
        buf.write(u"\3\2\2\2\u0682\u067e\3\2\2\2\u0683\u0686\3\2\2\2\u0684")
        buf.write(u"\u0682\3\2\2\2\u0684\u0685\3\2\2\2\u0685\u00ed\3\2\2")
        buf.write(u"\2\u0686\u0684\3\2\2\2\u0687\u0688\bx\1\2\u0688\u0689")
        buf.write(u"\5B\"\2\u0689\u0690\3\2\2\2\u068a\u068b\f\3\2\2\u068b")
        buf.write(u"\u068c\5z>\2\u068c\u068d\5B\"\2\u068d\u068f\3\2\2\2\u068e")
        buf.write(u"\u068a\3\2\2\2\u068f\u0692\3\2\2\2\u0690\u068e\3\2\2")
        buf.write(u"\2\u0690\u0691\3\2\2\2\u0691\u00ef\3\2\2\2\u0692\u0690")
        buf.write(u"\3\2\2\2\u0693\u0694\by\1\2\u0694\u0695\5R*\2\u0695\u069c")
        buf.write(u"\3\2\2\2\u0696\u0697\f\3\2\2\u0697\u0698\5z>\2\u0698")
        buf.write(u"\u0699\5R*\2\u0699\u069b\3\2\2\2\u069a\u0696\3\2\2\2")
        buf.write(u"\u069b\u069e\3\2\2\2\u069c\u069a\3\2\2\2\u069c\u069d")
        buf.write(u"\3\2\2\2\u069d\u00f1\3\2\2\2\u069e\u069c\3\2\2\2\u069f")
        buf.write(u"\u06a0\7\30\2\2\u06a0\u06a1\5\u00f4{\2\u06a1\u06a2\7")
        buf.write(u"\24\2\2\u06a2\u06a3\5\u00f4{\2\u06a3\u06a4\7\31\2\2\u06a4")
        buf.write(u"\u06ae\3\2\2\2\u06a5\u06a6\7\30\2\2\u06a6\u06a7\5\u00f6")
        buf.write(u"|\2\u06a7\u06a8\7\31\2\2\u06a8\u06ae\3\2\2\2\u06a9\u06aa")
        buf.write(u"\7*\2\2\u06aa\u06ab\5\u00f6|\2\u06ab\u06ac\7(\2\2\u06ac")
        buf.write(u"\u06ae\3\2\2\2\u06ad\u069f\3\2\2\2\u06ad\u06a5\3\2\2")
        buf.write(u"\2\u06ad\u06a9\3\2\2\2\u06ae\u00f3\3\2\2\2\u06af\u06bd")
        buf.write(u"\7\u009b\2\2\u06b0\u06bd\7\u009c\2\2\u06b1\u06bd\7\u00a3")
        buf.write(u"\2\2\u06b2\u06bd\7\u00a4\2\2\u06b3\u06bd\7\u009a\2\2")
        buf.write(u"\u06b4\u06bd\7\u00a8\2\2\u06b5\u06bd\7\u00a7\2\2\u06b6")
        buf.write(u"\u06bd\7\u00a2\2\2\u06b7\u06bd\7\u00a5\2\2\u06b8\u06bd")
        buf.write(u"\7\u00a6\2\2\u06b9\u06bd\7\u0099\2\2\u06ba\u06bd\7\u00a9")
        buf.write(u"\2\2\u06bb\u06bd\5\u0080A\2\u06bc\u06af\3\2\2\2\u06bc")
        buf.write(u"\u06b0\3\2\2\2\u06bc\u06b1\3\2\2\2\u06bc\u06b2\3\2\2")
        buf.write(u"\2\u06bc\u06b3\3\2\2\2\u06bc\u06b4\3\2\2\2\u06bc\u06b5")
        buf.write(u"\3\2\2\2\u06bc\u06b6\3\2\2\2\u06bc\u06b7\3\2\2\2\u06bc")
        buf.write(u"\u06b8\3\2\2\2\u06bc\u06b9\3\2\2\2\u06bc\u06ba\3\2\2")
        buf.write(u"\2\u06bc\u06bb\3\2\2\2\u06bd\u00f5\3\2\2\2\u06be\u06bf")
        buf.write(u"\b|\1\2\u06bf\u06c0\5\u00f4{\2\u06c0\u06c6\3\2\2\2\u06c1")
        buf.write(u"\u06c2\f\3\2\2\u06c2\u06c3\7\23\2\2\u06c3\u06c5\5\u00f4")
        buf.write(u"{\2\u06c4\u06c1\3\2\2\2\u06c5\u06c8\3\2\2\2\u06c6\u06c4")
        buf.write(u"\3\2\2\2\u06c6\u06c7\3\2\2\2\u06c7\u00f7\3\2\2\2\u06c8")
        buf.write(u"\u06c6\3\2\2\2\u06c9\u06ce\5\u00fc\177\2\u06ca\u06ce")
        buf.write(u"\5\u00fe\u0080\2\u06cb\u06ce\5\u00aeX\2\u06cc\u06ce\5")
        buf.write(u"\u00fa~\2\u06cd\u06c9\3\2\2\2\u06cd\u06ca\3\2\2\2\u06cd")
        buf.write(u"\u06cb\3\2\2\2\u06cd\u06cc\3\2\2\2\u06ce\u00f9\3\2\2")
        buf.write(u"\2\u06cf\u06d0\t\5\2\2\u06d0\u00fb\3\2\2\2\u06d1\u06d2")
        buf.write(u"\7\26\2\2\u06d2\u06d3\5V,\2\u06d3\u06d4\7\27\2\2\u06d4")
        buf.write(u"\u00fd\3\2\2\2\u06d5\u06d8\5\u00f4{\2\u06d6\u06d8\5\u0100")
        buf.write(u"\u0081\2\u06d7\u06d5\3\2\2\2\u06d7\u06d6\3\2\2\2\u06d8")
        buf.write(u"\u00ff\3\2\2\2\u06d9\u06df\5\u009aN\2\u06da\u06df\5\u0094")
        buf.write(u"K\2\u06db\u06df\5\u0096L\2\u06dc\u06df\5\u0104\u0083")
        buf.write(u"\2\u06dd\u06df\5\u0102\u0082\2\u06de\u06d9\3\2\2\2\u06de")
        buf.write(u"\u06da\3\2\2\2\u06de\u06db\3\2\2\2\u06de\u06dc\3\2\2")
        buf.write(u"\2\u06de\u06dd\3\2\2\2\u06df\u0101\3\2\2\2\u06e0\u06e2")
        buf.write(u"\7\26\2\2\u06e1\u06e3\5\u0106\u0084\2\u06e2\u06e1\3\2")
        buf.write(u"\2\2\u06e2\u06e3\3\2\2\2\u06e3\u06e4\3\2\2\2\u06e4\u06e5")
        buf.write(u"\7\27\2\2\u06e5\u0103\3\2\2\2\u06e6\u06e8\7\32\2\2\u06e7")
        buf.write(u"\u06e9\5\u0108\u0085\2\u06e8\u06e7\3\2\2\2\u06e8\u06e9")
        buf.write(u"\3\2\2\2\u06e9\u06ea\3\2\2\2\u06ea\u06eb\7\33\2\2\u06eb")
        buf.write(u"\u0105\3\2\2\2\u06ec\u06ed\b\u0084\1\2\u06ed\u06ee\5")
        buf.write(u"V,\2\u06ee\u06f4\3\2\2\2\u06ef\u06f0\f\3\2\2\u06f0\u06f1")
        buf.write(u"\7\23\2\2\u06f1\u06f3\5V,\2\u06f2\u06ef\3\2\2\2\u06f3")
        buf.write(u"\u06f6\3\2\2\2\u06f4\u06f2\3\2\2\2\u06f4\u06f5\3\2\2")
        buf.write(u"\2\u06f5\u0107\3\2\2\2\u06f6\u06f4\3\2\2\2\u06f7\u06f8")
        buf.write(u"\b\u0085\1\2\u06f8\u06f9\5\u010a\u0086\2\u06f9\u06ff")
        buf.write(u"\3\2\2\2\u06fa\u06fb\f\3\2\2\u06fb\u06fc\7\23\2\2\u06fc")
        buf.write(u"\u06fe\5\u010a\u0086\2\u06fd\u06fa\3\2\2\2\u06fe\u0701")
        buf.write(u"\3\2\2\2\u06ff\u06fd\3\2\2\2\u06ff\u0700\3\2\2\2\u0700")
        buf.write(u"\u0109\3\2\2\2\u0701\u06ff\3\2\2\2\u0702\u0703\5V,\2")
        buf.write(u"\u0703\u0704\7\21\2\2\u0704\u0705\5V,\2\u0705\u010b\3")
        buf.write(u"\2\2\2\u0706\u0707\5V,\2\u0707\u0708\7\21\2\2\u0708\u0709")
        buf.write(u"\5V,\2\u0709\u0710\3\2\2\2\u070a\u070b\5V,\2\u070b\u070c")
        buf.write(u"\7\21\2\2\u070c\u0710\3\2\2\2\u070d\u070e\7\21\2\2\u070e")
        buf.write(u"\u0710\5V,\2\u070f\u0706\3\2\2\2\u070f\u070a\3\2\2\2")
        buf.write(u"\u070f\u070d\3\2\2\2\u0710\u010d\3\2\2\2\u0711\u0712")
        buf.write(u"\5\u00b0Y\2\u0712\u0713\5\u0122\u0092\2\u0713\u0714\5")
        buf.write(u"V,\2\u0714\u010f\3\2\2\2\u0715\u0716\b\u0089\1\2\u0716")
        buf.write(u"\u0717\5\u00b0Y\2\u0717\u071c\3\2\2\2\u0718\u0719\f\3")
        buf.write(u"\2\2\u0719\u071b\5t;\2\u071a\u0718\3\2\2\2\u071b\u071e")
        buf.write(u"\3\2\2\2\u071c\u071a\3\2\2\2\u071c\u071d\3\2\2\2\u071d")
        buf.write(u"\u0111\3\2\2\2\u071e\u071c\3\2\2\2\u071f\u0720\6\u008a")
        buf.write(u"@\3\u0720\u0721\7\u009f\2\2\u0721\u0724\5\u00c2b\2\u0722")
        buf.write(u"\u0724\5V,\2\u0723\u071f\3\2\2\2\u0723\u0722\3\2\2\2")
        buf.write(u"\u0724\u0113\3\2\2\2\u0725\u072a\5\u0116\u008c\2\u0726")
        buf.write(u"\u0727\7\23\2\2\u0727\u0729\5\u0116\u008c\2\u0728\u0726")
        buf.write(u"\3\2\2\2\u0729\u072c\3\2\2\2\u072a\u0728\3\2\2\2\u072a")
        buf.write(u"\u072b\3\2\2\2\u072b\u0115\3\2\2\2\u072c\u072a\3\2\2")
        buf.write(u"\2\u072d\u0732\5\u00b0Y\2\u072e\u072f\7\25\2\2\u072f")
        buf.write(u"\u0731\5\u00b0Y\2\u0730\u072e\3\2\2\2\u0731\u0734\3\2")
        buf.write(u"\2\2\u0732\u0730\3\2\2\2\u0732\u0733\3\2\2\2\u0733\u0736")
        buf.write(u"\3\2\2\2\u0734\u0732\3\2\2\2\u0735\u0737\t\6\2\2\u0736")
        buf.write(u"\u0735\3\2\2\2\u0736\u0737\3\2\2\2\u0737\u0117\3\2\2")
        buf.write(u"\2\u0738\u073f\7\"\2\2\u0739\u073f\7#\2\2\u073a\u073f")
        buf.write(u"\5\u0124\u0093\2\u073b\u073f\5\u0126\u0094\2\u073c\u073f")
        buf.write(u"\5\u0128\u0095\2\u073d\u073f\5\u012a\u0096\2\u073e\u0738")
        buf.write(u"\3\2\2\2\u073e\u0739\3\2\2\2\u073e\u073a\3\2\2\2\u073e")
        buf.write(u"\u073b\3\2\2\2\u073e\u073c\3\2\2\2\u073e\u073d\3\2\2")
        buf.write(u"\2\u073f\u0119\3\2\2\2\u0740\u0741\7\u009f\2\2\u0741")
        buf.write(u"\u0742\6\u008eA\3\u0742\u011b\3\2\2\2\u0743\u0744\7\u009f")
        buf.write(u"\2\2\u0744\u0745\6\u008fB\3\u0745\u011d\3\2\2\2\u0746")
        buf.write(u"\u0747\7\u009f\2\2\u0747\u0748\6\u0090C\3\u0748\u011f")
        buf.write(u"\3\2\2\2\u0749\u074a\7\u009f\2\2\u074a\u074b\6\u0091")
        buf.write(u"D\3\u074b\u0121\3\2\2\2\u074c\u074d\7-\2\2\u074d\u0123")
        buf.write(u"\3\2\2\2\u074e\u074f\7$\2\2\u074f\u0125\3\2\2\2\u0750")
        buf.write(u"\u0751\7%\2\2\u0751\u0127\3\2\2\2\u0752\u0753\7&\2\2")
        buf.write(u"\u0753\u0129\3\2\2\2\u0754\u0755\t\7\2\2\u0755\u012b")
        buf.write(u"\3\2\2\2\u0756\u0757\7\u0084\2\2\u0757\u0758\5\u012e")
        buf.write(u"\u0098\2\u0758\u0759\7\22\2\2\u0759\u075e\3\2\2\2\u075a")
        buf.write(u"\u075b\5\u012e\u0098\2\u075b\u075c\7\22\2\2\u075c\u075e")
        buf.write(u"\3\2\2\2\u075d\u0756\3\2\2\2\u075d\u075a\3\2\2\2\u075e")
        buf.write(u"\u012d\3\2\2\2\u075f\u0760\b\u0098\1\2\u0760\u0761\5")
        buf.write(u"\u0130\u0099\2\u0761\u0766\3\2\2\2\u0762\u0763\f\3\2")
        buf.write(u"\2\u0763\u0765\5\u0136\u009c\2\u0764\u0762\3\2\2\2\u0765")
        buf.write(u"\u0768\3\2\2\2\u0766\u0764\3\2\2\2\u0766\u0767\3\2\2")
        buf.write(u"\2\u0767\u012f\3\2\2\2\u0768\u0766\3\2\2\2\u0769\u0771")
        buf.write(u"\5\u0132\u009a\2\u076a\u0771\5\u0134\u009b\2\u076b\u0771")
        buf.write(u"\5\u013e\u00a0\2\u076c\u0771\5\u0140\u00a1\2\u076d\u0771")
        buf.write(u"\5\u0142\u00a2\2\u076e\u0771\5\u0138\u009d\2\u076f\u0771")
        buf.write(u"\5\u013c\u009f\2\u0770\u0769\3\2\2\2\u0770\u076a\3\2")
        buf.write(u"\2\2\u0770\u076b\3\2\2\2\u0770\u076c\3\2\2\2\u0770\u076d")
        buf.write(u"\3\2\2\2\u0770\u076e\3\2\2\2\u0770\u076f\3\2\2\2\u0771")
        buf.write(u"\u0131\3\2\2\2\u0772\u0773\5\u00fa~\2\u0773\u0133\3\2")
        buf.write(u"\2\2\u0774\u0775\5\u011a\u008e\2\u0775\u0776\5\u0138")
        buf.write(u"\u009d\2\u0776\u0135\3\2\2\2\u0777\u0778\7\25\2\2\u0778")
        buf.write(u"\u077d\5\u0138\u009d\2\u0779\u077a\7\25\2\2\u077a\u077d")
        buf.write(u"\5\u0144\u00a3\2\u077b\u077d\5\u013c\u009f\2\u077c\u0777")
        buf.write(u"\3\2\2\2\u077c\u0779\3\2\2\2\u077c\u077b\3\2\2\2\u077d")
        buf.write(u"\u0137\3\2\2\2\u077e\u077f\5\u0144\u00a3\2\u077f\u0781")
        buf.write(u"\7\26\2\2\u0780\u0782\5\u013a\u009e\2\u0781\u0780\3\2")
        buf.write(u"\2\2\u0781\u0782\3\2\2\2\u0782\u0783\3\2\2\2\u0783\u0784")
        buf.write(u"\7\27\2\2\u0784\u0139\3\2\2\2\u0785\u0786\b\u009e\1\2")
        buf.write(u"\u0786\u0787\5\u012e\u0098\2\u0787\u078d\3\2\2\2\u0788")
        buf.write(u"\u0789\f\3\2\2\u0789\u078a\7\23\2\2\u078a\u078c\5\u012e")
        buf.write(u"\u0098\2\u078b\u0788\3\2\2\2\u078c\u078f\3\2\2\2\u078d")
        buf.write(u"\u078b\3\2\2\2\u078d\u078e\3\2\2\2\u078e\u013b\3\2\2")
        buf.write(u"\2\u078f\u078d\3\2\2\2\u0790\u0791\7\30\2\2\u0791\u0792")
        buf.write(u"\5\u012e\u0098\2\u0792\u0793\7\31\2\2\u0793\u013d\3\2")
        buf.write(u"\2\2\u0794\u0795\7\26\2\2\u0795\u0796\5\u012e\u0098\2")
        buf.write(u"\u0796\u0797\7\27\2\2\u0797\u013f\3\2\2\2\u0798\u0799")
        buf.write(u"\5\u0144\u00a3\2\u0799\u0141\3\2\2\2\u079a\u07a0\7\u00a3")
        buf.write(u"\2\2\u079b\u07a0\7\u00a5\2\2\u079c\u07a0\7\u00a2\2\2")
        buf.write(u"\u079d\u07a0\7\u0099\2\2\u079e\u07a0\7\u009a\2\2\u079f")
        buf.write(u"\u079a\3\2\2\2\u079f\u079b\3\2\2\2\u079f\u079c\3\2\2")
        buf.write(u"\2\u079f\u079d\3\2\2\2\u079f\u079e\3\2\2\2\u07a0\u0143")
        buf.write(u"\3\2\2\2\u07a1\u07a2\t\b\2\2\u07a2\u0145\3\2\2\2\u07a3")
        buf.write(u"\u07a4\7\u0084\2\2\u07a4\u07a7\5\u0148\u00a5\2\u07a5")
        buf.write(u"\u07a7\5\u0148\u00a5\2\u07a6\u07a3\3\2\2\2\u07a6\u07a5")
        buf.write(u"\3\2\2\2\u07a7\u0147\3\2\2\2\u07a8\u07a9\b\u00a5\1\2")
        buf.write(u"\u07a9\u07aa\5\u014a\u00a6\2\u07aa\u07af\3\2\2\2\u07ab")
        buf.write(u"\u07ac\f\3\2\2\u07ac\u07ae\5\u014c\u00a7\2\u07ad\u07ab")
        buf.write(u"\3\2\2\2\u07ae\u07b1\3\2\2\2\u07af\u07ad\3\2\2\2\u07af")
        buf.write(u"\u07b0\3\2\2\2\u07b0\u0149\3\2\2\2\u07b1\u07af\3\2\2")
        buf.write(u"\2\u07b2\u07b7\5\u0156\u00ac\2\u07b3\u07b7\5\u0158\u00ad")
        buf.write(u"\2\u07b4\u07b7\5\u015a\u00ae\2\u07b5\u07b7\5\u014e\u00a8")
        buf.write(u"\2\u07b6\u07b2\3\2\2\2\u07b6\u07b3\3\2\2\2\u07b6\u07b4")
        buf.write(u"\3\2\2\2\u07b6\u07b5\3\2\2\2\u07b7\u014b\3\2\2\2\u07b8")
        buf.write(u"\u07b9\7\25\2\2\u07b9\u07bf\5\u014e\u00a8\2\u07ba\u07bb")
        buf.write(u"\7\30\2\2\u07bb\u07bc\5\u0148\u00a5\2\u07bc\u07bd\7\31")
        buf.write(u"\2\2\u07bd\u07bf\3\2\2\2\u07be\u07b8\3\2\2\2\u07be\u07ba")
        buf.write(u"\3\2\2\2\u07bf\u014d\3\2\2\2\u07c0\u07c1\5\u015c\u00af")
        buf.write(u"\2\u07c1\u07c3\7\26\2\2\u07c2\u07c4\5\u0150\u00a9\2\u07c3")
        buf.write(u"\u07c2\3\2\2\2\u07c3\u07c4\3\2\2\2\u07c4\u07c5\3\2\2")
        buf.write(u"\2\u07c5\u07c6\7\27\2\2\u07c6\u014f\3\2\2\2\u07c7\u07ce")
        buf.write(u"\5\u0152\u00aa\2\u07c8\u07ce\5\u0154\u00ab\2\u07c9\u07ca")
        buf.write(u"\5\u0152\u00aa\2\u07ca\u07cb\7\23\2\2\u07cb\u07cc\5\u0154")
        buf.write(u"\u00ab\2\u07cc\u07ce\3\2\2\2\u07cd\u07c7\3\2\2\2\u07cd")
        buf.write(u"\u07c8\3\2\2\2\u07cd\u07c9\3\2\2\2\u07ce\u0151\3\2\2")
        buf.write(u"\2\u07cf\u07d0\b\u00aa\1\2\u07d0\u07d1\5\u0148\u00a5")
        buf.write(u"\2\u07d1\u07d7\3\2\2\2\u07d2\u07d3\f\3\2\2\u07d3\u07d4")
        buf.write(u"\7\23\2\2\u07d4\u07d6\5\u0148\u00a5\2\u07d5\u07d2\3\2")
        buf.write(u"\2\2\u07d6\u07d9\3\2\2\2\u07d7\u07d5\3\2\2\2\u07d7\u07d8")
        buf.write(u"\3\2\2\2\u07d8\u0153\3\2\2\2\u07d9\u07d7\3\2\2\2\u07da")
        buf.write(u"\u07db\b\u00ab\1\2\u07db\u07dc\5\u015c\u00af\2\u07dc")
        buf.write(u"\u07dd\7-\2\2\u07dd\u07de\5\u0148\u00a5\2\u07de\u07e7")
        buf.write(u"\3\2\2\2\u07df\u07e0\f\3\2\2\u07e0\u07e1\7\23\2\2\u07e1")
        buf.write(u"\u07e2\5\u015c\u00af\2\u07e2\u07e3\7-\2\2\u07e3\u07e4")
        buf.write(u"\5\u0148\u00a5\2\u07e4\u07e6\3\2\2\2\u07e5\u07df\3\2")
        buf.write(u"\2\2\u07e6\u07e9\3\2\2\2\u07e7\u07e5\3\2\2\2\u07e7\u07e8")
        buf.write(u"\3\2\2\2\u07e8\u0155\3\2\2\2\u07e9\u07e7\3\2\2\2\u07ea")
        buf.write(u"\u07eb\7\26\2\2\u07eb\u07ec\5\u0148\u00a5\2\u07ec\u07ed")
        buf.write(u"\7\27\2\2\u07ed\u0157\3\2\2\2\u07ee\u07ef\b\u00ad\1\2")
        buf.write(u"\u07ef\u07f2\7\u00a1\2\2\u07f0\u07f2\5\u015c\u00af\2")
        buf.write(u"\u07f1\u07ee\3\2\2\2\u07f1\u07f0\3\2\2\2\u07f2\u07f8")
        buf.write(u"\3\2\2\2\u07f3\u07f4\f\3\2\2\u07f4\u07f5\7\25\2\2\u07f5")
        buf.write(u"\u07f7\5\u015c\u00af\2\u07f6\u07f3\3\2\2\2\u07f7\u07fa")
        buf.write(u"\3\2\2\2\u07f8\u07f6\3\2\2\2\u07f8\u07f9\3\2\2\2\u07f9")
        buf.write(u"\u0159\3\2\2\2\u07fa\u07f8\3\2\2\2\u07fb\u0801\7\u00a3")
        buf.write(u"\2\2\u07fc\u0801\7\u00a5\2\2\u07fd\u0801\7\u00a2\2\2")
        buf.write(u"\u07fe\u0801\7\u0099\2\2\u07ff\u0801\7\u009a\2\2\u0800")
        buf.write(u"\u07fb\3\2\2\2\u0800\u07fc\3\2\2\2\u0800\u07fd\3\2\2")
        buf.write(u"\2\u0800\u07fe\3\2\2\2\u0800\u07ff\3\2\2\2\u0801\u015b")
        buf.write(u"\3\2\2\2\u0802\u0803\t\t\2\2\u0803\u015d\3\2\2\2\u0804")
        buf.write(u"\u0805\7\u0084\2\2\u0805\u0806\5\u0160\u00b1\2\u0806")
        buf.write(u"\u0807\7\22\2\2\u0807\u080c\3\2\2\2\u0808\u0809\5\u0160")
        buf.write(u"\u00b1\2\u0809\u080a\7\22\2\2\u080a\u080c\3\2\2\2\u080b")
        buf.write(u"\u0804\3\2\2\2\u080b\u0808\3\2\2\2\u080c\u015f\3\2\2")
        buf.write(u"\2\u080d\u080e\b\u00b1\1\2\u080e\u080f\5\u0162\u00b2")
        buf.write(u"\2\u080f\u0814\3\2\2\2\u0810\u0811\f\3\2\2\u0811\u0813")
        buf.write(u"\5\u0168\u00b5\2\u0812\u0810\3\2\2\2\u0813\u0816\3\2")
        buf.write(u"\2\2\u0814\u0812\3\2\2\2\u0814\u0815\3\2\2\2\u0815\u0161")
        buf.write(u"\3\2\2\2\u0816\u0814\3\2\2\2\u0817\u081d\5\u0164\u00b3")
        buf.write(u"\2\u0818\u081d\5\u0166\u00b4\2\u0819\u081d\5\u0170\u00b9")
        buf.write(u"\2\u081a\u081d\5\u0172\u00ba\2\u081b\u081d\5\u0176\u00bc")
        buf.write(u"\2\u081c\u0817\3\2\2\2\u081c\u0818\3\2\2\2\u081c\u0819")
        buf.write(u"\3\2\2\2\u081c\u081a\3\2\2\2\u081c\u081b\3\2\2\2\u081d")
        buf.write(u"\u0163\3\2\2\2\u081e\u081f\5\u00fa~\2\u081f\u0165\3\2")
        buf.write(u"\2\2\u0820\u0821\5\u011a\u008e\2\u0821\u0822\5\u016a")
        buf.write(u"\u00b6\2\u0822\u0167\3\2\2\2\u0823\u0824\7\25\2\2\u0824")
        buf.write(u"\u0827\5\u016a\u00b6\2\u0825\u0827\5\u016e\u00b8\2\u0826")
        buf.write(u"\u0823\3\2\2\2\u0826\u0825\3\2\2\2\u0827\u0169\3\2\2")
        buf.write(u"\2\u0828\u0829\5\u0178\u00bd\2\u0829\u082b\7\26\2\2\u082a")
        buf.write(u"\u082c\5\u016c\u00b7\2\u082b\u082a\3\2\2\2\u082b\u082c")
        buf.write(u"\3\2\2\2\u082c\u082d\3\2\2\2\u082d\u082e\7\27\2\2\u082e")
        buf.write(u"\u016b\3\2\2\2\u082f\u0830\b\u00b7\1\2\u0830\u0831\5")
        buf.write(u"\u0160\u00b1\2\u0831\u0837\3\2\2\2\u0832\u0833\f\3\2")
        buf.write(u"\2\u0833\u0834\7\23\2\2\u0834\u0836\5\u0160\u00b1\2\u0835")
        buf.write(u"\u0832\3\2\2\2\u0836\u0839\3\2\2\2\u0837\u0835\3\2\2")
        buf.write(u"\2\u0837\u0838\3\2\2\2\u0838\u016d\3\2\2\2\u0839\u0837")
        buf.write(u"\3\2\2\2\u083a\u083b\7\30\2\2\u083b\u083c\5\u0160\u00b1")
        buf.write(u"\2\u083c\u083d\7\31\2\2\u083d\u016f\3\2\2\2\u083e\u083f")
        buf.write(u"\7\26\2\2\u083f\u0840\5\u0160\u00b1\2\u0840\u0841\7\27")
        buf.write(u"\2\2\u0841\u0171\3\2\2\2\u0842\u0843\b\u00ba\1\2\u0843")
        buf.write(u"\u0844\5\u0178\u00bd\2\u0844\u084a\3\2\2\2\u0845\u0846")
        buf.write(u"\f\3\2\2\u0846\u0847\7\25\2\2\u0847\u0849\5\u0178\u00bd")
        buf.write(u"\2\u0848\u0845\3\2\2\2\u0849\u084c\3\2\2\2\u084a\u0848")
        buf.write(u"\3\2\2\2\u084a\u084b\3\2\2\2\u084b\u0173\3\2\2\2\u084c")
        buf.write(u"\u084a\3\2\2\2\u084d\u084e\b\u00bb\1\2\u084e\u084f\5")
        buf.write(u"\u0172\u00ba\2\u084f\u0854\3\2\2\2\u0850\u0851\f\3\2")
        buf.write(u"\2\u0851\u0853\7\u00a1\2\2\u0852\u0850\3\2\2\2\u0853")
        buf.write(u"\u0856\3\2\2\2\u0854\u0852\3\2\2\2\u0854\u0855\3\2\2")
        buf.write(u"\2\u0855\u0175\3\2\2\2\u0856\u0854\3\2\2\2\u0857\u085d")
        buf.write(u"\7\u00a3\2\2\u0858\u085d\7\u00a5\2\2\u0859\u085d\7\u00a2")
        buf.write(u"\2\2\u085a\u085d\7\u0099\2\2\u085b\u085d\7\u009a\2\2")
        buf.write(u"\u085c\u0857\3\2\2\2\u085c\u0858\3\2\2\2\u085c\u0859")
        buf.write(u"\3\2\2\2\u085c\u085a\3\2\2\2\u085c\u085b\3\2\2\2\u085d")
        buf.write(u"\u0177\3\2\2\2\u085e\u085f\t\n\2\2\u085f\u0179\3\2\2")
        buf.write(u"\2\u0860\u0861\7\u0084\2\2\u0861\u0862\5\u017c\u00bf")
        buf.write(u"\2\u0862\u0863\7\22\2\2\u0863\u0868\3\2\2\2\u0864\u0865")
        buf.write(u"\5\u017c\u00bf\2\u0865\u0866\7\22\2\2\u0866\u0868\3\2")
        buf.write(u"\2\2\u0867\u0860\3\2\2\2\u0867\u0864\3\2\2\2\u0868\u017b")
        buf.write(u"\3\2\2\2\u0869\u086a\b\u00bf\1\2\u086a\u086b\5\u017e")
        buf.write(u"\u00c0\2\u086b\u0870\3\2\2\2\u086c\u086d\f\3\2\2\u086d")
        buf.write(u"\u086f\5\u0184\u00c3\2\u086e\u086c\3\2\2\2\u086f\u0872")
        buf.write(u"\3\2\2\2\u0870\u086e\3\2\2\2\u0870\u0871\3\2\2\2\u0871")
        buf.write(u"\u017d\3\2\2\2\u0872\u0870\3\2\2\2\u0873\u0879\5\u0180")
        buf.write(u"\u00c1\2\u0874\u0879\5\u0182\u00c2\2\u0875\u0879\5\u018c")
        buf.write(u"\u00c7\2\u0876\u0879\5\u018e\u00c8\2\u0877\u0879\5\u0190")
        buf.write(u"\u00c9\2\u0878\u0873\3\2\2\2\u0878\u0874\3\2\2\2\u0878")
        buf.write(u"\u0875\3\2\2\2\u0878\u0876\3\2\2\2\u0878\u0877\3\2\2")
        buf.write(u"\2\u0879\u017f\3\2\2\2\u087a\u087b\5\u00fa~\2\u087b\u0181")
        buf.write(u"\3\2\2\2\u087c\u087d\5\u011a\u008e\2\u087d\u087e\5\u0186")
        buf.write(u"\u00c4\2\u087e\u0183\3\2\2\2\u087f\u0880\7\25\2\2\u0880")
        buf.write(u"\u0883\5\u0186\u00c4\2\u0881\u0883\5\u018a\u00c6\2\u0882")
        buf.write(u"\u087f\3\2\2\2\u0882\u0881\3\2\2\2\u0883\u0185\3\2\2")
        buf.write(u"\2\u0884\u0885\5\u0192\u00ca\2\u0885\u0887\7\26\2\2\u0886")
        buf.write(u"\u0888\5\u0188\u00c5\2\u0887\u0886\3\2\2\2\u0887\u0888")
        buf.write(u"\3\2\2\2\u0888\u0889\3\2\2\2\u0889\u088a\7\27\2\2\u088a")
        buf.write(u"\u0187\3\2\2\2\u088b\u088c\b\u00c5\1\2\u088c\u088d\5")
        buf.write(u"\u017c\u00bf\2\u088d\u0893\3\2\2\2\u088e\u088f\f\3\2")
        buf.write(u"\2\u088f\u0890\7\23\2\2\u0890\u0892\5\u017c\u00bf\2\u0891")
        buf.write(u"\u088e\3\2\2\2\u0892\u0895\3\2\2\2\u0893\u0891\3\2\2")
        buf.write(u"\2\u0893\u0894\3\2\2\2\u0894\u0189\3\2\2\2\u0895\u0893")
        buf.write(u"\3\2\2\2\u0896\u0897\7\30\2\2\u0897\u0898\5\u017c\u00bf")
        buf.write(u"\2\u0898\u0899\7\31\2\2\u0899\u018b\3\2\2\2\u089a\u089b")
        buf.write(u"\7\26\2\2\u089b\u089c\5\u017c\u00bf\2\u089c\u089d\7\27")
        buf.write(u"\2\2\u089d\u018d\3\2\2\2\u089e\u089f\b\u00c8\1\2\u089f")
        buf.write(u"\u08a2\7\u00a1\2\2\u08a0\u08a2\5\u0192\u00ca\2\u08a1")
        buf.write(u"\u089e\3\2\2\2\u08a1\u08a0\3\2\2\2\u08a2\u08a8\3\2\2")
        buf.write(u"\2\u08a3\u08a4\f\3\2\2\u08a4\u08a5\7\25\2\2\u08a5\u08a7")
        buf.write(u"\5\u0192\u00ca\2\u08a6\u08a3\3\2\2\2\u08a7\u08aa\3\2")
        buf.write(u"\2\2\u08a8\u08a6\3\2\2\2\u08a8\u08a9\3\2\2\2\u08a9\u018f")
        buf.write(u"\3\2\2\2\u08aa\u08a8\3\2\2\2\u08ab\u08b1\7\u00a3\2\2")
        buf.write(u"\u08ac\u08b1\7\u00a5\2\2\u08ad\u08b1\7\u00a2\2\2\u08ae")
        buf.write(u"\u08b1\7\u0099\2\2\u08af\u08b1\7\u009a\2\2\u08b0\u08ab")
        buf.write(u"\3\2\2\2\u08b0\u08ac\3\2\2\2\u08b0\u08ad\3\2\2\2\u08b0")
        buf.write(u"\u08ae\3\2\2\2\u08b0\u08af\3\2\2\2\u08b1\u0191\3\2\2")
        buf.write(u"\2\u08b2\u08b3\t\13\2\2\u08b3\u0193\3\2\2\2\u00b0\u019a")
        buf.write(u"\u019d\u01b6\u01bb\u01c6\u01cb\u01d6\u01dd\u01ea\u01f8")
        buf.write(u"\u020c\u0223\u022e\u0235\u023e\u0247\u0250\u0265\u026d")
        buf.write(u"\u0272\u0278\u027d\u0286\u028b\u0290\u02a8\u02b3\u02b7")
        buf.write(u"\u02ca\u02e0\u02e5\u02ee\u02f7\u0300\u031d\u0330\u0336")
        buf.write(u"\u0358\u0361\u0378\u0386\u038f\u0398\u03af\u03b3\u03c7")
        buf.write(u"\u042d\u042f\u043b\u0445\u0454\u0459\u0460\u0467\u0470")
        buf.write(u"\u0477\u0491\u049c\u04a0\u04a5\u04aa\u04ac\u04b6\u04c6")
        buf.write(u"\u04cf\u04d5\u04da\u04e1\u04e9\u04f7\u04ff\u0507\u050d")
        buf.write(u"\u0518\u0524\u052f\u053c\u0540\u0546\u0552\u0566\u0568")
        buf.write(u"\u056d\u057d\u0582\u058b\u0595\u059a\u059f\u05b1\u05b6")
        buf.write(u"\u05b9\u05bd\u05c2\u05c9\u05d4\u05d6\u05e2\u05ea\u05f5")
        buf.write(u"\u05fb\u0607\u060b\u0615\u061d\u0623\u062a\u062f\u0636")
        buf.write(u"\u063e\u0645\u0652\u065f\u0663\u0666\u066a\u066d\u0678")
        buf.write(u"\u0684\u0690\u069c\u06ad\u06bc\u06c6\u06cd\u06d7\u06de")
        buf.write(u"\u06e2\u06e8\u06f4\u06ff\u070f\u071c\u0723\u072a\u0732")
        buf.write(u"\u0736\u073e\u075d\u0766\u0770\u077c\u0781\u078d\u079f")
        buf.write(u"\u07a6\u07af\u07b6\u07be\u07c3\u07cd\u07d7\u07e7\u07f1")
        buf.write(u"\u07f8\u0800\u080b\u0814\u081c\u0826\u082b\u0837\u084a")
        buf.write(u"\u0854\u085c\u0867\u0870\u0878\u0882\u0887\u0893\u08a1")
        buf.write(u"\u08a8\u08b0")
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
                     u"'Code'", u"'Document'", u"'Blob'", u"'Image'", u"'UUID'", 
                     u"'abstract'", u"'all'", u"'always'", u"'and'", u"'any'", 
                     u"'as'", u"<INVALID>", u"'attr'", u"'attribute'", u"'attributes'", 
                     u"'bindings'", u"'by'", u"'case'", u"'catch'", u"'category'", 
                     u"'class'", u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'index'", u"'invoke'", u"'is'", u"'matching'", 
                     u"'method'", u"'methods'", u"'modulo'", u"'mutable'", 
                     u"'native'", u"'None'", u"'not'", u"<INVALID>", u"'null'", 
                     u"'on'", u"'one'", u"'open'", u"'operator'", u"'or'", 
                     u"'order'", u"'otherwise'", u"'pass'", u"'raise'", 
                     u"'read'", u"'receiving'", u"'resource'", u"'return'", 
                     u"'returning'", u"'rows'", u"'self'", u"'setter'", 
                     u"'singleton'", u"'sorted'", u"'storable'", u"'store'", 
                     u"'switch'", u"'test'", u"'this'", u"'throw'", u"'to'", 
                     u"'try'", u"'verifying'", u"'with'", u"'when'", u"'where'", 
                     u"'while'", u"'write'", u"<INVALID>", u"<INVALID>", 
                     u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

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
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DELETE", 
                      u"DESC", u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", 
                      u"ENUMERATED", u"EXCEPT", u"EXECUTE", u"EXPECTING", 
                      u"EXTENDS", u"FETCH", u"FINALLY", u"FOR", u"FROM", 
                      u"GETTER", u"IF", u"IN", u"INDEX", u"INVOKE", u"IS", 
                      u"MATCHING", u"METHOD", u"METHODS", u"MODULO", u"MUTABLE", 
                      u"NATIVE", u"NONE", u"NOT", u"NOTHING", u"NULL", u"ON", 
                      u"ONE", u"OPEN", u"OPERATOR", u"OR", u"ORDER", u"OTHERWISE", 
                      u"PASS", u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", 
                      u"RETURN", u"RETURNING", u"ROWS", u"SELF", u"SETTER", 
                      u"SINGLETON", u"SORTED", u"STORABLE", u"STORE", u"SWITCH", 
                      u"TEST", u"THIS", u"THROW", u"TO", u"TRY", u"VERIFYING", 
                      u"WITH", u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
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
    RULE_native_setter_declaration = 10
    RULE_getter_method_declaration = 11
    RULE_native_getter_declaration = 12
    RULE_native_category_declaration = 13
    RULE_native_resource_declaration = 14
    RULE_native_category_bindings = 15
    RULE_native_category_binding_list = 16
    RULE_abstract_method_declaration = 17
    RULE_concrete_method_declaration = 18
    RULE_native_method_declaration = 19
    RULE_test_method_declaration = 20
    RULE_assertion = 21
    RULE_typed_argument = 22
    RULE_statement = 23
    RULE_store_statement = 24
    RULE_method_call = 25
    RULE_method_selector = 26
    RULE_callable_parent = 27
    RULE_callable_selector = 28
    RULE_with_resource_statement = 29
    RULE_with_singleton_statement = 30
    RULE_switch_statement = 31
    RULE_switch_case_statement = 32
    RULE_for_each_statement = 33
    RULE_do_while_statement = 34
    RULE_while_statement = 35
    RULE_if_statement = 36
    RULE_else_if_statement_list = 37
    RULE_raise_statement = 38
    RULE_try_statement = 39
    RULE_catch_statement = 40
    RULE_return_statement = 41
    RULE_expression = 42
    RULE_closure_expression = 43
    RULE_instance_expression = 44
    RULE_method_expression = 45
    RULE_instance_selector = 46
    RULE_blob_expression = 47
    RULE_document_expression = 48
    RULE_constructor_expression = 49
    RULE_argument_assignment_list = 50
    RULE_argument_assignment = 51
    RULE_read_expression = 52
    RULE_write_statement = 53
    RULE_fetch_expression = 54
    RULE_sorted_expression = 55
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
    RULE_attribute_identifier = 88
    RULE_type_identifier = 89
    RULE_symbol_identifier = 90
    RULE_argument_list = 91
    RULE_argument = 92
    RULE_operator_argument = 93
    RULE_named_argument = 94
    RULE_code_argument = 95
    RULE_category_or_any_type = 96
    RULE_any_type = 97
    RULE_member_method_declaration_list = 98
    RULE_member_method_declaration = 99
    RULE_native_member_method_declaration_list = 100
    RULE_native_member_method_declaration = 101
    RULE_native_category_binding = 102
    RULE_python_category_binding = 103
    RULE_python_module = 104
    RULE_module_token = 105
    RULE_javascript_category_binding = 106
    RULE_javascript_module = 107
    RULE_variable_identifier_list = 108
    RULE_attribute_identifier_list = 109
    RULE_method_declaration = 110
    RULE_comment_statement = 111
    RULE_native_statement_list = 112
    RULE_native_statement = 113
    RULE_python_native_statement = 114
    RULE_javascript_native_statement = 115
    RULE_statement_list = 116
    RULE_assertion_list = 117
    RULE_switch_case_statement_list = 118
    RULE_catch_statement_list = 119
    RULE_literal_collection = 120
    RULE_atomic_literal = 121
    RULE_literal_list_literal = 122
    RULE_selectable_expression = 123
    RULE_this_expression = 124
    RULE_parenthesis_expression = 125
    RULE_literal_expression = 126
    RULE_collection_literal = 127
    RULE_tuple_literal = 128
    RULE_dict_literal = 129
    RULE_expression_tuple = 130
    RULE_dict_entry_list = 131
    RULE_dict_entry = 132
    RULE_slice_arguments = 133
    RULE_assign_variable_statement = 134
    RULE_assignable_instance = 135
    RULE_is_expression = 136
    RULE_order_by_list = 137
    RULE_order_by = 138
    RULE_operator = 139
    RULE_new_token = 140
    RULE_key_token = 141
    RULE_value_token = 142
    RULE_symbols_token = 143
    RULE_assign = 144
    RULE_multiply = 145
    RULE_divide = 146
    RULE_idivide = 147
    RULE_modulo = 148
    RULE_javascript_statement = 149
    RULE_javascript_expression = 150
    RULE_javascript_primary_expression = 151
    RULE_javascript_this_expression = 152
    RULE_javascript_new_expression = 153
    RULE_javascript_selector_expression = 154
    RULE_javascript_method_expression = 155
    RULE_javascript_arguments = 156
    RULE_javascript_item_expression = 157
    RULE_javascript_parenthesis_expression = 158
    RULE_javascript_identifier_expression = 159
    RULE_javascript_literal_expression = 160
    RULE_javascript_identifier = 161
    RULE_python_statement = 162
    RULE_python_expression = 163
    RULE_python_primary_expression = 164
    RULE_python_selector_expression = 165
    RULE_python_method_expression = 166
    RULE_python_argument_list = 167
    RULE_python_ordinal_argument_list = 168
    RULE_python_named_argument_list = 169
    RULE_python_parenthesis_expression = 170
    RULE_python_identifier_expression = 171
    RULE_python_literal_expression = 172
    RULE_python_identifier = 173
    RULE_java_statement = 174
    RULE_java_expression = 175
    RULE_java_primary_expression = 176
    RULE_java_this_expression = 177
    RULE_java_new_expression = 178
    RULE_java_selector_expression = 179
    RULE_java_method_expression = 180
    RULE_java_arguments = 181
    RULE_java_item_expression = 182
    RULE_java_parenthesis_expression = 183
    RULE_java_identifier_expression = 184
    RULE_java_class_identifier_expression = 185
    RULE_java_literal_expression = 186
    RULE_java_identifier = 187
    RULE_csharp_statement = 188
    RULE_csharp_expression = 189
    RULE_csharp_primary_expression = 190
    RULE_csharp_this_expression = 191
    RULE_csharp_new_expression = 192
    RULE_csharp_selector_expression = 193
    RULE_csharp_method_expression = 194
    RULE_csharp_arguments = 195
    RULE_csharp_item_expression = 196
    RULE_csharp_parenthesis_expression = 197
    RULE_csharp_identifier_expression = 198
    RULE_csharp_literal_expression = 199
    RULE_csharp_identifier = 200

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"typed_argument", 
                   u"statement", u"store_statement", u"method_call", u"method_selector", 
                   u"callable_parent", u"callable_selector", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"return_statement", 
                   u"expression", u"closure_expression", u"instance_expression", 
                   u"method_expression", u"instance_selector", u"blob_expression", 
                   u"document_expression", u"constructor_expression", u"argument_assignment_list", 
                   u"argument_assignment", u"read_expression", u"write_statement", 
                   u"fetch_expression", u"sorted_expression", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"lfs", 
                   u"lfp", u"indent", u"dedent", u"null_literal", u"declaration_list", 
                   u"declarations", u"declaration", u"resource_declaration", 
                   u"enum_declaration", u"native_symbol_list", u"category_symbol_list", 
                   u"symbol_list", u"attribute_constraint", u"list_literal", 
                   u"set_literal", u"expression_list", u"range_literal", 
                   u"typedef", u"primary_type", u"native_type", u"category_type", 
                   u"mutable_category_type", u"code_type", u"category_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"attribute_identifier", u"type_identifier", 
                   u"symbol_identifier", u"argument_list", u"argument", 
                   u"operator_argument", u"named_argument", u"code_argument", 
                   u"category_or_any_type", u"any_type", u"member_method_declaration_list", 
                   u"member_method_declaration", u"native_member_method_declaration_list", 
                   u"native_member_method_declaration", u"native_category_binding", 
                   u"python_category_binding", u"python_module", u"module_token", 
                   u"javascript_category_binding", u"javascript_module", 
                   u"variable_identifier_list", u"attribute_identifier_list", 
                   u"method_declaration", u"comment_statement", u"native_statement_list", 
                   u"native_statement", u"python_native_statement", u"javascript_native_statement", 
                   u"statement_list", u"assertion_list", u"switch_case_statement_list", 
                   u"catch_statement_list", u"literal_collection", u"atomic_literal", 
                   u"literal_list_literal", u"selectable_expression", u"this_expression", 
                   u"parenthesis_expression", u"literal_expression", u"collection_literal", 
                   u"tuple_literal", u"dict_literal", u"expression_tuple", 
                   u"dict_entry_list", u"dict_entry", u"slice_arguments", 
                   u"assign_variable_statement", u"assignable_instance", 
                   u"is_expression", u"order_by_list", u"order_by", u"operator", 
                   u"new_token", u"key_token", u"value_token", u"symbols_token", 
                   u"assign", u"multiply", u"divide", u"idivide", u"modulo", 
                   u"javascript_statement", u"javascript_expression", u"javascript_primary_expression", 
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
    DELETE=86
    DESC=87
    DO=88
    DOING=89
    EACH=90
    ELSE=91
    ENUM=92
    ENUMERATED=93
    EXCEPT=94
    EXECUTE=95
    EXPECTING=96
    EXTENDS=97
    FETCH=98
    FINALLY=99
    FOR=100
    FROM=101
    GETTER=102
    IF=103
    IN=104
    INDEX=105
    INVOKE=106
    IS=107
    MATCHING=108
    METHOD=109
    METHODS=110
    MODULO=111
    MUTABLE=112
    NATIVE=113
    NONE=114
    NOT=115
    NOTHING=116
    NULL=117
    ON=118
    ONE=119
    OPEN=120
    OPERATOR=121
    OR=122
    ORDER=123
    OTHERWISE=124
    PASS=125
    RAISE=126
    READ=127
    RECEIVING=128
    RESOURCE=129
    RETURN=130
    RETURNING=131
    ROWS=132
    SELF=133
    SETTER=134
    SINGLETON=135
    SORTED=136
    STORABLE=137
    STORE=138
    SWITCH=139
    TEST=140
    THIS=141
    THROW=142
    TO=143
    TRY=144
    VERIFYING=145
    WITH=146
    WHEN=147
    WHERE=148
    WHILE=149
    WRITE=150
    BOOLEAN_LITERAL=151
    CHAR_LITERAL=152
    MIN_INTEGER=153
    MAX_INTEGER=154
    SYMBOL_IDENTIFIER=155
    TYPE_IDENTIFIER=156
    VARIABLE_IDENTIFIER=157
    NATIVE_IDENTIFIER=158
    DOLLAR_IDENTIFIER=159
    TEXT_LITERAL=160
    INTEGER_LITERAL=161
    HEXA_LITERAL=162
    DECIMAL_LITERAL=163
    DATETIME_LITERAL=164
    TIME_LITERAL=165
    DATE_LITERAL=166
    PERIOD_LITERAL=167

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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
            self.state = 402
            self.match(SParser.ENUM)
            self.state = 403 
            localctx.name = self.type_identifier()
            self.state = 404
            self.match(SParser.LPAR)
            self.state = 411
            token = self._input.LA(1)
            if token in [SParser.TYPE_IDENTIFIER]:
                self.state = 405 
                localctx.derived = self.type_identifier()
                self.state = 408
                _la = self._input.LA(1)
                if _la==SParser.COMMA:
                    self.state = 406
                    self.match(SParser.COMMA)
                    self.state = 407 
                    localctx.attrs = self.attribute_identifier_list()



            elif token in [SParser.STORABLE, SParser.VARIABLE_IDENTIFIER]:
                self.state = 410 
                localctx.attrs = self.attribute_identifier_list()

            else:
                raise NoViableAltException(self)

            self.state = 413
            self.match(SParser.RPAR)
            self.state = 414
            self.match(SParser.COLON)
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
            self.state = 419
            self.match(SParser.ENUM)
            self.state = 420 
            localctx.name = self.type_identifier()
            self.state = 421
            self.match(SParser.LPAR)
            self.state = 422 
            localctx.typ = self.native_type()
            self.state = 423
            self.match(SParser.RPAR)
            self.state = 424
            self.match(SParser.COLON)
            self.state = 425 
            self.indent()
            self.state = 426 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 427 
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
            self.state = 429 
            localctx.name = self.symbol_identifier()
            self.state = 430
            self.match(SParser.EQ)
            self.state = 431 
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
            self.state = 433 
            localctx.name = self.symbol_identifier()
            self.state = 434
            self.match(SParser.LPAR)
            self.state = 436
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 435 
                localctx.args = self.argument_assignment_list(0)


            self.state = 438
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
            self.name = None # Attribute_identifierContext
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


        def attribute_identifier(self):
            return self.getTypedRuleContext(SParser.Attribute_identifierContext,0)


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
            self.state = 441
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 440
                self.match(SParser.STORABLE)


            self.state = 443
            self.match(SParser.ATTR)
            self.state = 444 
            localctx.name = self.attribute_identifier()
            self.state = 445
            self.match(SParser.LPAR)
            self.state = 446 
            localctx.typ = self.typedef(0)
            self.state = 447
            self.match(SParser.RPAR)
            self.state = 448
            self.match(SParser.COLON)
            self.state = 449 
            self.indent()
            self.state = 452
            token = self._input.LA(1)
            if token in [SParser.IN, SParser.MATCHING]:
                self.state = 450 
                localctx.match = self.attribute_constraint()

            elif token in [SParser.PASS]:
                self.state = 451
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 454 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
            self.state = 457
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 456
                self.match(SParser.STORABLE)


            self.state = 459
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 460 
            localctx.name = self.type_identifier()
            self.state = 461
            self.match(SParser.LPAR)
            self.state = 468
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 462 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 463 
                localctx.attrs = self.attribute_identifier_list()
                pass

            elif la_ == 3:
                self.state = 464 
                localctx.derived = self.derived_list()
                self.state = 465
                self.match(SParser.COMMA)
                self.state = 466 
                localctx.attrs = self.attribute_identifier_list()
                pass


            self.state = 470
            self.match(SParser.RPAR)
            self.state = 471
            self.match(SParser.COLON)
            self.state = 472 
            self.indent()
            self.state = 475
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 473 
                localctx.methods = self.member_method_declaration_list(0)

            elif token in [SParser.PASS]:
                self.state = 474
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 477 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
            self.state = 479
            self.match(SParser.SINGLETON)
            self.state = 480 
            localctx.name = self.type_identifier()
            self.state = 481
            self.match(SParser.LPAR)
            self.state = 482 
            localctx.attrs = self.attribute_identifier_list()
            self.state = 483
            self.match(SParser.RPAR)
            self.state = 484
            self.match(SParser.COLON)
            self.state = 485 
            self.indent()
            self.state = 488
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 486 
                localctx.methods = self.member_method_declaration_list(0)

            elif token in [SParser.PASS]:
                self.state = 487
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 490 
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
            self.state = 492 
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
            self.state = 494
            self.match(SParser.DEF)
            self.state = 495
            self.match(SParser.OPERATOR)
            self.state = 496 
            localctx.op = self.operator()
            self.state = 497
            self.match(SParser.LPAR)
            self.state = 498 
            localctx.arg = self.operator_argument()
            self.state = 499
            self.match(SParser.RPAR)
            self.state = 502
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 500
                self.match(SParser.RARROW)
                self.state = 501 
                localctx.typ = self.typedef(0)


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
            self.state = 509
            self.match(SParser.DEF)
            self.state = 510 
            localctx.name = self.variable_identifier()
            self.state = 511
            self.match(SParser.SETTER)
            self.state = 512
            self.match(SParser.LPAR)
            self.state = 513
            self.match(SParser.RPAR)
            self.state = 514
            self.match(SParser.COLON)
            self.state = 515 
            self.indent()
            self.state = 516 
            localctx.stmts = self.statement_list(0)
            self.state = 517 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_setter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

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


        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def getRuleIndex(self):
            return SParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = SParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(SParser.DEF)
            self.state = 520 
            localctx.name = self.variable_identifier()
            self.state = 522
            _la = self._input.LA(1)
            if _la==SParser.NATIVE:
                self.state = 521
                self.match(SParser.NATIVE)


            self.state = 524
            self.match(SParser.SETTER)
            self.state = 525
            self.match(SParser.LPAR)
            self.state = 526
            self.match(SParser.RPAR)
            self.state = 527
            self.match(SParser.COLON)
            self.state = 528 
            self.indent()
            self.state = 529 
            localctx.stmts = self.native_statement_list(0)
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
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(SParser.DEF)
            self.state = 533 
            localctx.name = self.variable_identifier()
            self.state = 534
            self.match(SParser.GETTER)
            self.state = 535
            self.match(SParser.LPAR)
            self.state = 536
            self.match(SParser.RPAR)
            self.state = 537
            self.match(SParser.COLON)
            self.state = 538 
            self.indent()
            self.state = 539 
            localctx.stmts = self.statement_list(0)
            self.state = 540 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_getter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

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


        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def getRuleIndex(self):
            return SParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = SParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(SParser.DEF)
            self.state = 543 
            localctx.name = self.variable_identifier()
            self.state = 545
            _la = self._input.LA(1)
            if _la==SParser.NATIVE:
                self.state = 544
                self.match(SParser.NATIVE)


            self.state = 547
            self.match(SParser.GETTER)
            self.state = 548
            self.match(SParser.LPAR)
            self.state = 549
            self.match(SParser.RPAR)
            self.state = 550
            self.match(SParser.COLON)
            self.state = 551 
            self.indent()
            self.state = 552 
            localctx.stmts = self.native_statement_list(0)
            self.state = 553 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 26, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 555
                self.match(SParser.STORABLE)


            self.state = 558
            self.match(SParser.NATIVE)
            self.state = 559
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 560 
            localctx.name = self.type_identifier()
            self.state = 561
            self.match(SParser.LPAR)
            self.state = 563
            _la = self._input.LA(1)
            if _la==SParser.STORABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 562 
                localctx.attrs = self.attribute_identifier_list()


            self.state = 565
            self.match(SParser.RPAR)
            self.state = 566
            self.match(SParser.COLON)
            self.state = 567 
            self.indent()
            self.state = 568 
            localctx.bindings = self.native_category_bindings()
            self.state = 572
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 569 
                self.lfp()
                self.state = 570 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 574 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 28, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(SParser.NATIVE)
            self.state = 577
            self.match(SParser.RESOURCE)
            self.state = 578 
            localctx.name = self.type_identifier()
            self.state = 579
            self.match(SParser.LPAR)
            self.state = 581
            _la = self._input.LA(1)
            if _la==SParser.STORABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 580 
                localctx.attrs = self.attribute_identifier_list()


            self.state = 583
            self.match(SParser.RPAR)
            self.state = 584
            self.match(SParser.COLON)
            self.state = 585 
            self.indent()
            self.state = 586 
            localctx.bindings = self.native_category_bindings()
            self.state = 590
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 587 
                self.lfp()
                self.state = 588 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 592 
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
        self.enterRule(localctx, 30, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(SParser.DEF)
            self.state = 595
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 596
            self.match(SParser.BINDINGS)
            self.state = 597
            self.match(SParser.COLON)
            self.state = 598 
            self.indent()
            self.state = 599 
            localctx.items = self.native_category_binding_list(0)
            self.state = 600 
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 603 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 611
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryBindingListItemContext(self, SParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 605
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 606 
                    self.lfp()
                    self.state = 607 
                    localctx.item = self.native_category_binding() 
                self.state = 613
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 34, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(SParser.ABSTRACT)
            self.state = 615
            self.match(SParser.DEF)
            self.state = 616 
            localctx.name = self.method_identifier()
            self.state = 617
            self.match(SParser.LPAR)
            self.state = 619
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 618 
                localctx.args = self.argument_list(0)


            self.state = 621
            self.match(SParser.RPAR)
            self.state = 624
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 622
                self.match(SParser.RARROW)
                self.state = 623 
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
        self.enterRule(localctx, 36, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.match(SParser.DEF)
            self.state = 627 
            localctx.name = self.method_identifier()
            self.state = 628
            self.match(SParser.LPAR)
            self.state = 630
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 629 
                localctx.args = self.argument_list(0)


            self.state = 632
            self.match(SParser.RPAR)
            self.state = 635
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 633
                self.match(SParser.RARROW)
                self.state = 634 
                localctx.typ = self.typedef(0)


            self.state = 637
            self.match(SParser.COLON)
            self.state = 638 
            self.indent()
            self.state = 639 
            localctx.stmts = self.statement_list(0)
            self.state = 640 
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


        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

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
        self.enterRule(localctx, 38, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self.match(SParser.DEF)
            self.state = 644
            _la = self._input.LA(1)
            if _la==SParser.NATIVE:
                self.state = 643
                self.match(SParser.NATIVE)


            self.state = 646 
            localctx.name = self.method_identifier()
            self.state = 647
            self.match(SParser.LPAR)
            self.state = 649
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 648 
                localctx.args = self.argument_list(0)


            self.state = 651
            self.match(SParser.RPAR)
            self.state = 654
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 652
                self.match(SParser.RARROW)
                self.state = 653 
                localctx.typ = self.category_or_any_type()


            self.state = 656
            self.match(SParser.COLON)
            self.state = 657 
            self.indent()
            self.state = 658 
            localctx.stmts = self.native_statement_list(0)
            self.state = 659 
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
        self.enterRule(localctx, 40, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(SParser.DEF)
            self.state = 662
            self.match(SParser.TEST)
            self.state = 663
            localctx.name = self.match(SParser.TEXT_LITERAL)
            self.state = 664
            self.match(SParser.LPAR)
            self.state = 665
            self.match(SParser.RPAR)
            self.state = 666
            self.match(SParser.COLON)
            self.state = 667 
            self.indent()
            self.state = 668 
            localctx.stmts = self.statement_list(0)
            self.state = 669 
            self.dedent()
            self.state = 670 
            self.lfp()
            self.state = 671
            self.match(SParser.VERIFYING)
            self.state = 672
            self.match(SParser.COLON)
            self.state = 678
            token = self._input.LA(1)
            if token in [SParser.LF]:
                self.state = 673 
                self.indent()
                self.state = 674 
                localctx.exps = self.assertion_list(0)
                self.state = 675 
                self.dedent()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                self.state = 677 
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
        self.enterRule(localctx, 42, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680 
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
            self.attrs = None # Attribute_identifier_listContext
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

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 44, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682 
            localctx.name = self.variable_identifier()
            self.state = 683
            self.match(SParser.COLON)
            self.state = 684 
            localctx.typ = self.category_or_any_type()
            self.state = 689
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 685
                self.match(SParser.LPAR)
                self.state = 686 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 687
                self.match(SParser.RPAR)


            self.state = 693
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 691
                self.match(SParser.EQ)
                self.state = 692 
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
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 712
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 695 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = SParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 696 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = SParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 697 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = SParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 698 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = SParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 699 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 6:
                localctx = SParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 700 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 7:
                localctx = SParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 701 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 8:
                localctx = SParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 702 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 9:
                localctx = SParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 703 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 10:
                localctx = SParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 704 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 11:
                localctx = SParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 705 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 12:
                localctx = SParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 706 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 13:
                localctx = SParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 707 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 14:
                localctx = SParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 708 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 15:
                localctx = SParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 709 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 16:
                localctx = SParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 710 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 17:
                localctx = SParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 711 
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
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(SParser.DELETE, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(SParser.LPAR)
            else:
                return self.getToken(SParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(SParser.RPAR)
            else:
                return self.getToken(SParser.RPAR, i)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(SParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(SParser.STORE, 0)

        def AND(self):
            return self.getToken(SParser.AND, 0)

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
        self.enterRule(localctx, 48, self.RULE_store_statement)
        try:
            self.state = 734
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 714
                self.match(SParser.DELETE)
                self.state = 715
                self.match(SParser.LPAR)
                self.state = 716 
                localctx.to_del = self.expression_list(0)
                self.state = 717
                self.match(SParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 719
                self.match(SParser.STORE)
                self.state = 720
                self.match(SParser.LPAR)
                self.state = 721 
                localctx.to_add = self.expression_list(0)
                self.state = 722
                self.match(SParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 724
                self.match(SParser.DELETE)
                self.state = 725
                self.match(SParser.LPAR)
                self.state = 726 
                localctx.to_del = self.expression_list(0)
                self.state = 727
                self.match(SParser.RPAR)
                self.state = 728
                self.match(SParser.AND)
                self.state = 729
                self.match(SParser.STORE)
                self.state = 730
                self.match(SParser.LPAR)
                self.state = 731 
                localctx.to_add = self.expression_list(0)
                self.state = 732
                self.match(SParser.RPAR)
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
        self.enterRule(localctx, 50, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736 
            localctx.method = self.method_selector()
            self.state = 737
            self.match(SParser.LPAR)
            self.state = 739
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 738 
                localctx.args = self.argument_assignment_list(0)


            self.state = 741
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
        self.enterRule(localctx, 52, self.RULE_method_selector)
        try:
            self.state = 748
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 743 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 744 
                localctx.parent = self.callable_parent(0)
                self.state = 745
                self.match(SParser.DOT)
                self.state = 746 
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 751 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 757
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CallableSelectorContext(self, SParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 753
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 754 
                    localctx.select = self.callable_selector() 
                self.state = 759
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_callable_selector)
        try:
            self.state = 766
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 760
                self.match(SParser.DOT)
                self.state = 761 
                localctx.name = self.variable_identifier()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 762
                self.match(SParser.LBRAK)
                self.state = 763 
                localctx.exp = self.expression(0)
                self.state = 764
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
        self.enterRule(localctx, 58, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            self.match(SParser.WITH)
            self.state = 769 
            localctx.stmt = self.assign_variable_statement()
            self.state = 770
            self.match(SParser.COLON)
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
        self.enterRule(localctx, 60, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.match(SParser.WITH)
            self.state = 776 
            localctx.typ = self.type_identifier()
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
        self.enterRule(localctx, 62, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.match(SParser.SWITCH)
            self.state = 783
            self.match(SParser.ON)
            self.state = 784 
            localctx.exp = self.expression(0)
            self.state = 785
            self.match(SParser.COLON)
            self.state = 786 
            self.indent()
            self.state = 787 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 795
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 788 
                self.lfp()
                self.state = 789
                self.match(SParser.OTHERWISE)
                self.state = 790
                self.match(SParser.COLON)
                self.state = 791 
                self.indent()
                self.state = 792 
                localctx.stmts = self.statement_list(0)
                self.state = 793 
                self.dedent()


            self.state = 797 
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
        self.enterRule(localctx, 64, self.RULE_switch_case_statement)
        try:
            self.state = 814
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = SParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 799
                self.match(SParser.WHEN)
                self.state = 800 
                localctx.exp = self.atomic_literal()
                self.state = 801
                self.match(SParser.COLON)
                self.state = 802 
                self.indent()
                self.state = 803 
                localctx.stmts = self.statement_list(0)
                self.state = 804 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = SParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 806
                self.match(SParser.WHEN)
                self.state = 807
                self.match(SParser.IN)
                self.state = 808 
                localctx.exp = self.literal_collection()
                self.state = 809
                self.match(SParser.COLON)
                self.state = 810 
                self.indent()
                self.state = 811 
                localctx.stmts = self.statement_list(0)
                self.state = 812 
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
        self.enterRule(localctx, 66, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 816
            self.match(SParser.FOR)
            self.state = 817 
            localctx.name1 = self.variable_identifier()
            self.state = 820
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 818
                self.match(SParser.COMMA)
                self.state = 819 
                localctx.name2 = self.variable_identifier()


            self.state = 822
            self.match(SParser.IN)
            self.state = 823 
            localctx.source = self.expression(0)
            self.state = 824
            self.match(SParser.COLON)
            self.state = 825 
            self.indent()
            self.state = 826 
            localctx.stmts = self.statement_list(0)
            self.state = 827 
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
        self.enterRule(localctx, 68, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(SParser.DO)
            self.state = 830
            self.match(SParser.COLON)
            self.state = 831 
            self.indent()
            self.state = 832 
            localctx.stmts = self.statement_list(0)
            self.state = 833 
            self.dedent()
            self.state = 834 
            self.lfp()
            self.state = 835
            self.match(SParser.WHILE)
            self.state = 836 
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
        self.enterRule(localctx, 70, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 838
            self.match(SParser.WHILE)
            self.state = 839 
            localctx.exp = self.expression(0)
            self.state = 840
            self.match(SParser.COLON)
            self.state = 841 
            self.indent()
            self.state = 842 
            localctx.stmts = self.statement_list(0)
            self.state = 843 
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
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 845
            self.match(SParser.IF)
            self.state = 846 
            localctx.exp = self.expression(0)
            self.state = 847
            self.match(SParser.COLON)
            self.state = 848 
            self.indent()
            self.state = 849 
            localctx.stmts = self.statement_list(0)
            self.state = 850 
            self.dedent()
            self.state = 854
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 851 
                self.lfp()
                self.state = 852 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 863
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 856 
                self.lfp()
                self.state = 857
                self.match(SParser.ELSE)
                self.state = 858
                self.match(SParser.COLON)
                self.state = 859 
                self.indent()
                self.state = 860 
                localctx.elseStmts = self.statement_list(0)
                self.state = 861 
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 866
            self.match(SParser.ELSE)
            self.state = 867
            self.match(SParser.IF)
            self.state = 868 
            localctx.exp = self.expression(0)
            self.state = 869
            self.match(SParser.COLON)
            self.state = 870 
            self.indent()
            self.state = 871 
            localctx.stmts = self.statement_list(0)
            self.state = 872 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 886
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ElseIfStatementListItemContext(self, SParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 874
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 875 
                    self.lfp()
                    self.state = 876
                    self.match(SParser.ELSE)
                    self.state = 877
                    self.match(SParser.IF)
                    self.state = 878 
                    localctx.exp = self.expression(0)
                    self.state = 879
                    self.match(SParser.COLON)
                    self.state = 880 
                    self.indent()
                    self.state = 881 
                    localctx.stmts = self.statement_list(0)
                    self.state = 882 
                    self.dedent() 
                self.state = 888
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
        self.enterRule(localctx, 76, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 889
            self.match(SParser.RAISE)
            self.state = 890 
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
        self.enterRule(localctx, 78, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 892
            self.match(SParser.TRY)
            self.state = 893 
            localctx.name = self.variable_identifier()
            self.state = 894
            self.match(SParser.COLON)
            self.state = 895 
            self.indent()
            self.state = 896 
            localctx.stmts = self.statement_list(0)
            self.state = 897 
            self.dedent()
            self.state = 898 
            self.lfs()
            self.state = 900
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 899 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 909
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 902
                self.match(SParser.EXCEPT)
                self.state = 903
                self.match(SParser.COLON)
                self.state = 904 
                self.indent()
                self.state = 905 
                localctx.anyStmts = self.statement_list(0)
                self.state = 906 
                self.dedent()
                self.state = 907 
                self.lfs()


            self.state = 918
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 911
                self.match(SParser.FINALLY)
                self.state = 912
                self.match(SParser.COLON)
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
        self.enterRule(localctx, 80, self.RULE_catch_statement)
        try:
            self.state = 941
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = SParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 922
                self.match(SParser.EXCEPT)
                self.state = 923 
                localctx.name = self.symbol_identifier()
                self.state = 924
                self.match(SParser.COLON)
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
                localctx = SParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 930
                self.match(SParser.EXCEPT)
                self.state = 931
                self.match(SParser.IN)
                self.state = 932
                self.match(SParser.LBRAK)
                self.state = 933 
                localctx.exp = self.symbol_list(0)
                self.state = 934
                self.match(SParser.RBRAK)
                self.state = 935
                self.match(SParser.COLON)
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
        self.enterRule(localctx, 82, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 943
            self.match(SParser.RETURN)
            self.state = 945
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
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


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(SParser.FOR, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIteratorExpression(self)


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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 965
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = SParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 948
                self.match(SParser.MINUS)
                self.state = 949 
                localctx.exp = self.expression(32)
                pass

            elif la_ == 2:
                localctx = SParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 950
                self.match(SParser.NOT)
                self.state = 951 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 3:
                localctx = SParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 952 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = SParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 953 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = SParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 954
                self.match(SParser.CODE)
                self.state = 955
                self.match(SParser.LPAR)
                self.state = 956 
                localctx.exp = self.expression(0)
                self.state = 957
                self.match(SParser.RPAR)
                pass

            elif la_ == 6:
                localctx = SParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 959
                self.match(SParser.EXECUTE)
                self.state = 960
                self.match(SParser.LPAR)
                self.state = 961 
                localctx.name = self.variable_identifier()
                self.state = 962
                self.match(SParser.RPAR)
                pass

            elif la_ == 7:
                localctx = SParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 964 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1069
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1067
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = SParser.MultiplyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 967
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 968 
                        self.multiply()
                        self.state = 969 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 2:
                        localctx = SParser.DivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 971
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 972 
                        self.divide()
                        self.state = 973 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 3:
                        localctx = SParser.ModuloExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 975
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 976 
                        self.modulo()
                        self.state = 977 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 4:
                        localctx = SParser.IntDivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 979
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 980 
                        self.idivide()
                        self.state = 981 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 5:
                        localctx = SParser.AddExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 983
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 984
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SParser.PLUS or _la==SParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 985 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 6:
                        localctx = SParser.LessThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 986
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 987
                        self.match(SParser.LT)
                        self.state = 988 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 7:
                        localctx = SParser.LessThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 989
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 990
                        self.match(SParser.LTE)
                        self.state = 991 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 8:
                        localctx = SParser.GreaterThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 992
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 993
                        self.match(SParser.GT)
                        self.state = 994 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 9:
                        localctx = SParser.GreaterThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 995
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 996
                        self.match(SParser.GTE)
                        self.state = 997 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 10:
                        localctx = SParser.EqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 998
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 999
                        self.match(SParser.EQ2)
                        self.state = 1000 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 11:
                        localctx = SParser.NotEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1001
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1002
                        self.match(SParser.XEQ)
                        self.state = 1003 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 12:
                        localctx = SParser.RoughlyEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1004
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1005
                        self.match(SParser.TEQ)
                        self.state = 1006 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 13:
                        localctx = SParser.OrExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1007
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1008
                        self.match(SParser.OR)
                        self.state = 1009 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 14:
                        localctx = SParser.AndExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1010
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1011
                        self.match(SParser.AND)
                        self.state = 1012 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 15:
                        localctx = SParser.TernaryExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1013
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1014
                        self.match(SParser.IF)
                        self.state = 1015 
                        localctx.test = self.expression(0)
                        self.state = 1016
                        self.match(SParser.ELSE)
                        self.state = 1017 
                        localctx.ifFalse = self.expression(15)
                        pass

                    elif la_ == 16:
                        localctx = SParser.InExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1019
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1020
                        self.match(SParser.IN)
                        self.state = 1021 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 17:
                        localctx = SParser.ContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1022
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1023
                        self.match(SParser.CONTAINS)
                        self.state = 1024 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 18:
                        localctx = SParser.ContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1025
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1026
                        self.match(SParser.CONTAINS)
                        self.state = 1027
                        self.match(SParser.ALL)
                        self.state = 1028 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 19:
                        localctx = SParser.ContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1029
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1030
                        self.match(SParser.CONTAINS)
                        self.state = 1031
                        self.match(SParser.ANY)
                        self.state = 1032 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 20:
                        localctx = SParser.NotInExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1033
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1034
                        self.match(SParser.NOT)
                        self.state = 1035
                        self.match(SParser.IN)
                        self.state = 1036 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 21:
                        localctx = SParser.NotContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1037
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1038
                        self.match(SParser.NOT)
                        self.state = 1039
                        self.match(SParser.CONTAINS)
                        self.state = 1040 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 22:
                        localctx = SParser.NotContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1041
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1042
                        self.match(SParser.NOT)
                        self.state = 1043
                        self.match(SParser.CONTAINS)
                        self.state = 1044
                        self.match(SParser.ALL)
                        self.state = 1045 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 23:
                        localctx = SParser.NotContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1046
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1047
                        self.match(SParser.NOT)
                        self.state = 1048
                        self.match(SParser.CONTAINS)
                        self.state = 1049
                        self.match(SParser.ANY)
                        self.state = 1050 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 24:
                        localctx = SParser.IteratorExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1051
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1052
                        self.match(SParser.FOR)
                        self.state = 1053 
                        localctx.name = self.variable_identifier()
                        self.state = 1054
                        self.match(SParser.IN)
                        self.state = 1055 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = SParser.IsNotExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1057
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1058
                        self.match(SParser.IS)
                        self.state = 1059
                        self.match(SParser.NOT)
                        self.state = 1060 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = SParser.IsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1061
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1062
                        self.match(SParser.IS)
                        self.state = 1063 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = SParser.CastExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1064
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1065
                        self.match(SParser.AS)
                        self.state = 1066 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1071
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1072 
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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1075 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1081
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SelectorExpressionContext(self, SParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1077
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1078 
                    localctx.selector = self.instance_selector() 
                self.state = 1083
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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



    class BlobExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.BlobExpressionContext, self).__init__(parser)
            self.exp = None # Blob_expressionContext
            self.copyFrom(ctx)

        def blob_expression(self):
            return self.getTypedRuleContext(SParser.Blob_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBlobExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBlobExpression(self)


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
        self.enterRule(localctx, 90, self.RULE_method_expression)
        try:
            self.state = 1091
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = SParser.BlobExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1084 
                localctx.exp = self.blob_expression()
                pass

            elif la_ == 2:
                localctx = SParser.DocumentExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1085 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 3:
                localctx = SParser.FetchExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1086 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 4:
                localctx = SParser.ReadExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1087 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 5:
                localctx = SParser.SortedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1088 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 6:
                localctx = SParser.MethodCallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1089 
                localctx.exp = self.method_call()
                pass

            elif la_ == 7:
                localctx = SParser.ConstructorExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1090 
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
        self.enterRule(localctx, 92, self.RULE_instance_selector)
        try:
            self.state = 1106
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1093
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1094
                self.match(SParser.DOT)
                self.state = 1095 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1096
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1097
                self.match(SParser.LBRAK)
                self.state = 1098 
                localctx.xslice = self.slice_arguments()
                self.state = 1099
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1101
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1102
                self.match(SParser.LBRAK)
                self.state = 1103 
                localctx.exp = self.expression(0)
                self.state = 1104
                self.match(SParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Blob_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(SParser.BLOB, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_blob_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = SParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_blob_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1108
            self.match(SParser.BLOB)
            self.state = 1109
            self.match(SParser.LPAR)
            self.state = 1111
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1110 
                self.expression(0)


            self.state = 1113
            self.match(SParser.RPAR)
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

        def DOCUMENT(self):
            return self.getToken(SParser.DOCUMENT, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


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
        self.enterRule(localctx, 96, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1115
            self.match(SParser.DOCUMENT)
            self.state = 1116
            self.match(SParser.LPAR)
            self.state = 1118
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1117 
                self.expression(0)


            self.state = 1120
            self.match(SParser.RPAR)
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
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(SParser.Mutable_category_typeContext,0)


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
        self.enterRule(localctx, 98, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1122 
            localctx.typ = self.mutable_category_type()
            self.state = 1123
            self.match(SParser.LPAR)
            self.state = 1125
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1124 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1127
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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1134
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = SParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1130 
                localctx.exp = self.expression(0)
                self.state = 1131
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = SParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1133 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentAssignmentListItemContext(self, SParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1136
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1137
                    self.match(SParser.COMMA)
                    self.state = 1138 
                    localctx.item = self.argument_assignment() 
                self.state = 1143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

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
        self.enterRule(localctx, 102, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1144 
            localctx.name = self.variable_identifier()
            self.state = 1145 
            self.assign()
            self.state = 1146 
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
        self.enterRule(localctx, 104, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1148
            self.match(SParser.READ)
            self.state = 1149
            self.match(SParser.FROM)
            self.state = 1150 
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
        self.enterRule(localctx, 106, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152
            self.match(SParser.WRITE)
            self.state = 1153 
            localctx.what = self.expression(0)
            self.state = 1154
            self.match(SParser.TO)
            self.state = 1155 
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
            self.typ = None # Mutable_category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def ONE(self):
            return self.getToken(SParser.ONE, 0)
        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(SParser.Mutable_category_typeContext,0)


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
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.typ = None # Mutable_category_typeContext
            self.xfilter = None # ExpressionContext
            self.xorder = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
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
        def ORDER(self):
            return self.getToken(SParser.ORDER, 0)
        def BY(self):
            return self.getToken(SParser.BY, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(SParser.Mutable_category_typeContext,0)

        def order_by_list(self):
            return self.getTypedRuleContext(SParser.Order_by_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchAll(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchAll(self)



    def fetch_expression(self):

        localctx = SParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_fetch_expression)
        self._la = 0 # Token type
        try:
            self.state = 1194
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = SParser.FetchListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1157
                self.match(SParser.FETCH)
                self.state = 1158 
                localctx.name = self.variable_identifier()
                self.state = 1159
                self.match(SParser.FROM)
                self.state = 1160 
                localctx.source = self.expression(0)
                self.state = 1161
                self.match(SParser.WHERE)
                self.state = 1162 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1164
                self.match(SParser.FETCH)
                self.state = 1165
                self.match(SParser.ONE)
                self.state = 1167
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE or _la==SParser.TYPE_IDENTIFIER:
                    self.state = 1166 
                    localctx.typ = self.mutable_category_type()


                self.state = 1169
                self.match(SParser.WHERE)
                self.state = 1170 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.FetchAllContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1171
                self.match(SParser.FETCH)
                self.state = 1178
                token = self._input.LA(1)
                if token in [SParser.ALL]:
                    self.state = 1172
                    self.match(SParser.ALL)

                elif token in [SParser.ROWS]:
                    self.state = 1173
                    self.match(SParser.ROWS)
                    self.state = 1174 
                    localctx.xstart = self.expression(0)
                    self.state = 1175
                    self.match(SParser.TO)
                    self.state = 1176 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1180
                self.match(SParser.LPAR)
                self.state = 1182
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE or _la==SParser.TYPE_IDENTIFIER:
                    self.state = 1181 
                    localctx.typ = self.mutable_category_type()


                self.state = 1184
                self.match(SParser.RPAR)
                self.state = 1187
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 1185
                    self.match(SParser.WHERE)
                    self.state = 1186 
                    localctx.xfilter = self.expression(0)


                self.state = 1192
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 1189
                    self.match(SParser.ORDER)
                    self.state = 1190
                    self.match(SParser.BY)
                    self.state = 1191 
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
        self.enterRule(localctx, 110, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1196
            self.match(SParser.SORTED)
            self.state = 1197
            self.match(SParser.LPAR)
            self.state = 1198 
            localctx.source = self.instance_expression(0)
            self.state = 1204
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 1199
                self.match(SParser.COMMA)
                self.state = 1200 
                self.key_token()
                self.state = 1201
                self.match(SParser.EQ)
                self.state = 1202 
                localctx.key = self.instance_expression(0)


            self.state = 1206
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
        self.enterRule(localctx, 112, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1208 
            localctx.inst = self.assignable_instance(0)
            self.state = 1209 
            self.assign()
            self.state = 1210 
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
        self.enterRule(localctx, 114, self.RULE_child_instance)
        try:
            self.state = 1220
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1212
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1213
                self.match(SParser.DOT)
                self.state = 1214 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1215
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1216
                self.match(SParser.LBRAK)
                self.state = 1217 
                localctx.exp = self.expression(0)
                self.state = 1218
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
        self.enterRule(localctx, 116, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1222 
            localctx.items = self.variable_identifier_list()
            self.state = 1223 
            self.assign()
            self.state = 1224 
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
        self.enterRule(localctx, 118, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1226
                    self.match(SParser.LF) 
                self.state = 1231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
        self.enterRule(localctx, 120, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1233 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1232
                self.match(SParser.LF)
                self.state = 1235 
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
        self.enterRule(localctx, 122, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1238 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1237
                self.match(SParser.LF)
                self.state = 1240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SParser.LF):
                    break

            self.state = 1242
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
        self.enterRule(localctx, 124, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.LF:
                self.state = 1244
                self.match(SParser.LF)
                self.state = 1249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1250
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
        self.enterRule(localctx, 126, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1252
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
        self.enterRule(localctx, 128, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = SParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1255
            _la = self._input.LA(1)
            if _la==SParser.COMMENT or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (SParser.ABSTRACT - 65)) | (1 << (SParser.ATTR - 65)) | (1 << (SParser.CATEGORY - 65)) | (1 << (SParser.CLASS - 65)) | (1 << (SParser.DEF - 65)) | (1 << (SParser.ENUM - 65)) | (1 << (SParser.NATIVE - 65)))) != 0) or _la==SParser.SINGLETON or _la==SParser.STORABLE:
                self.state = 1254 
                localctx.items = self.declarations(0)


            self.state = 1257 
            self.lfs()
            self.state = 1258
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
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1261 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.DeclarationListItemContext(self, SParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1263
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1264 
                    self.lfp()
                    self.state = 1265 
                    localctx.item = self.declaration() 
                self.state = 1271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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

        def attribute_declaration(self):
            return self.getTypedRuleContext(SParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(SParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(SParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(SParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(SParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = SParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMENT:
                self.state = 1272 
                self.comment_statement()
                self.state = 1273 
                self.lfp()
                self.state = 1279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1285
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.state = 1280 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1281 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1282 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1283 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1284 
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
        self.enterRule(localctx, 134, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1287 
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
        self.enterRule(localctx, 136, self.RULE_enum_declaration)
        try:
            self.state = 1291
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = SParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1289 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1290 
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
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1294 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeSymbolListItemContext(self, SParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1296
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1297 
                    self.lfp()
                    self.state = 1298 
                    localctx.item = self.native_symbol() 
                self.state = 1304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1306 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CategorySymbolListItemContext(self, SParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1308
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1309 
                    self.lfp()
                    self.state = 1310 
                    localctx.item = self.category_symbol() 
                self.state = 1316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

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
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1318 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SymbolListItemContext(self, SParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1320
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1321
                    self.match(SParser.COMMA)
                    self.state = 1322 
                    localctx.item = self.symbol_identifier() 
                self.state = 1327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

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
        self.enterRule(localctx, 144, self.RULE_attribute_constraint)
        try:
            self.state = 1338
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                localctx = SParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1328
                self.match(SParser.IN)
                self.state = 1329 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = SParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1330
                self.match(SParser.IN)
                self.state = 1331 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = SParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1332
                self.match(SParser.IN)
                self.state = 1333 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = SParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1334
                self.match(SParser.MATCHING)
                self.state = 1335
                localctx.text = self.match(SParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = SParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1336
                self.match(SParser.MATCHING)
                self.state = 1337 
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
        self.enterRule(localctx, 146, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1340
            self.match(SParser.LBRAK)
            self.state = 1342
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1341 
                localctx.items = self.expression_list(0)


            self.state = 1344
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
        self.enterRule(localctx, 148, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1346
            self.match(SParser.LT)
            self.state = 1348
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1347 
                localctx.items = self.expression_list(0)


            self.state = 1350
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
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1353 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ValueListItemContext(self, SParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1355
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1356
                    self.match(SParser.COMMA)
                    self.state = 1357 
                    localctx.item = self.expression(0) 
                self.state = 1362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
        self.enterRule(localctx, 152, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1363
            self.match(SParser.LBRAK)
            self.state = 1364 
            localctx.low = self.expression(0)
            self.state = 1365
            self.match(SParser.RANGE)
            self.state = 1366 
            localctx.high = self.expression(0)
            self.state = 1367
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
        _startState = 154
        self.enterRecursionRule(localctx, 154, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1370 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1380
                    la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
                    if la_ == 1:
                        localctx = SParser.SetTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1372
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1373
                        self.match(SParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = SParser.ListTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1374
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1375
                        self.match(SParser.LBRAK)
                        self.state = 1376
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = SParser.DictTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1377
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1378
                        self.match(SParser.LCURL)
                        self.state = 1379
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

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
        self.enterRule(localctx, 156, self.RULE_primary_type)
        try:
            self.state = 1387
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID]:
                localctx = SParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1385 
                localctx.n = self.native_type()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1386 
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



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(SParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(SParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(SParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(SParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DecimalTypeContext, self).__init__(parser)
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
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(SParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = SParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_native_type)
        try:
            self.state = 1403
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN]:
                localctx = SParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1389
                self.match(SParser.BOOLEAN)

            elif token in [SParser.CHARACTER]:
                localctx = SParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1390
                self.match(SParser.CHARACTER)

            elif token in [SParser.TEXT]:
                localctx = SParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1391
                self.match(SParser.TEXT)

            elif token in [SParser.IMAGE]:
                localctx = SParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1392
                self.match(SParser.IMAGE)

            elif token in [SParser.INTEGER]:
                localctx = SParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1393
                self.match(SParser.INTEGER)

            elif token in [SParser.DECIMAL]:
                localctx = SParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1394
                self.match(SParser.DECIMAL)

            elif token in [SParser.DOCUMENT]:
                localctx = SParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1395
                self.match(SParser.DOCUMENT)

            elif token in [SParser.DATE]:
                localctx = SParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1396
                self.match(SParser.DATE)

            elif token in [SParser.DATETIME]:
                localctx = SParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1397
                self.match(SParser.DATETIME)

            elif token in [SParser.TIME]:
                localctx = SParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1398
                self.match(SParser.TIME)

            elif token in [SParser.PERIOD]:
                localctx = SParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1399
                self.match(SParser.PERIOD)

            elif token in [SParser.CODE]:
                localctx = SParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1400
                self.match(SParser.CODE)

            elif token in [SParser.BLOB]:
                localctx = SParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1401
                self.match(SParser.BLOB)

            elif token in [SParser.UUID]:
                localctx = SParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1402
                self.match(SParser.UUID)

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
        self.enterRule(localctx, 160, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1405
            localctx.t1 = self.match(SParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

        def getRuleIndex(self):
            return SParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = SParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1408
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1407
                self.match(SParser.MUTABLE)


            self.state = 1410 
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
        self.enterRule(localctx, 164, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1412
            localctx.t1 = self.match(SParser.CODE)
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
        self.enterRule(localctx, 166, self.RULE_category_declaration)
        try:
            self.state = 1417
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                localctx = SParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1414 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1415 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1416 
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
        _startState = 168
        self.enterRecursionRule(localctx, 168, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1420 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.TypeIdentifierListItemContext(self, SParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1422
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1423
                    self.match(SParser.COMMA)
                    self.state = 1424 
                    localctx.item = self.type_identifier() 
                self.state = 1429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

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
        self.enterRule(localctx, 170, self.RULE_method_identifier)
        try:
            self.state = 1432
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1430 
                localctx.name = self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1431 
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
        self.enterRule(localctx, 172, self.RULE_identifier)
        try:
            self.state = 1437
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1434 
                localctx.name = self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1435 
                localctx.name = self.type_identifier()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                localctx = SParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1436 
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
        self.enterRule(localctx, 174, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1439
            self.match(SParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def getRuleIndex(self):
            return SParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = SParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1441
            _la = self._input.LA(1)
            if not(_la==SParser.STORABLE or _la==SParser.VARIABLE_IDENTIFIER):
                self._errHandler.recoverInline(self)
            self.consume()
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
        self.enterRule(localctx, 178, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1443
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
        self.enterRule(localctx, 180, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1445
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
        _startState = 182
        self.enterRecursionRule(localctx, 182, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1448 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentListItemContext(self, SParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1450
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1451
                    self.match(SParser.COMMA)
                    self.state = 1452 
                    localctx.item = self.argument() 
                self.state = 1457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

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
        self.enterRule(localctx, 184, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1463
            token = self._input.LA(1)
            if token in [SParser.CODE]:
                localctx = SParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1458 
                localctx.arg = self.code_argument()

            elif token in [SParser.MUTABLE, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1460
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE:
                    self.state = 1459
                    self.match(SParser.MUTABLE)


                self.state = 1462 
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
        self.enterRule(localctx, 186, self.RULE_operator_argument)
        try:
            self.state = 1467
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                localctx = SParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1465 
                localctx.arg = self.named_argument()
                pass

            elif la_ == 2:
                localctx = SParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1466 
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
        self.enterRule(localctx, 188, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1469 
            localctx.name = self.variable_identifier()
            self.state = 1472
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 1470
                self.match(SParser.EQ)
                self.state = 1471 
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
        self.enterRule(localctx, 190, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1474 
            self.code_type()
            self.state = 1475 
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
        self.enterRule(localctx, 192, self.RULE_category_or_any_type)
        try:
            self.state = 1479
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID, SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1477 
                localctx.typ = self.typedef(0)

            elif token in [SParser.ANY]:
                localctx = SParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1478 
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
        _startState = 194
        self.enterRecursionRule(localctx, 194, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1482
            self.match(SParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1492
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1490
                    la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
                    if la_ == 1:
                        localctx = SParser.AnyListTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1484
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1485
                        self.match(SParser.LBRAK)
                        self.state = 1486
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = SParser.AnyDictTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1487
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1488
                        self.match(SParser.LCURL)
                        self.state = 1489
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1494
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

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
        _startState = 196
        self.enterRecursionRule(localctx, 196, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1496 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CategoryMethodListItemContext(self, SParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1498
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1499 
                    self.lfp()
                    self.state = 1500 
                    localctx.item = self.member_method_declaration() 
                self.state = 1506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

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
        self.enterRule(localctx, 198, self.RULE_member_method_declaration)
        try:
            self.state = 1512
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1507 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1508 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1509 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1510 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1511 
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
        _startState = 200
        self.enterRecursionRule(localctx, 200, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1515 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1523
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,99,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryMethodListItemContext(self, SParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1517
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1518 
                    self.lfp()
                    self.state = 1519 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1525
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,99,self._ctx)

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

        def native_getter_declaration(self):
            return self.getTypedRuleContext(SParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(SParser.Native_setter_declarationContext,0)


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
        self.enterRule(localctx, 202, self.RULE_native_member_method_declaration)
        try:
            self.state = 1529
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1526 
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1527 
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1528 
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
        self.enterRule(localctx, 204, self.RULE_native_category_binding)
        try:
            self.state = 1541
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1531
                self.match(SParser.JAVA)
                self.state = 1532 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1533
                self.match(SParser.CSHARP)
                self.state = 1534 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1535
                self.match(SParser.PYTHON2)
                self.state = 1536 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1537
                self.match(SParser.PYTHON3)
                self.state = 1538 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1539
                self.match(SParser.JAVASCRIPT)
                self.state = 1540 
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
        self.enterRule(localctx, 206, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1543 
            localctx.id_ = self.identifier()
            self.state = 1545
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1544 
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
        self.enterRule(localctx, 208, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1547
            self.match(SParser.FROM)
            self.state = 1548 
            self.module_token()
            self.state = 1549
            self.match(SParser.COLON)
            self.state = 1550 
            self.identifier()
            self.state = 1555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,103,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1551
                    self.match(SParser.DOT)
                    self.state = 1552 
                    self.identifier() 
                self.state = 1557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

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
        self.enterRule(localctx, 210, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1558
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1559
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
        self.enterRule(localctx, 212, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1561 
            localctx.id_ = self.identifier()
            self.state = 1563
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 1562 
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
        self.enterRule(localctx, 214, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1565
            self.match(SParser.FROM)
            self.state = 1566 
            self.module_token()
            self.state = 1567
            self.match(SParser.COLON)
            self.state = 1569
            _la = self._input.LA(1)
            if _la==SParser.SLASH:
                self.state = 1568
                self.match(SParser.SLASH)


            self.state = 1571 
            self.javascript_identifier()
            self.state = 1576
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1572
                    self.match(SParser.SLASH)
                    self.state = 1573 
                    self.javascript_identifier() 
                self.state = 1578
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

            self.state = 1581
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                self.state = 1579
                self.match(SParser.DOT)
                self.state = 1580 
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

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = SParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1583 
            self.variable_identifier()
            self.state = 1588
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1584
                self.match(SParser.COMMA)
                self.state = 1585 
                self.variable_identifier()
                self.state = 1590
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = SParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1591 
            self.attribute_identifier()
            self.state = 1596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1592
                self.match(SParser.COMMA)
                self.state = 1593 
                self.attribute_identifier()
                self.state = 1598
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 220, self.RULE_method_declaration)
        try:
            self.state = 1603
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = SParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1599 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1600 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1601 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = SParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1602 
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
        self.enterRule(localctx, 222, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1605
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
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1608 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1616
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeStatementListItemContext(self, SParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1610
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1611 
                    self.lfp()
                    self.state = 1612 
                    localctx.item = self.native_statement() 
                self.state = 1618
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

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
        self.enterRule(localctx, 226, self.RULE_native_statement)
        try:
            self.state = 1629
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1619
                self.match(SParser.JAVA)
                self.state = 1620 
                localctx.stmt = self.java_statement()

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1621
                self.match(SParser.CSHARP)
                self.state = 1622 
                localctx.stmt = self.csharp_statement()

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1623
                self.match(SParser.PYTHON2)
                self.state = 1624 
                localctx.stmt = self.python_native_statement()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1625
                self.match(SParser.PYTHON3)
                self.state = 1626 
                localctx.stmt = self.python_native_statement()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1627
                self.match(SParser.JAVASCRIPT)
                self.state = 1628 
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
        self.enterRule(localctx, 228, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631 
            localctx.stmt = self.python_statement()
            self.state = 1633
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 1632
                self.match(SParser.SEMI)


            self.state = 1636
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.state = 1635 
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
        self.enterRule(localctx, 230, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1638 
            localctx.stmt = self.javascript_statement()
            self.state = 1640
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                self.state = 1639
                self.match(SParser.SEMI)


            self.state = 1643
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                self.state = 1642 
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
        _startState = 232
        self.enterRecursionRule(localctx, 232, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1646 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1654
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.StatementListItemContext(self, SParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1648
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1649 
                    self.lfp()
                    self.state = 1650 
                    localctx.item = self.statement() 
                self.state = 1656
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

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
        _startState = 234
        self.enterRecursionRule(localctx, 234, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1658 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1666
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.AssertionListItemContext(self, SParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1660
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1661 
                    self.lfp()
                    self.state = 1662 
                    localctx.item = self.assertion() 
                self.state = 1668
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

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
        _startState = 236
        self.enterRecursionRule(localctx, 236, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1670 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1678
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SwitchCaseStatementListItemContext(self, SParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1672
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1673 
                    self.lfp()
                    self.state = 1674 
                    localctx.item = self.switch_case_statement() 
                self.state = 1680
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

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
        _startState = 238
        self.enterRecursionRule(localctx, 238, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1682 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1690
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,120,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CatchStatementListItemContext(self, SParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1684
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1685 
                    self.lfp()
                    self.state = 1686 
                    localctx.item = self.catch_statement() 
                self.state = 1692
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,120,self._ctx)

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
        self.enterRule(localctx, 240, self.RULE_literal_collection)
        try:
            self.state = 1707
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                localctx = SParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1693
                self.match(SParser.LBRAK)
                self.state = 1694 
                localctx.low = self.atomic_literal()
                self.state = 1695
                self.match(SParser.RANGE)
                self.state = 1696 
                localctx.high = self.atomic_literal()
                self.state = 1697
                self.match(SParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = SParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1699
                self.match(SParser.LBRAK)
                self.state = 1700 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1701
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1703
                self.match(SParser.LT)
                self.state = 1704 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1705
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
        self.enterRule(localctx, 242, self.RULE_atomic_literal)
        try:
            self.state = 1722
            token = self._input.LA(1)
            if token in [SParser.MIN_INTEGER]:
                localctx = SParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1709
                localctx.t = self.match(SParser.MIN_INTEGER)

            elif token in [SParser.MAX_INTEGER]:
                localctx = SParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1710
                localctx.t = self.match(SParser.MAX_INTEGER)

            elif token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1711
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.HEXA_LITERAL]:
                localctx = SParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1712
                localctx.t = self.match(SParser.HEXA_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1713
                localctx.t = self.match(SParser.CHAR_LITERAL)

            elif token in [SParser.DATE_LITERAL]:
                localctx = SParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1714
                localctx.t = self.match(SParser.DATE_LITERAL)

            elif token in [SParser.TIME_LITERAL]:
                localctx = SParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1715
                localctx.t = self.match(SParser.TIME_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1716
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1717
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.DATETIME_LITERAL]:
                localctx = SParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1718
                localctx.t = self.match(SParser.DATETIME_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1719
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.PERIOD_LITERAL]:
                localctx = SParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1720
                localctx.t = self.match(SParser.PERIOD_LITERAL)

            elif token in [SParser.NONE]:
                localctx = SParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1721 
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
        _startState = 244
        self.enterRecursionRule(localctx, 244, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1725 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1732
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.LiteralListItemContext(self, SParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1727
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1728
                    self.match(SParser.COMMA)
                    self.state = 1729 
                    localctx.item = self.atomic_literal() 
                self.state = 1734
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

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
        self.enterRule(localctx, 246, self.RULE_selectable_expression)
        try:
            self.state = 1739
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                localctx = SParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1735 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1736 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = SParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1737 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = SParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1738 
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
        self.enterRule(localctx, 248, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1741
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
        self.enterRule(localctx, 250, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1743
            self.match(SParser.LPAR)
            self.state = 1744 
            localctx.exp = self.expression(0)
            self.state = 1745
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
        self.enterRule(localctx, 252, self.RULE_literal_expression)
        try:
            self.state = 1749
            token = self._input.LA(1)
            if token in [SParser.NONE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.MIN_INTEGER, SParser.MAX_INTEGER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.HEXA_LITERAL, SParser.DECIMAL_LITERAL, SParser.DATETIME_LITERAL, SParser.TIME_LITERAL, SParser.DATE_LITERAL, SParser.PERIOD_LITERAL]:
                localctx = SParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1747 
                localctx.exp = self.atomic_literal()

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.LCURL, SParser.LT]:
                localctx = SParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1748 
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
        self.enterRule(localctx, 254, self.RULE_collection_literal)
        try:
            self.state = 1756
            la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
            if la_ == 1:
                localctx = SParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1751 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = SParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1752 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = SParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1753 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = SParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1754 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = SParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1755 
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
        self.enterRule(localctx, 256, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1758
            self.match(SParser.LPAR)
            self.state = 1760
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1759 
                localctx.items = self.expression_tuple(0)


            self.state = 1762
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
        self.enterRule(localctx, 258, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1764
            self.match(SParser.LCURL)
            self.state = 1766
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1765 
                localctx.items = self.dict_entry_list(0)


            self.state = 1768
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
        _startState = 260
        self.enterRecursionRule(localctx, 260, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1771 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1778
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ValueTupleItemContext(self, SParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1773
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1774
                    self.match(SParser.COMMA)
                    self.state = 1775 
                    localctx.item = self.expression(0) 
                self.state = 1780
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

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
        _startState = 262
        self.enterRecursionRule(localctx, 262, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1782 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1789
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.DictEntryListItemContext(self, SParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1784
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1785
                    self.match(SParser.COMMA)
                    self.state = 1786 
                    localctx.item = self.dict_entry() 
                self.state = 1791
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

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
        self.enterRule(localctx, 264, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1792 
            localctx.key = self.expression(0)
            self.state = 1793
            self.match(SParser.COLON)
            self.state = 1794 
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
        self.enterRule(localctx, 266, self.RULE_slice_arguments)
        try:
            self.state = 1805
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                localctx = SParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1796 
                localctx.first = self.expression(0)
                self.state = 1797
                self.match(SParser.COLON)
                self.state = 1798 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1800 
                localctx.first = self.expression(0)
                self.state = 1801
                self.match(SParser.COLON)
                pass

            elif la_ == 3:
                localctx = SParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1803
                self.match(SParser.COLON)
                self.state = 1804 
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
        self.enterRule(localctx, 268, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1807 
            localctx.name = self.variable_identifier()
            self.state = 1808 
            self.assign()
            self.state = 1809 
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
        _startState = 270
        self.enterRecursionRule(localctx, 270, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1812 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1818
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,132,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ChildInstanceContext(self, SParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1814
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1815 
                    localctx.child = self.child_instance() 
                self.state = 1820
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,132,self._ctx)

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
        self.enterRule(localctx, 272, self.RULE_is_expression)
        try:
            self.state = 1825
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                localctx = SParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1821
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1822
                self.match(SParser.VARIABLE_IDENTIFIER)
                self.state = 1823 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = SParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1824 
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
            super(SParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Order_byContext)
            else:
                return self.getTypedRuleContext(SParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_order_by_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = SParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1827 
            self.order_by()
            self.state = 1832
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,134,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1828
                    self.match(SParser.COMMA)
                    self.state = 1829 
                    self.order_by() 
                self.state = 1834
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,134,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(SParser.DOT)
            else:
                return self.getToken(SParser.DOT, i)

        def ASC(self):
            return self.getToken(SParser.ASC, 0)

        def DESC(self):
            return self.getToken(SParser.DESC, 0)

        def getRuleIndex(self):
            return SParser.RULE_order_by

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = SParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1835 
            self.variable_identifier()
            self.state = 1840
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,135,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1836
                    self.match(SParser.DOT)
                    self.state = 1837 
                    self.variable_identifier() 
                self.state = 1842
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,135,self._ctx)

            self.state = 1844
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                self.state = 1843
                _la = self._input.LA(1)
                if not(_la==SParser.ASC or _la==SParser.DESC):
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
        self.enterRule(localctx, 278, self.RULE_operator)
        try:
            self.state = 1852
            token = self._input.LA(1)
            if token in [SParser.PLUS]:
                localctx = SParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1846
                self.match(SParser.PLUS)

            elif token in [SParser.MINUS]:
                localctx = SParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1847
                self.match(SParser.MINUS)

            elif token in [SParser.STAR]:
                localctx = SParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1848 
                self.multiply()

            elif token in [SParser.SLASH]:
                localctx = SParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1849 
                self.divide()

            elif token in [SParser.BSLASH]:
                localctx = SParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1850 
                self.idivide()

            elif token in [SParser.PERCENT, SParser.MODULO]:
                localctx = SParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1851 
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
            super(SParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = SParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1854
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1855
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
        self.enterRule(localctx, 282, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1857
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1858
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
        self.enterRule(localctx, 284, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1860
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1861
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
        self.enterRule(localctx, 286, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1863
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1864
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
        self.enterRule(localctx, 288, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1866
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
        self.enterRule(localctx, 290, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1868
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
        self.enterRule(localctx, 292, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1870
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
        self.enterRule(localctx, 294, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1872
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
        self.enterRule(localctx, 296, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1874
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
        self.enterRule(localctx, 298, self.RULE_javascript_statement)
        try:
            self.state = 1883
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1876
                self.match(SParser.RETURN)
                self.state = 1877 
                localctx.exp = self.javascript_expression(0)
                self.state = 1878
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1880 
                localctx.exp = self.javascript_expression(0)
                self.state = 1881
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
        _startState = 300
        self.enterRecursionRule(localctx, 300, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1886 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1892
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptSelectorExpressionContext(self, SParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1888
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1889 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1894
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

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


        def javascript_new_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_new_expressionContext,0)


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
        self.enterRule(localctx, 302, self.RULE_javascript_primary_expression)
        try:
            self.state = 1902
            la_ = self._interp.adaptivePredict(self._input,140,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1895 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1896 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1897 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1898 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1899 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1900 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1901 
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
        self.enterRule(localctx, 304, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1904 
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
            super(SParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(SParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = SParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1906 
            self.new_token()
            self.state = 1907 
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
        self.enterRule(localctx, 308, self.RULE_javascript_selector_expression)
        try:
            self.state = 1914
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = SParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1909
                self.match(SParser.DOT)
                self.state = 1910 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = SParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1911
                self.match(SParser.DOT)
                self.state = 1912 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = SParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1913 
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
        self.enterRule(localctx, 310, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1916 
            localctx.name = self.javascript_identifier()
            self.state = 1917
            self.match(SParser.LPAR)
            self.state = 1919
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 1918 
                localctx.args = self.javascript_arguments(0)


            self.state = 1921
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
        _startState = 312
        self.enterRecursionRule(localctx, 312, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1924 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1931
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,143,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptArgumentListItemContext(self, SParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1926
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1927
                    self.match(SParser.COMMA)
                    self.state = 1928 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1933
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,143,self._ctx)

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
        self.enterRule(localctx, 314, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1934
            self.match(SParser.LBRAK)
            self.state = 1935 
            localctx.exp = self.javascript_expression(0)
            self.state = 1936
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
        self.enterRule(localctx, 316, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1938
            self.match(SParser.LPAR)
            self.state = 1939 
            localctx.exp = self.javascript_expression(0)
            self.state = 1940
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
        self.enterRule(localctx, 318, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1942 
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
        self.enterRule(localctx, 320, self.RULE_javascript_literal_expression)
        try:
            self.state = 1949
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1944
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1945
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1946
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1947
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1948
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
        self.enterRule(localctx, 322, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1951
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)))) != 0)):
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
        self.enterRule(localctx, 324, self.RULE_python_statement)
        try:
            self.state = 1956
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1953
                self.match(SParser.RETURN)
                self.state = 1954 
                localctx.exp = self.python_expression(0)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1955 
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
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1959 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1965
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonSelectorExpressionContext(self, SParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1961
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1962 
                    localctx.child = self.python_selector_expression() 
                self.state = 1967
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

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
        self.enterRule(localctx, 328, self.RULE_python_primary_expression)
        try:
            self.state = 1972
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1968 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1969 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1970 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = SParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1971 
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
        self.enterRule(localctx, 330, self.RULE_python_selector_expression)
        try:
            self.state = 1980
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1974
                self.match(SParser.DOT)
                self.state = 1975 
                localctx.exp = self.python_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1976
                self.match(SParser.LBRAK)
                self.state = 1977 
                localctx.exp = self.python_expression(0)
                self.state = 1978
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
        self.enterRule(localctx, 332, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1982 
            localctx.name = self.python_identifier()
            self.state = 1983
            self.match(SParser.LPAR)
            self.state = 1985
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 1984 
                localctx.args = self.python_argument_list()


            self.state = 1987
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
        self.enterRule(localctx, 334, self.RULE_python_argument_list)
        try:
            self.state = 1995
            la_ = self._interp.adaptivePredict(self._input,150,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1989 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = SParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1990 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1991 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1992
                self.match(SParser.COMMA)
                self.state = 1993 
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
        _startState = 336
        self.enterRecursionRule(localctx, 336, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1998 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2005
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonOrdinalArgumentListItemContext(self, SParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2000
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2001
                    self.match(SParser.COMMA)
                    self.state = 2002 
                    localctx.item = self.python_expression(0) 
                self.state = 2007
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

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
        _startState = 338
        self.enterRecursionRule(localctx, 338, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2009 
            localctx.name = self.python_identifier()
            self.state = 2010
            self.match(SParser.EQ)
            self.state = 2011 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2021
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonNamedArgumentListItemContext(self, SParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2013
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2014
                    self.match(SParser.COMMA)
                    self.state = 2015 
                    localctx.name = self.python_identifier()
                    self.state = 2016
                    self.match(SParser.EQ)
                    self.state = 2017 
                    localctx.exp = self.python_expression(0) 
                self.state = 2023
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

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
        self.enterRule(localctx, 340, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2024
            self.match(SParser.LPAR)
            self.state = 2025 
            localctx.exp = self.python_expression(0)
            self.state = 2026
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
        _startState = 342
        self.enterRecursionRule(localctx, 342, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2031
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2029
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2030 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2038
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonChildIdentifierContext(self, SParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2033
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2034
                    self.match(SParser.DOT)
                    self.state = 2035 
                    localctx.name = self.python_identifier() 
                self.state = 2040
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

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
        self.enterRule(localctx, 344, self.RULE_python_literal_expression)
        try:
            self.state = 2046
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2041
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2042
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2043
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2044
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2045
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
        self.enterRule(localctx, 346, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2048
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)))) != 0)):
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
        self.enterRule(localctx, 348, self.RULE_java_statement)
        try:
            self.state = 2057
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2050
                self.match(SParser.RETURN)
                self.state = 2051 
                localctx.exp = self.java_expression(0)
                self.state = 2052
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.NATIVE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2054 
                localctx.exp = self.java_expression(0)
                self.state = 2055
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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2060 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2066
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaSelectorExpressionContext(self, SParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2062
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2063 
                    localctx.child = self.java_selector_expression() 
                self.state = 2068
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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


        def java_new_expression(self):
            return self.getTypedRuleContext(SParser.Java_new_expressionContext,0)


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
        self.enterRule(localctx, 352, self.RULE_java_primary_expression)
        try:
            self.state = 2074
            la_ = self._interp.adaptivePredict(self._input,158,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2069 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2070 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2071 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2072 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2073 
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
        self.enterRule(localctx, 354, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2076 
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
            super(SParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(SParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(SParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_new_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = SParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2078 
            self.new_token()
            self.state = 2079 
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
        self.enterRule(localctx, 358, self.RULE_java_selector_expression)
        try:
            self.state = 2084
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2081
                self.match(SParser.DOT)
                self.state = 2082 
                localctx.exp = self.java_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2083 
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
        self.enterRule(localctx, 360, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2086 
            localctx.name = self.java_identifier()
            self.state = 2087
            self.match(SParser.LPAR)
            self.state = 2089
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.NATIVE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 2088 
                localctx.args = self.java_arguments(0)


            self.state = 2091
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
        _startState = 362
        self.enterRecursionRule(localctx, 362, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2094 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaArgumentListItemContext(self, SParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2096
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2097
                    self.match(SParser.COMMA)
                    self.state = 2098 
                    localctx.item = self.java_expression(0) 
                self.state = 2103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

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
        self.enterRule(localctx, 364, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2104
            self.match(SParser.LBRAK)
            self.state = 2105 
            localctx.exp = self.java_expression(0)
            self.state = 2106
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
        self.enterRule(localctx, 366, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2108
            self.match(SParser.LPAR)
            self.state = 2109 
            localctx.exp = self.java_expression(0)
            self.state = 2110
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
        _startState = 368
        self.enterRecursionRule(localctx, 368, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2113 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildIdentifierContext(self, SParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2115
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2116
                    self.match(SParser.DOT)
                    self.state = 2117 
                    localctx.name = self.java_identifier() 
                self.state = 2122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

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
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2124 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,163,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildClassIdentifierContext(self, SParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2126
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2127
                    localctx.name = self.match(SParser.DOLLAR_IDENTIFIER) 
                self.state = 2132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,163,self._ctx)

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
        self.enterRule(localctx, 372, self.RULE_java_literal_expression)
        try:
            self.state = 2138
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2133
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2134
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2135
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2136
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2137
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
        self.enterRule(localctx, 374, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.NATIVE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)))) != 0)):
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
        self.enterRule(localctx, 376, self.RULE_csharp_statement)
        try:
            self.state = 2149
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2142
                self.match(SParser.RETURN)
                self.state = 2143 
                localctx.exp = self.csharp_expression(0)
                self.state = 2144
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2146 
                localctx.exp = self.csharp_expression(0)
                self.state = 2147
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
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2152 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpSelectorExpressionContext(self, SParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2154
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2155 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

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


        def csharp_new_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_new_expressionContext,0)


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
        self.enterRule(localctx, 380, self.RULE_csharp_primary_expression)
        try:
            self.state = 2166
            la_ = self._interp.adaptivePredict(self._input,167,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2161 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2162 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2163 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2164 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2165 
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
        self.enterRule(localctx, 382, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2168 
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
            super(SParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(SParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = SParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2170 
            self.new_token()
            self.state = 2171 
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
        self.enterRule(localctx, 386, self.RULE_csharp_selector_expression)
        try:
            self.state = 2176
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2173
                self.match(SParser.DOT)
                self.state = 2174 
                localctx.exp = self.csharp_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2175 
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
        self.enterRule(localctx, 388, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2178 
            localctx.name = self.csharp_identifier()
            self.state = 2179
            self.match(SParser.LPAR)
            self.state = 2181
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 2180 
                localctx.args = self.csharp_arguments(0)


            self.state = 2183
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
        _startState = 390
        self.enterRecursionRule(localctx, 390, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2186 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,170,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpArgumentListItemContext(self, SParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2188
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2189
                    self.match(SParser.COMMA)
                    self.state = 2190 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,170,self._ctx)

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
        self.enterRule(localctx, 392, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2196
            self.match(SParser.LBRAK)
            self.state = 2197 
            localctx.exp = self.csharp_expression(0)
            self.state = 2198
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
        self.enterRule(localctx, 394, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2200
            self.match(SParser.LPAR)
            self.state = 2201 
            localctx.exp = self.csharp_expression(0)
            self.state = 2202
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
        _startState = 396
        self.enterRecursionRule(localctx, 396, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2207
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2205
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.TEST, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2206 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpChildIdentifierContext(self, SParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2209
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2210
                    self.match(SParser.DOT)
                    self.state = 2211 
                    localctx.name = self.csharp_identifier() 
                self.state = 2216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

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
        self.enterRule(localctx, 398, self.RULE_csharp_literal_expression)
        try:
            self.state = 2222
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2217
                self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2218
                self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2219
                self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2220
                self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2221
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
        self.enterRule(localctx, 400, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)))) != 0)):
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
        self._predicates[16] = self.native_category_binding_list_sempred
        self._predicates[27] = self.callable_parent_sempred
        self._predicates[37] = self.else_if_statement_list_sempred
        self._predicates[42] = self.expression_sempred
        self._predicates[44] = self.instance_expression_sempred
        self._predicates[46] = self.instance_selector_sempred
        self._predicates[50] = self.argument_assignment_list_sempred
        self._predicates[57] = self.child_instance_sempred
        self._predicates[65] = self.declarations_sempred
        self._predicates[69] = self.native_symbol_list_sempred
        self._predicates[70] = self.category_symbol_list_sempred
        self._predicates[71] = self.symbol_list_sempred
        self._predicates[75] = self.expression_list_sempred
        self._predicates[77] = self.typedef_sempred
        self._predicates[84] = self.type_identifier_list_sempred
        self._predicates[91] = self.argument_list_sempred
        self._predicates[97] = self.any_type_sempred
        self._predicates[98] = self.member_method_declaration_list_sempred
        self._predicates[100] = self.native_member_method_declaration_list_sempred
        self._predicates[105] = self.module_token_sempred
        self._predicates[112] = self.native_statement_list_sempred
        self._predicates[116] = self.statement_list_sempred
        self._predicates[117] = self.assertion_list_sempred
        self._predicates[118] = self.switch_case_statement_list_sempred
        self._predicates[119] = self.catch_statement_list_sempred
        self._predicates[122] = self.literal_list_literal_sempred
        self._predicates[130] = self.expression_tuple_sempred
        self._predicates[131] = self.dict_entry_list_sempred
        self._predicates[135] = self.assignable_instance_sempred
        self._predicates[136] = self.is_expression_sempred
        self._predicates[140] = self.new_token_sempred
        self._predicates[141] = self.key_token_sempred
        self._predicates[142] = self.value_token_sempred
        self._predicates[143] = self.symbols_token_sempred
        self._predicates[150] = self.javascript_expression_sempred
        self._predicates[156] = self.javascript_arguments_sempred
        self._predicates[163] = self.python_expression_sempred
        self._predicates[168] = self.python_ordinal_argument_list_sempred
        self._predicates[169] = self.python_named_argument_list_sempred
        self._predicates[171] = self.python_identifier_expression_sempred
        self._predicates[175] = self.java_expression_sempred
        self._predicates[181] = self.java_arguments_sempred
        self._predicates[184] = self.java_identifier_expression_sempred
        self._predicates[185] = self.java_class_identifier_expression_sempred
        self._predicates[189] = self.csharp_expression_sempred
        self._predicates[195] = self.csharp_arguments_sempred
        self._predicates[198] = self.csharp_identifier_expression_sempred
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
                return self.precpred(self._ctx, 30)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 13)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.wasNot(SParser.WS)
         

            if predIndex == 32:
                return self.wasNot(SParser.WS)
         

            if predIndex == 33:
                return self.wasNot(SParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.wasNot(SParser.WS)
         

            if predIndex == 37:
                return self.wasNot(SParser.WS)
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"module")
         

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
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
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
         



