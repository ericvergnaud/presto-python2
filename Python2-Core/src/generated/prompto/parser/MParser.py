# Generated from MParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00b2\u08f4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca\t\u00ca\4\u00cb")
        buf.write(u"\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd\4\u00ce\t\u00ce")
        buf.write(u"\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1\t\u00d1\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\5\2\u01a9\n\2\3\2\5\2\u01ac\n\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u01c5\n")
        buf.write(u"\5\3\5\3\5\3\6\5\6\u01ca\n\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u01d8\n\6\3\6\3\6\3\6\3")
        buf.write(u"\6\5\6\u01de\n\6\5\6\u01e0\n\6\5\6\u01e2\n\6\3\6\3\6")
        buf.write(u"\3\7\3\7\3\7\5\7\u01e9\n\7\3\7\3\7\3\b\5\b\u01ee\n\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01f9\n\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\5\b\u0200\n\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u020d\n\t\3\t\3\t\3\n\3")
        buf.write(u"\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u021b")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u022f\n\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u0246\n\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\5\20\u0251")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\5\20\u0258\n\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\5\20\u0261\n\20\3\20\3\20")
        buf.write(u"\3\21\5\21\u0266\n\21\3\21\3\21\3\21\3\21\3\21\5\21\u026d")
        buf.write(u"\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0276\n")
        buf.write(u"\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u0289\n\23\f")
        buf.write(u"\23\16\23\u028c\13\23\3\24\3\24\3\24\3\24\3\24\5\24\u0293")
        buf.write(u"\n\24\3\24\3\24\3\24\5\24\u0298\n\24\3\25\3\25\3\25\3")
        buf.write(u"\25\5\25\u029e\n\25\3\25\3\25\3\25\5\25\u02a3\n\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u02ac\n\26\3\26")
        buf.write(u"\3\26\3\26\5\26\u02b1\n\26\3\26\3\26\3\26\5\26\u02b6")
        buf.write(u"\n\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\5\27\u02ce\n\27\3\30\3\30\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\5\31\u02d9\n\31\3\31\3\31\5\31\u02dd")
        buf.write(u"\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write(u"\u02f2\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\5\34\u030c\n\34\3\35\3\35\3")
        buf.write(u"\35\5\35\u0311\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\5\36\u031a\n\36\3\37\3\37\3\37\3\37\3\37\7\37\u0321")
        buf.write(u"\n\37\f\37\16\37\u0324\13\37\3 \3 \3 \3 \3 \3 \5 \u032c")
        buf.write(u"\n \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0349\n#\3")
        buf.write(u"#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$")
        buf.write(u"\u035c\n$\3%\3%\3%\3%\5%\u0362\n%\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0384\n(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\5(\u038d\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u03a2\n)\f)\16)\u03a5")
        buf.write(u"\13)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\5+\u03b2\n+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\5+\u03bb\n+\3+\3+\3+\3+\3+\3+\3+\5")
        buf.write(u"+\u03c4\n+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write(u"\3,\3,\3,\3,\3,\3,\3,\5,\u03db\n,\3-\3-\3.\3.\5.\u03e1")
        buf.write(u"\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\5/\u03f5\n/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u0464\n/\f/\16/\u0467")
        buf.write(u"\13/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\7\61\u0470\n")
        buf.write(u"\61\f\61\16\61\u0473\13\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write(u"\62\3\62\3\62\5\62\u047d\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write(u"\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u048c\n")
        buf.write(u"\63\3\64\3\64\3\64\5\64\u0491\n\64\3\64\3\64\3\65\3\65")
        buf.write(u"\3\65\5\65\u0498\n\65\3\65\3\65\3\66\3\66\3\66\3\66\3")
        buf.write(u"\66\5\66\u04a1\n\66\3\66\3\66\3\66\3\66\3\66\5\66\u04a8")
        buf.write(u"\n\66\3\66\3\66\5\66\u04ac\n\66\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\38\38\38\38\38\58\u04b8\n8\38\38\38\78\u04bd\n8\f")
        buf.write(u"8\168\u04c0\138\39\39\39\39\59\u04c6\n9\3:\3:\3:\3:\3")
        buf.write(u":\3;\3;\3;\3;\3;\3;\3<\3<\3<\5<\u04d6\n<\3<\3<\3<\3<")
        buf.write(u"\3<\3<\3<\3<\3<\5<\u04e1\n<\3<\3<\5<\u04e5\n<\3<\3<\3")
        buf.write(u"<\5<\u04ea\n<\3<\3<\3<\5<\u04ef\n<\5<\u04f1\n<\3=\3=")
        buf.write(u"\5=\u04f5\n=\3=\3=\3=\3=\3=\3=\3=\5=\u04fe\n=\3=\3=\3")
        buf.write(u">\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\5?\u050e\n?\3@\3@")
        buf.write(u"\3@\3@\3A\7A\u0515\nA\fA\16A\u0518\13A\3B\6B\u051b\n")
        buf.write(u"B\rB\16B\u051c\3C\6C\u0520\nC\rC\16C\u0521\3C\3C\3D\7")
        buf.write(u"D\u0527\nD\fD\16D\u052a\13D\3D\3D\3E\3E\3F\5F\u0531\n")
        buf.write(u"F\3F\3F\3F\3G\3G\3G\3G\7G\u053a\nG\fG\16G\u053d\13G\3")
        buf.write(u"H\3H\3H\7H\u0542\nH\fH\16H\u0545\13H\3H\3H\3H\3H\3H\5")
        buf.write(u"H\u054c\nH\3I\3I\3J\3J\5J\u0552\nJ\3K\3K\3K\3K\7K\u0558")
        buf.write(u"\nK\fK\16K\u055b\13K\3L\3L\3L\3L\7L\u0561\nL\fL\16L\u0564")
        buf.write(u"\13L\3M\3M\3M\7M\u0569\nM\fM\16M\u056c\13M\3N\3N\3N\3")
        buf.write(u"N\3N\3N\3N\3N\3N\3N\5N\u0578\nN\3O\5O\u057b\nO\3O\3O")
        buf.write(u"\5O\u057f\nO\3O\3O\3P\5P\u0584\nP\3P\3P\5P\u0588\nP\3")
        buf.write(u"P\3P\3Q\3Q\3Q\7Q\u058f\nQ\fQ\16Q\u0592\13Q\3R\3R\3R\3")
        buf.write(u"R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u05a6")
        buf.write(u"\nS\3S\3S\3S\3S\3S\3S\3S\3S\7S\u05b0\nS\fS\16S\u05b3")
        buf.write(u"\13S\3T\3T\5T\u05b7\nT\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U")
        buf.write(u"\3U\3U\3U\3U\3U\5U\u05c8\nU\3V\3V\3W\5W\u05cd\nW\3W\3")
        buf.write(u"W\3X\3X\3Y\3Y\3Y\5Y\u05d6\nY\3Z\3Z\3Z\7Z\u05db\nZ\fZ")
        buf.write(u"\16Z\u05de\13Z\3[\3[\5[\u05e2\n[\3\\\3\\\3\\\5\\\u05e7")
        buf.write(u"\n\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3a\7a\u05f4\na\fa")
        buf.write(u"\16a\u05f7\13a\3b\3b\5b\u05fb\nb\3b\5b\u05fe\nb\3c\3")
        buf.write(u"c\5c\u0602\nc\3d\3d\3d\5d\u0607\nd\3e\3e\3e\3f\3f\5f")
        buf.write(u"\u060e\nf\3g\3g\3g\3g\3g\3g\3g\3g\3g\7g\u0619\ng\fg\16")
        buf.write(u"g\u061c\13g\3h\3h\3h\3h\7h\u0622\nh\fh\16h\u0625\13h")
        buf.write(u"\3i\3i\3i\3i\3i\5i\u062c\ni\3j\3j\3j\3j\7j\u0632\nj\f")
        buf.write(u"j\16j\u0635\13j\3k\3k\3k\5k\u063a\nk\3l\3l\3l\3l\3l\3")
        buf.write(u"l\3l\3l\3l\3l\5l\u0646\nl\3m\3m\5m\u064a\nm\3n\3n\3n")
        buf.write(u"\3n\3n\3n\7n\u0652\nn\fn\16n\u0655\13n\3o\3o\5o\u0659")
        buf.write(u"\no\3p\3p\3p\3p\5p\u065f\np\3p\3p\3p\7p\u0664\np\fp\16")
        buf.write(u"p\u0667\13p\3p\3p\5p\u066b\np\3q\3q\3q\7q\u0670\nq\f")
        buf.write(u"q\16q\u0673\13q\3r\3r\3r\7r\u0678\nr\fr\16r\u067b\13")
        buf.write(u"r\3s\3s\3s\3s\5s\u0681\ns\3t\3t\3u\3u\3u\3u\7u\u0689")
        buf.write(u"\nu\fu\16u\u068c\13u\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\5")
        buf.write(u"v\u0698\nv\3w\3w\5w\u069c\nw\3w\5w\u069f\nw\3x\3x\5x")
        buf.write(u"\u06a3\nx\3x\5x\u06a6\nx\3y\3y\3y\3y\7y\u06ac\ny\fy\16")
        buf.write(u"y\u06af\13y\3z\3z\3z\3z\7z\u06b5\nz\fz\16z\u06b8\13z")
        buf.write(u"\3{\3{\3{\3{\7{\u06be\n{\f{\16{\u06c1\13{\3|\3|\3|\3")
        buf.write(u"|\7|\u06c7\n|\f|\16|\u06ca\13|\3}\3}\3}\3}\3}\3}\3}\3")
        buf.write(u"}\3}\3}\3}\3}\3}\3}\5}\u06da\n}\3~\3~\3~\3~\3~\3~\3~")
        buf.write(u"\3~\3~\3~\3~\3~\3~\3~\3~\5~\u06eb\n~\3\177\3\177\3\177")
        buf.write(u"\7\177\u06f0\n\177\f\177\16\177\u06f3\13\177\3\u0080")
        buf.write(u"\3\u0080\3\u0080\3\u0080\5\u0080\u06f9\n\u0080\3\u0081")
        buf.write(u"\3\u0081\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083")
        buf.write(u"\5\u0083\u0703\n\u0083\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\5\u0084\u070a\n\u0084\3\u0085\5\u0085\u070d")
        buf.write(u"\n\u0085\3\u0085\3\u0085\5\u0085\u0711\n\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0086\5\u0086\u0716\n\u0086\3\u0086\3\u0086")
        buf.write(u"\5\u0086\u071a\n\u0086\3\u0086\3\u0086\3\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0087\3\u0087\7\u0087\u0723\n\u0087\f\u0087")
        buf.write(u"\16\u0087\u0726\13\u0087\5\u0087\u0728\n\u0087\3\u0088")
        buf.write(u"\3\u0088\3\u0088\7\u0088\u072d\n\u0088\f\u0088\16\u0088")
        buf.write(u"\u0730\13\u0088\3\u0089\3\u0089\3\u0089\3\u0089\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008a\5\u008a\u073f\n\u008a\3\u008b\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\7\u008c")
        buf.write(u"\u074a\n\u008c\f\u008c\16\u008c\u074d\13\u008c\3\u008d")
        buf.write(u"\3\u008d\3\u008d\3\u008d\5\u008d\u0753\n\u008d\3\u008e")
        buf.write(u"\3\u008e\3\u008e\3\u008e\3\u008e\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\7\u0090\u0762")
        buf.write(u"\n\u0090\f\u0090\16\u0090\u0765\13\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\7\u0091\u076a\n\u0091\f\u0091\16\u0091\u076d")
        buf.write(u"\13\u0091\3\u0091\5\u0091\u0770\n\u0091\3\u0092\3\u0092")
        buf.write(u"\3\u0092\3\u0092\3\u0092\3\u0092\5\u0092\u0778\n\u0092")
        buf.write(u"\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094\3\u0095")
        buf.write(u"\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0097\3\u0097")
        buf.write(u"\3\u0097\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a")
        buf.write(u"\3\u009b\3\u009b\3\u009c\3\u009c\3\u009d\3\u009d\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009d\5\u009d\u079a\n\u009d")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\7\u009e\u07a1")
        buf.write(u"\n\u009e\f\u009e\16\u009e\u07a4\13\u009e\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\5\u009f\u07ad")
        buf.write(u"\n\u009f\3\u00a0\3\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a2")
        buf.write(u"\3\u00a2\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u07b9\n\u00a2")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\5\u00a3\u07be\n\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write(u"\7\u00a4\u07c8\n\u00a4\f\u00a4\16\u00a4\u07cb\13\u00a4")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\5\u00a8\u07dc\n\u00a8\3\u00a9\3\u00a9\3\u00aa")
        buf.write(u"\3\u00aa\3\u00aa\5\u00aa\u07e3\n\u00aa\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\7\u00ab\u07ea\n\u00ab\f\u00ab")
        buf.write(u"\16\u00ab\u07ed\13\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\5\u00ac\u07f4\n\u00ac\3\u00ad\3\u00ad\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u07fe")
        buf.write(u"\n\u00ae\3\u00af\3\u00af\3\u00af\5\u00af\u0803\n\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\5\u00b0\u080d\n\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u0815\n\u00b1\f\u00b1")
        buf.write(u"\16\u00b1\u0818\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\7\u00b2\u0825\n\u00b2\f\u00b2\16\u00b2\u0828\13\u00b2")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\5\u00b4\u0831\n\u00b4\3\u00b4\3\u00b4\3\u00b4\7\u00b4")
        buf.write(u"\u0836\n\u00b4\f\u00b4\16\u00b4\u0839\13\u00b4\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u0840\n\u00b5")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\5\u00b7\u084b\n\u00b7\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\3\u00b8\7\u00b8\u0852\n\u00b8\f\u00b8")
        buf.write(u"\16\u00b8\u0855\13\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\5\u00b9\u085c\n\u00b9\3\u00ba\3\u00ba\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bc\3\u00bc\3\u00bc\5\u00bc\u0866")
        buf.write(u"\n\u00bc\3\u00bd\3\u00bd\3\u00bd\5\u00bd\u086b\n\u00bd")
        buf.write(u"\3\u00bd\3\u00bd\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00be\7\u00be\u0875\n\u00be\f\u00be\16\u00be\u0878")
        buf.write(u"\13\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c0\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c1\7\u00c1\u0888\n\u00c1\f\u00c1\16\u00c1\u088b")
        buf.write(u"\13\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\7\u00c2")
        buf.write(u"\u0892\n\u00c2\f\u00c2\16\u00c2\u0895\13\u00c2\3\u00c3")
        buf.write(u"\3\u00c3\3\u00c3\3\u00c3\3\u00c3\5\u00c3\u089c\n\u00c3")
        buf.write(u"\3\u00c4\3\u00c4\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5")
        buf.write(u"\3\u00c5\3\u00c5\5\u00c5\u08a7\n\u00c5\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\7\u00c6\u08ae\n\u00c6\f\u00c6")
        buf.write(u"\16\u00c6\u08b1\13\u00c6\3\u00c7\3\u00c7\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c7\5\u00c7\u08b8\n\u00c7\3\u00c8\3\u00c8\3\u00c9")
        buf.write(u"\3\u00c9\3\u00c9\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u08c2")
        buf.write(u"\n\u00ca\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u08c7\n\u00cb")
        buf.write(u"\3\u00cb\3\u00cb\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\3\u00cc\7\u00cc\u08d1\n\u00cc\f\u00cc\16\u00cc\u08d4")
        buf.write(u"\13\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00ce\3\u00ce")
        buf.write(u"\3\u00ce\3\u00ce\3\u00cf\3\u00cf\3\u00cf\5\u00cf\u08e1")
        buf.write(u"\n\u00cf\3\u00cf\3\u00cf\3\u00cf\7\u00cf\u08e6\n\u00cf")
        buf.write(u"\f\u00cf\16\u00cf\u08e9\13\u00cf\3\u00d0\3\u00d0\3\u00d0")
        buf.write(u"\3\u00d0\3\u00d0\5\u00d0\u08f0\n\u00d0\3\u00d1\3\u00d1")
        buf.write(u"\3\u00d1\2\30$<P\\`n\u00a4\u00cc\u0116\u013a\u0146\u0154")
        buf.write(u"\u0160\u0162\u0166\u016e\u017a\u0180\u0182\u018a\u0196")
        buf.write(u"\u019c\u00d2\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write(u"\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write(u"vxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
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
        buf.write(u"\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a\u019c")
        buf.write(u"\u019e\u01a0\2\f\3\2UV\3\2\"#\4\2\u0092\u0092\u00a6\u00a6")
        buf.write(u"\4\2\u008e\u008e\u0096\u0096\4\2LL]]\4\2\'\'xx\f\2\64")
        buf.write(u"=CC{{~~\u0088\u0088\u008e\u008e\u0095\u0095\u009f\u009f")
        buf.write(u"\u00a4\u00a6\u00a8\u00a8\n\2\64=CC{{~~\u0088\u0088\u0095")
        buf.write(u"\u0096\u009f\u009f\u00a4\u00a6\13\2\64=CC{{~~\u0088\u0088")
        buf.write(u"\u008e\u008e\u0095\u0095\u009f\u009f\u00a4\u00a8\13\2")
        buf.write(u"\64=CC{{~~\u0088\u0088\u008e\u008e\u0095\u0095\u009f")
        buf.write(u"\u009f\u00a4\u00a6\2\u0972\2\u01a2\3\2\2\2\4\u01b3\3")
        buf.write(u"\2\2\2\6\u01bd\3\2\2\2\b\u01c1\3\2\2\2\n\u01c9\3\2\2")
        buf.write(u"\2\f\u01e5\3\2\2\2\16\u01ed\3\2\2\2\20\u0203\3\2\2\2")
        buf.write(u"\22\u0210\3\2\2\2\24\u0212\3\2\2\2\26\u0221\3\2\2\2\30")
        buf.write(u"\u022b\3\2\2\2\32\u0238\3\2\2\2\34\u0242\3\2\2\2\36\u0250")
        buf.write(u"\3\2\2\2 \u0265\3\2\2\2\"\u0279\3\2\2\2$\u0281\3\2\2")
        buf.write(u"\2&\u028d\3\2\2\2(\u0299\3\2\2\2*\u02a9\3\2\2\2,\u02bc")
        buf.write(u"\3\2\2\2.\u02cf\3\2\2\2\60\u02d1\3\2\2\2\62\u02f1\3\2")
        buf.write(u"\2\2\64\u02f3\3\2\2\2\66\u030b\3\2\2\28\u030d\3\2\2\2")
        buf.write(u":\u0319\3\2\2\2<\u031b\3\2\2\2>\u032b\3\2\2\2@\u032d")
        buf.write(u"\3\2\2\2B\u0334\3\2\2\2D\u033b\3\2\2\2F\u035b\3\2\2\2")
        buf.write(u"H\u035d\3\2\2\2J\u036a\3\2\2\2L\u0373\3\2\2\2N\u037a")
        buf.write(u"\3\2\2\2P\u038e\3\2\2\2R\u03a6\3\2\2\2T\u03a9\3\2\2\2")
        buf.write(u"V\u03da\3\2\2\2X\u03dc\3\2\2\2Z\u03de\3\2\2\2\\\u03f4")
        buf.write(u"\3\2\2\2^\u0468\3\2\2\2`\u046a\3\2\2\2b\u047c\3\2\2\2")
        buf.write(u"d\u048b\3\2\2\2f\u048d\3\2\2\2h\u0494\3\2\2\2j\u04ab")
        buf.write(u"\3\2\2\2l\u04ad\3\2\2\2n\u04b7\3\2\2\2p\u04c1\3\2\2\2")
        buf.write(u"r\u04c7\3\2\2\2t\u04cc\3\2\2\2v\u04f0\3\2\2\2x\u04f2")
        buf.write(u"\3\2\2\2z\u0501\3\2\2\2|\u050d\3\2\2\2~\u050f\3\2\2\2")
        buf.write(u"\u0080\u0516\3\2\2\2\u0082\u051a\3\2\2\2\u0084\u051f")
        buf.write(u"\3\2\2\2\u0086\u0528\3\2\2\2\u0088\u052d\3\2\2\2\u008a")
        buf.write(u"\u0530\3\2\2\2\u008c\u0535\3\2\2\2\u008e\u0543\3\2\2")
        buf.write(u"\2\u0090\u054d\3\2\2\2\u0092\u0551\3\2\2\2\u0094\u0553")
        buf.write(u"\3\2\2\2\u0096\u055c\3\2\2\2\u0098\u0565\3\2\2\2\u009a")
        buf.write(u"\u0577\3\2\2\2\u009c\u057a\3\2\2\2\u009e\u0583\3\2\2")
        buf.write(u"\2\u00a0\u058b\3\2\2\2\u00a2\u0593\3\2\2\2\u00a4\u05a5")
        buf.write(u"\3\2\2\2\u00a6\u05b6\3\2\2\2\u00a8\u05c7\3\2\2\2\u00aa")
        buf.write(u"\u05c9\3\2\2\2\u00ac\u05cc\3\2\2\2\u00ae\u05d0\3\2\2")
        buf.write(u"\2\u00b0\u05d5\3\2\2\2\u00b2\u05d7\3\2\2\2\u00b4\u05e1")
        buf.write(u"\3\2\2\2\u00b6\u05e6\3\2\2\2\u00b8\u05e8\3\2\2\2\u00ba")
        buf.write(u"\u05ea\3\2\2\2\u00bc\u05ec\3\2\2\2\u00be\u05ee\3\2\2")
        buf.write(u"\2\u00c0\u05f0\3\2\2\2\u00c2\u05fd\3\2\2\2\u00c4\u0601")
        buf.write(u"\3\2\2\2\u00c6\u0603\3\2\2\2\u00c8\u0608\3\2\2\2\u00ca")
        buf.write(u"\u060d\3\2\2\2\u00cc\u060f\3\2\2\2\u00ce\u061d\3\2\2")
        buf.write(u"\2\u00d0\u062b\3\2\2\2\u00d2\u062d\3\2\2\2\u00d4\u0639")
        buf.write(u"\3\2\2\2\u00d6\u0645\3\2\2\2\u00d8\u0647\3\2\2\2\u00da")
        buf.write(u"\u064b\3\2\2\2\u00dc\u0656\3\2\2\2\u00de\u065a\3\2\2")
        buf.write(u"\2\u00e0\u066c\3\2\2\2\u00e2\u0674\3\2\2\2\u00e4\u0680")
        buf.write(u"\3\2\2\2\u00e6\u0682\3\2\2\2\u00e8\u0684\3\2\2\2\u00ea")
        buf.write(u"\u0697\3\2\2\2\u00ec\u0699\3\2\2\2\u00ee\u06a0\3\2\2")
        buf.write(u"\2\u00f0\u06a7\3\2\2\2\u00f2\u06b0\3\2\2\2\u00f4\u06b9")
        buf.write(u"\3\2\2\2\u00f6\u06c2\3\2\2\2\u00f8\u06d9\3\2\2\2\u00fa")
        buf.write(u"\u06ea\3\2\2\2\u00fc\u06ec\3\2\2\2\u00fe\u06f8\3\2\2")
        buf.write(u"\2\u0100\u06fa\3\2\2\2\u0102\u06fc\3\2\2\2\u0104\u0702")
        buf.write(u"\3\2\2\2\u0106\u0709\3\2\2\2\u0108\u070c\3\2\2\2\u010a")
        buf.write(u"\u0715\3\2\2\2\u010c\u071d\3\2\2\2\u010e\u0729\3\2\2")
        buf.write(u"\2\u0110\u0731\3\2\2\2\u0112\u073e\3\2\2\2\u0114\u0740")
        buf.write(u"\3\2\2\2\u0116\u0744\3\2\2\2\u0118\u0752\3\2\2\2\u011a")
        buf.write(u"\u0754\3\2\2\2\u011c\u0759\3\2\2\2\u011e\u075e\3\2\2")
        buf.write(u"\2\u0120\u0766\3\2\2\2\u0122\u0777\3\2\2\2\u0124\u0779")
        buf.write(u"\3\2\2\2\u0126\u077c\3\2\2\2\u0128\u077f\3\2\2\2\u012a")
        buf.write(u"\u0782\3\2\2\2\u012c\u0785\3\2\2\2\u012e\u0788\3\2\2")
        buf.write(u"\2\u0130\u078a\3\2\2\2\u0132\u078c\3\2\2\2\u0134\u078e")
        buf.write(u"\3\2\2\2\u0136\u0790\3\2\2\2\u0138\u0799\3\2\2\2\u013a")
        buf.write(u"\u079b\3\2\2\2\u013c\u07ac\3\2\2\2\u013e\u07ae\3\2\2")
        buf.write(u"\2\u0140\u07b0\3\2\2\2\u0142\u07b8\3\2\2\2\u0144\u07ba")
        buf.write(u"\3\2\2\2\u0146\u07c1\3\2\2\2\u0148\u07cc\3\2\2\2\u014a")
        buf.write(u"\u07d0\3\2\2\2\u014c\u07d4\3\2\2\2\u014e\u07db\3\2\2")
        buf.write(u"\2\u0150\u07dd\3\2\2\2\u0152\u07e2\3\2\2\2\u0154\u07e4")
        buf.write(u"\3\2\2\2\u0156\u07f3\3\2\2\2\u0158\u07f5\3\2\2\2\u015a")
        buf.write(u"\u07fd\3\2\2\2\u015c\u07ff\3\2\2\2\u015e\u080c\3\2\2")
        buf.write(u"\2\u0160\u080e\3\2\2\2\u0162\u0819\3\2\2\2\u0164\u0829")
        buf.write(u"\3\2\2\2\u0166\u0830\3\2\2\2\u0168\u083f\3\2\2\2\u016a")
        buf.write(u"\u0841\3\2\2\2\u016c\u084a\3\2\2\2\u016e\u084c\3\2\2")
        buf.write(u"\2\u0170\u085b\3\2\2\2\u0172\u085d\3\2\2\2\u0174\u085f")
        buf.write(u"\3\2\2\2\u0176\u0865\3\2\2\2\u0178\u0867\3\2\2\2\u017a")
        buf.write(u"\u086e\3\2\2\2\u017c\u0879\3\2\2\2\u017e\u087d\3\2\2")
        buf.write(u"\2\u0180\u0881\3\2\2\2\u0182\u088c\3\2\2\2\u0184\u089b")
        buf.write(u"\3\2\2\2\u0186\u089d\3\2\2\2\u0188\u08a6\3\2\2\2\u018a")
        buf.write(u"\u08a8\3\2\2\2\u018c\u08b7\3\2\2\2\u018e\u08b9\3\2\2")
        buf.write(u"\2\u0190\u08bb\3\2\2\2\u0192\u08c1\3\2\2\2\u0194\u08c3")
        buf.write(u"\3\2\2\2\u0196\u08ca\3\2\2\2\u0198\u08d5\3\2\2\2\u019a")
        buf.write(u"\u08d9\3\2\2\2\u019c\u08e0\3\2\2\2\u019e\u08ef\3\2\2")
        buf.write(u"\2\u01a0\u08f1\3\2\2\2\u01a2\u01a3\7b\2\2\u01a3\u01a4")
        buf.write(u"\5\u00bc_\2\u01a4\u01ab\7\26\2\2\u01a5\u01a8\5\u00bc")
        buf.write(u"_\2\u01a6\u01a7\7\23\2\2\u01a7\u01a9\5\u00e2r\2\u01a8")
        buf.write(u"\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac\3\2\2")
        buf.write(u"\2\u01aa\u01ac\5\u00e2r\2\u01ab\u01a5\3\2\2\2\u01ab\u01aa")
        buf.write(u"\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\7\27\2\2\u01ae")
        buf.write(u"\u01af\7\21\2\2\u01af\u01b0\5\u0084C\2\u01b0\u01b1\5")
        buf.write(u"\u0096L\2\u01b1\u01b2\5\u0086D\2\u01b2\3\3\2\2\2\u01b3")
        buf.write(u"\u01b4\7b\2\2\u01b4\u01b5\5\u00bc_\2\u01b5\u01b6\7\26")
        buf.write(u"\2\2\u01b6\u01b7\5\u00a8U\2\u01b7\u01b8\7\27\2\2\u01b8")
        buf.write(u"\u01b9\7\21\2\2\u01b9\u01ba\5\u0084C\2\u01ba\u01bb\5")
        buf.write(u"\u0094K\2\u01bb\u01bc\5\u0086D\2\u01bc\5\3\2\2\2\u01bd")
        buf.write(u"\u01be\5\u00be`\2\u01be\u01bf\7-\2\2\u01bf\u01c0\5\\")
        buf.write(u"/\2\u01c0\7\3\2\2\2\u01c1\u01c2\5\u00be`\2\u01c2\u01c4")
        buf.write(u"\7\26\2\2\u01c3\u01c5\5n8\2\u01c4\u01c3\3\2\2\2\u01c4")
        buf.write(u"\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\7\27\2")
        buf.write(u"\2\u01c7\t\3\2\2\2\u01c8\u01ca\7\u0092\2\2\u01c9\u01c8")
        buf.write(u"\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write(u"\u01cc\7M\2\2\u01cc\u01cd\5\u00ba^\2\u01cd\u01ce\7\26")
        buf.write(u"\2\2\u01ce\u01cf\5\u00a4S\2\u01cf\u01d0\7\27\2\2\u01d0")
        buf.write(u"\u01d1\7\21\2\2\u01d1\u01e1\5\u0084C\2\u01d2\u01e2\7")
        buf.write(u"\u0086\2\2\u01d3\u01d7\5\u009aN\2\u01d4\u01d5\5\u0082")
        buf.write(u"B\2\u01d5\u01d6\5\f\7\2\u01d6\u01d8\3\2\2\2\u01d7\u01d4")
        buf.write(u"\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01e0\3\2\2\2\u01d9")
        buf.write(u"\u01dd\5\f\7\2\u01da\u01db\5\u0082B\2\u01db\u01dc\5\u009a")
        buf.write(u"N\2\u01dc\u01de\3\2\2\2\u01dd\u01da\3\2\2\2\u01dd\u01de")
        buf.write(u"\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01d3\3\2\2\2\u01df")
        buf.write(u"\u01d9\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01d2\3\2\2")
        buf.write(u"\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4")
        buf.write(u"\5\u0086D\2\u01e4\13\3\2\2\2\u01e5\u01e6\7r\2\2\u01e6")
        buf.write(u"\u01e8\7\26\2\2\u01e7\u01e9\5\u00e0q\2\u01e8\u01e7\3")
        buf.write(u"\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write(u"\u01eb\7\27\2\2\u01eb\r\3\2\2\2\u01ec\u01ee\7\u0092\2")
        buf.write(u"\2\u01ed\u01ec\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef")
        buf.write(u"\3\2\2\2\u01ef\u01f0\t\2\2\2\u01f0\u01f1\5\u00bc_\2\u01f1")
        buf.write(u"\u01f8\7\26\2\2\u01f2\u01f9\5\22\n\2\u01f3\u01f9\5\u00e2")
        buf.write(u"r\2\u01f4\u01f5\5\22\n\2\u01f5\u01f6\7\23\2\2\u01f6\u01f7")
        buf.write(u"\5\u00e2r\2\u01f7\u01f9\3\2\2\2\u01f8\u01f2\3\2\2\2\u01f8")
        buf.write(u"\u01f3\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f9\u01fa\3\2\2")
        buf.write(u"\2\u01fa\u01fb\7\27\2\2\u01fb\u01fc\7\21\2\2\u01fc\u01ff")
        buf.write(u"\5\u0084C\2\u01fd\u0200\5\u00ceh\2\u01fe\u0200\7\u0086")
        buf.write(u"\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200\u0201")
        buf.write(u"\3\2\2\2\u0201\u0202\5\u0086D\2\u0202\17\3\2\2\2\u0203")
        buf.write(u"\u0204\7\u0090\2\2\u0204\u0205\5\u00bc_\2\u0205\u0206")
        buf.write(u"\7\26\2\2\u0206\u0207\5\u00e2r\2\u0207\u0208\7\27\2\2")
        buf.write(u"\u0208\u0209\7\21\2\2\u0209\u020c\5\u0084C\2\u020a\u020d")
        buf.write(u"\5\u00ceh\2\u020b\u020d\7\u0086\2\2\u020c\u020a\3\2\2")
        buf.write(u"\2\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f")
        buf.write(u"\5\u0086D\2\u020f\21\3\2\2\2\u0210\u0211\5\u00b2Z\2\u0211")
        buf.write(u"\23\3\2\2\2\u0212\u0213\7Y\2\2\u0213\u0214\7\u0082\2")
        buf.write(u"\2\u0214\u0215\5\u0122\u0092\2\u0215\u0216\7\26\2\2\u0216")
        buf.write(u"\u0217\5\u00c4c\2\u0217\u021a\7\27\2\2\u0218\u0219\7")
        buf.write(u"\63\2\2\u0219\u021b\5\u00a4S\2\u021a\u0218\3\2\2\2\u021a")
        buf.write(u"\u021b\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021d\7\21\2")
        buf.write(u"\2\u021d\u021e\5\u0084C\2\u021e\u021f\5\u00f0y\2\u021f")
        buf.write(u"\u0220\5\u0086D\2\u0220\25\3\2\2\2\u0221\u0222\7Y\2\2")
        buf.write(u"\u0222\u0223\5\u00b8]\2\u0223\u0224\7\u008f\2\2\u0224")
        buf.write(u"\u0225\7\26\2\2\u0225\u0226\7\27\2\2\u0226\u0227\7\21")
        buf.write(u"\2\2\u0227\u0228\5\u0084C\2\u0228\u0229\5\u00f0y\2\u0229")
        buf.write(u"\u022a\5\u0086D\2\u022a\27\3\2\2\2\u022b\u022c\7Y\2\2")
        buf.write(u"\u022c\u022e\5\u00b8]\2\u022d\u022f\7z\2\2\u022e\u022d")
        buf.write(u"\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write(u"\u0231\7\u008f\2\2\u0231\u0232\7\26\2\2\u0232\u0233\7")
        buf.write(u"\27\2\2\u0233\u0234\7\21\2\2\u0234\u0235\5\u0084C\2\u0235")
        buf.write(u"\u0236\5\u00e8u\2\u0236\u0237\5\u0086D\2\u0237\31\3\2")
        buf.write(u"\2\2\u0238\u0239\7Y\2\2\u0239\u023a\5\u00b8]\2\u023a")
        buf.write(u"\u023b\7n\2\2\u023b\u023c\7\26\2\2\u023c\u023d\7\27\2")
        buf.write(u"\2\u023d\u023e\7\21\2\2\u023e\u023f\5\u0084C\2\u023f")
        buf.write(u"\u0240\5\u00f0y\2\u0240\u0241\5\u0086D\2\u0241\33\3\2")
        buf.write(u"\2\2\u0242\u0243\7Y\2\2\u0243\u0245\5\u00b8]\2\u0244")
        buf.write(u"\u0246\7z\2\2\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2\2")
        buf.write(u"\u0246\u0247\3\2\2\2\u0247\u0248\7n\2\2\u0248\u0249\7")
        buf.write(u"\26\2\2\u0249\u024a\7\27\2\2\u024a\u024b\7\21\2\2\u024b")
        buf.write(u"\u024c\5\u0084C\2\u024c\u024d\5\u00e8u\2\u024d\u024e")
        buf.write(u"\5\u0086D\2\u024e\35\3\2\2\2\u024f\u0251\7\u0092\2\2")
        buf.write(u"\u0250\u024f\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252")
        buf.write(u"\3\2\2\2\u0252\u0253\7z\2\2\u0253\u0254\t\2\2\2\u0254")
        buf.write(u"\u0255\5\u00bc_\2\u0255\u0257\7\26\2\2\u0256\u0258\5")
        buf.write(u"\u00e2r\2\u0257\u0256\3\2\2\2\u0257\u0258\3\2\2\2\u0258")
        buf.write(u"\u0259\3\2\2\2\u0259\u025a\7\27\2\2\u025a\u025b\7\21")
        buf.write(u"\2\2\u025b\u025c\5\u0084C\2\u025c\u0260\5\"\22\2\u025d")
        buf.write(u"\u025e\5\u0082B\2\u025e\u025f\5\u00d2j\2\u025f\u0261")
        buf.write(u"\3\2\2\2\u0260\u025d\3\2\2\2\u0260\u0261\3\2\2\2\u0261")
        buf.write(u"\u0262\3\2\2\2\u0262\u0263\5\u0086D\2\u0263\37\3\2\2")
        buf.write(u"\2\u0264\u0266\7\u0092\2\2\u0265\u0264\3\2\2\2\u0265")
        buf.write(u"\u0266\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268\7z\2\2")
        buf.write(u"\u0268\u0269\7\u008a\2\2\u0269\u026a\5\u00bc_\2\u026a")
        buf.write(u"\u026c\7\26\2\2\u026b\u026d\5\u00e2r\2\u026c\u026b\3")
        buf.write(u"\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write(u"\u026f\7\27\2\2\u026f\u0270\7\21\2\2\u0270\u0271\5\u0084")
        buf.write(u"C\2\u0271\u0275\5\"\22\2\u0272\u0273\5\u0082B\2\u0273")
        buf.write(u"\u0274\5\u00d2j\2\u0274\u0276\3\2\2\2\u0275\u0272\3\2")
        buf.write(u"\2\2\u0275\u0276\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278")
        buf.write(u"\5\u0086D\2\u0278!\3\2\2\2\u0279\u027a\7Y\2\2\u027a\u027b")
        buf.write(u"\t\2\2\2\u027b\u027c\7P\2\2\u027c\u027d\7\21\2\2\u027d")
        buf.write(u"\u027e\5\u0084C\2\u027e\u027f\5$\23\2\u027f\u0280\5\u0086")
        buf.write(u"D\2\u0280#\3\2\2\2\u0281\u0282\b\23\1\2\u0282\u0283\5")
        buf.write(u"\u00d6l\2\u0283\u028a\3\2\2\2\u0284\u0285\f\3\2\2\u0285")
        buf.write(u"\u0286\5\u0082B\2\u0286\u0287\5\u00d6l\2\u0287\u0289")
        buf.write(u"\3\2\2\2\u0288\u0284\3\2\2\2\u0289\u028c\3\2\2\2\u028a")
        buf.write(u"\u0288\3\2\2\2\u028a\u028b\3\2\2\2\u028b%\3\2\2\2\u028c")
        buf.write(u"\u028a\3\2\2\2\u028d\u028e\7F\2\2\u028e\u028f\7Y\2\2")
        buf.write(u"\u028f\u0290\5\u00b4[\2\u0290\u0292\7\26\2\2\u0291\u0293")
        buf.write(u"\5\u00c0a\2\u0292\u0291\3\2\2\2\u0292\u0293\3\2\2\2\u0293")
        buf.write(u"\u0294\3\2\2\2\u0294\u0297\7\27\2\2\u0295\u0296\7\63")
        buf.write(u"\2\2\u0296\u0298\5\u00a4S\2\u0297\u0295\3\2\2\2\u0297")
        buf.write(u"\u0298\3\2\2\2\u0298\'\3\2\2\2\u0299\u029a\7Y\2\2\u029a")
        buf.write(u"\u029b\5\u00b4[\2\u029b\u029d\7\26\2\2\u029c\u029e\5")
        buf.write(u"\u00c0a\2\u029d\u029c\3\2\2\2\u029d\u029e\3\2\2\2\u029e")
        buf.write(u"\u029f\3\2\2\2\u029f\u02a2\7\27\2\2\u02a0\u02a1\7\63")
        buf.write(u"\2\2\u02a1\u02a3\5\u00a4S\2\u02a2\u02a0\3\2\2\2\u02a2")
        buf.write(u"\u02a3\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a5\7\21\2")
        buf.write(u"\2\u02a5\u02a6\5\u0084C\2\u02a6\u02a7\5\u00f0y\2\u02a7")
        buf.write(u"\u02a8\5\u0086D\2\u02a8)\3\2\2\2\u02a9\u02ab\7Y\2\2\u02aa")
        buf.write(u"\u02ac\7z\2\2\u02ab\u02aa\3\2\2\2\u02ab\u02ac\3\2\2\2")
        buf.write(u"\u02ac\u02ad\3\2\2\2\u02ad\u02ae\5\u00b4[\2\u02ae\u02b0")
        buf.write(u"\7\26\2\2\u02af\u02b1\5\u00c0a\2\u02b0\u02af\3\2\2\2")
        buf.write(u"\u02b0\u02b1\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b5")
        buf.write(u"\7\27\2\2\u02b3\u02b4\7\63\2\2\u02b4\u02b6\5\u00caf\2")
        buf.write(u"\u02b5\u02b3\3\2\2\2\u02b5\u02b6\3\2\2\2\u02b6\u02b7")
        buf.write(u"\3\2\2\2\u02b7\u02b8\7\21\2\2\u02b8\u02b9\5\u0084C\2")
        buf.write(u"\u02b9\u02ba\5\u00e8u\2\u02ba\u02bb\5\u0086D\2\u02bb")
        buf.write(u"+\3\2\2\2\u02bc\u02bd\7Y\2\2\u02bd\u02be\7\u0095\2\2")
        buf.write(u"\u02be\u02bf\7\u00a9\2\2\u02bf\u02c0\7\26\2\2\u02c0\u02c1")
        buf.write(u"\7\27\2\2\u02c1\u02c2\7\21\2\2\u02c2\u02c3\5\u0084C\2")
        buf.write(u"\u02c3\u02c4\5\u00f0y\2\u02c4\u02c5\5\u0086D\2\u02c5")
        buf.write(u"\u02c6\5\u0082B\2\u02c6\u02c7\7\u009a\2\2\u02c7\u02cd")
        buf.write(u"\7\21\2\2\u02c8\u02c9\5\u0084C\2\u02c9\u02ca\5\u00f2")
        buf.write(u"z\2\u02ca\u02cb\5\u0086D\2\u02cb\u02ce\3\2\2\2\u02cc")
        buf.write(u"\u02ce\5\u00be`\2\u02cd\u02c8\3\2\2\2\u02cd\u02cc\3\2")
        buf.write(u"\2\2\u02ce-\3\2\2\2\u02cf\u02d0\5\\/\2\u02d0/\3\2\2\2")
        buf.write(u"\u02d1\u02d2\5\u00b8]\2\u02d2\u02d3\7\21\2\2\u02d3\u02d8")
        buf.write(u"\5\u00caf\2\u02d4\u02d5\7\26\2\2\u02d5\u02d6\5\u00e2")
        buf.write(u"r\2\u02d6\u02d7\7\27\2\2\u02d7\u02d9\3\2\2\2\u02d8\u02d4")
        buf.write(u"\3\2\2\2\u02d8\u02d9\3\2\2\2\u02d9\u02dc\3\2\2\2\u02da")
        buf.write(u"\u02db\7-\2\2\u02db\u02dd\5\u0104\u0083\2\u02dc\u02da")
        buf.write(u"\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\61\3\2\2\2\u02de\u02f2")
        buf.write(u"\58\35\2\u02df\u02f2\5z>\2\u02e0\u02f2\5~@\2\u02e1\u02f2")
        buf.write(u"\5\66\34\2\u02e2\u02f2\5\64\33\2\u02e3\u02f2\5X-\2\u02e4")
        buf.write(u"\u02f2\5Z.\2\u02e5\u02f2\5N(\2\u02e6\u02f2\5D#\2\u02e7")
        buf.write(u"\u02f2\5H%\2\u02e8\u02f2\5L\'\2\u02e9\u02f2\5J&\2\u02ea")
        buf.write(u"\u02f2\5R*\2\u02eb\u02f2\5T+\2\u02ec\u02f2\5r:\2\u02ed")
        buf.write(u"\u02f2\5@!\2\u02ee\u02f2\5B\"\2\u02ef\u02f2\5(\25\2\u02f0")
        buf.write(u"\u02f2\5\u00e6t\2\u02f1\u02de\3\2\2\2\u02f1\u02df\3\2")
        buf.write(u"\2\2\u02f1\u02e0\3\2\2\2\u02f1\u02e1\3\2\2\2\u02f1\u02e2")
        buf.write(u"\3\2\2\2\u02f1\u02e3\3\2\2\2\u02f1\u02e4\3\2\2\2\u02f1")
        buf.write(u"\u02e5\3\2\2\2\u02f1\u02e6\3\2\2\2\u02f1\u02e7\3\2\2")
        buf.write(u"\2\u02f1\u02e8\3\2\2\2\u02f1\u02e9\3\2\2\2\u02f1\u02ea")
        buf.write(u"\3\2\2\2\u02f1\u02eb\3\2\2\2\u02f1\u02ec\3\2\2\2\u02f1")
        buf.write(u"\u02ed\3\2\2\2\u02f1\u02ee\3\2\2\2\u02f1\u02ef\3\2\2")
        buf.write(u"\2\u02f1\u02f0\3\2\2\2\u02f2\63\3\2\2\2\u02f3\u02f4\7")
        buf.write(u"k\2\2\u02f4\u02f5\7\26\2\2\u02f5\u02f6\7\27\2\2\u02f6")
        buf.write(u"\65\3\2\2\2\u02f7\u02f8\7\\\2\2\u02f8\u02f9\7\26\2\2")
        buf.write(u"\u02f9\u02fa\5\u00a0Q\2\u02fa\u02fb\7\27\2\2\u02fb\u030c")
        buf.write(u"\3\2\2\2\u02fc\u02fd\7\u0093\2\2\u02fd\u02fe\7\26\2\2")
        buf.write(u"\u02fe\u02ff\5\u00a0Q\2\u02ff\u0300\7\27\2\2\u0300\u030c")
        buf.write(u"\3\2\2\2\u0301\u0302\7\\\2\2\u0302\u0303\7\26\2\2\u0303")
        buf.write(u"\u0304\5\u00a0Q\2\u0304\u0305\7\27\2\2\u0305\u0306\7")
        buf.write(u"I\2\2\u0306\u0307\7\u0093\2\2\u0307\u0308\7\26\2\2\u0308")
        buf.write(u"\u0309\5\u00a0Q\2\u0309\u030a\7\27\2\2\u030a\u030c\3")
        buf.write(u"\2\2\2\u030b\u02f7\3\2\2\2\u030b\u02fc\3\2\2\2\u030b")
        buf.write(u"\u0301\3\2\2\2\u030c\67\3\2\2\2\u030d\u030e\5:\36\2\u030e")
        buf.write(u"\u0310\7\26\2\2\u030f\u0311\5n8\2\u0310\u030f\3\2\2\2")
        buf.write(u"\u0310\u0311\3\2\2\2\u0311\u0312\3\2\2\2\u0312\u0313")
        buf.write(u"\7\27\2\2\u03139\3\2\2\2\u0314\u031a\5\u00b4[\2\u0315")
        buf.write(u"\u0316\5<\37\2\u0316\u0317\7\25\2\2\u0317\u0318\5\u00b4")
        buf.write(u"[\2\u0318\u031a\3\2\2\2\u0319\u0314\3\2\2\2\u0319\u0315")
        buf.write(u"\3\2\2\2\u031a;\3\2\2\2\u031b\u031c\b\37\1\2\u031c\u031d")
        buf.write(u"\5\u00b6\\\2\u031d\u0322\3\2\2\2\u031e\u031f\f\3\2\2")
        buf.write(u"\u031f\u0321\5> \2\u0320\u031e\3\2\2\2\u0321\u0324\3")
        buf.write(u"\2\2\2\u0322\u0320\3\2\2\2\u0322\u0323\3\2\2\2\u0323")
        buf.write(u"=\3\2\2\2\u0324\u0322\3\2\2\2\u0325\u0326\7\25\2\2\u0326")
        buf.write(u"\u032c\5\u00b8]\2\u0327\u0328\7\30\2\2\u0328\u0329\5")
        buf.write(u"\\/\2\u0329\u032a\7\31\2\2\u032a\u032c\3\2\2\2\u032b")
        buf.write(u"\u0325\3\2\2\2\u032b\u0327\3\2\2\2\u032c?\3\2\2\2\u032d")
        buf.write(u"\u032e\7\u009b\2\2\u032e\u032f\5\u0114\u008b\2\u032f")
        buf.write(u"\u0330\7\21\2\2\u0330\u0331\5\u0084C\2\u0331\u0332\5")
        buf.write(u"\u00f0y\2\u0332\u0333\5\u0086D\2\u0333A\3\2\2\2\u0334")
        buf.write(u"\u0335\7\u009b\2\2\u0335\u0336\5\u00bc_\2\u0336\u0337")
        buf.write(u"\7\21\2\2\u0337\u0338\5\u0084C\2\u0338\u0339\5\u00f0")
        buf.write(u"y\2\u0339\u033a\5\u0086D\2\u033aC\3\2\2\2\u033b\u033c")
        buf.write(u"\7\u0094\2\2\u033c\u033d\7\177\2\2\u033d\u033e\5\\/\2")
        buf.write(u"\u033e\u033f\7\21\2\2\u033f\u0340\5\u0084C\2\u0340\u0348")
        buf.write(u"\5\u00f4{\2\u0341\u0342\5\u0082B\2\u0342\u0343\7\u0085")
        buf.write(u"\2\2\u0343\u0344\7\21\2\2\u0344\u0345\5\u0084C\2\u0345")
        buf.write(u"\u0346\5\u00f0y\2\u0346\u0347\5\u0086D\2\u0347\u0349")
        buf.write(u"\3\2\2\2\u0348\u0341\3\2\2\2\u0348\u0349\3\2\2\2\u0349")
        buf.write(u"\u034a\3\2\2\2\u034a\u034b\5\u0086D\2\u034bE\3\2\2\2")
        buf.write(u"\u034c\u034d\7\u009c\2\2\u034d\u034e\5\u00fa~\2\u034e")
        buf.write(u"\u034f\7\21\2\2\u034f\u0350\5\u0084C\2\u0350\u0351\5")
        buf.write(u"\u00f0y\2\u0351\u0352\5\u0086D\2\u0352\u035c\3\2\2\2")
        buf.write(u"\u0353\u0354\7\u009c\2\2\u0354\u0355\7q\2\2\u0355\u0356")
        buf.write(u"\5\u00f8}\2\u0356\u0357\7\21\2\2\u0357\u0358\5\u0084")
        buf.write(u"C\2\u0358\u0359\5\u00f0y\2\u0359\u035a\5\u0086D\2\u035a")
        buf.write(u"\u035c\3\2\2\2\u035b\u034c\3\2\2\2\u035b\u0353\3\2\2")
        buf.write(u"\2\u035cG\3\2\2\2\u035d\u035e\7l\2\2\u035e\u0361\5\u00b8")
        buf.write(u"]\2\u035f\u0360\7\23\2\2\u0360\u0362\5\u00b8]\2\u0361")
        buf.write(u"\u035f\3\2\2\2\u0361\u0362\3\2\2\2\u0362\u0363\3\2\2")
        buf.write(u"\2\u0363\u0364\7q\2\2\u0364\u0365\5\\/\2\u0365\u0366")
        buf.write(u"\7\21\2\2\u0366\u0367\5\u0084C\2\u0367\u0368\5\u00f0")
        buf.write(u"y\2\u0368\u0369\5\u0086D\2\u0369I\3\2\2\2\u036a\u036b")
        buf.write(u"\7^\2\2\u036b\u036c\7\21\2\2\u036c\u036d\5\u0084C\2\u036d")
        buf.write(u"\u036e\5\u00f0y\2\u036e\u036f\5\u0086D\2\u036f\u0370")
        buf.write(u"\5\u0082B\2\u0370\u0371\7\u009e\2\2\u0371\u0372\5\\/")
        buf.write(u"\2\u0372K\3\2\2\2\u0373\u0374\7\u009e\2\2\u0374\u0375")
        buf.write(u"\5\\/\2\u0375\u0376\7\21\2\2\u0376\u0377\5\u0084C\2\u0377")
        buf.write(u"\u0378\5\u00f0y\2\u0378\u0379\5\u0086D\2\u0379M\3\2\2")
        buf.write(u"\2\u037a\u037b\7p\2\2\u037b\u037c\5\\/\2\u037c\u037d")
        buf.write(u"\7\21\2\2\u037d\u037e\5\u0084C\2\u037e\u037f\5\u00f0")
        buf.write(u"y\2\u037f\u0383\5\u0086D\2\u0380\u0381\5\u0082B\2\u0381")
        buf.write(u"\u0382\5P)\2\u0382\u0384\3\2\2\2\u0383\u0380\3\2\2\2")
        buf.write(u"\u0383\u0384\3\2\2\2\u0384\u038c\3\2\2\2\u0385\u0386")
        buf.write(u"\5\u0082B\2\u0386\u0387\7a\2\2\u0387\u0388\7\21\2\2\u0388")
        buf.write(u"\u0389\5\u0084C\2\u0389\u038a\5\u00f0y\2\u038a\u038b")
        buf.write(u"\5\u0086D\2\u038b\u038d\3\2\2\2\u038c\u0385\3\2\2\2\u038c")
        buf.write(u"\u038d\3\2\2\2\u038dO\3\2\2\2\u038e\u038f\b)\1\2\u038f")
        buf.write(u"\u0390\7a\2\2\u0390\u0391\7p\2\2\u0391\u0392\5\\/\2\u0392")
        buf.write(u"\u0393\7\21\2\2\u0393\u0394\5\u0084C\2\u0394\u0395\5")
        buf.write(u"\u00f0y\2\u0395\u0396\5\u0086D\2\u0396\u03a3\3\2\2\2")
        buf.write(u"\u0397\u0398\f\3\2\2\u0398\u0399\5\u0082B\2\u0399\u039a")
        buf.write(u"\7a\2\2\u039a\u039b\7p\2\2\u039b\u039c\5\\/\2\u039c\u039d")
        buf.write(u"\7\21\2\2\u039d\u039e\5\u0084C\2\u039e\u039f\5\u00f0")
        buf.write(u"y\2\u039f\u03a0\5\u0086D\2\u03a0\u03a2\3\2\2\2\u03a1")
        buf.write(u"\u0397\3\2\2\2\u03a2\u03a5\3\2\2\2\u03a3\u03a1\3\2\2")
        buf.write(u"\2\u03a3\u03a4\3\2\2\2\u03a4Q\3\2\2\2\u03a5\u03a3\3\2")
        buf.write(u"\2\2\u03a6\u03a7\7\u0087\2\2\u03a7\u03a8\5\\/\2\u03a8")
        buf.write(u"S\3\2\2\2\u03a9\u03aa\7\u0099\2\2\u03aa\u03ab\5\u00b8")
        buf.write(u"]\2\u03ab\u03ac\7\21\2\2\u03ac\u03ad\5\u0084C\2\u03ad")
        buf.write(u"\u03ae\5\u00f0y\2\u03ae\u03af\5\u0086D\2\u03af\u03b1")
        buf.write(u"\5\u0080A\2\u03b0\u03b2\5\u00f6|\2\u03b1\u03b0\3\2\2")
        buf.write(u"\2\u03b1\u03b2\3\2\2\2\u03b2\u03ba\3\2\2\2\u03b3\u03b4")
        buf.write(u"\7d\2\2\u03b4\u03b5\7\21\2\2\u03b5\u03b6\5\u0084C\2\u03b6")
        buf.write(u"\u03b7\5\u00f0y\2\u03b7\u03b8\5\u0086D\2\u03b8\u03b9")
        buf.write(u"\5\u0080A\2\u03b9\u03bb\3\2\2\2\u03ba\u03b3\3\2\2\2\u03ba")
        buf.write(u"\u03bb\3\2\2\2\u03bb\u03c3\3\2\2\2\u03bc\u03bd\7j\2\2")
        buf.write(u"\u03bd\u03be\7\21\2\2\u03be\u03bf\5\u0084C\2\u03bf\u03c0")
        buf.write(u"\5\u00f0y\2\u03c0\u03c1\5\u0086D\2\u03c1\u03c2\5\u0080")
        buf.write(u"A\2\u03c2\u03c4\3\2\2\2\u03c3\u03bc\3\2\2\2\u03c3\u03c4")
        buf.write(u"\3\2\2\2\u03c4\u03c5\3\2\2\2\u03c5\u03c6\5\u0080A\2\u03c6")
        buf.write(u"U\3\2\2\2\u03c7\u03c8\7d\2\2\u03c8\u03c9\5\u00be`\2\u03c9")
        buf.write(u"\u03ca\7\21\2\2\u03ca\u03cb\5\u0084C\2\u03cb\u03cc\5")
        buf.write(u"\u00f0y\2\u03cc\u03cd\5\u0086D\2\u03cd\u03ce\5\u0080")
        buf.write(u"A\2\u03ce\u03db\3\2\2\2\u03cf\u03d0\7d\2\2\u03d0\u03d1")
        buf.write(u"\7q\2\2\u03d1\u03d2\7\30\2\2\u03d2\u03d3\5\u0098M\2\u03d3")
        buf.write(u"\u03d4\7\31\2\2\u03d4\u03d5\7\21\2\2\u03d5\u03d6\5\u0084")
        buf.write(u"C\2\u03d6\u03d7\5\u00f0y\2\u03d7\u03d8\5\u0086D\2\u03d8")
        buf.write(u"\u03d9\5\u0080A\2\u03d9\u03db\3\2\2\2\u03da\u03c7\3\2")
        buf.write(u"\2\2\u03da\u03cf\3\2\2\2\u03dbW\3\2\2\2\u03dc\u03dd\7")
        buf.write(u"Q\2\2\u03ddY\3\2\2\2\u03de\u03e0\7\u008b\2\2\u03df\u03e1")
        buf.write(u"\5\\/\2\u03e0\u03df\3\2\2\2\u03e0\u03e1\3\2\2\2\u03e1")
        buf.write(u"[\3\2\2\2\u03e2\u03e3\b/\1\2\u03e3\u03f5\5`\61\2\u03e4")
        buf.write(u"\u03f5\5b\62\2\u03e5\u03e6\7#\2\2\u03e6\u03f5\5\\/$\u03e7")
        buf.write(u"\u03e8\7|\2\2\u03e8\u03f5\5\\/#\u03e9\u03ea\7?\2\2\u03ea")
        buf.write(u"\u03eb\7\26\2\2\u03eb\u03ec\5\\/\2\u03ec\u03ed\7\27\2")
        buf.write(u"\2\u03ed\u03f5\3\2\2\2\u03ee\u03ef\7e\2\2\u03ef\u03f0")
        buf.write(u"\7\26\2\2\u03f0\u03f1\5\u00b8]\2\u03f1\u03f2\7\27\2\2")
        buf.write(u"\u03f2\u03f5\3\2\2\2\u03f3\u03f5\5^\60\2\u03f4\u03e2")
        buf.write(u"\3\2\2\2\u03f4\u03e4\3\2\2\2\u03f4\u03e5\3\2\2\2\u03f4")
        buf.write(u"\u03e7\3\2\2\2\u03f4\u03e9\3\2\2\2\u03f4\u03ee\3\2\2")
        buf.write(u"\2\u03f4\u03f3\3\2\2\2\u03f5\u0465\3\2\2\2\u03f6\u03f7")
        buf.write(u"\f\"\2\2\u03f7\u03f8\5\u0130\u0099\2\u03f8\u03f9\5\\")
        buf.write(u"/#\u03f9\u0464\3\2\2\2\u03fa\u03fb\f!\2\2\u03fb\u03fc")
        buf.write(u"\5\u0132\u009a\2\u03fc\u03fd\5\\/\"\u03fd\u0464\3\2\2")
        buf.write(u"\2\u03fe\u03ff\f \2\2\u03ff\u0400\5\u0136\u009c\2\u0400")
        buf.write(u"\u0401\5\\/!\u0401\u0464\3\2\2\2\u0402\u0403\f\37\2\2")
        buf.write(u"\u0403\u0404\5\u0134\u009b\2\u0404\u0405\5\\/ \u0405")
        buf.write(u"\u0464\3\2\2\2\u0406\u0407\f\36\2\2\u0407\u0408\t\3\2")
        buf.write(u"\2\u0408\u0464\5\\/\37\u0409\u040a\f\34\2\2\u040a\u040b")
        buf.write(u"\7*\2\2\u040b\u0464\5\\/\35\u040c\u040d\f\33\2\2\u040d")
        buf.write(u"\u040e\7+\2\2\u040e\u0464\5\\/\34\u040f\u0410\f\32\2")
        buf.write(u"\2\u0410\u0411\7(\2\2\u0411\u0464\5\\/\33\u0412\u0413")
        buf.write(u"\f\31\2\2\u0413\u0414\7)\2\2\u0414\u0464\5\\/\32\u0415")
        buf.write(u"\u0416\f\26\2\2\u0416\u0417\7/\2\2\u0417\u0464\5\\/\27")
        buf.write(u"\u0418\u0419\f\25\2\2\u0419\u041a\7.\2\2\u041a\u0464")
        buf.write(u"\5\\/\26\u041b\u041c\f\24\2\2\u041c\u041d\7\60\2\2\u041d")
        buf.write(u"\u0464\5\\/\25\u041e\u041f\f\23\2\2\u041f\u0420\7X\2")
        buf.write(u"\2\u0420\u0464\5\\/\24\u0421\u0422\f\22\2\2\u0422\u0423")
        buf.write(u"\7q\2\2\u0423\u0464\5\\/\23\u0424\u0425\f\21\2\2\u0425")
        buf.write(u"\u0426\7o\2\2\u0426\u0464\5\\/\22\u0427\u0428\f\20\2")
        buf.write(u"\2\u0428\u0429\7o\2\2\u0429\u042a\7G\2\2\u042a\u0464")
        buf.write(u"\5\\/\21\u042b\u042c\f\17\2\2\u042c\u042d\7o\2\2\u042d")
        buf.write(u"\u042e\7J\2\2\u042e\u0464\5\\/\20\u042f\u0430\f\16\2")
        buf.write(u"\2\u0430\u0431\7|\2\2\u0431\u0432\7X\2\2\u0432\u0464")
        buf.write(u"\5\\/\17\u0433\u0434\f\r\2\2\u0434\u0435\7|\2\2\u0435")
        buf.write(u"\u0436\7q\2\2\u0436\u0464\5\\/\16\u0437\u0438\f\f\2\2")
        buf.write(u"\u0438\u0439\7|\2\2\u0439\u043a\7o\2\2\u043a\u0464\5")
        buf.write(u"\\/\r\u043b\u043c\f\13\2\2\u043c\u043d\7|\2\2\u043d\u043e")
        buf.write(u"\7o\2\2\u043e\u043f\7G\2\2\u043f\u0464\5\\/\f\u0440\u0441")
        buf.write(u"\f\n\2\2\u0441\u0442\7|\2\2\u0442\u0443\7o\2\2\u0443")
        buf.write(u"\u0444\7J\2\2\u0444\u0464\5\\/\13\u0445\u0446\f\t\2\2")
        buf.write(u"\u0446\u0447\7\u0083\2\2\u0447\u0464\5\\/\n\u0448\u0449")
        buf.write(u"\f\b\2\2\u0449\u044a\7I\2\2\u044a\u0464\5\\/\t\u044b")
        buf.write(u"\u044c\f\7\2\2\u044c\u044d\7p\2\2\u044d\u044e\5\\/\2")
        buf.write(u"\u044e\u044f\7a\2\2\u044f\u0450\5\\/\b\u0450\u0464\3")
        buf.write(u"\2\2\2\u0451\u0452\f\3\2\2\u0452\u0453\7l\2\2\u0453\u0454")
        buf.write(u"\5\u00b8]\2\u0454\u0455\7q\2\2\u0455\u0456\5\\/\4\u0456")
        buf.write(u"\u0464\3\2\2\2\u0457\u0458\f&\2\2\u0458\u0464\5t;\2\u0459")
        buf.write(u"\u045a\f\35\2\2\u045a\u045b\7K\2\2\u045b\u0464\5\u00ca")
        buf.write(u"f\2\u045c\u045d\f\30\2\2\u045d\u045e\7t\2\2\u045e\u045f")
        buf.write(u"\7|\2\2\u045f\u0464\5\u0118\u008d\2\u0460\u0461\f\27")
        buf.write(u"\2\2\u0461\u0462\7t\2\2\u0462\u0464\5\u0118\u008d\2\u0463")
        buf.write(u"\u03f6\3\2\2\2\u0463\u03fa\3\2\2\2\u0463\u03fe\3\2\2")
        buf.write(u"\2\u0463\u0402\3\2\2\2\u0463\u0406\3\2\2\2\u0463\u0409")
        buf.write(u"\3\2\2\2\u0463\u040c\3\2\2\2\u0463\u040f\3\2\2\2\u0463")
        buf.write(u"\u0412\3\2\2\2\u0463\u0415\3\2\2\2\u0463\u0418\3\2\2")
        buf.write(u"\2\u0463\u041b\3\2\2\2\u0463\u041e\3\2\2\2\u0463\u0421")
        buf.write(u"\3\2\2\2\u0463\u0424\3\2\2\2\u0463\u0427\3\2\2\2\u0463")
        buf.write(u"\u042b\3\2\2\2\u0463\u042f\3\2\2\2\u0463\u0433\3\2\2")
        buf.write(u"\2\u0463\u0437\3\2\2\2\u0463\u043b\3\2\2\2\u0463\u0440")
        buf.write(u"\3\2\2\2\u0463\u0445\3\2\2\2\u0463\u0448\3\2\2\2\u0463")
        buf.write(u"\u044b\3\2\2\2\u0463\u0451\3\2\2\2\u0463\u0457\3\2\2")
        buf.write(u"\2\u0463\u0459\3\2\2\2\u0463\u045c\3\2\2\2\u0463\u0460")
        buf.write(u"\3\2\2\2\u0464\u0467\3\2\2\2\u0465\u0463\3\2\2\2\u0465")
        buf.write(u"\u0466\3\2\2\2\u0466]\3\2\2\2\u0467\u0465\3\2\2\2\u0468")
        buf.write(u"\u0469\5\u00bc_\2\u0469_\3\2\2\2\u046a\u046b\b\61\1\2")
        buf.write(u"\u046b\u046c\5\u00fe\u0080\2\u046c\u0471\3\2\2\2\u046d")
        buf.write(u"\u046e\f\3\2\2\u046e\u0470\5d\63\2\u046f\u046d\3\2\2")
        buf.write(u"\2\u0470\u0473\3\2\2\2\u0471\u046f\3\2\2\2\u0471\u0472")
        buf.write(u"\3\2\2\2\u0472a\3\2\2\2\u0473\u0471\3\2\2\2\u0474\u047d")
        buf.write(u"\5f\64\2\u0475\u047d\5h\65\2\u0476\u047d\5v<\2\u0477")
        buf.write(u"\u047d\5\u011a\u008e\2\u0478\u047d\5\u011c\u008f\2\u0479")
        buf.write(u"\u047d\5x=\2\u047a\u047d\58\35\2\u047b\u047d\5j\66\2")
        buf.write(u"\u047c\u0474\3\2\2\2\u047c\u0475\3\2\2\2\u047c\u0476")
        buf.write(u"\3\2\2\2\u047c\u0477\3\2\2\2\u047c\u0478\3\2\2\2\u047c")
        buf.write(u"\u0479\3\2\2\2\u047c\u047a\3\2\2\2\u047c\u047b\3\2\2")
        buf.write(u"\2\u047dc\3\2\2\2\u047e\u047f\6\63$\3\u047f\u0480\7\25")
        buf.write(u"\2\2\u0480\u048c\5\u00b8]\2\u0481\u0482\6\63%\3\u0482")
        buf.write(u"\u0483\7\30\2\2\u0483\u0484\5\u0112\u008a\2\u0484\u0485")
        buf.write(u"\7\31\2\2\u0485\u048c\3\2\2\2\u0486\u0487\6\63&\3\u0487")
        buf.write(u"\u0488\7\30\2\2\u0488\u0489\5\\/\2\u0489\u048a\7\31\2")
        buf.write(u"\2\u048a\u048c\3\2\2\2\u048b\u047e\3\2\2\2\u048b\u0481")
        buf.write(u"\3\2\2\2\u048b\u0486\3\2\2\2\u048ce\3\2\2\2\u048d\u048e")
        buf.write(u"\7A\2\2\u048e\u0490\7\26\2\2\u048f\u0491\5\\/\2\u0490")
        buf.write(u"\u048f\3\2\2\2\u0490\u0491\3\2\2\2\u0491\u0492\3\2\2")
        buf.write(u"\2\u0492\u0493\7\27\2\2\u0493g\3\2\2\2\u0494\u0495\7")
        buf.write(u"@\2\2\u0495\u0497\7\26\2\2\u0496\u0498\5\\/\2\u0497\u0496")
        buf.write(u"\3\2\2\2\u0497\u0498\3\2\2\2\u0498\u0499\3\2\2\2\u0499")
        buf.write(u"\u049a\7\27\2\2\u049ai\3\2\2\2\u049b\u049c\5\u00acW\2")
        buf.write(u"\u049c\u049d\7\26\2\2\u049d\u04a0\5l\67\2\u049e\u049f")
        buf.write(u"\7\23\2\2\u049f\u04a1\5n8\2\u04a0\u049e\3\2\2\2\u04a0")
        buf.write(u"\u04a1\3\2\2\2\u04a1\u04a2\3\2\2\2\u04a2\u04a3\7\27\2")
        buf.write(u"\2\u04a3\u04ac\3\2\2\2\u04a4\u04a5\5\u00acW\2\u04a5\u04a7")
        buf.write(u"\7\26\2\2\u04a6\u04a8\5n8\2\u04a7\u04a6\3\2\2\2\u04a7")
        buf.write(u"\u04a8\3\2\2\2\u04a8\u04a9\3\2\2\2\u04a9\u04aa\7\27\2")
        buf.write(u"\2\u04aa\u04ac\3\2\2\2\u04ab\u049b\3\2\2\2\u04ab\u04a4")
        buf.write(u"\3\2\2\2\u04ack\3\2\2\2\u04ad\u04ae\7m\2\2\u04ae\u04af")
        buf.write(u"\5\u012e\u0098\2\u04af\u04b0\5\\/\2\u04b0\u04b1\6\67")
        buf.write(u"\'\3\u04b1m\3\2\2\2\u04b2\u04b3\b8\1\2\u04b3\u04b4\5")
        buf.write(u"\\/\2\u04b4\u04b5\68(\3\u04b5\u04b8\3\2\2\2\u04b6\u04b8")
        buf.write(u"\5p9\2\u04b7\u04b2\3\2\2\2\u04b7\u04b6\3\2\2\2\u04b8")
        buf.write(u"\u04be\3\2\2\2\u04b9\u04ba\f\3\2\2\u04ba\u04bb\7\23\2")
        buf.write(u"\2\u04bb\u04bd\5p9\2\u04bc\u04b9\3\2\2\2\u04bd\u04c0")
        buf.write(u"\3\2\2\2\u04be\u04bc\3\2\2\2\u04be\u04bf\3\2\2\2\u04bf")
        buf.write(u"o\3\2\2\2\u04c0\u04be\3\2\2\2\u04c1\u04c5\5\u00b8]\2")
        buf.write(u"\u04c2\u04c3\5\u012e\u0098\2\u04c3\u04c4\5\\/\2\u04c4")
        buf.write(u"\u04c6\3\2\2\2\u04c5\u04c2\3\2\2\2\u04c5\u04c6\3\2\2")
        buf.write(u"\2\u04c6q\3\2\2\2\u04c7\u04c8\7\u009f\2\2\u04c8\u04c9")
        buf.write(u"\5\\/\2\u04c9\u04ca\7\u0098\2\2\u04ca\u04cb\5\\/\2\u04cb")
        buf.write(u"s\3\2\2\2\u04cc\u04cd\7i\2\2\u04cd\u04ce\7\u009b\2\2")
        buf.write(u"\u04ce\u04cf\5\u00b8]\2\u04cf\u04d0\7\u009d\2\2\u04d0")
        buf.write(u"\u04d1\5\\/\2\u04d1u\3\2\2\2\u04d2\u04d3\7h\2\2\u04d3")
        buf.write(u"\u04d5\7\u0080\2\2\u04d4\u04d6\5\u00acW\2\u04d5\u04d4")
        buf.write(u"\3\2\2\2\u04d5\u04d6\3\2\2\2\u04d6\u04d7\3\2\2\2\u04d7")
        buf.write(u"\u04d8\7\u009d\2\2\u04d8\u04f1\5\\/\2\u04d9\u04e0\7h")
        buf.write(u"\2\2\u04da\u04e1\7G\2\2\u04db\u04dc\7\u008d\2\2\u04dc")
        buf.write(u"\u04dd\5\\/\2\u04dd\u04de\7\u0098\2\2\u04de\u04df\5\\")
        buf.write(u"/\2\u04df\u04e1\3\2\2\2\u04e0\u04da\3\2\2\2\u04e0\u04db")
        buf.write(u"\3\2\2\2\u04e1\u04e2\3\2\2\2\u04e2\u04e4\7\26\2\2\u04e3")
        buf.write(u"\u04e5\5\u00acW\2\u04e4\u04e3\3\2\2\2\u04e4\u04e5\3\2")
        buf.write(u"\2\2\u04e5\u04e6\3\2\2\2\u04e6\u04e9\7\27\2\2\u04e7\u04e8")
        buf.write(u"\7\u009d\2\2\u04e8\u04ea\5\\/\2\u04e9\u04e7\3\2\2\2\u04e9")
        buf.write(u"\u04ea\3\2\2\2\u04ea\u04ee\3\2\2\2\u04eb\u04ec\7\u0084")
        buf.write(u"\2\2\u04ec\u04ed\7R\2\2\u04ed\u04ef\5\u011e\u0090\2\u04ee")
        buf.write(u"\u04eb\3\2\2\2\u04ee\u04ef\3\2\2\2\u04ef\u04f1\3\2\2")
        buf.write(u"\2\u04f0\u04d2\3\2\2\2\u04f0\u04d9\3\2\2\2\u04f1w\3\2")
        buf.write(u"\2\2\u04f2\u04f4\7\u0091\2\2\u04f3\u04f5\7]\2\2\u04f4")
        buf.write(u"\u04f3\3\2\2\2\u04f4\u04f5\3\2\2\2\u04f5\u04f6\3\2\2")
        buf.write(u"\2\u04f6\u04f7\7\26\2\2\u04f7\u04fd\5`\61\2\u04f8\u04f9")
        buf.write(u"\7\23\2\2\u04f9\u04fa\5\u0126\u0094\2\u04fa\u04fb\7-")
        buf.write(u"\2\2\u04fb\u04fc\5`\61\2\u04fc\u04fe\3\2\2\2\u04fd\u04f8")
        buf.write(u"\3\2\2\2\u04fd\u04fe\3\2\2\2\u04fe\u04ff\3\2\2\2\u04ff")
        buf.write(u"\u0500\7\27\2\2\u0500y\3\2\2\2\u0501\u0502\5\u0116\u008c")
        buf.write(u"\2\u0502\u0503\5\u012e\u0098\2\u0503\u0504\5\\/\2\u0504")
        buf.write(u"{\3\2\2\2\u0505\u0506\6?*\3\u0506\u0507\7\25\2\2\u0507")
        buf.write(u"\u050e\5\u00b8]\2\u0508\u0509\6?+\3\u0509\u050a\7\30")
        buf.write(u"\2\2\u050a\u050b\5\\/\2\u050b\u050c\7\31\2\2\u050c\u050e")
        buf.write(u"\3\2\2\2\u050d\u0505\3\2\2\2\u050d\u0508\3\2\2\2\u050e")
        buf.write(u"}\3\2\2\2\u050f\u0510\5\u00e0q\2\u0510\u0511\5\u012e")
        buf.write(u"\u0098\2\u0511\u0512\5\\/\2\u0512\177\3\2\2\2\u0513\u0515")
        buf.write(u"\7\7\2\2\u0514\u0513\3\2\2\2\u0515\u0518\3\2\2\2\u0516")
        buf.write(u"\u0514\3\2\2\2\u0516\u0517\3\2\2\2\u0517\u0081\3\2\2")
        buf.write(u"\2\u0518\u0516\3\2\2\2\u0519\u051b\7\7\2\2\u051a\u0519")
        buf.write(u"\3\2\2\2\u051b\u051c\3\2\2\2\u051c\u051a\3\2\2\2\u051c")
        buf.write(u"\u051d\3\2\2\2\u051d\u0083\3\2\2\2\u051e\u0520\7\7\2")
        buf.write(u"\2\u051f\u051e\3\2\2\2\u0520\u0521\3\2\2\2\u0521\u051f")
        buf.write(u"\3\2\2\2\u0521\u0522\3\2\2\2\u0522\u0523\3\2\2\2\u0523")
        buf.write(u"\u0524\7\3\2\2\u0524\u0085\3\2\2\2\u0525\u0527\7\7\2")
        buf.write(u"\2\u0526\u0525\3\2\2\2\u0527\u052a\3\2\2\2\u0528\u0526")
        buf.write(u"\3\2\2\2\u0528\u0529\3\2\2\2\u0529\u052b\3\2\2\2\u052a")
        buf.write(u"\u0528\3\2\2\2\u052b\u052c\7\4\2\2\u052c\u0087\3\2\2")
        buf.write(u"\2\u052d\u052e\7{\2\2\u052e\u0089\3\2\2\2\u052f\u0531")
        buf.write(u"\5\u008cG\2\u0530\u052f\3\2\2\2\u0530\u0531\3\2\2\2\u0531")
        buf.write(u"\u0532\3\2\2\2\u0532\u0533\5\u0080A\2\u0533\u0534\7\2")
        buf.write(u"\2\3\u0534\u008b\3\2\2\2\u0535\u053b\5\u008eH\2\u0536")
        buf.write(u"\u0537\5\u0082B\2\u0537\u0538\5\u008eH\2\u0538\u053a")
        buf.write(u"\3\2\2\2\u0539\u0536\3\2\2\2\u053a\u053d\3\2\2\2\u053b")
        buf.write(u"\u0539\3\2\2\2\u053b\u053c\3\2\2\2\u053c\u008d\3\2\2")
        buf.write(u"\2\u053d\u053b\3\2\2\2\u053e\u053f\5\u00e6t\2\u053f\u0540")
        buf.write(u"\5\u0082B\2\u0540\u0542\3\2\2\2\u0541\u053e\3\2\2\2\u0542")
        buf.write(u"\u0545\3\2\2\2\u0543\u0541\3\2\2\2\u0543\u0544\3\2\2")
        buf.write(u"\2\u0544\u054b\3\2\2\2\u0545\u0543\3\2\2\2\u0546\u054c")
        buf.write(u"\5\n\6\2\u0547\u054c\5\u00b0Y\2\u0548\u054c\5\u0090I")
        buf.write(u"\2\u0549\u054c\5\u0092J\2\u054a\u054c\5\u00e4s\2\u054b")
        buf.write(u"\u0546\3\2\2\2\u054b\u0547\3\2\2\2\u054b\u0548\3\2\2")
        buf.write(u"\2\u054b\u0549\3\2\2\2\u054b\u054a\3\2\2\2\u054c\u008f")
        buf.write(u"\3\2\2\2\u054d\u054e\5 \21\2\u054e\u0091\3\2\2\2\u054f")
        buf.write(u"\u0552\5\2\2\2\u0550\u0552\5\4\3\2\u0551\u054f\3\2\2")
        buf.write(u"\2\u0551\u0550\3\2\2\2\u0552\u0093\3\2\2\2\u0553\u0559")
        buf.write(u"\5\6\4\2\u0554\u0555\5\u0082B\2\u0555\u0556\5\6\4\2\u0556")
        buf.write(u"\u0558\3\2\2\2\u0557\u0554\3\2\2\2\u0558\u055b\3\2\2")
        buf.write(u"\2\u0559\u0557\3\2\2\2\u0559\u055a\3\2\2\2\u055a\u0095")
        buf.write(u"\3\2\2\2\u055b\u0559\3\2\2\2\u055c\u0562\5\b\5\2\u055d")
        buf.write(u"\u055e\5\u0082B\2\u055e\u055f\5\b\5\2\u055f\u0561\3\2")
        buf.write(u"\2\2\u0560\u055d\3\2\2\2\u0561\u0564\3\2\2\2\u0562\u0560")
        buf.write(u"\3\2\2\2\u0562\u0563\3\2\2\2\u0563\u0097\3\2\2\2\u0564")
        buf.write(u"\u0562\3\2\2\2\u0565\u056a\5\u00be`\2\u0566\u0567\7\23")
        buf.write(u"\2\2\u0567\u0569\5\u00be`\2\u0568\u0566\3\2\2\2\u0569")
        buf.write(u"\u056c\3\2\2\2\u056a\u0568\3\2\2\2\u056a\u056b\3\2\2")
        buf.write(u"\2\u056b\u0099\3\2\2\2\u056c\u056a\3\2\2\2\u056d\u056e")
        buf.write(u"\7q\2\2\u056e\u0578\5\u009cO\2\u056f\u0570\7q\2\2\u0570")
        buf.write(u"\u0578\5\u009eP\2\u0571\u0572\7q\2\2\u0572\u0578\5\u00a2")
        buf.write(u"R\2\u0573\u0574\7u\2\2\u0574\u0578\7\u00a9\2\2\u0575")
        buf.write(u"\u0576\7u\2\2\u0576\u0578\5\\/\2\u0577\u056d\3\2\2\2")
        buf.write(u"\u0577\u056f\3\2\2\2\u0577\u0571\3\2\2\2\u0577\u0573")
        buf.write(u"\3\2\2\2\u0577\u0575\3\2\2\2\u0578\u009b\3\2\2\2\u0579")
        buf.write(u"\u057b\7y\2\2\u057a\u0579\3\2\2\2\u057a\u057b\3\2\2\2")
        buf.write(u"\u057b\u057c\3\2\2\2\u057c\u057e\7\30\2\2\u057d\u057f")
        buf.write(u"\5\u00a0Q\2\u057e\u057d\3\2\2\2\u057e\u057f\3\2\2\2\u057f")
        buf.write(u"\u0580\3\2\2\2\u0580\u0581\7\31\2\2\u0581\u009d\3\2\2")
        buf.write(u"\2\u0582\u0584\7y\2\2\u0583\u0582\3\2\2\2\u0583\u0584")
        buf.write(u"\3\2\2\2\u0584\u0585\3\2\2\2\u0585\u0587\7*\2\2\u0586")
        buf.write(u"\u0588\5\u00a0Q\2\u0587\u0586\3\2\2\2\u0587\u0588\3\2")
        buf.write(u"\2\2\u0588\u0589\3\2\2\2\u0589\u058a\7(\2\2\u058a\u009f")
        buf.write(u"\3\2\2\2\u058b\u0590\5\\/\2\u058c\u058d\7\23\2\2\u058d")
        buf.write(u"\u058f\5\\/\2\u058e\u058c\3\2\2\2\u058f\u0592\3\2\2\2")
        buf.write(u"\u0590\u058e\3\2\2\2\u0590\u0591\3\2\2\2\u0591\u00a1")
        buf.write(u"\3\2\2\2\u0592\u0590\3\2\2\2\u0593\u0594\7\30\2\2\u0594")
        buf.write(u"\u0595\5\\/\2\u0595\u0596\7\24\2\2\u0596\u0597\5\\/\2")
        buf.write(u"\u0597\u0598\7\31\2\2\u0598\u00a3\3\2\2\2\u0599\u059a")
        buf.write(u"\bS\1\2\u059a\u05a6\5\u00a6T\2\u059b\u059c\7E\2\2\u059c")
        buf.write(u"\u059d\7*\2\2\u059d\u059e\5\u00a4S\2\u059e\u059f\7(\2")
        buf.write(u"\2\u059f\u05a6\3\2\2\2\u05a0\u05a1\7D\2\2\u05a1\u05a2")
        buf.write(u"\7*\2\2\u05a2\u05a3\5\u00a4S\2\u05a3\u05a4\7(\2\2\u05a4")
        buf.write(u"\u05a6\3\2\2\2\u05a5\u0599\3\2\2\2\u05a5\u059b\3\2\2")
        buf.write(u"\2\u05a5\u05a0\3\2\2\2\u05a6\u05b1\3\2\2\2\u05a7\u05a8")
        buf.write(u"\f\7\2\2\u05a8\u05b0\7,\2\2\u05a9\u05aa\f\6\2\2\u05aa")
        buf.write(u"\u05ab\7\30\2\2\u05ab\u05b0\7\31\2\2\u05ac\u05ad\f\5")
        buf.write(u"\2\2\u05ad\u05ae\7\32\2\2\u05ae\u05b0\7\33\2\2\u05af")
        buf.write(u"\u05a7\3\2\2\2\u05af\u05a9\3\2\2\2\u05af\u05ac\3\2\2")
        buf.write(u"\2\u05b0\u05b3\3\2\2\2\u05b1\u05af\3\2\2\2\u05b1\u05b2")
        buf.write(u"\3\2\2\2\u05b2\u00a5\3\2\2\2\u05b3\u05b1\3\2\2\2\u05b4")
        buf.write(u"\u05b7\5\u00a8U\2\u05b5\u05b7\5\u00aaV\2\u05b6\u05b4")
        buf.write(u"\3\2\2\2\u05b6\u05b5\3\2\2\2\u05b7\u00a7\3\2\2\2\u05b8")
        buf.write(u"\u05c8\7\64\2\2\u05b9\u05c8\7\65\2\2\u05ba\u05c8\7\66")
        buf.write(u"\2\2\u05bb\u05c8\7B\2\2\u05bc\u05c8\7\67\2\2\u05bd\u05c8")
        buf.write(u"\78\2\2\u05be\u05c8\7@\2\2\u05bf\u05c8\79\2\2\u05c0\u05c8")
        buf.write(u"\7;\2\2\u05c1\u05c8\7:\2\2\u05c2\u05c8\7<\2\2\u05c3\u05c8")
        buf.write(u"\7=\2\2\u05c4\u05c8\7?\2\2\u05c5\u05c8\7A\2\2\u05c6\u05c8")
        buf.write(u"\7C\2\2\u05c7\u05b8\3\2\2\2\u05c7\u05b9\3\2\2\2\u05c7")
        buf.write(u"\u05ba\3\2\2\2\u05c7\u05bb\3\2\2\2\u05c7\u05bc\3\2\2")
        buf.write(u"\2\u05c7\u05bd\3\2\2\2\u05c7\u05be\3\2\2\2\u05c7\u05bf")
        buf.write(u"\3\2\2\2\u05c7\u05c0\3\2\2\2\u05c7\u05c1\3\2\2\2\u05c7")
        buf.write(u"\u05c2\3\2\2\2\u05c7\u05c3\3\2\2\2\u05c7\u05c4\3\2\2")
        buf.write(u"\2\u05c7\u05c5\3\2\2\2\u05c7\u05c6\3\2\2\2\u05c8\u00a9")
        buf.write(u"\3\2\2\2\u05c9\u05ca\7\u00a5\2\2\u05ca\u00ab\3\2\2\2")
        buf.write(u"\u05cb\u05cd\7y\2\2\u05cc\u05cb\3\2\2\2\u05cc\u05cd\3")
        buf.write(u"\2\2\2\u05cd\u05ce\3\2\2\2\u05ce\u05cf\5\u00aaV\2\u05cf")
        buf.write(u"\u00ad\3\2\2\2\u05d0\u05d1\7?\2\2\u05d1\u00af\3\2\2\2")
        buf.write(u"\u05d2\u05d6\5\16\b\2\u05d3\u05d6\5\36\20\2\u05d4\u05d6")
        buf.write(u"\5\20\t\2\u05d5\u05d2\3\2\2\2\u05d5\u05d3\3\2\2\2\u05d5")
        buf.write(u"\u05d4\3\2\2\2\u05d6\u00b1\3\2\2\2\u05d7\u05dc\5\u00bc")
        buf.write(u"_\2\u05d8\u05d9\7\23\2\2\u05d9\u05db\5\u00bc_\2\u05da")
        buf.write(u"\u05d8\3\2\2\2\u05db\u05de\3\2\2\2\u05dc\u05da\3\2\2")
        buf.write(u"\2\u05dc\u05dd\3\2\2\2\u05dd\u00b3\3\2\2\2\u05de\u05dc")
        buf.write(u"\3\2\2\2\u05df\u05e2\5\u00b8]\2\u05e0\u05e2\5\u00bc_")
        buf.write(u"\2\u05e1\u05df\3\2\2\2\u05e1\u05e0\3\2\2\2\u05e2\u00b5")
        buf.write(u"\3\2\2\2\u05e3\u05e7\5\u00b8]\2\u05e4\u05e7\5\u00bc_")
        buf.write(u"\2\u05e5\u05e7\5\u00be`\2\u05e6\u05e3\3\2\2\2\u05e6\u05e4")
        buf.write(u"\3\2\2\2\u05e6\u05e5\3\2\2\2\u05e7\u00b7\3\2\2\2\u05e8")
        buf.write(u"\u05e9\7\u00a6\2\2\u05e9\u00b9\3\2\2\2\u05ea\u05eb\t")
        buf.write(u"\4\2\2\u05eb\u00bb\3\2\2\2\u05ec\u05ed\7\u00a5\2\2\u05ed")
        buf.write(u"\u00bd\3\2\2\2\u05ee\u05ef\7\u00a4\2\2\u05ef\u00bf\3")
        buf.write(u"\2\2\2\u05f0\u05f5\5\u00c2b\2\u05f1\u05f2\7\23\2\2\u05f2")
        buf.write(u"\u05f4\5\u00c2b\2\u05f3\u05f1\3\2\2\2\u05f4\u05f7\3\2")
        buf.write(u"\2\2\u05f5\u05f3\3\2\2\2\u05f5\u05f6\3\2\2\2\u05f6\u00c1")
        buf.write(u"\3\2\2\2\u05f7\u05f5\3\2\2\2\u05f8\u05fe\5\u00c8e\2\u05f9")
        buf.write(u"\u05fb\7y\2\2\u05fa\u05f9\3\2\2\2\u05fa\u05fb\3\2\2\2")
        buf.write(u"\u05fb\u05fc\3\2\2\2\u05fc\u05fe\5\u00c4c\2\u05fd\u05f8")
        buf.write(u"\3\2\2\2\u05fd\u05fa\3\2\2\2\u05fe\u00c3\3\2\2\2\u05ff")
        buf.write(u"\u0602\5\u00c6d\2\u0600\u0602\5\60\31\2\u0601\u05ff\3")
        buf.write(u"\2\2\2\u0601\u0600\3\2\2\2\u0602\u00c5\3\2\2\2\u0603")
        buf.write(u"\u0606\5\u00b8]\2\u0604\u0605\7-\2\2\u0605\u0607\5\u0104")
        buf.write(u"\u0083\2\u0606\u0604\3\2\2\2\u0606\u0607\3\2\2\2\u0607")
        buf.write(u"\u00c7\3\2\2\2\u0608\u0609\5\u00aeX\2\u0609\u060a\5\u00b8")
        buf.write(u"]\2\u060a\u00c9\3\2\2\2\u060b\u060e\5\u00a4S\2\u060c")
        buf.write(u"\u060e\5\u00ccg\2\u060d\u060b\3\2\2\2\u060d\u060c\3\2")
        buf.write(u"\2\2\u060e\u00cb\3\2\2\2\u060f\u0610\bg\1\2\u0610\u0611")
        buf.write(u"\7J\2\2\u0611\u061a\3\2\2\2\u0612\u0613\f\4\2\2\u0613")
        buf.write(u"\u0614\7\30\2\2\u0614\u0619\7\31\2\2\u0615\u0616\f\3")
        buf.write(u"\2\2\u0616\u0617\7\32\2\2\u0617\u0619\7\33\2\2\u0618")
        buf.write(u"\u0612\3\2\2\2\u0618\u0615\3\2\2\2\u0619\u061c\3\2\2")
        buf.write(u"\2\u061a\u0618\3\2\2\2\u061a\u061b\3\2\2\2\u061b\u00cd")
        buf.write(u"\3\2\2\2\u061c\u061a\3\2\2\2\u061d\u0623\5\u00d0i\2\u061e")
        buf.write(u"\u061f\5\u0082B\2\u061f\u0620\5\u00d0i\2\u0620\u0622")
        buf.write(u"\3\2\2\2\u0621\u061e\3\2\2\2\u0622\u0625\3\2\2\2\u0623")
        buf.write(u"\u0621\3\2\2\2\u0623\u0624\3\2\2\2\u0624\u00cf\3\2\2")
        buf.write(u"\2\u0625\u0623\3\2\2\2\u0626\u062c\5\26\f\2\u0627\u062c")
        buf.write(u"\5\32\16\2\u0628\u062c\5(\25\2\u0629\u062c\5&\24\2\u062a")
        buf.write(u"\u062c\5\24\13\2\u062b\u0626\3\2\2\2\u062b\u0627\3\2")
        buf.write(u"\2\2\u062b\u0628\3\2\2\2\u062b\u0629\3\2\2\2\u062b\u062a")
        buf.write(u"\3\2\2\2\u062c\u00d1\3\2\2\2\u062d\u0633\5\u00d4k\2\u062e")
        buf.write(u"\u062f\5\u0082B\2\u062f\u0630\5\u00d4k\2\u0630\u0632")
        buf.write(u"\3\2\2\2\u0631\u062e\3\2\2\2\u0632\u0635\3\2\2\2\u0633")
        buf.write(u"\u0631\3\2\2\2\u0633\u0634\3\2\2\2\u0634\u00d3\3\2\2")
        buf.write(u"\2\u0635\u0633\3\2\2\2\u0636\u063a\5\34\17\2\u0637\u063a")
        buf.write(u"\5\30\r\2\u0638\u063a\5*\26\2\u0639\u0636\3\2\2\2\u0639")
        buf.write(u"\u0637\3\2\2\2\u0639\u0638\3\2\2\2\u063a\u00d5\3\2\2")
        buf.write(u"\2\u063b\u063c\7\13\2\2\u063c\u0646\5\u0182\u00c2\2\u063d")
        buf.write(u"\u063e\7\f\2\2\u063e\u0646\5\u019c\u00cf\2\u063f\u0640")
        buf.write(u"\7\r\2\2\u0640\u0646\5\u00d8m\2\u0641\u0642\7\16\2\2")
        buf.write(u"\u0642\u0646\5\u00d8m\2\u0643\u0644\7\17\2\2\u0644\u0646")
        buf.write(u"\5\u00dco\2\u0645\u063b\3\2\2\2\u0645\u063d\3\2\2\2\u0645")
        buf.write(u"\u063f\3\2\2\2\u0645\u0641\3\2\2\2\u0645\u0643\3\2\2")
        buf.write(u"\2\u0646\u00d7\3\2\2\2\u0647\u0649\5\u00b6\\\2\u0648")
        buf.write(u"\u064a\5\u00dan\2\u0649\u0648\3\2\2\2\u0649\u064a\3\2")
        buf.write(u"\2\2\u064a\u00d9\3\2\2\2\u064b\u064c\7m\2\2\u064c\u064d")
        buf.write(u"\5\u0128\u0095\2\u064d\u064e\7\21\2\2\u064e\u0653\5\u00b6")
        buf.write(u"\\\2\u064f\u0650\7\25\2\2\u0650\u0652\5\u00b6\\\2\u0651")
        buf.write(u"\u064f\3\2\2\2\u0652\u0655\3\2\2\2\u0653\u0651\3\2\2")
        buf.write(u"\2\u0653\u0654\3\2\2\2\u0654\u00db\3\2\2\2\u0655\u0653")
        buf.write(u"\3\2\2\2\u0656\u0658\5\u00b6\\\2\u0657\u0659\5\u00de")
        buf.write(u"p\2\u0658\u0657\3\2\2\2\u0658\u0659\3\2\2\2\u0659\u00dd")
        buf.write(u"\3\2\2\2\u065a\u065b\7m\2\2\u065b\u065c\5\u0128\u0095")
        buf.write(u"\2\u065c\u065e\7\21\2\2\u065d\u065f\7%\2\2\u065e\u065d")
        buf.write(u"\3\2\2\2\u065e\u065f\3\2\2\2\u065f\u0660\3\2\2\2\u0660")
        buf.write(u"\u0665\5\u0150\u00a9\2\u0661\u0662\7%\2\2\u0662\u0664")
        buf.write(u"\5\u0150\u00a9\2\u0663\u0661\3\2\2\2\u0664\u0667\3\2")
        buf.write(u"\2\2\u0665\u0663\3\2\2\2\u0665\u0666\3\2\2\2\u0666\u066a")
        buf.write(u"\3\2\2\2\u0667\u0665\3\2\2\2\u0668\u0669\7\25\2\2\u0669")
        buf.write(u"\u066b\5\u0150\u00a9\2\u066a\u0668\3\2\2\2\u066a\u066b")
        buf.write(u"\3\2\2\2\u066b\u00df\3\2\2\2\u066c\u0671\5\u00b8]\2\u066d")
        buf.write(u"\u066e\7\23\2\2\u066e\u0670\5\u00b8]\2\u066f\u066d\3")
        buf.write(u"\2\2\2\u0670\u0673\3\2\2\2\u0671\u066f\3\2\2\2\u0671")
        buf.write(u"\u0672\3\2\2\2\u0672\u00e1\3\2\2\2\u0673\u0671\3\2\2")
        buf.write(u"\2\u0674\u0679\5\u00ba^\2\u0675\u0676\7\23\2\2\u0676")
        buf.write(u"\u0678\5\u00ba^\2\u0677\u0675\3\2\2\2\u0678\u067b\3\2")
        buf.write(u"\2\2\u0679\u0677\3\2\2\2\u0679\u067a\3\2\2\2\u067a\u00e3")
        buf.write(u"\3\2\2\2\u067b\u0679\3\2\2\2\u067c\u0681\5&\24\2\u067d")
        buf.write(u"\u0681\5(\25\2\u067e\u0681\5*\26\2\u067f\u0681\5,\27")
        buf.write(u"\2\u0680\u067c\3\2\2\2\u0680\u067d\3\2\2\2\u0680\u067e")
        buf.write(u"\3\2\2\2\u0680\u067f\3\2\2\2\u0681\u00e5\3\2\2\2\u0682")
        buf.write(u"\u0683\7\n\2\2\u0683\u00e7\3\2\2\2\u0684\u068a\5\u00ea")
        buf.write(u"v\2\u0685\u0686\5\u0082B\2\u0686\u0687\5\u00eav\2\u0687")
        buf.write(u"\u0689\3\2\2\2\u0688\u0685\3\2\2\2\u0689\u068c\3\2\2")
        buf.write(u"\2\u068a\u0688\3\2\2\2\u068a\u068b\3\2\2\2\u068b\u00e9")
        buf.write(u"\3\2\2\2\u068c\u068a\3\2\2\2\u068d\u068e\7\13\2\2\u068e")
        buf.write(u"\u0698\5\u016c\u00b7\2\u068f\u0690\7\f\2\2\u0690\u0698")
        buf.write(u"\5\u0188\u00c5\2\u0691\u0692\7\r\2\2\u0692\u0698\5\u00ec")
        buf.write(u"w\2\u0693\u0694\7\16\2\2\u0694\u0698\5\u00ecw\2\u0695")
        buf.write(u"\u0696\7\17\2\2\u0696\u0698\5\u00eex\2\u0697\u068d\3")
        buf.write(u"\2\2\2\u0697\u068f\3\2\2\2\u0697\u0691\3\2\2\2\u0697")
        buf.write(u"\u0693\3\2\2\2\u0697\u0695\3\2\2\2\u0698\u00eb\3\2\2")
        buf.write(u"\2\u0699\u069b\5\u0152\u00aa\2\u069a\u069c\7\22\2\2\u069b")
        buf.write(u"\u069a\3\2\2\2\u069b\u069c\3\2\2\2\u069c\u069e\3\2\2")
        buf.write(u"\2\u069d\u069f\5\u00dan\2\u069e\u069d\3\2\2\2\u069e\u069f")
        buf.write(u"\3\2\2\2\u069f\u00ed\3\2\2\2\u06a0\u06a2\5\u0138\u009d")
        buf.write(u"\2\u06a1\u06a3\7\22\2\2\u06a2\u06a1\3\2\2\2\u06a2\u06a3")
        buf.write(u"\3\2\2\2\u06a3\u06a5\3\2\2\2\u06a4\u06a6\5\u00dep\2\u06a5")
        buf.write(u"\u06a4\3\2\2\2\u06a5\u06a6\3\2\2\2\u06a6\u00ef\3\2\2")
        buf.write(u"\2\u06a7\u06ad\5\62\32\2\u06a8\u06a9\5\u0082B\2\u06a9")
        buf.write(u"\u06aa\5\62\32\2\u06aa\u06ac\3\2\2\2\u06ab\u06a8\3\2")
        buf.write(u"\2\2\u06ac\u06af\3\2\2\2\u06ad\u06ab\3\2\2\2\u06ad\u06ae")
        buf.write(u"\3\2\2\2\u06ae\u00f1\3\2\2\2\u06af\u06ad\3\2\2\2\u06b0")
        buf.write(u"\u06b6\5.\30\2\u06b1\u06b2\5\u0082B\2\u06b2\u06b3\5.")
        buf.write(u"\30\2\u06b3\u06b5\3\2\2\2\u06b4\u06b1\3\2\2\2\u06b5\u06b8")
        buf.write(u"\3\2\2\2\u06b6\u06b4\3\2\2\2\u06b6\u06b7\3\2\2\2\u06b7")
        buf.write(u"\u00f3\3\2\2\2\u06b8\u06b6\3\2\2\2\u06b9\u06bf\5F$\2")
        buf.write(u"\u06ba\u06bb\5\u0082B\2\u06bb\u06bc\5F$\2\u06bc\u06be")
        buf.write(u"\3\2\2\2\u06bd\u06ba\3\2\2\2\u06be\u06c1\3\2\2\2\u06bf")
        buf.write(u"\u06bd\3\2\2\2\u06bf\u06c0\3\2\2\2\u06c0\u00f5\3\2\2")
        buf.write(u"\2\u06c1\u06bf\3\2\2\2\u06c2\u06c8\5V,\2\u06c3\u06c4")
        buf.write(u"\5\u0082B\2\u06c4\u06c5\5V,\2\u06c5\u06c7\3\2\2\2\u06c6")
        buf.write(u"\u06c3\3\2\2\2\u06c7\u06ca\3\2\2\2\u06c8\u06c6\3\2\2")
        buf.write(u"\2\u06c8\u06c9\3\2\2\2\u06c9\u00f7\3\2\2\2\u06ca\u06c8")
        buf.write(u"\3\2\2\2\u06cb\u06cc\7\30\2\2\u06cc\u06cd\5\u00fa~\2")
        buf.write(u"\u06cd\u06ce\7\24\2\2\u06ce\u06cf\5\u00fa~\2\u06cf\u06d0")
        buf.write(u"\7\31\2\2\u06d0\u06da\3\2\2\2\u06d1\u06d2\7\30\2\2\u06d2")
        buf.write(u"\u06d3\5\u00fc\177\2\u06d3\u06d4\7\31\2\2\u06d4\u06da")
        buf.write(u"\3\2\2\2\u06d5\u06d6\7*\2\2\u06d6\u06d7\5\u00fc\177\2")
        buf.write(u"\u06d7\u06d8\7(\2\2\u06d8\u06da\3\2\2\2\u06d9\u06cb\3")
        buf.write(u"\2\2\2\u06d9\u06d1\3\2\2\2\u06d9\u06d5\3\2\2\2\u06da")
        buf.write(u"\u00f9\3\2\2\2\u06db\u06eb\7\u00a2\2\2\u06dc\u06eb\7")
        buf.write(u"\u00a3\2\2\u06dd\u06eb\7\u00ab\2\2\u06de\u06eb\7\u00ac")
        buf.write(u"\2\2\u06df\u06eb\7\u00a1\2\2\u06e0\u06eb\7\u00b0\2\2")
        buf.write(u"\u06e1\u06eb\7\u00af\2\2\u06e2\u06eb\7\u00a9\2\2\u06e3")
        buf.write(u"\u06eb\7\u00ad\2\2\u06e4\u06eb\7\u00ae\2\2\u06e5\u06eb")
        buf.write(u"\7\u00a0\2\2\u06e6\u06eb\7\u00b1\2\2\u06e7\u06eb\7\u00b2")
        buf.write(u"\2\2\u06e8\u06eb\7\u00aa\2\2\u06e9\u06eb\5\u0088E\2\u06ea")
        buf.write(u"\u06db\3\2\2\2\u06ea\u06dc\3\2\2\2\u06ea\u06dd\3\2\2")
        buf.write(u"\2\u06ea\u06de\3\2\2\2\u06ea\u06df\3\2\2\2\u06ea\u06e0")
        buf.write(u"\3\2\2\2\u06ea\u06e1\3\2\2\2\u06ea\u06e2\3\2\2\2\u06ea")
        buf.write(u"\u06e3\3\2\2\2\u06ea\u06e4\3\2\2\2\u06ea\u06e5\3\2\2")
        buf.write(u"\2\u06ea\u06e6\3\2\2\2\u06ea\u06e7\3\2\2\2\u06ea\u06e8")
        buf.write(u"\3\2\2\2\u06ea\u06e9\3\2\2\2\u06eb\u00fb\3\2\2\2\u06ec")
        buf.write(u"\u06f1\5\u00fa~\2\u06ed\u06ee\7\23\2\2\u06ee\u06f0\5")
        buf.write(u"\u00fa~\2\u06ef\u06ed\3\2\2\2\u06f0\u06f3\3\2\2\2\u06f1")
        buf.write(u"\u06ef\3\2\2\2\u06f1\u06f2\3\2\2\2\u06f2\u00fd\3\2\2")
        buf.write(u"\2\u06f3\u06f1\3\2\2\2\u06f4\u06f9\5\u0102\u0082\2\u06f5")
        buf.write(u"\u06f9\5\u0104\u0083\2\u06f6\u06f9\5\u00b6\\\2\u06f7")
        buf.write(u"\u06f9\5\u0100\u0081\2\u06f8\u06f4\3\2\2\2\u06f8\u06f5")
        buf.write(u"\3\2\2\2\u06f8\u06f6\3\2\2\2\u06f8\u06f7\3\2\2\2\u06f9")
        buf.write(u"\u00ff\3\2\2\2\u06fa\u06fb\t\5\2\2\u06fb\u0101\3\2\2")
        buf.write(u"\2\u06fc\u06fd\7\26\2\2\u06fd\u06fe\5\\/\2\u06fe\u06ff")
        buf.write(u"\7\27\2\2\u06ff\u0103\3\2\2\2\u0700\u0703\5\u00fa~\2")
        buf.write(u"\u0701\u0703\5\u0106\u0084\2\u0702\u0700\3\2\2\2\u0702")
        buf.write(u"\u0701\3\2\2\2\u0703\u0105\3\2\2\2\u0704\u070a\5\u00a2")
        buf.write(u"R\2\u0705\u070a\5\u009cO\2\u0706\u070a\5\u009eP\2\u0707")
        buf.write(u"\u070a\5\u010a\u0086\2\u0708\u070a\5\u0108\u0085\2\u0709")
        buf.write(u"\u0704\3\2\2\2\u0709\u0705\3\2\2\2\u0709\u0706\3\2\2")
        buf.write(u"\2\u0709\u0707\3\2\2\2\u0709\u0708\3\2\2\2\u070a\u0107")
        buf.write(u"\3\2\2\2\u070b\u070d\7y\2\2\u070c\u070b\3\2\2\2\u070c")
        buf.write(u"\u070d\3\2\2\2\u070d\u070e\3\2\2\2\u070e\u0710\7\26\2")
        buf.write(u"\2\u070f\u0711\5\u010c\u0087\2\u0710\u070f\3\2\2\2\u0710")
        buf.write(u"\u0711\3\2\2\2\u0711\u0712\3\2\2\2\u0712\u0713\7\27\2")
        buf.write(u"\2\u0713\u0109\3\2\2\2\u0714\u0716\7y\2\2\u0715\u0714")
        buf.write(u"\3\2\2\2\u0715\u0716\3\2\2\2\u0716\u0717\3\2\2\2\u0717")
        buf.write(u"\u0719\7\32\2\2\u0718\u071a\5\u010e\u0088\2\u0719\u0718")
        buf.write(u"\3\2\2\2\u0719\u071a\3\2\2\2\u071a\u071b\3\2\2\2\u071b")
        buf.write(u"\u071c\7\33\2\2\u071c\u010b\3\2\2\2\u071d\u071e\5\\/")
        buf.write(u"\2\u071e\u0727\7\23\2\2\u071f\u0724\5\\/\2\u0720\u0721")
        buf.write(u"\7\23\2\2\u0721\u0723\5\\/\2\u0722\u0720\3\2\2\2\u0723")
        buf.write(u"\u0726\3\2\2\2\u0724\u0722\3\2\2\2\u0724\u0725\3\2\2")
        buf.write(u"\2\u0725\u0728\3\2\2\2\u0726\u0724\3\2\2\2\u0727\u071f")
        buf.write(u"\3\2\2\2\u0727\u0728\3\2\2\2\u0728\u010d\3\2\2\2\u0729")
        buf.write(u"\u072e\5\u0110\u0089\2\u072a\u072b\7\23\2\2\u072b\u072d")
        buf.write(u"\5\u0110\u0089\2\u072c\u072a\3\2\2\2\u072d\u0730\3\2")
        buf.write(u"\2\2\u072e\u072c\3\2\2\2\u072e\u072f\3\2\2\2\u072f\u010f")
        buf.write(u"\3\2\2\2\u0730\u072e\3\2\2\2\u0731\u0732\5\\/\2\u0732")
        buf.write(u"\u0733\7\21\2\2\u0733\u0734\5\\/\2\u0734\u0111\3\2\2")
        buf.write(u"\2\u0735\u0736\5\\/\2\u0736\u0737\7\21\2\2\u0737\u0738")
        buf.write(u"\5\\/\2\u0738\u073f\3\2\2\2\u0739\u073a\5\\/\2\u073a")
        buf.write(u"\u073b\7\21\2\2\u073b\u073f\3\2\2\2\u073c\u073d\7\21")
        buf.write(u"\2\2\u073d\u073f\5\\/\2\u073e\u0735\3\2\2\2\u073e\u0739")
        buf.write(u"\3\2\2\2\u073e\u073c\3\2\2\2\u073f\u0113\3\2\2\2\u0740")
        buf.write(u"\u0741\5\u00b8]\2\u0741\u0742\5\u012e\u0098\2\u0742\u0743")
        buf.write(u"\5\\/\2\u0743\u0115\3\2\2\2\u0744\u0745\b\u008c\1\2\u0745")
        buf.write(u"\u0746\5\u00b8]\2\u0746\u074b\3\2\2\2\u0747\u0748\f\3")
        buf.write(u"\2\2\u0748\u074a\5|?\2\u0749\u0747\3\2\2\2\u074a\u074d")
        buf.write(u"\3\2\2\2\u074b\u0749\3\2\2\2\u074b\u074c\3\2\2\2\u074c")
        buf.write(u"\u0117\3\2\2\2\u074d\u074b\3\2\2\2\u074e\u074f\6\u008d")
        buf.write(u"\62\3\u074f\u0750\7\u00a6\2\2\u0750\u0753\5\u00caf\2")
        buf.write(u"\u0751\u0753\5\\/\2\u0752\u074e\3\2\2\2\u0752\u0751\3")
        buf.write(u"\2\2\2\u0753\u0119\3\2\2\2\u0754\u0755\7\u0088\2\2\u0755")
        buf.write(u"\u0756\7G\2\2\u0756\u0757\7m\2\2\u0757\u0758\5\\/\2\u0758")
        buf.write(u"\u011b\3\2\2\2\u0759\u075a\7\u0088\2\2\u075a\u075b\7")
        buf.write(u"\u0080\2\2\u075b\u075c\7m\2\2\u075c\u075d\5\\/\2\u075d")
        buf.write(u"\u011d\3\2\2\2\u075e\u0763\5\u0120\u0091\2\u075f\u0760")
        buf.write(u"\7\23\2\2\u0760\u0762\5\u0120\u0091\2\u0761\u075f\3\2")
        buf.write(u"\2\2\u0762\u0765\3\2\2\2\u0763\u0761\3\2\2\2\u0763\u0764")
        buf.write(u"\3\2\2\2\u0764\u011f\3\2\2\2\u0765\u0763\3\2\2\2\u0766")
        buf.write(u"\u076b\5\u00b8]\2\u0767\u0768\7\25\2\2\u0768\u076a\5")
        buf.write(u"\u00b8]\2\u0769\u0767\3\2\2\2\u076a\u076d\3\2\2\2\u076b")
        buf.write(u"\u0769\3\2\2\2\u076b\u076c\3\2\2\2\u076c\u076f\3\2\2")
        buf.write(u"\2\u076d\u076b\3\2\2\2\u076e\u0770\t\6\2\2\u076f\u076e")
        buf.write(u"\3\2\2\2\u076f\u0770\3\2\2\2\u0770\u0121\3\2\2\2\u0771")
        buf.write(u"\u0778\7\"\2\2\u0772\u0778\7#\2\2\u0773\u0778\5\u0130")
        buf.write(u"\u0099\2\u0774\u0778\5\u0132\u009a\2\u0775\u0778\5\u0134")
        buf.write(u"\u009b\2\u0776\u0778\5\u0136\u009c\2\u0777\u0771\3\2")
        buf.write(u"\2\2\u0777\u0772\3\2\2\2\u0777\u0773\3\2\2\2\u0777\u0774")
        buf.write(u"\3\2\2\2\u0777\u0775\3\2\2\2\u0777\u0776\3\2\2\2\u0778")
        buf.write(u"\u0123\3\2\2\2\u0779\u077a\7\u00a6\2\2\u077a\u077b\6")
        buf.write(u"\u0093\63\3\u077b\u0125\3\2\2\2\u077c\u077d\7\u00a6\2")
        buf.write(u"\2\u077d\u077e\6\u0094\64\3\u077e\u0127\3\2\2\2\u077f")
        buf.write(u"\u0780\7\u00a6\2\2\u0780\u0781\6\u0095\65\3\u0781\u0129")
        buf.write(u"\3\2\2\2\u0782\u0783\7\u00a6\2\2\u0783\u0784\6\u0096")
        buf.write(u"\66\3\u0784\u012b\3\2\2\2\u0785\u0786\7\u00a6\2\2\u0786")
        buf.write(u"\u0787\6\u0097\67\3\u0787\u012d\3\2\2\2\u0788\u0789\7")
        buf.write(u"-\2\2\u0789\u012f\3\2\2\2\u078a\u078b\7$\2\2\u078b\u0131")
        buf.write(u"\3\2\2\2\u078c\u078d\7%\2\2\u078d\u0133\3\2\2\2\u078e")
        buf.write(u"\u078f\7&\2\2\u078f\u0135\3\2\2\2\u0790\u0791\t\7\2\2")
        buf.write(u"\u0791\u0137\3\2\2\2\u0792\u0793\7\u008b\2\2\u0793\u0794")
        buf.write(u"\5\u013a\u009e\2\u0794\u0795\7\22\2\2\u0795\u079a\3\2")
        buf.write(u"\2\2\u0796\u0797\5\u013a\u009e\2\u0797\u0798\7\22\2\2")
        buf.write(u"\u0798\u079a\3\2\2\2\u0799\u0792\3\2\2\2\u0799\u0796")
        buf.write(u"\3\2\2\2\u079a\u0139\3\2\2\2\u079b\u079c\b\u009e\1\2")
        buf.write(u"\u079c\u079d\5\u013c\u009f\2\u079d\u07a2\3\2\2\2\u079e")
        buf.write(u"\u079f\f\3\2\2\u079f\u07a1\5\u0142\u00a2\2\u07a0\u079e")
        buf.write(u"\3\2\2\2\u07a1\u07a4\3\2\2\2\u07a2\u07a0\3\2\2\2\u07a2")
        buf.write(u"\u07a3\3\2\2\2\u07a3\u013b\3\2\2\2\u07a4\u07a2\3\2\2")
        buf.write(u"\2\u07a5\u07ad\5\u013e\u00a0\2\u07a6\u07ad\5\u0140\u00a1")
        buf.write(u"\2\u07a7\u07ad\5\u014a\u00a6\2\u07a8\u07ad\5\u014c\u00a7")
        buf.write(u"\2\u07a9\u07ad\5\u014e\u00a8\2\u07aa\u07ad\5\u0144\u00a3")
        buf.write(u"\2\u07ab\u07ad\5\u0148\u00a5\2\u07ac\u07a5\3\2\2\2\u07ac")
        buf.write(u"\u07a6\3\2\2\2\u07ac\u07a7\3\2\2\2\u07ac\u07a8\3\2\2")
        buf.write(u"\2\u07ac\u07a9\3\2\2\2\u07ac\u07aa\3\2\2\2\u07ac\u07ab")
        buf.write(u"\3\2\2\2\u07ad\u013d\3\2\2\2\u07ae\u07af\5\u0100\u0081")
        buf.write(u"\2\u07af\u013f\3\2\2\2\u07b0\u07b1\5\u0124\u0093\2\u07b1")
        buf.write(u"\u07b2\5\u0144\u00a3\2\u07b2\u0141\3\2\2\2\u07b3\u07b4")
        buf.write(u"\7\25\2\2\u07b4\u07b9\5\u0144\u00a3\2\u07b5\u07b6\7\25")
        buf.write(u"\2\2\u07b6\u07b9\5\u0150\u00a9\2\u07b7\u07b9\5\u0148")
        buf.write(u"\u00a5\2\u07b8\u07b3\3\2\2\2\u07b8\u07b5\3\2\2\2\u07b8")
        buf.write(u"\u07b7\3\2\2\2\u07b9\u0143\3\2\2\2\u07ba\u07bb\5\u0150")
        buf.write(u"\u00a9\2\u07bb\u07bd\7\26\2\2\u07bc\u07be\5\u0146\u00a4")
        buf.write(u"\2\u07bd\u07bc\3\2\2\2\u07bd\u07be\3\2\2\2\u07be\u07bf")
        buf.write(u"\3\2\2\2\u07bf\u07c0\7\27\2\2\u07c0\u0145\3\2\2\2\u07c1")
        buf.write(u"\u07c2\b\u00a4\1\2\u07c2\u07c3\5\u013a\u009e\2\u07c3")
        buf.write(u"\u07c9\3\2\2\2\u07c4\u07c5\f\3\2\2\u07c5\u07c6\7\23\2")
        buf.write(u"\2\u07c6\u07c8\5\u013a\u009e\2\u07c7\u07c4\3\2\2\2\u07c8")
        buf.write(u"\u07cb\3\2\2\2\u07c9\u07c7\3\2\2\2\u07c9\u07ca\3\2\2")
        buf.write(u"\2\u07ca\u0147\3\2\2\2\u07cb\u07c9\3\2\2\2\u07cc\u07cd")
        buf.write(u"\7\30\2\2\u07cd\u07ce\5\u013a\u009e\2\u07ce\u07cf\7\31")
        buf.write(u"\2\2\u07cf\u0149\3\2\2\2\u07d0\u07d1\7\26\2\2\u07d1\u07d2")
        buf.write(u"\5\u013a\u009e\2\u07d2\u07d3\7\27\2\2\u07d3\u014b\3\2")
        buf.write(u"\2\2\u07d4\u07d5\5\u0150\u00a9\2\u07d5\u014d\3\2\2\2")
        buf.write(u"\u07d6\u07dc\7\u00ab\2\2\u07d7\u07dc\7\u00ad\2\2\u07d8")
        buf.write(u"\u07dc\7\u00a9\2\2\u07d9\u07dc\7\u00a0\2\2\u07da\u07dc")
        buf.write(u"\7\u00a1\2\2\u07db\u07d6\3\2\2\2\u07db\u07d7\3\2\2\2")
        buf.write(u"\u07db\u07d8\3\2\2\2\u07db\u07d9\3\2\2\2\u07db\u07da")
        buf.write(u"\3\2\2\2\u07dc\u014f\3\2\2\2\u07dd\u07de\t\b\2\2\u07de")
        buf.write(u"\u0151\3\2\2\2\u07df\u07e0\7\u008b\2\2\u07e0\u07e3\5")
        buf.write(u"\u0154\u00ab\2\u07e1\u07e3\5\u0154\u00ab\2\u07e2\u07df")
        buf.write(u"\3\2\2\2\u07e2\u07e1\3\2\2\2\u07e3\u0153\3\2\2\2\u07e4")
        buf.write(u"\u07e5\b\u00ab\1\2\u07e5\u07e6\5\u0156\u00ac\2\u07e6")
        buf.write(u"\u07eb\3\2\2\2\u07e7\u07e8\f\3\2\2\u07e8\u07ea\5\u015a")
        buf.write(u"\u00ae\2\u07e9\u07e7\3\2\2\2\u07ea\u07ed\3\2\2\2\u07eb")
        buf.write(u"\u07e9\3\2\2\2\u07eb\u07ec\3\2\2\2\u07ec\u0155\3\2\2")
        buf.write(u"\2\u07ed\u07eb\3\2\2\2\u07ee\u07f4\5\u0158\u00ad\2\u07ef")
        buf.write(u"\u07f4\5\u0164\u00b3\2\u07f0\u07f4\5\u0166\u00b4\2\u07f1")
        buf.write(u"\u07f4\5\u0168\u00b5\2\u07f2\u07f4\5\u015c\u00af\2\u07f3")
        buf.write(u"\u07ee\3\2\2\2\u07f3\u07ef\3\2\2\2\u07f3\u07f0\3\2\2")
        buf.write(u"\2\u07f3\u07f1\3\2\2\2\u07f3\u07f2\3\2\2\2\u07f4\u0157")
        buf.write(u"\3\2\2\2\u07f5\u07f6\5\u0100\u0081\2\u07f6\u0159\3\2")
        buf.write(u"\2\2\u07f7\u07f8\7\25\2\2\u07f8\u07fe\5\u015c\u00af\2")
        buf.write(u"\u07f9\u07fa\7\30\2\2\u07fa\u07fb\5\u0154\u00ab\2\u07fb")
        buf.write(u"\u07fc\7\31\2\2\u07fc\u07fe\3\2\2\2\u07fd\u07f7\3\2\2")
        buf.write(u"\2\u07fd\u07f9\3\2\2\2\u07fe\u015b\3\2\2\2\u07ff\u0800")
        buf.write(u"\5\u016a\u00b6\2\u0800\u0802\7\26\2\2\u0801\u0803\5\u015e")
        buf.write(u"\u00b0\2\u0802\u0801\3\2\2\2\u0802\u0803\3\2\2\2\u0803")
        buf.write(u"\u0804\3\2\2\2\u0804\u0805\7\27\2\2\u0805\u015d\3\2\2")
        buf.write(u"\2\u0806\u080d\5\u0160\u00b1\2\u0807\u080d\5\u0162\u00b2")
        buf.write(u"\2\u0808\u0809\5\u0160\u00b1\2\u0809\u080a\7\23\2\2\u080a")
        buf.write(u"\u080b\5\u0162\u00b2\2\u080b\u080d\3\2\2\2\u080c\u0806")
        buf.write(u"\3\2\2\2\u080c\u0807\3\2\2\2\u080c\u0808\3\2\2\2\u080d")
        buf.write(u"\u015f\3\2\2\2\u080e\u080f\b\u00b1\1\2\u080f\u0810\5")
        buf.write(u"\u0154\u00ab\2\u0810\u0816\3\2\2\2\u0811\u0812\f\3\2")
        buf.write(u"\2\u0812\u0813\7\23\2\2\u0813\u0815\5\u0154\u00ab\2\u0814")
        buf.write(u"\u0811\3\2\2\2\u0815\u0818\3\2\2\2\u0816\u0814\3\2\2")
        buf.write(u"\2\u0816\u0817\3\2\2\2\u0817\u0161\3\2\2\2\u0818\u0816")
        buf.write(u"\3\2\2\2\u0819\u081a\b\u00b2\1\2\u081a\u081b\5\u016a")
        buf.write(u"\u00b6\2\u081b\u081c\7-\2\2\u081c\u081d\5\u0154\u00ab")
        buf.write(u"\2\u081d\u0826\3\2\2\2\u081e\u081f\f\3\2\2\u081f\u0820")
        buf.write(u"\7\23\2\2\u0820\u0821\5\u016a\u00b6\2\u0821\u0822\7-")
        buf.write(u"\2\2\u0822\u0823\5\u0154\u00ab\2\u0823\u0825\3\2\2\2")
        buf.write(u"\u0824\u081e\3\2\2\2\u0825\u0828\3\2\2\2\u0826\u0824")
        buf.write(u"\3\2\2\2\u0826\u0827\3\2\2\2\u0827\u0163\3\2\2\2\u0828")
        buf.write(u"\u0826\3\2\2\2\u0829\u082a\7\26\2\2\u082a\u082b\5\u0154")
        buf.write(u"\u00ab\2\u082b\u082c\7\27\2\2\u082c\u0165\3\2\2\2\u082d")
        buf.write(u"\u082e\b\u00b4\1\2\u082e\u0831\7\u00a8\2\2\u082f\u0831")
        buf.write(u"\5\u016a\u00b6\2\u0830\u082d\3\2\2\2\u0830\u082f\3\2")
        buf.write(u"\2\2\u0831\u0837\3\2\2\2\u0832\u0833\f\3\2\2\u0833\u0834")
        buf.write(u"\7\25\2\2\u0834\u0836\5\u016a\u00b6\2\u0835\u0832\3\2")
        buf.write(u"\2\2\u0836\u0839\3\2\2\2\u0837\u0835\3\2\2\2\u0837\u0838")
        buf.write(u"\3\2\2\2\u0838\u0167\3\2\2\2\u0839\u0837\3\2\2\2\u083a")
        buf.write(u"\u0840\7\u00ab\2\2\u083b\u0840\7\u00ad\2\2\u083c\u0840")
        buf.write(u"\7\u00a9\2\2\u083d\u0840\7\u00a0\2\2\u083e\u0840\7\u00a1")
        buf.write(u"\2\2\u083f\u083a\3\2\2\2\u083f\u083b\3\2\2\2\u083f\u083c")
        buf.write(u"\3\2\2\2\u083f\u083d\3\2\2\2\u083f\u083e\3\2\2\2\u0840")
        buf.write(u"\u0169\3\2\2\2\u0841\u0842\t\t\2\2\u0842\u016b\3\2\2")
        buf.write(u"\2\u0843\u0844\7\u008b\2\2\u0844\u0845\5\u016e\u00b8")
        buf.write(u"\2\u0845\u0846\7\22\2\2\u0846\u084b\3\2\2\2\u0847\u0848")
        buf.write(u"\5\u016e\u00b8\2\u0848\u0849\7\22\2\2\u0849\u084b\3\2")
        buf.write(u"\2\2\u084a\u0843\3\2\2\2\u084a\u0847\3\2\2\2\u084b\u016d")
        buf.write(u"\3\2\2\2\u084c\u084d\b\u00b8\1\2\u084d\u084e\5\u0170")
        buf.write(u"\u00b9\2\u084e\u0853\3\2\2\2\u084f\u0850\f\3\2\2\u0850")
        buf.write(u"\u0852\5\u0176\u00bc\2\u0851\u084f\3\2\2\2\u0852\u0855")
        buf.write(u"\3\2\2\2\u0853\u0851\3\2\2\2\u0853\u0854\3\2\2\2\u0854")
        buf.write(u"\u016f\3\2\2\2\u0855\u0853\3\2\2\2\u0856\u085c\5\u0172")
        buf.write(u"\u00ba\2\u0857\u085c\5\u0174\u00bb\2\u0858\u085c\5\u017e")
        buf.write(u"\u00c0\2\u0859\u085c\5\u0180\u00c1\2\u085a\u085c\5\u0184")
        buf.write(u"\u00c3\2\u085b\u0856\3\2\2\2\u085b\u0857\3\2\2\2\u085b")
        buf.write(u"\u0858\3\2\2\2\u085b\u0859\3\2\2\2\u085b\u085a\3\2\2")
        buf.write(u"\2\u085c\u0171\3\2\2\2\u085d\u085e\5\u0100\u0081\2\u085e")
        buf.write(u"\u0173\3\2\2\2\u085f\u0860\5\u0124\u0093\2\u0860\u0861")
        buf.write(u"\5\u0178\u00bd\2\u0861\u0175\3\2\2\2\u0862\u0863\7\25")
        buf.write(u"\2\2\u0863\u0866\5\u0178\u00bd\2\u0864\u0866\5\u017c")
        buf.write(u"\u00bf\2\u0865\u0862\3\2\2\2\u0865\u0864\3\2\2\2\u0866")
        buf.write(u"\u0177\3\2\2\2\u0867\u0868\5\u0186\u00c4\2\u0868\u086a")
        buf.write(u"\7\26\2\2\u0869\u086b\5\u017a\u00be\2\u086a\u0869\3\2")
        buf.write(u"\2\2\u086a\u086b\3\2\2\2\u086b\u086c\3\2\2\2\u086c\u086d")
        buf.write(u"\7\27\2\2\u086d\u0179\3\2\2\2\u086e\u086f\b\u00be\1\2")
        buf.write(u"\u086f\u0870\5\u016e\u00b8\2\u0870\u0876\3\2\2\2\u0871")
        buf.write(u"\u0872\f\3\2\2\u0872\u0873\7\23\2\2\u0873\u0875\5\u016e")
        buf.write(u"\u00b8\2\u0874\u0871\3\2\2\2\u0875\u0878\3\2\2\2\u0876")
        buf.write(u"\u0874\3\2\2\2\u0876\u0877\3\2\2\2\u0877\u017b\3\2\2")
        buf.write(u"\2\u0878\u0876\3\2\2\2\u0879\u087a\7\30\2\2\u087a\u087b")
        buf.write(u"\5\u016e\u00b8\2\u087b\u087c\7\31\2\2\u087c\u017d\3\2")
        buf.write(u"\2\2\u087d\u087e\7\26\2\2\u087e\u087f\5\u016e\u00b8\2")
        buf.write(u"\u087f\u0880\7\27\2\2\u0880\u017f\3\2\2\2\u0881\u0882")
        buf.write(u"\b\u00c1\1\2\u0882\u0883\5\u0186\u00c4\2\u0883\u0889")
        buf.write(u"\3\2\2\2\u0884\u0885\f\3\2\2\u0885\u0886\7\25\2\2\u0886")
        buf.write(u"\u0888\5\u0186\u00c4\2\u0887\u0884\3\2\2\2\u0888\u088b")
        buf.write(u"\3\2\2\2\u0889\u0887\3\2\2\2\u0889\u088a\3\2\2\2\u088a")
        buf.write(u"\u0181\3\2\2\2\u088b\u0889\3\2\2\2\u088c\u088d\b\u00c2")
        buf.write(u"\1\2\u088d\u088e\5\u0180\u00c1\2\u088e\u0893\3\2\2\2")
        buf.write(u"\u088f\u0890\f\3\2\2\u0890\u0892\7\u00a8\2\2\u0891\u088f")
        buf.write(u"\3\2\2\2\u0892\u0895\3\2\2\2\u0893\u0891\3\2\2\2\u0893")
        buf.write(u"\u0894\3\2\2\2\u0894\u0183\3\2\2\2\u0895\u0893\3\2\2")
        buf.write(u"\2\u0896\u089c\7\u00ab\2\2\u0897\u089c\7\u00ad\2\2\u0898")
        buf.write(u"\u089c\7\u00a9\2\2\u0899\u089c\7\u00a0\2\2\u089a\u089c")
        buf.write(u"\7\u00a1\2\2\u089b\u0896\3\2\2\2\u089b\u0897\3\2\2\2")
        buf.write(u"\u089b\u0898\3\2\2\2\u089b\u0899\3\2\2\2\u089b\u089a")
        buf.write(u"\3\2\2\2\u089c\u0185\3\2\2\2\u089d\u089e\t\n\2\2\u089e")
        buf.write(u"\u0187\3\2\2\2\u089f\u08a0\7\u008b\2\2\u08a0\u08a1\5")
        buf.write(u"\u018a\u00c6\2\u08a1\u08a2\7\22\2\2\u08a2\u08a7\3\2\2")
        buf.write(u"\2\u08a3\u08a4\5\u018a\u00c6\2\u08a4\u08a5\7\22\2\2\u08a5")
        buf.write(u"\u08a7\3\2\2\2\u08a6\u089f\3\2\2\2\u08a6\u08a3\3\2\2")
        buf.write(u"\2\u08a7\u0189\3\2\2\2\u08a8\u08a9\b\u00c6\1\2\u08a9")
        buf.write(u"\u08aa\5\u018c\u00c7\2\u08aa\u08af\3\2\2\2\u08ab\u08ac")
        buf.write(u"\f\3\2\2\u08ac\u08ae\5\u0192\u00ca\2\u08ad\u08ab\3\2")
        buf.write(u"\2\2\u08ae\u08b1\3\2\2\2\u08af\u08ad\3\2\2\2\u08af\u08b0")
        buf.write(u"\3\2\2\2\u08b0\u018b\3\2\2\2\u08b1\u08af\3\2\2\2\u08b2")
        buf.write(u"\u08b8\5\u018e\u00c8\2\u08b3\u08b8\5\u0190\u00c9\2\u08b4")
        buf.write(u"\u08b8\5\u019a\u00ce\2\u08b5\u08b8\5\u019c\u00cf\2\u08b6")
        buf.write(u"\u08b8\5\u019e\u00d0\2\u08b7\u08b2\3\2\2\2\u08b7\u08b3")
        buf.write(u"\3\2\2\2\u08b7\u08b4\3\2\2\2\u08b7\u08b5\3\2\2\2\u08b7")
        buf.write(u"\u08b6\3\2\2\2\u08b8\u018d\3\2\2\2\u08b9\u08ba\5\u0100")
        buf.write(u"\u0081\2\u08ba\u018f\3\2\2\2\u08bb\u08bc\5\u0124\u0093")
        buf.write(u"\2\u08bc\u08bd\5\u0194\u00cb\2\u08bd\u0191\3\2\2\2\u08be")
        buf.write(u"\u08bf\7\25\2\2\u08bf\u08c2\5\u0194\u00cb\2\u08c0\u08c2")
        buf.write(u"\5\u0198\u00cd\2\u08c1\u08be\3\2\2\2\u08c1\u08c0\3\2")
        buf.write(u"\2\2\u08c2\u0193\3\2\2\2\u08c3\u08c4\5\u01a0\u00d1\2")
        buf.write(u"\u08c4\u08c6\7\26\2\2\u08c5\u08c7\5\u0196\u00cc\2\u08c6")
        buf.write(u"\u08c5\3\2\2\2\u08c6\u08c7\3\2\2\2\u08c7\u08c8\3\2\2")
        buf.write(u"\2\u08c8\u08c9\7\27\2\2\u08c9\u0195\3\2\2\2\u08ca\u08cb")
        buf.write(u"\b\u00cc\1\2\u08cb\u08cc\5\u018a\u00c6\2\u08cc\u08d2")
        buf.write(u"\3\2\2\2\u08cd\u08ce\f\3\2\2\u08ce\u08cf\7\23\2\2\u08cf")
        buf.write(u"\u08d1\5\u018a\u00c6\2\u08d0\u08cd\3\2\2\2\u08d1\u08d4")
        buf.write(u"\3\2\2\2\u08d2\u08d0\3\2\2\2\u08d2\u08d3\3\2\2\2\u08d3")
        buf.write(u"\u0197\3\2\2\2\u08d4\u08d2\3\2\2\2\u08d5\u08d6\7\30\2")
        buf.write(u"\2\u08d6\u08d7\5\u018a\u00c6\2\u08d7\u08d8\7\31\2\2\u08d8")
        buf.write(u"\u0199\3\2\2\2\u08d9\u08da\7\26\2\2\u08da\u08db\5\u018a")
        buf.write(u"\u00c6\2\u08db\u08dc\7\27\2\2\u08dc\u019b\3\2\2\2\u08dd")
        buf.write(u"\u08de\b\u00cf\1\2\u08de\u08e1\7\u00a8\2\2\u08df\u08e1")
        buf.write(u"\5\u01a0\u00d1\2\u08e0\u08dd\3\2\2\2\u08e0\u08df\3\2")
        buf.write(u"\2\2\u08e1\u08e7\3\2\2\2\u08e2\u08e3\f\3\2\2\u08e3\u08e4")
        buf.write(u"\7\25\2\2\u08e4\u08e6\5\u01a0\u00d1\2\u08e5\u08e2\3\2")
        buf.write(u"\2\2\u08e6\u08e9\3\2\2\2\u08e7\u08e5\3\2\2\2\u08e7\u08e8")
        buf.write(u"\3\2\2\2\u08e8\u019d\3\2\2\2\u08e9\u08e7\3\2\2\2\u08ea")
        buf.write(u"\u08f0\7\u00ab\2\2\u08eb\u08f0\7\u00ad\2\2\u08ec\u08f0")
        buf.write(u"\7\u00a9\2\2\u08ed\u08f0\7\u00a0\2\2\u08ee\u08f0\7\u00a1")
        buf.write(u"\2\2\u08ef\u08ea\3\2\2\2\u08ef\u08eb\3\2\2\2\u08ef\u08ec")
        buf.write(u"\3\2\2\2\u08ef\u08ed\3\2\2\2\u08ef\u08ee\3\2\2\2\u08f0")
        buf.write(u"\u019f\3\2\2\2\u08f1\u08f2\t\13\2\2\u08f2\u01a1\3\2\2")
        buf.write(u"\2\u00bf\u01a8\u01ab\u01c4\u01c9\u01d7\u01dd\u01df\u01e1")
        buf.write(u"\u01e8\u01ed\u01f8\u01ff\u020c\u021a\u022e\u0245\u0250")
        buf.write(u"\u0257\u0260\u0265\u026c\u0275\u028a\u0292\u0297\u029d")
        buf.write(u"\u02a2\u02ab\u02b0\u02b5\u02cd\u02d8\u02dc\u02f1\u030b")
        buf.write(u"\u0310\u0319\u0322\u032b\u0348\u035b\u0361\u0383\u038c")
        buf.write(u"\u03a3\u03b1\u03ba\u03c3\u03da\u03e0\u03f4\u0463\u0465")
        buf.write(u"\u0471\u047c\u048b\u0490\u0497\u04a0\u04a7\u04ab\u04b7")
        buf.write(u"\u04be\u04c5\u04d5\u04e0\u04e4\u04e9\u04ee\u04f0\u04f4")
        buf.write(u"\u04fd\u050d\u0516\u051c\u0521\u0528\u0530\u053b\u0543")
        buf.write(u"\u054b\u0551\u0559\u0562\u056a\u0577\u057a\u057e\u0583")
        buf.write(u"\u0587\u0590\u05a5\u05af\u05b1\u05b6\u05c7\u05cc\u05d5")
        buf.write(u"\u05dc\u05e1\u05e6\u05f5\u05fa\u05fd\u0601\u0606\u060d")
        buf.write(u"\u0618\u061a\u0623\u062b\u0633\u0639\u0645\u0649\u0653")
        buf.write(u"\u0658\u065e\u0665\u066a\u0671\u0679\u0680\u068a\u0697")
        buf.write(u"\u069b\u069e\u06a2\u06a5\u06ad\u06b6\u06bf\u06c8\u06d9")
        buf.write(u"\u06ea\u06f1\u06f8\u0702\u0709\u070c\u0710\u0715\u0719")
        buf.write(u"\u0724\u0727\u072e\u073e\u074b\u0752\u0763\u076b\u076f")
        buf.write(u"\u0777\u0799\u07a2\u07ac\u07b8\u07bd\u07c9\u07db\u07e2")
        buf.write(u"\u07eb\u07f3\u07fd\u0802\u080c\u0816\u0826\u0830\u0837")
        buf.write(u"\u083f\u084a\u0853\u085b\u0865\u086a\u0876\u0889\u0893")
        buf.write(u"\u089b\u08a6\u08af\u08b7\u08c1\u08c6\u08d2\u08e0\u08e7")
        buf.write(u"\u08ef")
        return buf.getvalue()


class MParser ( AbstractParser ):

    grammarFileName = "MParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"<INVALID>", 
                     u"'Java:'", u"'C#:'", u"'Python2:'", u"'Python3:'", 
                     u"'JavaScript:'", u"'Swift:'", u"':'", u"';'", u"<INVALID>", 
                     u"'..'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", 
                     u"<INVALID>", u"'-'", u"'*'", u"'/'", u"'\\'", u"'%'", 
                     u"'>'", u"'>='", u"'<'", u"'<='", u"'<>'", u"'='", 
                     u"'!='", u"'=='", u"'~='", u"'~'", u"'<-'", u"'->'", 
                     u"'Boolean'", u"'Character'", u"'Text'", u"'Integer'", 
                     u"'Decimal'", u"'Date'", u"'Time'", u"'DateTime'", 
                     u"'Period'", u"'Version'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'Blob'", u"'Image'", u"'UUID'", u"'Iterator'", 
                     u"'Cursor'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"<INVALID>", u"'attr'", 
                     u"'attribute'", u"'attributes'", u"'bindings'", u"'break'", 
                     u"'by'", u"'case'", u"'catch'", u"'category'", u"'class'", 
                     u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'filtered'", u"'finally'", u"'flush'", u"'for'", 
                     u"'from'", u"'getter'", u"'has'", u"'if'", u"'in'", 
                     u"'index'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
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
                      u"TIME", u"DATETIME", u"PERIOD", u"VERSION", u"METHOD_T", 
                      u"CODE", u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", 
                      u"ITERATOR", u"CURSOR", u"ABSTRACT", u"ALL", u"ALWAYS", 
                      u"AND", u"ANY", u"AS", u"ASC", u"ATTR", u"ATTRIBUTE", 
                      u"ATTRIBUTES", u"BINDINGS", u"BREAK", u"BY", u"CASE", 
                      u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", u"CONTAINS", 
                      u"DEF", u"DEFAULT", u"DEFINE", u"DELETE", u"DESC", 
                      u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FILTERED", u"FINALLY", u"FLUSH", u"FOR", u"FROM", 
                      u"GETTER", u"HAS", u"IF", u"IN", u"INDEX", u"INVOKE", 
                      u"IS", u"MATCHING", u"METHOD", u"METHODS", u"MODULO", 
                      u"MUTABLE", u"NATIVE", u"NONE", u"NOT", u"NOTHING", 
                      u"NULL", u"ON", u"ONE", u"OPEN", u"OPERATOR", u"OR", 
                      u"ORDER", u"OTHERWISE", u"PASS", u"RAISE", u"READ", 
                      u"RECEIVING", u"RESOURCE", u"RETURN", u"RETURNING", 
                      u"ROWS", u"SELF", u"SETTER", u"SINGLETON", u"SORTED", 
                      u"STORABLE", u"STORE", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"VERIFYING", u"WITH", u"WHEN", 
                      u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"UUID_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL", u"VERSION_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_index_clause = 5
    RULE_concrete_category_declaration = 6
    RULE_singleton_category_declaration = 7
    RULE_derived_list = 8
    RULE_operator_method_declaration = 9
    RULE_setter_method_declaration = 10
    RULE_native_setter_declaration = 11
    RULE_getter_method_declaration = 12
    RULE_native_getter_declaration = 13
    RULE_native_category_declaration = 14
    RULE_native_resource_declaration = 15
    RULE_native_category_bindings = 16
    RULE_native_category_binding_list = 17
    RULE_abstract_method_declaration = 18
    RULE_concrete_method_declaration = 19
    RULE_native_method_declaration = 20
    RULE_test_method_declaration = 21
    RULE_assertion = 22
    RULE_typed_argument = 23
    RULE_statement = 24
    RULE_flush_statement = 25
    RULE_store_statement = 26
    RULE_method_call = 27
    RULE_method_selector = 28
    RULE_callable_parent = 29
    RULE_callable_selector = 30
    RULE_with_resource_statement = 31
    RULE_with_singleton_statement = 32
    RULE_switch_statement = 33
    RULE_switch_case_statement = 34
    RULE_for_each_statement = 35
    RULE_do_while_statement = 36
    RULE_while_statement = 37
    RULE_if_statement = 38
    RULE_else_if_statement_list = 39
    RULE_raise_statement = 40
    RULE_try_statement = 41
    RULE_catch_statement = 42
    RULE_break_statement = 43
    RULE_return_statement = 44
    RULE_expression = 45
    RULE_closure_expression = 46
    RULE_instance_expression = 47
    RULE_method_expression = 48
    RULE_instance_selector = 49
    RULE_blob_expression = 50
    RULE_document_expression = 51
    RULE_constructor_expression = 52
    RULE_copy_from = 53
    RULE_argument_assignment_list = 54
    RULE_argument_assignment = 55
    RULE_write_statement = 56
    RULE_filtered_list_suffix = 57
    RULE_fetch_store_expression = 58
    RULE_sorted_expression = 59
    RULE_assign_instance_statement = 60
    RULE_child_instance = 61
    RULE_assign_tuple_statement = 62
    RULE_lfs = 63
    RULE_lfp = 64
    RULE_indent = 65
    RULE_dedent = 66
    RULE_null_literal = 67
    RULE_declaration_list = 68
    RULE_declarations = 69
    RULE_declaration = 70
    RULE_resource_declaration = 71
    RULE_enum_declaration = 72
    RULE_native_symbol_list = 73
    RULE_category_symbol_list = 74
    RULE_symbol_list = 75
    RULE_attribute_constraint = 76
    RULE_list_literal = 77
    RULE_set_literal = 78
    RULE_expression_list = 79
    RULE_range_literal = 80
    RULE_typedef = 81
    RULE_primary_type = 82
    RULE_native_type = 83
    RULE_category_type = 84
    RULE_mutable_category_type = 85
    RULE_code_type = 86
    RULE_category_declaration = 87
    RULE_type_identifier_list = 88
    RULE_method_identifier = 89
    RULE_identifier = 90
    RULE_variable_identifier = 91
    RULE_attribute_identifier = 92
    RULE_type_identifier = 93
    RULE_symbol_identifier = 94
    RULE_argument_list = 95
    RULE_argument = 96
    RULE_operator_argument = 97
    RULE_named_argument = 98
    RULE_code_argument = 99
    RULE_category_or_any_type = 100
    RULE_any_type = 101
    RULE_member_method_declaration_list = 102
    RULE_member_method_declaration = 103
    RULE_native_member_method_declaration_list = 104
    RULE_native_member_method_declaration = 105
    RULE_native_category_binding = 106
    RULE_python_category_binding = 107
    RULE_python_module = 108
    RULE_javascript_category_binding = 109
    RULE_javascript_module = 110
    RULE_variable_identifier_list = 111
    RULE_attribute_identifier_list = 112
    RULE_method_declaration = 113
    RULE_comment_statement = 114
    RULE_native_statement_list = 115
    RULE_native_statement = 116
    RULE_python_native_statement = 117
    RULE_javascript_native_statement = 118
    RULE_statement_list = 119
    RULE_assertion_list = 120
    RULE_switch_case_statement_list = 121
    RULE_catch_statement_list = 122
    RULE_literal_collection = 123
    RULE_atomic_literal = 124
    RULE_literal_list_literal = 125
    RULE_selectable_expression = 126
    RULE_this_expression = 127
    RULE_parenthesis_expression = 128
    RULE_literal_expression = 129
    RULE_collection_literal = 130
    RULE_tuple_literal = 131
    RULE_dict_literal = 132
    RULE_expression_tuple = 133
    RULE_dict_entry_list = 134
    RULE_dict_entry = 135
    RULE_slice_arguments = 136
    RULE_assign_variable_statement = 137
    RULE_assignable_instance = 138
    RULE_is_expression = 139
    RULE_read_all_expression = 140
    RULE_read_one_expression = 141
    RULE_order_by_list = 142
    RULE_order_by = 143
    RULE_operator = 144
    RULE_new_token = 145
    RULE_key_token = 146
    RULE_module_token = 147
    RULE_value_token = 148
    RULE_symbols_token = 149
    RULE_assign = 150
    RULE_multiply = 151
    RULE_divide = 152
    RULE_idivide = 153
    RULE_modulo = 154
    RULE_javascript_statement = 155
    RULE_javascript_expression = 156
    RULE_javascript_primary_expression = 157
    RULE_javascript_this_expression = 158
    RULE_javascript_new_expression = 159
    RULE_javascript_selector_expression = 160
    RULE_javascript_method_expression = 161
    RULE_javascript_arguments = 162
    RULE_javascript_item_expression = 163
    RULE_javascript_parenthesis_expression = 164
    RULE_javascript_identifier_expression = 165
    RULE_javascript_literal_expression = 166
    RULE_javascript_identifier = 167
    RULE_python_statement = 168
    RULE_python_expression = 169
    RULE_python_primary_expression = 170
    RULE_python_self_expression = 171
    RULE_python_selector_expression = 172
    RULE_python_method_expression = 173
    RULE_python_argument_list = 174
    RULE_python_ordinal_argument_list = 175
    RULE_python_named_argument_list = 176
    RULE_python_parenthesis_expression = 177
    RULE_python_identifier_expression = 178
    RULE_python_literal_expression = 179
    RULE_python_identifier = 180
    RULE_java_statement = 181
    RULE_java_expression = 182
    RULE_java_primary_expression = 183
    RULE_java_this_expression = 184
    RULE_java_new_expression = 185
    RULE_java_selector_expression = 186
    RULE_java_method_expression = 187
    RULE_java_arguments = 188
    RULE_java_item_expression = 189
    RULE_java_parenthesis_expression = 190
    RULE_java_identifier_expression = 191
    RULE_java_class_identifier_expression = 192
    RULE_java_literal_expression = 193
    RULE_java_identifier = 194
    RULE_csharp_statement = 195
    RULE_csharp_expression = 196
    RULE_csharp_primary_expression = 197
    RULE_csharp_this_expression = 198
    RULE_csharp_new_expression = 199
    RULE_csharp_selector_expression = 200
    RULE_csharp_method_expression = 201
    RULE_csharp_arguments = 202
    RULE_csharp_item_expression = 203
    RULE_csharp_parenthesis_expression = 204
    RULE_csharp_identifier_expression = 205
    RULE_csharp_literal_expression = 206
    RULE_csharp_identifier = 207

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"index_clause", u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"typed_argument", 
                   u"statement", u"flush_statement", u"store_statement", 
                   u"method_call", u"method_selector", u"callable_parent", 
                   u"callable_selector", u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"break_statement", u"return_statement", 
                   u"expression", u"closure_expression", u"instance_expression", 
                   u"method_expression", u"instance_selector", u"blob_expression", 
                   u"document_expression", u"constructor_expression", u"copy_from", 
                   u"argument_assignment_list", u"argument_assignment", 
                   u"write_statement", u"filtered_list_suffix", u"fetch_store_expression", 
                   u"sorted_expression", u"assign_instance_statement", u"child_instance", 
                   u"assign_tuple_statement", u"lfs", u"lfp", u"indent", 
                   u"dedent", u"null_literal", u"declaration_list", u"declarations", 
                   u"declaration", u"resource_declaration", u"enum_declaration", 
                   u"native_symbol_list", u"category_symbol_list", u"symbol_list", 
                   u"attribute_constraint", u"list_literal", u"set_literal", 
                   u"expression_list", u"range_literal", u"typedef", u"primary_type", 
                   u"native_type", u"category_type", u"mutable_category_type", 
                   u"code_type", u"category_declaration", u"type_identifier_list", 
                   u"method_identifier", u"identifier", u"variable_identifier", 
                   u"attribute_identifier", u"type_identifier", u"symbol_identifier", 
                   u"argument_list", u"argument", u"operator_argument", 
                   u"named_argument", u"code_argument", u"category_or_any_type", 
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"javascript_category_binding", u"javascript_module", 
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
                   u"is_expression", u"read_all_expression", u"read_one_expression", 
                   u"order_by_list", u"order_by", u"operator", u"new_token", 
                   u"key_token", u"module_token", u"value_token", u"symbols_token", 
                   u"assign", u"multiply", u"divide", u"idivide", u"modulo", 
                   u"javascript_statement", u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_new_expression", 
                   u"javascript_selector_expression", u"javascript_method_expression", 
                   u"javascript_arguments", u"javascript_item_expression", 
                   u"javascript_parenthesis_expression", u"javascript_identifier_expression", 
                   u"javascript_literal_expression", u"javascript_identifier", 
                   u"python_statement", u"python_expression", u"python_primary_expression", 
                   u"python_self_expression", u"python_selector_expression", 
                   u"python_method_expression", u"python_argument_list", 
                   u"python_ordinal_argument_list", u"python_named_argument_list", 
                   u"python_parenthesis_expression", u"python_identifier_expression", 
                   u"python_literal_expression", u"python_identifier", u"java_statement", 
                   u"java_expression", u"java_primary_expression", u"java_this_expression", 
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
    VERSION=59
    METHOD_T=60
    CODE=61
    DOCUMENT=62
    BLOB=63
    IMAGE=64
    UUID=65
    ITERATOR=66
    CURSOR=67
    ABSTRACT=68
    ALL=69
    ALWAYS=70
    AND=71
    ANY=72
    AS=73
    ASC=74
    ATTR=75
    ATTRIBUTE=76
    ATTRIBUTES=77
    BINDINGS=78
    BREAK=79
    BY=80
    CASE=81
    CATCH=82
    CATEGORY=83
    CLASS=84
    CLOSE=85
    CONTAINS=86
    DEF=87
    DEFAULT=88
    DEFINE=89
    DELETE=90
    DESC=91
    DO=92
    DOING=93
    EACH=94
    ELSE=95
    ENUM=96
    ENUMERATED=97
    EXCEPT=98
    EXECUTE=99
    EXPECTING=100
    EXTENDS=101
    FETCH=102
    FILTERED=103
    FINALLY=104
    FLUSH=105
    FOR=106
    FROM=107
    GETTER=108
    HAS=109
    IF=110
    IN=111
    INDEX=112
    INVOKE=113
    IS=114
    MATCHING=115
    METHOD=116
    METHODS=117
    MODULO=118
    MUTABLE=119
    NATIVE=120
    NONE=121
    NOT=122
    NOTHING=123
    NULL=124
    ON=125
    ONE=126
    OPEN=127
    OPERATOR=128
    OR=129
    ORDER=130
    OTHERWISE=131
    PASS=132
    RAISE=133
    READ=134
    RECEIVING=135
    RESOURCE=136
    RETURN=137
    RETURNING=138
    ROWS=139
    SELF=140
    SETTER=141
    SINGLETON=142
    SORTED=143
    STORABLE=144
    STORE=145
    SWITCH=146
    TEST=147
    THIS=148
    THROW=149
    TO=150
    TRY=151
    VERIFYING=152
    WITH=153
    WHEN=154
    WHERE=155
    WHILE=156
    WRITE=157
    BOOLEAN_LITERAL=158
    CHAR_LITERAL=159
    MIN_INTEGER=160
    MAX_INTEGER=161
    SYMBOL_IDENTIFIER=162
    TYPE_IDENTIFIER=163
    VARIABLE_IDENTIFIER=164
    NATIVE_IDENTIFIER=165
    DOLLAR_IDENTIFIER=166
    TEXT_LITERAL=167
    UUID_LITERAL=168
    INTEGER_LITERAL=169
    HEXA_LITERAL=170
    DECIMAL_LITERAL=171
    DATETIME_LITERAL=172
    TIME_LITERAL=173
    DATE_LITERAL=174
    PERIOD_LITERAL=175
    VERSION_LITERAL=176

    def __init__(self, input, output=sys.stdout):
        super(MParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.symbols = None # Category_symbol_listContext

        def ENUM(self):
            return self.getToken(MParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(MParser.Category_symbol_listContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def getRuleIndex(self):
            return MParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_category_declaration"):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_category_declaration"):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = MParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MParser.ENUM)
            self.state = 417
            localctx.name = self.type_identifier()
            self.state = 418
            self.match(MParser.LPAR)
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.TYPE_IDENTIFIER]:
                self.state = 419
                localctx.derived = self.type_identifier()
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.COMMA:
                    self.state = 420
                    self.match(MParser.COMMA)
                    self.state = 421
                    localctx.attrs = self.attribute_identifier_list()


                pass
            elif token in [MParser.STORABLE, MParser.VARIABLE_IDENTIFIER]:
                self.state = 424
                localctx.attrs = self.attribute_identifier_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 427
            self.match(MParser.RPAR)
            self.state = 428
            self.match(MParser.COLON)
            self.state = 429
            self.indent()
            self.state = 430
            localctx.symbols = self.category_symbol_list()
            self.state = 431
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
            super(MParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUM(self):
            return self.getToken(MParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(MParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(MParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_native_declaration"):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_native_declaration"):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = MParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MParser.ENUM)
            self.state = 434
            localctx.name = self.type_identifier()
            self.state = 435
            self.match(MParser.LPAR)
            self.state = 436
            localctx.typ = self.native_type()
            self.state = 437
            self.match(MParser.RPAR)
            self.state = 438
            self.match(MParser.COLON)
            self.state = 439
            self.indent()
            self.state = 440
            localctx.symbols = self.native_symbol_list()
            self.state = 441
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
            super(MParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol"):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol"):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = MParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            localctx.name = self.symbol_identifier()
            self.state = 444
            self.match(MParser.EQ)
            self.state = 445
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
            super(MParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_category_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol"):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol"):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = MParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            localctx.name = self.symbol_identifier()
            self.state = 448
            self.match(MParser.LPAR)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 449
                localctx.args = self.argument_assignment_list(0)


            self.state = 452
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Index_clauseContext

        def ATTR(self):
            return self.getToken(MParser.ATTR, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def attribute_identifier(self):
            return self.getTypedRuleContext(MParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(MParser.Attribute_constraintContext,0)


        def index_clause(self):
            return self.getTypedRuleContext(MParser.Index_clauseContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def getRuleIndex(self):
            return MParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_declaration"):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_declaration"):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = MParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 454
                self.match(MParser.STORABLE)


            self.state = 457
            self.match(MParser.ATTR)
            self.state = 458
            localctx.name = self.attribute_identifier()
            self.state = 459
            self.match(MParser.LPAR)
            self.state = 460
            localctx.typ = self.typedef(0)
            self.state = 461
            self.match(MParser.RPAR)
            self.state = 462
            self.match(MParser.COLON)
            self.state = 463
            self.indent()
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.PASS]:
                self.state = 464
                self.match(MParser.PASS)
                pass
            elif token in [MParser.IN, MParser.INDEX, MParser.MATCHING]:
                self.state = 477
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MParser.IN, MParser.MATCHING]:
                    self.state = 465
                    localctx.match = self.attribute_constraint()
                    self.state = 469
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 466
                        self.lfp()
                        self.state = 467
                        localctx.indices = self.index_clause()


                    pass
                elif token in [MParser.INDEX]:
                    self.state = 471
                    localctx.indices = self.index_clause()
                    self.state = 475
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 472
                        self.lfp()
                        self.state = 473
                        localctx.match = self.attribute_constraint()


                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 481
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Index_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Index_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.indices = None # Variable_identifier_listContext

        def INDEX(self):
            return self.getToken(MParser.INDEX, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(MParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_index_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterIndex_clause"):
                listener.enterIndex_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIndex_clause"):
                listener.exitIndex_clause(self)




    def index_clause(self):

        localctx = MParser.Index_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_index_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MParser.INDEX)
            self.state = 484
            self.match(MParser.LPAR)
            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 485
                localctx.indices = self.variable_identifier_list()


            self.state = 488
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_identifier_listContext
            self.methods = None # Member_method_declaration_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(MParser.Derived_listContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_category_declaration"):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_category_declaration"):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = MParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 490
                self.match(MParser.STORABLE)


            self.state = 493
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 494
            localctx.name = self.type_identifier()
            self.state = 495
            self.match(MParser.LPAR)
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 496
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 497
                localctx.attrs = self.attribute_identifier_list()
                pass

            elif la_ == 3:
                self.state = 498
                localctx.derived = self.derived_list()
                self.state = 499
                self.match(MParser.COMMA)
                self.state = 500
                localctx.attrs = self.attribute_identifier_list()
                pass


            self.state = 504
            self.match(MParser.RPAR)
            self.state = 505
            self.match(MParser.COLON)
            self.state = 506
            self.indent()
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 507
                localctx.methods = self.member_method_declaration_list()
                pass
            elif token in [MParser.PASS]:
                self.state = 508
                self.match(MParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 511
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
            super(MParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.methods = None # Member_method_declaration_listContext

        def SINGLETON(self):
            return self.getToken(MParser.SINGLETON, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSingleton_category_declaration"):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleton_category_declaration"):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = MParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(MParser.SINGLETON)
            self.state = 514
            localctx.name = self.type_identifier()
            self.state = 515
            self.match(MParser.LPAR)
            self.state = 516
            localctx.attrs = self.attribute_identifier_list()
            self.state = 517
            self.match(MParser.RPAR)
            self.state = 518
            self.match(MParser.COLON)
            self.state = 519
            self.indent()
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 520
                localctx.methods = self.member_method_declaration_list()
                pass
            elif token in [MParser.PASS]:
                self.state = 521
                self.match(MParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 524
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
            super(MParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Type_identifier_listContext

        def type_identifier_list(self):
            return self.getTypedRuleContext(MParser.Type_identifier_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_derived_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDerived_list"):
                listener.enterDerived_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerived_list"):
                listener.exitDerived_list(self)




    def derived_list(self):

        localctx = MParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            localctx.items = self.type_identifier_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def OPERATOR(self):
            return self.getToken(MParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(MParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(MParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def getRuleIndex(self):
            return MParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_method_declaration"):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_method_declaration"):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = MParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MParser.DEF)
            self.state = 529
            self.match(MParser.OPERATOR)
            self.state = 530
            localctx.op = self.operator()
            self.state = 531
            self.match(MParser.LPAR)
            self.state = 532
            localctx.arg = self.operator_argument()
            self.state = 533
            self.match(MParser.RPAR)
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 534
                self.match(MParser.RARROW)
                self.state = 535
                localctx.typ = self.typedef(0)


            self.state = 538
            self.match(MParser.COLON)
            self.state = 539
            self.indent()
            self.state = 540
            localctx.stmts = self.statement_list()
            self.state = 541
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
            super(MParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def SETTER(self):
            return self.getToken(MParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSetter_method_declaration"):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetter_method_declaration"):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = MParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(MParser.DEF)
            self.state = 544
            localctx.name = self.variable_identifier()
            self.state = 545
            self.match(MParser.SETTER)
            self.state = 546
            self.match(MParser.LPAR)
            self.state = 547
            self.match(MParser.RPAR)
            self.state = 548
            self.match(MParser.COLON)
            self.state = 549
            self.indent()
            self.state = 550
            localctx.stmts = self.statement_list()
            self.state = 551
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
            super(MParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def SETTER(self):
            return self.getToken(MParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(MParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def getRuleIndex(self):
            return MParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_setter_declaration"):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_setter_declaration"):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = MParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(MParser.DEF)
            self.state = 554
            localctx.name = self.variable_identifier()
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 555
                self.match(MParser.NATIVE)


            self.state = 558
            self.match(MParser.SETTER)
            self.state = 559
            self.match(MParser.LPAR)
            self.state = 560
            self.match(MParser.RPAR)
            self.state = 561
            self.match(MParser.COLON)
            self.state = 562
            self.indent()
            self.state = 563
            localctx.stmts = self.native_statement_list()
            self.state = 564
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
            super(MParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def GETTER(self):
            return self.getToken(MParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterGetter_method_declaration"):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGetter_method_declaration"):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = MParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MParser.DEF)
            self.state = 567
            localctx.name = self.variable_identifier()
            self.state = 568
            self.match(MParser.GETTER)
            self.state = 569
            self.match(MParser.LPAR)
            self.state = 570
            self.match(MParser.RPAR)
            self.state = 571
            self.match(MParser.COLON)
            self.state = 572
            self.indent()
            self.state = 573
            localctx.stmts = self.statement_list()
            self.state = 574
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
            super(MParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def GETTER(self):
            return self.getToken(MParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(MParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def getRuleIndex(self):
            return MParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_getter_declaration"):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_getter_declaration"):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = MParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(MParser.DEF)
            self.state = 577
            localctx.name = self.variable_identifier()
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 578
                self.match(MParser.NATIVE)


            self.state = 581
            self.match(MParser.GETTER)
            self.state = 582
            self.match(MParser.LPAR)
            self.state = 583
            self.match(MParser.RPAR)
            self.state = 584
            self.match(MParser.COLON)
            self.state = 585
            self.indent()
            self.state = 586
            localctx.stmts = self.native_statement_list()
            self.state = 587
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
            super(MParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_declaration"):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_declaration"):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = MParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 589
                self.match(MParser.STORABLE)


            self.state = 592
            self.match(MParser.NATIVE)
            self.state = 593
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 594
            localctx.name = self.type_identifier()
            self.state = 595
            self.match(MParser.LPAR)
            self.state = 597
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 596
                localctx.attrs = self.attribute_identifier_list()


            self.state = 599
            self.match(MParser.RPAR)
            self.state = 600
            self.match(MParser.COLON)
            self.state = 601
            self.indent()
            self.state = 602
            localctx.bindings = self.native_category_bindings()
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 603
                self.lfp()
                self.state = 604
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 608
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
            super(MParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(MParser.RESOURCE, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_resource_declaration"):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_resource_declaration"):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = MParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 610
                self.match(MParser.STORABLE)


            self.state = 613
            self.match(MParser.NATIVE)
            self.state = 614
            self.match(MParser.RESOURCE)
            self.state = 615
            localctx.name = self.type_identifier()
            self.state = 616
            self.match(MParser.LPAR)
            self.state = 618
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 617
                localctx.attrs = self.attribute_identifier_list()


            self.state = 620
            self.match(MParser.RPAR)
            self.state = 621
            self.match(MParser.COLON)
            self.state = 622
            self.indent()
            self.state = 623
            localctx.bindings = self.native_category_bindings()
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 624
                self.lfp()
                self.state = 625
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 629
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
            super(MParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def BINDINGS(self):
            return self.getToken(MParser.BINDINGS, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(MParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_bindings"):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_bindings"):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = MParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.match(MParser.DEF)
            self.state = 632
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 633
            self.match(MParser.BINDINGS)
            self.state = 634
            self.match(MParser.COLON)
            self.state = 635
            self.indent()
            self.state = 636
            localctx.items = self.native_category_binding_list(0)
            self.state = 637
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
            super(MParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(MParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_binding_listContext)
            super(MParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(MParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingListItem"):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingListItem"):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_binding_listContext)
            super(MParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingList"):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingList"):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 640
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 648
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.NativeCategoryBindingListItemContext(self, MParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 642
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 643
                    self.lfp()
                    self.state = 644
                    localctx.item = self.native_category_binding() 
                self.state = 650
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext

        def ABSTRACT(self):
            return self.getToken(MParser.ABSTRACT, 0)

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def getRuleIndex(self):
            return MParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAbstract_method_declaration"):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAbstract_method_declaration"):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = MParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.match(MParser.ABSTRACT)
            self.state = 652
            self.match(MParser.DEF)
            self.state = 653
            localctx.name = self.method_identifier()
            self.state = 654
            self.match(MParser.LPAR)
            self.state = 656
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 655
                localctx.args = self.argument_list()


            self.state = 658
            self.match(MParser.RPAR)
            self.state = 661
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 659
                self.match(MParser.RARROW)
                self.state = 660
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
            super(MParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def getRuleIndex(self):
            return MParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_method_declaration"):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_method_declaration"):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = MParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 663
            self.match(MParser.DEF)
            self.state = 664
            localctx.name = self.method_identifier()
            self.state = 665
            self.match(MParser.LPAR)
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 666
                localctx.args = self.argument_list()


            self.state = 669
            self.match(MParser.RPAR)
            self.state = 672
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 670
                self.match(MParser.RARROW)
                self.state = 671
                localctx.typ = self.typedef(0)


            self.state = 674
            self.match(MParser.COLON)
            self.state = 675
            self.indent()
            self.state = 676
            localctx.stmts = self.statement_list()
            self.state = 677
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
            super(MParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(MParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MParser.Argument_listContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_method_declaration"):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_method_declaration"):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = MParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(MParser.DEF)
            self.state = 681
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 680
                self.match(MParser.NATIVE)


            self.state = 683
            localctx.name = self.method_identifier()
            self.state = 684
            self.match(MParser.LPAR)
            self.state = 686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 685
                localctx.args = self.argument_list()


            self.state = 688
            self.match(MParser.RPAR)
            self.state = 691
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 689
                self.match(MParser.RARROW)
                self.state = 690
                localctx.typ = self.category_or_any_type()


            self.state = 693
            self.match(MParser.COLON)
            self.state = 694
            self.indent()
            self.state = 695
            localctx.stmts = self.native_statement_list()
            self.state = 696
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
            super(MParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def VERIFYING(self):
            return self.getToken(MParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(MParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterTest_method_declaration"):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTest_method_declaration"):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = MParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.match(MParser.DEF)
            self.state = 699
            self.match(MParser.TEST)
            self.state = 700
            localctx.name = self.match(MParser.TEXT_LITERAL)
            self.state = 701
            self.match(MParser.LPAR)
            self.state = 702
            self.match(MParser.RPAR)
            self.state = 703
            self.match(MParser.COLON)
            self.state = 704
            self.indent()
            self.state = 705
            localctx.stmts = self.statement_list()
            self.state = 706
            self.dedent()
            self.state = 707
            self.lfp()
            self.state = 708
            self.match(MParser.VERIFYING)
            self.state = 709
            self.match(MParser.COLON)
            self.state = 715
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.LF]:
                self.state = 710
                self.indent()
                self.state = 711
                localctx.exps = self.assertion_list()
                self.state = 712
                self.dedent()
                pass
            elif token in [MParser.SYMBOL_IDENTIFIER]:
                self.state = 714
                localctx.error = self.symbol_identifier()
                pass
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
            super(MParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assertion

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion"):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion"):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = MParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
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
            super(MParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_identifier_listContext
            self.value = None # Literal_expressionContext

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_typed_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterTyped_argument"):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTyped_argument"):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = MParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
            localctx.name = self.variable_identifier()
            self.state = 720
            self.match(MParser.COLON)
            self.state = 721
            localctx.typ = self.category_or_any_type()
            self.state = 726
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.LPAR:
                self.state = 722
                self.match(MParser.LPAR)
                self.state = 723
                localctx.attrs = self.attribute_identifier_list()
                self.state = 724
                self.match(MParser.RPAR)


            self.state = 730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 728
                self.match(MParser.EQ)
                self.state = 729
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
            super(MParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(MParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(MParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCommentStatement"):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCommentStatement"):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(MParser.Store_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterStoreStatement"):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStoreStatement"):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(MParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithSingletonStatement"):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithSingletonStatement"):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(MParser.Write_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWriteStatement"):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWriteStatement"):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(MParser.While_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWhileStatement"):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhileStatement"):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(MParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithResourceStatement"):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithResourceStatement"):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(MParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRaiseStatement"):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaiseStatement"):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(MParser.Break_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBreakStatement"):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreakStatement"):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(MParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignInstanceStatement"):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignInstanceStatement"):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(MParser.If_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIfStatement"):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIfStatement"):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(MParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSwitchStatement"):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitchStatement"):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(MParser.Try_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTryStatement"):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTryStatement"):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(MParser.Method_callContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodCallStatement"):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodCallStatement"):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(MParser.Return_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReturnStatement"):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturnStatement"):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(MParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignTupleStatement"):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignTupleStatement"):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureStatement"):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureStatement"):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(MParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFlushStatement"):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlushStatement"):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(MParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDoWhileStatement"):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDoWhileStatement"):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(MParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterForEachStatement"):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitForEachStatement"):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = MParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = MParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = MParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 733
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = MParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 734
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = MParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 735
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = MParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 736
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = MParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 737
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = MParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 738
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = MParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 739
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = MParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 740
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = MParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 741
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = MParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 742
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = MParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 743
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = MParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 744
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = MParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 745
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = MParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 746
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = MParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 747
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = MParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 748
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = MParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 749
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = MParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 750
                localctx.decl = self.comment_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Flush_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(MParser.FLUSH, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def getRuleIndex(self):
            return MParser.RULE_flush_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFlush_statement"):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlush_statement"):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = MParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self.match(MParser.FLUSH)
            self.state = 754
            self.match(MParser.LPAR)
            self.state = 755
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(MParser.DELETE, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(MParser.LPAR)
            else:
                return self.getToken(MParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(MParser.RPAR)
            else:
                return self.getToken(MParser.RPAR, i)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(MParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(MParser.STORE, 0)

        def AND(self):
            return self.getToken(MParser.AND, 0)

        def getRuleIndex(self):
            return MParser.RULE_store_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterStore_statement"):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStore_statement"):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = MParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_store_statement)
        try:
            self.state = 777
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 757
                self.match(MParser.DELETE)
                self.state = 758
                self.match(MParser.LPAR)
                self.state = 759
                localctx.to_del = self.expression_list()
                self.state = 760
                self.match(MParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 762
                self.match(MParser.STORE)
                self.state = 763
                self.match(MParser.LPAR)
                self.state = 764
                localctx.to_add = self.expression_list()
                self.state = 765
                self.match(MParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 767
                self.match(MParser.DELETE)
                self.state = 768
                self.match(MParser.LPAR)
                self.state = 769
                localctx.to_del = self.expression_list()
                self.state = 770
                self.match(MParser.RPAR)
                self.state = 771
                self.match(MParser.AND)
                self.state = 772
                self.match(MParser.STORE)
                self.state = 773
                self.match(MParser.LPAR)
                self.state = 774
                localctx.to_add = self.expression_list()
                self.state = 775
                self.match(MParser.RPAR)
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
            super(MParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(MParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_call

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_call"):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_call"):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = MParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            localctx.method = self.method_selector()
            self.state = 780
            self.match(MParser.LPAR)
            self.state = 782
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 781
                localctx.args = self.argument_assignment_list(0)


            self.state = 784
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(MParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Method_selectorContext)
            super(MParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(MParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodParent"):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodParent"):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Method_selectorContext)
            super(MParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodName"):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodName"):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = MParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_selector)
        try:
            self.state = 791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = MParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 786
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 787
                localctx.parent = self.callable_parent(0)
                self.state = 788
                self.match(MParser.DOT)
                self.state = 789
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
            super(MParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(MParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_parentContext)
            super(MParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(MParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(MParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableSelector"):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableSelector"):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_parentContext)
            super(MParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableRoot"):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableRoot"):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 794
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 800
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CallableSelectorContext(self, MParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 796
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 797
                    localctx.select = self.callable_selector() 
                self.state = 802
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(MParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_selectorContext)
            super(MParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableItemSelector"):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableItemSelector"):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_selectorContext)
            super(MParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableMemberSelector"):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableMemberSelector"):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = MParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callable_selector)
        try:
            self.state = 809
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 803
                self.match(MParser.DOT)
                self.state = 804
                localctx.name = self.variable_identifier()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 805
                self.match(MParser.LBRAK)
                self.state = 806
                localctx.exp = self.expression(0)
                self.state = 807
                self.match(MParser.RBRAK)
                pass
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
            super(MParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(MParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_resource_statement"):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_resource_statement"):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = MParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
            self.match(MParser.WITH)
            self.state = 812
            localctx.stmt = self.assign_variable_statement()
            self.state = 813
            self.match(MParser.COLON)
            self.state = 814
            self.indent()
            self.state = 815
            localctx.stmts = self.statement_list()
            self.state = 816
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
            super(MParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_singleton_statement"):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_singleton_statement"):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = MParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 818
            self.match(MParser.WITH)
            self.state = 819
            localctx.typ = self.type_identifier()
            self.state = 820
            self.match(MParser.COLON)
            self.state = 821
            self.indent()
            self.state = 822
            localctx.stmts = self.statement_list()
            self.state = 823
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
            super(MParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(MParser.SWITCH, 0)

        def ON(self):
            return self.getToken(MParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(MParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(MParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_switch_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_statement"):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_statement"):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = MParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 825
            self.match(MParser.SWITCH)
            self.state = 826
            self.match(MParser.ON)
            self.state = 827
            localctx.exp = self.expression(0)
            self.state = 828
            self.match(MParser.COLON)
            self.state = 829
            self.indent()
            self.state = 830
            localctx.cases = self.switch_case_statement_list()
            self.state = 838
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 831
                self.lfp()
                self.state = 832
                self.match(MParser.OTHERWISE)
                self.state = 833
                self.match(MParser.COLON)
                self.state = 834
                self.indent()
                self.state = 835
                localctx.stmts = self.statement_list()
                self.state = 836
                self.dedent()


            self.state = 840
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
            super(MParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(MParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Switch_case_statementContext)
            super(MParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(MParser.WHEN, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(MParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAtomicSwitchCase"):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomicSwitchCase"):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Switch_case_statementContext)
            super(MParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(MParser.WHEN, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(MParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCollectionSwitchCase"):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollectionSwitchCase"):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = MParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_switch_case_statement)
        try:
            self.state = 857
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = MParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 842
                self.match(MParser.WHEN)
                self.state = 843
                localctx.exp = self.atomic_literal()
                self.state = 844
                self.match(MParser.COLON)
                self.state = 845
                self.indent()
                self.state = 846
                localctx.stmts = self.statement_list()
                self.state = 847
                self.dedent()
                pass

            elif la_ == 2:
                localctx = MParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 849
                self.match(MParser.WHEN)
                self.state = 850
                self.match(MParser.IN)
                self.state = 851
                localctx.exp = self.literal_collection()
                self.state = 852
                self.match(MParser.COLON)
                self.state = 853
                self.indent()
                self.state = 854
                localctx.stmts = self.statement_list()
                self.state = 855
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
            super(MParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(MParser.FOR, 0)

        def IN(self):
            return self.getToken(MParser.IN, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def getRuleIndex(self):
            return MParser.RULE_for_each_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFor_each_statement"):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFor_each_statement"):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = MParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 859
            self.match(MParser.FOR)
            self.state = 860
            localctx.name1 = self.variable_identifier()
            self.state = 863
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.COMMA:
                self.state = 861
                self.match(MParser.COMMA)
                self.state = 862
                localctx.name2 = self.variable_identifier()


            self.state = 865
            self.match(MParser.IN)
            self.state = 866
            localctx.source = self.expression(0)
            self.state = 867
            self.match(MParser.COLON)
            self.state = 868
            self.indent()
            self.state = 869
            localctx.stmts = self.statement_list()
            self.state = 870
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
            super(MParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(MParser.DO, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(MParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_do_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterDo_while_statement"):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDo_while_statement"):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = MParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 872
            self.match(MParser.DO)
            self.state = 873
            self.match(MParser.COLON)
            self.state = 874
            self.indent()
            self.state = 875
            localctx.stmts = self.statement_list()
            self.state = 876
            self.dedent()
            self.state = 877
            self.lfp()
            self.state = 878
            self.match(MParser.WHILE)
            self.state = 879
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
            super(MParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(MParser.WHILE, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWhile_statement"):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhile_statement"):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = MParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self.match(MParser.WHILE)
            self.state = 882
            localctx.exp = self.expression(0)
            self.state = 883
            self.match(MParser.COLON)
            self.state = 884
            self.indent()
            self.state = 885
            localctx.stmts = self.statement_list()
            self.state = 886
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
            super(MParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(MParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(MParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(MParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_if_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterIf_statement"):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf_statement"):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = MParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 888
            self.match(MParser.IF)
            self.state = 889
            localctx.exp = self.expression(0)
            self.state = 890
            self.match(MParser.COLON)
            self.state = 891
            self.indent()
            self.state = 892
            localctx.stmts = self.statement_list()
            self.state = 893
            self.dedent()
            self.state = 897
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 894
                self.lfp()
                self.state = 895
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 906
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 899
                self.lfp()
                self.state = 900
                self.match(MParser.ELSE)
                self.state = 901
                self.match(MParser.COLON)
                self.state = 902
                self.indent()
                self.state = 903
                localctx.elseStmts = self.statement_list()
                self.state = 904
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
            super(MParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(MParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Else_if_statement_listContext)
            super(MParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)
        def IF(self):
            return self.getToken(MParser.IF, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementList"):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementList"):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Else_if_statement_listContext)
            super(MParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)
        def IF(self):
            return self.getToken(MParser.IF, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(MParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementListItem"):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementListItem"):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 909
            self.match(MParser.ELSE)
            self.state = 910
            self.match(MParser.IF)
            self.state = 911
            localctx.exp = self.expression(0)
            self.state = 912
            self.match(MParser.COLON)
            self.state = 913
            self.indent()
            self.state = 914
            localctx.stmts = self.statement_list()
            self.state = 915
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 929
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ElseIfStatementListItemContext(self, MParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 917
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 918
                    self.lfp()
                    self.state = 919
                    self.match(MParser.ELSE)
                    self.state = 920
                    self.match(MParser.IF)
                    self.state = 921
                    localctx.exp = self.expression(0)
                    self.state = 922
                    self.match(MParser.COLON)
                    self.state = 923
                    self.indent()
                    self.state = 924
                    localctx.stmts = self.statement_list()
                    self.state = 925
                    self.dedent() 
                self.state = 931
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(MParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_raise_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterRaise_statement"):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaise_statement"):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = MParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 932
            self.match(MParser.RAISE)
            self.state = 933
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
            super(MParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(MParser.TRY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfsContext)
            else:
                return self.getTypedRuleContext(MParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(MParser.Statement_listContext,i)


        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)

        def FINALLY(self):
            return self.getToken(MParser.FINALLY, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(MParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_try_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterTry_statement"):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTry_statement"):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = MParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 935
            self.match(MParser.TRY)
            self.state = 936
            localctx.name = self.variable_identifier()
            self.state = 937
            self.match(MParser.COLON)
            self.state = 938
            self.indent()
            self.state = 939
            localctx.stmts = self.statement_list()
            self.state = 940
            self.dedent()
            self.state = 941
            self.lfs()
            self.state = 943
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 942
                localctx.handlers = self.catch_statement_list()


            self.state = 952
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EXCEPT:
                self.state = 945
                self.match(MParser.EXCEPT)
                self.state = 946
                self.match(MParser.COLON)
                self.state = 947
                self.indent()
                self.state = 948
                localctx.anyStmts = self.statement_list()
                self.state = 949
                self.dedent()
                self.state = 950
                self.lfs()


            self.state = 961
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.FINALLY:
                self.state = 954
                self.match(MParser.FINALLY)
                self.state = 955
                self.match(MParser.COLON)
                self.state = 956
                self.indent()
                self.state = 957
                localctx.finalStmts = self.statement_list()
                self.state = 958
                self.dedent()
                self.state = 959
                self.lfs()


            self.state = 963
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
            super(MParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(MParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Catch_statementContext)
            super(MParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(MParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchAtomicStatement"):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchAtomicStatement"):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Catch_statementContext)
            super(MParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(MParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(MParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchCollectionStatement"):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchCollectionStatement"):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = MParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_catch_statement)
        try:
            self.state = 984
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = MParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 965
                self.match(MParser.EXCEPT)
                self.state = 966
                localctx.name = self.symbol_identifier()
                self.state = 967
                self.match(MParser.COLON)
                self.state = 968
                self.indent()
                self.state = 969
                localctx.stmts = self.statement_list()
                self.state = 970
                self.dedent()
                self.state = 971
                self.lfs()
                pass

            elif la_ == 2:
                localctx = MParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 973
                self.match(MParser.EXCEPT)
                self.state = 974
                self.match(MParser.IN)
                self.state = 975
                self.match(MParser.LBRAK)
                self.state = 976
                localctx.exp = self.symbol_list()
                self.state = 977
                self.match(MParser.RBRAK)
                self.state = 978
                self.match(MParser.COLON)
                self.state = 979
                self.indent()
                self.state = 980
                localctx.stmts = self.statement_list()
                self.state = 981
                self.dedent()
                self.state = 982
                self.lfs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MParser.BREAK, 0)

        def getRuleIndex(self):
            return MParser.RULE_break_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterBreak_statement"):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreak_statement"):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = MParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 986
            self.match(MParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_return_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterReturn_statement"):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturn_statement"):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = MParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 988
            self.match(MParser.RETURN)
            self.state = 990
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 989
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
            super(MParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(MParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(MParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIntDivideExpression"):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntDivideExpression"):
                listener.exitIntDivideExpression(self)


    class HasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.HasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ANY(self):
            return self.getToken(MParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAnyExpression"):
                listener.enterHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAnyExpression"):
                listener.exitHasAnyExpression(self)


    class HasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.HasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasExpression"):
                listener.enterHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasExpression"):
                listener.exitHasExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MParser.IF, 0)
        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterTernaryExpression"):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTernaryExpression"):
                listener.exitTernaryExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(MParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotEqualsExpression"):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotEqualsExpression"):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterInExpression"):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInExpression"):
                listener.exitInExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotExpression"):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotExpression"):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(MParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanExpression"):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanExpression"):
                listener.exitGreaterThanExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(MParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOrExpression"):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrExpression"):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(MParser.CODE, 0)
        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeExpression"):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeExpression"):
                listener.exitCodeExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(MParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanOrEqualExpression"):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanOrEqualExpression"):
                listener.exitLessThanOrEqualExpression(self)


    class NotHasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotHasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ANY(self):
            return self.getToken(MParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAnyExpression"):
                listener.enterNotHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAnyExpression"):
                listener.exitNotHasAnyExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(MParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndExpression"):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndExpression"):
                listener.exitAndExpression(self)


    class NotHasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotHasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasExpression"):
                listener.enterNotHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasExpression"):
                listener.exitNotHasExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(MParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureExpression"):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureExpression"):
                listener.exitClosureExpression(self)


    class NotHasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotHasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAllExpression"):
                listener.enterNotHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAllExpression"):
                listener.exitNotHasAllExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterContainsExpression"):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContainsExpression"):
                listener.exitContainsExpression(self)


    class FilteredListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.FilteredListExpressionContext, self).__init__(parser)
            self.src = None # ExpressionContext
            self.copyFrom(ctx)

        def filtered_list_suffix(self):
            return self.getTypedRuleContext(MParser.Filtered_list_suffixContext,0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFilteredListExpression"):
                listener.enterFilteredListExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFilteredListExpression"):
                listener.exitFilteredListExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotContainsExpression"):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotContainsExpression"):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(MParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterMultiplyExpression"):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiplyExpression"):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(MParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterRoughlyEqualsExpression"):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRoughlyEqualsExpression"):
                listener.exitRoughlyEqualsExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(MParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExecuteExpression"):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExecuteExpression"):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(MParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodExpression"):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodExpression"):
                listener.exitMethodExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(MParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanOrEqualExpression"):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanOrEqualExpression"):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotInExpression"):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotInExpression"):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(MParser.FOR, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorExpression"):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorExpression"):
                listener.exitIteratorExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(MParser.IS, 0)
        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(MParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsNotExpression"):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotExpression"):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(MParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterDivideExpression"):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivideExpression"):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(MParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(MParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsExpression"):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsExpression"):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMinusExpression"):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinusExpression"):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(MParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAddExpression"):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddExpression"):
                listener.exitAddExpression(self)


    class HasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.HasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAllExpression"):
                listener.enterHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAllExpression"):
                listener.exitHasAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(MParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterInstanceExpression"):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInstanceExpression"):
                listener.exitInstanceExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(MParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCastExpression"):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCastExpression"):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(MParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterModuloExpression"):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModuloExpression"):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(MParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanExpression"):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanExpression"):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(MParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterEqualsExpression"):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEqualsExpression"):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1010
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = MParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 993
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 994
                localctx.exp = self.method_expression()
                pass

            elif la_ == 3:
                localctx = MParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 995
                self.match(MParser.MINUS)
                self.state = 996
                localctx.exp = self.expression(34)
                pass

            elif la_ == 4:
                localctx = MParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 997
                self.match(MParser.NOT)
                self.state = 998
                localctx.exp = self.expression(33)
                pass

            elif la_ == 5:
                localctx = MParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 999
                self.match(MParser.CODE)
                self.state = 1000
                self.match(MParser.LPAR)
                self.state = 1001
                localctx.exp = self.expression(0)
                self.state = 1002
                self.match(MParser.RPAR)
                pass

            elif la_ == 6:
                localctx = MParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1004
                self.match(MParser.EXECUTE)
                self.state = 1005
                self.match(MParser.LPAR)
                self.state = 1006
                localctx.name = self.variable_identifier()
                self.state = 1007
                self.match(MParser.RPAR)
                pass

            elif la_ == 7:
                localctx = MParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1009
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = MParser.MultiplyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1012
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1013
                        self.multiply()
                        self.state = 1014
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 2:
                        localctx = MParser.DivideExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1016
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1017
                        self.divide()
                        self.state = 1018
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 3:
                        localctx = MParser.ModuloExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1020
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1021
                        self.modulo()
                        self.state = 1022
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 4:
                        localctx = MParser.IntDivideExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1024
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1025
                        self.idivide()
                        self.state = 1026
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 5:
                        localctx = MParser.AddExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1028
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1029
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MParser.PLUS or _la==MParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 1030
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 6:
                        localctx = MParser.LessThanExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1031
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1032
                        self.match(MParser.LT)
                        self.state = 1033
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 7:
                        localctx = MParser.LessThanOrEqualExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1034
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1035
                        self.match(MParser.LTE)
                        self.state = 1036
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 8:
                        localctx = MParser.GreaterThanExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1037
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1038
                        self.match(MParser.GT)
                        self.state = 1039
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 9:
                        localctx = MParser.GreaterThanOrEqualExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1040
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1041
                        self.match(MParser.GTE)
                        self.state = 1042
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 10:
                        localctx = MParser.EqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1043
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1044
                        self.match(MParser.EQ2)
                        self.state = 1045
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 11:
                        localctx = MParser.NotEqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1046
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1047
                        self.match(MParser.XEQ)
                        self.state = 1048
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 12:
                        localctx = MParser.RoughlyEqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1049
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1050
                        self.match(MParser.TEQ)
                        self.state = 1051
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 13:
                        localctx = MParser.ContainsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1052
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1053
                        self.match(MParser.CONTAINS)
                        self.state = 1054
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 14:
                        localctx = MParser.InExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1055
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1056
                        self.match(MParser.IN)
                        self.state = 1057
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 15:
                        localctx = MParser.HasExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1058
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1059
                        self.match(MParser.HAS)
                        self.state = 1060
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 16:
                        localctx = MParser.HasAllExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1061
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1062
                        self.match(MParser.HAS)
                        self.state = 1063
                        self.match(MParser.ALL)
                        self.state = 1064
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 17:
                        localctx = MParser.HasAnyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1065
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1066
                        self.match(MParser.HAS)
                        self.state = 1067
                        self.match(MParser.ANY)
                        self.state = 1068
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 18:
                        localctx = MParser.NotContainsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1069
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1070
                        self.match(MParser.NOT)
                        self.state = 1071
                        self.match(MParser.CONTAINS)
                        self.state = 1072
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 19:
                        localctx = MParser.NotInExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1073
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1074
                        self.match(MParser.NOT)
                        self.state = 1075
                        self.match(MParser.IN)
                        self.state = 1076
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 20:
                        localctx = MParser.NotHasExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1077
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1078
                        self.match(MParser.NOT)
                        self.state = 1079
                        self.match(MParser.HAS)
                        self.state = 1080
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 21:
                        localctx = MParser.NotHasAllExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1081
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1082
                        self.match(MParser.NOT)
                        self.state = 1083
                        self.match(MParser.HAS)
                        self.state = 1084
                        self.match(MParser.ALL)
                        self.state = 1085
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 22:
                        localctx = MParser.NotHasAnyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1086
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1087
                        self.match(MParser.NOT)
                        self.state = 1088
                        self.match(MParser.HAS)
                        self.state = 1089
                        self.match(MParser.ANY)
                        self.state = 1090
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 23:
                        localctx = MParser.OrExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1091
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1092
                        self.match(MParser.OR)
                        self.state = 1093
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 24:
                        localctx = MParser.AndExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1094
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1095
                        self.match(MParser.AND)
                        self.state = 1096
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 25:
                        localctx = MParser.TernaryExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1097
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1098
                        self.match(MParser.IF)
                        self.state = 1099
                        localctx.test = self.expression(0)
                        self.state = 1100
                        self.match(MParser.ELSE)
                        self.state = 1101
                        localctx.ifFalse = self.expression(6)
                        pass

                    elif la_ == 26:
                        localctx = MParser.IteratorExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1103
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1104
                        self.match(MParser.FOR)
                        self.state = 1105
                        localctx.name = self.variable_identifier()
                        self.state = 1106
                        self.match(MParser.IN)
                        self.state = 1107
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 27:
                        localctx = MParser.FilteredListExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.src = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1109
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 1110
                        self.filtered_list_suffix()
                        pass

                    elif la_ == 28:
                        localctx = MParser.CastExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1111
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1112
                        self.match(MParser.AS)
                        self.state = 1113
                        localctx.right = self.category_or_any_type()
                        pass

                    elif la_ == 29:
                        localctx = MParser.IsNotExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1114
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1115
                        self.match(MParser.IS)
                        self.state = 1116
                        self.match(MParser.NOT)
                        self.state = 1117
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 30:
                        localctx = MParser.IsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1118
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1119
                        self.match(MParser.IS)
                        self.state = 1120
                        localctx.right = self.is_expression()
                        pass

             
                self.state = 1125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_closure_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterClosure_expression"):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosure_expression"):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = MParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1126
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
            super(MParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(MParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_expressionContext)
            super(MParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(MParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(MParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectorExpression"):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectorExpression"):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_expressionContext)
            super(MParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(MParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectableExpression"):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectableExpression"):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1129
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.SelectorExpressionContext(self, MParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1131
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1132
                    localctx.selector = self.instance_selector() 
                self.state = 1137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blob_expression(self):
            return self.getTypedRuleContext(MParser.Blob_expressionContext,0)


        def document_expression(self):
            return self.getTypedRuleContext(MParser.Document_expressionContext,0)


        def fetch_store_expression(self):
            return self.getTypedRuleContext(MParser.Fetch_store_expressionContext,0)


        def read_all_expression(self):
            return self.getTypedRuleContext(MParser.Read_all_expressionContext,0)


        def read_one_expression(self):
            return self.getTypedRuleContext(MParser.Read_one_expressionContext,0)


        def sorted_expression(self):
            return self.getTypedRuleContext(MParser.Sorted_expressionContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MParser.Method_callContext,0)


        def constructor_expression(self):
            return self.getTypedRuleContext(MParser.Constructor_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_expression"):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_expression"):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = MParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_method_expression)
        try:
            self.state = 1146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1138
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1139
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1140
                self.fetch_store_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1141
                self.read_all_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1142
                self.read_one_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1143
                self.sorted_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1144
                self.method_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1145
                self.constructor_expression()
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
            super(MParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(MParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_selectorContext)
            super(MParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(MParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceSelector"):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceSelector"):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_selectorContext)
            super(MParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberSelector"):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberSelector"):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_selectorContext)
            super(MParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemSelector"):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemSelector"):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = MParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance_selector)
        try:
            self.state = 1161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = MParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1148
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1149
                self.match(MParser.DOT)
                self.state = 1150
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1151
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1152
                self.match(MParser.LBRAK)
                self.state = 1153
                localctx.xslice = self.slice_arguments()
                self.state = 1154
                self.match(MParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = MParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1156
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1157
                self.match(MParser.LBRAK)
                self.state = 1158
                localctx.exp = self.expression(0)
                self.state = 1159
                self.match(MParser.RBRAK)
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
            super(MParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(MParser.BLOB, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_blob_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterBlob_expression"):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlob_expression"):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = MParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_blob_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163
            self.match(MParser.BLOB)
            self.state = 1164
            self.match(MParser.LPAR)
            self.state = 1166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1165
                self.expression(0)


            self.state = 1168
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(MParser.DOCUMENT, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_document_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterDocument_expression"):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocument_expression"):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = MParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1170
            self.match(MParser.DOCUMENT)
            self.state = 1171
            self.match(MParser.LPAR)
            self.state = 1173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1172
                self.expression(0)


            self.state = 1175
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(MParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Constructor_expressionContext)
            super(MParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.copyExp = None # Copy_fromContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)

        def copy_from(self):
            return self.getTypedRuleContext(MParser.Copy_fromContext,0)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorFrom"):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorFrom"):
                listener.exitConstructorFrom(self)


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Constructor_expressionContext)
            super(MParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorNoFrom"):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorNoFrom"):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = MParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = MParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1177
                localctx.typ = self.mutable_category_type()
                self.state = 1178
                self.match(MParser.LPAR)
                self.state = 1179
                localctx.copyExp = self.copy_from()
                self.state = 1182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.COMMA:
                    self.state = 1180
                    self.match(MParser.COMMA)
                    self.state = 1181
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1184
                self.match(MParser.RPAR)
                pass

            elif la_ == 2:
                localctx = MParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1186
                localctx.typ = self.mutable_category_type()
                self.state = 1187
                self.match(MParser.LPAR)
                self.state = 1189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                    self.state = 1188
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1191
                self.match(MParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Copy_fromContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Copy_fromContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_copy_from

        def enterRule(self, listener):
            if hasattr(listener, "enterCopy_from"):
                listener.enterCopy_from(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCopy_from"):
                listener.exitCopy_from(self)




    def copy_from(self):

        localctx = MParser.Copy_fromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_copy_from)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1195
            self.match(MParser.FROM)
            self.state = 1196
            self.assign()
            self.state = 1197
            localctx.exp = self.expression(0)
            self.state = 1198
            if not self.willNotBe(self.equalToken()):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(MParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExpressionAssignmentList"):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpressionAssignmentList"):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(MParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentList"):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentList"):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(MParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentListItem"):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListItem"):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = MParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1201
                localctx.exp = self.expression(0)
                self.state = 1202
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = MParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1204
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ArgumentAssignmentListItemContext(self, MParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1207
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1208
                    self.match(MParser.COMMA)
                    self.state = 1209
                    localctx.item = self.argument_assignment() 
                self.state = 1214
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
            super(MParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_argument_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_assignment"):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_assignment"):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = MParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1215
            localctx.name = self.variable_identifier()
            self.state = 1219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 1216
                self.assign()
                self.state = 1217
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TO(self):
            return self.getToken(MParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MParser.RULE_write_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWrite_statement"):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWrite_statement"):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = MParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1221
            self.match(MParser.WRITE)
            self.state = 1222
            localctx.what = self.expression(0)
            self.state = 1223
            self.match(MParser.TO)
            self.state = 1224
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filtered_list_suffixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Filtered_list_suffixContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.predicate = None # ExpressionContext

        def FILTERED(self):
            return self.getToken(MParser.FILTERED, 0)

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_filtered_list_suffix

        def enterRule(self, listener):
            if hasattr(listener, "enterFiltered_list_suffix"):
                listener.enterFiltered_list_suffix(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFiltered_list_suffix"):
                listener.exitFiltered_list_suffix(self)




    def filtered_list_suffix(self):

        localctx = MParser.Filtered_list_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_filtered_list_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1226
            self.match(MParser.FILTERED)
            self.state = 1227
            self.match(MParser.WITH)
            self.state = 1228
            localctx.name = self.variable_identifier()
            self.state = 1229
            self.match(MParser.WHERE)
            self.state = 1230
            localctx.predicate = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_store_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(MParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Fetch_store_expressionContext)
            super(MParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(MParser.FETCH, 0)
        def ONE(self):
            return self.getToken(MParser.ONE, 0)
        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchOne"):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchOne"):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Fetch_store_expressionContext)
            super(MParser.FetchManyContext, self).__init__(parser)
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(MParser.FETCH, 0)
        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def ROWS(self):
            return self.getToken(MParser.ROWS, 0)
        def TO(self):
            return self.getToken(MParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)

        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)
        def ORDER(self):
            return self.getToken(MParser.ORDER, 0)
        def BY(self):
            return self.getToken(MParser.BY, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)

        def order_by_list(self):
            return self.getTypedRuleContext(MParser.Order_by_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchMany"):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchMany"):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = MParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                localctx = MParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1232
                self.match(MParser.FETCH)
                self.state = 1233
                self.match(MParser.ONE)
                self.state = 1235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE or _la==MParser.TYPE_IDENTIFIER:
                    self.state = 1234
                    localctx.typ = self.mutable_category_type()


                self.state = 1237
                self.match(MParser.WHERE)
                self.state = 1238
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1239
                self.match(MParser.FETCH)
                self.state = 1246
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MParser.ALL]:
                    self.state = 1240
                    self.match(MParser.ALL)
                    pass
                elif token in [MParser.ROWS]:
                    self.state = 1241
                    self.match(MParser.ROWS)
                    self.state = 1242
                    localctx.xstart = self.expression(0)
                    self.state = 1243
                    self.match(MParser.TO)
                    self.state = 1244
                    localctx.xstop = self.expression(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1248
                self.match(MParser.LPAR)
                self.state = 1250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE or _la==MParser.TYPE_IDENTIFIER:
                    self.state = 1249
                    localctx.typ = self.mutable_category_type()


                self.state = 1252
                self.match(MParser.RPAR)
                self.state = 1255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 1253
                    self.match(MParser.WHERE)
                    self.state = 1254
                    localctx.predicate = self.expression(0)


                self.state = 1260
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                if la_ == 1:
                    self.state = 1257
                    self.match(MParser.ORDER)
                    self.state = 1258
                    self.match(MParser.BY)
                    self.state = 1259
                    localctx.orderby = self.order_by_list()


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
            super(MParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(MParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(MParser.Instance_expressionContext,i)


        def DESC(self):
            return self.getToken(MParser.DESC, 0)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(MParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def getRuleIndex(self):
            return MParser.RULE_sorted_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterSorted_expression"):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSorted_expression"):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = MParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1264
            self.match(MParser.SORTED)
            self.state = 1266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.DESC:
                self.state = 1265
                self.match(MParser.DESC)


            self.state = 1268
            self.match(MParser.LPAR)
            self.state = 1269
            localctx.source = self.instance_expression(0)
            self.state = 1275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.COMMA:
                self.state = 1270
                self.match(MParser.COMMA)
                self.state = 1271
                self.key_token()
                self.state = 1272
                self.match(MParser.EQ)
                self.state = 1273
                localctx.key = self.instance_expression(0)


            self.state = 1277
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(MParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_instance_statement"):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_instance_statement"):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = MParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1279
            localctx.inst = self.assignable_instance(0)
            self.state = 1280
            self.assign()
            self.state = 1281
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
            super(MParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(MParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Child_instanceContext)
            super(MParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberInstance"):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberInstance"):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Child_instanceContext)
            super(MParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemInstance"):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemInstance"):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = MParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_child_instance)
        try:
            self.state = 1291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = MParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1283
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1284
                self.match(MParser.DOT)
                self.state = 1285
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1286
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1287
                self.match(MParser.LBRAK)
                self.state = 1288
                localctx.exp = self.expression(0)
                self.state = 1289
                self.match(MParser.RBRAK)
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
            super(MParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(MParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_tuple_statement"):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_tuple_statement"):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = MParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1293
            localctx.items = self.variable_identifier_list()
            self.state = 1294
            self.assign()
            self.state = 1295
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
            super(MParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_lfs

        def enterRule(self, listener):
            if hasattr(listener, "enterLfs"):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfs"):
                listener.exitLfs(self)




    def lfs(self):

        localctx = MParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1297
                    self.match(MParser.LF) 
                self.state = 1302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_lfp

        def enterRule(self, listener):
            if hasattr(listener, "enterLfp"):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfp"):
                listener.exitLfp(self)




    def lfp(self):

        localctx = MParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1304 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1303
                self.match(MParser.LF)
                self.state = 1306 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MParser.LF):
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
            super(MParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(MParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_indent

        def enterRule(self, listener):
            if hasattr(listener, "enterIndent"):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIndent"):
                listener.exitIndent(self)




    def indent(self):

        localctx = MParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1309 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1308
                self.match(MParser.LF)
                self.state = 1311 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MParser.LF):
                    break

            self.state = 1313
            self.match(MParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(MParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_dedent

        def enterRule(self, listener):
            if hasattr(listener, "enterDedent"):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDedent"):
                listener.exitDedent(self)




    def dedent(self):

        localctx = MParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.LF:
                self.state = 1315
                self.match(MParser.LF)
                self.state = 1320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1321
            self.match(MParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def getRuleIndex(self):
            return MParser.RULE_null_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterNull_literal"):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNull_literal"):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = MParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1323
            self.match(MParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(MParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Declaration_listContext)
            super(MParser.FullDeclarationListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(MParser.LfsContext,0)

        def EOF(self):
            return self.getToken(MParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(MParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFullDeclarationList"):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFullDeclarationList"):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = MParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = MParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.COMMENT or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (MParser.ABSTRACT - 68)) | (1 << (MParser.ATTR - 68)) | (1 << (MParser.CATEGORY - 68)) | (1 << (MParser.CLASS - 68)) | (1 << (MParser.DEF - 68)) | (1 << (MParser.ENUM - 68)) | (1 << (MParser.NATIVE - 68)))) != 0) or _la==MParser.SINGLETON or _la==MParser.STORABLE:
                self.state = 1325
                self.declarations()


            self.state = 1328
            self.lfs()
            self.state = 1329
            self.match(MParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_declarations

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclarations"):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclarations"):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = MParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1331
            self.declaration()
            self.state = 1337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1332
                    self.lfp()
                    self.state = 1333
                    self.declaration() 
                self.state = 1339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(MParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(MParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(MParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(MParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(MParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = MParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMENT:
                self.state = 1340
                self.comment_statement()
                self.state = 1341
                self.lfp()
                self.state = 1347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.state = 1348
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1349
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1350
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1351
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1352
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
            super(MParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(MParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterResource_declaration"):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResource_declaration"):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = MParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1355
            self.native_resource_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(MParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(MParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_enum_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_declaration"):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_declaration"):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = MParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_enum_declaration)
        try:
            self.state = 1359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1357
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1358
                self.enum_native_declaration()
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
            super(MParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(MParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol_list"):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol_list"):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = MParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1361
            self.native_symbol()
            self.state = 1367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1362
                    self.lfp()
                    self.state = 1363
                    self.native_symbol() 
                self.state = 1369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(MParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol_list"):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol_list"):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = MParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1370
            self.category_symbol()
            self.state = 1376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1371
                    self.lfp()
                    self.state = 1372
                    self.category_symbol() 
                self.state = 1378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_list"):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_list"):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = MParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1379
            self.symbol_identifier()
            self.state = 1384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1380
                self.match(MParser.COMMA)
                self.state = 1381
                self.symbol_identifier()
                self.state = 1386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(MParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(MParser.Set_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingSet"):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingSet"):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(MParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingPattern"):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingPattern"):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(MParser.List_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingList"):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingList"):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(MParser.Range_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingRange"):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingRange"):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(MParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingExpression"):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingExpression"):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = MParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_attribute_constraint)
        try:
            self.state = 1397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                localctx = MParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1387
                self.match(MParser.IN)
                self.state = 1388
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = MParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1389
                self.match(MParser.IN)
                self.state = 1390
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = MParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1391
                self.match(MParser.IN)
                self.state = 1392
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = MParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1393
                self.match(MParser.MATCHING)
                self.state = 1394
                localctx.text = self.match(MParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = MParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1395
                self.match(MParser.MATCHING)
                self.state = 1396
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
            super(MParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterList_literal"):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList_literal"):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = MParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1399
                self.match(MParser.MUTABLE)


            self.state = 1402
            self.match(MParser.LBRAK)
            self.state = 1404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1403
                self.expression_list()


            self.state = 1406
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_set_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterSet_literal"):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSet_literal"):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = MParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1408
                self.match(MParser.MUTABLE)


            self.state = 1411
            self.match(MParser.LT)
            self.state = 1413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1412
                self.expression_list()


            self.state = 1415
            self.match(MParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_expression_list

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_list"):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_list"):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = MParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1417
            self.expression(0)
            self.state = 1422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1418
                self.match(MParser.COMMA)
                self.state = 1419
                self.expression(0)
                self.state = 1424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(MParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MParser.RULE_range_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterRange_literal"):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_literal"):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = MParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1425
            self.match(MParser.LBRAK)
            self.state = 1426
            localctx.low = self.expression(0)
            self.state = 1427
            self.match(MParser.RANGE)
            self.state = 1428
            localctx.high = self.expression(0)
            self.state = 1429
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(MParser.TypedefContext, self).copyFrom(ctx)


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(MParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(MParser.LT, 0)
        def GT(self):
            return self.getToken(MParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorType"):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorType"):
                listener.exitIteratorType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(MParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSetType"):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetType"):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterListType"):
                listener.enterListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitListType"):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDictType"):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDictType"):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(MParser.CURSOR, 0)
        def LT(self):
            return self.getToken(MParser.LT, 0)
        def GT(self):
            return self.getToken(MParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCursorType"):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCursorType"):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(MParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPrimaryType"):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrimaryType"):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 162
        self.enterRecursionRule(localctx, 162, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.TYPE_IDENTIFIER]:
                localctx = MParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1432
                localctx.p = self.primary_type()
                pass
            elif token in [MParser.CURSOR]:
                localctx = MParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1433
                self.match(MParser.CURSOR)
                self.state = 1434
                self.match(MParser.LT)
                self.state = 1435
                localctx.c = self.typedef(0)
                self.state = 1436
                self.match(MParser.GT)
                pass
            elif token in [MParser.ITERATOR]:
                localctx = MParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1438
                self.match(MParser.ITERATOR)
                self.state = 1439
                self.match(MParser.LT)
                self.state = 1440
                localctx.i = self.typedef(0)
                self.state = 1441
                self.match(MParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1453
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
                    if la_ == 1:
                        localctx = MParser.SetTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1445
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1446
                        self.match(MParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = MParser.ListTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1447
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1448
                        self.match(MParser.LBRAK)
                        self.state = 1449
                        self.match(MParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = MParser.DictTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1450
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1451
                        self.match(MParser.LCURL)
                        self.state = 1452
                        self.match(MParser.RCURL)
                        pass

             
                self.state = 1457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(MParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Primary_typeContext)
            super(MParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(MParser.Native_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeType"):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeType"):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Primary_typeContext)
            super(MParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(MParser.Category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCategoryType"):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategoryType"):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = MParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_primary_type)
        try:
            self.state = 1460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID]:
                localctx = MParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1458
                localctx.n = self.native_type()
                pass
            elif token in [MParser.TYPE_IDENTIFIER]:
                localctx = MParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1459
                localctx.c = self.category_type()
                pass
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
            super(MParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(MParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodType"):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodType"):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanType"):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanType"):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(MParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDocumentType"):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocumentType"):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterType"):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterType"):
                listener.exitCharacterType(self)


    class VersionTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.VersionTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionType"):
                listener.enterVersionType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionType"):
                listener.exitVersionType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextType"):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextType"):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(MParser.IMAGE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterImageType"):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImageType"):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeType"):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeType"):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerType"):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerType"):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeType"):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeType"):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(MParser.BLOB, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBlobType"):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlobType"):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDType"):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDType"):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalType"):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalType"):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(MParser.CODE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCodeType"):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeType"):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateType"):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateType"):
                listener.exitDateType(self)



    def native_type(self):

        localctx = MParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_native_type)
        try:
            self.state = 1477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN]:
                localctx = MParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1462
                self.match(MParser.BOOLEAN)
                pass
            elif token in [MParser.CHARACTER]:
                localctx = MParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1463
                self.match(MParser.CHARACTER)
                pass
            elif token in [MParser.TEXT]:
                localctx = MParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1464
                self.match(MParser.TEXT)
                pass
            elif token in [MParser.IMAGE]:
                localctx = MParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1465
                self.match(MParser.IMAGE)
                pass
            elif token in [MParser.INTEGER]:
                localctx = MParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1466
                self.match(MParser.INTEGER)
                pass
            elif token in [MParser.DECIMAL]:
                localctx = MParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1467
                self.match(MParser.DECIMAL)
                pass
            elif token in [MParser.DOCUMENT]:
                localctx = MParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1468
                self.match(MParser.DOCUMENT)
                pass
            elif token in [MParser.DATE]:
                localctx = MParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1469
                self.match(MParser.DATE)
                pass
            elif token in [MParser.DATETIME]:
                localctx = MParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1470
                self.match(MParser.DATETIME)
                pass
            elif token in [MParser.TIME]:
                localctx = MParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1471
                self.match(MParser.TIME)
                pass
            elif token in [MParser.PERIOD]:
                localctx = MParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1472
                self.match(MParser.PERIOD)
                pass
            elif token in [MParser.VERSION]:
                localctx = MParser.VersionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1473
                self.match(MParser.VERSION)
                pass
            elif token in [MParser.CODE]:
                localctx = MParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1474
                self.match(MParser.CODE)
                pass
            elif token in [MParser.BLOB]:
                localctx = MParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1475
                self.match(MParser.BLOB)
                pass
            elif token in [MParser.UUID]:
                localctx = MParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1476
                self.match(MParser.UUID)
                pass
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
            super(MParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_type"):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_type"):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = MParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
            localctx.t1 = self.match(MParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(MParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def getRuleIndex(self):
            return MParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterMutable_category_type"):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMutable_category_type"):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = MParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1481
                self.match(MParser.MUTABLE)


            self.state = 1484
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
            super(MParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(MParser.CODE, 0)

        def getRuleIndex(self):
            return MParser.RULE_code_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_type"):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_type"):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = MParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1486
            localctx.t1 = self.match(MParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(MParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConcreteCategoryDeclaration"):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteCategoryDeclaration"):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(MParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryDeclaration"):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryDeclaration"):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(MParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingletonCategoryDeclaration"):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingletonCategoryDeclaration"):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = MParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_category_declaration)
        try:
            self.state = 1491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                localctx = MParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1488
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = MParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1489
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = MParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1490
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
            super(MParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier_list"):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier_list"):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = MParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_type_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1493
            self.type_identifier()
            self.state = 1498
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,98,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1494
                    self.match(MParser.COMMA)
                    self.state = 1495
                    self.type_identifier() 
                self.state = 1500
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,98,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_identifier"):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_identifier"):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = MParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_method_identifier)
        try:
            self.state = 1503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1501
                self.variable_identifier()
                pass
            elif token in [MParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1502
                self.type_identifier()
                pass
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
            super(MParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(MParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTypeIdentifier"):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTypeIdentifier"):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSymbolIdentifier"):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbolIdentifier"):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterVariableIdentifier"):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableIdentifier"):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = MParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_identifier)
        try:
            self.state = 1508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1505
                self.variable_identifier()
                pass
            elif token in [MParser.TYPE_IDENTIFIER]:
                localctx = MParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1506
                self.type_identifier()
                pass
            elif token in [MParser.SYMBOL_IDENTIFIER]:
                localctx = MParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1507
                self.symbol_identifier()
                pass
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
            super(MParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_variable_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier"):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier"):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = MParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1510
            self.match(MParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def getRuleIndex(self):
            return MParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier"):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier"):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = MParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1512
            _la = self._input.LA(1)
            if not(_la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
            super(MParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_type_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier"):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier"):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = MParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1514
            self.match(MParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_identifier"):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_identifier"):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = MParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1516
            self.match(MParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(MParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_argument_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_list"):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_list"):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = MParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1518
            self.argument()
            self.state = 1523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1519
                self.match(MParser.COMMA)
                self.state = 1520
                self.argument()
                self.state = 1525
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(MParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a MParser.ArgumentContext)
            super(MParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(MParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorArgument"):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorArgument"):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a MParser.ArgumentContext)
            super(MParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(MParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeArgument"):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeArgument"):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = MParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.CODE]:
                localctx = MParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1526
                localctx.arg = self.code_argument()
                pass
            elif token in [MParser.MUTABLE, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1528
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE:
                    self.state = 1527
                    self.match(MParser.MUTABLE)


                self.state = 1530
                localctx.arg = self.operator_argument()
                pass
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
            super(MParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def named_argument(self):
            return self.getTypedRuleContext(MParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(MParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return MParser.RULE_operator_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_argument"):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_argument"):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = MParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_operator_argument)
        try:
            self.state = 1535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1533
                self.named_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1534
                self.typed_argument()
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
            super(MParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_named_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterNamed_argument"):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNamed_argument"):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = MParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1537
            self.variable_identifier()
            self.state = 1540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 1538
                self.match(MParser.EQ)
                self.state = 1539
                self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(MParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_code_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_argument"):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_argument"):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = MParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1542
            self.code_type()
            self.state = 1543
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
            super(MParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(MParser.Any_typeContext,0)


        def getRuleIndex(self):
            return MParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_or_any_type"):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_or_any_type"):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = MParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_category_or_any_type)
        try:
            self.state = 1547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1545
                self.typedef(0)
                pass
            elif token in [MParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1546
                self.any_type(0)
                pass
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
            super(MParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(MParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(MParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyListType"):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyListType"):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(MParser.ANY, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyType"):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyType"):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(MParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyDictType"):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyDictType"):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 202
        self.enterRecursionRule(localctx, 202, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1550
            self.match(MParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,108,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1558
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
                    if la_ == 1:
                        localctx = MParser.AnyListTypeContext(self, MParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1552
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1553
                        self.match(MParser.LBRAK)
                        self.state = 1554
                        self.match(MParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = MParser.AnyDictTypeContext(self, MParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1555
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1556
                        self.match(MParser.LCURL)
                        self.state = 1557
                        self.match(MParser.RCURL)
                        pass

             
                self.state = 1562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(MParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration_list"):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration_list"):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = MParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1563
            self.member_method_declaration()
            self.state = 1569
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,109,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1564
                    self.lfp()
                    self.state = 1565
                    self.member_method_declaration() 
                self.state = 1571
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(MParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(MParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(MParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(MParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration"):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration"):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = MParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_member_method_declaration)
        try:
            self.state = 1577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1572
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1573
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1574
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1575
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1576
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
            super(MParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(MParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration_list"):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration_list"):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = MParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1579
            self.native_member_method_declaration()
            self.state = 1585
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1580
                    self.lfp()
                    self.state = 1581
                    self.native_member_method_declaration() 
                self.state = 1587
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(MParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(MParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(MParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration"):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration"):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = MParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_native_member_method_declaration)
        try:
            self.state = 1591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1588
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1589
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1590
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
            super(MParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(MParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(MParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(MParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2CategoryBinding"):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2CategoryBinding"):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(MParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(MParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3CategoryBinding"):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3CategoryBinding"):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(MParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCategoryBinding"):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCategoryBinding"):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(MParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCategoryBinding"):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCategoryBinding"):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(MParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(MParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptCategoryBinding"):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptCategoryBinding"):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = MParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_native_category_binding)
        try:
            self.state = 1603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.JAVA]:
                localctx = MParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1593
                self.match(MParser.JAVA)
                self.state = 1594
                localctx.binding = self.java_class_identifier_expression(0)
                pass
            elif token in [MParser.CSHARP]:
                localctx = MParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1595
                self.match(MParser.CSHARP)
                self.state = 1596
                localctx.binding = self.csharp_identifier_expression(0)
                pass
            elif token in [MParser.PYTHON2]:
                localctx = MParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1597
                self.match(MParser.PYTHON2)
                self.state = 1598
                localctx.binding = self.python_category_binding()
                pass
            elif token in [MParser.PYTHON3]:
                localctx = MParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1599
                self.match(MParser.PYTHON3)
                self.state = 1600
                localctx.binding = self.python_category_binding()
                pass
            elif token in [MParser.JAVASCRIPT]:
                localctx = MParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1601
                self.match(MParser.JAVASCRIPT)
                self.state = 1602
                localctx.binding = self.javascript_category_binding()
                pass
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
            super(MParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(MParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_category_binding"):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_category_binding"):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = MParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1605
            self.identifier()
            self.state = 1607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.state = 1606
                self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(MParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(MParser.DOT)
            else:
                return self.getToken(MParser.DOT, i)

        def getRuleIndex(self):
            return MParser.RULE_python_module

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_module"):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_module"):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = MParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1609
            self.match(MParser.FROM)
            self.state = 1610
            self.module_token()
            self.state = 1611
            self.match(MParser.COLON)
            self.state = 1612
            self.identifier()
            self.state = 1617
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1613
                    self.match(MParser.DOT)
                    self.state = 1614
                    self.identifier() 
                self.state = 1619
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,115,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(MParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_category_binding"):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_category_binding"):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = MParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1620
            self.identifier()
            self.state = 1622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                self.state = 1621
                self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(MParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(MParser.SLASH)
            else:
                return self.getToken(MParser.SLASH, i)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)

        def getRuleIndex(self):
            return MParser.RULE_javascript_module

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_module"):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_module"):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = MParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1624
            self.match(MParser.FROM)
            self.state = 1625
            self.module_token()
            self.state = 1626
            self.match(MParser.COLON)
            self.state = 1628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.SLASH:
                self.state = 1627
                self.match(MParser.SLASH)


            self.state = 1630
            self.javascript_identifier()
            self.state = 1635
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1631
                    self.match(MParser.SLASH)
                    self.state = 1632
                    self.javascript_identifier() 
                self.state = 1637
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

            self.state = 1640
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
            if la_ == 1:
                self.state = 1638
                self.match(MParser.DOT)
                self.state = 1639
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
            super(MParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier_list"):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier_list"):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = MParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1642
            self.variable_identifier()
            self.state = 1647
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1643
                self.match(MParser.COMMA)
                self.state = 1644
                self.variable_identifier()
                self.state = 1649
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
            super(MParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier_list"):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier_list"):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = MParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1650
            self.attribute_identifier()
            self.state = 1655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1651
                self.match(MParser.COMMA)
                self.state = 1652
                self.attribute_identifier()
                self.state = 1657
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
            super(MParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(MParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(MParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(MParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_declaration"):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_declaration"):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = MParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_method_declaration)
        try:
            self.state = 1662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1658
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1659
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1660
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1661
                self.test_method_declaration()
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
            super(MParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(MParser.COMMENT, 0)

        def getRuleIndex(self):
            return MParser.RULE_comment_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterComment_statement"):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComment_statement"):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = MParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1664
            self.match(MParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_native_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_statement_list"):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_statement_list"):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = MParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1666
            self.native_statement()
            self.state = 1672
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1667
                    self.lfp()
                    self.state = 1668
                    self.native_statement() 
                self.state = 1674
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(MParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.CSharpNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(MParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(MParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpNativeStatement"):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpNativeStatement"):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(MParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(MParser.Java_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaNativeStatement"):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaNativeStatement"):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(MParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(MParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptNativeStatement"):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptNativeStatement"):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(MParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(MParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2NativeStatement"):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2NativeStatement"):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(MParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(MParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3NativeStatement"):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3NativeStatement"):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = MParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_native_statement)
        try:
            self.state = 1685
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.JAVA]:
                localctx = MParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1675
                self.match(MParser.JAVA)
                self.state = 1676
                self.java_statement()
                pass
            elif token in [MParser.CSHARP]:
                localctx = MParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1677
                self.match(MParser.CSHARP)
                self.state = 1678
                self.csharp_statement()
                pass
            elif token in [MParser.PYTHON2]:
                localctx = MParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1679
                self.match(MParser.PYTHON2)
                self.state = 1680
                self.python_native_statement()
                pass
            elif token in [MParser.PYTHON3]:
                localctx = MParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1681
                self.match(MParser.PYTHON3)
                self.state = 1682
                self.python_native_statement()
                pass
            elif token in [MParser.JAVASCRIPT]:
                localctx = MParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1683
                self.match(MParser.JAVASCRIPT)
                self.state = 1684
                self.javascript_native_statement()
                pass
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
            super(MParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(MParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(MParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_native_statement"):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_native_statement"):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = MParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1687
            self.python_statement()
            self.state = 1689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.SEMI:
                self.state = 1688
                self.match(MParser.SEMI)


            self.state = 1692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.FROM:
                self.state = 1691
                self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(MParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(MParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_native_statement"):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_native_statement"):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = MParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1694
            self.javascript_statement()
            self.state = 1696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.SEMI:
                self.state = 1695
                self.match(MParser.SEMI)


            self.state = 1699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.FROM:
                self.state = 1698
                self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.StatementContext)
            else:
                return self.getTypedRuleContext(MParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterStatement_list"):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStatement_list"):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = MParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1701
            self.statement()
            self.state = 1707
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1702
                    self.lfp()
                    self.state = 1703
                    self.statement() 
                self.state = 1709
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.AssertionContext)
            else:
                return self.getTypedRuleContext(MParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_assertion_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion_list"):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion_list"):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = MParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1710
            self.assertion()
            self.state = 1716
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1711
                    self.lfp()
                    self.state = 1712
                    self.assertion() 
                self.state = 1718
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_case_statement_list"):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_case_statement_list"):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = MParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1719
            self.switch_case_statement()
            self.state = 1725
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,131,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1720
                    self.lfp()
                    self.state = 1721
                    self.switch_case_statement() 
                self.state = 1727
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,131,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCatch_statement_list"):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatch_statement_list"):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = MParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1728
            self.catch_statement()
            self.state = 1734
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,132,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1729
                    self.lfp()
                    self.state = 1730
                    self.catch_statement() 
                self.state = 1736
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,132,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(MParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a MParser.Literal_collectionContext)
            super(MParser.LiteralListLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(MParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralListLiteral"):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralListLiteral"):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a MParser.Literal_collectionContext)
            super(MParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(MParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(MParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralRangeLiteral"):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralRangeLiteral"):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a MParser.Literal_collectionContext)
            super(MParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(MParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(MParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralSetLiteral"):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralSetLiteral"):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = MParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_literal_collection)
        try:
            self.state = 1751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                localctx = MParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1737
                self.match(MParser.LBRAK)
                self.state = 1738
                localctx.low = self.atomic_literal()
                self.state = 1739
                self.match(MParser.RANGE)
                self.state = 1740
                localctx.high = self.atomic_literal()
                self.state = 1741
                self.match(MParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = MParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1743
                self.match(MParser.LBRAK)
                self.state = 1744
                self.literal_list_literal()
                self.state = 1745
                self.match(MParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = MParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1747
                self.match(MParser.LT)
                self.state = 1748
                self.literal_list_literal()
                self.state = 1749
                self.match(MParser.GT)
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
            super(MParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(MParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(MParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMinIntegerLiteral"):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinIntegerLiteral"):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(MParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateLiteral"):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateLiteral"):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanLiteral"):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanLiteral"):
                listener.exitBooleanLiteral(self)


    class VersionLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.VersionLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def VERSION_LITERAL(self):
            return self.getToken(MParser.VERSION_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionLiteral"):
                listener.enterVersionLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionLiteral"):
                listener.exitVersionLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(MParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHexadecimalLiteral"):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHexadecimalLiteral"):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(MParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDLiteral"):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDLiteral"):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(MParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMaxIntegerLiteral"):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMaxIntegerLiteral"):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(MParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeLiteral"):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeLiteral"):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(MParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodLiteral"):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodLiteral"):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalLiteral"):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalLiteral"):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextLiteral"):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextLiteral"):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(MParser.Null_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNullLiteral"):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNullLiteral"):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerLiteral"):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerLiteral"):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(MParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeLiteral"):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeLiteral"):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterLiteral"):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterLiteral"):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = MParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_atomic_literal)
        try:
            self.state = 1768
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.MIN_INTEGER]:
                localctx = MParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1753
                localctx.t = self.match(MParser.MIN_INTEGER)
                pass
            elif token in [MParser.MAX_INTEGER]:
                localctx = MParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1754
                localctx.t = self.match(MParser.MAX_INTEGER)
                pass
            elif token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1755
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.HEXA_LITERAL]:
                localctx = MParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1756
                localctx.t = self.match(MParser.HEXA_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1757
                localctx.t = self.match(MParser.CHAR_LITERAL)
                pass
            elif token in [MParser.DATE_LITERAL]:
                localctx = MParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1758
                localctx.t = self.match(MParser.DATE_LITERAL)
                pass
            elif token in [MParser.TIME_LITERAL]:
                localctx = MParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1759
                localctx.t = self.match(MParser.TIME_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1760
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1761
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.DATETIME_LITERAL]:
                localctx = MParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1762
                localctx.t = self.match(MParser.DATETIME_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1763
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.PERIOD_LITERAL]:
                localctx = MParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1764
                localctx.t = self.match(MParser.PERIOD_LITERAL)
                pass
            elif token in [MParser.VERSION_LITERAL]:
                localctx = MParser.VersionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1765
                localctx.t = self.match(MParser.VERSION_LITERAL)
                pass
            elif token in [MParser.UUID_LITERAL]:
                localctx = MParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1766
                localctx.t = self.match(MParser.UUID_LITERAL)
                pass
            elif token in [MParser.NONE]:
                localctx = MParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1767
                localctx.n = self.null_literal()
                pass
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
            super(MParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(MParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_list_literal"):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_list_literal"):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = MParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1770
            self.atomic_literal()
            self.state = 1775
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1771
                self.match(MParser.COMMA)
                self.state = 1772
                self.atomic_literal()
                self.state = 1777
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(MParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterThisExpression"):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThisExpression"):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesisExpression"):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesisExpression"):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralExpression"):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralExpression"):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifierExpression"):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifierExpression"):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = MParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_selectable_expression)
        try:
            self.state = 1782
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                localctx = MParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1778
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = MParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1779
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = MParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1780
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = MParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1781
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
            super(MParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def THIS(self):
            return self.getToken(MParser.THIS, 0)

        def getRuleIndex(self):
            return MParser.RULE_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterThis_expression"):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThis_expression"):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = MParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1784
            _la = self._input.LA(1)
            if not(_la==MParser.SELF or _la==MParser.THIS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
            super(MParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def getRuleIndex(self):
            return MParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesis_expression"):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesis_expression"):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = MParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1786
            self.match(MParser.LPAR)
            self.state = 1787
            self.expression(0)
            self.state = 1788
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self):
            return self.getTypedRuleContext(MParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(MParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return MParser.RULE_literal_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_expression"):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_expression"):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = MParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_literal_expression)
        try:
            self.state = 1792
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.NONE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.MIN_INTEGER, MParser.MAX_INTEGER, MParser.TEXT_LITERAL, MParser.UUID_LITERAL, MParser.INTEGER_LITERAL, MParser.HEXA_LITERAL, MParser.DECIMAL_LITERAL, MParser.DATETIME_LITERAL, MParser.TIME_LITERAL, MParser.DATE_LITERAL, MParser.PERIOD_LITERAL, MParser.VERSION_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1790
                self.atomic_literal()
                pass
            elif token in [MParser.LPAR, MParser.LBRAK, MParser.LCURL, MParser.LT, MParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1791
                self.collection_literal()
                pass
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
            super(MParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(MParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(MParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(MParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(MParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(MParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return MParser.RULE_collection_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterCollection_literal"):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollection_literal"):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = MParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_collection_literal)
        try:
            self.state = 1799
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,138,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1794
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1795
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1796
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1797
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1798
                self.tuple_literal()
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
            super(MParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(MParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_tuple_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterTuple_literal"):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTuple_literal"):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = MParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1802
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1801
                self.match(MParser.MUTABLE)


            self.state = 1804
            self.match(MParser.LPAR)
            self.state = 1806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1805
                self.expression_tuple()


            self.state = 1808
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(MParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_dict_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_literal"):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_literal"):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = MParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1811
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1810
                self.match(MParser.MUTABLE)


            self.state = 1813
            self.match(MParser.LCURL)
            self.state = 1815
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1814
                self.dict_entry_list()


            self.state = 1817
            self.match(MParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_expression_tuple

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_tuple"):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_tuple"):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = MParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1819
            self.expression(0)
            self.state = 1820
            self.match(MParser.COMMA)
            self.state = 1829
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (MParser.EXECUTE - 99)) | (1 << (MParser.FETCH - 99)) | (1 << (MParser.MUTABLE - 99)) | (1 << (MParser.NONE - 99)) | (1 << (MParser.NOT - 99)) | (1 << (MParser.READ - 99)) | (1 << (MParser.SELF - 99)) | (1 << (MParser.SORTED - 99)) | (1 << (MParser.THIS - 99)) | (1 << (MParser.BOOLEAN_LITERAL - 99)) | (1 << (MParser.CHAR_LITERAL - 99)) | (1 << (MParser.MIN_INTEGER - 99)) | (1 << (MParser.MAX_INTEGER - 99)) | (1 << (MParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (MParser.TYPE_IDENTIFIER - 163)) | (1 << (MParser.VARIABLE_IDENTIFIER - 163)) | (1 << (MParser.TEXT_LITERAL - 163)) | (1 << (MParser.UUID_LITERAL - 163)) | (1 << (MParser.INTEGER_LITERAL - 163)) | (1 << (MParser.HEXA_LITERAL - 163)) | (1 << (MParser.DECIMAL_LITERAL - 163)) | (1 << (MParser.DATETIME_LITERAL - 163)) | (1 << (MParser.TIME_LITERAL - 163)) | (1 << (MParser.DATE_LITERAL - 163)) | (1 << (MParser.PERIOD_LITERAL - 163)) | (1 << (MParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1821
                self.expression(0)
                self.state = 1826
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MParser.COMMA:
                    self.state = 1822
                    self.match(MParser.COMMA)
                    self.state = 1823
                    self.expression(0)
                    self.state = 1828
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(MParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry_list"):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry_list"):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = MParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1831
            self.dict_entry()
            self.state = 1836
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1832
                self.match(MParser.COMMA)
                self.state = 1833
                self.dict_entry()
                self.state = 1838
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_entryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MParser.RULE_dict_entry

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry"):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry"):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = MParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1839
            localctx.key = self.expression(0)
            self.state = 1840
            self.match(MParser.COLON)
            self.state = 1841
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
            super(MParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Slice_argumentsContext)
            super(MParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstAndLast"):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstAndLast"):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Slice_argumentsContext)
            super(MParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceLastOnly"):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceLastOnly"):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Slice_argumentsContext)
            super(MParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstOnly"):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstOnly"):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = MParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_slice_arguments)
        try:
            self.state = 1852
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                localctx = MParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1843
                localctx.first = self.expression(0)
                self.state = 1844
                self.match(MParser.COLON)
                self.state = 1845
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1847
                localctx.first = self.expression(0)
                self.state = 1848
                self.match(MParser.COLON)
                pass

            elif la_ == 3:
                localctx = MParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1850
                self.match(MParser.COLON)
                self.state = 1851
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
            super(MParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_variable_statement"):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_variable_statement"):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = MParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1854
            self.variable_identifier()
            self.state = 1855
            self.assign()
            self.state = 1856
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignable_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(MParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Assignable_instanceContext)
            super(MParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(MParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(MParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterChildInstance"):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitChildInstance"):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Assignable_instanceContext)
            super(MParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRootInstance"):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRootInstance"):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 276
        self.enterRecursionRule(localctx, 276, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1859
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1865
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,147,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ChildInstanceContext(self, MParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1861
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1862
                    self.child_instance() 
                self.state = 1867
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,147,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(MParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Is_expressionContext)
            super(MParser.IsATypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsATypeExpression"):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsATypeExpression"):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Is_expressionContext)
            super(MParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsOtherExpression"):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsOtherExpression"):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = MParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_is_expression)
        try:
            self.state = 1872
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                localctx = MParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1868
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1869
                self.match(MParser.VARIABLE_IDENTIFIER)
                self.state = 1870
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = MParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1871
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_all_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Read_all_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def ALL(self):
            return self.getToken(MParser.ALL, 0)

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_read_all_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_all_expression"):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_all_expression"):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = MParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1874
            self.match(MParser.READ)
            self.state = 1875
            self.match(MParser.ALL)
            self.state = 1876
            self.match(MParser.FROM)
            self.state = 1877
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_one_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Read_one_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def ONE(self):
            return self.getToken(MParser.ONE, 0)

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_read_one_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_one_expression"):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_one_expression"):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = MParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1879
            self.match(MParser.READ)
            self.state = 1880
            self.match(MParser.ONE)
            self.state = 1881
            self.match(MParser.FROM)
            self.state = 1882
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_by_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Order_byContext)
            else:
                return self.getTypedRuleContext(MParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_order_by_list

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by_list"):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by_list"):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = MParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            self.order_by()
            self.state = 1889
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,149,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1885
                    self.match(MParser.COMMA)
                    self.state = 1886
                    self.order_by() 
                self.state = 1891
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,149,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(MParser.DOT)
            else:
                return self.getToken(MParser.DOT, i)

        def ASC(self):
            return self.getToken(MParser.ASC, 0)

        def DESC(self):
            return self.getToken(MParser.DESC, 0)

        def getRuleIndex(self):
            return MParser.RULE_order_by

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by"):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by"):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = MParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892
            self.variable_identifier()
            self.state = 1897
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1893
                    self.match(MParser.DOT)
                    self.state = 1894
                    self.variable_identifier() 
                self.state = 1899
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

            self.state = 1901
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,151,self._ctx)
            if la_ == 1:
                self.state = 1900
                _la = self._input.LA(1)
                if not(_la==MParser.ASC or _la==MParser.DESC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
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
            super(MParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(MParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(MParser.PLUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorPlus"):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorPlus"):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(MParser.DivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorDivide"):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorDivide"):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(MParser.IdivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorIDivide"):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorIDivide"):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(MParser.MultiplyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMultiply"):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMultiply"):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMinus"):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMinus"):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(MParser.ModuloContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorModulo"):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorModulo"):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = MParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_operator)
        try:
            self.state = 1909
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.PLUS]:
                localctx = MParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1903
                self.match(MParser.PLUS)
                pass
            elif token in [MParser.MINUS]:
                localctx = MParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1904
                self.match(MParser.MINUS)
                pass
            elif token in [MParser.STAR]:
                localctx = MParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1905
                self.multiply()
                pass
            elif token in [MParser.SLASH]:
                localctx = MParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1906
                self.divide()
                pass
            elif token in [MParser.BSLASH]:
                localctx = MParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1907
                self.idivide()
                pass
            elif token in [MParser.PERCENT, MParser.MODULO]:
                localctx = MParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1908
                self.modulo()
                pass
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
            super(MParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_new_token

        def enterRule(self, listener):
            if hasattr(listener, "enterNew_token"):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNew_token"):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = MParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1911
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1912
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
            super(MParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_key_token

        def enterRule(self, listener):
            if hasattr(listener, "enterKey_token"):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey_token"):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = MParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1914
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1915
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

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_module_token

        def enterRule(self, listener):
            if hasattr(listener, "enterModule_token"):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModule_token"):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = MParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1917
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1918
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

    class Value_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_value_token

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_token"):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_token"):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = MParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1920
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1921
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
            super(MParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_symbols_token

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbols_token"):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbols_token"):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = MParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1923
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1924
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
            super(MParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def getRuleIndex(self):
            return MParser.RULE_assign

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)




    def assign(self):

        localctx = MParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1926
            self.match(MParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MParser.STAR, 0)

        def getRuleIndex(self):
            return MParser.RULE_multiply

        def enterRule(self, listener):
            if hasattr(listener, "enterMultiply"):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiply"):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = MParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1928
            self.match(MParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(MParser.SLASH, 0)

        def getRuleIndex(self):
            return MParser.RULE_divide

        def enterRule(self, listener):
            if hasattr(listener, "enterDivide"):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivide"):
                listener.exitDivide(self)




    def divide(self):

        localctx = MParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1930
            self.match(MParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(MParser.BSLASH, 0)

        def getRuleIndex(self):
            return MParser.RULE_idivide

        def enterRule(self, listener):
            if hasattr(listener, "enterIdivide"):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdivide"):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = MParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932
            self.match(MParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(MParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(MParser.MODULO, 0)

        def getRuleIndex(self):
            return MParser.RULE_modulo

        def enterRule(self, listener):
            if hasattr(listener, "enterModulo"):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModulo"):
                listener.exitModulo(self)




    def modulo(self):

        localctx = MParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1934
            _la = self._input.LA(1)
            if not(_la==MParser.PERCENT or _la==MParser.MODULO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
            super(MParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_statementContext)
            super(MParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptStatement"):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptStatement"):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_statementContext)
            super(MParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptReturnStatement"):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptReturnStatement"):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = MParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_javascript_statement)
        try:
            self.state = 1943
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1936
                self.match(MParser.RETURN)
                self.state = 1937
                localctx.exp = self.javascript_expression(0)
                self.state = 1938
                self.match(MParser.SEMI)
                pass
            elif token in [MParser.LPAR, MParser.LBRAK, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1940
                localctx.exp = self.javascript_expression(0)
                self.state = 1941
                self.match(MParser.SEMI)
                pass
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
            super(MParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_expressionContext)
            super(MParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptSelectorExpression"):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptSelectorExpression"):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_expressionContext)
            super(MParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptPrimaryExpression"):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptPrimaryExpression"):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 312
        self.enterRecursionRule(localctx, 312, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1946
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1952
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavascriptSelectorExpressionContext(self, MParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1948
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1949
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1954
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_primary_expression"):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_primary_expression"):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = MParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_javascript_primary_expression)
        try:
            self.state = 1962
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,155,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1955
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1956
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1957
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1958
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1959
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1960
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1961
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
            super(MParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_this_expression"):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_this_expression"):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = MParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1964
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
            super(MParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(MParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_new_expression"):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_new_expression"):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = MParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1966
            self.new_token()
            self.state = 1967
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
            super(MParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(MParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMemberExpression"):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMemberExpression"):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptItemExpression"):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptItemExpression"):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMethodExpression"):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMethodExpression"):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = MParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_javascript_selector_expression)
        try:
            self.state = 1974
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,156,self._ctx)
            if la_ == 1:
                localctx = MParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1969
                self.match(MParser.DOT)
                self.state = 1970
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = MParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1971
                self.match(MParser.DOT)
                self.state = 1972
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = MParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1973
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
            super(MParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(MParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(MParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_method_expression"):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_method_expression"):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = MParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1976
            localctx.name = self.javascript_identifier()
            self.state = 1977
            self.match(MParser.LPAR)
            self.state = 1979
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.LBRAK - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.THIS - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.BOOLEAN_LITERAL - 121)) | (1 << (MParser.CHAR_LITERAL - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)) | (1 << (MParser.DOLLAR_IDENTIFIER - 121)) | (1 << (MParser.TEXT_LITERAL - 121)) | (1 << (MParser.INTEGER_LITERAL - 121)) | (1 << (MParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 1978
                localctx.args = self.javascript_arguments(0)


            self.state = 1981
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_argumentsContext)
            super(MParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentList"):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentList"):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_argumentsContext)
            super(MParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(MParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentListItem"):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentListItem"):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 324
        self.enterRecursionRule(localctx, 324, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1984
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1991
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavascriptArgumentListItemContext(self, MParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1986
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1987
                    self.match(MParser.COMMA)
                    self.state = 1988
                    localctx.item = self.javascript_expression(0) 
                self.state = 1993
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_item_expression"):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_item_expression"):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = MParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1994
            self.match(MParser.LBRAK)
            self.state = 1995
            localctx.exp = self.javascript_expression(0)
            self.state = 1996
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_parenthesis_expression"):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_parenthesis_expression"):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = MParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1998
            self.match(MParser.LPAR)
            self.state = 1999
            localctx.exp = self.javascript_expression(0)
            self.state = 2000
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(MParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier_expression"):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier_expression"):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = MParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2002
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
            super(MParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptIntegerLiteral"):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptIntegerLiteral"):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptBooleanLiteral"):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptBooleanLiteral"):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptCharacterLiteral"):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptCharacterLiteral"):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptTextLiteral"):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptTextLiteral"):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptDecimalLiteral"):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptDecimalLiteral"):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = MParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_literal_expression)
        try:
            self.state = 2009
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2004
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2005
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2006
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2007
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2008
                localctx.t = self.match(MParser.CHAR_LITERAL)
                pass
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
            super(MParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier"):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier"):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = MParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2011
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)) | (1 << (MParser.DOLLAR_IDENTIFIER - 121)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
            super(MParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(MParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_statementContext)
            super(MParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonStatement"):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonStatement"):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_statementContext)
            super(MParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonReturnStatement"):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonReturnStatement"):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = MParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_python_statement)
        try:
            self.state = 2016
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2013
                self.match(MParser.RETURN)
                self.state = 2014
                localctx.exp = self.python_expression(0)
                pass
            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2015
                localctx.exp = self.python_expression(0)
                pass
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
            super(MParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_expressionContext)
            super(MParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(MParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelectorExpression"):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelectorExpression"):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_expressionContext)
            super(MParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(MParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPrimaryExpression"):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPrimaryExpression"):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 338
        self.enterRecursionRule(localctx, 338, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2019
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2025
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonSelectorExpressionContext(self, MParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2021
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2022
                    localctx.child = self.python_selector_expression() 
                self.state = 2027
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonParenthesisExpression"):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonParenthesisExpression"):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifierExpression"):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifierExpression"):
                listener.exitPythonIdentifierExpression(self)


    class PythonSelfExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonSelfExpressionContext, self).__init__(parser)
            self.exp = None # Python_self_expressionContext
            self.copyFrom(ctx)

        def python_self_expression(self):
            return self.getTypedRuleContext(MParser.Python_self_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelfExpression"):
                listener.enterPythonSelfExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelfExpression"):
                listener.exitPythonSelfExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(MParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonLiteralExpression"):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonLiteralExpression"):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(MParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonGlobalMethodExpression"):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonGlobalMethodExpression"):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = MParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_python_primary_expression)
        try:
            self.state = 2033
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,162,self._ctx)
            if la_ == 1:
                localctx = MParser.PythonSelfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2028
                localctx.exp = self.python_self_expression()
                pass

            elif la_ == 2:
                localctx = MParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2029
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 3:
                localctx = MParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2030
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 4:
                localctx = MParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2031
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 5:
                localctx = MParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2032
                localctx.exp = self.python_method_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_self_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_self_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_self_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_self_expression"):
                listener.enterPython_self_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_self_expression"):
                listener.exitPython_self_expression(self)




    def python_self_expression(self):

        localctx = MParser.Python_self_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_self_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2035
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_selector_expressionContext)
            super(MParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(MParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonMethodExpression"):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonMethodExpression"):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_selector_expressionContext)
            super(MParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonItemExpression"):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonItemExpression"):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = MParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_selector_expression)
        try:
            self.state = 2043
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2037
                self.match(MParser.DOT)
                self.state = 2038
                localctx.exp = self.python_method_expression()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2039
                self.match(MParser.LBRAK)
                self.state = 2040
                localctx.exp = self.python_expression(0)
                self.state = 2041
                self.match(MParser.RBRAK)
                pass
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
            super(MParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_method_expression"):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_method_expression"):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = MParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2045
            localctx.name = self.python_identifier()
            self.state = 2046
            self.match(MParser.LPAR)
            self.state = 2048
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.THIS - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.BOOLEAN_LITERAL - 121)) | (1 << (MParser.CHAR_LITERAL - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)) | (1 << (MParser.DOLLAR_IDENTIFIER - 121)) | (1 << (MParser.TEXT_LITERAL - 121)) | (1 << (MParser.INTEGER_LITERAL - 121)) | (1 << (MParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2047
                localctx.args = self.python_argument_list()


            self.state = 2050
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(MParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalOnlyArgumentList"):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalOnlyArgumentList"):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedOnlyArgumentList"):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedOnlyArgumentList"):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonArgumentList"):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonArgumentList"):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = MParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_python_argument_list)
        try:
            self.state = 2058
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                localctx = MParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2052
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = MParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2053
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = MParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2054
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2055
                self.match(MParser.COMMA)
                self.state = 2056
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
            super(MParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(MParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_ordinal_argument_listContext)
            super(MParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentList"):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentList"):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_ordinal_argument_listContext)
            super(MParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentListItem"):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentListItem"):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2061
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2068
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonOrdinalArgumentListItemContext(self, MParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2063
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2064
                    self.match(MParser.COMMA)
                    self.state = 2065
                    localctx.item = self.python_expression(0) 
                self.state = 2070
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(MParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_named_argument_listContext)
            super(MParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(MParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentList"):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentList"):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_named_argument_listContext)
            super(MParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def EQ(self):
            return self.getToken(MParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentListItem"):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentListItem"):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2072
            localctx.name = self.python_identifier()
            self.state = 2073
            self.match(MParser.EQ)
            self.state = 2074
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2084
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,167,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonNamedArgumentListItemContext(self, MParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2076
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2077
                    self.match(MParser.COMMA)
                    self.state = 2078
                    localctx.name = self.python_identifier()
                    self.state = 2079
                    self.match(MParser.EQ)
                    self.state = 2080
                    localctx.exp = self.python_expression(0) 
                self.state = 2086
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,167,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_parenthesis_expression"):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_parenthesis_expression"):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = MParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2087
            self.match(MParser.LPAR)
            self.state = 2088
            localctx.exp = self.python_expression(0)
            self.state = 2089
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonChildIdentifier"):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonChildIdentifier"):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPromptoIdentifier"):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPromptoIdentifier"):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifier"):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifier"):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 356
        self.enterRecursionRule(localctx, 356, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2094
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOLLAR_IDENTIFIER]:
                localctx = MParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2092
                self.match(MParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.NONE, MParser.NULL, MParser.READ, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2093
                localctx.name = self.python_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,169,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonChildIdentifierContext(self, MParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2096
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2097
                    self.match(MParser.DOT)
                    self.state = 2098
                    localctx.name = self.python_identifier() 
                self.state = 2103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,169,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIntegerLiteral"):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIntegerLiteral"):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonBooleanLiteral"):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonBooleanLiteral"):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonCharacterLiteral"):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonCharacterLiteral"):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonTextLiteral"):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonTextLiteral"):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonDecimalLiteral"):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonDecimalLiteral"):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = MParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_python_literal_expression)
        try:
            self.state = 2109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2104
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2105
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2106
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2107
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2108
                localctx.t = self.match(MParser.CHAR_LITERAL)
                pass
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
            super(MParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def THIS(self):
            return self.getToken(MParser.THIS, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_python_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_identifier"):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_identifier"):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = MParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2111
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.THIS - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
            super(MParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(MParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_statementContext)
            super(MParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaReturnStatement"):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaReturnStatement"):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_statementContext)
            super(MParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaStatement"):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaStatement"):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = MParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_java_statement)
        try:
            self.state = 2120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2113
                self.match(MParser.RETURN)
                self.state = 2114
                localctx.exp = self.java_expression(0)
                self.state = 2115
                self.match(MParser.SEMI)
                pass
            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.NATIVE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2117
                localctx.exp = self.java_expression(0)
                self.state = 2118
                self.match(MParser.SEMI)
                pass
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
            super(MParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_expressionContext)
            super(MParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(MParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaSelectorExpression"):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaSelectorExpression"):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_expressionContext)
            super(MParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(MParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaPrimaryExpression"):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaPrimaryExpression"):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 364
        self.enterRecursionRule(localctx, 364, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2123
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaSelectorExpressionContext(self, MParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2125
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2126
                    localctx.child = self.java_selector_expression() 
                self.state = 2131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(MParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(MParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(MParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_primary_expression"):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_primary_expression"):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = MParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_java_primary_expression)
        try:
            self.state = 2137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2132
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2133
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2134
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2135
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2136
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
            super(MParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_this_expression"):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_this_expression"):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = MParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2139
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
            super(MParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(MParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(MParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_new_expression"):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_new_expression"):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = MParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2141
            self.new_token()
            self.state = 2142
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
            super(MParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_selector_expressionContext)
            super(MParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(MParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaItemExpression"):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaItemExpression"):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_selector_expressionContext)
            super(MParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(MParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaMethodExpression"):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaMethodExpression"):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = MParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_java_selector_expression)
        try:
            self.state = 2147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2144
                self.match(MParser.DOT)
                self.state = 2145
                localctx.exp = self.java_method_expression()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2146
                localctx.exp = self.java_item_expression()
                pass
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
            super(MParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(MParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(MParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_method_expression"):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_method_expression"):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = MParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2149
            localctx.name = self.java_identifier()
            self.state = 2150
            self.match(MParser.LPAR)
            self.state = 2152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.THIS - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.BOOLEAN_LITERAL - 121)) | (1 << (MParser.CHAR_LITERAL - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)) | (1 << (MParser.NATIVE_IDENTIFIER - 121)) | (1 << (MParser.DOLLAR_IDENTIFIER - 121)) | (1 << (MParser.TEXT_LITERAL - 121)) | (1 << (MParser.INTEGER_LITERAL - 121)) | (1 << (MParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2151
                localctx.args = self.java_arguments(0)


            self.state = 2154
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_argumentsContext)
            super(MParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(MParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentListItem"):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentListItem"):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_argumentsContext)
            super(MParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentList"):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentList"):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2157
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,176,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaArgumentListItemContext(self, MParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2159
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2160
                    self.match(MParser.COMMA)
                    self.state = 2161
                    localctx.item = self.java_expression(0) 
                self.state = 2166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,176,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_item_expression"):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_item_expression"):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = MParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2167
            self.match(MParser.LBRAK)
            self.state = 2168
            localctx.exp = self.java_expression(0)
            self.state = 2169
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_parenthesis_expression"):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_parenthesis_expression"):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = MParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2171
            self.match(MParser.LPAR)
            self.state = 2172
            localctx.exp = self.java_expression(0)
            self.state = 2173
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_identifier_expressionContext)
            super(MParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(MParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIdentifier"):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIdentifier"):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_identifier_expressionContext)
            super(MParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(MParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildIdentifier"):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildIdentifier"):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 382
        self.enterRecursionRule(localctx, 382, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2176
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaChildIdentifierContext(self, MParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2178
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2179
                    self.match(MParser.DOT)
                    self.state = 2180
                    localctx.name = self.java_identifier() 
                self.state = 2185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_class_identifier_expressionContext)
            super(MParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaClassIdentifier"):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaClassIdentifier"):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_class_identifier_expressionContext)
            super(MParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildClassIdentifier"):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildClassIdentifier"):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 384
        self.enterRecursionRule(localctx, 384, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2187
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,178,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaChildClassIdentifierContext(self, MParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2189
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2190
                    localctx.name = self.match(MParser.DOLLAR_IDENTIFIER) 
                self.state = 2195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,178,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaBooleanLiteral"):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaBooleanLiteral"):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCharacterLiteral"):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCharacterLiteral"):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIntegerLiteral"):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIntegerLiteral"):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaTextLiteral"):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaTextLiteral"):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaDecimalLiteral"):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaDecimalLiteral"):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = MParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_java_literal_expression)
        try:
            self.state = 2201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2196
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2197
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2198
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2199
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2200
                localctx.t = self.match(MParser.CHAR_LITERAL)
                pass
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
            super(MParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(MParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_java_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_identifier"):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_identifier"):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = MParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2203
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)) | (1 << (MParser.NATIVE_IDENTIFIER - 121)) | (1 << (MParser.DOLLAR_IDENTIFIER - 121)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
            super(MParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_statementContext)
            super(MParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpReturnStatement"):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpReturnStatement"):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_statementContext)
            super(MParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpStatement"):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpStatement"):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = MParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_csharp_statement)
        try:
            self.state = 2212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2205
                self.match(MParser.RETURN)
                self.state = 2206
                localctx.exp = self.csharp_expression(0)
                self.state = 2207
                self.match(MParser.SEMI)
                pass
            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2209
                localctx.exp = self.csharp_expression(0)
                self.state = 2210
                self.match(MParser.SEMI)
                pass
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
            super(MParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_expressionContext)
            super(MParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpSelectorExpression"):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpSelectorExpression"):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_expressionContext)
            super(MParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPrimaryExpression"):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPrimaryExpression"):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 392
        self.enterRecursionRule(localctx, 392, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2215
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,181,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpSelectorExpressionContext(self, MParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2217
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2218
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,181,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_primary_expression"):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_primary_expression"):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = MParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_csharp_primary_expression)
        try:
            self.state = 2229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,182,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2224
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2225
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2226
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2227
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2228
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
            super(MParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_this_expression"):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_this_expression"):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = MParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2231
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
            super(MParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(MParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_new_expression"):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_new_expression"):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = MParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2233
            self.new_token()
            self.state = 2234
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
            super(MParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_selector_expressionContext)
            super(MParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpMethodExpression"):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpMethodExpression"):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_selector_expressionContext)
            super(MParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpItemExpression"):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpItemExpression"):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = MParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_csharp_selector_expression)
        try:
            self.state = 2239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2236
                self.match(MParser.DOT)
                self.state = 2237
                localctx.exp = self.csharp_method_expression()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2238
                localctx.exp = self.csharp_item_expression()
                pass
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
            super(MParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(MParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(MParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_method_expression"):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_method_expression"):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = MParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2241
            localctx.name = self.csharp_identifier()
            self.state = 2242
            self.match(MParser.LPAR)
            self.state = 2244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.THIS - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.BOOLEAN_LITERAL - 121)) | (1 << (MParser.CHAR_LITERAL - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)) | (1 << (MParser.DOLLAR_IDENTIFIER - 121)) | (1 << (MParser.TEXT_LITERAL - 121)) | (1 << (MParser.INTEGER_LITERAL - 121)) | (1 << (MParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2243
                localctx.args = self.csharp_arguments(0)


            self.state = 2246
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_argumentsContext)
            super(MParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentList"):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentList"):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_argumentsContext)
            super(MParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(MParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentListItem"):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentListItem"):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 404
        self.enterRecursionRule(localctx, 404, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2249
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpArgumentListItemContext(self, MParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2251
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2252
                    self.match(MParser.COMMA)
                    self.state = 2253
                    localctx.item = self.csharp_expression(0) 
                self.state = 2258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_item_expression"):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_item_expression"):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = MParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2259
            self.match(MParser.LBRAK)
            self.state = 2260
            localctx.exp = self.csharp_expression(0)
            self.state = 2261
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_parenthesis_expression"):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_parenthesis_expression"):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = MParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2263
            self.match(MParser.LPAR)
            self.state = 2264
            localctx.exp = self.csharp_expression(0)
            self.state = 2265
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(MParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIdentifier"):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIdentifier"):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(MParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpChildIdentifier"):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpChildIdentifier"):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPromptoIdentifier"):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPromptoIdentifier"):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 410
        self.enterRecursionRule(localctx, 410, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOLLAR_IDENTIFIER]:
                localctx = MParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2268
                self.match(MParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2269
                localctx.name = self.csharp_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,187,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpChildIdentifierContext(self, MParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2272
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2273
                    self.match(MParser.DOT)
                    self.state = 2274
                    localctx.name = self.csharp_identifier() 
                self.state = 2279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,187,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpBooleanLiteral"):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpBooleanLiteral"):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIntegerLiteral"):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIntegerLiteral"):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpDecimalLiteral"):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpDecimalLiteral"):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCharacterLiteral"):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCharacterLiteral"):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpTextLiteral"):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpTextLiteral"):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = MParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_csharp_literal_expression)
        try:
            self.state = 2285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2280
                self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2281
                self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2282
                self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2283
                self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2284
                self.match(MParser.CHAR_LITERAL)
                pass
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
            super(MParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_identifier"):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_identifier"):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = MParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2287
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (MParser.NONE - 121)) | (1 << (MParser.NULL - 121)) | (1 << (MParser.READ - 121)) | (1 << (MParser.SELF - 121)) | (1 << (MParser.TEST - 121)) | (1 << (MParser.WRITE - 121)) | (1 << (MParser.SYMBOL_IDENTIFIER - 121)) | (1 << (MParser.TYPE_IDENTIFIER - 121)) | (1 << (MParser.VARIABLE_IDENTIFIER - 121)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
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
        self._predicates[17] = self.native_category_binding_list_sempred
        self._predicates[29] = self.callable_parent_sempred
        self._predicates[39] = self.else_if_statement_list_sempred
        self._predicates[45] = self.expression_sempred
        self._predicates[47] = self.instance_expression_sempred
        self._predicates[49] = self.instance_selector_sempred
        self._predicates[53] = self.copy_from_sempred
        self._predicates[54] = self.argument_assignment_list_sempred
        self._predicates[61] = self.child_instance_sempred
        self._predicates[81] = self.typedef_sempred
        self._predicates[101] = self.any_type_sempred
        self._predicates[138] = self.assignable_instance_sempred
        self._predicates[139] = self.is_expression_sempred
        self._predicates[145] = self.new_token_sempred
        self._predicates[146] = self.key_token_sempred
        self._predicates[147] = self.module_token_sempred
        self._predicates[148] = self.value_token_sempred
        self._predicates[149] = self.symbols_token_sempred
        self._predicates[156] = self.javascript_expression_sempred
        self._predicates[162] = self.javascript_arguments_sempred
        self._predicates[169] = self.python_expression_sempred
        self._predicates[175] = self.python_ordinal_argument_list_sempred
        self._predicates[176] = self.python_named_argument_list_sempred
        self._predicates[178] = self.python_identifier_expression_sempred
        self._predicates[182] = self.java_expression_sempred
        self._predicates[188] = self.java_arguments_sempred
        self._predicates[191] = self.java_identifier_expression_sempred
        self._predicates[192] = self.java_class_identifier_expression_sempred
        self._predicates[196] = self.csharp_expression_sempred
        self._predicates[202] = self.csharp_arguments_sempred
        self._predicates[205] = self.csharp_identifier_expression_sempred
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
                return self.precpred(self._ctx, 32)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 32:
                return self.precpred(self._ctx, 21)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.wasNot(MParser.WS)
         

            if predIndex == 35:
                return self.wasNot(MParser.WS)
         

            if predIndex == 36:
                return self.wasNot(MParser.WS)
         

    def copy_from_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.willNotBe(self.equalToken())
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.wasNot(MParser.WS)
         

            if predIndex == 41:
                return self.wasNot(MParser.WS)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         




