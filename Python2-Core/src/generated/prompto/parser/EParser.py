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
        buf.write(u"\u009b\u0861\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0187\n\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\5\2\u018e\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u01ac\n\5\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\5\6\u01b4\n\6\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write(u"\u01bb\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01c6")
        buf.write(u"\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01cf\n\7\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01de")
        buf.write(u"\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01e7\n\b\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\5\t\u01ee\n\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\5\n\u01f8\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\5\r\u021e\n\r\3\r\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u022c\n\r\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5")
        buf.write(u"\16\u023a\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\5\16\u0248\n\16\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\7\20\u025a\n\20\f\20\16\20\u025d\13\20\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0267\n\21\5")
        buf.write(u"\21\u0269\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write(u"\u0272\n\22\3\22\3\22\5\22\u0276\n\22\3\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\5\23\u027e\n\23\3\23\3\23\5\23\u0282")
        buf.write(u"\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\5\24\u0291\n\24\3\24\3\24\5\24\u0295")
        buf.write(u"\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\5\25\u02b0\n\25\3\26\3\26\3")
        buf.write(u"\27\3\27\3\27\5\27\u02b7\n\27\3\30\3\30\3\30\5\30\u02bc")
        buf.write(u"\n\30\3\30\3\30\5\30\u02c0\n\30\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\5\31\u02d1\n\31\3\32\3\32\5\32\u02d5\n\32\3\32\5\32")
        buf.write(u"\u02d8\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\5\35\u02f9\n\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\5\36\u030c\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0313")
        buf.write(u"\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write(u"\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\5\"\u0335\n\"\3\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\5\"\u033e\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u0353\n#\f#\16#\u0356")
        buf.write(u"\13#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0365")
        buf.write(u"\n%\3%\3%\3%\5%\u036a\n%\3%\3%\3%\3%\3%\3%\5%\u0372\n")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\3%\5%\u037b\n%\3%\3%\3&\3&\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0392")
        buf.write(u"\n&\3\'\3\'\5\'\u0396\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5")
        buf.write(u"(\u03b2\n(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7(\u0412\n(\f(\16(\u0415")
        buf.write(u"\13(\3)\3)\3)\3)\3)\7)\u041c\n)\f)\16)\u041f\13)\3*\3")
        buf.write(u"*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3-\3-\3-\3-\3-\7-\u0431")
        buf.write(u"\n-\f-\16-\u0434\13-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\5.\u0443\n.\3/\3/\3\60\5\60\u0448\n\60\3\60\3")
        buf.write(u"\60\3\60\3\60\5\60\u044e\n\60\3\60\3\60\3\60\5\60\u0453")
        buf.write(u"\n\60\5\60\u0455\n\60\3\60\5\60\u0458\n\60\3\60\3\60")
        buf.write(u"\3\60\3\60\5\60\u045e\n\60\5\60\u0460\n\60\5\60\u0462")
        buf.write(u"\n\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write(u"\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0480\n")
        buf.write(u"\65\3\66\3\66\3\66\3\66\3\66\5\66\u0487\n\66\5\66\u0489")
        buf.write(u"\n\66\3\66\3\66\3\66\5\66\u048e\n\66\5\66\u0490\n\66")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u0499\n\67\f")
        buf.write(u"\67\16\67\u049c\13\67\38\38\38\38\39\39\39\39\3:\3:\3")
        buf.write(u":\3:\3:\3:\3:\3:\5:\u04ae\n:\3;\3;\3;\3;\3<\7<\u04b5")
        buf.write(u"\n<\f<\16<\u04b8\13<\3=\6=\u04bb\n=\r=\16=\u04bc\3>\6")
        buf.write(u">\u04c0\n>\r>\16>\u04c1\3>\3>\3?\7?\u04c7\n?\f?\16?\u04ca")
        buf.write(u"\13?\3?\3?\3@\3@\3A\5A\u04d1\nA\3A\3A\3A\3B\3B\3B\3B")
        buf.write(u"\3B\3B\3B\7B\u04dd\nB\fB\16B\u04e0\13B\3C\3C\3C\3C\3")
        buf.write(u"C\5C\u04e7\nC\3D\3D\3E\3E\5E\u04ed\nE\3F\3F\3F\3F\3F")
        buf.write(u"\3F\3F\7F\u04f6\nF\fF\16F\u04f9\13F\3G\3G\3G\3G\3G\3")
        buf.write(u"G\3G\7G\u0502\nG\fG\16G\u0505\13G\3H\3H\3H\3H\3H\3H\7")
        buf.write(u"H\u050d\nH\fH\16H\u0510\13H\3I\3I\3I\3I\3I\3I\3I\3I\3")
        buf.write(u"I\3I\5I\u051c\nI\3J\3J\5J\u0520\nJ\3J\3J\3K\3K\5K\u0526")
        buf.write(u"\nK\3K\3K\3L\3L\3L\3L\3L\3L\7L\u0530\nL\fL\16L\u0533")
        buf.write(u"\13L\3M\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N")
        buf.write(u"\3N\7N\u0546\nN\fN\16N\u0549\13N\3O\3O\5O\u054d\nO\3")
        buf.write(u"P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u0559\nP\3Q\3Q\3R\3R")
        buf.write(u"\3S\3S\3T\3T\3T\5T\u0564\nT\3U\3U\3U\3U\3U\3U\7U\u056c")
        buf.write(u"\nU\fU\16U\u056f\13U\3V\3V\5V\u0573\nV\3W\3W\3W\5W\u0578")
        buf.write(u"\nW\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3[\3[\3[\3[\7[\u0586\n[\f")
        buf.write(u"[\16[\u0589\13[\3\\\3\\\5\\\u058d\n\\\3\\\5\\\u0590\n")
        buf.write(u"\\\3]\3]\5]\u0594\n]\3^\3^\3^\5^\u0599\n^\3_\3_\3_\3")
        buf.write(u"`\3`\5`\u05a0\n`\3a\3a\3a\3a\3a\3a\3a\3a\3a\7a\u05ab")
        buf.write(u"\na\fa\16a\u05ae\13a\3b\3b\3b\3b\3b\3b\3b\7b\u05b7\n")
        buf.write(u"b\fb\16b\u05ba\13b\3c\3c\3c\3c\3c\5c\u05c1\nc\3d\3d\3")
        buf.write(u"d\3d\3d\3d\3d\7d\u05ca\nd\fd\16d\u05cd\13d\3e\3e\5e\u05d1")
        buf.write(u"\ne\3f\3f\3f\3f\3f\3f\3f\3f\3f\3f\5f\u05dd\nf\3g\3g\5")
        buf.write(u"g\u05e1\ng\3h\3h\3h\3h\3h\3h\7h\u05e9\nh\fh\16h\u05ec")
        buf.write(u"\13h\3i\3i\3i\3j\3j\5j\u05f3\nj\3k\3k\3k\3k\5k\u05f9")
        buf.write(u"\nk\3k\3k\3k\7k\u05fe\nk\fk\16k\u0601\13k\3k\3k\5k\u0605")
        buf.write(u"\nk\3l\3l\3l\3l\3l\3l\7l\u060d\nl\fl\16l\u0610\13l\3")
        buf.write(u"m\3m\3m\3m\5m\u0616\nm\3n\3n\3n\3n\3n\3n\3n\7n\u061f")
        buf.write(u"\nn\fn\16n\u0622\13n\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\5")
        buf.write(u"o\u062e\no\3p\3p\5p\u0632\np\3p\5p\u0635\np\3q\3q\5q")
        buf.write(u"\u0639\nq\3q\5q\u063c\nq\3r\3r\3r\3r\3r\3r\3r\7r\u0645")
        buf.write(u"\nr\fr\16r\u0648\13r\3s\3s\3s\3s\3s\3s\3s\7s\u0651\n")
        buf.write(u"s\fs\16s\u0654\13s\3t\3t\3t\3t\3t\3t\3t\7t\u065d\nt\f")
        buf.write(u"t\16t\u0660\13t\3u\3u\3u\3u\3u\3u\3u\7u\u0669\nu\fu\16")
        buf.write(u"u\u066c\13u\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write(u"v\5v\u067c\nv\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w")
        buf.write(u"\5w\u068b\nw\3x\3x\3x\3x\3x\3x\7x\u0693\nx\fx\16x\u0696")
        buf.write(u"\13x\3y\3y\3y\3y\5y\u069c\ny\3z\3z\3{\3{\3{\3{\3|\3|")
        buf.write(u"\5|\u06a6\n|\3}\3}\3}\3}\3}\5}\u06ad\n}\3~\3~\5~\u06b1")
        buf.write(u"\n~\3~\3~\3\177\3\177\5\177\u06b7\n\177\3\177\3\177\3")
        buf.write(u"\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\7\u0080")
        buf.write(u"\u06c1\n\u0080\f\u0080\16\u0080\u06c4\13\u0080\3\u0081")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\7\u0081\u06cc")
        buf.write(u"\n\u0081\f\u0081\16\u0081\u06cf\13\u0081\3\u0082\3\u0082")
        buf.write(u"\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083\u06de\n\u0083")
        buf.write(u"\3\u0084\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\7\u0085\u06e9\n\u0085\f\u0085\16\u0085")
        buf.write(u"\u06ec\13\u0085\3\u0086\3\u0086\3\u0086\3\u0086\5\u0086")
        buf.write(u"\u06f2\n\u0086\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\5\u0087\u06fa\n\u0087\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0089\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\3\u008b")
        buf.write(u"\3\u008b\3\u008c\3\u008c\3\u008d\3\u008d\3\u008e\3\u008e")
        buf.write(u"\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write(u"\3\u0090\3\u0090\5\u0090\u0716\n\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0091\7\u0091\u071d\n\u0091\f\u0091")
        buf.write(u"\16\u0091\u0720\13\u0091\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\3\u0092\5\u0092\u0728\n\u0092\3\u0093\3\u0093")
        buf.write(u"\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\5\u0094\u0731")
        buf.write(u"\n\u0094\3\u0095\3\u0095\3\u0095\5\u0095\u0736\n\u0095")
        buf.write(u"\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write(u"\3\u0096\7\u0096\u0740\n\u0096\f\u0096\16\u0096\u0743")
        buf.write(u"\13\u0096\3\u0097\3\u0097\3\u0097\3\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a\3\u009a")
        buf.write(u"\3\u009a\3\u009a\5\u009a\u0754\n\u009a\3\u009b\3\u009b")
        buf.write(u"\3\u009c\3\u009c\3\u009c\5\u009c\u075b\n\u009c\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009d\7\u009d\u0762\n\u009d")
        buf.write(u"\f\u009d\16\u009d\u0765\13\u009d\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\5\u009e\u076b\n\u009e\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u009f\5\u009f\u0773\n\u009f\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a0\5\u00a0\u0778\n\u00a0\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\5\u00a1")
        buf.write(u"\u0782\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\7\u00a2\u078a\n\u00a2\f\u00a2\16\u00a2\u078d")
        buf.write(u"\13\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\7\u00a3\u079a")
        buf.write(u"\n\u00a3\f\u00a3\16\u00a3\u079d\13\u00a3\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u07a6")
        buf.write(u"\n\u00a5\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u07ab\n\u00a5")
        buf.write(u"\f\u00a5\16\u00a5\u07ae\13\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a6\5\u00a6\u07b5\n\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\5\u00a8\u07c0\n\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\7\u00a9\u07c7\n\u00a9\f\u00a9\16\u00a9\u07ca")
        buf.write(u"\13\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa\u07d0")
        buf.write(u"\n\u00aa\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac\5\u00ac")
        buf.write(u"\u07d7\n\u00ac\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u07dc")
        buf.write(u"\n\u00ad\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\7\u00ae\u07e6\n\u00ae\f\u00ae\16\u00ae")
        buf.write(u"\u07e9\13\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\7\u00b1\u07f9\n\u00b1\f\u00b1\16\u00b1")
        buf.write(u"\u07fc\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\7\u00b2\u0803\n\u00b2\f\u00b2\16\u00b2\u0806\13\u00b2")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\5\u00b3\u080d")
        buf.write(u"\n\u00b3\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u0818\n\u00b5\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u081f\n\u00b6")
        buf.write(u"\f\u00b6\16\u00b6\u0822\13\u00b6\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\5\u00b7\u0828\n\u00b7\3\u00b8\3\u00b8\3\u00b9")
        buf.write(u"\3\u00b9\3\u00b9\5\u00b9\u082f\n\u00b9\3\u00ba\3\u00ba")
        buf.write(u"\3\u00ba\5\u00ba\u0834\n\u00ba\3\u00ba\3\u00ba\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u083e")
        buf.write(u"\n\u00bb\f\u00bb\16\u00bb\u0841\13\u00bb\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be")
        buf.write(u"\3\u00be\3\u00be\5\u00be\u084e\n\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00be\7\u00be\u0853\n\u00be\f\u00be\16\u00be\u0856")
        buf.write(u"\13\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf\5\u00bf")
        buf.write(u"\u085d\n\u00bf\3\u00c0\3\u00c0\3\u00c0\2*\36DNPXl\u0082")
        buf.write(u"\u008a\u008c\u008e\u0096\u009a\u00a8\u00b4\u00c0\u00c2")
        buf.write(u"\u00c6\u00d6\u00da\u00e2\u00e4\u00e6\u00e8\u00ee\u00fe")
        buf.write(u"\u0100\u0108\u0120\u012a\u0138\u0142\u0144\u0148\u0150")
        buf.write(u"\u015a\u0160\u0162\u016a\u0174\u017a\u00c1\2\4\6\b\n")
        buf.write(u"\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:")
        buf.write(u"<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write(u"\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write(u"\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write(u"\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba")
        buf.write(u"\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc")
        buf.write(u"\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de")
        buf.write(u"\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0")
        buf.write(u"\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102")
        buf.write(u"\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112\u0114")
        buf.write(u"\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124\u0126")
        buf.write(u"\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136\u0138")
        buf.write(u"\u013a\u013c\u013e\u0140\u0142\u0144\u0146\u0148\u014a")
        buf.write(u"\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a\u015c")
        buf.write(u"\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c\u016e")
        buf.write(u"\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e\2\t")
        buf.write(u"\3\2!\"\4\2{{\u0081\u0081\4\2&&hh\b\2\63;vv\u0080\u0080")
        buf.write(u"\u0089\u0089\u008e\u0090\u0092\u0092\b\2\63;vv{{\u0080")
        buf.write(u"\u0081\u0089\u0089\u008e\u0090\7\2\63;vv\u0080\u0080")
        buf.write(u"\u0089\u0089\u008e\u0092\7\2\63;vv\u0080\u0080\u0089")
        buf.write(u"\u0089\u008e\u0090\u08c8\2\u0180\3\2\2\2\4\u0195\3\2")
        buf.write(u"\2\2\6\u01a1\3\2\2\2\b\u01a7\3\2\2\2\n\u01ad\3\2\2\2")
        buf.write(u"\f\u01b5\3\2\2\2\16\u01d0\3\2\2\2\20\u01ed\3\2\2\2\22")
        buf.write(u"\u01ef\3\2\2\2\24\u01ff\3\2\2\2\26\u0208\3\2\2\2\30\u0211")
        buf.write(u"\3\2\2\2\32\u022d\3\2\2\2\34\u0249\3\2\2\2\36\u0252\3")
        buf.write(u"\2\2\2 \u0268\3\2\2\2\"\u026a\3\2\2\2$\u0277\3\2\2\2")
        buf.write(u"&\u0289\3\2\2\2(\u029c\3\2\2\2*\u02b1\3\2\2\2,\u02b3")
        buf.write(u"\3\2\2\2.\u02b8\3\2\2\2\60\u02d0\3\2\2\2\62\u02d7\3\2")
        buf.write(u"\2\2\64\u02d9\3\2\2\2\66\u02e2\3\2\2\28\u02eb\3\2\2\2")
        buf.write(u":\u030b\3\2\2\2<\u030d\3\2\2\2>\u031b\3\2\2\2@\u0324")
        buf.write(u"\3\2\2\2B\u032b\3\2\2\2D\u033f\3\2\2\2F\u0357\3\2\2\2")
        buf.write(u"H\u035a\3\2\2\2J\u0391\3\2\2\2L\u0393\3\2\2\2N\u03b1")
        buf.write(u"\3\2\2\2P\u0416\3\2\2\2R\u0420\3\2\2\2T\u0424\3\2\2\2")
        buf.write(u"V\u0429\3\2\2\2X\u042b\3\2\2\2Z\u0442\3\2\2\2\\\u0444")
        buf.write(u"\3\2\2\2^\u0461\3\2\2\2`\u0463\3\2\2\2b\u0467\3\2\2\2")
        buf.write(u"d\u046c\3\2\2\2f\u0470\3\2\2\2h\u0478\3\2\2\2j\u048f")
        buf.write(u"\3\2\2\2l\u0491\3\2\2\2n\u049d\3\2\2\2p\u04a1\3\2\2\2")
        buf.write(u"r\u04ad\3\2\2\2t\u04af\3\2\2\2v\u04b6\3\2\2\2x\u04ba")
        buf.write(u"\3\2\2\2z\u04bf\3\2\2\2|\u04c8\3\2\2\2~\u04cd\3\2\2\2")
        buf.write(u"\u0080\u04d0\3\2\2\2\u0082\u04d5\3\2\2\2\u0084\u04e6")
        buf.write(u"\3\2\2\2\u0086\u04e8\3\2\2\2\u0088\u04ec\3\2\2\2\u008a")
        buf.write(u"\u04ee\3\2\2\2\u008c\u04fa\3\2\2\2\u008e\u0506\3\2\2")
        buf.write(u"\2\u0090\u051b\3\2\2\2\u0092\u051d\3\2\2\2\u0094\u0523")
        buf.write(u"\3\2\2\2\u0096\u0529\3\2\2\2\u0098\u0534\3\2\2\2\u009a")
        buf.write(u"\u053a\3\2\2\2\u009c\u054c\3\2\2\2\u009e\u0558\3\2\2")
        buf.write(u"\2\u00a0\u055a\3\2\2\2\u00a2\u055c\3\2\2\2\u00a4\u055e")
        buf.write(u"\3\2\2\2\u00a6\u0563\3\2\2\2\u00a8\u0565\3\2\2\2\u00aa")
        buf.write(u"\u0572\3\2\2\2\u00ac\u0577\3\2\2\2\u00ae\u0579\3\2\2")
        buf.write(u"\2\u00b0\u057b\3\2\2\2\u00b2\u057d\3\2\2\2\u00b4\u057f")
        buf.write(u"\3\2\2\2\u00b6\u058f\3\2\2\2\u00b8\u0593\3\2\2\2\u00ba")
        buf.write(u"\u0595\3\2\2\2\u00bc\u059a\3\2\2\2\u00be\u059f\3\2\2")
        buf.write(u"\2\u00c0\u05a1\3\2\2\2\u00c2\u05af\3\2\2\2\u00c4\u05c0")
        buf.write(u"\3\2\2\2\u00c6\u05c2\3\2\2\2\u00c8\u05d0\3\2\2\2\u00ca")
        buf.write(u"\u05dc\3\2\2\2\u00cc\u05de\3\2\2\2\u00ce\u05e2\3\2\2")
        buf.write(u"\2\u00d0\u05ed\3\2\2\2\u00d2\u05f0\3\2\2\2\u00d4\u05f4")
        buf.write(u"\3\2\2\2\u00d6\u0606\3\2\2\2\u00d8\u0615\3\2\2\2\u00da")
        buf.write(u"\u0617\3\2\2\2\u00dc\u062d\3\2\2\2\u00de\u062f\3\2\2")
        buf.write(u"\2\u00e0\u0636\3\2\2\2\u00e2\u063d\3\2\2\2\u00e4\u0649")
        buf.write(u"\3\2\2\2\u00e6\u0655\3\2\2\2\u00e8\u0661\3\2\2\2\u00ea")
        buf.write(u"\u067b\3\2\2\2\u00ec\u068a\3\2\2\2\u00ee\u068c\3\2\2")
        buf.write(u"\2\u00f0\u069b\3\2\2\2\u00f2\u069d\3\2\2\2\u00f4\u069f")
        buf.write(u"\3\2\2\2\u00f6\u06a5\3\2\2\2\u00f8\u06ac\3\2\2\2\u00fa")
        buf.write(u"\u06ae\3\2\2\2\u00fc\u06b4\3\2\2\2\u00fe\u06ba\3\2\2")
        buf.write(u"\2\u0100\u06c5\3\2\2\2\u0102\u06d0\3\2\2\2\u0104\u06dd")
        buf.write(u"\3\2\2\2\u0106\u06df\3\2\2\2\u0108\u06e3\3\2\2\2\u010a")
        buf.write(u"\u06f1\3\2\2\2\u010c\u06f9\3\2\2\2\u010e\u06fb\3\2\2")
        buf.write(u"\2\u0110\u06fe\3\2\2\2\u0112\u0701\3\2\2\2\u0114\u0704")
        buf.write(u"\3\2\2\2\u0116\u0706\3\2\2\2\u0118\u0708\3\2\2\2\u011a")
        buf.write(u"\u070a\3\2\2\2\u011c\u070c\3\2\2\2\u011e\u0715\3\2\2")
        buf.write(u"\2\u0120\u0717\3\2\2\2\u0122\u0727\3\2\2\2\u0124\u0729")
        buf.write(u"\3\2\2\2\u0126\u0730\3\2\2\2\u0128\u0732\3\2\2\2\u012a")
        buf.write(u"\u0739\3\2\2\2\u012c\u0744\3\2\2\2\u012e\u0748\3\2\2")
        buf.write(u"\2\u0130\u074c\3\2\2\2\u0132\u0753\3\2\2\2\u0134\u0755")
        buf.write(u"\3\2\2\2\u0136\u075a\3\2\2\2\u0138\u075c\3\2\2\2\u013a")
        buf.write(u"\u076a\3\2\2\2\u013c\u0772\3\2\2\2\u013e\u0774\3\2\2")
        buf.write(u"\2\u0140\u0781\3\2\2\2\u0142\u0783\3\2\2\2\u0144\u078e")
        buf.write(u"\3\2\2\2\u0146\u079e\3\2\2\2\u0148\u07a5\3\2\2\2\u014a")
        buf.write(u"\u07b4\3\2\2\2\u014c\u07b6\3\2\2\2\u014e\u07bf\3\2\2")
        buf.write(u"\2\u0150\u07c1\3\2\2\2\u0152\u07cf\3\2\2\2\u0154\u07d1")
        buf.write(u"\3\2\2\2\u0156\u07d6\3\2\2\2\u0158\u07d8\3\2\2\2\u015a")
        buf.write(u"\u07df\3\2\2\2\u015c\u07ea\3\2\2\2\u015e\u07ee\3\2\2")
        buf.write(u"\2\u0160\u07f2\3\2\2\2\u0162\u07fd\3\2\2\2\u0164\u080c")
        buf.write(u"\3\2\2\2\u0166\u080e\3\2\2\2\u0168\u0817\3\2\2\2\u016a")
        buf.write(u"\u0819\3\2\2\2\u016c\u0827\3\2\2\2\u016e\u0829\3\2\2")
        buf.write(u"\2\u0170\u082e\3\2\2\2\u0172\u0830\3\2\2\2\u0174\u0837")
        buf.write(u"\3\2\2\2\u0176\u0842\3\2\2\2\u0178\u0846\3\2\2\2\u017a")
        buf.write(u"\u084d\3\2\2\2\u017c\u085c\3\2\2\2\u017e\u085e\3\2\2")
        buf.write(u"\2\u0180\u0181\7Q\2\2\u0181\u0182\5\u00b0Y\2\u0182\u0183")
        buf.write(u"\7D\2\2\u0183\u0186\7W\2\2\u0184\u0187\7K\2\2\u0185\u0187")
        buf.write(u"\5\u00b0Y\2\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write(u"\u018d\3\2\2\2\u0188\u0189\5 \21\2\u0189\u018a\7\22\2")
        buf.write(u"\2\u018a\u018b\7B\2\2\u018b\u018e\3\2\2\2\u018c\u018e")
        buf.write(u"\7\u0085\2\2\u018d\u0188\3\2\2\2\u018d\u018c\3\2\2\2")
        buf.write(u"\u018e\u018f\3\2\2\2\u018f\u0190\5\u0112\u008a\2\u0190")
        buf.write(u"\u0191\7\20\2\2\u0191\u0192\5z>\2\u0192\u0193\5\u008c")
        buf.write(u"G\2\u0193\u0194\5|?\2\u0194\3\3\2\2\2\u0195\u0196\7Q")
        buf.write(u"\2\2\u0196\u0197\5\u00b0Y\2\u0197\u0198\7D\2\2\u0198")
        buf.write(u"\u0199\7W\2\2\u0199\u019a\5\u009eP\2\u019a\u019b\7\u0085")
        buf.write(u"\2\2\u019b\u019c\5\u0112\u008a\2\u019c\u019d\7\20\2\2")
        buf.write(u"\u019d\u019e\5z>\2\u019e\u019f\5\u008aF\2\u019f\u01a0")
        buf.write(u"\5|?\2\u01a0\5\3\2\2\2\u01a1\u01a2\5\u00b2Z\2\u01a2\u01a3")
        buf.write(u"\7\u0085\2\2\u01a3\u01a4\5N(\2\u01a4\u01a5\7D\2\2\u01a5")
        buf.write(u"\u01a6\5\u0110\u0089\2\u01a6\7\3\2\2\2\u01a7\u01a8\5")
        buf.write(u"\u00b2Z\2\u01a8\u01ab\5l\67\2\u01a9\u01aa\7B\2\2\u01aa")
        buf.write(u"\u01ac\5n8\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write(u"\u01ac\t\3\2\2\2\u01ad\u01ae\7Q\2\2\u01ae\u01af\5\u00ae")
        buf.write(u"X\2\u01af\u01b0\7D\2\2\u01b0\u01b1\5\u009aN\2\u01b1\u01b3")
        buf.write(u"\7F\2\2\u01b2\u01b4\5\u0090I\2\u01b3\u01b2\3\2\2\2\u01b3")
        buf.write(u"\u01b4\3\2\2\2\u01b4\13\3\2\2\2\u01b5\u01b6\7Q\2\2\u01b6")
        buf.write(u"\u01b7\5\u00b0Y\2\u01b7\u01ba\7D\2\2\u01b8\u01bb\7K\2")
        buf.write(u"\2\u01b9\u01bb\5\20\t\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9")
        buf.write(u"\3\2\2\2\u01bb\u01ce\3\2\2\2\u01bc\u01c5\5 \21\2\u01bd")
        buf.write(u"\u01be\7\22\2\2\u01be\u01bf\7B\2\2\u01bf\u01c0\7g\2\2")
        buf.write(u"\u01c0\u01c1\7\20\2\2\u01c1\u01c2\5z>\2\u01c2\u01c3\5")
        buf.write(u"\u00c2b\2\u01c3\u01c4\5|?\2\u01c4\u01c6\3\2\2\2\u01c5")
        buf.write(u"\u01bd\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01cf\3\2\2")
        buf.write(u"\2\u01c7\u01c8\7\u0085\2\2\u01c8\u01c9\7g\2\2\u01c9\u01ca")
        buf.write(u"\7\20\2\2\u01ca\u01cb\5z>\2\u01cb\u01cc\5\u00c2b\2\u01cc")
        buf.write(u"\u01cd\5|?\2\u01cd\u01cf\3\2\2\2\u01ce\u01bc\3\2\2\2")
        buf.write(u"\u01ce\u01c7\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\r\3\2")
        buf.write(u"\2\2\u01d0\u01d1\7Q\2\2\u01d1\u01d2\5\u00b0Y\2\u01d2")
        buf.write(u"\u01d3\7D\2\2\u01d3\u01e6\7}\2\2\u01d4\u01dd\5 \21\2")
        buf.write(u"\u01d5\u01d6\7\22\2\2\u01d6\u01d7\7B\2\2\u01d7\u01d8")
        buf.write(u"\7g\2\2\u01d8\u01d9\7\20\2\2\u01d9\u01da\5z>\2\u01da")
        buf.write(u"\u01db\5\u00c2b\2\u01db\u01dc\5|?\2\u01dc\u01de\3\2\2")
        buf.write(u"\2\u01dd\u01d5\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e7")
        buf.write(u"\3\2\2\2\u01df\u01e0\7\u0085\2\2\u01e0\u01e1\7g\2\2\u01e1")
        buf.write(u"\u01e2\7\20\2\2\u01e2\u01e3\5z>\2\u01e3\u01e4\5\u00c2")
        buf.write(u"b\2\u01e4\u01e5\5|?\2\u01e5\u01e7\3\2\2\2\u01e6\u01d4")
        buf.write(u"\3\2\2\2\u01e6\u01df\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write(u"\17\3\2\2\2\u01e8\u01ee\5\u00a8U\2\u01e9\u01ea\5\u00a8")
        buf.write(u"U\2\u01ea\u01eb\7B\2\2\u01eb\u01ec\5\u00b0Y\2\u01ec\u01ee")
        buf.write(u"\3\2\2\2\u01ed\u01e8\3\2\2\2\u01ed\u01e9\3\2\2\2\u01ee")
        buf.write(u"\21\3\2\2\2\u01ef\u01f0\7Q\2\2\u01f0\u01f1\5\u010c\u0087")
        buf.write(u"\2\u01f1\u01f2\7D\2\2\u01f2\u01f3\7q\2\2\u01f3\u01f4")
        buf.write(u"\7w\2\2\u01f4\u01f7\5\u00b8]\2\u01f5\u01f6\7z\2\2\u01f6")
        buf.write(u"\u01f8\5\u009aN\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2")
        buf.write(u"\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\7S\2\2\u01fa\u01fb")
        buf.write(u"\7\20\2\2\u01fb\u01fc\5z>\2\u01fc\u01fd\5\u00e2r\2\u01fd")
        buf.write(u"\u01fe\5|?\2\u01fe\23\3\2\2\2\u01ff\u0200\7Q\2\2\u0200")
        buf.write(u"\u0201\5\u00aeX\2\u0201\u0202\7|\2\2\u0202\u0203\7S\2")
        buf.write(u"\2\u0203\u0204\7\20\2\2\u0204\u0205\5z>\2\u0205\u0206")
        buf.write(u"\5\u00e2r\2\u0206\u0207\5|?\2\u0207\25\3\2\2\2\u0208")
        buf.write(u"\u0209\7Q\2\2\u0209\u020a\5\u00aeX\2\u020a\u020b\7`\2")
        buf.write(u"\2\u020b\u020c\7S\2\2\u020c\u020d\7\20\2\2\u020d\u020e")
        buf.write(u"\5z>\2\u020e\u020f\5\u00e2r\2\u020f\u0210\5|?\2\u0210")
        buf.write(u"\27\3\2\2\2\u0211\u0212\7Q\2\2\u0212\u0213\5\u00b0Y\2")
        buf.write(u"\u0213\u0214\7D\2\2\u0214\u0215\7j\2\2\u0215\u021d\7")
        buf.write(u"K\2\2\u0216\u0217\5 \21\2\u0217\u0218\7\22\2\2\u0218")
        buf.write(u"\u0219\7B\2\2\u0219\u021a\7H\2\2\u021a\u021e\3\2\2\2")
        buf.write(u"\u021b\u021c\7\u0085\2\2\u021c\u021e\7H\2\2\u021d\u0216")
        buf.write(u"\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write(u"\u0220\7\20\2\2\u0220\u0221\5z>\2\u0221\u0222\5\34\17")
        buf.write(u"\2\u0222\u022b\5|?\2\u0223\u0224\5x=\2\u0224\u0225\7")
        buf.write(u"B\2\2\u0225\u0226\7g\2\2\u0226\u0227\7\20\2\2\u0227\u0228")
        buf.write(u"\5z>\2\u0228\u0229\5\u00c6d\2\u0229\u022a\5|?\2\u022a")
        buf.write(u"\u022c\3\2\2\2\u022b\u0223\3\2\2\2\u022b\u022c\3\2\2")
        buf.write(u"\2\u022c\31\3\2\2\2\u022d\u022e\7Q\2\2\u022e\u022f\5")
        buf.write(u"\u00b0Y\2\u022f\u0230\7D\2\2\u0230\u0231\7j\2\2\u0231")
        buf.write(u"\u0239\7x\2\2\u0232\u0233\5 \21\2\u0233\u0234\7\22\2")
        buf.write(u"\2\u0234\u0235\7B\2\2\u0235\u0236\7H\2\2\u0236\u023a")
        buf.write(u"\3\2\2\2\u0237\u0238\7\u0085\2\2\u0238\u023a\7H\2\2\u0239")
        buf.write(u"\u0232\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\3\2\2")
        buf.write(u"\2\u023b\u023c\7\20\2\2\u023c\u023d\5z>\2\u023d\u023e")
        buf.write(u"\5\34\17\2\u023e\u0247\5|?\2\u023f\u0240\5x=\2\u0240")
        buf.write(u"\u0241\7B\2\2\u0241\u0242\7g\2\2\u0242\u0243\7\20\2\2")
        buf.write(u"\u0243\u0244\5z>\2\u0244\u0245\5\u00c6d\2\u0245\u0246")
        buf.write(u"\5|?\2\u0246\u0248\3\2\2\2\u0247\u023f\3\2\2\2\u0247")
        buf.write(u"\u0248\3\2\2\2\u0248\33\3\2\2\2\u0249\u024a\7Q\2\2\u024a")
        buf.write(u"\u024b\7K\2\2\u024b\u024c\7H\2\2\u024c\u024d\7D\2\2\u024d")
        buf.write(u"\u024e\7\20\2\2\u024e\u024f\5z>\2\u024f\u0250\5\36\20")
        buf.write(u"\2\u0250\u0251\5|?\2\u0251\35\3\2\2\2\u0252\u0253\b\20")
        buf.write(u"\1\2\u0253\u0254\5\u00caf\2\u0254\u025b\3\2\2\2\u0255")
        buf.write(u"\u0256\f\3\2\2\u0256\u0257\5x=\2\u0257\u0258\5\u00ca")
        buf.write(u"f\2\u0258\u025a\3\2\2\2\u0259\u0255\3\2\2\2\u025a\u025d")
        buf.write(u"\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025c")
        buf.write(u"\37\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u025f\7\u0085\2")
        buf.write(u"\2\u025f\u0260\7F\2\2\u0260\u0269\5\u00aeX\2\u0261\u0262")
        buf.write(u"\7\u0085\2\2\u0262\u0263\7G\2\2\u0263\u0266\5\u00d6l")
        buf.write(u"\2\u0264\u0265\7B\2\2\u0265\u0267\5\u00aeX\2\u0266\u0264")
        buf.write(u"\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0269\3\2\2\2\u0268")
        buf.write(u"\u025e\3\2\2\2\u0268\u0261\3\2\2\2\u0269!\3\2\2\2\u026a")
        buf.write(u"\u026b\7Q\2\2\u026b\u026c\5\u00aaV\2\u026c\u026d\7D\2")
        buf.write(u"\2\u026d\u026e\7?\2\2\u026e\u0271\7f\2\2\u026f\u0270")
        buf.write(u"\7w\2\2\u0270\u0272\5,\27\2\u0271\u026f\3\2\2\2\u0271")
        buf.write(u"\u0272\3\2\2\2\u0272\u0275\3\2\2\2\u0273\u0274\7z\2\2")
        buf.write(u"\u0274\u0276\5\u009aN\2\u0275\u0273\3\2\2\2\u0275\u0276")
        buf.write(u"\3\2\2\2\u0276#\3\2\2\2\u0277\u0278\7Q\2\2\u0278\u0279")
        buf.write(u"\5\u00aaV\2\u0279\u027a\7D\2\2\u027a\u027d\7f\2\2\u027b")
        buf.write(u"\u027c\7w\2\2\u027c\u027e\5,\27\2\u027d\u027b\3\2\2\2")
        buf.write(u"\u027d\u027e\3\2\2\2\u027e\u0281\3\2\2\2\u027f\u0280")
        buf.write(u"\7z\2\2\u0280\u0282\5\u009aN\2\u0281\u027f\3\2\2\2\u0281")
        buf.write(u"\u0282\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0284\7S\2\2")
        buf.write(u"\u0284\u0285\7\20\2\2\u0285\u0286\5z>\2\u0286\u0287\5")
        buf.write(u"\u00e2r\2\u0287\u0288\5|?\2\u0288%\3\2\2\2\u0289\u028a")
        buf.write(u"\7Q\2\2\u028a\u028b\5\u00aaV\2\u028b\u028c\7D\2\2\u028c")
        buf.write(u"\u028d\7j\2\2\u028d\u0290\7f\2\2\u028e\u028f\7w\2\2\u028f")
        buf.write(u"\u0291\5,\27\2\u0290\u028e\3\2\2\2\u0290\u0291\3\2\2")
        buf.write(u"\2\u0291\u0294\3\2\2\2\u0292\u0293\7z\2\2\u0293\u0295")
        buf.write(u"\5\u00be`\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2\2\2\u0295")
        buf.write(u"\u0296\3\2\2\2\u0296\u0297\7S\2\2\u0297\u0298\7\20\2")
        buf.write(u"\2\u0298\u0299\5z>\2\u0299\u029a\5\u00dan\2\u029a\u029b")
        buf.write(u"\5|?\2\u029b\'\3\2\2\2\u029c\u029d\7Q\2\2\u029d\u029e")
        buf.write(u"\7\u0093\2\2\u029e\u029f\7D\2\2\u029f\u02a0\7\u0080\2")
        buf.write(u"\2\u02a0\u02a1\7f\2\2\u02a1\u02a2\7S\2\2\u02a2\u02a3")
        buf.write(u"\7\20\2\2\u02a3\u02a4\5z>\2\u02a4\u02a5\5\u00e2r\2\u02a5")
        buf.write(u"\u02a6\5|?\2\u02a6\u02a7\5x=\2\u02a7\u02a8\7B\2\2\u02a8")
        buf.write(u"\u02a9\7Z\2\2\u02a9\u02af\7\20\2\2\u02aa\u02ab\5z>\2")
        buf.write(u"\u02ab\u02ac\5\u00e4s\2\u02ac\u02ad\5|?\2\u02ad\u02b0")
        buf.write(u"\3\2\2\2\u02ae\u02b0\5\u00b2Z\2\u02af\u02aa\3\2\2\2\u02af")
        buf.write(u"\u02ae\3\2\2\2\u02b0)\3\2\2\2\u02b1\u02b2\5N(\2\u02b2")
        buf.write(u"+\3\2\2\2\u02b3\u02b6\5\u00b4[\2\u02b4\u02b5\7B\2\2\u02b5")
        buf.write(u"\u02b7\5\u00b6\\\2\u02b6\u02b4\3\2\2\2\u02b6\u02b7\3")
        buf.write(u"\2\2\2\u02b7-\3\2\2\2\u02b8\u02b9\5\u00be`\2\u02b9\u02bb")
        buf.write(u"\5\u00aeX\2\u02ba\u02bc\5 \21\2\u02bb\u02ba\3\2\2\2\u02bb")
        buf.write(u"\u02bc\3\2\2\2\u02bc\u02bf\3\2\2\2\u02bd\u02be\7,\2\2")
        buf.write(u"\u02be\u02c0\5\u00f6|\2\u02bf\u02bd\3\2\2\2\u02bf\u02c0")
        buf.write(u"\3\2\2\2\u02c0/\3\2\2\2\u02c1\u02d1\5p9\2\u02c2\u02d1")
        buf.write(u"\5\62\32\2\u02c3\u02d1\5t;\2\u02c4\u02d1\5L\'\2\u02c5")
        buf.write(u"\u02d1\5B\"\2\u02c6\u02d1\58\35\2\u02c7\u02d1\5<\37\2")
        buf.write(u"\u02c8\u02d1\5@!\2\u02c9\u02d1\5> \2\u02ca\u02d1\5F$")
        buf.write(u"\2\u02cb\u02d1\5H%\2\u02cc\u02d1\5b\62\2\u02cd\u02d1")
        buf.write(u"\5\64\33\2\u02ce\u02d1\5\66\34\2\u02cf\u02d1\5$\23\2")
        buf.write(u"\u02d0\u02c1\3\2\2\2\u02d0\u02c2\3\2\2\2\u02d0\u02c3")
        buf.write(u"\3\2\2\2\u02d0\u02c4\3\2\2\2\u02d0\u02c5\3\2\2\2\u02d0")
        buf.write(u"\u02c6\3\2\2\2\u02d0\u02c7\3\2\2\2\u02d0\u02c8\3\2\2")
        buf.write(u"\2\u02d0\u02c9\3\2\2\2\u02d0\u02ca\3\2\2\2\u02d0\u02cb")
        buf.write(u"\3\2\2\2\u02d0\u02cc\3\2\2\2\u02d0\u02cd\3\2\2\2\u02d0")
        buf.write(u"\u02ce\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1\61\3\2\2\2\u02d2")
        buf.write(u"\u02d4\5P)\2\u02d3\u02d5\5j\66\2\u02d4\u02d3\3\2\2\2")
        buf.write(u"\u02d4\u02d5\3\2\2\2\u02d5\u02d8\3\2\2\2\u02d6\u02d8")
        buf.write(u"\5T+\2\u02d7\u02d2\3\2\2\2\u02d7\u02d6\3\2\2\2\u02d8")
        buf.write(u"\63\3\2\2\2\u02d9\u02da\7\u0085\2\2\u02da\u02db\5\u0106")
        buf.write(u"\u0084\2\u02db\u02dc\7\22\2\2\u02dc\u02dd\7R\2\2\u02dd")
        buf.write(u"\u02de\7\20\2\2\u02de\u02df\5z>\2\u02df\u02e0\5\u00e2")
        buf.write(u"r\2\u02e0\u02e1\5|?\2\u02e1\65\3\2\2\2\u02e2\u02e3\7")
        buf.write(u"\u0085\2\2\u02e3\u02e4\5\u00b0Y\2\u02e4\u02e5\7\22\2")
        buf.write(u"\2\u02e5\u02e6\7R\2\2\u02e6\u02e7\7\20\2\2\u02e7\u02e8")
        buf.write(u"\5z>\2\u02e8\u02e9\5\u00e2r\2\u02e9\u02ea\5|?\2\u02ea")
        buf.write(u"\67\3\2\2\2\u02eb\u02ec\7\177\2\2\u02ec\u02ed\7o\2\2")
        buf.write(u"\u02ed\u02ee\5N(\2\u02ee\u02ef\7\20\2\2\u02ef\u02f0\5")
        buf.write(u"z>\2\u02f0\u02f8\5\u00e6t\2\u02f1\u02f2\5x=\2\u02f2\u02f3")
        buf.write(u"\7s\2\2\u02f3\u02f4\7\20\2\2\u02f4\u02f5\5z>\2\u02f5")
        buf.write(u"\u02f6\5\u00e2r\2\u02f6\u02f7\5|?\2\u02f7\u02f9\3\2\2")
        buf.write(u"\2\u02f8\u02f1\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9\u02fa")
        buf.write(u"\3\2\2\2\u02fa\u02fb\5|?\2\u02fb9\3\2\2\2\u02fc\u02fd")
        buf.write(u"\7\u0086\2\2\u02fd\u02fe\5\u00ecw\2\u02fe\u02ff\7\20")
        buf.write(u"\2\2\u02ff\u0300\5z>\2\u0300\u0301\5\u00e2r\2\u0301\u0302")
        buf.write(u"\5|?\2\u0302\u030c\3\2\2\2\u0303\u0304\7\u0086\2\2\u0304")
        buf.write(u"\u0305\7b\2\2\u0305\u0306\5\u00eav\2\u0306\u0307\7\20")
        buf.write(u"\2\2\u0307\u0308\5z>\2\u0308\u0309\5\u00e2r\2\u0309\u030a")
        buf.write(u"\5|?\2\u030a\u030c\3\2\2\2\u030b\u02fc\3\2\2\2\u030b")
        buf.write(u"\u0303\3\2\2\2\u030c;\3\2\2\2\u030d\u030e\7^\2\2\u030e")
        buf.write(u"\u030f\7T\2\2\u030f\u0312\5\u00aeX\2\u0310\u0311\7\22")
        buf.write(u"\2\2\u0311\u0313\5\u00aeX\2\u0312\u0310\3\2\2\2\u0312")
        buf.write(u"\u0313\3\2\2\2\u0313\u0314\3\2\2\2\u0314\u0315\7b\2\2")
        buf.write(u"\u0315\u0316\5N(\2\u0316\u0317\7\20\2\2\u0317\u0318\5")
        buf.write(u"z>\2\u0318\u0319\5\u00e2r\2\u0319\u031a\5|?\2\u031a=")
        buf.write(u"\3\2\2\2\u031b\u031c\7R\2\2\u031c\u031d\7\20\2\2\u031d")
        buf.write(u"\u031e\5z>\2\u031e\u031f\5\u00e2r\2\u031f\u0320\5|?\2")
        buf.write(u"\u0320\u0321\5x=\2\u0321\u0322\7\u0088\2\2\u0322\u0323")
        buf.write(u"\5N(\2\u0323?\3\2\2\2\u0324\u0325\7\u0088\2\2\u0325\u0326")
        buf.write(u"\5N(\2\u0326\u0327\7\20\2\2\u0327\u0328\5z>\2\u0328\u0329")
        buf.write(u"\5\u00e2r\2\u0329\u032a\5|?\2\u032aA\3\2\2\2\u032b\u032c")
        buf.write(u"\7a\2\2\u032c\u032d\5N(\2\u032d\u032e\7\20\2\2\u032e")
        buf.write(u"\u032f\5z>\2\u032f\u0330\5\u00e2r\2\u0330\u0334\5|?\2")
        buf.write(u"\u0331\u0332\5x=\2\u0332\u0333\5D#\2\u0333\u0335\3\2")
        buf.write(u"\2\2\u0334\u0331\3\2\2\2\u0334\u0335\3\2\2\2\u0335\u033d")
        buf.write(u"\3\2\2\2\u0336\u0337\5x=\2\u0337\u0338\7U\2\2\u0338\u0339")
        buf.write(u"\7\20\2\2\u0339\u033a\5z>\2\u033a\u033b\5\u00e2r\2\u033b")
        buf.write(u"\u033c\5|?\2\u033c\u033e\3\2\2\2\u033d\u0336\3\2\2\2")
        buf.write(u"\u033d\u033e\3\2\2\2\u033eC\3\2\2\2\u033f\u0340\b#\1")
        buf.write(u"\2\u0340\u0341\7U\2\2\u0341\u0342\7a\2\2\u0342\u0343")
        buf.write(u"\5N(\2\u0343\u0344\7\20\2\2\u0344\u0345\5z>\2\u0345\u0346")
        buf.write(u"\5\u00e2r\2\u0346\u0347\5|?\2\u0347\u0354\3\2\2\2\u0348")
        buf.write(u"\u0349\f\3\2\2\u0349\u034a\5x=\2\u034a\u034b\7U\2\2\u034b")
        buf.write(u"\u034c\7a\2\2\u034c\u034d\5N(\2\u034d\u034e\7\20\2\2")
        buf.write(u"\u034e\u034f\5z>\2\u034f\u0350\5\u00e2r\2\u0350\u0351")
        buf.write(u"\5|?\2\u0351\u0353\3\2\2\2\u0352\u0348\3\2\2\2\u0353")
        buf.write(u"\u0356\3\2\2\2\u0354\u0352\3\2\2\2\u0354\u0355\3\2\2")
        buf.write(u"\2\u0355E\3\2\2\2\u0356\u0354\3\2\2\2\u0357\u0358\7u")
        buf.write(u"\2\2\u0358\u0359\5N(\2\u0359G\3\2\2\2\u035a\u035b\7\177")
        buf.write(u"\2\2\u035b\u035c\7o\2\2\u035c\u035d\5\u00aeX\2\u035d")
        buf.write(u"\u035e\7S\2\2\u035e\u035f\7\20\2\2\u035f\u0360\5z>\2")
        buf.write(u"\u0360\u0361\5\u00e2r\2\u0361\u0362\5|?\2\u0362\u0364")
        buf.write(u"\5v<\2\u0363\u0365\5\u00e8u\2\u0364\u0363\3\2\2\2\u0364")
        buf.write(u"\u0365\3\2\2\2\u0365\u0371\3\2\2\2\u0366\u036a\7s\2\2")
        buf.write(u"\u0367\u0368\7\u0086\2\2\u0368\u036a\7C\2\2\u0369\u0366")
        buf.write(u"\3\2\2\2\u0369\u0367\3\2\2\2\u036a\u036b\3\2\2\2\u036b")
        buf.write(u"\u036c\7\20\2\2\u036c\u036d\5z>\2\u036d\u036e\5\u00e2")
        buf.write(u"r\2\u036e\u036f\5|?\2\u036f\u0370\5v<\2\u0370\u0372\3")
        buf.write(u"\2\2\2\u0371\u0369\3\2\2\2\u0371\u0372\3\2\2\2\u0372")
        buf.write(u"\u037a\3\2\2\2\u0373\u0374\7A\2\2\u0374\u0375\7\20\2")
        buf.write(u"\2\u0375\u0376\5z>\2\u0376\u0377\5\u00e2r\2\u0377\u0378")
        buf.write(u"\5|?\2\u0378\u0379\5v<\2\u0379\u037b\3\2\2\2\u037a\u0373")
        buf.write(u"\3\2\2\2\u037a\u037b\3\2\2\2\u037b\u037c\3\2\2\2\u037c")
        buf.write(u"\u037d\5v<\2\u037dI\3\2\2\2\u037e\u037f\7\u0086\2\2\u037f")
        buf.write(u"\u0380\5\u00b2Z\2\u0380\u0381\7\20\2\2\u0381\u0382\5")
        buf.write(u"z>\2\u0382\u0383\5\u00e2r\2\u0383\u0384\5|?\2\u0384\u0385")
        buf.write(u"\5v<\2\u0385\u0392\3\2\2\2\u0386\u0387\7\u0086\2\2\u0387")
        buf.write(u"\u0388\7b\2\2\u0388\u0389\7\27\2\2\u0389\u038a\5\u008e")
        buf.write(u"H\2\u038a\u038b\7\30\2\2\u038b\u038c\7\20\2\2\u038c\u038d")
        buf.write(u"\5z>\2\u038d\u038e\5\u00e2r\2\u038e\u038f\5|?\2\u038f")
        buf.write(u"\u0390\5v<\2\u0390\u0392\3\2\2\2\u0391\u037e\3\2\2\2")
        buf.write(u"\u0391\u0386\3\2\2\2\u0392K\3\2\2\2\u0393\u0395\7y\2")
        buf.write(u"\2\u0394\u0396\5N(\2\u0395\u0394\3\2\2\2\u0395\u0396")
        buf.write(u"\3\2\2\2\u0396M\3\2\2\2\u0397\u0398\b(\1\2\u0398\u0399")
        buf.write(u"\7\"\2\2\u0399\u03b2\5N((\u039a\u039b\7l\2\2\u039b\u03b2")
        buf.write(u"\5N(\'\u039c\u039d\7=\2\2\u039d\u039e\7\20\2\2\u039e")
        buf.write(u"\u03b2\5N(\f\u039f\u03b2\5X-\2\u03a0\u03b2\5P)\2\u03a1")
        buf.write(u"\u03a2\5P)\2\u03a2\u03a3\5j\66\2\u03a3\u03b2\3\2\2\2")
        buf.write(u"\u03a4\u03a5\7Y\2\2\u03a5\u03a6\7\20\2\2\u03a6\u03b2")
        buf.write(u"\5\u00aeX\2\u03a7\u03a8\7<\2\2\u03a8\u03a9\7\20\2\2\u03a9")
        buf.write(u"\u03b2\5\u00aaV\2\u03aa\u03b2\5\\/\2\u03ab\u03b2\5^\60")
        buf.write(u"\2\u03ac\u03b2\5f\64\2\u03ad\u03b2\5`\61\2\u03ae\u03b2")
        buf.write(u"\5h\65\2\u03af\u03b2\5d\63\2\u03b0\u03b2\5T+\2\u03b1")
        buf.write(u"\u0397\3\2\2\2\u03b1\u039a\3\2\2\2\u03b1\u039c\3\2\2")
        buf.write(u"\2\u03b1\u039f\3\2\2\2\u03b1\u03a0\3\2\2\2\u03b1\u03a1")
        buf.write(u"\3\2\2\2\u03b1\u03a4\3\2\2\2\u03b1\u03a7\3\2\2\2\u03b1")
        buf.write(u"\u03aa\3\2\2\2\u03b1\u03ab\3\2\2\2\u03b1\u03ac\3\2\2")
        buf.write(u"\2\u03b1\u03ad\3\2\2\2\u03b1\u03ae\3\2\2\2\u03b1\u03af")
        buf.write(u"\3\2\2\2\u03b1\u03b0\3\2\2\2\u03b2\u0413\3\2\2\2\u03b3")
        buf.write(u"\u03b4\f&\2\2\u03b4\u03b5\5\u0116\u008c\2\u03b5\u03b6")
        buf.write(u"\5N(\'\u03b6\u0412\3\2\2\2\u03b7\u03b8\f%\2\2\u03b8\u03b9")
        buf.write(u"\5\u0118\u008d\2\u03b9\u03ba\5N(&\u03ba\u0412\3\2\2\2")
        buf.write(u"\u03bb\u03bc\f$\2\2\u03bc\u03bd\5\u011c\u008f\2\u03bd")
        buf.write(u"\u03be\5N(%\u03be\u0412\3\2\2\2\u03bf\u03c0\f#\2\2\u03c0")
        buf.write(u"\u03c1\5\u011a\u008e\2\u03c1\u03c2\5N($\u03c2\u0412\3")
        buf.write(u"\2\2\2\u03c3\u03c4\f\"\2\2\u03c4\u03c5\t\2\2\2\u03c5")
        buf.write(u"\u0412\5N(#\u03c6\u03c7\f!\2\2\u03c7\u03c8\7)\2\2\u03c8")
        buf.write(u"\u0412\5N(\"\u03c9\u03ca\f \2\2\u03ca\u03cb\7*\2\2\u03cb")
        buf.write(u"\u0412\5N(!\u03cc\u03cd\f\37\2\2\u03cd\u03ce\7\'\2\2")
        buf.write(u"\u03ce\u0412\5N( \u03cf\u03d0\f\36\2\2\u03d0\u03d1\7")
        buf.write(u"(\2\2\u03d1\u0412\5N(\37\u03d2\u03d3\f\33\2\2\u03d3\u03d4")
        buf.write(u"\7,\2\2\u03d4\u0412\5N(\34\u03d5\u03d6\f\32\2\2\u03d6")
        buf.write(u"\u03d7\7+\2\2\u03d7\u0412\5N(\33\u03d8\u03d9\f\31\2\2")
        buf.write(u"\u03d9\u03da\7\60\2\2\u03da\u0412\5N(\32\u03db\u03dc")
        buf.write(u"\f\30\2\2\u03dc\u03dd\7r\2\2\u03dd\u0412\5N(\31\u03de")
        buf.write(u"\u03df\f\27\2\2\u03df\u03e0\7B\2\2\u03e0\u0412\5N(\30")
        buf.write(u"\u03e1\u03e2\f\26\2\2\u03e2\u03e3\7a\2\2\u03e3\u03e4")
        buf.write(u"\5N(\2\u03e4\u03e5\7U\2\2\u03e5\u03e6\5N(\27\u03e6\u0412")
        buf.write(u"\3\2\2\2\u03e7\u03e8\f\24\2\2\u03e8\u03e9\7b\2\2\u03e9")
        buf.write(u"\u0412\5N(\25\u03ea\u03eb\f\23\2\2\u03eb\u03ec\7N\2\2")
        buf.write(u"\u03ec\u0412\5N(\24\u03ed\u03ee\f\22\2\2\u03ee\u03ef")
        buf.write(u"\7N\2\2\u03ef\u03f0\7@\2\2\u03f0\u0412\5N(\23\u03f1\u03f2")
        buf.write(u"\f\21\2\2\u03f2\u03f3\7N\2\2\u03f3\u03f4\7C\2\2\u03f4")
        buf.write(u"\u0412\5N(\22\u03f5\u03f6\f\20\2\2\u03f6\u03f7\7l\2\2")
        buf.write(u"\u03f7\u03f8\7b\2\2\u03f8\u0412\5N(\21\u03f9\u03fa\f")
        buf.write(u"\17\2\2\u03fa\u03fb\7l\2\2\u03fb\u03fc\7N\2\2\u03fc\u0412")
        buf.write(u"\5N(\20\u03fd\u03fe\f\16\2\2\u03fe\u03ff\7l\2\2\u03ff")
        buf.write(u"\u0400\7N\2\2\u0400\u0401\7@\2\2\u0401\u0412\5N(\17\u0402")
        buf.write(u"\u0403\f\r\2\2\u0403\u0404\7l\2\2\u0404\u0405\7N\2\2")
        buf.write(u"\u0405\u0406\7C\2\2\u0406\u0412\5N(\16\u0407\u0408\f")
        buf.write(u"\35\2\2\u0408\u0409\7d\2\2\u0409\u040a\7l\2\2\u040a\u0412")
        buf.write(u"\5\u010a\u0086\2\u040b\u040c\f\34\2\2\u040c\u040d\7d")
        buf.write(u"\2\2\u040d\u0412\5\u010a\u0086\2\u040e\u040f\f\25\2\2")
        buf.write(u"\u040f\u0410\7D\2\2\u0410\u0412\5\u00be`\2\u0411\u03b3")
        buf.write(u"\3\2\2\2\u0411\u03b7\3\2\2\2\u0411\u03bb\3\2\2\2\u0411")
        buf.write(u"\u03bf\3\2\2\2\u0411\u03c3\3\2\2\2\u0411\u03c6\3\2\2")
        buf.write(u"\2\u0411\u03c9\3\2\2\2\u0411\u03cc\3\2\2\2\u0411\u03cf")
        buf.write(u"\3\2\2\2\u0411\u03d2\3\2\2\2\u0411\u03d5\3\2\2\2\u0411")
        buf.write(u"\u03d8\3\2\2\2\u0411\u03db\3\2\2\2\u0411\u03de\3\2\2")
        buf.write(u"\2\u0411\u03e1\3\2\2\2\u0411\u03e7\3\2\2\2\u0411\u03ea")
        buf.write(u"\3\2\2\2\u0411\u03ed\3\2\2\2\u0411\u03f1\3\2\2\2\u0411")
        buf.write(u"\u03f5\3\2\2\2\u0411\u03f9\3\2\2\2\u0411\u03fd\3\2\2")
        buf.write(u"\2\u0411\u0402\3\2\2\2\u0411\u0407\3\2\2\2\u0411\u040b")
        buf.write(u"\3\2\2\2\u0411\u040e\3\2\2\2\u0412\u0415\3\2\2\2\u0413")
        buf.write(u"\u0411\3\2\2\2\u0413\u0414\3\2\2\2\u0414O\3\2\2\2\u0415")
        buf.write(u"\u0413\3\2\2\2\u0416\u0417\b)\1\2\u0417\u0418\5\u00ac")
        buf.write(u"W\2\u0418\u041d\3\2\2\2\u0419\u041a\f\3\2\2\u041a\u041c")
        buf.write(u"\5R*\2\u041b\u0419\3\2\2\2\u041c\u041f\3\2\2\2\u041d")
        buf.write(u"\u041b\3\2\2\2\u041d\u041e\3\2\2\2\u041eQ\3\2\2\2\u041f")
        buf.write(u"\u041d\3\2\2\2\u0420\u0421\6*\37\3\u0421\u0422\7\24\2")
        buf.write(u"\2\u0422\u0423\5\u00acW\2\u0423S\3\2\2\2\u0424\u0425")
        buf.write(u"\7c\2\2\u0425\u0426\7\20\2\2\u0426\u0427\5\u00aeX\2\u0427")
        buf.write(u"\u0428\5V,\2\u0428U\3\2\2\2\u0429\u042a\6, \3\u042aW")
        buf.write(u"\3\2\2\2\u042b\u042c\b-\1\2\u042c\u042d\5\u00f0y\2\u042d")
        buf.write(u"\u0432\3\2\2\2\u042e\u042f\f\3\2\2\u042f\u0431\5Z.\2")
        buf.write(u"\u0430\u042e\3\2\2\2\u0431\u0434\3\2\2\2\u0432\u0430")
        buf.write(u"\3\2\2\2\u0432\u0433\3\2\2\2\u0433Y\3\2\2\2\u0434\u0432")
        buf.write(u"\3\2\2\2\u0435\u0436\6.\"\3\u0436\u0437\7\24\2\2\u0437")
        buf.write(u"\u0443\5\u00aeX\2\u0438\u0439\6.#\3\u0439\u043a\7\27")
        buf.write(u"\2\2\u043a\u043b\5\u0104\u0083\2\u043b\u043c\7\30\2\2")
        buf.write(u"\u043c\u0443\3\2\2\2\u043d\u043e\6.$\3\u043e\u043f\7")
        buf.write(u"\27\2\2\u043f\u0440\5N(\2\u0440\u0441\7\30\2\2\u0441")
        buf.write(u"\u0443\3\2\2\2\u0442\u0435\3\2\2\2\u0442\u0438\3\2\2")
        buf.write(u"\2\u0442\u043d\3\2\2\2\u0443[\3\2\2\2\u0444\u0445\5\u00a4")
        buf.write(u"S\2\u0445]\3\2\2\2\u0446\u0448\7i\2\2\u0447\u0446\3\2")
        buf.write(u"\2\2\u0447\u0448\3\2\2\2\u0448\u0449\3\2\2\2\u0449\u044a")
        buf.write(u"\5\u00a0Q\2\u044a\u044b\7_\2\2\u044b\u0454\5N(\2\u044c")
        buf.write(u"\u044e\7\22\2\2\u044d\u044c\3\2\2\2\u044d\u044e\3\2\2")
        buf.write(u"\2\u044e\u044f\3\2\2\2\u044f\u0452\5l\67\2\u0450\u0451")
        buf.write(u"\7B\2\2\u0451\u0453\5n8\2\u0452\u0450\3\2\2\2\u0452\u0453")
        buf.write(u"\3\2\2\2\u0453\u0455\3\2\2\2\u0454\u044d\3\2\2\2\u0454")
        buf.write(u"\u0455\3\2\2\2\u0455\u0462\3\2\2\2\u0456\u0458\7i\2\2")
        buf.write(u"\u0457\u0456\3\2\2\2\u0457\u0458\3\2\2\2\u0458\u0459")
        buf.write(u"\3\2\2\2\u0459\u045f\5\u00a0Q\2\u045a\u045d\5l\67\2\u045b")
        buf.write(u"\u045c\7B\2\2\u045c\u045e\5n8\2\u045d\u045b\3\2\2\2\u045d")
        buf.write(u"\u045e\3\2\2\2\u045e\u0460\3\2\2\2\u045f\u045a\3\2\2")
        buf.write(u"\2\u045f\u0460\3\2\2\2\u0460\u0462\3\2\2\2\u0461\u0447")
        buf.write(u"\3\2\2\2\u0461\u0457\3\2\2\2\u0462_\3\2\2\2\u0463\u0464")
        buf.write(u"\7v\2\2\u0464\u0465\7_\2\2\u0465\u0466\5N(\2\u0466a\3")
        buf.write(u"\2\2\2\u0467\u0468\7\u0089\2\2\u0468\u0469\5N(\2\u0469")
        buf.write(u"\u046a\7\u0083\2\2\u046a\u046b\5N(\2\u046bc\3\2\2\2\u046c")
        buf.write(u"\u046d\5P)\2\u046d\u046e\7\"\2\2\u046e\u046f\5N(\2\u046f")
        buf.write(u"e\3\2\2\2\u0470\u0471\7\\\2\2\u0471\u0472\7C\2\2\u0472")
        buf.write(u"\u0473\5\u00aeX\2\u0473\u0474\7_\2\2\u0474\u0475\5N(")
        buf.write(u"\2\u0475\u0476\7\u0087\2\2\u0476\u0477\5N(\2\u0477g\3")
        buf.write(u"\2\2\2\u0478\u0479\7~\2\2\u0479\u047f\5X-\2\u047a\u047b")
        buf.write(u"\7\u0085\2\2\u047b\u047c\5X-\2\u047c\u047d\7D\2\2\u047d")
        buf.write(u"\u047e\5\u010e\u0088\2\u047e\u0480\3\2\2\2\u047f\u047a")
        buf.write(u"\3\2\2\2\u047f\u0480\3\2\2\2\u0480i\3\2\2\2\u0481\u0482")
        buf.write(u"\6\66%\3\u0482\u0488\5N(\2\u0483\u0486\5l\67\2\u0484")
        buf.write(u"\u0485\7B\2\2\u0485\u0487\5n8\2\u0486\u0484\3\2\2\2\u0486")
        buf.write(u"\u0487\3\2\2\2\u0487\u0489\3\2\2\2\u0488\u0483\3\2\2")
        buf.write(u"\2\u0488\u0489\3\2\2\2\u0489\u0490\3\2\2\2\u048a\u048d")
        buf.write(u"\5l\67\2\u048b\u048c\7B\2\2\u048c\u048e\5n8\2\u048d\u048b")
        buf.write(u"\3\2\2\2\u048d\u048e\3\2\2\2\u048e\u0490\3\2\2\2\u048f")
        buf.write(u"\u0481\3\2\2\2\u048f\u048a\3\2\2\2\u0490k\3\2\2\2\u0491")
        buf.write(u"\u0492\b\67\1\2\u0492\u0493\7\u0085\2\2\u0493\u0494\5")
        buf.write(u"n8\2\u0494\u049a\3\2\2\2\u0495\u0496\f\3\2\2\u0496\u0497")
        buf.write(u"\7\22\2\2\u0497\u0499\5n8\2\u0498\u0495\3\2\2\2\u0499")
        buf.write(u"\u049c\3\2\2\2\u049a\u0498\3\2\2\2\u049a\u049b\3\2\2")
        buf.write(u"\2\u049bm\3\2\2\2\u049c\u049a\3\2\2\2\u049d\u049e\5N")
        buf.write(u"(\2\u049e\u049f\7D\2\2\u049f\u04a0\5\u00aeX\2\u04a0o")
        buf.write(u"\3\2\2\2\u04a1\u04a2\5\u0108\u0085\2\u04a2\u04a3\5\u0114")
        buf.write(u"\u008b\2\u04a3\u04a4\5N(\2\u04a4q\3\2\2\2\u04a5\u04a6")
        buf.write(u"\6:\'\3\u04a6\u04a7\7\24\2\2\u04a7\u04ae\5\u00aeX\2\u04a8")
        buf.write(u"\u04a9\6:(\3\u04a9\u04aa\7\27\2\2\u04aa\u04ab\5N(\2\u04ab")
        buf.write(u"\u04ac\7\30\2\2\u04ac\u04ae\3\2\2\2\u04ad\u04a5\3\2\2")
        buf.write(u"\2\u04ad\u04a8\3\2\2\2\u04aes\3\2\2\2\u04af\u04b0\5\u00d6")
        buf.write(u"l\2\u04b0\u04b1\5\u0114\u008b\2\u04b1\u04b2\5N(\2\u04b2")
        buf.write(u"u\3\2\2\2\u04b3\u04b5\7\7\2\2\u04b4\u04b3\3\2\2\2\u04b5")
        buf.write(u"\u04b8\3\2\2\2\u04b6\u04b4\3\2\2\2\u04b6\u04b7\3\2\2")
        buf.write(u"\2\u04b7w\3\2\2\2\u04b8\u04b6\3\2\2\2\u04b9\u04bb\7\7")
        buf.write(u"\2\2\u04ba\u04b9\3\2\2\2\u04bb\u04bc\3\2\2\2\u04bc\u04ba")
        buf.write(u"\3\2\2\2\u04bc\u04bd\3\2\2\2\u04bdy\3\2\2\2\u04be\u04c0")
        buf.write(u"\7\7\2\2\u04bf\u04be\3\2\2\2\u04c0\u04c1\3\2\2\2\u04c1")
        buf.write(u"\u04bf\3\2\2\2\u04c1\u04c2\3\2\2\2\u04c2\u04c3\3\2\2")
        buf.write(u"\2\u04c3\u04c4\7\3\2\2\u04c4{\3\2\2\2\u04c5\u04c7\7\7")
        buf.write(u"\2\2\u04c6\u04c5\3\2\2\2\u04c7\u04ca\3\2\2\2\u04c8\u04c6")
        buf.write(u"\3\2\2\2\u04c8\u04c9\3\2\2\2\u04c9\u04cb\3\2\2\2\u04ca")
        buf.write(u"\u04c8\3\2\2\2\u04cb\u04cc\7\4\2\2\u04cc}\3\2\2\2\u04cd")
        buf.write(u"\u04ce\7m\2\2\u04ce\177\3\2\2\2\u04cf\u04d1\5\u0082B")
        buf.write(u"\2\u04d0\u04cf\3\2\2\2\u04d0\u04d1\3\2\2\2\u04d1\u04d2")
        buf.write(u"\3\2\2\2\u04d2\u04d3\5v<\2\u04d3\u04d4\7\2\2\3\u04d4")
        buf.write(u"\u0081\3\2\2\2\u04d5\u04d6\bB\1\2\u04d6\u04d7\5\u0084")
        buf.write(u"C\2\u04d7\u04de\3\2\2\2\u04d8\u04d9\f\3\2\2\u04d9\u04da")
        buf.write(u"\5x=\2\u04da\u04db\5\u0084C\2\u04db\u04dd\3\2\2\2\u04dc")
        buf.write(u"\u04d8\3\2\2\2\u04dd\u04e0\3\2\2\2\u04de\u04dc\3\2\2")
        buf.write(u"\2\u04de\u04df\3\2\2\2\u04df\u0083\3\2\2\2\u04e0\u04de")
        buf.write(u"\3\2\2\2\u04e1\u04e7\5\n\6\2\u04e2\u04e7\5\u00a6T\2\u04e3")
        buf.write(u"\u04e7\5\u0086D\2\u04e4\u04e7\5\u0088E\2\u04e5\u04e7")
        buf.write(u"\5\u00d8m\2\u04e6\u04e1\3\2\2\2\u04e6\u04e2\3\2\2\2\u04e6")
        buf.write(u"\u04e3\3\2\2\2\u04e6\u04e4\3\2\2\2\u04e6\u04e5\3\2\2")
        buf.write(u"\2\u04e7\u0085\3\2\2\2\u04e8\u04e9\5\32\16\2\u04e9\u0087")
        buf.write(u"\3\2\2\2\u04ea\u04ed\5\2\2\2\u04eb\u04ed\5\4\3\2\u04ec")
        buf.write(u"\u04ea\3\2\2\2\u04ec\u04eb\3\2\2\2\u04ed\u0089\3\2\2")
        buf.write(u"\2\u04ee\u04ef\bF\1\2\u04ef\u04f0\5\6\4\2\u04f0\u04f7")
        buf.write(u"\3\2\2\2\u04f1\u04f2\f\3\2\2\u04f2\u04f3\5x=\2\u04f3")
        buf.write(u"\u04f4\5\6\4\2\u04f4\u04f6\3\2\2\2\u04f5\u04f1\3\2\2")
        buf.write(u"\2\u04f6\u04f9\3\2\2\2\u04f7\u04f5\3\2\2\2\u04f7\u04f8")
        buf.write(u"\3\2\2\2\u04f8\u008b\3\2\2\2\u04f9\u04f7\3\2\2\2\u04fa")
        buf.write(u"\u04fb\bG\1\2\u04fb\u04fc\5\b\5\2\u04fc\u0503\3\2\2\2")
        buf.write(u"\u04fd\u04fe\f\3\2\2\u04fe\u04ff\5x=\2\u04ff\u0500\5")
        buf.write(u"\b\5\2\u0500\u0502\3\2\2\2\u0501\u04fd\3\2\2\2\u0502")
        buf.write(u"\u0505\3\2\2\2\u0503\u0501\3\2\2\2\u0503\u0504\3\2\2")
        buf.write(u"\2\u0504\u008d\3\2\2\2\u0505\u0503\3\2\2\2\u0506\u0507")
        buf.write(u"\bH\1\2\u0507\u0508\5\u00b2Z\2\u0508\u050e\3\2\2\2\u0509")
        buf.write(u"\u050a\f\3\2\2\u050a\u050b\7\22\2\2\u050b\u050d\5\u00b2")
        buf.write(u"Z\2\u050c\u0509\3\2\2\2\u050d\u0510\3\2\2\2\u050e\u050c")
        buf.write(u"\3\2\2\2\u050e\u050f\3\2\2\2\u050f\u008f\3\2\2\2\u0510")
        buf.write(u"\u050e\3\2\2\2\u0511\u0512\7b\2\2\u0512\u051c\5\u0092")
        buf.write(u"J\2\u0513\u0514\7b\2\2\u0514\u051c\5\u0094K\2\u0515\u0516")
        buf.write(u"\7b\2\2\u0516\u051c\5\u0098M\2\u0517\u0518\7e\2\2\u0518")
        buf.write(u"\u051c\7\u0093\2\2\u0519\u051a\7e\2\2\u051a\u051c\5N")
        buf.write(u"(\2\u051b\u0511\3\2\2\2\u051b\u0513\3\2\2\2\u051b\u0515")
        buf.write(u"\3\2\2\2\u051b\u0517\3\2\2\2\u051b\u0519\3\2\2\2\u051c")
        buf.write(u"\u0091\3\2\2\2\u051d\u051f\7\27\2\2\u051e\u0520\5\u0096")
        buf.write(u"L\2\u051f\u051e\3\2\2\2\u051f\u0520\3\2\2\2\u0520\u0521")
        buf.write(u"\3\2\2\2\u0521\u0522\7\30\2\2\u0522\u0093\3\2\2\2\u0523")
        buf.write(u"\u0525\7)\2\2\u0524\u0526\5\u0096L\2\u0525\u0524\3\2")
        buf.write(u"\2\2\u0525\u0526\3\2\2\2\u0526\u0527\3\2\2\2\u0527\u0528")
        buf.write(u"\7\'\2\2\u0528\u0095\3\2\2\2\u0529\u052a\bL\1\2\u052a")
        buf.write(u"\u052b\5N(\2\u052b\u0531\3\2\2\2\u052c\u052d\f\3\2\2")
        buf.write(u"\u052d\u052e\7\22\2\2\u052e\u0530\5N(\2\u052f\u052c\3")
        buf.write(u"\2\2\2\u0530\u0533\3\2\2\2\u0531\u052f\3\2\2\2\u0531")
        buf.write(u"\u0532\3\2\2\2\u0532\u0097\3\2\2\2\u0533\u0531\3\2\2")
        buf.write(u"\2\u0534\u0535\7\27\2\2\u0535\u0536\5N(\2\u0536\u0537")
        buf.write(u"\7\23\2\2\u0537\u0538\5N(\2\u0538\u0539\7\30\2\2\u0539")
        buf.write(u"\u0099\3\2\2\2\u053a\u053b\bN\1\2\u053b\u053c\5\u009c")
        buf.write(u"O\2\u053c\u0547\3\2\2\2\u053d\u053e\f\5\2\2\u053e\u0546")
        buf.write(u"\7+\2\2\u053f\u0540\f\4\2\2\u0540\u0541\7\27\2\2\u0541")
        buf.write(u"\u0546\7\30\2\2\u0542\u0543\f\3\2\2\u0543\u0544\7\31")
        buf.write(u"\2\2\u0544\u0546\7\32\2\2\u0545\u053d\3\2\2\2\u0545\u053f")
        buf.write(u"\3\2\2\2\u0545\u0542\3\2\2\2\u0546\u0549\3\2\2\2\u0547")
        buf.write(u"\u0545\3\2\2\2\u0547\u0548\3\2\2\2\u0548\u009b\3\2\2")
        buf.write(u"\2\u0549\u0547\3\2\2\2\u054a\u054d\5\u009eP\2\u054b\u054d")
        buf.write(u"\5\u00a0Q\2\u054c\u054a\3\2\2\2\u054c\u054b\3\2\2\2\u054d")
        buf.write(u"\u009d\3\2\2\2\u054e\u0559\7\63\2\2\u054f\u0559\7\64")
        buf.write(u"\2\2\u0550\u0559\7\65\2\2\u0551\u0559\7\66\2\2\u0552")
        buf.write(u"\u0559\7\67\2\2\u0553\u0559\78\2\2\u0554\u0559\7:\2\2")
        buf.write(u"\u0555\u0559\79\2\2\u0556\u0559\7;\2\2\u0557\u0559\7")
        buf.write(u"=\2\2\u0558\u054e\3\2\2\2\u0558\u054f\3\2\2\2\u0558\u0550")
        buf.write(u"\3\2\2\2\u0558\u0551\3\2\2\2\u0558\u0552\3\2\2\2\u0558")
        buf.write(u"\u0553\3\2\2\2\u0558\u0554\3\2\2\2\u0558\u0555\3\2\2")
        buf.write(u"\2\u0558\u0556\3\2\2\2\u0558\u0557\3\2\2\2\u0559\u009f")
        buf.write(u"\3\2\2\2\u055a\u055b\7\u008f\2\2\u055b\u00a1\3\2\2\2")
        buf.write(u"\u055c\u055d\7=\2\2\u055d\u00a3\3\2\2\2\u055e\u055f\7")
        buf.write(u">\2\2\u055f\u00a5\3\2\2\2\u0560\u0564\5\f\7\2\u0561\u0564")
        buf.write(u"\5\30\r\2\u0562\u0564\5\16\b\2\u0563\u0560\3\2\2\2\u0563")
        buf.write(u"\u0561\3\2\2\2\u0563\u0562\3\2\2\2\u0564\u00a7\3\2\2")
        buf.write(u"\2\u0565\u0566\bU\1\2\u0566\u0567\5\u00b0Y\2\u0567\u056d")
        buf.write(u"\3\2\2\2\u0568\u0569\f\3\2\2\u0569\u056a\7\22\2\2\u056a")
        buf.write(u"\u056c\5\u00b0Y\2\u056b\u0568\3\2\2\2\u056c\u056f\3\2")
        buf.write(u"\2\2\u056d\u056b\3\2\2\2\u056d\u056e\3\2\2\2\u056e\u00a9")
        buf.write(u"\3\2\2\2\u056f\u056d\3\2\2\2\u0570\u0573\5\u00aeX\2\u0571")
        buf.write(u"\u0573\5\u00b0Y\2\u0572\u0570\3\2\2\2\u0572\u0571\3\2")
        buf.write(u"\2\2\u0573\u00ab\3\2\2\2\u0574\u0578\5\u00aeX\2\u0575")
        buf.write(u"\u0578\5\u00b0Y\2\u0576\u0578\5\u00b2Z\2\u0577\u0574")
        buf.write(u"\3\2\2\2\u0577\u0575\3\2\2\2\u0577\u0576\3\2\2\2\u0578")
        buf.write(u"\u00ad\3\2\2\2\u0579\u057a\7\u0090\2\2\u057a\u00af\3")
        buf.write(u"\2\2\2\u057b\u057c\7\u008f\2\2\u057c\u00b1\3\2\2\2\u057d")
        buf.write(u"\u057e\7\u008e\2\2\u057e\u00b3\3\2\2\2\u057f\u0580\b")
        buf.write(u"[\1\2\u0580\u0581\5\u00b6\\\2\u0581\u0587\3\2\2\2\u0582")
        buf.write(u"\u0583\f\3\2\2\u0583\u0584\7\22\2\2\u0584\u0586\5\u00b6")
        buf.write(u"\\\2\u0585\u0582\3\2\2\2\u0586\u0589\3\2\2\2\u0587\u0585")
        buf.write(u"\3\2\2\2\u0587\u0588\3\2\2\2\u0588\u00b5\3\2\2\2\u0589")
        buf.write(u"\u0587\3\2\2\2\u058a\u0590\5\u00bc_\2\u058b\u058d\7i")
        buf.write(u"\2\2\u058c\u058b\3\2\2\2\u058c\u058d\3\2\2\2\u058d\u058e")
        buf.write(u"\3\2\2\2\u058e\u0590\5\u00b8]\2\u058f\u058a\3\2\2\2\u058f")
        buf.write(u"\u058c\3\2\2\2\u0590\u00b7\3\2\2\2\u0591\u0594\5\u00ba")
        buf.write(u"^\2\u0592\u0594\5.\30\2\u0593\u0591\3\2\2\2\u0593\u0592")
        buf.write(u"\3\2\2\2\u0594\u00b9\3\2\2\2\u0595\u0598\5\u00aeX\2\u0596")
        buf.write(u"\u0597\7,\2\2\u0597\u0599\5\u00f6|\2\u0598\u0596\3\2")
        buf.write(u"\2\2\u0598\u0599\3\2\2\2\u0599\u00bb\3\2\2\2\u059a\u059b")
        buf.write(u"\5\u00a2R\2\u059b\u059c\5\u00aeX\2\u059c\u00bd\3\2\2")
        buf.write(u"\2\u059d\u05a0\5\u009aN\2\u059e\u05a0\5\u00c0a\2\u059f")
        buf.write(u"\u059d\3\2\2\2\u059f\u059e\3\2\2\2\u05a0\u00bf\3\2\2")
        buf.write(u"\2\u05a1\u05a2\ba\1\2\u05a2\u05a3\7C\2\2\u05a3\u05ac")
        buf.write(u"\3\2\2\2\u05a4\u05a5\f\4\2\2\u05a5\u05a6\7\27\2\2\u05a6")
        buf.write(u"\u05ab\7\30\2\2\u05a7\u05a8\f\3\2\2\u05a8\u05a9\7\31")
        buf.write(u"\2\2\u05a9\u05ab\7\32\2\2\u05aa\u05a4\3\2\2\2\u05aa\u05a7")
        buf.write(u"\3\2\2\2\u05ab\u05ae\3\2\2\2\u05ac\u05aa\3\2\2\2\u05ac")
        buf.write(u"\u05ad\3\2\2\2\u05ad\u00c1\3\2\2\2\u05ae\u05ac\3\2\2")
        buf.write(u"\2\u05af\u05b0\bb\1\2\u05b0\u05b1\5\u00c4c\2\u05b1\u05b8")
        buf.write(u"\3\2\2\2\u05b2\u05b3\f\3\2\2\u05b3\u05b4\5x=\2\u05b4")
        buf.write(u"\u05b5\5\u00c4c\2\u05b5\u05b7\3\2\2\2\u05b6\u05b2\3\2")
        buf.write(u"\2\2\u05b7\u05ba\3\2\2\2\u05b8\u05b6\3\2\2\2\u05b8\u05b9")
        buf.write(u"\3\2\2\2\u05b9\u00c3\3\2\2\2\u05ba\u05b8\3\2\2\2\u05bb")
        buf.write(u"\u05c1\5\24\13\2\u05bc\u05c1\5\26\f\2\u05bd\u05c1\5$")
        buf.write(u"\23\2\u05be\u05c1\5\"\22\2\u05bf\u05c1\5\22\n\2\u05c0")
        buf.write(u"\u05bb\3\2\2\2\u05c0\u05bc\3\2\2\2\u05c0\u05bd\3\2\2")
        buf.write(u"\2\u05c0\u05be\3\2\2\2\u05c0\u05bf\3\2\2\2\u05c1\u00c5")
        buf.write(u"\3\2\2\2\u05c2\u05c3\bd\1\2\u05c3\u05c4\5\u00c8e\2\u05c4")
        buf.write(u"\u05cb\3\2\2\2\u05c5\u05c6\f\3\2\2\u05c6\u05c7\5x=\2")
        buf.write(u"\u05c7\u05c8\5\u00c8e\2\u05c8\u05ca\3\2\2\2\u05c9\u05c5")
        buf.write(u"\3\2\2\2\u05ca\u05cd\3\2\2\2\u05cb\u05c9\3\2\2\2\u05cb")
        buf.write(u"\u05cc\3\2\2\2\u05cc\u00c7\3\2\2\2\u05cd\u05cb\3\2\2")
        buf.write(u"\2\u05ce\u05d1\5\u00c4c\2\u05cf\u05d1\5&\24\2\u05d0\u05ce")
        buf.write(u"\3\2\2\2\u05d0\u05cf\3\2\2\2\u05d1\u00c9\3\2\2\2\u05d2")
        buf.write(u"\u05d3\7\n\2\2\u05d3\u05dd\5\u0162\u00b2\2\u05d4\u05d5")
        buf.write(u"\7\13\2\2\u05d5\u05dd\5\u017a\u00be\2\u05d6\u05d7\7\f")
        buf.write(u"\2\2\u05d7\u05dd\5\u00ccg\2\u05d8\u05d9\7\r\2\2\u05d9")
        buf.write(u"\u05dd\5\u00ccg\2\u05da\u05db\7\16\2\2\u05db\u05dd\5")
        buf.write(u"\u00d2j\2\u05dc\u05d2\3\2\2\2\u05dc\u05d4\3\2\2\2\u05dc")
        buf.write(u"\u05d6\3\2\2\2\u05dc\u05d8\3\2\2\2\u05dc\u05da\3\2\2")
        buf.write(u"\2\u05dd\u00cb\3\2\2\2\u05de\u05e0\5\u00acW\2\u05df\u05e1")
        buf.write(u"\5\u00ceh\2\u05e0\u05df\3\2\2\2\u05e0\u05e1\3\2\2\2\u05e1")
        buf.write(u"\u00cd\3\2\2\2\u05e2\u05e3\7_\2\2\u05e3\u05e4\5\u00d0")
        buf.write(u"i\2\u05e4\u05e5\7\20\2\2\u05e5\u05ea\5\u00acW\2\u05e6")
        buf.write(u"\u05e7\7\24\2\2\u05e7\u05e9\5\u00acW\2\u05e8\u05e6\3")
        buf.write(u"\2\2\2\u05e9\u05ec\3\2\2\2\u05ea\u05e8\3\2\2\2\u05ea")
        buf.write(u"\u05eb\3\2\2\2\u05eb\u00cf\3\2\2\2\u05ec\u05ea\3\2\2")
        buf.write(u"\2\u05ed\u05ee\7\u0090\2\2\u05ee\u05ef\6i\67\3\u05ef")
        buf.write(u"\u00d1\3\2\2\2\u05f0\u05f2\5\u00acW\2\u05f1\u05f3\5\u00d4")
        buf.write(u"k\2\u05f2\u05f1\3\2\2\2\u05f2\u05f3\3\2\2\2\u05f3\u00d3")
        buf.write(u"\3\2\2\2\u05f4\u05f5\7_\2\2\u05f5\u05f6\5\u00d0i\2\u05f6")
        buf.write(u"\u05f8\7\20\2\2\u05f7\u05f9\7$\2\2\u05f8\u05f7\3\2\2")
        buf.write(u"\2\u05f8\u05f9\3\2\2\2\u05f9\u05fa\3\2\2\2\u05fa\u05ff")
        buf.write(u"\5\u0134\u009b\2\u05fb\u05fc\7$\2\2\u05fc\u05fe\5\u0134")
        buf.write(u"\u009b\2\u05fd\u05fb\3\2\2\2\u05fe\u0601\3\2\2\2\u05ff")
        buf.write(u"\u05fd\3\2\2\2\u05ff\u0600\3\2\2\2\u0600\u0604\3\2\2")
        buf.write(u"\2\u0601\u05ff\3\2\2\2\u0602\u0603\7\24\2\2\u0603\u0605")
        buf.write(u"\5\u0134\u009b\2\u0604\u0602\3\2\2\2\u0604\u0605\3\2")
        buf.write(u"\2\2\u0605\u00d5\3\2\2\2\u0606\u0607\bl\1\2\u0607\u0608")
        buf.write(u"\5\u00aeX\2\u0608\u060e\3\2\2\2\u0609\u060a\f\3\2\2\u060a")
        buf.write(u"\u060b\7\22\2\2\u060b\u060d\5\u00aeX\2\u060c\u0609\3")
        buf.write(u"\2\2\2\u060d\u0610\3\2\2\2\u060e\u060c\3\2\2\2\u060e")
        buf.write(u"\u060f\3\2\2\2\u060f\u00d7\3\2\2\2\u0610\u060e\3\2\2")
        buf.write(u"\2\u0611\u0616\5\"\22\2\u0612\u0616\5$\23\2\u0613\u0616")
        buf.write(u"\5&\24\2\u0614\u0616\5(\25\2\u0615\u0611\3\2\2\2\u0615")
        buf.write(u"\u0612\3\2\2\2\u0615\u0613\3\2\2\2\u0615\u0614\3\2\2")
        buf.write(u"\2\u0616\u00d9\3\2\2\2\u0617\u0618\bn\1\2\u0618\u0619")
        buf.write(u"\5\u00dco\2\u0619\u0620\3\2\2\2\u061a\u061b\f\3\2\2\u061b")
        buf.write(u"\u061c\5x=\2\u061c\u061d\5\u00dco\2\u061d\u061f\3\2\2")
        buf.write(u"\2\u061e\u061a\3\2\2\2\u061f\u0622\3\2\2\2\u0620\u061e")
        buf.write(u"\3\2\2\2\u0620\u0621\3\2\2\2\u0621\u00db\3\2\2\2\u0622")
        buf.write(u"\u0620\3\2\2\2\u0623\u0624\7\n\2\2\u0624\u062e\5\u014e")
        buf.write(u"\u00a8\2\u0625\u0626\7\13\2\2\u0626\u062e\5\u0168\u00b5")
        buf.write(u"\2\u0627\u0628\7\f\2\2\u0628\u062e\5\u00dep\2\u0629\u062a")
        buf.write(u"\7\r\2\2\u062a\u062e\5\u00dep\2\u062b\u062c\7\16\2\2")
        buf.write(u"\u062c\u062e\5\u00e0q\2\u062d\u0623\3\2\2\2\u062d\u0625")
        buf.write(u"\3\2\2\2\u062d\u0627\3\2\2\2\u062d\u0629\3\2\2\2\u062d")
        buf.write(u"\u062b\3\2\2\2\u062e\u00dd\3\2\2\2\u062f\u0631\5\u0136")
        buf.write(u"\u009c\2\u0630\u0632\7\21\2\2\u0631\u0630\3\2\2\2\u0631")
        buf.write(u"\u0632\3\2\2\2\u0632\u0634\3\2\2\2\u0633\u0635\5\u00ce")
        buf.write(u"h\2\u0634\u0633\3\2\2\2\u0634\u0635\3\2\2\2\u0635\u00df")
        buf.write(u"\3\2\2\2\u0636\u0638\5\u011e\u0090\2\u0637\u0639\7\21")
        buf.write(u"\2\2\u0638\u0637\3\2\2\2\u0638\u0639\3\2\2\2\u0639\u063b")
        buf.write(u"\3\2\2\2\u063a\u063c\5\u00d4k\2\u063b\u063a\3\2\2\2\u063b")
        buf.write(u"\u063c\3\2\2\2\u063c\u00e1\3\2\2\2\u063d\u063e\br\1\2")
        buf.write(u"\u063e\u063f\5\60\31\2\u063f\u0646\3\2\2\2\u0640\u0641")
        buf.write(u"\f\3\2\2\u0641\u0642\5x=\2\u0642\u0643\5\60\31\2\u0643")
        buf.write(u"\u0645\3\2\2\2\u0644\u0640\3\2\2\2\u0645\u0648\3\2\2")
        buf.write(u"\2\u0646\u0644\3\2\2\2\u0646\u0647\3\2\2\2\u0647\u00e3")
        buf.write(u"\3\2\2\2\u0648\u0646\3\2\2\2\u0649\u064a\bs\1\2\u064a")
        buf.write(u"\u064b\5*\26\2\u064b\u0652\3\2\2\2\u064c\u064d\f\3\2")
        buf.write(u"\2\u064d\u064e\5x=\2\u064e\u064f\5*\26\2\u064f\u0651")
        buf.write(u"\3\2\2\2\u0650\u064c\3\2\2\2\u0651\u0654\3\2\2\2\u0652")
        buf.write(u"\u0650\3\2\2\2\u0652\u0653\3\2\2\2\u0653\u00e5\3\2\2")
        buf.write(u"\2\u0654\u0652\3\2\2\2\u0655\u0656\bt\1\2\u0656\u0657")
        buf.write(u"\5:\36\2\u0657\u065e\3\2\2\2\u0658\u0659\f\3\2\2\u0659")
        buf.write(u"\u065a\5x=\2\u065a\u065b\5:\36\2\u065b\u065d\3\2\2\2")
        buf.write(u"\u065c\u0658\3\2\2\2\u065d\u0660\3\2\2\2\u065e\u065c")
        buf.write(u"\3\2\2\2\u065e\u065f\3\2\2\2\u065f\u00e7\3\2\2\2\u0660")
        buf.write(u"\u065e\3\2\2\2\u0661\u0662\bu\1\2\u0662\u0663\5J&\2\u0663")
        buf.write(u"\u066a\3\2\2\2\u0664\u0665\f\3\2\2\u0665\u0666\5x=\2")
        buf.write(u"\u0666\u0667\5J&\2\u0667\u0669\3\2\2\2\u0668\u0664\3")
        buf.write(u"\2\2\2\u0669\u066c\3\2\2\2\u066a\u0668\3\2\2\2\u066a")
        buf.write(u"\u066b\3\2\2\2\u066b\u00e9\3\2\2\2\u066c\u066a\3\2\2")
        buf.write(u"\2\u066d\u066e\7\27\2\2\u066e\u066f\5\u00ecw\2\u066f")
        buf.write(u"\u0670\7\23\2\2\u0670\u0671\5\u00ecw\2\u0671\u0672\7")
        buf.write(u"\30\2\2\u0672\u067c\3\2\2\2\u0673\u0674\7\27\2\2\u0674")
        buf.write(u"\u0675\5\u00eex\2\u0675\u0676\7\30\2\2\u0676\u067c\3")
        buf.write(u"\2\2\2\u0677\u0678\7)\2\2\u0678\u0679\5\u00eex\2\u0679")
        buf.write(u"\u067a\7\'\2\2\u067a\u067c\3\2\2\2\u067b\u066d\3\2\2")
        buf.write(u"\2\u067b\u0673\3\2\2\2\u067b\u0677\3\2\2\2\u067c\u00eb")
        buf.write(u"\3\2\2\2\u067d\u068b\7\u008c\2\2\u067e\u068b\7\u008d")
        buf.write(u"\2\2\u067f\u068b\7\u0094\2\2\u0680\u068b\7\u0095\2\2")
        buf.write(u"\u0681\u068b\7\u008b\2\2\u0682\u068b\7\u0099\2\2\u0683")
        buf.write(u"\u068b\7\u0098\2\2\u0684\u068b\7\u0093\2\2\u0685\u068b")
        buf.write(u"\7\u0096\2\2\u0686\u068b\7\u0097\2\2\u0687\u068b\7\u008a")
        buf.write(u"\2\2\u0688\u068b\7\u009a\2\2\u0689\u068b\5~@\2\u068a")
        buf.write(u"\u067d\3\2\2\2\u068a\u067e\3\2\2\2\u068a\u067f\3\2\2")
        buf.write(u"\2\u068a\u0680\3\2\2\2\u068a\u0681\3\2\2\2\u068a\u0682")
        buf.write(u"\3\2\2\2\u068a\u0683\3\2\2\2\u068a\u0684\3\2\2\2\u068a")
        buf.write(u"\u0685\3\2\2\2\u068a\u0686\3\2\2\2\u068a\u0687\3\2\2")
        buf.write(u"\2\u068a\u0688\3\2\2\2\u068a\u0689\3\2\2\2\u068b\u00ed")
        buf.write(u"\3\2\2\2\u068c\u068d\bx\1\2\u068d\u068e\5\u00ecw\2\u068e")
        buf.write(u"\u0694\3\2\2\2\u068f\u0690\f\3\2\2\u0690\u0691\7\22\2")
        buf.write(u"\2\u0691\u0693\5\u00ecw\2\u0692\u068f\3\2\2\2\u0693\u0696")
        buf.write(u"\3\2\2\2\u0694\u0692\3\2\2\2\u0694\u0695\3\2\2\2\u0695")
        buf.write(u"\u00ef\3\2\2\2\u0696\u0694\3\2\2\2\u0697\u069c\5\u00f4")
        buf.write(u"{\2\u0698\u069c\5\u00f6|\2\u0699\u069c\5\u00acW\2\u069a")
        buf.write(u"\u069c\5\u00f2z\2\u069b\u0697\3\2\2\2\u069b\u0698\3\2")
        buf.write(u"\2\2\u069b\u0699\3\2\2\2\u069b\u069a\3\2\2\2\u069c\u00f1")
        buf.write(u"\3\2\2\2\u069d\u069e\t\3\2\2\u069e\u00f3\3\2\2\2\u069f")
        buf.write(u"\u06a0\7\25\2\2\u06a0\u06a1\5N(\2\u06a1\u06a2\7\26\2")
        buf.write(u"\2\u06a2\u00f5\3\2\2\2\u06a3\u06a6\5\u00ecw\2\u06a4\u06a6")
        buf.write(u"\5\u00f8}\2\u06a5\u06a3\3\2\2\2\u06a5\u06a4\3\2\2\2\u06a6")
        buf.write(u"\u00f7\3\2\2\2\u06a7\u06ad\5\u0098M\2\u06a8\u06ad\5\u0092")
        buf.write(u"J\2\u06a9\u06ad\5\u0094K\2\u06aa\u06ad\5\u00fc\177\2")
        buf.write(u"\u06ab\u06ad\5\u00fa~\2\u06ac\u06a7\3\2\2\2\u06ac\u06a8")
        buf.write(u"\3\2\2\2\u06ac\u06a9\3\2\2\2\u06ac\u06aa\3\2\2\2\u06ac")
        buf.write(u"\u06ab\3\2\2\2\u06ad\u00f9\3\2\2\2\u06ae\u06b0\7\25\2")
        buf.write(u"\2\u06af\u06b1\5\u00fe\u0080\2\u06b0\u06af\3\2\2\2\u06b0")
        buf.write(u"\u06b1\3\2\2\2\u06b1\u06b2\3\2\2\2\u06b2\u06b3\7\26\2")
        buf.write(u"\2\u06b3\u00fb\3\2\2\2\u06b4\u06b6\7\31\2\2\u06b5\u06b7")
        buf.write(u"\5\u0100\u0081\2\u06b6\u06b5\3\2\2\2\u06b6\u06b7\3\2")
        buf.write(u"\2\2\u06b7\u06b8\3\2\2\2\u06b8\u06b9\7\32\2\2\u06b9\u00fd")
        buf.write(u"\3\2\2\2\u06ba\u06bb\b\u0080\1\2\u06bb\u06bc\5N(\2\u06bc")
        buf.write(u"\u06c2\3\2\2\2\u06bd\u06be\f\3\2\2\u06be\u06bf\7\22\2")
        buf.write(u"\2\u06bf\u06c1\5N(\2\u06c0\u06bd\3\2\2\2\u06c1\u06c4")
        buf.write(u"\3\2\2\2\u06c2\u06c0\3\2\2\2\u06c2\u06c3\3\2\2\2\u06c3")
        buf.write(u"\u00ff\3\2\2\2\u06c4\u06c2\3\2\2\2\u06c5\u06c6\b\u0081")
        buf.write(u"\1\2\u06c6\u06c7\5\u0102\u0082\2\u06c7\u06cd\3\2\2\2")
        buf.write(u"\u06c8\u06c9\f\3\2\2\u06c9\u06ca\7\22\2\2\u06ca\u06cc")
        buf.write(u"\5\u0102\u0082\2\u06cb\u06c8\3\2\2\2\u06cc\u06cf\3\2")
        buf.write(u"\2\2\u06cd\u06cb\3\2\2\2\u06cd\u06ce\3\2\2\2\u06ce\u0101")
        buf.write(u"\3\2\2\2\u06cf\u06cd\3\2\2\2\u06d0\u06d1\5N(\2\u06d1")
        buf.write(u"\u06d2\7\20\2\2\u06d2\u06d3\5N(\2\u06d3\u0103\3\2\2\2")
        buf.write(u"\u06d4\u06d5\5N(\2\u06d5\u06d6\7\20\2\2\u06d6\u06d7\5")
        buf.write(u"N(\2\u06d7\u06de\3\2\2\2\u06d8\u06d9\5N(\2\u06d9\u06da")
        buf.write(u"\7\20\2\2\u06da\u06de\3\2\2\2\u06db\u06dc\7\20\2\2\u06dc")
        buf.write(u"\u06de\5N(\2\u06dd\u06d4\3\2\2\2\u06dd\u06d8\3\2\2\2")
        buf.write(u"\u06dd\u06db\3\2\2\2\u06de\u0105\3\2\2\2\u06df\u06e0")
        buf.write(u"\5\u00aeX\2\u06e0\u06e1\5\u0114\u008b\2\u06e1\u06e2\5")
        buf.write(u"N(\2\u06e2\u0107\3\2\2\2\u06e3\u06e4\b\u0085\1\2\u06e4")
        buf.write(u"\u06e5\5\u00aeX\2\u06e5\u06ea\3\2\2\2\u06e6\u06e7\f\3")
        buf.write(u"\2\2\u06e7\u06e9\5r:\2\u06e8\u06e6\3\2\2\2\u06e9\u06ec")
        buf.write(u"\3\2\2\2\u06ea\u06e8\3\2\2\2\u06ea\u06eb\3\2\2\2\u06eb")
        buf.write(u"\u0109\3\2\2\2\u06ec\u06ea\3\2\2\2\u06ed\u06ee\6\u0086")
        buf.write(u"B\3\u06ee\u06ef\7\u0090\2\2\u06ef\u06f2\5\u00be`\2\u06f0")
        buf.write(u"\u06f2\5N(\2\u06f1\u06ed\3\2\2\2\u06f1\u06f0\3\2\2\2")
        buf.write(u"\u06f2\u010b\3\2\2\2\u06f3\u06fa\7!\2\2\u06f4\u06fa\7")
        buf.write(u"\"\2\2\u06f5\u06fa\5\u0116\u008c\2\u06f6\u06fa\5\u0118")
        buf.write(u"\u008d\2\u06f7\u06fa\5\u011a\u008e\2\u06f8\u06fa\5\u011c")
        buf.write(u"\u008f\2\u06f9\u06f3\3\2\2\2\u06f9\u06f4\3\2\2\2\u06f9")
        buf.write(u"\u06f5\3\2\2\2\u06f9\u06f6\3\2\2\2\u06f9\u06f7\3\2\2")
        buf.write(u"\2\u06f9\u06f8\3\2\2\2\u06fa\u010d\3\2\2\2\u06fb\u06fc")
        buf.write(u"\7\u0090\2\2\u06fc\u06fd\6\u0088C\3\u06fd\u010f\3\2\2")
        buf.write(u"\2\u06fe\u06ff\7\u0090\2\2\u06ff\u0700\6\u0089D\3\u0700")
        buf.write(u"\u0111\3\2\2\2\u0701\u0702\7\u0090\2\2\u0702\u0703\6")
        buf.write(u"\u008aE\3\u0703\u0113\3\2\2\2\u0704\u0705\7,\2\2\u0705")
        buf.write(u"\u0115\3\2\2\2\u0706\u0707\7#\2\2\u0707\u0117\3\2\2\2")
        buf.write(u"\u0708\u0709\7$\2\2\u0709\u0119\3\2\2\2\u070a\u070b\7")
        buf.write(u"%\2\2\u070b\u011b\3\2\2\2\u070c\u070d\t\4\2\2\u070d\u011d")
        buf.write(u"\3\2\2\2\u070e\u070f\7y\2\2\u070f\u0710\5\u0120\u0091")
        buf.write(u"\2\u0710\u0711\7\21\2\2\u0711\u0716\3\2\2\2\u0712\u0713")
        buf.write(u"\5\u0120\u0091\2\u0713\u0714\7\21\2\2\u0714\u0716\3\2")
        buf.write(u"\2\2\u0715\u070e\3\2\2\2\u0715\u0712\3\2\2\2\u0716\u011f")
        buf.write(u"\3\2\2\2\u0717\u0718\b\u0091\1\2\u0718\u0719\5\u0122")
        buf.write(u"\u0092\2\u0719\u071e\3\2\2\2\u071a\u071b\f\3\2\2\u071b")
        buf.write(u"\u071d\5\u0126\u0094\2\u071c\u071a\3\2\2\2\u071d\u0720")
        buf.write(u"\3\2\2\2\u071e\u071c\3\2\2\2\u071e\u071f\3\2\2\2\u071f")
        buf.write(u"\u0121\3\2\2\2\u0720\u071e\3\2\2\2\u0721\u0728\5\u0124")
        buf.write(u"\u0093\2\u0722\u0728\5\u012e\u0098\2\u0723\u0728\5\u0130")
        buf.write(u"\u0099\2\u0724\u0728\5\u0132\u009a\2\u0725\u0728\5\u0128")
        buf.write(u"\u0095\2\u0726\u0728\5\u012c\u0097\2\u0727\u0721\3\2")
        buf.write(u"\2\2\u0727\u0722\3\2\2\2\u0727\u0723\3\2\2\2\u0727\u0724")
        buf.write(u"\3\2\2\2\u0727\u0725\3\2\2\2\u0727\u0726\3\2\2\2\u0728")
        buf.write(u"\u0123\3\2\2\2\u0729\u072a\5\u00f2z\2\u072a\u0125\3\2")
        buf.write(u"\2\2\u072b\u072c\7\24\2\2\u072c\u0731\5\u0128\u0095\2")
        buf.write(u"\u072d\u072e\7\24\2\2\u072e\u0731\5\u0134\u009b\2\u072f")
        buf.write(u"\u0731\5\u012c\u0097\2\u0730\u072b\3\2\2\2\u0730\u072d")
        buf.write(u"\3\2\2\2\u0730\u072f\3\2\2\2\u0731\u0127\3\2\2\2\u0732")
        buf.write(u"\u0733\5\u0134\u009b\2\u0733\u0735\7\25\2\2\u0734\u0736")
        buf.write(u"\5\u012a\u0096\2\u0735\u0734\3\2\2\2\u0735\u0736\3\2")
        buf.write(u"\2\2\u0736\u0737\3\2\2\2\u0737\u0738\7\26\2\2\u0738\u0129")
        buf.write(u"\3\2\2\2\u0739\u073a\b\u0096\1\2\u073a\u073b\5\u0120")
        buf.write(u"\u0091\2\u073b\u0741\3\2\2\2\u073c\u073d\f\3\2\2\u073d")
        buf.write(u"\u073e\7\22\2\2\u073e\u0740\5\u0120\u0091\2\u073f\u073c")
        buf.write(u"\3\2\2\2\u0740\u0743\3\2\2\2\u0741\u073f\3\2\2\2\u0741")
        buf.write(u"\u0742\3\2\2\2\u0742\u012b\3\2\2\2\u0743\u0741\3\2\2")
        buf.write(u"\2\u0744\u0745\7\27\2\2\u0745\u0746\5\u0120\u0091\2\u0746")
        buf.write(u"\u0747\7\30\2\2\u0747\u012d\3\2\2\2\u0748\u0749\7\25")
        buf.write(u"\2\2\u0749\u074a\5\u0120\u0091\2\u074a\u074b\7\26\2\2")
        buf.write(u"\u074b\u012f\3\2\2\2\u074c\u074d\5\u0134\u009b\2\u074d")
        buf.write(u"\u0131\3\2\2\2\u074e\u0754\7\u0094\2\2\u074f\u0754\7")
        buf.write(u"\u0096\2\2\u0750\u0754\7\u0093\2\2\u0751\u0754\7\u008a")
        buf.write(u"\2\2\u0752\u0754\7\u008b\2\2\u0753\u074e\3\2\2\2\u0753")
        buf.write(u"\u074f\3\2\2\2\u0753\u0750\3\2\2\2\u0753\u0751\3\2\2")
        buf.write(u"\2\u0753\u0752\3\2\2\2\u0754\u0133\3\2\2\2\u0755\u0756")
        buf.write(u"\t\5\2\2\u0756\u0135\3\2\2\2\u0757\u0758\7y\2\2\u0758")
        buf.write(u"\u075b\5\u0138\u009d\2\u0759\u075b\5\u0138\u009d\2\u075a")
        buf.write(u"\u0757\3\2\2\2\u075a\u0759\3\2\2\2\u075b\u0137\3\2\2")
        buf.write(u"\2\u075c\u075d\b\u009d\1\2\u075d\u075e\5\u013a\u009e")
        buf.write(u"\2\u075e\u0763\3\2\2\2\u075f\u0760\f\3\2\2\u0760\u0762")
        buf.write(u"\5\u013c\u009f\2\u0761\u075f\3\2\2\2\u0762\u0765\3\2")
        buf.write(u"\2\2\u0763\u0761\3\2\2\2\u0763\u0764\3\2\2\2\u0764\u0139")
        buf.write(u"\3\2\2\2\u0765\u0763\3\2\2\2\u0766\u076b\5\u0146\u00a4")
        buf.write(u"\2\u0767\u076b\5\u0148\u00a5\2\u0768\u076b\5\u014a\u00a6")
        buf.write(u"\2\u0769\u076b\5\u013e\u00a0\2\u076a\u0766\3\2\2\2\u076a")
        buf.write(u"\u0767\3\2\2\2\u076a\u0768\3\2\2\2\u076a\u0769\3\2\2")
        buf.write(u"\2\u076b\u013b\3\2\2\2\u076c\u076d\7\24\2\2\u076d\u0773")
        buf.write(u"\5\u013e\u00a0\2\u076e\u076f\7\27\2\2\u076f\u0770\5\u0138")
        buf.write(u"\u009d\2\u0770\u0771\7\30\2\2\u0771\u0773\3\2\2\2\u0772")
        buf.write(u"\u076c\3\2\2\2\u0772\u076e\3\2\2\2\u0773\u013d\3\2\2")
        buf.write(u"\2\u0774\u0775\5\u014c\u00a7\2\u0775\u0777\7\25\2\2\u0776")
        buf.write(u"\u0778\5\u0140\u00a1\2\u0777\u0776\3\2\2\2\u0777\u0778")
        buf.write(u"\3\2\2\2\u0778\u0779\3\2\2\2\u0779\u077a\7\26\2\2\u077a")
        buf.write(u"\u013f\3\2\2\2\u077b\u0782\5\u0142\u00a2\2\u077c\u0782")
        buf.write(u"\5\u0144\u00a3\2\u077d\u077e\5\u0142\u00a2\2\u077e\u077f")
        buf.write(u"\7\22\2\2\u077f\u0780\5\u0144\u00a3\2\u0780\u0782\3\2")
        buf.write(u"\2\2\u0781\u077b\3\2\2\2\u0781\u077c\3\2\2\2\u0781\u077d")
        buf.write(u"\3\2\2\2\u0782\u0141\3\2\2\2\u0783\u0784\b\u00a2\1\2")
        buf.write(u"\u0784\u0785\5\u0138\u009d\2\u0785\u078b\3\2\2\2\u0786")
        buf.write(u"\u0787\f\3\2\2\u0787\u0788\7\22\2\2\u0788\u078a\5\u0138")
        buf.write(u"\u009d\2\u0789\u0786\3\2\2\2\u078a\u078d\3\2\2\2\u078b")
        buf.write(u"\u0789\3\2\2\2\u078b\u078c\3\2\2\2\u078c\u0143\3\2\2")
        buf.write(u"\2\u078d\u078b\3\2\2\2\u078e\u078f\b\u00a3\1\2\u078f")
        buf.write(u"\u0790\5\u014c\u00a7\2\u0790\u0791\7,\2\2\u0791\u0792")
        buf.write(u"\5\u0138\u009d\2\u0792\u079b\3\2\2\2\u0793\u0794\f\3")
        buf.write(u"\2\2\u0794\u0795\7\22\2\2\u0795\u0796\5\u014c\u00a7\2")
        buf.write(u"\u0796\u0797\7,\2\2\u0797\u0798\5\u0138\u009d\2\u0798")
        buf.write(u"\u079a\3\2\2\2\u0799\u0793\3\2\2\2\u079a\u079d\3\2\2")
        buf.write(u"\2\u079b\u0799\3\2\2\2\u079b\u079c\3\2\2\2\u079c\u0145")
        buf.write(u"\3\2\2\2\u079d\u079b\3\2\2\2\u079e\u079f\7\25\2\2\u079f")
        buf.write(u"\u07a0\5\u0138\u009d\2\u07a0\u07a1\7\26\2\2\u07a1\u0147")
        buf.write(u"\3\2\2\2\u07a2\u07a3\b\u00a5\1\2\u07a3\u07a6\7\u0092")
        buf.write(u"\2\2\u07a4\u07a6\5\u014c\u00a7\2\u07a5\u07a2\3\2\2\2")
        buf.write(u"\u07a5\u07a4\3\2\2\2\u07a6\u07ac\3\2\2\2\u07a7\u07a8")
        buf.write(u"\f\3\2\2\u07a8\u07a9\7\24\2\2\u07a9\u07ab\5\u014c\u00a7")
        buf.write(u"\2\u07aa\u07a7\3\2\2\2\u07ab\u07ae\3\2\2\2\u07ac\u07aa")
        buf.write(u"\3\2\2\2\u07ac\u07ad\3\2\2\2\u07ad\u0149\3\2\2\2\u07ae")
        buf.write(u"\u07ac\3\2\2\2\u07af\u07b5\7\u0094\2\2\u07b0\u07b5\7")
        buf.write(u"\u0096\2\2\u07b1\u07b5\7\u0093\2\2\u07b2\u07b5\7\u008a")
        buf.write(u"\2\2\u07b3\u07b5\7\u008b\2\2\u07b4\u07af\3\2\2\2\u07b4")
        buf.write(u"\u07b0\3\2\2\2\u07b4\u07b1\3\2\2\2\u07b4\u07b2\3\2\2")
        buf.write(u"\2\u07b4\u07b3\3\2\2\2\u07b5\u014b\3\2\2\2\u07b6\u07b7")
        buf.write(u"\t\6\2\2\u07b7\u014d\3\2\2\2\u07b8\u07b9\7y\2\2\u07b9")
        buf.write(u"\u07ba\5\u0150\u00a9\2\u07ba\u07bb\7\21\2\2\u07bb\u07c0")
        buf.write(u"\3\2\2\2\u07bc\u07bd\5\u0150\u00a9\2\u07bd\u07be\7\21")
        buf.write(u"\2\2\u07be\u07c0\3\2\2\2\u07bf\u07b8\3\2\2\2\u07bf\u07bc")
        buf.write(u"\3\2\2\2\u07c0\u014f\3\2\2\2\u07c1\u07c2\b\u00a9\1\2")
        buf.write(u"\u07c2\u07c3\5\u0152\u00aa\2\u07c3\u07c8\3\2\2\2\u07c4")
        buf.write(u"\u07c5\f\3\2\2\u07c5\u07c7\5\u0156\u00ac\2\u07c6\u07c4")
        buf.write(u"\3\2\2\2\u07c7\u07ca\3\2\2\2\u07c8\u07c6\3\2\2\2\u07c8")
        buf.write(u"\u07c9\3\2\2\2\u07c9\u0151\3\2\2\2\u07ca\u07c8\3\2\2")
        buf.write(u"\2\u07cb\u07d0\5\u0154\u00ab\2\u07cc\u07d0\5\u015e\u00b0")
        buf.write(u"\2\u07cd\u07d0\5\u0160\u00b1\2\u07ce\u07d0\5\u0164\u00b3")
        buf.write(u"\2\u07cf\u07cb\3\2\2\2\u07cf\u07cc\3\2\2\2\u07cf\u07cd")
        buf.write(u"\3\2\2\2\u07cf\u07ce\3\2\2\2\u07d0\u0153\3\2\2\2\u07d1")
        buf.write(u"\u07d2\5\u00f2z\2\u07d2\u0155\3\2\2\2\u07d3\u07d4\7\24")
        buf.write(u"\2\2\u07d4\u07d7\5\u0158\u00ad\2\u07d5\u07d7\5\u015c")
        buf.write(u"\u00af\2\u07d6\u07d3\3\2\2\2\u07d6\u07d5\3\2\2\2\u07d7")
        buf.write(u"\u0157\3\2\2\2\u07d8\u07d9\5\u0166\u00b4\2\u07d9\u07db")
        buf.write(u"\7\25\2\2\u07da\u07dc\5\u015a\u00ae\2\u07db\u07da\3\2")
        buf.write(u"\2\2\u07db\u07dc\3\2\2\2\u07dc\u07dd\3\2\2\2\u07dd\u07de")
        buf.write(u"\7\26\2\2\u07de\u0159\3\2\2\2\u07df\u07e0\b\u00ae\1\2")
        buf.write(u"\u07e0\u07e1\5\u0150\u00a9\2\u07e1\u07e7\3\2\2\2\u07e2")
        buf.write(u"\u07e3\f\3\2\2\u07e3\u07e4\7\22\2\2\u07e4\u07e6\5\u0150")
        buf.write(u"\u00a9\2\u07e5\u07e2\3\2\2\2\u07e6\u07e9\3\2\2\2\u07e7")
        buf.write(u"\u07e5\3\2\2\2\u07e7\u07e8\3\2\2\2\u07e8\u015b\3\2\2")
        buf.write(u"\2\u07e9\u07e7\3\2\2\2\u07ea\u07eb\7\27\2\2\u07eb\u07ec")
        buf.write(u"\5\u0150\u00a9\2\u07ec\u07ed\7\30\2\2\u07ed\u015d\3\2")
        buf.write(u"\2\2\u07ee\u07ef\7\25\2\2\u07ef\u07f0\5\u0150\u00a9\2")
        buf.write(u"\u07f0\u07f1\7\26\2\2\u07f1\u015f\3\2\2\2\u07f2\u07f3")
        buf.write(u"\b\u00b1\1\2\u07f3\u07f4\5\u0166\u00b4\2\u07f4\u07fa")
        buf.write(u"\3\2\2\2\u07f5\u07f6\f\3\2\2\u07f6\u07f7\7\24\2\2\u07f7")
        buf.write(u"\u07f9\5\u0166\u00b4\2\u07f8\u07f5\3\2\2\2\u07f9\u07fc")
        buf.write(u"\3\2\2\2\u07fa\u07f8\3\2\2\2\u07fa\u07fb\3\2\2\2\u07fb")
        buf.write(u"\u0161\3\2\2\2\u07fc\u07fa\3\2\2\2\u07fd\u07fe\b\u00b2")
        buf.write(u"\1\2\u07fe\u07ff\5\u0160\u00b1\2\u07ff\u0804\3\2\2\2")
        buf.write(u"\u0800\u0801\f\3\2\2\u0801\u0803\7\u0092\2\2\u0802\u0800")
        buf.write(u"\3\2\2\2\u0803\u0806\3\2\2\2\u0804\u0802\3\2\2\2\u0804")
        buf.write(u"\u0805\3\2\2\2\u0805\u0163\3\2\2\2\u0806\u0804\3\2\2")
        buf.write(u"\2\u0807\u080d\7\u0094\2\2\u0808\u080d\7\u0096\2\2\u0809")
        buf.write(u"\u080d\7\u0093\2\2\u080a\u080d\7\u008a\2\2\u080b\u080d")
        buf.write(u"\7\u008b\2\2\u080c\u0807\3\2\2\2\u080c\u0808\3\2\2\2")
        buf.write(u"\u080c\u0809\3\2\2\2\u080c\u080a\3\2\2\2\u080c\u080b")
        buf.write(u"\3\2\2\2\u080d\u0165\3\2\2\2\u080e\u080f\t\7\2\2\u080f")
        buf.write(u"\u0167\3\2\2\2\u0810\u0811\7y\2\2\u0811\u0812\5\u016a")
        buf.write(u"\u00b6\2\u0812\u0813\7\21\2\2\u0813\u0818\3\2\2\2\u0814")
        buf.write(u"\u0815\5\u016a\u00b6\2\u0815\u0816\7\21\2\2\u0816\u0818")
        buf.write(u"\3\2\2\2\u0817\u0810\3\2\2\2\u0817\u0814\3\2\2\2\u0818")
        buf.write(u"\u0169\3\2\2\2\u0819\u081a\b\u00b6\1\2\u081a\u081b\5")
        buf.write(u"\u016c\u00b7\2\u081b\u0820\3\2\2\2\u081c\u081d\f\3\2")
        buf.write(u"\2\u081d\u081f\5\u0170\u00b9\2\u081e\u081c\3\2\2\2\u081f")
        buf.write(u"\u0822\3\2\2\2\u0820\u081e\3\2\2\2\u0820\u0821\3\2\2")
        buf.write(u"\2\u0821\u016b\3\2\2\2\u0822\u0820\3\2\2\2\u0823\u0828")
        buf.write(u"\5\u016e\u00b8\2\u0824\u0828\5\u0178\u00bd\2\u0825\u0828")
        buf.write(u"\5\u017a\u00be\2\u0826\u0828\5\u017c\u00bf\2\u0827\u0823")
        buf.write(u"\3\2\2\2\u0827\u0824\3\2\2\2\u0827\u0825\3\2\2\2\u0827")
        buf.write(u"\u0826\3\2\2\2\u0828\u016d\3\2\2\2\u0829\u082a\5\u00f2")
        buf.write(u"z\2\u082a\u016f\3\2\2\2\u082b\u082c\7\24\2\2\u082c\u082f")
        buf.write(u"\5\u0172\u00ba\2\u082d\u082f\5\u0176\u00bc\2\u082e\u082b")
        buf.write(u"\3\2\2\2\u082e\u082d\3\2\2\2\u082f\u0171\3\2\2\2\u0830")
        buf.write(u"\u0831\5\u017e\u00c0\2\u0831\u0833\7\25\2\2\u0832\u0834")
        buf.write(u"\5\u0174\u00bb\2\u0833\u0832\3\2\2\2\u0833\u0834\3\2")
        buf.write(u"\2\2\u0834\u0835\3\2\2\2\u0835\u0836\7\26\2\2\u0836\u0173")
        buf.write(u"\3\2\2\2\u0837\u0838\b\u00bb\1\2\u0838\u0839\5\u016a")
        buf.write(u"\u00b6\2\u0839\u083f\3\2\2\2\u083a\u083b\f\3\2\2\u083b")
        buf.write(u"\u083c\7\22\2\2\u083c\u083e\5\u016a\u00b6\2\u083d\u083a")
        buf.write(u"\3\2\2\2\u083e\u0841\3\2\2\2\u083f\u083d\3\2\2\2\u083f")
        buf.write(u"\u0840\3\2\2\2\u0840\u0175\3\2\2\2\u0841\u083f\3\2\2")
        buf.write(u"\2\u0842\u0843\7\27\2\2\u0843\u0844\5\u016a\u00b6\2\u0844")
        buf.write(u"\u0845\7\30\2\2\u0845\u0177\3\2\2\2\u0846\u0847\7\25")
        buf.write(u"\2\2\u0847\u0848\5\u016a\u00b6\2\u0848\u0849\7\26\2\2")
        buf.write(u"\u0849\u0179\3\2\2\2\u084a\u084b\b\u00be\1\2\u084b\u084e")
        buf.write(u"\7\u0092\2\2\u084c\u084e\5\u017e\u00c0\2\u084d\u084a")
        buf.write(u"\3\2\2\2\u084d\u084c\3\2\2\2\u084e\u0854\3\2\2\2\u084f")
        buf.write(u"\u0850\f\3\2\2\u0850\u0851\7\24\2\2\u0851\u0853\5\u017e")
        buf.write(u"\u00c0\2\u0852\u084f\3\2\2\2\u0853\u0856\3\2\2\2\u0854")
        buf.write(u"\u0852\3\2\2\2\u0854\u0855\3\2\2\2\u0855\u017b\3\2\2")
        buf.write(u"\2\u0856\u0854\3\2\2\2\u0857\u085d\7\u0094\2\2\u0858")
        buf.write(u"\u085d\7\u0096\2\2\u0859\u085d\7\u0093\2\2\u085a\u085d")
        buf.write(u"\7\u008a\2\2\u085b\u085d\7\u008b\2\2\u085c\u0857\3\2")
        buf.write(u"\2\2\u085c\u0858\3\2\2\2\u085c\u0859\3\2\2\2\u085c\u085a")
        buf.write(u"\3\2\2\2\u085c\u085b\3\2\2\2\u085d\u017d\3\2\2\2\u085e")
        buf.write(u"\u085f\t\b\2\2\u085f\u017f\3\2\2\2\u00aa\u0186\u018d")
        buf.write(u"\u01ab\u01b3\u01ba\u01c5\u01ce\u01dd\u01e6\u01ed\u01f7")
        buf.write(u"\u021d\u022b\u0239\u0247\u025b\u0266\u0268\u0271\u0275")
        buf.write(u"\u027d\u0281\u0290\u0294\u02af\u02b6\u02bb\u02bf\u02d0")
        buf.write(u"\u02d4\u02d7\u02f8\u030b\u0312\u0334\u033d\u0354\u0364")
        buf.write(u"\u0369\u0371\u037a\u0391\u0395\u03b1\u0411\u0413\u041d")
        buf.write(u"\u0432\u0442\u0447\u044d\u0452\u0454\u0457\u045d\u045f")
        buf.write(u"\u0461\u047f\u0486\u0488\u048d\u048f\u049a\u04ad\u04b6")
        buf.write(u"\u04bc\u04c1\u04c8\u04d0\u04de\u04e6\u04ec\u04f7\u0503")
        buf.write(u"\u050e\u051b\u051f\u0525\u0531\u0545\u0547\u054c\u0558")
        buf.write(u"\u0563\u056d\u0572\u0577\u0587\u058c\u058f\u0593\u0598")
        buf.write(u"\u059f\u05aa\u05ac\u05b8\u05c0\u05cb\u05d0\u05dc\u05e0")
        buf.write(u"\u05ea\u05f2\u05f8\u05ff\u0604\u060e\u0615\u0620\u062d")
        buf.write(u"\u0631\u0634\u0638\u063b\u0646\u0652\u065e\u066a\u067b")
        buf.write(u"\u068a\u0694\u069b\u06a5\u06ac\u06b0\u06b6\u06c2\u06cd")
        buf.write(u"\u06dd\u06ea\u06f1\u06f9\u0715\u071e\u0727\u0730\u0735")
        buf.write(u"\u0741\u0753\u075a\u0763\u076a\u0772\u0777\u0781\u078b")
        buf.write(u"\u079b\u07a5\u07ac\u07b4\u07bf\u07c8\u07cf\u07d6\u07db")
        buf.write(u"\u07e7\u07fa\u0804\u080c\u0817\u0820\u0827\u082e\u0833")
        buf.write(u"\u083f\u084d\u0854\u085c")
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
                     u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'\\'", u"'%'", u"'>'", u"'>='", u"'<'", 
                     u"'<='", u"'<>'", u"'='", u"'!='", u"'=='", u"'~='", 
                     u"'~'", u"'<-'", u"'->'", u"'Boolean'", u"'Character'", 
                     u"'Text'", u"'Integer'", u"'Decimal'", u"'Date'", u"'Time'", 
                     u"'DateTime'", u"'Period'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"'attr'", u"'attribute'", 
                     u"'attributes'", u"'bindings'", u"'case'", u"'catch'", 
                     u"'category'", u"'class'", u"'close'", u"'contains'", 
                     u"'def'", u"'default'", u"'define'", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
                     u"'methods'", u"'modulo'", u"'mutable'", u"'native'", 
                     u"'None'", u"'not'", u"<INVALID>", u"'null'", u"'on'", 
                     u"'open'", u"'operator'", u"'or'", u"'otherwise'", 
                     u"'pass'", u"'raise'", u"'read'", u"'receiving'", u"'resource'", 
                     u"'return'", u"'returning'", u"'self'", u"'setter'", 
                     u"'singleton'", u"'sorted'", u"'switch'", u"'test'", 
                     u"'this'", u"'throw'", u"'to'", u"'try'", u"'with'", 
                     u"'when'", u"'where'", u"'while'", u"'write'", u"<INVALID>", 
                     u"<INVALID>", u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"INDENT", u"DEDENT", u"LF_TAB", u"LF_MORE", 
                      u"LF", u"TAB", u"WS", u"JAVA", u"CSHARP", u"PYTHON2", 
                      u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", u"SEMI", 
                      u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", u"LBRAK", 
                      u"RBRAK", u"LCURL", u"RCURL", u"QMARK", u"XMARK", 
                      u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", u"MINUS", 
                      u"STAR", u"SLASH", u"BSLASH", u"PERCENT", u"GT", u"GTE", 
                      u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", u"EQ2", u"TEQ", 
                      u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", u"CHARACTER", 
                      u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", u"TIME", 
                      u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", u"DOCUMENT", 
                      u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", u"ANY", u"AS", 
                      u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", u"BINDINGS", 
                      u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DO", 
                      u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FINALLY", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INVOKE", u"IS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"OPEN", u"OPERATOR", 
                      u"OR", u"OTHERWISE", u"PASS", u"RAISE", u"READ", u"RECEIVING", 
                      u"RESOURCE", u"RETURN", u"RETURNING", u"SELF", u"SETTER", 
                      u"SINGLETON", u"SORTED", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"WITH", u"WHEN", u"WHERE", 
                      u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", u"CHAR_LITERAL", 
                      u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"INTEGER_LITERAL", 
                      u"HEXA_LITERAL", u"DECIMAL_LITERAL", u"DATETIME_LITERAL", 
                      u"TIME_LITERAL", u"DATE_LITERAL", u"PERIOD_LITERAL", 
                      u"COMMENT" ]

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
    RULE_method_call_statement = 24
    RULE_with_resource_statement = 25
    RULE_with_singleton_statement = 26
    RULE_switch_statement = 27
    RULE_switch_case_statement = 28
    RULE_for_each_statement = 29
    RULE_do_while_statement = 30
    RULE_while_statement = 31
    RULE_if_statement = 32
    RULE_else_if_statement_list = 33
    RULE_raise_statement = 34
    RULE_try_statement = 35
    RULE_catch_statement = 36
    RULE_return_statement = 37
    RULE_expression = 38
    RULE_unresolved_expression = 39
    RULE_unresolved_selector = 40
    RULE_invocation_expression = 41
    RULE_invocation_trailer = 42
    RULE_instance_expression = 43
    RULE_instance_selector = 44
    RULE_document_expression = 45
    RULE_constructor_expression = 46
    RULE_read_expression = 47
    RULE_write_statement = 48
    RULE_ambiguous_expression = 49
    RULE_fetch_expression = 50
    RULE_sorted_expression = 51
    RULE_argument_assignment_list = 52
    RULE_with_argument_assignment_list = 53
    RULE_argument_assignment = 54
    RULE_assign_instance_statement = 55
    RULE_child_instance = 56
    RULE_assign_tuple_statement = 57
    RULE_lfs = 58
    RULE_lfp = 59
    RULE_indent = 60
    RULE_dedent = 61
    RULE_null_literal = 62
    RULE_declaration_list = 63
    RULE_declarations = 64
    RULE_declaration = 65
    RULE_resource_declaration = 66
    RULE_enum_declaration = 67
    RULE_native_symbol_list = 68
    RULE_category_symbol_list = 69
    RULE_symbol_list = 70
    RULE_attribute_constraint = 71
    RULE_list_literal = 72
    RULE_set_literal = 73
    RULE_expression_list = 74
    RULE_range_literal = 75
    RULE_typedef = 76
    RULE_primary_type = 77
    RULE_native_type = 78
    RULE_category_type = 79
    RULE_code_type = 80
    RULE_document_type = 81
    RULE_category_declaration = 82
    RULE_type_identifier_list = 83
    RULE_method_identifier = 84
    RULE_identifier = 85
    RULE_variable_identifier = 86
    RULE_type_identifier = 87
    RULE_symbol_identifier = 88
    RULE_argument_list = 89
    RULE_argument = 90
    RULE_operator_argument = 91
    RULE_named_argument = 92
    RULE_code_argument = 93
    RULE_category_or_any_type = 94
    RULE_any_type = 95
    RULE_member_method_declaration_list = 96
    RULE_member_method_declaration = 97
    RULE_native_member_method_declaration_list = 98
    RULE_native_member_method_declaration = 99
    RULE_native_category_binding = 100
    RULE_python_category_binding = 101
    RULE_python_module = 102
    RULE_module_token = 103
    RULE_javascript_category_binding = 104
    RULE_javascript_module = 105
    RULE_variable_identifier_list = 106
    RULE_method_declaration = 107
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
                   u"test_method_declaration", u"assertion", u"full_argument_list", 
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
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"module_token", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"method_declaration", 
                   u"native_statement_list", u"native_statement", u"python_native_statement", 
                   u"javascript_native_statement", u"statement_list", u"assertion_list", 
                   u"switch_case_statement_list", u"catch_statement_list", 
                   u"literal_collection", u"atomic_literal", u"literal_list_literal", 
                   u"selectable_expression", u"this_expression", u"parenthesis_expression", 
                   u"literal_expression", u"collection_literal", u"tuple_literal", 
                   u"dict_literal", u"expression_tuple", u"dict_entry_list", 
                   u"dict_entry", u"slice_arguments", u"assign_variable_statement", 
                   u"assignable_instance", u"is_expression", u"operator", 
                   u"key_token", u"value_token", u"symbols_token", u"assign", 
                   u"multiply", u"divide", u"idivide", u"modulo", u"javascript_statement", 
                   u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_selector_expression", 
                   u"javascript_method_expression", u"javascript_arguments", 
                   u"javascript_item_expression", u"javascript_parenthesis_expression", 
                   u"javascript_identifier_expression", u"javascript_literal_expression", 
                   u"javascript_identifier", u"python_statement", u"python_expression", 
                   u"python_primary_expression", u"python_selector_expression", 
                   u"python_method_expression", u"python_argument_list", 
                   u"python_ordinal_argument_list", u"python_named_argument_list", 
                   u"python_parenthesis_expression", u"python_identifier_expression", 
                   u"python_literal_expression", u"python_identifier", u"java_statement", 
                   u"java_expression", u"java_primary_expression", u"java_this_expression", 
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
    AMP=27
    AMP2=28
    PIPE=29
    PIPE2=30
    PLUS=31
    MINUS=32
    STAR=33
    SLASH=34
    BSLASH=35
    PERCENT=36
    GT=37
    GTE=38
    LT=39
    LTE=40
    LTGT=41
    EQ=42
    XEQ=43
    EQ2=44
    TEQ=45
    TILDE=46
    LARROW=47
    RARROW=48
    BOOLEAN=49
    CHARACTER=50
    TEXT=51
    INTEGER=52
    DECIMAL=53
    DATE=54
    TIME=55
    DATETIME=56
    PERIOD=57
    METHOD_T=58
    CODE=59
    DOCUMENT=60
    ABSTRACT=61
    ALL=62
    ALWAYS=63
    AND=64
    ANY=65
    AS=66
    ATTR=67
    ATTRIBUTE=68
    ATTRIBUTES=69
    BINDINGS=70
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
    EXPECTING=88
    EXTENDS=89
    FETCH=90
    FINALLY=91
    FOR=92
    FROM=93
    GETTER=94
    IF=95
    IN=96
    INVOKE=97
    IS=98
    MATCHING=99
    METHOD=100
    METHODS=101
    MODULO=102
    MUTABLE=103
    NATIVE=104
    NONE=105
    NOT=106
    NOTHING=107
    NULL=108
    ON=109
    OPEN=110
    OPERATOR=111
    OR=112
    OTHERWISE=113
    PASS=114
    RAISE=115
    READ=116
    RECEIVING=117
    RESOURCE=118
    RETURN=119
    RETURNING=120
    SELF=121
    SETTER=122
    SINGLETON=123
    SORTED=124
    SWITCH=125
    TEST=126
    THIS=127
    THROW=128
    TO=129
    TRY=130
    WITH=131
    WHEN=132
    WHERE=133
    WHILE=134
    WRITE=135
    BOOLEAN_LITERAL=136
    CHAR_LITERAL=137
    MIN_INTEGER=138
    MAX_INTEGER=139
    SYMBOL_IDENTIFIER=140
    TYPE_IDENTIFIER=141
    VARIABLE_IDENTIFIER=142
    NATIVE_IDENTIFIER=143
    DOLLAR_IDENTIFIER=144
    TEXT_LITERAL=145
    INTEGER_LITERAL=146
    HEXA_LITERAL=147
    DECIMAL_LITERAL=148
    DATETIME_LITERAL=149
    TIME_LITERAL=150
    DATE_LITERAL=151
    PERIOD_LITERAL=152
    COMMENT=153

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
            self.state = 382
            self.match(EParser.DEFINE)
            self.state = 383 
            localctx.name = self.type_identifier()
            self.state = 384
            self.match(EParser.AS)
            self.state = 385
            self.match(EParser.ENUMERATED)
            self.state = 388
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 386
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 387 
                localctx.derived = self.type_identifier()

            else:
                raise NoViableAltException(self)

            self.state = 395
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 390 
                localctx.attrs = self.attribute_list()
                self.state = 391
                self.match(EParser.COMMA)
                self.state = 392
                self.match(EParser.AND)
                pass

            elif la_ == 2:
                self.state = 394
                self.match(EParser.WITH)
                pass


            self.state = 397 
            self.symbols_token()
            self.state = 398
            self.match(EParser.COLON)
            self.state = 399 
            self.indent()
            self.state = 400 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 401 
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
            self.state = 403
            self.match(EParser.DEFINE)
            self.state = 404 
            localctx.name = self.type_identifier()
            self.state = 405
            self.match(EParser.AS)
            self.state = 406
            self.match(EParser.ENUMERATED)
            self.state = 407 
            localctx.typ = self.native_type()
            self.state = 408
            self.match(EParser.WITH)
            self.state = 409 
            self.symbols_token()
            self.state = 410
            self.match(EParser.COLON)
            self.state = 411 
            self.indent()
            self.state = 412 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 413 
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
            self.state = 415 
            localctx.name = self.symbol_identifier()
            self.state = 416
            self.match(EParser.WITH)
            self.state = 417 
            localctx.exp = self.expression(0)
            self.state = 418
            self.match(EParser.AS)
            self.state = 419 
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
            self.state = 421 
            localctx.name = self.symbol_identifier()
            self.state = 422 
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 425
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 423
                self.match(EParser.AND)
                self.state = 424 
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
            self.state = 427
            self.match(EParser.DEFINE)
            self.state = 428 
            localctx.name = self.variable_identifier()
            self.state = 429
            self.match(EParser.AS)
            self.state = 430 
            localctx.typ = self.typedef(0)
            self.state = 431
            self.match(EParser.ATTRIBUTE)
            self.state = 433
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 432 
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(EParser.DEFINE)
            self.state = 436 
            localctx.name = self.type_identifier()
            self.state = 437
            self.match(EParser.AS)
            self.state = 440
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 438
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 439 
                localctx.derived = self.derived_list()

            else:
                raise NoViableAltException(self)

            self.state = 460
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 442 
                localctx.attrs = self.attribute_list()
                self.state = 451
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 443
                    self.match(EParser.COMMA)
                    self.state = 444
                    self.match(EParser.AND)
                    self.state = 445
                    self.match(EParser.METHODS)
                    self.state = 446
                    self.match(EParser.COLON)
                    self.state = 447 
                    self.indent()
                    self.state = 448 
                    localctx.methods = self.member_method_declaration_list(0)
                    self.state = 449 
                    self.dedent()



            elif la_ == 2:
                self.state = 453
                self.match(EParser.WITH)
                self.state = 454
                self.match(EParser.METHODS)
                self.state = 455
                self.match(EParser.COLON)
                self.state = 456 
                self.indent()
                self.state = 457 
                localctx.methods = self.member_method_declaration_list(0)
                self.state = 458 
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
            self.state = 462
            self.match(EParser.DEFINE)
            self.state = 463 
            localctx.name = self.type_identifier()
            self.state = 464
            self.match(EParser.AS)
            self.state = 465
            self.match(EParser.SINGLETON)
            self.state = 484
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 466 
                localctx.attrs = self.attribute_list()
                self.state = 475
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 467
                    self.match(EParser.COMMA)
                    self.state = 468
                    self.match(EParser.AND)
                    self.state = 469
                    self.match(EParser.METHODS)
                    self.state = 470
                    self.match(EParser.COLON)
                    self.state = 471 
                    self.indent()
                    self.state = 472 
                    localctx.methods = self.member_method_declaration_list(0)
                    self.state = 473 
                    self.dedent()



            elif la_ == 2:
                self.state = 477
                self.match(EParser.WITH)
                self.state = 478
                self.match(EParser.METHODS)
                self.state = 479
                self.match(EParser.COLON)
                self.state = 480 
                self.indent()
                self.state = 481 
                localctx.methods = self.member_method_declaration_list(0)
                self.state = 482 
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
            self.state = 491
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 486 
                localctx.items = self.type_identifier_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 487 
                localctx.items = self.type_identifier_list(0)
                self.state = 488
                self.match(EParser.AND)
                self.state = 489 
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
            self.state = 493
            self.match(EParser.DEFINE)
            self.state = 494 
            localctx.op = self.operator()
            self.state = 495
            self.match(EParser.AS)
            self.state = 496
            self.match(EParser.OPERATOR)
            self.state = 497
            self.match(EParser.RECEIVING)
            self.state = 498 
            localctx.arg = self.operator_argument()
            self.state = 501
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 499
                self.match(EParser.RETURNING)
                self.state = 500 
                localctx.typ = self.typedef(0)


            self.state = 503
            self.match(EParser.DOING)
            self.state = 504
            self.match(EParser.COLON)
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
            self.state = 509
            self.match(EParser.DEFINE)
            self.state = 510 
            localctx.name = self.variable_identifier()
            self.state = 511
            self.match(EParser.SETTER)
            self.state = 512
            self.match(EParser.DOING)
            self.state = 513
            self.match(EParser.COLON)
            self.state = 514 
            self.indent()
            self.state = 515 
            localctx.stmts = self.statement_list(0)
            self.state = 516 
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
            self.state = 518
            self.match(EParser.DEFINE)
            self.state = 519 
            localctx.name = self.variable_identifier()
            self.state = 520
            self.match(EParser.GETTER)
            self.state = 521
            self.match(EParser.DOING)
            self.state = 522
            self.match(EParser.COLON)
            self.state = 523 
            self.indent()
            self.state = 524 
            localctx.stmts = self.statement_list(0)
            self.state = 525 
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(EParser.DEFINE)
            self.state = 528 
            localctx.name = self.type_identifier()
            self.state = 529
            self.match(EParser.AS)
            self.state = 530
            self.match(EParser.NATIVE)
            self.state = 531
            self.match(EParser.CATEGORY)
            self.state = 539
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 532 
                localctx.attrs = self.attribute_list()
                self.state = 533
                self.match(EParser.COMMA)
                self.state = 534
                self.match(EParser.AND)
                self.state = 535
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 537
                self.match(EParser.WITH)
                self.state = 538
                self.match(EParser.BINDINGS)
                pass


            self.state = 541
            self.match(EParser.COLON)
            self.state = 542 
            self.indent()
            self.state = 543 
            localctx.bindings = self.native_category_bindings()
            self.state = 544 
            self.dedent()
            self.state = 553
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 545 
                self.lfp()
                self.state = 546
                self.match(EParser.AND)
                self.state = 547
                self.match(EParser.METHODS)
                self.state = 548
                self.match(EParser.COLON)
                self.state = 549 
                self.indent()
                self.state = 550 
                localctx.methods = self.native_member_method_declaration_list(0)
                self.state = 551 
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
            self.state = 555
            self.match(EParser.DEFINE)
            self.state = 556 
            localctx.name = self.type_identifier()
            self.state = 557
            self.match(EParser.AS)
            self.state = 558
            self.match(EParser.NATIVE)
            self.state = 559
            self.match(EParser.RESOURCE)
            self.state = 567
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 560 
                localctx.attrs = self.attribute_list()
                self.state = 561
                self.match(EParser.COMMA)
                self.state = 562
                self.match(EParser.AND)
                self.state = 563
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 565
                self.match(EParser.WITH)
                self.state = 566
                self.match(EParser.BINDINGS)
                pass


            self.state = 569
            self.match(EParser.COLON)
            self.state = 570 
            self.indent()
            self.state = 571 
            localctx.bindings = self.native_category_bindings()
            self.state = 572 
            self.dedent()
            self.state = 581
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 573 
                self.lfp()
                self.state = 574
                self.match(EParser.AND)
                self.state = 575
                self.match(EParser.METHODS)
                self.state = 576
                self.match(EParser.COLON)
                self.state = 577 
                self.indent()
                self.state = 578 
                localctx.methods = self.native_member_method_declaration_list(0)
                self.state = 579 
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
            self.state = 583
            self.match(EParser.DEFINE)
            self.state = 584
            self.match(EParser.CATEGORY)
            self.state = 585
            self.match(EParser.BINDINGS)
            self.state = 586
            self.match(EParser.AS)
            self.state = 587
            self.match(EParser.COLON)
            self.state = 588 
            self.indent()
            self.state = 589 
            localctx.items = self.native_category_binding_list(0)
            self.state = 590 
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

            self.state = 593 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 601
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryBindingListItemContext(self, EParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 595
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 596 
                    self.lfp()
                    self.state = 597 
                    localctx.item = self.native_category_binding() 
                self.state = 603
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
            self.state = 614
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 604
                self.match(EParser.WITH)
                self.state = 605
                self.match(EParser.ATTRIBUTE)
                self.state = 606 
                localctx.item = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 607
                self.match(EParser.WITH)
                self.state = 608
                self.match(EParser.ATTRIBUTES)
                self.state = 609 
                localctx.items = self.variable_identifier_list(0)
                self.state = 612
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 610
                    self.match(EParser.AND)
                    self.state = 611 
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
            self.state = 616
            self.match(EParser.DEFINE)
            self.state = 617 
            localctx.name = self.method_identifier()
            self.state = 618
            self.match(EParser.AS)
            self.state = 619
            self.match(EParser.ABSTRACT)
            self.state = 620
            self.match(EParser.METHOD)
            self.state = 623
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 621
                self.match(EParser.RECEIVING)
                self.state = 622 
                localctx.args = self.full_argument_list()


            self.state = 627
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 625
                self.match(EParser.RETURNING)
                self.state = 626 
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
            self.state = 629
            self.match(EParser.DEFINE)
            self.state = 630 
            localctx.name = self.method_identifier()
            self.state = 631
            self.match(EParser.AS)
            self.state = 632
            self.match(EParser.METHOD)
            self.state = 635
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 633
                self.match(EParser.RECEIVING)
                self.state = 634 
                localctx.args = self.full_argument_list()


            self.state = 639
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 637
                self.match(EParser.RETURNING)
                self.state = 638 
                localctx.typ = self.typedef(0)


            self.state = 641
            self.match(EParser.DOING)
            self.state = 642
            self.match(EParser.COLON)
            self.state = 643 
            self.indent()
            self.state = 644 
            localctx.stmts = self.statement_list(0)
            self.state = 645 
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
            self.state = 647
            self.match(EParser.DEFINE)
            self.state = 648 
            localctx.name = self.method_identifier()
            self.state = 649
            self.match(EParser.AS)
            self.state = 650
            self.match(EParser.NATIVE)
            self.state = 651
            self.match(EParser.METHOD)
            self.state = 654
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 652
                self.match(EParser.RECEIVING)
                self.state = 653 
                localctx.args = self.full_argument_list()


            self.state = 658
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 656
                self.match(EParser.RETURNING)
                self.state = 657 
                localctx.typ = self.category_or_any_type()


            self.state = 660
            self.match(EParser.DOING)
            self.state = 661
            self.match(EParser.COLON)
            self.state = 662 
            self.indent()
            self.state = 663 
            localctx.stmts = self.native_statement_list(0)
            self.state = 664 
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

        def EXPECTING(self):
            return self.getToken(EParser.EXPECTING, 0)

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
            self.state = 666
            self.match(EParser.DEFINE)
            self.state = 667
            localctx.name = self.match(EParser.TEXT_LITERAL)
            self.state = 668
            self.match(EParser.AS)
            self.state = 669
            self.match(EParser.TEST)
            self.state = 670
            self.match(EParser.METHOD)
            self.state = 671
            self.match(EParser.DOING)
            self.state = 672
            self.match(EParser.COLON)
            self.state = 673 
            self.indent()
            self.state = 674 
            localctx.stmts = self.statement_list(0)
            self.state = 675 
            self.dedent()
            self.state = 676 
            self.lfp()
            self.state = 677
            self.match(EParser.AND)
            self.state = 678
            self.match(EParser.EXPECTING)
            self.state = 679
            self.match(EParser.COLON)
            self.state = 685
            token = self._input.LA(1)
            if token in [EParser.LF]:
                self.state = 680 
                self.indent()
                self.state = 681 
                localctx.exps = self.assertion_list(0)
                self.state = 682 
                self.dedent()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                self.state = 684 
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
            self.state = 687 
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
            self.state = 689 
            localctx.items = self.argument_list(0)
            self.state = 692
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 690
                self.match(EParser.AND)
                self.state = 691 
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
            self.state = 694 
            localctx.typ = self.category_or_any_type()
            self.state = 695 
            localctx.name = self.variable_identifier()
            self.state = 697
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 696 
                localctx.attrs = self.attribute_list()


            self.state = 701
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 699
                self.match(EParser.EQ)
                self.state = 700 
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
            self.state = 718
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 703 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 704 
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 705 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 706 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 5:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 707 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 6:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 708 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 7:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 709 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 8:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 710 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 9:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 711 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 10:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 712 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 11:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 713 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 12:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 714 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 13:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 715 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 14:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 716 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 15:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 717 
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
        self.enterRule(localctx, 48, self.RULE_method_call_statement)
        try:
            self.state = 725
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 720 
                localctx.exp = self.unresolved_expression(0)
                self.state = 722
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 721 
                    localctx.args = self.argument_assignment_list()



            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 724 
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
        self.enterRule(localctx, 50, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.match(EParser.WITH)
            self.state = 728 
            localctx.stmt = self.assign_variable_statement()
            self.state = 729
            self.match(EParser.COMMA)
            self.state = 730
            self.match(EParser.DO)
            self.state = 731
            self.match(EParser.COLON)
            self.state = 732 
            self.indent()
            self.state = 733 
            localctx.stmts = self.statement_list(0)
            self.state = 734 
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
        self.enterRule(localctx, 52, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736
            self.match(EParser.WITH)
            self.state = 737 
            localctx.typ = self.type_identifier()
            self.state = 738
            self.match(EParser.COMMA)
            self.state = 739
            self.match(EParser.DO)
            self.state = 740
            self.match(EParser.COLON)
            self.state = 741 
            self.indent()
            self.state = 742 
            localctx.stmts = self.statement_list(0)
            self.state = 743 
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
        self.enterRule(localctx, 54, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 745
            self.match(EParser.SWITCH)
            self.state = 746
            self.match(EParser.ON)
            self.state = 747 
            localctx.exp = self.expression(0)
            self.state = 748
            self.match(EParser.COLON)
            self.state = 749 
            self.indent()
            self.state = 750 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 758
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 751 
                self.lfp()
                self.state = 752
                self.match(EParser.OTHERWISE)
                self.state = 753
                self.match(EParser.COLON)
                self.state = 754 
                self.indent()
                self.state = 755 
                localctx.stmts = self.statement_list(0)
                self.state = 756 
                self.dedent()


            self.state = 760 
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
        self.enterRule(localctx, 56, self.RULE_switch_case_statement)
        try:
            self.state = 777
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 762
                self.match(EParser.WHEN)
                self.state = 763 
                localctx.exp = self.atomic_literal()
                self.state = 764
                self.match(EParser.COLON)
                self.state = 765 
                self.indent()
                self.state = 766 
                localctx.stmts = self.statement_list(0)
                self.state = 767 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 769
                self.match(EParser.WHEN)
                self.state = 770
                self.match(EParser.IN)
                self.state = 771 
                localctx.exp = self.literal_collection()
                self.state = 772
                self.match(EParser.COLON)
                self.state = 773 
                self.indent()
                self.state = 774 
                localctx.stmts = self.statement_list(0)
                self.state = 775 
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
        self.enterRule(localctx, 58, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            self.match(EParser.FOR)
            self.state = 780
            self.match(EParser.EACH)
            self.state = 781 
            localctx.name1 = self.variable_identifier()
            self.state = 784
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 782
                self.match(EParser.COMMA)
                self.state = 783 
                localctx.name2 = self.variable_identifier()


            self.state = 786
            self.match(EParser.IN)
            self.state = 787 
            localctx.source = self.expression(0)
            self.state = 788
            self.match(EParser.COLON)
            self.state = 789 
            self.indent()
            self.state = 790 
            localctx.stmts = self.statement_list(0)
            self.state = 791 
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
        self.enterRule(localctx, 60, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.match(EParser.DO)
            self.state = 794
            self.match(EParser.COLON)
            self.state = 795 
            self.indent()
            self.state = 796 
            localctx.stmts = self.statement_list(0)
            self.state = 797 
            self.dedent()
            self.state = 798 
            self.lfp()
            self.state = 799
            self.match(EParser.WHILE)
            self.state = 800 
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
        self.enterRule(localctx, 62, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
            self.match(EParser.WHILE)
            self.state = 803 
            localctx.exp = self.expression(0)
            self.state = 804
            self.match(EParser.COLON)
            self.state = 805 
            self.indent()
            self.state = 806 
            localctx.stmts = self.statement_list(0)
            self.state = 807 
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
        self.enterRule(localctx, 64, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self.match(EParser.IF)
            self.state = 810 
            localctx.exp = self.expression(0)
            self.state = 811
            self.match(EParser.COLON)
            self.state = 812 
            self.indent()
            self.state = 813 
            localctx.stmts = self.statement_list(0)
            self.state = 814 
            self.dedent()
            self.state = 818
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 815 
                self.lfp()
                self.state = 816 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 827
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 820 
                self.lfp()
                self.state = 821
                self.match(EParser.ELSE)
                self.state = 822
                self.match(EParser.COLON)
                self.state = 823 
                self.indent()
                self.state = 824 
                localctx.elseStmts = self.statement_list(0)
                self.state = 825 
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 830
            self.match(EParser.ELSE)
            self.state = 831
            self.match(EParser.IF)
            self.state = 832 
            localctx.exp = self.expression(0)
            self.state = 833
            self.match(EParser.COLON)
            self.state = 834 
            self.indent()
            self.state = 835 
            localctx.stmts = self.statement_list(0)
            self.state = 836 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 850
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 838
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 839 
                    self.lfp()
                    self.state = 840
                    self.match(EParser.ELSE)
                    self.state = 841
                    self.match(EParser.IF)
                    self.state = 842 
                    localctx.exp = self.expression(0)
                    self.state = 843
                    self.match(EParser.COLON)
                    self.state = 844 
                    self.indent()
                    self.state = 845 
                    localctx.stmts = self.statement_list(0)
                    self.state = 846 
                    self.dedent() 
                self.state = 852
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 853
            self.match(EParser.RAISE)
            self.state = 854 
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
        self.enterRule(localctx, 70, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 856
            self.match(EParser.SWITCH)
            self.state = 857
            self.match(EParser.ON)
            self.state = 858 
            localctx.name = self.variable_identifier()
            self.state = 859
            self.match(EParser.DOING)
            self.state = 860
            self.match(EParser.COLON)
            self.state = 861 
            self.indent()
            self.state = 862 
            localctx.stmts = self.statement_list(0)
            self.state = 863 
            self.dedent()
            self.state = 864 
            self.lfs()
            self.state = 866
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 865 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 879
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 871
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 868
                    self.match(EParser.OTHERWISE)

                elif token in [EParser.WHEN]:
                    self.state = 869
                    self.match(EParser.WHEN)
                    self.state = 870
                    self.match(EParser.ANY)

                else:
                    raise NoViableAltException(self)

                self.state = 873
                self.match(EParser.COLON)
                self.state = 874 
                self.indent()
                self.state = 875 
                localctx.anyStmts = self.statement_list(0)
                self.state = 876 
                self.dedent()
                self.state = 877 
                self.lfs()


            self.state = 888
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 881
                self.match(EParser.ALWAYS)
                self.state = 882
                self.match(EParser.COLON)
                self.state = 883 
                self.indent()
                self.state = 884 
                localctx.finalStmts = self.statement_list(0)
                self.state = 885 
                self.dedent()
                self.state = 886 
                self.lfs()


            self.state = 890 
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
        self.enterRule(localctx, 72, self.RULE_catch_statement)
        try:
            self.state = 911
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 892
                self.match(EParser.WHEN)
                self.state = 893 
                localctx.name = self.symbol_identifier()
                self.state = 894
                self.match(EParser.COLON)
                self.state = 895 
                self.indent()
                self.state = 896 
                localctx.stmts = self.statement_list(0)
                self.state = 897 
                self.dedent()
                self.state = 898 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 900
                self.match(EParser.WHEN)
                self.state = 901
                self.match(EParser.IN)
                self.state = 902
                self.match(EParser.LBRAK)
                self.state = 903 
                localctx.exp = self.symbol_list(0)
                self.state = 904
                self.match(EParser.RBRAK)
                self.state = 905
                self.match(EParser.COLON)
                self.state = 906 
                self.indent()
                self.state = 907 
                localctx.stmts = self.statement_list(0)
                self.state = 908 
                self.dedent()
                self.state = 909 
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
        self.enterRule(localctx, 74, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 913
            self.match(EParser.RETURN)
            self.state = 915
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 914 
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 943
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 918
                self.match(EParser.MINUS)
                self.state = 919 
                localctx.exp = self.expression(38)
                pass

            elif la_ == 2:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 920
                self.match(EParser.NOT)
                self.state = 921 
                localctx.exp = self.expression(37)
                pass

            elif la_ == 3:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 922
                self.match(EParser.CODE)
                self.state = 923
                self.match(EParser.COLON)
                self.state = 924 
                localctx.exp = self.expression(10)
                pass

            elif la_ == 4:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 925 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 926 
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 6:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 927 
                localctx.exp = self.unresolved_expression(0)
                self.state = 928 
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 930
                self.match(EParser.EXECUTE)
                self.state = 931
                self.match(EParser.COLON)
                self.state = 932 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 933
                self.match(EParser.METHOD_T)
                self.state = 934
                self.match(EParser.COLON)
                self.state = 935 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 936 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 10:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 937 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 11:
                localctx = EParser.FetchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 938 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 12:
                localctx = EParser.ReadExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 939 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 13:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 940 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 14:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 941 
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 15:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 942 
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1041
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1039
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 945
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 946 
                        self.multiply()
                        self.state = 947 
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 949
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 950 
                        self.divide()
                        self.state = 951 
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 953
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 954 
                        self.modulo()
                        self.state = 955 
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 957
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 958 
                        self.idivide()
                        self.state = 959 
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 961
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 962
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 963 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 964
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 965
                        self.match(EParser.LT)
                        self.state = 966 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 967
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 968
                        self.match(EParser.LTE)
                        self.state = 969 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 970
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 971
                        self.match(EParser.GT)
                        self.state = 972 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 973
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 974
                        self.match(EParser.GTE)
                        self.state = 975 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 976
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 977
                        self.match(EParser.EQ)
                        self.state = 978 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 979
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 980
                        self.match(EParser.LTGT)
                        self.state = 981 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 982
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 983
                        self.match(EParser.TILDE)
                        self.state = 984 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 13:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 985
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 986
                        self.match(EParser.OR)
                        self.state = 987 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 14:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 988
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 989
                        self.match(EParser.AND)
                        self.state = 990 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 15:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 991
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 992
                        self.match(EParser.IF)
                        self.state = 993 
                        localctx.test = self.expression(0)
                        self.state = 994
                        self.match(EParser.ELSE)
                        self.state = 995 
                        localctx.ifFalse = self.expression(21)
                        pass

                    elif la_ == 16:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 997
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 998
                        self.match(EParser.IN)
                        self.state = 999 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 17:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1000
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1001
                        self.match(EParser.CONTAINS)
                        self.state = 1002 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 18:
                        localctx = EParser.ContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1003
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1004
                        self.match(EParser.CONTAINS)
                        self.state = 1005
                        self.match(EParser.ALL)
                        self.state = 1006 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 19:
                        localctx = EParser.ContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1007
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1008
                        self.match(EParser.CONTAINS)
                        self.state = 1009
                        self.match(EParser.ANY)
                        self.state = 1010 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1011
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1012
                        self.match(EParser.NOT)
                        self.state = 1013
                        self.match(EParser.IN)
                        self.state = 1014 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1015
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1016
                        self.match(EParser.NOT)
                        self.state = 1017
                        self.match(EParser.CONTAINS)
                        self.state = 1018 
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1019
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1020
                        self.match(EParser.NOT)
                        self.state = 1021
                        self.match(EParser.CONTAINS)
                        self.state = 1022
                        self.match(EParser.ALL)
                        self.state = 1023 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 23:
                        localctx = EParser.NotContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1024
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1025
                        self.match(EParser.NOT)
                        self.state = 1026
                        self.match(EParser.CONTAINS)
                        self.state = 1027
                        self.match(EParser.ANY)
                        self.state = 1028 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 24:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1029
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1030
                        self.match(EParser.IS)
                        self.state = 1031
                        self.match(EParser.NOT)
                        self.state = 1032 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 25:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1033
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1034
                        self.match(EParser.IS)
                        self.state = 1035 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1036
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1037
                        self.match(EParser.AS)
                        self.state = 1038 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1043
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1045 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1051
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1047
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1048 
                    localctx.selector = self.unresolved_selector() 
                self.state = 1053
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1054
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1055
            self.match(EParser.DOT)
            self.state = 1056 
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
        self.enterRule(localctx, 82, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1058
            self.match(EParser.INVOKE)
            self.state = 1059
            self.match(EParser.COLON)
            self.state = 1060 
            localctx.name = self.variable_identifier()
            self.state = 1061 
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
        self.enterRule(localctx, 84, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1063
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1066 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1072
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1068
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1069 
                    localctx.selector = self.instance_selector() 
                self.state = 1074
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_instance_selector)
        try:
            self.state = 1088
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1075
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1076
                self.match(EParser.DOT)
                self.state = 1077 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1078
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1079
                self.match(EParser.LBRAK)
                self.state = 1080 
                localctx.xslice = self.slice_arguments()
                self.state = 1081
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1083
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1084
                self.match(EParser.LBRAK)
                self.state = 1085 
                localctx.exp = self.expression(0)
                self.state = 1086
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
        self.enterRule(localctx, 90, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1090 
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

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)
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
            self.typ = None # Category_typeContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)
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
        self.enterRule(localctx, 92, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1119
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1093
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1092
                    self.match(EParser.MUTABLE)


                self.state = 1095 
                localctx.typ = self.category_type()
                self.state = 1096
                self.match(EParser.FROM)
                self.state = 1097 
                localctx.firstArg = self.expression(0)
                self.state = 1106
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 1099
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1098
                        self.match(EParser.COMMA)


                    self.state = 1101 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1104
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        self.state = 1102
                        self.match(EParser.AND)
                        self.state = 1103 
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1109
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1108
                    self.match(EParser.MUTABLE)


                self.state = 1111 
                localctx.typ = self.category_type()
                self.state = 1117
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 1112 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1115
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        self.state = 1113
                        self.match(EParser.AND)
                        self.state = 1114 
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
        self.enterRule(localctx, 94, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1121
            self.match(EParser.READ)
            self.state = 1122
            self.match(EParser.FROM)
            self.state = 1123 
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
        self.enterRule(localctx, 96, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1125
            self.match(EParser.WRITE)
            self.state = 1126 
            localctx.what = self.expression(0)
            self.state = 1127
            self.match(EParser.TO)
            self.state = 1128 
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
        self.enterRule(localctx, 98, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1130 
            localctx.method = self.unresolved_expression(0)
            self.state = 1131
            self.match(EParser.MINUS)
            self.state = 1132 
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
        self.enterRule(localctx, 100, self.RULE_fetch_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1134
            self.match(EParser.FETCH)
            self.state = 1135
            self.match(EParser.ANY)
            self.state = 1136 
            localctx.name = self.variable_identifier()
            self.state = 1137
            self.match(EParser.FROM)
            self.state = 1138 
            localctx.source = self.expression(0)
            self.state = 1139
            self.match(EParser.WHERE)
            self.state = 1140 
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
        self.enterRule(localctx, 102, self.RULE_sorted_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1142
            self.match(EParser.SORTED)
            self.state = 1143 
            localctx.source = self.instance_expression(0)
            self.state = 1149
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 1144
                self.match(EParser.WITH)
                self.state = 1145 
                localctx.key = self.instance_expression(0)
                self.state = 1146
                self.match(EParser.AS)
                self.state = 1147 
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
        self.enterRule(localctx, 104, self.RULE_argument_assignment_list)
        try:
            self.state = 1165
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1151
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1152 
                localctx.exp = self.expression(0)
                self.state = 1158
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 1153 
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1156
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        self.state = 1154
                        self.match(EParser.AND)
                        self.state = 1155 
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1160 
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1163
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 1161
                    self.match(EParser.AND)
                    self.state = 1162 
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1168
            self.match(EParser.WITH)
            self.state = 1169 
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1171
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1172
                    self.match(EParser.COMMA)
                    self.state = 1173 
                    localctx.item = self.argument_assignment() 
                self.state = 1178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

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
        self.enterRule(localctx, 108, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1179 
            localctx.exp = self.expression(0)
            self.state = 1180
            self.match(EParser.AS)
            self.state = 1181 
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
        self.enterRule(localctx, 110, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1183 
            localctx.inst = self.assignable_instance(0)
            self.state = 1184 
            self.assign()
            self.state = 1185 
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
        self.enterRule(localctx, 112, self.RULE_child_instance)
        try:
            self.state = 1195
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1187
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1188
                self.match(EParser.DOT)
                self.state = 1189 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1190
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1191
                self.match(EParser.LBRAK)
                self.state = 1192 
                localctx.exp = self.expression(0)
                self.state = 1193
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
        self.enterRule(localctx, 114, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1197 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1198 
            self.assign()
            self.state = 1199 
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
        self.enterRule(localctx, 116, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1201
                    self.match(EParser.LF) 
                self.state = 1206
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
        self.enterRule(localctx, 118, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1208 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1207
                self.match(EParser.LF)
                self.state = 1210 
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
        self.enterRule(localctx, 120, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1213 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1212
                self.match(EParser.LF)
                self.state = 1215 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1217
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
        self.enterRule(localctx, 122, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1219
                self.match(EParser.LF)
                self.state = 1224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1225
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
        self.enterRule(localctx, 124, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1227
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
        self.enterRule(localctx, 126, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1230
            _la = self._input.LA(1)
            if _la==EParser.DEFINE:
                self.state = 1229 
                localctx.items = self.declarations(0)


            self.state = 1232 
            self.lfs()
            self.state = 1233
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
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1236 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DeclarationListItemContext(self, EParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1238
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1239 
                    self.lfp()
                    self.state = 1240 
                    localctx.item = self.declaration() 
                self.state = 1246
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
            super(EParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declaration

     
        def copyFrom(self, ctx):
            super(EParser.DeclarationContext, self).copyFrom(ctx)



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
        self.enterRule(localctx, 130, self.RULE_declaration)
        try:
            self.state = 1252
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1247 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1248 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1249 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1250 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = EParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1251 
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
        self.enterRule(localctx, 132, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1254 
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
        self.enterRule(localctx, 134, self.RULE_enum_declaration)
        try:
            self.state = 1258
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = EParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1256 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1257 
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
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1261 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeSymbolListItemContext(self, EParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1263
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1264 
                    self.lfp()
                    self.state = 1265 
                    localctx.item = self.native_symbol() 
                self.state = 1271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

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
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1273 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategorySymbolListItemContext(self, EParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1275
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1276 
                    self.lfp()
                    self.state = 1277 
                    localctx.item = self.category_symbol() 
                self.state = 1283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1285 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SymbolListItemContext(self, EParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1287
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1288
                    self.match(EParser.COMMA)
                    self.state = 1289 
                    localctx.item = self.symbol_identifier() 
                self.state = 1294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

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
        self.enterRule(localctx, 142, self.RULE_attribute_constraint)
        try:
            self.state = 1305
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1295
                self.match(EParser.IN)
                self.state = 1296 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1297
                self.match(EParser.IN)
                self.state = 1298 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1299
                self.match(EParser.IN)
                self.state = 1300 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1301
                self.match(EParser.MATCHING)
                self.state = 1302
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1303
                self.match(EParser.MATCHING)
                self.state = 1304 
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
        self.enterRule(localctx, 144, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1307
            self.match(EParser.LBRAK)
            self.state = 1309
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1308 
                localctx.items = self.expression_list(0)


            self.state = 1311
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
        self.enterRule(localctx, 146, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1313
            self.match(EParser.LT)
            self.state = 1315
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1314 
                localctx.items = self.expression_list(0)


            self.state = 1317
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
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1320 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueListItemContext(self, EParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1322
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1323
                    self.match(EParser.COMMA)
                    self.state = 1324 
                    localctx.item = self.expression(0) 
                self.state = 1329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

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
        self.enterRule(localctx, 150, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1330
            self.match(EParser.LBRAK)
            self.state = 1331 
            localctx.low = self.expression(0)
            self.state = 1332
            self.match(EParser.RANGE)
            self.state = 1333 
            localctx.high = self.expression(0)
            self.state = 1334
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
        _startState = 152
        self.enterRecursionRule(localctx, 152, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1337 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1347
                    la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                    if la_ == 1:
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1339
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1340
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1341
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1342
                        self.match(EParser.LBRAK)
                        self.state = 1343
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1344
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1345
                        self.match(EParser.LCURL)
                        self.state = 1346
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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
        self.enterRule(localctx, 154, self.RULE_primary_type)
        try:
            self.state = 1354
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1352 
                localctx.n = self.native_type()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1353 
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



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_native_type)
        try:
            self.state = 1366
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1356
                localctx.t1 = self.match(EParser.BOOLEAN)

            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1357
                localctx.t1 = self.match(EParser.CHARACTER)

            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1358
                localctx.t1 = self.match(EParser.TEXT)

            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1359
                localctx.t1 = self.match(EParser.INTEGER)

            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1360
                localctx.t1 = self.match(EParser.DECIMAL)

            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1361
                localctx.t1 = self.match(EParser.DATE)

            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1362
                localctx.t1 = self.match(EParser.DATETIME)

            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1363
                localctx.t1 = self.match(EParser.TIME)

            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1364
                localctx.t1 = self.match(EParser.PERIOD)

            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1365
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
        self.enterRule(localctx, 158, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1368
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
        self.enterRule(localctx, 160, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1370
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
        self.enterRule(localctx, 162, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1372
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
        self.enterRule(localctx, 164, self.RULE_category_declaration)
        try:
            self.state = 1377
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1374 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1375 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1376 
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
        _startState = 166
        self.enterRecursionRule(localctx, 166, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1380 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.TypeIdentifierListItemContext(self, EParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1382
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1383
                    self.match(EParser.COMMA)
                    self.state = 1384 
                    localctx.item = self.type_identifier() 
                self.state = 1389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

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
        self.enterRule(localctx, 168, self.RULE_method_identifier)
        try:
            self.state = 1392
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1390 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1391 
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
        self.enterRule(localctx, 170, self.RULE_identifier)
        try:
            self.state = 1397
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1394 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1395 
                localctx.name = self.type_identifier()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1396 
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
        self.enterRule(localctx, 172, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1399
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
        self.enterRule(localctx, 174, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
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
        self.enterRule(localctx, 176, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1403
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
        _startState = 178
        self.enterRecursionRule(localctx, 178, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1406 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentListItemContext(self, EParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1408
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1409
                    self.match(EParser.COMMA)
                    self.state = 1410 
                    localctx.item = self.argument() 
                self.state = 1415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

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
        self.enterRule(localctx, 180, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1421
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1416 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1418
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1417
                    self.match(EParser.MUTABLE)


                self.state = 1420 
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
        self.enterRule(localctx, 182, self.RULE_operator_argument)
        try:
            self.state = 1425
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1423 
                localctx.arg = self.named_argument()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1424 
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
        self.enterRule(localctx, 184, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1427 
            localctx.name = self.variable_identifier()
            self.state = 1430
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.state = 1428
                self.match(EParser.EQ)
                self.state = 1429 
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
        self.enterRule(localctx, 186, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1432 
            self.code_type()
            self.state = 1433 
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
        self.enterRule(localctx, 188, self.RULE_category_or_any_type)
        try:
            self.state = 1437
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1435 
                localctx.typ = self.typedef(0)

            elif token in [EParser.ANY]:
                localctx = EParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1436 
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
        _startState = 190
        self.enterRecursionRule(localctx, 190, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1440
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1448
                    la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1442
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1443
                        self.match(EParser.LBRAK)
                        self.state = 1444
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1445
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1446
                        self.match(EParser.LCURL)
                        self.state = 1447
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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
        _startState = 192
        self.enterRecursionRule(localctx, 192, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1454 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,95,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategoryMethodListItemContext(self, EParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1456
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1457 
                    self.lfp()
                    self.state = 1458 
                    localctx.item = self.member_method_declaration() 
                self.state = 1464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,95,self._ctx)

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
        self.enterRule(localctx, 194, self.RULE_member_method_declaration)
        try:
            self.state = 1470
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1465 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1466 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1467 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1468 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1469 
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
        _startState = 196
        self.enterRecursionRule(localctx, 196, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1473 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryMethodListItemContext(self, EParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1475
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1476 
                    self.lfp()
                    self.state = 1477 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

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
        self.enterRule(localctx, 198, self.RULE_native_member_method_declaration)
        try:
            self.state = 1486
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1484 
                self.member_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1485 
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
        self.enterRule(localctx, 200, self.RULE_native_category_binding)
        try:
            self.state = 1498
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1488
                self.match(EParser.JAVA)
                self.state = 1489 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1490
                self.match(EParser.CSHARP)
                self.state = 1491 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1492
                self.match(EParser.PYTHON2)
                self.state = 1493 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1494
                self.match(EParser.PYTHON3)
                self.state = 1495 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1496
                self.match(EParser.JAVASCRIPT)
                self.state = 1497 
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
        self.enterRule(localctx, 202, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1500 
            localctx.id_ = self.identifier()
            self.state = 1502
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.state = 1501 
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
        self.enterRule(localctx, 204, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1504
            self.match(EParser.FROM)
            self.state = 1505 
            self.module_token()
            self.state = 1506
            self.match(EParser.COLON)
            self.state = 1507 
            self.identifier()
            self.state = 1512
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1508
                    self.match(EParser.DOT)
                    self.state = 1509 
                    self.identifier() 
                self.state = 1514
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

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
        self.enterRule(localctx, 206, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1515
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1516
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
        self.enterRule(localctx, 208, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1518 
            localctx.id_ = self.identifier()
            self.state = 1520
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1519 
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
        self.enterRule(localctx, 210, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1522
            self.match(EParser.FROM)
            self.state = 1523 
            self.module_token()
            self.state = 1524
            self.match(EParser.COLON)
            self.state = 1526
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1525
                self.match(EParser.SLASH)


            self.state = 1528 
            self.javascript_identifier()
            self.state = 1533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,104,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1529
                    self.match(EParser.SLASH)
                    self.state = 1530 
                    self.javascript_identifier() 
                self.state = 1535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

            self.state = 1538
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 1536
                self.match(EParser.DOT)
                self.state = 1537 
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
        _startState = 212
        self.enterRecursionRule(localctx, 212, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1541 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.VariableListItemContext(self, EParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1543
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1544
                    self.match(EParser.COMMA)
                    self.state = 1545 
                    localctx.item = self.variable_identifier() 
                self.state = 1550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

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
        self.enterRule(localctx, 214, self.RULE_method_declaration)
        try:
            self.state = 1555
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                localctx = EParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1551 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1552 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1553 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1554 
                localctx.decl = self.test_method_declaration()
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
        _startState = 216
        self.enterRecursionRule(localctx, 216, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1558 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,108,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeStatementListItemContext(self, EParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1560
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1561 
                    self.lfp()
                    self.state = 1562 
                    localctx.item = self.native_statement() 
                self.state = 1568
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

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
        self.enterRule(localctx, 218, self.RULE_native_statement)
        try:
            self.state = 1579
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1569
                self.match(EParser.JAVA)
                self.state = 1570 
                localctx.stmt = self.java_statement()

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1571
                self.match(EParser.CSHARP)
                self.state = 1572 
                localctx.stmt = self.csharp_statement()

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1573
                self.match(EParser.PYTHON2)
                self.state = 1574 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1575
                self.match(EParser.PYTHON3)
                self.state = 1576 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1577
                self.match(EParser.JAVASCRIPT)
                self.state = 1578 
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
        self.enterRule(localctx, 220, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1581 
            localctx.stmt = self.python_statement()
            self.state = 1583
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 1582
                self.match(EParser.SEMI)


            self.state = 1586
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.state = 1585 
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
        self.enterRule(localctx, 222, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1588 
            localctx.stmt = self.javascript_statement()
            self.state = 1590
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.state = 1589
                self.match(EParser.SEMI)


            self.state = 1593
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 1592 
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
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1596 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1604
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.StatementListItemContext(self, EParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1598
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1599 
                    self.lfp()
                    self.state = 1600 
                    localctx.item = self.statement() 
                self.state = 1606
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

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
        _startState = 226
        self.enterRecursionRule(localctx, 226, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1608 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1616
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.AssertionListItemContext(self, EParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1610
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1611 
                    self.lfp()
                    self.state = 1612 
                    localctx.item = self.assertion() 
                self.state = 1618
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,115,self._ctx)

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
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1620 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1628
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SwitchCaseStatementListItemContext(self, EParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1622
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1623 
                    self.lfp()
                    self.state = 1624 
                    localctx.item = self.switch_case_statement() 
                self.state = 1630
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

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
        _startState = 230
        self.enterRecursionRule(localctx, 230, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1632 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1640
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CatchStatementListItemContext(self, EParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1634
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1635 
                    self.lfp()
                    self.state = 1636 
                    localctx.item = self.catch_statement() 
                self.state = 1642
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

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
        self.enterRule(localctx, 232, self.RULE_literal_collection)
        try:
            self.state = 1657
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1643
                self.match(EParser.LBRAK)
                self.state = 1644 
                localctx.low = self.atomic_literal()
                self.state = 1645
                self.match(EParser.RANGE)
                self.state = 1646 
                localctx.high = self.atomic_literal()
                self.state = 1647
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1649
                self.match(EParser.LBRAK)
                self.state = 1650 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1651
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1653
                self.match(EParser.LT)
                self.state = 1654 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1655
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
        self.enterRule(localctx, 234, self.RULE_atomic_literal)
        try:
            self.state = 1672
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1659
                localctx.t = self.match(EParser.MIN_INTEGER)

            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1660
                localctx.t = self.match(EParser.MAX_INTEGER)

            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1661
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1662
                localctx.t = self.match(EParser.HEXA_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1663
                localctx.t = self.match(EParser.CHAR_LITERAL)

            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1664
                localctx.t = self.match(EParser.DATE_LITERAL)

            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1665
                localctx.t = self.match(EParser.TIME_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1666
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1667
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1668
                localctx.t = self.match(EParser.DATETIME_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1669
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1670
                localctx.t = self.match(EParser.PERIOD_LITERAL)

            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1671 
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
        _startState = 236
        self.enterRecursionRule(localctx, 236, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1675 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1682
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,120,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.LiteralListItemContext(self, EParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1677
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1678
                    self.match(EParser.COMMA)
                    self.state = 1679 
                    localctx.item = self.atomic_literal() 
                self.state = 1684
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,120,self._ctx)

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
        self.enterRule(localctx, 238, self.RULE_selectable_expression)
        try:
            self.state = 1689
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1685 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1686 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1687 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1688 
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
        self.enterRule(localctx, 240, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1691
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
        self.enterRule(localctx, 242, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1693
            self.match(EParser.LPAR)
            self.state = 1694 
            localctx.exp = self.expression(0)
            self.state = 1695
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
        self.enterRule(localctx, 244, self.RULE_literal_expression)
        try:
            self.state = 1699
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                localctx = EParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1697 
                localctx.exp = self.atomic_literal()

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT]:
                localctx = EParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1698 
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
        self.enterRule(localctx, 246, self.RULE_collection_literal)
        try:
            self.state = 1706
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                localctx = EParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1701 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = EParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1702 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = EParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1703 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = EParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1704 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = EParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1705 
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
        self.enterRule(localctx, 248, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1708
            self.match(EParser.LPAR)
            self.state = 1710
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1709 
                localctx.items = self.expression_tuple(0)


            self.state = 1712
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
        self.enterRule(localctx, 250, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1714
            self.match(EParser.LCURL)
            self.state = 1716
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1715 
                localctx.items = self.dict_entry_list(0)


            self.state = 1718
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
        _startState = 252
        self.enterRecursionRule(localctx, 252, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1721 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1728
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueTupleItemContext(self, EParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1723
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1724
                    self.match(EParser.COMMA)
                    self.state = 1725 
                    localctx.item = self.expression(0) 
                self.state = 1730
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

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
        _startState = 254
        self.enterRecursionRule(localctx, 254, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1732 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1739
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DictEntryListItemContext(self, EParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1734
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1735
                    self.match(EParser.COMMA)
                    self.state = 1736 
                    localctx.item = self.dict_entry() 
                self.state = 1741
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

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
        self.enterRule(localctx, 256, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1742 
            localctx.key = self.expression(0)
            self.state = 1743
            self.match(EParser.COLON)
            self.state = 1744 
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
        self.enterRule(localctx, 258, self.RULE_slice_arguments)
        try:
            self.state = 1755
            la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1746 
                localctx.first = self.expression(0)
                self.state = 1747
                self.match(EParser.COLON)
                self.state = 1748 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1750 
                localctx.first = self.expression(0)
                self.state = 1751
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1753
                self.match(EParser.COLON)
                self.state = 1754 
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
        self.enterRule(localctx, 260, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1757 
            localctx.name = self.variable_identifier()
            self.state = 1758 
            self.assign()
            self.state = 1759 
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
        _startState = 262
        self.enterRecursionRule(localctx, 262, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1762 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1768
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1764
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1765 
                    localctx.child = self.child_instance() 
                self.state = 1770
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

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
        self.enterRule(localctx, 264, self.RULE_is_expression)
        try:
            self.state = 1775
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1771
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1772
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1773 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1774 
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
        self.enterRule(localctx, 266, self.RULE_operator)
        try:
            self.state = 1783
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1777
                self.match(EParser.PLUS)

            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1778
                self.match(EParser.MINUS)

            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1779 
                self.multiply()

            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1780 
                self.divide()

            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1781 
                self.idivide()

            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1782 
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
        self.enterRule(localctx, 268, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1785
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1786
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
        self.enterRule(localctx, 270, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1788
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1789
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
        self.enterRule(localctx, 272, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1791
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1792
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
        self.enterRule(localctx, 274, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1794
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
        self.enterRule(localctx, 276, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1796
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
        self.enterRule(localctx, 278, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1798
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
        self.enterRule(localctx, 280, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1800
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
        self.enterRule(localctx, 282, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1802
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
        self.enterRule(localctx, 284, self.RULE_javascript_statement)
        try:
            self.state = 1811
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1804
                self.match(EParser.RETURN)
                self.state = 1805 
                localctx.exp = self.javascript_expression(0)
                self.state = 1806
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1808 
                localctx.exp = self.javascript_expression(0)
                self.state = 1809
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
        _startState = 286
        self.enterRecursionRule(localctx, 286, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1814 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1820
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1816
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1817 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1822
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

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
        self.enterRule(localctx, 288, self.RULE_javascript_primary_expression)
        try:
            self.state = 1829
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1823 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1824 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1825 
                self.javascript_identifier_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1826 
                self.javascript_literal_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1827 
                self.javascript_method_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1828 
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
        self.enterRule(localctx, 290, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1831 
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
        self.enterRule(localctx, 292, self.RULE_javascript_selector_expression)
        try:
            self.state = 1838
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                localctx = EParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1833
                self.match(EParser.DOT)
                self.state = 1834 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = EParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1835
                self.match(EParser.DOT)
                self.state = 1836 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = EParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1837 
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
        self.enterRule(localctx, 294, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1840 
            localctx.name = self.javascript_identifier()
            self.state = 1841
            self.match(EParser.LPAR)
            self.state = 1843
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1842 
                localctx.args = self.javascript_arguments(0)


            self.state = 1845
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
        _startState = 296
        self.enterRecursionRule(localctx, 296, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1848 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1855
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1850
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1851
                    self.match(EParser.COMMA)
                    self.state = 1852 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1857
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

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
        self.enterRule(localctx, 298, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1858
            self.match(EParser.LBRAK)
            self.state = 1859 
            localctx.exp = self.javascript_expression(0)
            self.state = 1860
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
        self.enterRule(localctx, 300, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1862
            self.match(EParser.LPAR)
            self.state = 1863 
            localctx.exp = self.javascript_expression(0)
            self.state = 1864
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
        self.enterRule(localctx, 302, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1866 
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
        self.enterRule(localctx, 304, self.RULE_javascript_literal_expression)
        try:
            self.state = 1873
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1868
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1869
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1870
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1871
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1872
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
        self.enterRule(localctx, 306, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1875
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)))) != 0)):
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
        self.enterRule(localctx, 308, self.RULE_python_statement)
        try:
            self.state = 1880
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1877
                self.match(EParser.RETURN)
                self.state = 1878 
                localctx.exp = self.python_expression(0)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1879 
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
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1883 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1889
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1885
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1886 
                    localctx.child = self.python_selector_expression() 
                self.state = 1891
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

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
        self.enterRule(localctx, 312, self.RULE_python_primary_expression)
        try:
            self.state = 1896
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1892 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1893 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1894 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1895 
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
        self.enterRule(localctx, 314, self.RULE_python_selector_expression)
        try:
            self.state = 1904
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1898
                self.match(EParser.DOT)
                self.state = 1899 
                localctx.exp = self.python_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1900
                self.match(EParser.LBRAK)
                self.state = 1901 
                localctx.exp = self.python_expression(0)
                self.state = 1902
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
        self.enterRule(localctx, 316, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1906 
            localctx.name = self.python_identifier()
            self.state = 1907
            self.match(EParser.LPAR)
            self.state = 1909
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1908 
                localctx.args = self.python_argument_list()


            self.state = 1911
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
        self.enterRule(localctx, 318, self.RULE_python_argument_list)
        try:
            self.state = 1919
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1913 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1914 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1915 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1916
                self.match(EParser.COMMA)
                self.state = 1917 
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
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1922 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1929
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1924
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1925
                    self.match(EParser.COMMA)
                    self.state = 1926 
                    localctx.item = self.python_expression(0) 
                self.state = 1931
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

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
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1933 
            localctx.name = self.python_identifier()
            self.state = 1934
            self.match(EParser.EQ)
            self.state = 1935 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1945
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1937
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1938
                    self.match(EParser.COMMA)
                    self.state = 1939 
                    localctx.name = self.python_identifier()
                    self.state = 1940
                    self.match(EParser.EQ)
                    self.state = 1941 
                    localctx.exp = self.python_expression(0) 
                self.state = 1947
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

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
        self.enterRule(localctx, 324, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1948
            self.match(EParser.LPAR)
            self.state = 1949 
            localctx.exp = self.python_expression(0)
            self.state = 1950
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
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1955
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1953
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1954 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1962
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,148,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1957
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1958
                    self.match(EParser.DOT)
                    self.state = 1959 
                    localctx.name = self.python_identifier() 
                self.state = 1964
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,148,self._ctx)

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
        self.enterRule(localctx, 328, self.RULE_python_literal_expression)
        try:
            self.state = 1970
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1965
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1966
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1967
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1968
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1969
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
        self.enterRule(localctx, 330, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1972
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self.enterRule(localctx, 332, self.RULE_java_statement)
        try:
            self.state = 1981
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1974
                self.match(EParser.RETURN)
                self.state = 1975 
                localctx.exp = self.java_expression(0)
                self.state = 1976
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1978 
                localctx.exp = self.java_expression(0)
                self.state = 1979
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
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1984 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1990
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 1986
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1987 
                    localctx.child = self.java_selector_expression() 
                self.state = 1992
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

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
        self.enterRule(localctx, 336, self.RULE_java_primary_expression)
        try:
            self.state = 1997
            token = self._input.LA(1)
            if token in [EParser.SELF, EParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1993 
                self.java_this_expression()

            elif token in [EParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1994 
                self.java_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1995 
                self.java_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1996 
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
        self.enterRule(localctx, 338, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1999 
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
        self.enterRule(localctx, 340, self.RULE_java_selector_expression)
        try:
            self.state = 2004
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2001
                self.match(EParser.DOT)
                self.state = 2002 
                localctx.exp = self.java_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2003 
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
        self.enterRule(localctx, 342, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2006 
            localctx.name = self.java_identifier()
            self.state = 2007
            self.match(EParser.LPAR)
            self.state = 2009
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.NATIVE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 2008 
                localctx.args = self.java_arguments(0)


            self.state = 2011
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
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2014 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2021
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,155,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2016
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2017
                    self.match(EParser.COMMA)
                    self.state = 2018 
                    localctx.item = self.java_expression(0) 
                self.state = 2023
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

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
        self.enterRule(localctx, 346, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2024
            self.match(EParser.LBRAK)
            self.state = 2025 
            localctx.exp = self.java_expression(0)
            self.state = 2026
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
        self.enterRule(localctx, 348, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2028
            self.match(EParser.LPAR)
            self.state = 2029 
            localctx.exp = self.java_expression(0)
            self.state = 2030
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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2033 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2040
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2035
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2036
                    self.match(EParser.DOT)
                    self.state = 2037 
                    localctx.name = self.java_identifier() 
                self.state = 2042
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

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
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2044 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2050
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2046
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2047
                    localctx.name = self.match(EParser.DOLLAR_IDENTIFIER) 
                self.state = 2052
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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
        self.enterRule(localctx, 354, self.RULE_java_literal_expression)
        try:
            self.state = 2058
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2053
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2054
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2055
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2056
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2057
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
        self.enterRule(localctx, 356, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2060
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.NATIVE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)))) != 0)):
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
        self.enterRule(localctx, 358, self.RULE_csharp_statement)
        try:
            self.state = 2069
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2062
                self.match(EParser.RETURN)
                self.state = 2063 
                localctx.exp = self.csharp_expression(0)
                self.state = 2064
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2066 
                localctx.exp = self.csharp_expression(0)
                self.state = 2067
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
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2072 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2078
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2074
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2075 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2080
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

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
        self.enterRule(localctx, 362, self.RULE_csharp_primary_expression)
        try:
            self.state = 2085
            token = self._input.LA(1)
            if token in [EParser.SELF, EParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2081 
                self.csharp_this_expression()

            elif token in [EParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2082 
                self.csharp_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2083 
                self.csharp_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2084 
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
        self.enterRule(localctx, 364, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2087 
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
        self.enterRule(localctx, 366, self.RULE_csharp_selector_expression)
        try:
            self.state = 2092
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2089
                self.match(EParser.DOT)
                self.state = 2090 
                localctx.exp = self.csharp_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2091 
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
        self.enterRule(localctx, 368, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2094 
            localctx.name = self.csharp_identifier()
            self.state = 2095
            self.match(EParser.LPAR)
            self.state = 2097
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 2096 
                localctx.args = self.csharp_arguments(0)


            self.state = 2099
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
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2102 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,164,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2104
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2105
                    self.match(EParser.COMMA)
                    self.state = 2106 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,164,self._ctx)

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
        self.enterRule(localctx, 372, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2112
            self.match(EParser.LBRAK)
            self.state = 2113 
            localctx.exp = self.csharp_expression(0)
            self.state = 2114
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
        self.enterRule(localctx, 374, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2116
            self.match(EParser.LPAR)
            self.state = 2117 
            localctx.exp = self.csharp_expression(0)
            self.state = 2118
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
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2123
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2121
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2122 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2125
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2126
                    self.match(EParser.DOT)
                    self.state = 2127 
                    localctx.name = self.csharp_identifier() 
                self.state = 2132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

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
        self.enterRule(localctx, 378, self.RULE_csharp_literal_expression)
        try:
            self.state = 2138
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2133
                self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2134
                self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2135
                self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2136
                self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2137
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
        self.enterRule(localctx, 380, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self._predicates[33] = self.else_if_statement_list_sempred
        self._predicates[38] = self.expression_sempred
        self._predicates[39] = self.unresolved_expression_sempred
        self._predicates[40] = self.unresolved_selector_sempred
        self._predicates[42] = self.invocation_trailer_sempred
        self._predicates[43] = self.instance_expression_sempred
        self._predicates[44] = self.instance_selector_sempred
        self._predicates[52] = self.argument_assignment_list_sempred
        self._predicates[53] = self.with_argument_assignment_list_sempred
        self._predicates[56] = self.child_instance_sempred
        self._predicates[64] = self.declarations_sempred
        self._predicates[68] = self.native_symbol_list_sempred
        self._predicates[69] = self.category_symbol_list_sempred
        self._predicates[70] = self.symbol_list_sempred
        self._predicates[74] = self.expression_list_sempred
        self._predicates[76] = self.typedef_sempred
        self._predicates[83] = self.type_identifier_list_sempred
        self._predicates[89] = self.argument_list_sempred
        self._predicates[95] = self.any_type_sempred
        self._predicates[96] = self.member_method_declaration_list_sempred
        self._predicates[98] = self.native_member_method_declaration_list_sempred
        self._predicates[103] = self.module_token_sempred
        self._predicates[106] = self.variable_identifier_list_sempred
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
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def assertion_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.willBeAOrAn()
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 78:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 79:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 80:
                return self.precpred(self._ctx, 1)
         


