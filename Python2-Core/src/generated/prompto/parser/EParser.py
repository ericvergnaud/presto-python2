# Generated from EParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00b2\u093a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1\t\u00d1\4\u00d2")
        buf.write(u"\t\u00d2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u01ab\n\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\5\2\u01b2\n\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u01d0\n\5\3")
        buf.write(u"\6\3\6\3\6\3\6\5\6\u01d6\n\6\3\6\3\6\3\6\5\6\u01db\n")
        buf.write(u"\6\3\6\3\6\3\6\3\6\5\6\u01e1\n\6\5\6\u01e3\n\6\3\6\5")
        buf.write(u"\6\u01e6\n\6\3\7\3\7\3\7\3\7\5\7\u01ec\n\7\3\7\3\7\5")
        buf.write(u"\7\u01f0\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write(u"\u01fb\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0204\n\7")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\5\b\u0213\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u021c")
        buf.write(u"\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u0223\n\t\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\n\5\n\u022d\n\n\3\n\3\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\f\3\f\3\f\3\f\5\f\u0243\n\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u025a\n\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u0267\n\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0272\n\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\5\17\u0280\n\17\3\20\3\20\3\20\3\20\5\20\u0286")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5")
        buf.write(u"\20\u0291\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\5\20\u029f\n\20\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\7\22\u02b1\n\22\f\22\16\22\u02b4\13\22\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u02be\n\23\5")
        buf.write(u"\23\u02c0\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write(u"\u02c9\n\24\3\24\3\24\5\24\u02cd\n\24\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\5\25\u02d5\n\25\3\25\3\25\5\25\u02d9")
        buf.write(u"\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write(u"\26\5\26\u02e5\n\26\3\26\3\26\3\26\5\26\u02ea\n\26\3")
        buf.write(u"\26\3\26\5\26\u02ee\n\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0309")
        buf.write(u"\n\27\3\30\3\30\3\31\3\31\3\31\5\31\u0310\n\31\3\32\3")
        buf.write(u"\32\3\32\5\32\u0315\n\32\3\32\3\32\5\32\u0319\n\32\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u032e\n")
        buf.write(u"\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\5\35\u033c\n\35\3\36\3\36\5\36\u0340\n\36")
        buf.write(u"\3\36\5\36\u0343\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0364\n!\3!\3!\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\5\"\u0377\n\"\3#\3#\3#\3#\3#\5#\u037e\n#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write(u"\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u03a0\n&\3&\3&\3")
        buf.write(u"&\3&\3&\3&\3&\5&\u03a9\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'")
        buf.write(u"\u03be\n\'\f\'\16\'\u03c1\13\'\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\5)\u03d0\n)\3)\3)\3)\5)\u03d5\n)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\5)\u03dd\n)\3)\3)\3)\3)\3)\3)\3)\5)\u03e6")
        buf.write(u"\n)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write(u"*\3*\3*\3*\3*\5*\u03fd\n*\3+\3+\3,\3,\5,\u0403\n,\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0421\n-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\7-\u0491\n-\f-\16-\u0494\13-\3.\3.\3.\3.\3.\7.\u049b")
        buf.write(u"\n.\f.\16.\u049e\13.\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\7\62\u04b0\n")
        buf.write(u"\62\f\62\16\62\u04b3\13\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u04c2\n\63")
        buf.write(u"\3\64\3\64\3\64\5\64\u04c7\n\64\3\65\3\65\3\65\3\65\3")
        buf.write(u"\66\3\66\3\66\3\66\5\66\u04d1\n\66\3\66\3\66\3\66\5\66")
        buf.write(u"\u04d6\n\66\5\66\u04d8\n\66\3\66\3\66\3\66\3\66\5\66")
        buf.write(u"\u04de\n\66\5\66\u04e0\n\66\5\66\u04e2\n\66\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\38\38\38\38\39\39\39\39\39\39\3:\3:\3")
        buf.write(u":\5:\u04f6\n:\3:\3:\3:\3:\3:\5:\u04fd\n:\3:\3:\5:\u0501")
        buf.write(u"\n:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u050c\n:\3:\3:\5:\u0510")
        buf.write(u"\n:\3:\3:\3:\5:\u0515\n:\5:\u0517\n:\3;\3;\5;\u051b\n")
        buf.write(u";\3;\3;\3;\3;\3;\3;\5;\u0523\n;\3<\3<\3<\3<\3<\5<\u052a")
        buf.write(u"\n<\5<\u052c\n<\3<\3<\3<\5<\u0531\n<\5<\u0533\n<\3=\3")
        buf.write(u"=\3=\3=\3=\3=\3=\7=\u053c\n=\f=\16=\u053f\13=\3>\3>\3")
        buf.write(u">\5>\u0544\n>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@")
        buf.write(u"\3@\5@\u0554\n@\3A\3A\3A\3A\3B\7B\u055b\nB\fB\16B\u055e")
        buf.write(u"\13B\3C\6C\u0561\nC\rC\16C\u0562\3D\6D\u0566\nD\rD\16")
        buf.write(u"D\u0567\3D\3D\3E\7E\u056d\nE\fE\16E\u0570\13E\3E\3E\3")
        buf.write(u"F\3F\3G\5G\u0577\nG\3G\3G\3G\3H\3H\3H\3H\7H\u0580\nH")
        buf.write(u"\fH\16H\u0583\13H\3I\3I\3I\7I\u0588\nI\fI\16I\u058b\13")
        buf.write(u"I\3I\3I\3I\3I\3I\5I\u0592\nI\3J\3J\3K\3K\5K\u0598\nK")
        buf.write(u"\3L\3L\3L\3L\7L\u059e\nL\fL\16L\u05a1\13L\3M\3M\3M\3")
        buf.write(u"M\7M\u05a7\nM\fM\16M\u05aa\13M\3N\3N\3N\7N\u05af\nN\f")
        buf.write(u"N\16N\u05b2\13N\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u05be")
        buf.write(u"\nO\3P\5P\u05c1\nP\3P\3P\5P\u05c5\nP\3P\3P\3Q\5Q\u05ca")
        buf.write(u"\nQ\3Q\3Q\5Q\u05ce\nQ\3Q\3Q\3R\3R\3R\7R\u05d5\nR\fR\16")
        buf.write(u"R\u05d8\13R\3S\3S\3S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3T\3")
        buf.write(u"T\3T\3T\3T\3T\5T\u05ec\nT\3T\3T\3T\3T\3T\3T\3T\3T\7T")
        buf.write(u"\u05f6\nT\fT\16T\u05f9\13T\3U\3U\5U\u05fd\nU\3V\3V\3")
        buf.write(u"V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u060e\nV\3W")
        buf.write(u"\3W\3X\5X\u0613\nX\3X\3X\3Y\3Y\3Z\3Z\3Z\5Z\u061c\nZ\3")
        buf.write(u"[\3[\3[\7[\u0621\n[\f[\16[\u0624\13[\3\\\3\\\5\\\u0628")
        buf.write(u"\n\\\3]\3]\3]\5]\u062d\n]\3^\3^\3_\3_\3`\3`\3a\3a\3b")
        buf.write(u"\3b\3b\7b\u063a\nb\fb\16b\u063d\13b\3c\3c\5c\u0641\n")
        buf.write(u"c\3c\5c\u0644\nc\3d\3d\5d\u0648\nd\3e\3e\3e\5e\u064d")
        buf.write(u"\ne\3f\3f\3f\3g\3g\5g\u0654\ng\3h\3h\3h\3h\3h\3h\3h\3")
        buf.write(u"h\3h\7h\u065f\nh\fh\16h\u0662\13h\3i\3i\3i\3i\7i\u0668")
        buf.write(u"\ni\fi\16i\u066b\13i\3j\3j\3j\3j\3j\5j\u0672\nj\3k\3")
        buf.write(u"k\3k\3k\7k\u0678\nk\fk\16k\u067b\13k\3l\3l\3l\5l\u0680")
        buf.write(u"\nl\3m\3m\3m\3m\3m\3m\3m\3m\3m\3m\5m\u068c\nm\3n\3n\5")
        buf.write(u"n\u0690\nn\3o\3o\3o\3o\3o\3o\7o\u0698\no\fo\16o\u069b")
        buf.write(u"\13o\3p\3p\5p\u069f\np\3q\3q\3q\3q\5q\u06a5\nq\3q\3q")
        buf.write(u"\3q\7q\u06aa\nq\fq\16q\u06ad\13q\3q\3q\5q\u06b1\nq\3")
        buf.write(u"r\3r\3r\7r\u06b6\nr\fr\16r\u06b9\13r\3s\3s\3s\7s\u06be")
        buf.write(u"\ns\fs\16s\u06c1\13s\3t\3t\3t\3t\5t\u06c7\nt\3u\3u\3")
        buf.write(u"v\3v\3v\3v\7v\u06cf\nv\fv\16v\u06d2\13v\3w\3w\3w\3w\3")
        buf.write(u"w\3w\3w\3w\3w\3w\5w\u06de\nw\3x\3x\5x\u06e2\nx\3x\5x")
        buf.write(u"\u06e5\nx\3y\3y\5y\u06e9\ny\3y\5y\u06ec\ny\3z\3z\3z\3")
        buf.write(u"z\7z\u06f2\nz\fz\16z\u06f5\13z\3{\3{\3{\3{\7{\u06fb\n")
        buf.write(u"{\f{\16{\u06fe\13{\3|\3|\3|\3|\7|\u0704\n|\f|\16|\u0707")
        buf.write(u"\13|\3}\3}\3}\3}\7}\u070d\n}\f}\16}\u0710\13}\3~\3~\3")
        buf.write(u"~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\5~\u0720\n~\3\177")
        buf.write(u"\3\177\3\177\3\177\3\177\3\177\3\177\3\177\3\177\3\177")
        buf.write(u"\3\177\3\177\3\177\3\177\3\177\5\177\u0731\n\177\3\u0080")
        buf.write(u"\3\u0080\3\u0080\7\u0080\u0736\n\u0080\f\u0080\16\u0080")
        buf.write(u"\u0739\13\u0080\3\u0081\3\u0081\3\u0081\3\u0081\5\u0081")
        buf.write(u"\u073f\n\u0081\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0084\3\u0084\5\u0084\u0749\n\u0084\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\3\u0085\5\u0085\u0750\n\u0085")
        buf.write(u"\3\u0086\5\u0086\u0753\n\u0086\3\u0086\3\u0086\5\u0086")
        buf.write(u"\u0757\n\u0086\3\u0086\3\u0086\3\u0087\5\u0087\u075c")
        buf.write(u"\n\u0087\3\u0087\3\u0087\5\u0087\u0760\n\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\7\u0088")
        buf.write(u"\u0769\n\u0088\f\u0088\16\u0088\u076c\13\u0088\5\u0088")
        buf.write(u"\u076e\n\u0088\3\u0089\3\u0089\3\u0089\7\u0089\u0773")
        buf.write(u"\n\u0089\f\u0089\16\u0089\u0776\13\u0089\3\u008a\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b\u0785\n\u008b")
        buf.write(u"\3\u008c\3\u008c\3\u008c\3\u008c\3\u008d\3\u008d\3\u008d")
        buf.write(u"\3\u008d\3\u008d\7\u008d\u0790\n\u008d\f\u008d\16\u008d")
        buf.write(u"\u0793\13\u008d\3\u008e\3\u008e\3\u008e\3\u008e\5\u008e")
        buf.write(u"\u0799\n\u008e\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\7\u0091\u07a8\n\u0091\f\u0091\16\u0091\u07ab")
        buf.write(u"\13\u0091\3\u0092\3\u0092\3\u0092\7\u0092\u07b0\n\u0092")
        buf.write(u"\f\u0092\16\u0092\u07b3\13\u0092\3\u0092\5\u0092\u07b6")
        buf.write(u"\n\u0092\3\u0093\3\u0093\3\u0093\3\u0093\3\u0093\3\u0093")
        buf.write(u"\5\u0093\u07be\n\u0093\3\u0094\3\u0094\3\u0094\3\u0095")
        buf.write(u"\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0097\3\u0097")
        buf.write(u"\3\u0097\3\u0098\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a")
        buf.write(u"\3\u009a\3\u009b\3\u009b\3\u009c\3\u009c\3\u009d\3\u009d")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\5\u009e\u07e0\n\u009e\3\u009f\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\7\u009f\u07e7\n\u009f\f\u009f\16\u009f\u07ea")
        buf.write(u"\13\u009f\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\5\u00a0\u07f3\n\u00a0\3\u00a1\3\u00a1\3\u00a2")
        buf.write(u"\3\u00a2\3\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\5\u00a3\u07ff\n\u00a3\3\u00a4\3\u00a4\3\u00a4\5\u00a4")
        buf.write(u"\u0804\n\u00a4\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u080e\n\u00a5\f\u00a5")
        buf.write(u"\16\u00a5\u0811\13\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\3\u00a9\5\u00a9\u0822\n\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u0829")
        buf.write(u"\n\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\7\u00ac")
        buf.write(u"\u0830\n\u00ac\f\u00ac\16\u00ac\u0833\13\u00ac\3\u00ad")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u083a\n\u00ad")
        buf.write(u"\3\u00ae\3\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\5\u00af\u0844\n\u00af\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\5\u00b0\u0849\n\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\3\u00b1\5\u00b1\u0853\n\u00b1")
        buf.write(u"\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\7\u00b2")
        buf.write(u"\u085b\n\u00b2\f\u00b2\16\u00b2\u085e\13\u00b2\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\7\u00b3\u086b\n\u00b3\f\u00b3")
        buf.write(u"\16\u00b3\u086e\13\u00b3\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u0877\n\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\7\u00b5\u087c\n\u00b5\f\u00b5\16\u00b5")
        buf.write(u"\u087f\13\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\5\u00b6\u0886\n\u00b6\3\u00b7\3\u00b7\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\5\u00b8\u0891")
        buf.write(u"\n\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\7\u00b9")
        buf.write(u"\u0898\n\u00b9\f\u00b9\16\u00b9\u089b\13\u00b9\3\u00ba")
        buf.write(u"\3\u00ba\3\u00ba\3\u00ba\3\u00ba\5\u00ba\u08a2\n\u00ba")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd")
        buf.write(u"\3\u00bd\5\u00bd\u08ac\n\u00bd\3\u00be\3\u00be\3\u00be")
        buf.write(u"\5\u00be\u08b1\n\u00be\3\u00be\3\u00be\3\u00bf\3\u00bf")
        buf.write(u"\3\u00bf\3\u00bf\3\u00bf\3\u00bf\7\u00bf\u08bb\n\u00bf")
        buf.write(u"\f\u00bf\16\u00bf\u08be\13\u00bf\3\u00c0\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c2\3\u00c2")
        buf.write(u"\3\u00c2\3\u00c2\3\u00c2\3\u00c2\7\u00c2\u08ce\n\u00c2")
        buf.write(u"\f\u00c2\16\u00c2\u08d1\13\u00c2\3\u00c3\3\u00c3\3\u00c3")
        buf.write(u"\3\u00c3\3\u00c3\7\u00c3\u08d8\n\u00c3\f\u00c3\16\u00c3")
        buf.write(u"\u08db\13\u00c3\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\5\u00c4\u08e2\n\u00c4\3\u00c5\3\u00c5\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c6\5\u00c6\u08ed")
        buf.write(u"\n\u00c6\3\u00c7\3\u00c7\3\u00c7\3\u00c7\3\u00c7\7\u00c7")
        buf.write(u"\u08f4\n\u00c7\f\u00c7\16\u00c7\u08f7\13\u00c7\3\u00c8")
        buf.write(u"\3\u00c8\3\u00c8\3\u00c8\3\u00c8\5\u00c8\u08fe\n\u00c8")
        buf.write(u"\3\u00c9\3\u00c9\3\u00ca\3\u00ca\3\u00ca\3\u00cb\3\u00cb")
        buf.write(u"\3\u00cb\5\u00cb\u0908\n\u00cb\3\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\5\u00cc\u090d\n\u00cc\3\u00cc\3\u00cc\3\u00cd\3\u00cd")
        buf.write(u"\3\u00cd\3\u00cd\3\u00cd\3\u00cd\7\u00cd\u0917\n\u00cd")
        buf.write(u"\f\u00cd\16\u00cd\u091a\13\u00cd\3\u00ce\3\u00ce\3\u00ce")
        buf.write(u"\3\u00ce\3\u00cf\3\u00cf\3\u00cf\3\u00cf\3\u00d0\3\u00d0")
        buf.write(u"\3\u00d0\5\u00d0\u0927\n\u00d0\3\u00d0\3\u00d0\3\u00d0")
        buf.write(u"\7\u00d0\u092c\n\u00d0\f\u00d0\16\u00d0\u092f\13\u00d0")
        buf.write(u"\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\5\u00d1\u0936")
        buf.write(u"\n\u00d1\3\u00d2\3\u00d2\3\u00d2\2\30\"LXZbx\u00a6\u00ce")
        buf.write(u"\u0118\u013c\u0148\u0156\u0162\u0164\u0168\u0170\u017c")
        buf.write(u"\u0182\u0184\u018c\u0198\u019e\u00d3\2\4\6\b\n\f\16\20")
        buf.write(u"\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJ")
        buf.write(u"LNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write(u"\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write(u"\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac")
        buf.write(u"\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be")
        buf.write(u"\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0")
        buf.write(u"\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2")
        buf.write(u"\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4")
        buf.write(u"\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106")
        buf.write(u"\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118")
        buf.write(u"\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a")
        buf.write(u"\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c")
        buf.write(u"\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e")
        buf.write(u"\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160")
        buf.write(u"\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172")
        buf.write(u"\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182\u0184")
        buf.write(u"\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194\u0196")
        buf.write(u"\u0198\u019a\u019c\u019e\u01a0\u01a2\2\13\3\2\"#\4\2")
        buf.write(u"\u0092\u0092\u00a6\u00a6\4\2\u008e\u008e\u0096\u0096")
        buf.write(u"\4\2LL]]\4\2\'\'xx\f\2\64=CC{{~~\u0088\u0088\u008e\u008e")
        buf.write(u"\u0095\u0095\u009f\u009f\u00a4\u00a6\u00a8\u00a8\n\2")
        buf.write(u"\64=CC{{~~\u0088\u0088\u0095\u0096\u009f\u009f\u00a4")
        buf.write(u"\u00a6\13\2\64=CC{{~~\u0088\u0088\u008e\u008e\u0095\u0095")
        buf.write(u"\u009f\u009f\u00a4\u00a8\13\2\64=CC{{~~\u0088\u0088\u008e")
        buf.write(u"\u008e\u0095\u0095\u009f\u009f\u00a4\u00a6\2\u09c7\2")
        buf.write(u"\u01a4\3\2\2\2\4\u01b9\3\2\2\2\6\u01c5\3\2\2\2\b\u01cb")
        buf.write(u"\3\2\2\2\n\u01d1\3\2\2\2\f\u01e7\3\2\2\2\16\u0205\3\2")
        buf.write(u"\2\2\20\u0222\3\2\2\2\22\u0224\3\2\2\2\24\u0234\3\2\2")
        buf.write(u"\2\26\u023e\3\2\2\2\30\u024b\3\2\2\2\32\u0255\3\2\2\2")
        buf.write(u"\34\u0262\3\2\2\2\36\u0281\3\2\2\2 \u02a0\3\2\2\2\"\u02a9")
        buf.write(u"\3\2\2\2$\u02bf\3\2\2\2&\u02c1\3\2\2\2(\u02ce\3\2\2\2")
        buf.write(u"*\u02e0\3\2\2\2,\u02f5\3\2\2\2.\u030a\3\2\2\2\60\u030c")
        buf.write(u"\3\2\2\2\62\u0311\3\2\2\2\64\u032d\3\2\2\2\66\u032f\3")
        buf.write(u"\2\2\28\u033b\3\2\2\2:\u0342\3\2\2\2<\u0344\3\2\2\2>")
        buf.write(u"\u034d\3\2\2\2@\u0356\3\2\2\2B\u0376\3\2\2\2D\u0378\3")
        buf.write(u"\2\2\2F\u0386\3\2\2\2H\u038f\3\2\2\2J\u0396\3\2\2\2L")
        buf.write(u"\u03aa\3\2\2\2N\u03c2\3\2\2\2P\u03c5\3\2\2\2R\u03fc\3")
        buf.write(u"\2\2\2T\u03fe\3\2\2\2V\u0400\3\2\2\2X\u0420\3\2\2\2Z")
        buf.write(u"\u0495\3\2\2\2\\\u049f\3\2\2\2^\u04a3\3\2\2\2`\u04a8")
        buf.write(u"\3\2\2\2b\u04aa\3\2\2\2d\u04c1\3\2\2\2f\u04c3\3\2\2\2")
        buf.write(u"h\u04c8\3\2\2\2j\u04e1\3\2\2\2l\u04e3\3\2\2\2n\u04e8")
        buf.write(u"\3\2\2\2p\u04ec\3\2\2\2r\u0516\3\2\2\2t\u0518\3\2\2\2")
        buf.write(u"v\u0532\3\2\2\2x\u0534\3\2\2\2z\u0543\3\2\2\2|\u0547")
        buf.write(u"\3\2\2\2~\u0553\3\2\2\2\u0080\u0555\3\2\2\2\u0082\u055c")
        buf.write(u"\3\2\2\2\u0084\u0560\3\2\2\2\u0086\u0565\3\2\2\2\u0088")
        buf.write(u"\u056e\3\2\2\2\u008a\u0573\3\2\2\2\u008c\u0576\3\2\2")
        buf.write(u"\2\u008e\u057b\3\2\2\2\u0090\u0589\3\2\2\2\u0092\u0593")
        buf.write(u"\3\2\2\2\u0094\u0597\3\2\2\2\u0096\u0599\3\2\2\2\u0098")
        buf.write(u"\u05a2\3\2\2\2\u009a\u05ab\3\2\2\2\u009c\u05bd\3\2\2")
        buf.write(u"\2\u009e\u05c0\3\2\2\2\u00a0\u05c9\3\2\2\2\u00a2\u05d1")
        buf.write(u"\3\2\2\2\u00a4\u05d9\3\2\2\2\u00a6\u05eb\3\2\2\2\u00a8")
        buf.write(u"\u05fc\3\2\2\2\u00aa\u060d\3\2\2\2\u00ac\u060f\3\2\2")
        buf.write(u"\2\u00ae\u0612\3\2\2\2\u00b0\u0616\3\2\2\2\u00b2\u061b")
        buf.write(u"\3\2\2\2\u00b4\u061d\3\2\2\2\u00b6\u0627\3\2\2\2\u00b8")
        buf.write(u"\u062c\3\2\2\2\u00ba\u062e\3\2\2\2\u00bc\u0630\3\2\2")
        buf.write(u"\2\u00be\u0632\3\2\2\2\u00c0\u0634\3\2\2\2\u00c2\u0636")
        buf.write(u"\3\2\2\2\u00c4\u0643\3\2\2\2\u00c6\u0647\3\2\2\2\u00c8")
        buf.write(u"\u0649\3\2\2\2\u00ca\u064e\3\2\2\2\u00cc\u0653\3\2\2")
        buf.write(u"\2\u00ce\u0655\3\2\2\2\u00d0\u0663\3\2\2\2\u00d2\u0671")
        buf.write(u"\3\2\2\2\u00d4\u0673\3\2\2\2\u00d6\u067f\3\2\2\2\u00d8")
        buf.write(u"\u068b\3\2\2\2\u00da\u068d\3\2\2\2\u00dc\u0691\3\2\2")
        buf.write(u"\2\u00de\u069c\3\2\2\2\u00e0\u06a0\3\2\2\2\u00e2\u06b2")
        buf.write(u"\3\2\2\2\u00e4\u06ba\3\2\2\2\u00e6\u06c6\3\2\2\2\u00e8")
        buf.write(u"\u06c8\3\2\2\2\u00ea\u06ca\3\2\2\2\u00ec\u06dd\3\2\2")
        buf.write(u"\2\u00ee\u06df\3\2\2\2\u00f0\u06e6\3\2\2\2\u00f2\u06ed")
        buf.write(u"\3\2\2\2\u00f4\u06f6\3\2\2\2\u00f6\u06ff\3\2\2\2\u00f8")
        buf.write(u"\u0708\3\2\2\2\u00fa\u071f\3\2\2\2\u00fc\u0730\3\2\2")
        buf.write(u"\2\u00fe\u0732\3\2\2\2\u0100\u073e\3\2\2\2\u0102\u0740")
        buf.write(u"\3\2\2\2\u0104\u0742\3\2\2\2\u0106\u0748\3\2\2\2\u0108")
        buf.write(u"\u074f\3\2\2\2\u010a\u0752\3\2\2\2\u010c\u075b\3\2\2")
        buf.write(u"\2\u010e\u0763\3\2\2\2\u0110\u076f\3\2\2\2\u0112\u0777")
        buf.write(u"\3\2\2\2\u0114\u0784\3\2\2\2\u0116\u0786\3\2\2\2\u0118")
        buf.write(u"\u078a\3\2\2\2\u011a\u0798\3\2\2\2\u011c\u079a\3\2\2")
        buf.write(u"\2\u011e\u079f\3\2\2\2\u0120\u07a4\3\2\2\2\u0122\u07ac")
        buf.write(u"\3\2\2\2\u0124\u07bd\3\2\2\2\u0126\u07bf\3\2\2\2\u0128")
        buf.write(u"\u07c2\3\2\2\2\u012a\u07c5\3\2\2\2\u012c\u07c8\3\2\2")
        buf.write(u"\2\u012e\u07cb\3\2\2\2\u0130\u07ce\3\2\2\2\u0132\u07d0")
        buf.write(u"\3\2\2\2\u0134\u07d2\3\2\2\2\u0136\u07d4\3\2\2\2\u0138")
        buf.write(u"\u07d6\3\2\2\2\u013a\u07df\3\2\2\2\u013c\u07e1\3\2\2")
        buf.write(u"\2\u013e\u07f2\3\2\2\2\u0140\u07f4\3\2\2\2\u0142\u07f6")
        buf.write(u"\3\2\2\2\u0144\u07fe\3\2\2\2\u0146\u0800\3\2\2\2\u0148")
        buf.write(u"\u0807\3\2\2\2\u014a\u0812\3\2\2\2\u014c\u0816\3\2\2")
        buf.write(u"\2\u014e\u081a\3\2\2\2\u0150\u0821\3\2\2\2\u0152\u0823")
        buf.write(u"\3\2\2\2\u0154\u0828\3\2\2\2\u0156\u082a\3\2\2\2\u0158")
        buf.write(u"\u0839\3\2\2\2\u015a\u083b\3\2\2\2\u015c\u0843\3\2\2")
        buf.write(u"\2\u015e\u0845\3\2\2\2\u0160\u0852\3\2\2\2\u0162\u0854")
        buf.write(u"\3\2\2\2\u0164\u085f\3\2\2\2\u0166\u086f\3\2\2\2\u0168")
        buf.write(u"\u0876\3\2\2\2\u016a\u0885\3\2\2\2\u016c\u0887\3\2\2")
        buf.write(u"\2\u016e\u0890\3\2\2\2\u0170\u0892\3\2\2\2\u0172\u08a1")
        buf.write(u"\3\2\2\2\u0174\u08a3\3\2\2\2\u0176\u08a5\3\2\2\2\u0178")
        buf.write(u"\u08ab\3\2\2\2\u017a\u08ad\3\2\2\2\u017c\u08b4\3\2\2")
        buf.write(u"\2\u017e\u08bf\3\2\2\2\u0180\u08c3\3\2\2\2\u0182\u08c7")
        buf.write(u"\3\2\2\2\u0184\u08d2\3\2\2\2\u0186\u08e1\3\2\2\2\u0188")
        buf.write(u"\u08e3\3\2\2\2\u018a\u08ec\3\2\2\2\u018c\u08ee\3\2\2")
        buf.write(u"\2\u018e\u08fd\3\2\2\2\u0190\u08ff\3\2\2\2\u0192\u0901")
        buf.write(u"\3\2\2\2\u0194\u0907\3\2\2\2\u0196\u0909\3\2\2\2\u0198")
        buf.write(u"\u0910\3\2\2\2\u019a\u091b\3\2\2\2\u019c\u091f\3\2\2")
        buf.write(u"\2\u019e\u0926\3\2\2\2\u01a0\u0935\3\2\2\2\u01a2\u0937")
        buf.write(u"\3\2\2\2\u01a4\u01a5\7[\2\2\u01a5\u01a6\5\u00be`\2\u01a6")
        buf.write(u"\u01a7\7K\2\2\u01a7\u01aa\7c\2\2\u01a8\u01ab\7U\2\2\u01a9")
        buf.write(u"\u01ab\5\u00be`\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2")
        buf.write(u"\2\2\u01ab\u01b1\3\2\2\2\u01ac\u01ad\5$\23\2\u01ad\u01ae")
        buf.write(u"\7\23\2\2\u01ae\u01af\7I\2\2\u01af\u01b2\3\2\2\2\u01b0")
        buf.write(u"\u01b2\7\u009b\2\2\u01b1\u01ac\3\2\2\2\u01b1\u01b0\3")
        buf.write(u"\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\5\u012e\u0098")
        buf.write(u"\2\u01b4\u01b5\7\21\2\2\u01b5\u01b6\5\u0086D\2\u01b6")
        buf.write(u"\u01b7\5\u0098M\2\u01b7\u01b8\5\u0088E\2\u01b8\3\3\2")
        buf.write(u"\2\2\u01b9\u01ba\7[\2\2\u01ba\u01bb\5\u00be`\2\u01bb")
        buf.write(u"\u01bc\7K\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\5\u00aa")
        buf.write(u"V\2\u01be\u01bf\7\u009b\2\2\u01bf\u01c0\5\u012e\u0098")
        buf.write(u"\2\u01c0\u01c1\7\21\2\2\u01c1\u01c2\5\u0086D\2\u01c2")
        buf.write(u"\u01c3\5\u0096L\2\u01c3\u01c4\5\u0088E\2\u01c4\5\3\2")
        buf.write(u"\2\2\u01c5\u01c6\5\u00c0a\2\u01c6\u01c7\7\u009b\2\2\u01c7")
        buf.write(u"\u01c8\5X-\2\u01c8\u01c9\7K\2\2\u01c9\u01ca\5\u012c\u0097")
        buf.write(u"\2\u01ca\7\3\2\2\2\u01cb\u01cc\5\u00c0a\2\u01cc\u01cf")
        buf.write(u"\5x=\2\u01cd\u01ce\7I\2\2\u01ce\u01d0\5z>\2\u01cf\u01cd")
        buf.write(u"\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\t\3\2\2\2\u01d1\u01d2")
        buf.write(u"\7[\2\2\u01d2\u01d3\5\u00bc_\2\u01d3\u01d5\7K\2\2\u01d4")
        buf.write(u"\u01d6\7\u0092\2\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3")
        buf.write(u"\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\5\u00a6T\2\u01d8")
        buf.write(u"\u01da\7N\2\2\u01d9\u01db\5\u009cO\2\u01da\u01d9\3\2")
        buf.write(u"\2\2\u01da\u01db\3\2\2\2\u01db\u01e5\3\2\2\2\u01dc\u01e2")
        buf.write(u"\7\u009b\2\2\u01dd\u01e0\5\u00e2r\2\u01de\u01df\7I\2")
        buf.write(u"\2\u01df\u01e1\5\u00ba^\2\u01e0\u01de\3\2\2\2\u01e0\u01e1")
        buf.write(u"\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01dd\3\2\2\2\u01e2")
        buf.write(u"\u01e3\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\7r\2\2")
        buf.write(u"\u01e5\u01dc\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\13\3\2")
        buf.write(u"\2\2\u01e7\u01e8\7[\2\2\u01e8\u01e9\5\u00be`\2\u01e9")
        buf.write(u"\u01eb\7K\2\2\u01ea\u01ec\7\u0092\2\2\u01eb\u01ea\3\2")
        buf.write(u"\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01f0")
        buf.write(u"\7U\2\2\u01ee\u01f0\5\20\t\2\u01ef\u01ed\3\2\2\2\u01ef")
        buf.write(u"\u01ee\3\2\2\2\u01f0\u0203\3\2\2\2\u01f1\u01fa\5$\23")
        buf.write(u"\2\u01f2\u01f3\7\23\2\2\u01f3\u01f4\7I\2\2\u01f4\u01f5")
        buf.write(u"\7w\2\2\u01f5\u01f6\7\21\2\2\u01f6\u01f7\5\u0086D\2\u01f7")
        buf.write(u"\u01f8\5\u00d0i\2\u01f8\u01f9\5\u0088E\2\u01f9\u01fb")
        buf.write(u"\3\2\2\2\u01fa\u01f2\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write(u"\u0204\3\2\2\2\u01fc\u01fd\7\u009b\2\2\u01fd\u01fe\7")
        buf.write(u"w\2\2\u01fe\u01ff\7\21\2\2\u01ff\u0200\5\u0086D\2\u0200")
        buf.write(u"\u0201\5\u00d0i\2\u0201\u0202\5\u0088E\2\u0202\u0204")
        buf.write(u"\3\2\2\2\u0203\u01f1\3\2\2\2\u0203\u01fc\3\2\2\2\u0203")
        buf.write(u"\u0204\3\2\2\2\u0204\r\3\2\2\2\u0205\u0206\7[\2\2\u0206")
        buf.write(u"\u0207\5\u00be`\2\u0207\u0208\7K\2\2\u0208\u021b\7\u0090")
        buf.write(u"\2\2\u0209\u0212\5$\23\2\u020a\u020b\7\23\2\2\u020b\u020c")
        buf.write(u"\7I\2\2\u020c\u020d\7w\2\2\u020d\u020e\7\21\2\2\u020e")
        buf.write(u"\u020f\5\u0086D\2\u020f\u0210\5\u00d0i\2\u0210\u0211")
        buf.write(u"\5\u0088E\2\u0211\u0213\3\2\2\2\u0212\u020a\3\2\2\2\u0212")
        buf.write(u"\u0213\3\2\2\2\u0213\u021c\3\2\2\2\u0214\u0215\7\u009b")
        buf.write(u"\2\2\u0215\u0216\7w\2\2\u0216\u0217\7\21\2\2\u0217\u0218")
        buf.write(u"\5\u0086D\2\u0218\u0219\5\u00d0i\2\u0219\u021a\5\u0088")
        buf.write(u"E\2\u021a\u021c\3\2\2\2\u021b\u0209\3\2\2\2\u021b\u0214")
        buf.write(u"\3\2\2\2\u021b\u021c\3\2\2\2\u021c\17\3\2\2\2\u021d\u0223")
        buf.write(u"\5\u00b4[\2\u021e\u021f\5\u00b4[\2\u021f\u0220\7I\2\2")
        buf.write(u"\u0220\u0221\5\u00be`\2\u0221\u0223\3\2\2\2\u0222\u021d")
        buf.write(u"\3\2\2\2\u0222\u021e\3\2\2\2\u0223\21\3\2\2\2\u0224\u0225")
        buf.write(u"\7[\2\2\u0225\u0226\5\u0124\u0093\2\u0226\u0227\7K\2")
        buf.write(u"\2\u0227\u0228\7\u0082\2\2\u0228\u0229\7\u0089\2\2\u0229")
        buf.write(u"\u022c\5\u00c6d\2\u022a\u022b\7\u008c\2\2\u022b\u022d")
        buf.write(u"\5\u00a6T\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write(u"\u022e\3\2\2\2\u022e\u022f\7_\2\2\u022f\u0230\7\21\2")
        buf.write(u"\2\u0230\u0231\5\u0086D\2\u0231\u0232\5\u00f2z\2\u0232")
        buf.write(u"\u0233\5\u0088E\2\u0233\23\3\2\2\2\u0234\u0235\7[\2\2")
        buf.write(u"\u0235\u0236\5\u00ba^\2\u0236\u0237\7K\2\2\u0237\u0238")
        buf.write(u"\7\u008f\2\2\u0238\u0239\7_\2\2\u0239\u023a\7\21\2\2")
        buf.write(u"\u023a\u023b\5\u0086D\2\u023b\u023c\5\u00f2z\2\u023c")
        buf.write(u"\u023d\5\u0088E\2\u023d\25\3\2\2\2\u023e\u023f\7[\2\2")
        buf.write(u"\u023f\u0240\5\u00ba^\2\u0240\u0242\7K\2\2\u0241\u0243")
        buf.write(u"\7z\2\2\u0242\u0241\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write(u"\u0244\3\2\2\2\u0244\u0245\7\u008f\2\2\u0245\u0246\7")
        buf.write(u"_\2\2\u0246\u0247\7\21\2\2\u0247\u0248\5\u0086D\2\u0248")
        buf.write(u"\u0249\5\u00eav\2\u0249\u024a\5\u0088E\2\u024a\27\3\2")
        buf.write(u"\2\2\u024b\u024c\7[\2\2\u024c\u024d\5\u00ba^\2\u024d")
        buf.write(u"\u024e\7K\2\2\u024e\u024f\7n\2\2\u024f\u0250\7_\2\2\u0250")
        buf.write(u"\u0251\7\21\2\2\u0251\u0252\5\u0086D\2\u0252\u0253\5")
        buf.write(u"\u00f2z\2\u0253\u0254\5\u0088E\2\u0254\31\3\2\2\2\u0255")
        buf.write(u"\u0256\7[\2\2\u0256\u0257\5\u00ba^\2\u0257\u0259\7K\2")
        buf.write(u"\2\u0258\u025a\7z\2\2\u0259\u0258\3\2\2\2\u0259\u025a")
        buf.write(u"\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025c\7n\2\2\u025c")
        buf.write(u"\u025d\7_\2\2\u025d\u025e\7\21\2\2\u025e\u025f\5\u0086")
        buf.write(u"D\2\u025f\u0260\5\u00eav\2\u0260\u0261\5\u0088E\2\u0261")
        buf.write(u"\33\3\2\2\2\u0262\u0263\7[\2\2\u0263\u0264\5\u00be`\2")
        buf.write(u"\u0264\u0266\7K\2\2\u0265\u0267\7\u0092\2\2\u0266\u0265")
        buf.write(u"\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268\3\2\2\2\u0268")
        buf.write(u"\u0269\7z\2\2\u0269\u0271\7U\2\2\u026a\u026b\5$\23\2")
        buf.write(u"\u026b\u026c\7\23\2\2\u026c\u026d\7I\2\2\u026d\u026e")
        buf.write(u"\7P\2\2\u026e\u0272\3\2\2\2\u026f\u0270\7\u009b\2\2\u0270")
        buf.write(u"\u0272\7P\2\2\u0271\u026a\3\2\2\2\u0271\u026f\3\2\2\2")
        buf.write(u"\u0272\u0273\3\2\2\2\u0273\u0274\7\21\2\2\u0274\u0275")
        buf.write(u"\5\u0086D\2\u0275\u0276\5 \21\2\u0276\u027f\5\u0088E")
        buf.write(u"\2\u0277\u0278\5\u0084C\2\u0278\u0279\7I\2\2\u0279\u027a")
        buf.write(u"\7w\2\2\u027a\u027b\7\21\2\2\u027b\u027c\5\u0086D\2\u027c")
        buf.write(u"\u027d\5\u00d4k\2\u027d\u027e\5\u0088E\2\u027e\u0280")
        buf.write(u"\3\2\2\2\u027f\u0277\3\2\2\2\u027f\u0280\3\2\2\2\u0280")
        buf.write(u"\35\3\2\2\2\u0281\u0282\7[\2\2\u0282\u0283\5\u00be`\2")
        buf.write(u"\u0283\u0285\7K\2\2\u0284\u0286\7\u0092\2\2\u0285\u0284")
        buf.write(u"\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0287\3\2\2\2\u0287")
        buf.write(u"\u0288\7z\2\2\u0288\u0290\7\u008a\2\2\u0289\u028a\5$")
        buf.write(u"\23\2\u028a\u028b\7\23\2\2\u028b\u028c\7I\2\2\u028c\u028d")
        buf.write(u"\7P\2\2\u028d\u0291\3\2\2\2\u028e\u028f\7\u009b\2\2\u028f")
        buf.write(u"\u0291\7P\2\2\u0290\u0289\3\2\2\2\u0290\u028e\3\2\2\2")
        buf.write(u"\u0291\u0292\3\2\2\2\u0292\u0293\7\21\2\2\u0293\u0294")
        buf.write(u"\5\u0086D\2\u0294\u0295\5 \21\2\u0295\u029e\5\u0088E")
        buf.write(u"\2\u0296\u0297\5\u0084C\2\u0297\u0298\7I\2\2\u0298\u0299")
        buf.write(u"\7w\2\2\u0299\u029a\7\21\2\2\u029a\u029b\5\u0086D\2\u029b")
        buf.write(u"\u029c\5\u00d4k\2\u029c\u029d\5\u0088E\2\u029d\u029f")
        buf.write(u"\3\2\2\2\u029e\u0296\3\2\2\2\u029e\u029f\3\2\2\2\u029f")
        buf.write(u"\37\3\2\2\2\u02a0\u02a1\7[\2\2\u02a1\u02a2\7U\2\2\u02a2")
        buf.write(u"\u02a3\7P\2\2\u02a3\u02a4\7K\2\2\u02a4\u02a5\7\21\2\2")
        buf.write(u"\u02a5\u02a6\5\u0086D\2\u02a6\u02a7\5\"\22\2\u02a7\u02a8")
        buf.write(u"\5\u0088E\2\u02a8!\3\2\2\2\u02a9\u02aa\b\22\1\2\u02aa")
        buf.write(u"\u02ab\5\u00d8m\2\u02ab\u02b2\3\2\2\2\u02ac\u02ad\f\3")
        buf.write(u"\2\2\u02ad\u02ae\5\u0084C\2\u02ae\u02af\5\u00d8m\2\u02af")
        buf.write(u"\u02b1\3\2\2\2\u02b0\u02ac\3\2\2\2\u02b1\u02b4\3\2\2")
        buf.write(u"\2\u02b2\u02b0\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3#\3\2")
        buf.write(u"\2\2\u02b4\u02b2\3\2\2\2\u02b5\u02b6\7\u009b\2\2\u02b6")
        buf.write(u"\u02b7\7N\2\2\u02b7\u02c0\5\u00bc_\2\u02b8\u02b9\7\u009b")
        buf.write(u"\2\2\u02b9\u02ba\7O\2\2\u02ba\u02bd\5\u00e4s\2\u02bb")
        buf.write(u"\u02bc\7I\2\2\u02bc\u02be\5\u00bc_\2\u02bd\u02bb\3\2")
        buf.write(u"\2\2\u02bd\u02be\3\2\2\2\u02be\u02c0\3\2\2\2\u02bf\u02b5")
        buf.write(u"\3\2\2\2\u02bf\u02b8\3\2\2\2\u02c0%\3\2\2\2\u02c1\u02c2")
        buf.write(u"\7[\2\2\u02c2\u02c3\5\u00b6\\\2\u02c3\u02c4\7K\2\2\u02c4")
        buf.write(u"\u02c5\7F\2\2\u02c5\u02c8\7v\2\2\u02c6\u02c7\7\u0089")
        buf.write(u"\2\2\u02c7\u02c9\5\60\31\2\u02c8\u02c6\3\2\2\2\u02c8")
        buf.write(u"\u02c9\3\2\2\2\u02c9\u02cc\3\2\2\2\u02ca\u02cb\7\u008c")
        buf.write(u"\2\2\u02cb\u02cd\5\u00a6T\2\u02cc\u02ca\3\2\2\2\u02cc")
        buf.write(u"\u02cd\3\2\2\2\u02cd\'\3\2\2\2\u02ce\u02cf\7[\2\2\u02cf")
        buf.write(u"\u02d0\5\u00b6\\\2\u02d0\u02d1\7K\2\2\u02d1\u02d4\7v")
        buf.write(u"\2\2\u02d2\u02d3\7\u0089\2\2\u02d3\u02d5\5\60\31\2\u02d4")
        buf.write(u"\u02d2\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u02d8\3\2\2")
        buf.write(u"\2\u02d6\u02d7\7\u008c\2\2\u02d7\u02d9\5\u00a6T\2\u02d8")
        buf.write(u"\u02d6\3\2\2\2\u02d8\u02d9\3\2\2\2\u02d9\u02da\3\2\2")
        buf.write(u"\2\u02da\u02db\7_\2\2\u02db\u02dc\7\21\2\2\u02dc\u02dd")
        buf.write(u"\5\u0086D\2\u02dd\u02de\5\u00f2z\2\u02de\u02df\5\u0088")
        buf.write(u"E\2\u02df)\3\2\2\2\u02e0\u02e1\7[\2\2\u02e1\u02e2\5\u00b6")
        buf.write(u"\\\2\u02e2\u02e4\7K\2\2\u02e3\u02e5\7z\2\2\u02e4\u02e3")
        buf.write(u"\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6")
        buf.write(u"\u02e9\7v\2\2\u02e7\u02e8\7\u0089\2\2\u02e8\u02ea\5\60")
        buf.write(u"\31\2\u02e9\u02e7\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea\u02ed")
        buf.write(u"\3\2\2\2\u02eb\u02ec\7\u008c\2\2\u02ec\u02ee\5\u00cc")
        buf.write(u"g\2\u02ed\u02eb\3\2\2\2\u02ed\u02ee\3\2\2\2\u02ee\u02ef")
        buf.write(u"\3\2\2\2\u02ef\u02f0\7_\2\2\u02f0\u02f1\7\21\2\2\u02f1")
        buf.write(u"\u02f2\5\u0086D\2\u02f2\u02f3\5\u00eav\2\u02f3\u02f4")
        buf.write(u"\5\u0088E\2\u02f4+\3\2\2\2\u02f5\u02f6\7[\2\2\u02f6\u02f7")
        buf.write(u"\7\u00a9\2\2\u02f7\u02f8\7K\2\2\u02f8\u02f9\7\u0095\2")
        buf.write(u"\2\u02f9\u02fa\7v\2\2\u02fa\u02fb\7_\2\2\u02fb\u02fc")
        buf.write(u"\7\21\2\2\u02fc\u02fd\5\u0086D\2\u02fd\u02fe\5\u00f2")
        buf.write(u"z\2\u02fe\u02ff\5\u0088E\2\u02ff\u0300\5\u0084C\2\u0300")
        buf.write(u"\u0301\7I\2\2\u0301\u0308\7\u009a\2\2\u0302\u0303\7\21")
        buf.write(u"\2\2\u0303\u0304\5\u0086D\2\u0304\u0305\5\u00f4{\2\u0305")
        buf.write(u"\u0306\5\u0088E\2\u0306\u0309\3\2\2\2\u0307\u0309\5\u00c0")
        buf.write(u"a\2\u0308\u0302\3\2\2\2\u0308\u0307\3\2\2\2\u0309-\3")
        buf.write(u"\2\2\2\u030a\u030b\5X-\2\u030b/\3\2\2\2\u030c\u030f\5")
        buf.write(u"\u00c2b\2\u030d\u030e\7I\2\2\u030e\u0310\5\u00c4c\2\u030f")
        buf.write(u"\u030d\3\2\2\2\u030f\u0310\3\2\2\2\u0310\61\3\2\2\2\u0311")
        buf.write(u"\u0312\5\u00ccg\2\u0312\u0314\5\u00ba^\2\u0313\u0315")
        buf.write(u"\5$\23\2\u0314\u0313\3\2\2\2\u0314\u0315\3\2\2\2\u0315")
        buf.write(u"\u0318\3\2\2\2\u0316\u0317\7-\2\2\u0317\u0319\5\u0106")
        buf.write(u"\u0084\2\u0318\u0316\3\2\2\2\u0318\u0319\3\2\2\2\u0319")
        buf.write(u"\63\3\2\2\2\u031a\u032e\5|?\2\u031b\u032e\5:\36\2\u031c")
        buf.write(u"\u032e\5\u0080A\2\u031d\u032e\58\35\2\u031e\u032e\5\66")
        buf.write(u"\34\2\u031f\u032e\5T+\2\u0320\u032e\5V,\2\u0321\u032e")
        buf.write(u"\5J&\2\u0322\u032e\5@!\2\u0323\u032e\5D#\2\u0324\u032e")
        buf.write(u"\5H%\2\u0325\u032e\5F$\2\u0326\u032e\5N(\2\u0327\u032e")
        buf.write(u"\5P)\2\u0328\u032e\5l\67\2\u0329\u032e\5<\37\2\u032a")
        buf.write(u"\u032e\5> \2\u032b\u032e\5(\25\2\u032c\u032e\5\u00e8")
        buf.write(u"u\2\u032d\u031a\3\2\2\2\u032d\u031b\3\2\2\2\u032d\u031c")
        buf.write(u"\3\2\2\2\u032d\u031d\3\2\2\2\u032d\u031e\3\2\2\2\u032d")
        buf.write(u"\u031f\3\2\2\2\u032d\u0320\3\2\2\2\u032d\u0321\3\2\2")
        buf.write(u"\2\u032d\u0322\3\2\2\2\u032d\u0323\3\2\2\2\u032d\u0324")
        buf.write(u"\3\2\2\2\u032d\u0325\3\2\2\2\u032d\u0326\3\2\2\2\u032d")
        buf.write(u"\u0327\3\2\2\2\u032d\u0328\3\2\2\2\u032d\u0329\3\2\2")
        buf.write(u"\2\u032d\u032a\3\2\2\2\u032d\u032b\3\2\2\2\u032d\u032c")
        buf.write(u"\3\2\2\2\u032e\65\3\2\2\2\u032f\u0330\7k\2\2\u0330\67")
        buf.write(u"\3\2\2\2\u0331\u0332\7\\\2\2\u0332\u033c\5\u00a2R\2\u0333")
        buf.write(u"\u0334\7\u0093\2\2\u0334\u033c\5\u00a2R\2\u0335\u0336")
        buf.write(u"\7\\\2\2\u0336\u0337\5\u00a2R\2\u0337\u0338\7I\2\2\u0338")
        buf.write(u"\u0339\7\u0093\2\2\u0339\u033a\5\u00a2R\2\u033a\u033c")
        buf.write(u"\3\2\2\2\u033b\u0331\3\2\2\2\u033b\u0333\3\2\2\2\u033b")
        buf.write(u"\u0335\3\2\2\2\u033c9\3\2\2\2\u033d\u033f\5Z.\2\u033e")
        buf.write(u"\u0340\5v<\2\u033f\u033e\3\2\2\2\u033f\u0340\3\2\2\2")
        buf.write(u"\u0340\u0343\3\2\2\2\u0341\u0343\5^\60\2\u0342\u033d")
        buf.write(u"\3\2\2\2\u0342\u0341\3\2\2\2\u0343;\3\2\2\2\u0344\u0345")
        buf.write(u"\7\u009b\2\2\u0345\u0346\5\u0116\u008c\2\u0346\u0347")
        buf.write(u"\7\23\2\2\u0347\u0348\7^\2\2\u0348\u0349\7\21\2\2\u0349")
        buf.write(u"\u034a\5\u0086D\2\u034a\u034b\5\u00f2z\2\u034b\u034c")
        buf.write(u"\5\u0088E\2\u034c=\3\2\2\2\u034d\u034e\7\u009b\2\2\u034e")
        buf.write(u"\u034f\5\u00be`\2\u034f\u0350\7\23\2\2\u0350\u0351\7")
        buf.write(u"^\2\2\u0351\u0352\7\21\2\2\u0352\u0353\5\u0086D\2\u0353")
        buf.write(u"\u0354\5\u00f2z\2\u0354\u0355\5\u0088E\2\u0355?\3\2\2")
        buf.write(u"\2\u0356\u0357\7\u0094\2\2\u0357\u0358\7\177\2\2\u0358")
        buf.write(u"\u0359\5X-\2\u0359\u035a\7\21\2\2\u035a\u035b\5\u0086")
        buf.write(u"D\2\u035b\u0363\5\u00f6|\2\u035c\u035d\5\u0084C\2\u035d")
        buf.write(u"\u035e\7\u0085\2\2\u035e\u035f\7\21\2\2\u035f\u0360\5")
        buf.write(u"\u0086D\2\u0360\u0361\5\u00f2z\2\u0361\u0362\5\u0088")
        buf.write(u"E\2\u0362\u0364\3\2\2\2\u0363\u035c\3\2\2\2\u0363\u0364")
        buf.write(u"\3\2\2\2\u0364\u0365\3\2\2\2\u0365\u0366\5\u0088E\2\u0366")
        buf.write(u"A\3\2\2\2\u0367\u0368\7\u009c\2\2\u0368\u0369\5\u00fc")
        buf.write(u"\177\2\u0369\u036a\7\21\2\2\u036a\u036b\5\u0086D\2\u036b")
        buf.write(u"\u036c\5\u00f2z\2\u036c\u036d\5\u0088E\2\u036d\u0377")
        buf.write(u"\3\2\2\2\u036e\u036f\7\u009c\2\2\u036f\u0370\7q\2\2\u0370")
        buf.write(u"\u0371\5\u00fa~\2\u0371\u0372\7\21\2\2\u0372\u0373\5")
        buf.write(u"\u0086D\2\u0373\u0374\5\u00f2z\2\u0374\u0375\5\u0088")
        buf.write(u"E\2\u0375\u0377\3\2\2\2\u0376\u0367\3\2\2\2\u0376\u036e")
        buf.write(u"\3\2\2\2\u0377C\3\2\2\2\u0378\u0379\7l\2\2\u0379\u037a")
        buf.write(u"\7`\2\2\u037a\u037d\5\u00ba^\2\u037b\u037c\7\23\2\2\u037c")
        buf.write(u"\u037e\5\u00ba^\2\u037d\u037b\3\2\2\2\u037d\u037e\3\2")
        buf.write(u"\2\2\u037e\u037f\3\2\2\2\u037f\u0380\7q\2\2\u0380\u0381")
        buf.write(u"\5X-\2\u0381\u0382\7\21\2\2\u0382\u0383\5\u0086D\2\u0383")
        buf.write(u"\u0384\5\u00f2z\2\u0384\u0385\5\u0088E\2\u0385E\3\2\2")
        buf.write(u"\2\u0386\u0387\7^\2\2\u0387\u0388\7\21\2\2\u0388\u0389")
        buf.write(u"\5\u0086D\2\u0389\u038a\5\u00f2z\2\u038a\u038b\5\u0088")
        buf.write(u"E\2\u038b\u038c\5\u0084C\2\u038c\u038d\7\u009e\2\2\u038d")
        buf.write(u"\u038e\5X-\2\u038eG\3\2\2\2\u038f\u0390\7\u009e\2\2\u0390")
        buf.write(u"\u0391\5X-\2\u0391\u0392\7\21\2\2\u0392\u0393\5\u0086")
        buf.write(u"D\2\u0393\u0394\5\u00f2z\2\u0394\u0395\5\u0088E\2\u0395")
        buf.write(u"I\3\2\2\2\u0396\u0397\7p\2\2\u0397\u0398\5X-\2\u0398")
        buf.write(u"\u0399\7\21\2\2\u0399\u039a\5\u0086D\2\u039a\u039b\5")
        buf.write(u"\u00f2z\2\u039b\u039f\5\u0088E\2\u039c\u039d\5\u0084")
        buf.write(u"C\2\u039d\u039e\5L\'\2\u039e\u03a0\3\2\2\2\u039f\u039c")
        buf.write(u"\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0\u03a8\3\2\2\2\u03a1")
        buf.write(u"\u03a2\5\u0084C\2\u03a2\u03a3\7a\2\2\u03a3\u03a4\7\21")
        buf.write(u"\2\2\u03a4\u03a5\5\u0086D\2\u03a5\u03a6\5\u00f2z\2\u03a6")
        buf.write(u"\u03a7\5\u0088E\2\u03a7\u03a9\3\2\2\2\u03a8\u03a1\3\2")
        buf.write(u"\2\2\u03a8\u03a9\3\2\2\2\u03a9K\3\2\2\2\u03aa\u03ab\b")
        buf.write(u"\'\1\2\u03ab\u03ac\7a\2\2\u03ac\u03ad\7p\2\2\u03ad\u03ae")
        buf.write(u"\5X-\2\u03ae\u03af\7\21\2\2\u03af\u03b0\5\u0086D\2\u03b0")
        buf.write(u"\u03b1\5\u00f2z\2\u03b1\u03b2\5\u0088E\2\u03b2\u03bf")
        buf.write(u"\3\2\2\2\u03b3\u03b4\f\3\2\2\u03b4\u03b5\5\u0084C\2\u03b5")
        buf.write(u"\u03b6\7a\2\2\u03b6\u03b7\7p\2\2\u03b7\u03b8\5X-\2\u03b8")
        buf.write(u"\u03b9\7\21\2\2\u03b9\u03ba\5\u0086D\2\u03ba\u03bb\5")
        buf.write(u"\u00f2z\2\u03bb\u03bc\5\u0088E\2\u03bc\u03be\3\2\2\2")
        buf.write(u"\u03bd\u03b3\3\2\2\2\u03be\u03c1\3\2\2\2\u03bf\u03bd")
        buf.write(u"\3\2\2\2\u03bf\u03c0\3\2\2\2\u03c0M\3\2\2\2\u03c1\u03bf")
        buf.write(u"\3\2\2\2\u03c2\u03c3\7\u0087\2\2\u03c3\u03c4\5X-\2\u03c4")
        buf.write(u"O\3\2\2\2\u03c5\u03c6\7\u0094\2\2\u03c6\u03c7\7\177\2")
        buf.write(u"\2\u03c7\u03c8\5\u00ba^\2\u03c8\u03c9\7_\2\2\u03c9\u03ca")
        buf.write(u"\7\21\2\2\u03ca\u03cb\5\u0086D\2\u03cb\u03cc\5\u00f2")
        buf.write(u"z\2\u03cc\u03cd\5\u0088E\2\u03cd\u03cf\5\u0082B\2\u03ce")
        buf.write(u"\u03d0\5\u00f8}\2\u03cf\u03ce\3\2\2\2\u03cf\u03d0\3\2")
        buf.write(u"\2\2\u03d0\u03dc\3\2\2\2\u03d1\u03d5\7\u0085\2\2\u03d2")
        buf.write(u"\u03d3\7\u009c\2\2\u03d3\u03d5\7J\2\2\u03d4\u03d1\3\2")
        buf.write(u"\2\2\u03d4\u03d2\3\2\2\2\u03d5\u03d6\3\2\2\2\u03d6\u03d7")
        buf.write(u"\7\21\2\2\u03d7\u03d8\5\u0086D\2\u03d8\u03d9\5\u00f2")
        buf.write(u"z\2\u03d9\u03da\5\u0088E\2\u03da\u03db\5\u0082B\2\u03db")
        buf.write(u"\u03dd\3\2\2\2\u03dc\u03d4\3\2\2\2\u03dc\u03dd\3\2\2")
        buf.write(u"\2\u03dd\u03e5\3\2\2\2\u03de\u03df\7H\2\2\u03df\u03e0")
        buf.write(u"\7\21\2\2\u03e0\u03e1\5\u0086D\2\u03e1\u03e2\5\u00f2")
        buf.write(u"z\2\u03e2\u03e3\5\u0088E\2\u03e3\u03e4\5\u0082B\2\u03e4")
        buf.write(u"\u03e6\3\2\2\2\u03e5\u03de\3\2\2\2\u03e5\u03e6\3\2\2")
        buf.write(u"\2\u03e6\u03e7\3\2\2\2\u03e7\u03e8\5\u0082B\2\u03e8Q")
        buf.write(u"\3\2\2\2\u03e9\u03ea\7\u009c\2\2\u03ea\u03eb\5\u00c0")
        buf.write(u"a\2\u03eb\u03ec\7\21\2\2\u03ec\u03ed\5\u0086D\2\u03ed")
        buf.write(u"\u03ee\5\u00f2z\2\u03ee\u03ef\5\u0088E\2\u03ef\u03f0")
        buf.write(u"\5\u0082B\2\u03f0\u03fd\3\2\2\2\u03f1\u03f2\7\u009c\2")
        buf.write(u"\2\u03f2\u03f3\7q\2\2\u03f3\u03f4\7\30\2\2\u03f4\u03f5")
        buf.write(u"\5\u009aN\2\u03f5\u03f6\7\31\2\2\u03f6\u03f7\7\21\2\2")
        buf.write(u"\u03f7\u03f8\5\u0086D\2\u03f8\u03f9\5\u00f2z\2\u03f9")
        buf.write(u"\u03fa\5\u0088E\2\u03fa\u03fb\5\u0082B\2\u03fb\u03fd")
        buf.write(u"\3\2\2\2\u03fc\u03e9\3\2\2\2\u03fc\u03f1\3\2\2\2\u03fd")
        buf.write(u"S\3\2\2\2\u03fe\u03ff\7Q\2\2\u03ffU\3\2\2\2\u0400\u0402")
        buf.write(u"\7\u008b\2\2\u0401\u0403\5X-\2\u0402\u0401\3\2\2\2\u0402")
        buf.write(u"\u0403\3\2\2\2\u0403W\3\2\2\2\u0404\u0405\b-\1\2\u0405")
        buf.write(u"\u0421\5b\62\2\u0406\u0421\5Z.\2\u0407\u0408\5Z.\2\u0408")
        buf.write(u"\u0409\5v<\2\u0409\u0421\3\2\2\2\u040a\u040b\7#\2\2\u040b")
        buf.write(u"\u0421\5X-.\u040c\u040d\7|\2\2\u040d\u0421\5X--\u040e")
        buf.write(u"\u040f\7?\2\2\u040f\u0410\7\21\2\2\u0410\u0421\5X-\20")
        buf.write(u"\u0411\u0412\7e\2\2\u0412\u0413\7\21\2\2\u0413\u0421")
        buf.write(u"\5\u00ba^\2\u0414\u0415\7>\2\2\u0415\u0416\7\21\2\2\u0416")
        buf.write(u"\u0421\5\u00b6\\\2\u0417\u0421\5h\65\2\u0418\u0421\5")
        buf.write(u"f\64\2\u0419\u0421\5j\66\2\u041a\u0421\5r:\2\u041b\u0421")
        buf.write(u"\5\u011c\u008f\2\u041c\u0421\5\u011e\u0090\2\u041d\u0421")
        buf.write(u"\5t;\2\u041e\u0421\5n8\2\u041f\u0421\5^\60\2\u0420\u0404")
        buf.write(u"\3\2\2\2\u0420\u0406\3\2\2\2\u0420\u0407\3\2\2\2\u0420")
        buf.write(u"\u040a\3\2\2\2\u0420\u040c\3\2\2\2\u0420\u040e\3\2\2")
        buf.write(u"\2\u0420\u0411\3\2\2\2\u0420\u0414\3\2\2\2\u0420\u0417")
        buf.write(u"\3\2\2\2\u0420\u0418\3\2\2\2\u0420\u0419\3\2\2\2\u0420")
        buf.write(u"\u041a\3\2\2\2\u0420\u041b\3\2\2\2\u0420\u041c\3\2\2")
        buf.write(u"\2\u0420\u041d\3\2\2\2\u0420\u041e\3\2\2\2\u0420\u041f")
        buf.write(u"\3\2\2\2\u0421\u0492\3\2\2\2\u0422\u0423\f,\2\2\u0423")
        buf.write(u"\u0424\5\u0132\u009a\2\u0424\u0425\5X--\u0425\u0491\3")
        buf.write(u"\2\2\2\u0426\u0427\f+\2\2\u0427\u0428\5\u0134\u009b\2")
        buf.write(u"\u0428\u0429\5X-,\u0429\u0491\3\2\2\2\u042a\u042b\f*")
        buf.write(u"\2\2\u042b\u042c\5\u0138\u009d\2\u042c\u042d\5X-+\u042d")
        buf.write(u"\u0491\3\2\2\2\u042e\u042f\f)\2\2\u042f\u0430\5\u0136")
        buf.write(u"\u009c\2\u0430\u0431\5X-*\u0431\u0491\3\2\2\2\u0432\u0433")
        buf.write(u"\f(\2\2\u0433\u0434\t\2\2\2\u0434\u0491\5X-)\u0435\u0436")
        buf.write(u"\f&\2\2\u0436\u0437\7*\2\2\u0437\u0491\5X-\'\u0438\u0439")
        buf.write(u"\f%\2\2\u0439\u043a\7+\2\2\u043a\u0491\5X-&\u043b\u043c")
        buf.write(u"\f$\2\2\u043c\u043d\7(\2\2\u043d\u0491\5X-%\u043e\u043f")
        buf.write(u"\f#\2\2\u043f\u0440\7)\2\2\u0440\u0491\5X-$\u0441\u0442")
        buf.write(u"\f \2\2\u0442\u0443\7-\2\2\u0443\u0491\5X-!\u0444\u0445")
        buf.write(u"\f\37\2\2\u0445\u0446\7,\2\2\u0446\u0491\5X- \u0447\u0448")
        buf.write(u"\f\36\2\2\u0448\u0449\7\61\2\2\u0449\u0491\5X-\37\u044a")
        buf.write(u"\u044b\f\35\2\2\u044b\u044c\7X\2\2\u044c\u0491\5X-\36")
        buf.write(u"\u044d\u044e\f\34\2\2\u044e\u044f\7q\2\2\u044f\u0491")
        buf.write(u"\5X-\35\u0450\u0451\f\33\2\2\u0451\u0452\7o\2\2\u0452")
        buf.write(u"\u0491\5X-\34\u0453\u0454\f\32\2\2\u0454\u0455\7o\2\2")
        buf.write(u"\u0455\u0456\7G\2\2\u0456\u0491\5X-\33\u0457\u0458\f")
        buf.write(u"\31\2\2\u0458\u0459\7o\2\2\u0459\u045a\7J\2\2\u045a\u0491")
        buf.write(u"\5X-\32\u045b\u045c\f\30\2\2\u045c\u045d\7|\2\2\u045d")
        buf.write(u"\u045e\7X\2\2\u045e\u0491\5X-\31\u045f\u0460\f\27\2\2")
        buf.write(u"\u0460\u0461\7|\2\2\u0461\u0462\7q\2\2\u0462\u0491\5")
        buf.write(u"X-\30\u0463\u0464\f\26\2\2\u0464\u0465\7|\2\2\u0465\u0466")
        buf.write(u"\7o\2\2\u0466\u0491\5X-\27\u0467\u0468\f\25\2\2\u0468")
        buf.write(u"\u0469\7|\2\2\u0469\u046a\7o\2\2\u046a\u046b\7G\2\2\u046b")
        buf.write(u"\u0491\5X-\26\u046c\u046d\f\24\2\2\u046d\u046e\7|\2\2")
        buf.write(u"\u046e\u046f\7o\2\2\u046f\u0470\7J\2\2\u0470\u0491\5")
        buf.write(u"X-\25\u0471\u0472\f\23\2\2\u0472\u0473\7\u0083\2\2\u0473")
        buf.write(u"\u0491\5X-\24\u0474\u0475\f\22\2\2\u0475\u0476\7I\2\2")
        buf.write(u"\u0476\u0491\5X-\23\u0477\u0478\f\21\2\2\u0478\u0479")
        buf.write(u"\7p\2\2\u0479\u047a\5X-\2\u047a\u047b\7a\2\2\u047b\u047c")
        buf.write(u"\5X-\22\u047c\u0491\3\2\2\2\u047d\u047e\f\3\2\2\u047e")
        buf.write(u"\u047f\7l\2\2\u047f\u0480\7`\2\2\u0480\u0481\5\u00ba")
        buf.write(u"^\2\u0481\u0482\7q\2\2\u0482\u0483\5X-\4\u0483\u0491")
        buf.write(u"\3\2\2\2\u0484\u0485\f\'\2\2\u0485\u0486\7K\2\2\u0486")
        buf.write(u"\u0491\5\u00ccg\2\u0487\u0488\f\"\2\2\u0488\u0489\7t")
        buf.write(u"\2\2\u0489\u048a\7|\2\2\u048a\u0491\5\u011a\u008e\2\u048b")
        buf.write(u"\u048c\f!\2\2\u048c\u048d\7t\2\2\u048d\u0491\5\u011a")
        buf.write(u"\u008e\2\u048e\u048f\f\n\2\2\u048f\u0491\5p9\2\u0490")
        buf.write(u"\u0422\3\2\2\2\u0490\u0426\3\2\2\2\u0490\u042a\3\2\2")
        buf.write(u"\2\u0490\u042e\3\2\2\2\u0490\u0432\3\2\2\2\u0490\u0435")
        buf.write(u"\3\2\2\2\u0490\u0438\3\2\2\2\u0490\u043b\3\2\2\2\u0490")
        buf.write(u"\u043e\3\2\2\2\u0490\u0441\3\2\2\2\u0490\u0444\3\2\2")
        buf.write(u"\2\u0490\u0447\3\2\2\2\u0490\u044a\3\2\2\2\u0490\u044d")
        buf.write(u"\3\2\2\2\u0490\u0450\3\2\2\2\u0490\u0453\3\2\2\2\u0490")
        buf.write(u"\u0457\3\2\2\2\u0490\u045b\3\2\2\2\u0490\u045f\3\2\2")
        buf.write(u"\2\u0490\u0463\3\2\2\2\u0490\u0467\3\2\2\2\u0490\u046c")
        buf.write(u"\3\2\2\2\u0490\u0471\3\2\2\2\u0490\u0474\3\2\2\2\u0490")
        buf.write(u"\u0477\3\2\2\2\u0490\u047d\3\2\2\2\u0490\u0484\3\2\2")
        buf.write(u"\2\u0490\u0487\3\2\2\2\u0490\u048b\3\2\2\2\u0490\u048e")
        buf.write(u"\3\2\2\2\u0491\u0494\3\2\2\2\u0492\u0490\3\2\2\2\u0492")
        buf.write(u"\u0493\3\2\2\2\u0493Y\3\2\2\2\u0494\u0492\3\2\2\2\u0495")
        buf.write(u"\u0496\b.\1\2\u0496\u0497\5\u00b8]\2\u0497\u049c\3\2")
        buf.write(u"\2\2\u0498\u0499\f\3\2\2\u0499\u049b\5\\/\2\u049a\u0498")
        buf.write(u"\3\2\2\2\u049b\u049e\3\2\2\2\u049c\u049a\3\2\2\2\u049c")
        buf.write(u"\u049d\3\2\2\2\u049d[\3\2\2\2\u049e\u049c\3\2\2\2\u049f")
        buf.write(u"\u04a0\6/#\3\u04a0\u04a1\7\25\2\2\u04a1\u04a2\5\u00b8")
        buf.write(u"]\2\u04a2]\3\2\2\2\u04a3\u04a4\7s\2\2\u04a4\u04a5\7\21")
        buf.write(u"\2\2\u04a5\u04a6\5\u00ba^\2\u04a6\u04a7\5`\61\2\u04a7")
        buf.write(u"_\3\2\2\2\u04a8\u04a9\6\61$\3\u04a9a\3\2\2\2\u04aa\u04ab")
        buf.write(u"\b\62\1\2\u04ab\u04ac\5\u0100\u0081\2\u04ac\u04b1\3\2")
        buf.write(u"\2\2\u04ad\u04ae\f\3\2\2\u04ae\u04b0\5d\63\2\u04af\u04ad")
        buf.write(u"\3\2\2\2\u04b0\u04b3\3\2\2\2\u04b1\u04af\3\2\2\2\u04b1")
        buf.write(u"\u04b2\3\2\2\2\u04b2c\3\2\2\2\u04b3\u04b1\3\2\2\2\u04b4")
        buf.write(u"\u04b5\6\63&\3\u04b5\u04b6\7\25\2\2\u04b6\u04c2\5\u00ba")
        buf.write(u"^\2\u04b7\u04b8\6\63\'\3\u04b8\u04b9\7\30\2\2\u04b9\u04ba")
        buf.write(u"\5\u0114\u008b\2\u04ba\u04bb\7\31\2\2\u04bb\u04c2\3\2")
        buf.write(u"\2\2\u04bc\u04bd\6\63(\3\u04bd\u04be\7\30\2\2\u04be\u04bf")
        buf.write(u"\5X-\2\u04bf\u04c0\7\31\2\2\u04c0\u04c2\3\2\2\2\u04c1")
        buf.write(u"\u04b4\3\2\2\2\u04c1\u04b7\3\2\2\2\u04c1\u04bc\3\2\2")
        buf.write(u"\2\u04c2e\3\2\2\2\u04c3\u04c6\7@\2\2\u04c4\u04c5\7m\2")
        buf.write(u"\2\u04c5\u04c7\5X-\2\u04c6\u04c4\3\2\2\2\u04c6\u04c7")
        buf.write(u"\3\2\2\2\u04c7g\3\2\2\2\u04c8\u04c9\7A\2\2\u04c9\u04ca")
        buf.write(u"\7m\2\2\u04ca\u04cb\5X-\2\u04cbi\3\2\2\2\u04cc\u04cd")
        buf.write(u"\5\u00aeX\2\u04cd\u04ce\7m\2\2\u04ce\u04d7\5X-\2\u04cf")
        buf.write(u"\u04d1\7\23\2\2\u04d0\u04cf\3\2\2\2\u04d0\u04d1\3\2\2")
        buf.write(u"\2\u04d1\u04d2\3\2\2\2\u04d2\u04d5\5x=\2\u04d3\u04d4")
        buf.write(u"\7I\2\2\u04d4\u04d6\5z>\2\u04d5\u04d3\3\2\2\2\u04d5\u04d6")
        buf.write(u"\3\2\2\2\u04d6\u04d8\3\2\2\2\u04d7\u04d0\3\2\2\2\u04d7")
        buf.write(u"\u04d8\3\2\2\2\u04d8\u04e2\3\2\2\2\u04d9\u04df\5\u00ae")
        buf.write(u"X\2\u04da\u04dd\5x=\2\u04db\u04dc\7I\2\2\u04dc\u04de")
        buf.write(u"\5z>\2\u04dd\u04db\3\2\2\2\u04dd\u04de\3\2\2\2\u04de")
        buf.write(u"\u04e0\3\2\2\2\u04df\u04da\3\2\2\2\u04df\u04e0\3\2\2")
        buf.write(u"\2\u04e0\u04e2\3\2\2\2\u04e1\u04cc\3\2\2\2\u04e1\u04d9")
        buf.write(u"\3\2\2\2\u04e2k\3\2\2\2\u04e3\u04e4\7\u009f\2\2\u04e4")
        buf.write(u"\u04e5\5X-\2\u04e5\u04e6\7\u0098\2\2\u04e6\u04e7\5X-")
        buf.write(u"\2\u04e7m\3\2\2\2\u04e8\u04e9\5Z.\2\u04e9\u04ea\7#\2")
        buf.write(u"\2\u04ea\u04eb\5X-\2\u04ebo\3\2\2\2\u04ec\u04ed\7i\2")
        buf.write(u"\2\u04ed\u04ee\7\u009b\2\2\u04ee\u04ef\5\u00ba^\2\u04ef")
        buf.write(u"\u04f0\7\u009d\2\2\u04f0\u04f1\5X-\2\u04f1q\3\2\2\2\u04f2")
        buf.write(u"\u04f3\7h\2\2\u04f3\u04f5\7\u0080\2\2\u04f4\u04f6\5\u00ae")
        buf.write(u"X\2\u04f5\u04f4\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6\u04f7")
        buf.write(u"\3\2\2\2\u04f7\u04f8\7\u009d\2\2\u04f8\u0517\5X-\2\u04f9")
        buf.write(u"\u050b\7h\2\2\u04fa\u04fc\7G\2\2\u04fb\u04fd\5\u00ae")
        buf.write(u"X\2\u04fc\u04fb\3\2\2\2\u04fc\u04fd\3\2\2\2\u04fd\u050c")
        buf.write(u"\3\2\2\2\u04fe\u0500\5\u00aeX\2\u04ff\u0501\7\u008d\2")
        buf.write(u"\2\u0500\u04ff\3\2\2\2\u0500\u0501\3\2\2\2\u0501\u0502")
        buf.write(u"\3\2\2\2\u0502\u0503\5X-\2\u0503\u0504\7\u0098\2\2\u0504")
        buf.write(u"\u0505\5X-\2\u0505\u050c\3\2\2\2\u0506\u0507\7\u008d")
        buf.write(u"\2\2\u0507\u0508\5X-\2\u0508\u0509\7\u0098\2\2\u0509")
        buf.write(u"\u050a\5X-\2\u050a\u050c\3\2\2\2\u050b\u04fa\3\2\2\2")
        buf.write(u"\u050b\u04fe\3\2\2\2\u050b\u0506\3\2\2\2\u050c\u050f")
        buf.write(u"\3\2\2\2\u050d\u050e\7\u009d\2\2\u050e\u0510\5X-\2\u050f")
        buf.write(u"\u050d\3\2\2\2\u050f\u0510\3\2\2\2\u0510\u0514\3\2\2")
        buf.write(u"\2\u0511\u0512\7\u0084\2\2\u0512\u0513\7R\2\2\u0513\u0515")
        buf.write(u"\5\u0120\u0091\2\u0514\u0511\3\2\2\2\u0514\u0515\3\2")
        buf.write(u"\2\2\u0515\u0517\3\2\2\2\u0516\u04f2\3\2\2\2\u0516\u04f9")
        buf.write(u"\3\2\2\2\u0517s\3\2\2\2\u0518\u051a\7\u0091\2\2\u0519")
        buf.write(u"\u051b\7]\2\2\u051a\u0519\3\2\2\2\u051a\u051b\3\2\2\2")
        buf.write(u"\u051b\u051c\3\2\2\2\u051c\u0522\5b\62\2\u051d\u051e")
        buf.write(u"\7\u009b\2\2\u051e\u051f\5b\62\2\u051f\u0520\7K\2\2\u0520")
        buf.write(u"\u0521\5\u0128\u0095\2\u0521\u0523\3\2\2\2\u0522\u051d")
        buf.write(u"\3\2\2\2\u0522\u0523\3\2\2\2\u0523u\3\2\2\2\u0524\u0525")
        buf.write(u"\6<)\3\u0525\u052b\5X-\2\u0526\u0529\5x=\2\u0527\u0528")
        buf.write(u"\7I\2\2\u0528\u052a\5z>\2\u0529\u0527\3\2\2\2\u0529\u052a")
        buf.write(u"\3\2\2\2\u052a\u052c\3\2\2\2\u052b\u0526\3\2\2\2\u052b")
        buf.write(u"\u052c\3\2\2\2\u052c\u0533\3\2\2\2\u052d\u0530\5x=\2")
        buf.write(u"\u052e\u052f\7I\2\2\u052f\u0531\5z>\2\u0530\u052e\3\2")
        buf.write(u"\2\2\u0530\u0531\3\2\2\2\u0531\u0533\3\2\2\2\u0532\u0524")
        buf.write(u"\3\2\2\2\u0532\u052d\3\2\2\2\u0533w\3\2\2\2\u0534\u0535")
        buf.write(u"\b=\1\2\u0535\u0536\7\u009b\2\2\u0536\u0537\5z>\2\u0537")
        buf.write(u"\u053d\3\2\2\2\u0538\u0539\f\3\2\2\u0539\u053a\7\23\2")
        buf.write(u"\2\u053a\u053c\5z>\2\u053b\u0538\3\2\2\2\u053c\u053f")
        buf.write(u"\3\2\2\2\u053d\u053b\3\2\2\2\u053d\u053e\3\2\2\2\u053e")
        buf.write(u"y\3\2\2\2\u053f\u053d\3\2\2\2\u0540\u0541\5X-\2\u0541")
        buf.write(u"\u0542\7K\2\2\u0542\u0544\3\2\2\2\u0543\u0540\3\2\2\2")
        buf.write(u"\u0543\u0544\3\2\2\2\u0544\u0545\3\2\2\2\u0545\u0546")
        buf.write(u"\5\u00ba^\2\u0546{\3\2\2\2\u0547\u0548\5\u0118\u008d")
        buf.write(u"\2\u0548\u0549\5\u0130\u0099\2\u0549\u054a\5X-\2\u054a")
        buf.write(u"}\3\2\2\2\u054b\u054c\6@+\3\u054c\u054d\7\25\2\2\u054d")
        buf.write(u"\u0554\5\u00ba^\2\u054e\u054f\6@,\3\u054f\u0550\7\30")
        buf.write(u"\2\2\u0550\u0551\5X-\2\u0551\u0552\7\31\2\2\u0552\u0554")
        buf.write(u"\3\2\2\2\u0553\u054b\3\2\2\2\u0553\u054e\3\2\2\2\u0554")
        buf.write(u"\177\3\2\2\2\u0555\u0556\5\u00e2r\2\u0556\u0557\5\u0130")
        buf.write(u"\u0099\2\u0557\u0558\5X-\2\u0558\u0081\3\2\2\2\u0559")
        buf.write(u"\u055b\7\7\2\2\u055a\u0559\3\2\2\2\u055b\u055e\3\2\2")
        buf.write(u"\2\u055c\u055a\3\2\2\2\u055c\u055d\3\2\2\2\u055d\u0083")
        buf.write(u"\3\2\2\2\u055e\u055c\3\2\2\2\u055f\u0561\7\7\2\2\u0560")
        buf.write(u"\u055f\3\2\2\2\u0561\u0562\3\2\2\2\u0562\u0560\3\2\2")
        buf.write(u"\2\u0562\u0563\3\2\2\2\u0563\u0085\3\2\2\2\u0564\u0566")
        buf.write(u"\7\7\2\2\u0565\u0564\3\2\2\2\u0566\u0567\3\2\2\2\u0567")
        buf.write(u"\u0565\3\2\2\2\u0567\u0568\3\2\2\2\u0568\u0569\3\2\2")
        buf.write(u"\2\u0569\u056a\7\3\2\2\u056a\u0087\3\2\2\2\u056b\u056d")
        buf.write(u"\7\7\2\2\u056c\u056b\3\2\2\2\u056d\u0570\3\2\2\2\u056e")
        buf.write(u"\u056c\3\2\2\2\u056e\u056f\3\2\2\2\u056f\u0571\3\2\2")
        buf.write(u"\2\u0570\u056e\3\2\2\2\u0571\u0572\7\4\2\2\u0572\u0089")
        buf.write(u"\3\2\2\2\u0573\u0574\7}\2\2\u0574\u008b\3\2\2\2\u0575")
        buf.write(u"\u0577\5\u008eH\2\u0576\u0575\3\2\2\2\u0576\u0577\3\2")
        buf.write(u"\2\2\u0577\u0578\3\2\2\2\u0578\u0579\5\u0082B\2\u0579")
        buf.write(u"\u057a\7\2\2\3\u057a\u008d\3\2\2\2\u057b\u0581\5\u0090")
        buf.write(u"I\2\u057c\u057d\5\u0084C\2\u057d\u057e\5\u0090I\2\u057e")
        buf.write(u"\u0580\3\2\2\2\u057f\u057c\3\2\2\2\u0580\u0583\3\2\2")
        buf.write(u"\2\u0581\u057f\3\2\2\2\u0581\u0582\3\2\2\2\u0582\u008f")
        buf.write(u"\3\2\2\2\u0583\u0581\3\2\2\2\u0584\u0585\5\u00e8u\2\u0585")
        buf.write(u"\u0586\5\u0084C\2\u0586\u0588\3\2\2\2\u0587\u0584\3\2")
        buf.write(u"\2\2\u0588\u058b\3\2\2\2\u0589\u0587\3\2\2\2\u0589\u058a")
        buf.write(u"\3\2\2\2\u058a\u0591\3\2\2\2\u058b\u0589\3\2\2\2\u058c")
        buf.write(u"\u0592\5\n\6\2\u058d\u0592\5\u00b2Z\2\u058e\u0592\5\u0092")
        buf.write(u"J\2\u058f\u0592\5\u0094K\2\u0590\u0592\5\u00e6t\2\u0591")
        buf.write(u"\u058c\3\2\2\2\u0591\u058d\3\2\2\2\u0591\u058e\3\2\2")
        buf.write(u"\2\u0591\u058f\3\2\2\2\u0591\u0590\3\2\2\2\u0592\u0091")
        buf.write(u"\3\2\2\2\u0593\u0594\5\36\20\2\u0594\u0093\3\2\2\2\u0595")
        buf.write(u"\u0598\5\2\2\2\u0596\u0598\5\4\3\2\u0597\u0595\3\2\2")
        buf.write(u"\2\u0597\u0596\3\2\2\2\u0598\u0095\3\2\2\2\u0599\u059f")
        buf.write(u"\5\6\4\2\u059a\u059b\5\u0084C\2\u059b\u059c\5\6\4\2\u059c")
        buf.write(u"\u059e\3\2\2\2\u059d\u059a\3\2\2\2\u059e\u05a1\3\2\2")
        buf.write(u"\2\u059f\u059d\3\2\2\2\u059f\u05a0\3\2\2\2\u05a0\u0097")
        buf.write(u"\3\2\2\2\u05a1\u059f\3\2\2\2\u05a2\u05a8\5\b\5\2\u05a3")
        buf.write(u"\u05a4\5\u0084C\2\u05a4\u05a5\5\b\5\2\u05a5\u05a7\3\2")
        buf.write(u"\2\2\u05a6\u05a3\3\2\2\2\u05a7\u05aa\3\2\2\2\u05a8\u05a6")
        buf.write(u"\3\2\2\2\u05a8\u05a9\3\2\2\2\u05a9\u0099\3\2\2\2\u05aa")
        buf.write(u"\u05a8\3\2\2\2\u05ab\u05b0\5\u00c0a\2\u05ac\u05ad\7\23")
        buf.write(u"\2\2\u05ad\u05af\5\u00c0a\2\u05ae\u05ac\3\2\2\2\u05af")
        buf.write(u"\u05b2\3\2\2\2\u05b0\u05ae\3\2\2\2\u05b0\u05b1\3\2\2")
        buf.write(u"\2\u05b1\u009b\3\2\2\2\u05b2\u05b0\3\2\2\2\u05b3\u05b4")
        buf.write(u"\7q\2\2\u05b4\u05be\5\u009eP\2\u05b5\u05b6\7q\2\2\u05b6")
        buf.write(u"\u05be\5\u00a0Q\2\u05b7\u05b8\7q\2\2\u05b8\u05be\5\u00a4")
        buf.write(u"S\2\u05b9\u05ba\7u\2\2\u05ba\u05be\7\u00a9\2\2\u05bb")
        buf.write(u"\u05bc\7u\2\2\u05bc\u05be\5X-\2\u05bd\u05b3\3\2\2\2\u05bd")
        buf.write(u"\u05b5\3\2\2\2\u05bd\u05b7\3\2\2\2\u05bd\u05b9\3\2\2")
        buf.write(u"\2\u05bd\u05bb\3\2\2\2\u05be\u009d\3\2\2\2\u05bf\u05c1")
        buf.write(u"\7y\2\2\u05c0\u05bf\3\2\2\2\u05c0\u05c1\3\2\2\2\u05c1")
        buf.write(u"\u05c2\3\2\2\2\u05c2\u05c4\7\30\2\2\u05c3\u05c5\5\u00a2")
        buf.write(u"R\2\u05c4\u05c3\3\2\2\2\u05c4\u05c5\3\2\2\2\u05c5\u05c6")
        buf.write(u"\3\2\2\2\u05c6\u05c7\7\31\2\2\u05c7\u009f\3\2\2\2\u05c8")
        buf.write(u"\u05ca\7y\2\2\u05c9\u05c8\3\2\2\2\u05c9\u05ca\3\2\2\2")
        buf.write(u"\u05ca\u05cb\3\2\2\2\u05cb\u05cd\7*\2\2\u05cc\u05ce\5")
        buf.write(u"\u00a2R\2\u05cd\u05cc\3\2\2\2\u05cd\u05ce\3\2\2\2\u05ce")
        buf.write(u"\u05cf\3\2\2\2\u05cf\u05d0\7(\2\2\u05d0\u00a1\3\2\2\2")
        buf.write(u"\u05d1\u05d6\5X-\2\u05d2\u05d3\7\23\2\2\u05d3\u05d5\5")
        buf.write(u"X-\2\u05d4\u05d2\3\2\2\2\u05d5\u05d8\3\2\2\2\u05d6\u05d4")
        buf.write(u"\3\2\2\2\u05d6\u05d7\3\2\2\2\u05d7\u00a3\3\2\2\2\u05d8")
        buf.write(u"\u05d6\3\2\2\2\u05d9\u05da\7\30\2\2\u05da\u05db\5X-\2")
        buf.write(u"\u05db\u05dc\7\24\2\2\u05dc\u05dd\5X-\2\u05dd\u05de\7")
        buf.write(u"\31\2\2\u05de\u00a5\3\2\2\2\u05df\u05e0\bT\1\2\u05e0")
        buf.write(u"\u05ec\5\u00a8U\2\u05e1\u05e2\7E\2\2\u05e2\u05e3\7*\2")
        buf.write(u"\2\u05e3\u05e4\5\u00a6T\2\u05e4\u05e5\7(\2\2\u05e5\u05ec")
        buf.write(u"\3\2\2\2\u05e6\u05e7\7D\2\2\u05e7\u05e8\7*\2\2\u05e8")
        buf.write(u"\u05e9\5\u00a6T\2\u05e9\u05ea\7(\2\2\u05ea\u05ec\3\2")
        buf.write(u"\2\2\u05eb\u05df\3\2\2\2\u05eb\u05e1\3\2\2\2\u05eb\u05e6")
        buf.write(u"\3\2\2\2\u05ec\u05f7\3\2\2\2\u05ed\u05ee\f\7\2\2\u05ee")
        buf.write(u"\u05f6\7,\2\2\u05ef\u05f0\f\6\2\2\u05f0\u05f1\7\30\2")
        buf.write(u"\2\u05f1\u05f6\7\31\2\2\u05f2\u05f3\f\5\2\2\u05f3\u05f4")
        buf.write(u"\7\32\2\2\u05f4\u05f6\7\33\2\2\u05f5\u05ed\3\2\2\2\u05f5")
        buf.write(u"\u05ef\3\2\2\2\u05f5\u05f2\3\2\2\2\u05f6\u05f9\3\2\2")
        buf.write(u"\2\u05f7\u05f5\3\2\2\2\u05f7\u05f8\3\2\2\2\u05f8\u00a7")
        buf.write(u"\3\2\2\2\u05f9\u05f7\3\2\2\2\u05fa\u05fd\5\u00aaV\2\u05fb")
        buf.write(u"\u05fd\5\u00acW\2\u05fc\u05fa\3\2\2\2\u05fc\u05fb\3\2")
        buf.write(u"\2\2\u05fd\u00a9\3\2\2\2\u05fe\u060e\7\64\2\2\u05ff\u060e")
        buf.write(u"\7\65\2\2\u0600\u060e\7\66\2\2\u0601\u060e\7B\2\2\u0602")
        buf.write(u"\u060e\7\67\2\2\u0603\u060e\78\2\2\u0604\u060e\7@\2\2")
        buf.write(u"\u0605\u060e\79\2\2\u0606\u060e\7;\2\2\u0607\u060e\7")
        buf.write(u":\2\2\u0608\u060e\7<\2\2\u0609\u060e\7=\2\2\u060a\u060e")
        buf.write(u"\7?\2\2\u060b\u060e\7A\2\2\u060c\u060e\7C\2\2\u060d\u05fe")
        buf.write(u"\3\2\2\2\u060d\u05ff\3\2\2\2\u060d\u0600\3\2\2\2\u060d")
        buf.write(u"\u0601\3\2\2\2\u060d\u0602\3\2\2\2\u060d\u0603\3\2\2")
        buf.write(u"\2\u060d\u0604\3\2\2\2\u060d\u0605\3\2\2\2\u060d\u0606")
        buf.write(u"\3\2\2\2\u060d\u0607\3\2\2\2\u060d\u0608\3\2\2\2\u060d")
        buf.write(u"\u0609\3\2\2\2\u060d\u060a\3\2\2\2\u060d\u060b\3\2\2")
        buf.write(u"\2\u060d\u060c\3\2\2\2\u060e\u00ab\3\2\2\2\u060f\u0610")
        buf.write(u"\7\u00a5\2\2\u0610\u00ad\3\2\2\2\u0611\u0613\7y\2\2\u0612")
        buf.write(u"\u0611\3\2\2\2\u0612\u0613\3\2\2\2\u0613\u0614\3\2\2")
        buf.write(u"\2\u0614\u0615\5\u00acW\2\u0615\u00af\3\2\2\2\u0616\u0617")
        buf.write(u"\7?\2\2\u0617\u00b1\3\2\2\2\u0618\u061c\5\f\7\2\u0619")
        buf.write(u"\u061c\5\34\17\2\u061a\u061c\5\16\b\2\u061b\u0618\3\2")
        buf.write(u"\2\2\u061b\u0619\3\2\2\2\u061b\u061a\3\2\2\2\u061c\u00b3")
        buf.write(u"\3\2\2\2\u061d\u0622\5\u00be`\2\u061e\u061f\7\23\2\2")
        buf.write(u"\u061f\u0621\5\u00be`\2\u0620\u061e\3\2\2\2\u0621\u0624")
        buf.write(u"\3\2\2\2\u0622\u0620\3\2\2\2\u0622\u0623\3\2\2\2\u0623")
        buf.write(u"\u00b5\3\2\2\2\u0624\u0622\3\2\2\2\u0625\u0628\5\u00ba")
        buf.write(u"^\2\u0626\u0628\5\u00be`\2\u0627\u0625\3\2\2\2\u0627")
        buf.write(u"\u0626\3\2\2\2\u0628\u00b7\3\2\2\2\u0629\u062d\5\u00ba")
        buf.write(u"^\2\u062a\u062d\5\u00be`\2\u062b\u062d\5\u00c0a\2\u062c")
        buf.write(u"\u0629\3\2\2\2\u062c\u062a\3\2\2\2\u062c\u062b\3\2\2")
        buf.write(u"\2\u062d\u00b9\3\2\2\2\u062e\u062f\7\u00a6\2\2\u062f")
        buf.write(u"\u00bb\3\2\2\2\u0630\u0631\t\3\2\2\u0631\u00bd\3\2\2")
        buf.write(u"\2\u0632\u0633\7\u00a5\2\2\u0633\u00bf\3\2\2\2\u0634")
        buf.write(u"\u0635\7\u00a4\2\2\u0635\u00c1\3\2\2\2\u0636\u063b\5")
        buf.write(u"\u00c4c\2\u0637\u0638\7\23\2\2\u0638\u063a\5\u00c4c\2")
        buf.write(u"\u0639\u0637\3\2\2\2\u063a\u063d\3\2\2\2\u063b\u0639")
        buf.write(u"\3\2\2\2\u063b\u063c\3\2\2\2\u063c\u00c3\3\2\2\2\u063d")
        buf.write(u"\u063b\3\2\2\2\u063e\u0644\5\u00caf\2\u063f\u0641\7y")
        buf.write(u"\2\2\u0640\u063f\3\2\2\2\u0640\u0641\3\2\2\2\u0641\u0642")
        buf.write(u"\3\2\2\2\u0642\u0644\5\u00c6d\2\u0643\u063e\3\2\2\2\u0643")
        buf.write(u"\u0640\3\2\2\2\u0644\u00c5\3\2\2\2\u0645\u0648\5\u00c8")
        buf.write(u"e\2\u0646\u0648\5\62\32\2\u0647\u0645\3\2\2\2\u0647\u0646")
        buf.write(u"\3\2\2\2\u0648\u00c7\3\2\2\2\u0649\u064c\5\u00ba^\2\u064a")
        buf.write(u"\u064b\7-\2\2\u064b\u064d\5\u0106\u0084\2\u064c\u064a")
        buf.write(u"\3\2\2\2\u064c\u064d\3\2\2\2\u064d\u00c9\3\2\2\2\u064e")
        buf.write(u"\u064f\5\u00b0Y\2\u064f\u0650\5\u00ba^\2\u0650\u00cb")
        buf.write(u"\3\2\2\2\u0651\u0654\5\u00a6T\2\u0652\u0654\5\u00ceh")
        buf.write(u"\2\u0653\u0651\3\2\2\2\u0653\u0652\3\2\2\2\u0654\u00cd")
        buf.write(u"\3\2\2\2\u0655\u0656\bh\1\2\u0656\u0657\7J\2\2\u0657")
        buf.write(u"\u0660\3\2\2\2\u0658\u0659\f\4\2\2\u0659\u065a\7\30\2")
        buf.write(u"\2\u065a\u065f\7\31\2\2\u065b\u065c\f\3\2\2\u065c\u065d")
        buf.write(u"\7\32\2\2\u065d\u065f\7\33\2\2\u065e\u0658\3\2\2\2\u065e")
        buf.write(u"\u065b\3\2\2\2\u065f\u0662\3\2\2\2\u0660\u065e\3\2\2")
        buf.write(u"\2\u0660\u0661\3\2\2\2\u0661\u00cf\3\2\2\2\u0662\u0660")
        buf.write(u"\3\2\2\2\u0663\u0669\5\u00d2j\2\u0664\u0665\5\u0084C")
        buf.write(u"\2\u0665\u0666\5\u00d2j\2\u0666\u0668\3\2\2\2\u0667\u0664")
        buf.write(u"\3\2\2\2\u0668\u066b\3\2\2\2\u0669\u0667\3\2\2\2\u0669")
        buf.write(u"\u066a\3\2\2\2\u066a\u00d1\3\2\2\2\u066b\u0669\3\2\2")
        buf.write(u"\2\u066c\u0672\5\24\13\2\u066d\u0672\5\30\r\2\u066e\u0672")
        buf.write(u"\5(\25\2\u066f\u0672\5&\24\2\u0670\u0672\5\22\n\2\u0671")
        buf.write(u"\u066c\3\2\2\2\u0671\u066d\3\2\2\2\u0671\u066e\3\2\2")
        buf.write(u"\2\u0671\u066f\3\2\2\2\u0671\u0670\3\2\2\2\u0672\u00d3")
        buf.write(u"\3\2\2\2\u0673\u0679\5\u00d6l\2\u0674\u0675\5\u0084C")
        buf.write(u"\2\u0675\u0676\5\u00d6l\2\u0676\u0678\3\2\2\2\u0677\u0674")
        buf.write(u"\3\2\2\2\u0678\u067b\3\2\2\2\u0679\u0677\3\2\2\2\u0679")
        buf.write(u"\u067a\3\2\2\2\u067a\u00d5\3\2\2\2\u067b\u0679\3\2\2")
        buf.write(u"\2\u067c\u0680\5\32\16\2\u067d\u0680\5\26\f\2\u067e\u0680")
        buf.write(u"\5*\26\2\u067f\u067c\3\2\2\2\u067f\u067d\3\2\2\2\u067f")
        buf.write(u"\u067e\3\2\2\2\u0680\u00d7\3\2\2\2\u0681\u0682\7\13\2")
        buf.write(u"\2\u0682\u068c\5\u0184\u00c3\2\u0683\u0684\7\f\2\2\u0684")
        buf.write(u"\u068c\5\u019e\u00d0\2\u0685\u0686\7\r\2\2\u0686\u068c")
        buf.write(u"\5\u00dan\2\u0687\u0688\7\16\2\2\u0688\u068c\5\u00da")
        buf.write(u"n\2\u0689\u068a\7\17\2\2\u068a\u068c\5\u00dep\2\u068b")
        buf.write(u"\u0681\3\2\2\2\u068b\u0683\3\2\2\2\u068b\u0685\3\2\2")
        buf.write(u"\2\u068b\u0687\3\2\2\2\u068b\u0689\3\2\2\2\u068c\u00d9")
        buf.write(u"\3\2\2\2\u068d\u068f\5\u00b8]\2\u068e\u0690\5\u00dco")
        buf.write(u"\2\u068f\u068e\3\2\2\2\u068f\u0690\3\2\2\2\u0690\u00db")
        buf.write(u"\3\2\2\2\u0691\u0692\7m\2\2\u0692\u0693\5\u012a\u0096")
        buf.write(u"\2\u0693\u0694\7\21\2\2\u0694\u0699\5\u00b8]\2\u0695")
        buf.write(u"\u0696\7\25\2\2\u0696\u0698\5\u00b8]\2\u0697\u0695\3")
        buf.write(u"\2\2\2\u0698\u069b\3\2\2\2\u0699\u0697\3\2\2\2\u0699")
        buf.write(u"\u069a\3\2\2\2\u069a\u00dd\3\2\2\2\u069b\u0699\3\2\2")
        buf.write(u"\2\u069c\u069e\5\u00b8]\2\u069d\u069f\5\u00e0q\2\u069e")
        buf.write(u"\u069d\3\2\2\2\u069e\u069f\3\2\2\2\u069f\u00df\3\2\2")
        buf.write(u"\2\u06a0\u06a1\7m\2\2\u06a1\u06a2\5\u012a\u0096\2\u06a2")
        buf.write(u"\u06a4\7\21\2\2\u06a3\u06a5\7%\2\2\u06a4\u06a3\3\2\2")
        buf.write(u"\2\u06a4\u06a5\3\2\2\2\u06a5\u06a6\3\2\2\2\u06a6\u06ab")
        buf.write(u"\5\u0152\u00aa\2\u06a7\u06a8\7%\2\2\u06a8\u06aa\5\u0152")
        buf.write(u"\u00aa\2\u06a9\u06a7\3\2\2\2\u06aa\u06ad\3\2\2\2\u06ab")
        buf.write(u"\u06a9\3\2\2\2\u06ab\u06ac\3\2\2\2\u06ac\u06b0\3\2\2")
        buf.write(u"\2\u06ad\u06ab\3\2\2\2\u06ae\u06af\7\25\2\2\u06af\u06b1")
        buf.write(u"\5\u0152\u00aa\2\u06b0\u06ae\3\2\2\2\u06b0\u06b1\3\2")
        buf.write(u"\2\2\u06b1\u00e1\3\2\2\2\u06b2\u06b7\5\u00ba^\2\u06b3")
        buf.write(u"\u06b4\7\23\2\2\u06b4\u06b6\5\u00ba^\2\u06b5\u06b3\3")
        buf.write(u"\2\2\2\u06b6\u06b9\3\2\2\2\u06b7\u06b5\3\2\2\2\u06b7")
        buf.write(u"\u06b8\3\2\2\2\u06b8\u00e3\3\2\2\2\u06b9\u06b7\3\2\2")
        buf.write(u"\2\u06ba\u06bf\5\u00bc_\2\u06bb\u06bc\7\23\2\2\u06bc")
        buf.write(u"\u06be\5\u00bc_\2\u06bd\u06bb\3\2\2\2\u06be\u06c1\3\2")
        buf.write(u"\2\2\u06bf\u06bd\3\2\2\2\u06bf\u06c0\3\2\2\2\u06c0\u00e5")
        buf.write(u"\3\2\2\2\u06c1\u06bf\3\2\2\2\u06c2\u06c7\5&\24\2\u06c3")
        buf.write(u"\u06c7\5(\25\2\u06c4\u06c7\5*\26\2\u06c5\u06c7\5,\27")
        buf.write(u"\2\u06c6\u06c2\3\2\2\2\u06c6\u06c3\3\2\2\2\u06c6\u06c4")
        buf.write(u"\3\2\2\2\u06c6\u06c5\3\2\2\2\u06c7\u00e7\3\2\2\2\u06c8")
        buf.write(u"\u06c9\7\n\2\2\u06c9\u00e9\3\2\2\2\u06ca\u06d0\5\u00ec")
        buf.write(u"w\2\u06cb\u06cc\5\u0084C\2\u06cc\u06cd\5\u00ecw\2\u06cd")
        buf.write(u"\u06cf\3\2\2\2\u06ce\u06cb\3\2\2\2\u06cf\u06d2\3\2\2")
        buf.write(u"\2\u06d0\u06ce\3\2\2\2\u06d0\u06d1\3\2\2\2\u06d1\u00eb")
        buf.write(u"\3\2\2\2\u06d2\u06d0\3\2\2\2\u06d3\u06d4\7\13\2\2\u06d4")
        buf.write(u"\u06de\5\u016e\u00b8\2\u06d5\u06d6\7\f\2\2\u06d6\u06de")
        buf.write(u"\5\u018a\u00c6\2\u06d7\u06d8\7\r\2\2\u06d8\u06de\5\u00ee")
        buf.write(u"x\2\u06d9\u06da\7\16\2\2\u06da\u06de\5\u00eex\2\u06db")
        buf.write(u"\u06dc\7\17\2\2\u06dc\u06de\5\u00f0y\2\u06dd\u06d3\3")
        buf.write(u"\2\2\2\u06dd\u06d5\3\2\2\2\u06dd\u06d7\3\2\2\2\u06dd")
        buf.write(u"\u06d9\3\2\2\2\u06dd\u06db\3\2\2\2\u06de\u00ed\3\2\2")
        buf.write(u"\2\u06df\u06e1\5\u0154\u00ab\2\u06e0\u06e2\7\22\2\2\u06e1")
        buf.write(u"\u06e0\3\2\2\2\u06e1\u06e2\3\2\2\2\u06e2\u06e4\3\2\2")
        buf.write(u"\2\u06e3\u06e5\5\u00dco\2\u06e4\u06e3\3\2\2\2\u06e4\u06e5")
        buf.write(u"\3\2\2\2\u06e5\u00ef\3\2\2\2\u06e6\u06e8\5\u013a\u009e")
        buf.write(u"\2\u06e7\u06e9\7\22\2\2\u06e8\u06e7\3\2\2\2\u06e8\u06e9")
        buf.write(u"\3\2\2\2\u06e9\u06eb\3\2\2\2\u06ea\u06ec\5\u00e0q\2\u06eb")
        buf.write(u"\u06ea\3\2\2\2\u06eb\u06ec\3\2\2\2\u06ec\u00f1\3\2\2")
        buf.write(u"\2\u06ed\u06f3\5\64\33\2\u06ee\u06ef\5\u0084C\2\u06ef")
        buf.write(u"\u06f0\5\64\33\2\u06f0\u06f2\3\2\2\2\u06f1\u06ee\3\2")
        buf.write(u"\2\2\u06f2\u06f5\3\2\2\2\u06f3\u06f1\3\2\2\2\u06f3\u06f4")
        buf.write(u"\3\2\2\2\u06f4\u00f3\3\2\2\2\u06f5\u06f3\3\2\2\2\u06f6")
        buf.write(u"\u06fc\5.\30\2\u06f7\u06f8\5\u0084C\2\u06f8\u06f9\5.")
        buf.write(u"\30\2\u06f9\u06fb\3\2\2\2\u06fa\u06f7\3\2\2\2\u06fb\u06fe")
        buf.write(u"\3\2\2\2\u06fc\u06fa\3\2\2\2\u06fc\u06fd\3\2\2\2\u06fd")
        buf.write(u"\u00f5\3\2\2\2\u06fe\u06fc\3\2\2\2\u06ff\u0705\5B\"\2")
        buf.write(u"\u0700\u0701\5\u0084C\2\u0701\u0702\5B\"\2\u0702\u0704")
        buf.write(u"\3\2\2\2\u0703\u0700\3\2\2\2\u0704\u0707\3\2\2\2\u0705")
        buf.write(u"\u0703\3\2\2\2\u0705\u0706\3\2\2\2\u0706\u00f7\3\2\2")
        buf.write(u"\2\u0707\u0705\3\2\2\2\u0708\u070e\5R*\2\u0709\u070a")
        buf.write(u"\5\u0084C\2\u070a\u070b\5R*\2\u070b\u070d\3\2\2\2\u070c")
        buf.write(u"\u0709\3\2\2\2\u070d\u0710\3\2\2\2\u070e\u070c\3\2\2")
        buf.write(u"\2\u070e\u070f\3\2\2\2\u070f\u00f9\3\2\2\2\u0710\u070e")
        buf.write(u"\3\2\2\2\u0711\u0712\7\30\2\2\u0712\u0713\5\u00fc\177")
        buf.write(u"\2\u0713\u0714\7\24\2\2\u0714\u0715\5\u00fc\177\2\u0715")
        buf.write(u"\u0716\7\31\2\2\u0716\u0720\3\2\2\2\u0717\u0718\7\30")
        buf.write(u"\2\2\u0718\u0719\5\u00fe\u0080\2\u0719\u071a\7\31\2\2")
        buf.write(u"\u071a\u0720\3\2\2\2\u071b\u071c\7*\2\2\u071c\u071d\5")
        buf.write(u"\u00fe\u0080\2\u071d\u071e\7(\2\2\u071e\u0720\3\2\2\2")
        buf.write(u"\u071f\u0711\3\2\2\2\u071f\u0717\3\2\2\2\u071f\u071b")
        buf.write(u"\3\2\2\2\u0720\u00fb\3\2\2\2\u0721\u0731\7\u00a2\2\2")
        buf.write(u"\u0722\u0731\7\u00a3\2\2\u0723\u0731\7\u00ab\2\2\u0724")
        buf.write(u"\u0731\7\u00ac\2\2\u0725\u0731\7\u00a1\2\2\u0726\u0731")
        buf.write(u"\7\u00b0\2\2\u0727\u0731\7\u00af\2\2\u0728\u0731\7\u00a9")
        buf.write(u"\2\2\u0729\u0731\7\u00ad\2\2\u072a\u0731\7\u00ae\2\2")
        buf.write(u"\u072b\u0731\7\u00a0\2\2\u072c\u0731\7\u00b1\2\2\u072d")
        buf.write(u"\u0731\7\u00b2\2\2\u072e\u0731\7\u00aa\2\2\u072f\u0731")
        buf.write(u"\5\u008aF\2\u0730\u0721\3\2\2\2\u0730\u0722\3\2\2\2\u0730")
        buf.write(u"\u0723\3\2\2\2\u0730\u0724\3\2\2\2\u0730\u0725\3\2\2")
        buf.write(u"\2\u0730\u0726\3\2\2\2\u0730\u0727\3\2\2\2\u0730\u0728")
        buf.write(u"\3\2\2\2\u0730\u0729\3\2\2\2\u0730\u072a\3\2\2\2\u0730")
        buf.write(u"\u072b\3\2\2\2\u0730\u072c\3\2\2\2\u0730\u072d\3\2\2")
        buf.write(u"\2\u0730\u072e\3\2\2\2\u0730\u072f\3\2\2\2\u0731\u00fd")
        buf.write(u"\3\2\2\2\u0732\u0737\5\u00fc\177\2\u0733\u0734\7\23\2")
        buf.write(u"\2\u0734\u0736\5\u00fc\177\2\u0735\u0733\3\2\2\2\u0736")
        buf.write(u"\u0739\3\2\2\2\u0737\u0735\3\2\2\2\u0737\u0738\3\2\2")
        buf.write(u"\2\u0738\u00ff\3\2\2\2\u0739\u0737\3\2\2\2\u073a\u073f")
        buf.write(u"\5\u0104\u0083\2\u073b\u073f\5\u0106\u0084\2\u073c\u073f")
        buf.write(u"\5\u00b8]\2\u073d\u073f\5\u0102\u0082\2\u073e\u073a\3")
        buf.write(u"\2\2\2\u073e\u073b\3\2\2\2\u073e\u073c\3\2\2\2\u073e")
        buf.write(u"\u073d\3\2\2\2\u073f\u0101\3\2\2\2\u0740\u0741\t\4\2")
        buf.write(u"\2\u0741\u0103\3\2\2\2\u0742\u0743\7\26\2\2\u0743\u0744")
        buf.write(u"\5X-\2\u0744\u0745\7\27\2\2\u0745\u0105\3\2\2\2\u0746")
        buf.write(u"\u0749\5\u00fc\177\2\u0747\u0749\5\u0108\u0085\2\u0748")
        buf.write(u"\u0746\3\2\2\2\u0748\u0747\3\2\2\2\u0749\u0107\3\2\2")
        buf.write(u"\2\u074a\u0750\5\u00a4S\2\u074b\u0750\5\u009eP\2\u074c")
        buf.write(u"\u0750\5\u00a0Q\2\u074d\u0750\5\u010c\u0087\2\u074e\u0750")
        buf.write(u"\5\u010a\u0086\2\u074f\u074a\3\2\2\2\u074f\u074b\3\2")
        buf.write(u"\2\2\u074f\u074c\3\2\2\2\u074f\u074d\3\2\2\2\u074f\u074e")
        buf.write(u"\3\2\2\2\u0750\u0109\3\2\2\2\u0751\u0753\7y\2\2\u0752")
        buf.write(u"\u0751\3\2\2\2\u0752\u0753\3\2\2\2\u0753\u0754\3\2\2")
        buf.write(u"\2\u0754\u0756\7\26\2\2\u0755\u0757\5\u010e\u0088\2\u0756")
        buf.write(u"\u0755\3\2\2\2\u0756\u0757\3\2\2\2\u0757\u0758\3\2\2")
        buf.write(u"\2\u0758\u0759\7\27\2\2\u0759\u010b\3\2\2\2\u075a\u075c")
        buf.write(u"\7y\2\2\u075b\u075a\3\2\2\2\u075b\u075c\3\2\2\2\u075c")
        buf.write(u"\u075d\3\2\2\2\u075d\u075f\7\32\2\2\u075e\u0760\5\u0110")
        buf.write(u"\u0089\2\u075f\u075e\3\2\2\2\u075f\u0760\3\2\2\2\u0760")
        buf.write(u"\u0761\3\2\2\2\u0761\u0762\7\33\2\2\u0762\u010d\3\2\2")
        buf.write(u"\2\u0763\u0764\5X-\2\u0764\u076d\7\23\2\2\u0765\u076a")
        buf.write(u"\5X-\2\u0766\u0767\7\23\2\2\u0767\u0769\5X-\2\u0768\u0766")
        buf.write(u"\3\2\2\2\u0769\u076c\3\2\2\2\u076a\u0768\3\2\2\2\u076a")
        buf.write(u"\u076b\3\2\2\2\u076b\u076e\3\2\2\2\u076c\u076a\3\2\2")
        buf.write(u"\2\u076d\u0765\3\2\2\2\u076d\u076e\3\2\2\2\u076e\u010f")
        buf.write(u"\3\2\2\2\u076f\u0774\5\u0112\u008a\2\u0770\u0771\7\23")
        buf.write(u"\2\2\u0771\u0773\5\u0112\u008a\2\u0772\u0770\3\2\2\2")
        buf.write(u"\u0773\u0776\3\2\2\2\u0774\u0772\3\2\2\2\u0774\u0775")
        buf.write(u"\3\2\2\2\u0775\u0111\3\2\2\2\u0776\u0774\3\2\2\2\u0777")
        buf.write(u"\u0778\5X-\2\u0778\u0779\7\21\2\2\u0779\u077a\5X-\2\u077a")
        buf.write(u"\u0113\3\2\2\2\u077b\u077c\5X-\2\u077c\u077d\7\21\2\2")
        buf.write(u"\u077d\u077e\5X-\2\u077e\u0785\3\2\2\2\u077f\u0780\5")
        buf.write(u"X-\2\u0780\u0781\7\21\2\2\u0781\u0785\3\2\2\2\u0782\u0783")
        buf.write(u"\7\21\2\2\u0783\u0785\5X-\2\u0784\u077b\3\2\2\2\u0784")
        buf.write(u"\u077f\3\2\2\2\u0784\u0782\3\2\2\2\u0785\u0115\3\2\2")
        buf.write(u"\2\u0786\u0787\5\u00ba^\2\u0787\u0788\5\u0130\u0099\2")
        buf.write(u"\u0788\u0789\5X-\2\u0789\u0117\3\2\2\2\u078a\u078b\b")
        buf.write(u"\u008d\1\2\u078b\u078c\5\u00ba^\2\u078c\u0791\3\2\2\2")
        buf.write(u"\u078d\u078e\f\3\2\2\u078e\u0790\5~@\2\u078f\u078d\3")
        buf.write(u"\2\2\2\u0790\u0793\3\2\2\2\u0791\u078f\3\2\2\2\u0791")
        buf.write(u"\u0792\3\2\2\2\u0792\u0119\3\2\2\2\u0793\u0791\3\2\2")
        buf.write(u"\2\u0794\u0795\6\u008e\63\3\u0795\u0796\7\u00a6\2\2\u0796")
        buf.write(u"\u0799\5\u00ccg\2\u0797\u0799\5X-\2\u0798\u0794\3\2\2")
        buf.write(u"\2\u0798\u0797\3\2\2\2\u0799\u011b\3\2\2\2\u079a\u079b")
        buf.write(u"\7\u0088\2\2\u079b\u079c\7G\2\2\u079c\u079d\7m\2\2\u079d")
        buf.write(u"\u079e\5X-\2\u079e\u011d\3\2\2\2\u079f\u07a0\7\u0088")
        buf.write(u"\2\2\u07a0\u07a1\7\u0080\2\2\u07a1\u07a2\7m\2\2\u07a2")
        buf.write(u"\u07a3\5X-\2\u07a3\u011f\3\2\2\2\u07a4\u07a9\5\u0122")
        buf.write(u"\u0092\2\u07a5\u07a6\7\23\2\2\u07a6\u07a8\5\u0122\u0092")
        buf.write(u"\2\u07a7\u07a5\3\2\2\2\u07a8\u07ab\3\2\2\2\u07a9\u07a7")
        buf.write(u"\3\2\2\2\u07a9\u07aa\3\2\2\2\u07aa\u0121\3\2\2\2\u07ab")
        buf.write(u"\u07a9\3\2\2\2\u07ac\u07b1\5\u00ba^\2\u07ad\u07ae\7\25")
        buf.write(u"\2\2\u07ae\u07b0\5\u00ba^\2\u07af\u07ad\3\2\2\2\u07b0")
        buf.write(u"\u07b3\3\2\2\2\u07b1\u07af\3\2\2\2\u07b1\u07b2\3\2\2")
        buf.write(u"\2\u07b2\u07b5\3\2\2\2\u07b3\u07b1\3\2\2\2\u07b4\u07b6")
        buf.write(u"\t\5\2\2\u07b5\u07b4\3\2\2\2\u07b5\u07b6\3\2\2\2\u07b6")
        buf.write(u"\u0123\3\2\2\2\u07b7\u07be\7\"\2\2\u07b8\u07be\7#\2\2")
        buf.write(u"\u07b9\u07be\5\u0132\u009a\2\u07ba\u07be\5\u0134\u009b")
        buf.write(u"\2\u07bb\u07be\5\u0136\u009c\2\u07bc\u07be\5\u0138\u009d")
        buf.write(u"\2\u07bd\u07b7\3\2\2\2\u07bd\u07b8\3\2\2\2\u07bd\u07b9")
        buf.write(u"\3\2\2\2\u07bd\u07ba\3\2\2\2\u07bd\u07bb\3\2\2\2\u07bd")
        buf.write(u"\u07bc\3\2\2\2\u07be\u0125\3\2\2\2\u07bf\u07c0\7\u00a6")
        buf.write(u"\2\2\u07c0\u07c1\6\u0094\64\3\u07c1\u0127\3\2\2\2\u07c2")
        buf.write(u"\u07c3\7\u00a6\2\2\u07c3\u07c4\6\u0095\65\3\u07c4\u0129")
        buf.write(u"\3\2\2\2\u07c5\u07c6\7\u00a6\2\2\u07c6\u07c7\6\u0096")
        buf.write(u"\66\3\u07c7\u012b\3\2\2\2\u07c8\u07c9\7\u00a6\2\2\u07c9")
        buf.write(u"\u07ca\6\u0097\67\3\u07ca\u012d\3\2\2\2\u07cb\u07cc\7")
        buf.write(u"\u00a6\2\2\u07cc\u07cd\6\u00988\3\u07cd\u012f\3\2\2\2")
        buf.write(u"\u07ce\u07cf\7-\2\2\u07cf\u0131\3\2\2\2\u07d0\u07d1\7")
        buf.write(u"$\2\2\u07d1\u0133\3\2\2\2\u07d2\u07d3\7%\2\2\u07d3\u0135")
        buf.write(u"\3\2\2\2\u07d4\u07d5\7&\2\2\u07d5\u0137\3\2\2\2\u07d6")
        buf.write(u"\u07d7\t\6\2\2\u07d7\u0139\3\2\2\2\u07d8\u07d9\7\u008b")
        buf.write(u"\2\2\u07d9\u07da\5\u013c\u009f\2\u07da\u07db\7\22\2\2")
        buf.write(u"\u07db\u07e0\3\2\2\2\u07dc\u07dd\5\u013c\u009f\2\u07dd")
        buf.write(u"\u07de\7\22\2\2\u07de\u07e0\3\2\2\2\u07df\u07d8\3\2\2")
        buf.write(u"\2\u07df\u07dc\3\2\2\2\u07e0\u013b\3\2\2\2\u07e1\u07e2")
        buf.write(u"\b\u009f\1\2\u07e2\u07e3\5\u013e\u00a0\2\u07e3\u07e8")
        buf.write(u"\3\2\2\2\u07e4\u07e5\f\3\2\2\u07e5\u07e7\5\u0144\u00a3")
        buf.write(u"\2\u07e6\u07e4\3\2\2\2\u07e7\u07ea\3\2\2\2\u07e8\u07e6")
        buf.write(u"\3\2\2\2\u07e8\u07e9\3\2\2\2\u07e9\u013d\3\2\2\2\u07ea")
        buf.write(u"\u07e8\3\2\2\2\u07eb\u07f3\5\u0140\u00a1\2\u07ec\u07f3")
        buf.write(u"\5\u0142\u00a2\2\u07ed\u07f3\5\u014c\u00a7\2\u07ee\u07f3")
        buf.write(u"\5\u014e\u00a8\2\u07ef\u07f3\5\u0150\u00a9\2\u07f0\u07f3")
        buf.write(u"\5\u0146\u00a4\2\u07f1\u07f3\5\u014a\u00a6\2\u07f2\u07eb")
        buf.write(u"\3\2\2\2\u07f2\u07ec\3\2\2\2\u07f2\u07ed\3\2\2\2\u07f2")
        buf.write(u"\u07ee\3\2\2\2\u07f2\u07ef\3\2\2\2\u07f2\u07f0\3\2\2")
        buf.write(u"\2\u07f2\u07f1\3\2\2\2\u07f3\u013f\3\2\2\2\u07f4\u07f5")
        buf.write(u"\5\u0102\u0082\2\u07f5\u0141\3\2\2\2\u07f6\u07f7\5\u0126")
        buf.write(u"\u0094\2\u07f7\u07f8\5\u0146\u00a4\2\u07f8\u0143\3\2")
        buf.write(u"\2\2\u07f9\u07fa\7\25\2\2\u07fa\u07ff\5\u0146\u00a4\2")
        buf.write(u"\u07fb\u07fc\7\25\2\2\u07fc\u07ff\5\u0152\u00aa\2\u07fd")
        buf.write(u"\u07ff\5\u014a\u00a6\2\u07fe\u07f9\3\2\2\2\u07fe\u07fb")
        buf.write(u"\3\2\2\2\u07fe\u07fd\3\2\2\2\u07ff\u0145\3\2\2\2\u0800")
        buf.write(u"\u0801\5\u0152\u00aa\2\u0801\u0803\7\26\2\2\u0802\u0804")
        buf.write(u"\5\u0148\u00a5\2\u0803\u0802\3\2\2\2\u0803\u0804\3\2")
        buf.write(u"\2\2\u0804\u0805\3\2\2\2\u0805\u0806\7\27\2\2\u0806\u0147")
        buf.write(u"\3\2\2\2\u0807\u0808\b\u00a5\1\2\u0808\u0809\5\u013c")
        buf.write(u"\u009f\2\u0809\u080f\3\2\2\2\u080a\u080b\f\3\2\2\u080b")
        buf.write(u"\u080c\7\23\2\2\u080c\u080e\5\u013c\u009f\2\u080d\u080a")
        buf.write(u"\3\2\2\2\u080e\u0811\3\2\2\2\u080f\u080d\3\2\2\2\u080f")
        buf.write(u"\u0810\3\2\2\2\u0810\u0149\3\2\2\2\u0811\u080f\3\2\2")
        buf.write(u"\2\u0812\u0813\7\30\2\2\u0813\u0814\5\u013c\u009f\2\u0814")
        buf.write(u"\u0815\7\31\2\2\u0815\u014b\3\2\2\2\u0816\u0817\7\26")
        buf.write(u"\2\2\u0817\u0818\5\u013c\u009f\2\u0818\u0819\7\27\2\2")
        buf.write(u"\u0819\u014d\3\2\2\2\u081a\u081b\5\u0152\u00aa\2\u081b")
        buf.write(u"\u014f\3\2\2\2\u081c\u0822\7\u00ab\2\2\u081d\u0822\7")
        buf.write(u"\u00ad\2\2\u081e\u0822\7\u00a9\2\2\u081f\u0822\7\u00a0")
        buf.write(u"\2\2\u0820\u0822\7\u00a1\2\2\u0821\u081c\3\2\2\2\u0821")
        buf.write(u"\u081d\3\2\2\2\u0821\u081e\3\2\2\2\u0821\u081f\3\2\2")
        buf.write(u"\2\u0821\u0820\3\2\2\2\u0822\u0151\3\2\2\2\u0823\u0824")
        buf.write(u"\t\7\2\2\u0824\u0153\3\2\2\2\u0825\u0826\7\u008b\2\2")
        buf.write(u"\u0826\u0829\5\u0156\u00ac\2\u0827\u0829\5\u0156\u00ac")
        buf.write(u"\2\u0828\u0825\3\2\2\2\u0828\u0827\3\2\2\2\u0829\u0155")
        buf.write(u"\3\2\2\2\u082a\u082b\b\u00ac\1\2\u082b\u082c\5\u0158")
        buf.write(u"\u00ad\2\u082c\u0831\3\2\2\2\u082d\u082e\f\3\2\2\u082e")
        buf.write(u"\u0830\5\u015c\u00af\2\u082f\u082d\3\2\2\2\u0830\u0833")
        buf.write(u"\3\2\2\2\u0831\u082f\3\2\2\2\u0831\u0832\3\2\2\2\u0832")
        buf.write(u"\u0157\3\2\2\2\u0833\u0831\3\2\2\2\u0834\u083a\5\u015a")
        buf.write(u"\u00ae\2\u0835\u083a\5\u0166\u00b4\2\u0836\u083a\5\u0168")
        buf.write(u"\u00b5\2\u0837\u083a\5\u016a\u00b6\2\u0838\u083a\5\u015e")
        buf.write(u"\u00b0\2\u0839\u0834\3\2\2\2\u0839\u0835\3\2\2\2\u0839")
        buf.write(u"\u0836\3\2\2\2\u0839\u0837\3\2\2\2\u0839\u0838\3\2\2")
        buf.write(u"\2\u083a\u0159\3\2\2\2\u083b\u083c\5\u0102\u0082\2\u083c")
        buf.write(u"\u015b\3\2\2\2\u083d\u083e\7\25\2\2\u083e\u0844\5\u015e")
        buf.write(u"\u00b0\2\u083f\u0840\7\30\2\2\u0840\u0841\5\u0156\u00ac")
        buf.write(u"\2\u0841\u0842\7\31\2\2\u0842\u0844\3\2\2\2\u0843\u083d")
        buf.write(u"\3\2\2\2\u0843\u083f\3\2\2\2\u0844\u015d\3\2\2\2\u0845")
        buf.write(u"\u0846\5\u016c\u00b7\2\u0846\u0848\7\26\2\2\u0847\u0849")
        buf.write(u"\5\u0160\u00b1\2\u0848\u0847\3\2\2\2\u0848\u0849\3\2")
        buf.write(u"\2\2\u0849\u084a\3\2\2\2\u084a\u084b\7\27\2\2\u084b\u015f")
        buf.write(u"\3\2\2\2\u084c\u0853\5\u0162\u00b2\2\u084d\u0853\5\u0164")
        buf.write(u"\u00b3\2\u084e\u084f\5\u0162\u00b2\2\u084f\u0850\7\23")
        buf.write(u"\2\2\u0850\u0851\5\u0164\u00b3\2\u0851\u0853\3\2\2\2")
        buf.write(u"\u0852\u084c\3\2\2\2\u0852\u084d\3\2\2\2\u0852\u084e")
        buf.write(u"\3\2\2\2\u0853\u0161\3\2\2\2\u0854\u0855\b\u00b2\1\2")
        buf.write(u"\u0855\u0856\5\u0156\u00ac\2\u0856\u085c\3\2\2\2\u0857")
        buf.write(u"\u0858\f\3\2\2\u0858\u0859\7\23\2\2\u0859\u085b\5\u0156")
        buf.write(u"\u00ac\2\u085a\u0857\3\2\2\2\u085b\u085e\3\2\2\2\u085c")
        buf.write(u"\u085a\3\2\2\2\u085c\u085d\3\2\2\2\u085d\u0163\3\2\2")
        buf.write(u"\2\u085e\u085c\3\2\2\2\u085f\u0860\b\u00b3\1\2\u0860")
        buf.write(u"\u0861\5\u016c\u00b7\2\u0861\u0862\7-\2\2\u0862\u0863")
        buf.write(u"\5\u0156\u00ac\2\u0863\u086c\3\2\2\2\u0864\u0865\f\3")
        buf.write(u"\2\2\u0865\u0866\7\23\2\2\u0866\u0867\5\u016c\u00b7\2")
        buf.write(u"\u0867\u0868\7-\2\2\u0868\u0869\5\u0156\u00ac\2\u0869")
        buf.write(u"\u086b\3\2\2\2\u086a\u0864\3\2\2\2\u086b\u086e\3\2\2")
        buf.write(u"\2\u086c\u086a\3\2\2\2\u086c\u086d\3\2\2\2\u086d\u0165")
        buf.write(u"\3\2\2\2\u086e\u086c\3\2\2\2\u086f\u0870\7\26\2\2\u0870")
        buf.write(u"\u0871\5\u0156\u00ac\2\u0871\u0872\7\27\2\2\u0872\u0167")
        buf.write(u"\3\2\2\2\u0873\u0874\b\u00b5\1\2\u0874\u0877\7\u00a8")
        buf.write(u"\2\2\u0875\u0877\5\u016c\u00b7\2\u0876\u0873\3\2\2\2")
        buf.write(u"\u0876\u0875\3\2\2\2\u0877\u087d\3\2\2\2\u0878\u0879")
        buf.write(u"\f\3\2\2\u0879\u087a\7\25\2\2\u087a\u087c\5\u016c\u00b7")
        buf.write(u"\2\u087b\u0878\3\2\2\2\u087c\u087f\3\2\2\2\u087d\u087b")
        buf.write(u"\3\2\2\2\u087d\u087e\3\2\2\2\u087e\u0169\3\2\2\2\u087f")
        buf.write(u"\u087d\3\2\2\2\u0880\u0886\7\u00ab\2\2\u0881\u0886\7")
        buf.write(u"\u00ad\2\2\u0882\u0886\7\u00a9\2\2\u0883\u0886\7\u00a0")
        buf.write(u"\2\2\u0884\u0886\7\u00a1\2\2\u0885\u0880\3\2\2\2\u0885")
        buf.write(u"\u0881\3\2\2\2\u0885\u0882\3\2\2\2\u0885\u0883\3\2\2")
        buf.write(u"\2\u0885\u0884\3\2\2\2\u0886\u016b\3\2\2\2\u0887\u0888")
        buf.write(u"\t\b\2\2\u0888\u016d\3\2\2\2\u0889\u088a\7\u008b\2\2")
        buf.write(u"\u088a\u088b\5\u0170\u00b9\2\u088b\u088c\7\22\2\2\u088c")
        buf.write(u"\u0891\3\2\2\2\u088d\u088e\5\u0170\u00b9\2\u088e\u088f")
        buf.write(u"\7\22\2\2\u088f\u0891\3\2\2\2\u0890\u0889\3\2\2\2\u0890")
        buf.write(u"\u088d\3\2\2\2\u0891\u016f\3\2\2\2\u0892\u0893\b\u00b9")
        buf.write(u"\1\2\u0893\u0894\5\u0172\u00ba\2\u0894\u0899\3\2\2\2")
        buf.write(u"\u0895\u0896\f\3\2\2\u0896\u0898\5\u0178\u00bd\2\u0897")
        buf.write(u"\u0895\3\2\2\2\u0898\u089b\3\2\2\2\u0899\u0897\3\2\2")
        buf.write(u"\2\u0899\u089a\3\2\2\2\u089a\u0171\3\2\2\2\u089b\u0899")
        buf.write(u"\3\2\2\2\u089c\u08a2\5\u0174\u00bb\2\u089d\u08a2\5\u0176")
        buf.write(u"\u00bc\2\u089e\u08a2\5\u0180\u00c1\2\u089f\u08a2\5\u0182")
        buf.write(u"\u00c2\2\u08a0\u08a2\5\u0186\u00c4\2\u08a1\u089c\3\2")
        buf.write(u"\2\2\u08a1\u089d\3\2\2\2\u08a1\u089e\3\2\2\2\u08a1\u089f")
        buf.write(u"\3\2\2\2\u08a1\u08a0\3\2\2\2\u08a2\u0173\3\2\2\2\u08a3")
        buf.write(u"\u08a4\5\u0102\u0082\2\u08a4\u0175\3\2\2\2\u08a5\u08a6")
        buf.write(u"\5\u0126\u0094\2\u08a6\u08a7\5\u017a\u00be\2\u08a7\u0177")
        buf.write(u"\3\2\2\2\u08a8\u08a9\7\25\2\2\u08a9\u08ac\5\u017a\u00be")
        buf.write(u"\2\u08aa\u08ac\5\u017e\u00c0\2\u08ab\u08a8\3\2\2\2\u08ab")
        buf.write(u"\u08aa\3\2\2\2\u08ac\u0179\3\2\2\2\u08ad\u08ae\5\u0188")
        buf.write(u"\u00c5\2\u08ae\u08b0\7\26\2\2\u08af\u08b1\5\u017c\u00bf")
        buf.write(u"\2\u08b0\u08af\3\2\2\2\u08b0\u08b1\3\2\2\2\u08b1\u08b2")
        buf.write(u"\3\2\2\2\u08b2\u08b3\7\27\2\2\u08b3\u017b\3\2\2\2\u08b4")
        buf.write(u"\u08b5\b\u00bf\1\2\u08b5\u08b6\5\u0170\u00b9\2\u08b6")
        buf.write(u"\u08bc\3\2\2\2\u08b7\u08b8\f\3\2\2\u08b8\u08b9\7\23\2")
        buf.write(u"\2\u08b9\u08bb\5\u0170\u00b9\2\u08ba\u08b7\3\2\2\2\u08bb")
        buf.write(u"\u08be\3\2\2\2\u08bc\u08ba\3\2\2\2\u08bc\u08bd\3\2\2")
        buf.write(u"\2\u08bd\u017d\3\2\2\2\u08be\u08bc\3\2\2\2\u08bf\u08c0")
        buf.write(u"\7\30\2\2\u08c0\u08c1\5\u0170\u00b9\2\u08c1\u08c2\7\31")
        buf.write(u"\2\2\u08c2\u017f\3\2\2\2\u08c3\u08c4\7\26\2\2\u08c4\u08c5")
        buf.write(u"\5\u0170\u00b9\2\u08c5\u08c6\7\27\2\2\u08c6\u0181\3\2")
        buf.write(u"\2\2\u08c7\u08c8\b\u00c2\1\2\u08c8\u08c9\5\u0188\u00c5")
        buf.write(u"\2\u08c9\u08cf\3\2\2\2\u08ca\u08cb\f\3\2\2\u08cb\u08cc")
        buf.write(u"\7\25\2\2\u08cc\u08ce\5\u0188\u00c5\2\u08cd\u08ca\3\2")
        buf.write(u"\2\2\u08ce\u08d1\3\2\2\2\u08cf\u08cd\3\2\2\2\u08cf\u08d0")
        buf.write(u"\3\2\2\2\u08d0\u0183\3\2\2\2\u08d1\u08cf\3\2\2\2\u08d2")
        buf.write(u"\u08d3\b\u00c3\1\2\u08d3\u08d4\5\u0182\u00c2\2\u08d4")
        buf.write(u"\u08d9\3\2\2\2\u08d5\u08d6\f\3\2\2\u08d6\u08d8\7\u00a8")
        buf.write(u"\2\2\u08d7\u08d5\3\2\2\2\u08d8\u08db\3\2\2\2\u08d9\u08d7")
        buf.write(u"\3\2\2\2\u08d9\u08da\3\2\2\2\u08da\u0185\3\2\2\2\u08db")
        buf.write(u"\u08d9\3\2\2\2\u08dc\u08e2\7\u00ab\2\2\u08dd\u08e2\7")
        buf.write(u"\u00ad\2\2\u08de\u08e2\7\u00a9\2\2\u08df\u08e2\7\u00a0")
        buf.write(u"\2\2\u08e0\u08e2\7\u00a1\2\2\u08e1\u08dc\3\2\2\2\u08e1")
        buf.write(u"\u08dd\3\2\2\2\u08e1\u08de\3\2\2\2\u08e1\u08df\3\2\2")
        buf.write(u"\2\u08e1\u08e0\3\2\2\2\u08e2\u0187\3\2\2\2\u08e3\u08e4")
        buf.write(u"\t\t\2\2\u08e4\u0189\3\2\2\2\u08e5\u08e6\7\u008b\2\2")
        buf.write(u"\u08e6\u08e7\5\u018c\u00c7\2\u08e7\u08e8\7\22\2\2\u08e8")
        buf.write(u"\u08ed\3\2\2\2\u08e9\u08ea\5\u018c\u00c7\2\u08ea\u08eb")
        buf.write(u"\7\22\2\2\u08eb\u08ed\3\2\2\2\u08ec\u08e5\3\2\2\2\u08ec")
        buf.write(u"\u08e9\3\2\2\2\u08ed\u018b\3\2\2\2\u08ee\u08ef\b\u00c7")
        buf.write(u"\1\2\u08ef\u08f0\5\u018e\u00c8\2\u08f0\u08f5\3\2\2\2")
        buf.write(u"\u08f1\u08f2\f\3\2\2\u08f2\u08f4\5\u0194\u00cb\2\u08f3")
        buf.write(u"\u08f1\3\2\2\2\u08f4\u08f7\3\2\2\2\u08f5\u08f3\3\2\2")
        buf.write(u"\2\u08f5\u08f6\3\2\2\2\u08f6\u018d\3\2\2\2\u08f7\u08f5")
        buf.write(u"\3\2\2\2\u08f8\u08fe\5\u0190\u00c9\2\u08f9\u08fe\5\u0192")
        buf.write(u"\u00ca\2\u08fa\u08fe\5\u019c\u00cf\2\u08fb\u08fe\5\u019e")
        buf.write(u"\u00d0\2\u08fc\u08fe\5\u01a0\u00d1\2\u08fd\u08f8\3\2")
        buf.write(u"\2\2\u08fd\u08f9\3\2\2\2\u08fd\u08fa\3\2\2\2\u08fd\u08fb")
        buf.write(u"\3\2\2\2\u08fd\u08fc\3\2\2\2\u08fe\u018f\3\2\2\2\u08ff")
        buf.write(u"\u0900\5\u0102\u0082\2\u0900\u0191\3\2\2\2\u0901\u0902")
        buf.write(u"\5\u0126\u0094\2\u0902\u0903\5\u0196\u00cc\2\u0903\u0193")
        buf.write(u"\3\2\2\2\u0904\u0905\7\25\2\2\u0905\u0908\5\u0196\u00cc")
        buf.write(u"\2\u0906\u0908\5\u019a\u00ce\2\u0907\u0904\3\2\2\2\u0907")
        buf.write(u"\u0906\3\2\2\2\u0908\u0195\3\2\2\2\u0909\u090a\5\u01a2")
        buf.write(u"\u00d2\2\u090a\u090c\7\26\2\2\u090b\u090d\5\u0198\u00cd")
        buf.write(u"\2\u090c\u090b\3\2\2\2\u090c\u090d\3\2\2\2\u090d\u090e")
        buf.write(u"\3\2\2\2\u090e\u090f\7\27\2\2\u090f\u0197\3\2\2\2\u0910")
        buf.write(u"\u0911\b\u00cd\1\2\u0911\u0912\5\u018c\u00c7\2\u0912")
        buf.write(u"\u0918\3\2\2\2\u0913\u0914\f\3\2\2\u0914\u0915\7\23\2")
        buf.write(u"\2\u0915\u0917\5\u018c\u00c7\2\u0916\u0913\3\2\2\2\u0917")
        buf.write(u"\u091a\3\2\2\2\u0918\u0916\3\2\2\2\u0918\u0919\3\2\2")
        buf.write(u"\2\u0919\u0199\3\2\2\2\u091a\u0918\3\2\2\2\u091b\u091c")
        buf.write(u"\7\30\2\2\u091c\u091d\5\u018c\u00c7\2\u091d\u091e\7\31")
        buf.write(u"\2\2\u091e\u019b\3\2\2\2\u091f\u0920\7\26\2\2\u0920\u0921")
        buf.write(u"\5\u018c\u00c7\2\u0921\u0922\7\27\2\2\u0922\u019d\3\2")
        buf.write(u"\2\2\u0923\u0924\b\u00d0\1\2\u0924\u0927\7\u00a8\2\2")
        buf.write(u"\u0925\u0927\5\u01a2\u00d2\2\u0926\u0923\3\2\2\2\u0926")
        buf.write(u"\u0925\3\2\2\2\u0927\u092d\3\2\2\2\u0928\u0929\f\3\2")
        buf.write(u"\2\u0929\u092a\7\25\2\2\u092a\u092c\5\u01a2\u00d2\2\u092b")
        buf.write(u"\u0928\3\2\2\2\u092c\u092f\3\2\2\2\u092d\u092b\3\2\2")
        buf.write(u"\2\u092d\u092e\3\2\2\2\u092e\u019f\3\2\2\2\u092f\u092d")
        buf.write(u"\3\2\2\2\u0930\u0936\7\u00ab\2\2\u0931\u0936\7\u00ad")
        buf.write(u"\2\2\u0932\u0936\7\u00a9\2\2\u0933\u0936\7\u00a0\2\2")
        buf.write(u"\u0934\u0936\7\u00a1\2\2\u0935\u0930\3\2\2\2\u0935\u0931")
        buf.write(u"\3\2\2\2\u0935\u0932\3\2\2\2\u0935\u0933\3\2\2\2\u0935")
        buf.write(u"\u0934\3\2\2\2\u0936\u01a1\3\2\2\2\u0937\u0938\t\n\2")
        buf.write(u"\2\u0938\u01a3\3\2\2\2\u00c9\u01aa\u01b1\u01cf\u01d5")
        buf.write(u"\u01da\u01e0\u01e2\u01e5\u01eb\u01ef\u01fa\u0203\u0212")
        buf.write(u"\u021b\u0222\u022c\u0242\u0259\u0266\u0271\u027f\u0285")
        buf.write(u"\u0290\u029e\u02b2\u02bd\u02bf\u02c8\u02cc\u02d4\u02d8")
        buf.write(u"\u02e4\u02e9\u02ed\u0308\u030f\u0314\u0318\u032d\u033b")
        buf.write(u"\u033f\u0342\u0363\u0376\u037d\u039f\u03a8\u03bf\u03cf")
        buf.write(u"\u03d4\u03dc\u03e5\u03fc\u0402\u0420\u0490\u0492\u049c")
        buf.write(u"\u04b1\u04c1\u04c6\u04d0\u04d5\u04d7\u04dd\u04df\u04e1")
        buf.write(u"\u04f5\u04fc\u0500\u050b\u050f\u0514\u0516\u051a\u0522")
        buf.write(u"\u0529\u052b\u0530\u0532\u053d\u0543\u0553\u055c\u0562")
        buf.write(u"\u0567\u056e\u0576\u0581\u0589\u0591\u0597\u059f\u05a8")
        buf.write(u"\u05b0\u05bd\u05c0\u05c4\u05c9\u05cd\u05d6\u05eb\u05f5")
        buf.write(u"\u05f7\u05fc\u060d\u0612\u061b\u0622\u0627\u062c\u063b")
        buf.write(u"\u0640\u0643\u0647\u064c\u0653\u065e\u0660\u0669\u0671")
        buf.write(u"\u0679\u067f\u068b\u068f\u0699\u069e\u06a4\u06ab\u06b0")
        buf.write(u"\u06b7\u06bf\u06c6\u06d0\u06dd\u06e1\u06e4\u06e8\u06eb")
        buf.write(u"\u06f3\u06fc\u0705\u070e\u071f\u0730\u0737\u073e\u0748")
        buf.write(u"\u074f\u0752\u0756\u075b\u075f\u076a\u076d\u0774\u0784")
        buf.write(u"\u0791\u0798\u07a9\u07b1\u07b5\u07bd\u07df\u07e8\u07f2")
        buf.write(u"\u07fe\u0803\u080f\u0821\u0828\u0831\u0839\u0843\u0848")
        buf.write(u"\u0852\u085c\u086c\u0876\u087d\u0885\u0890\u0899\u08a1")
        buf.write(u"\u08ab\u08b0\u08bc\u08cf\u08d9\u08e1\u08ec\u08f5\u08fd")
        buf.write(u"\u0907\u090c\u0918\u0926\u092d\u0935")
        return buf.getvalue()


class EParser ( AbstractParser ):

    grammarFileName = "EParser.g4"

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
    RULE_attribute_list = 17
    RULE_abstract_method_declaration = 18
    RULE_concrete_method_declaration = 19
    RULE_native_method_declaration = 20
    RULE_test_method_declaration = 21
    RULE_assertion = 22
    RULE_full_argument_list = 23
    RULE_typed_argument = 24
    RULE_statement = 25
    RULE_flush_statement = 26
    RULE_store_statement = 27
    RULE_method_call_statement = 28
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
    RULE_break_statement = 41
    RULE_return_statement = 42
    RULE_expression = 43
    RULE_unresolved_expression = 44
    RULE_unresolved_selector = 45
    RULE_invocation_expression = 46
    RULE_invocation_trailer = 47
    RULE_instance_expression = 48
    RULE_instance_selector = 49
    RULE_document_expression = 50
    RULE_blob_expression = 51
    RULE_constructor_expression = 52
    RULE_write_statement = 53
    RULE_ambiguous_expression = 54
    RULE_filtered_list_suffix = 55
    RULE_fetch_store_expression = 56
    RULE_sorted_expression = 57
    RULE_argument_assignment_list = 58
    RULE_with_argument_assignment_list = 59
    RULE_argument_assignment = 60
    RULE_assign_instance_statement = 61
    RULE_child_instance = 62
    RULE_assign_tuple_statement = 63
    RULE_lfs = 64
    RULE_lfp = 65
    RULE_indent = 66
    RULE_dedent = 67
    RULE_null_literal = 68
    RULE_declaration_list = 69
    RULE_declarations = 70
    RULE_declaration = 71
    RULE_resource_declaration = 72
    RULE_enum_declaration = 73
    RULE_native_symbol_list = 74
    RULE_category_symbol_list = 75
    RULE_symbol_list = 76
    RULE_attribute_constraint = 77
    RULE_list_literal = 78
    RULE_set_literal = 79
    RULE_expression_list = 80
    RULE_range_literal = 81
    RULE_typedef = 82
    RULE_primary_type = 83
    RULE_native_type = 84
    RULE_category_type = 85
    RULE_mutable_category_type = 86
    RULE_code_type = 87
    RULE_category_declaration = 88
    RULE_type_identifier_list = 89
    RULE_method_identifier = 90
    RULE_identifier = 91
    RULE_variable_identifier = 92
    RULE_attribute_identifier = 93
    RULE_type_identifier = 94
    RULE_symbol_identifier = 95
    RULE_argument_list = 96
    RULE_argument = 97
    RULE_operator_argument = 98
    RULE_named_argument = 99
    RULE_code_argument = 100
    RULE_category_or_any_type = 101
    RULE_any_type = 102
    RULE_member_method_declaration_list = 103
    RULE_member_method_declaration = 104
    RULE_native_member_method_declaration_list = 105
    RULE_native_member_method_declaration = 106
    RULE_native_category_binding = 107
    RULE_python_category_binding = 108
    RULE_python_module = 109
    RULE_javascript_category_binding = 110
    RULE_javascript_module = 111
    RULE_variable_identifier_list = 112
    RULE_attribute_identifier_list = 113
    RULE_method_declaration = 114
    RULE_comment_statement = 115
    RULE_native_statement_list = 116
    RULE_native_statement = 117
    RULE_python_native_statement = 118
    RULE_javascript_native_statement = 119
    RULE_statement_list = 120
    RULE_assertion_list = 121
    RULE_switch_case_statement_list = 122
    RULE_catch_statement_list = 123
    RULE_literal_collection = 124
    RULE_atomic_literal = 125
    RULE_literal_list_literal = 126
    RULE_selectable_expression = 127
    RULE_this_expression = 128
    RULE_parenthesis_expression = 129
    RULE_literal_expression = 130
    RULE_collection_literal = 131
    RULE_tuple_literal = 132
    RULE_dict_literal = 133
    RULE_expression_tuple = 134
    RULE_dict_entry_list = 135
    RULE_dict_entry = 136
    RULE_slice_arguments = 137
    RULE_assign_variable_statement = 138
    RULE_assignable_instance = 139
    RULE_is_expression = 140
    RULE_read_all_expression = 141
    RULE_read_one_expression = 142
    RULE_order_by_list = 143
    RULE_order_by = 144
    RULE_operator = 145
    RULE_new_token = 146
    RULE_key_token = 147
    RULE_module_token = 148
    RULE_value_token = 149
    RULE_symbols_token = 150
    RULE_assign = 151
    RULE_multiply = 152
    RULE_divide = 153
    RULE_idivide = 154
    RULE_modulo = 155
    RULE_javascript_statement = 156
    RULE_javascript_expression = 157
    RULE_javascript_primary_expression = 158
    RULE_javascript_this_expression = 159
    RULE_javascript_new_expression = 160
    RULE_javascript_selector_expression = 161
    RULE_javascript_method_expression = 162
    RULE_javascript_arguments = 163
    RULE_javascript_item_expression = 164
    RULE_javascript_parenthesis_expression = 165
    RULE_javascript_identifier_expression = 166
    RULE_javascript_literal_expression = 167
    RULE_javascript_identifier = 168
    RULE_python_statement = 169
    RULE_python_expression = 170
    RULE_python_primary_expression = 171
    RULE_python_self_expression = 172
    RULE_python_selector_expression = 173
    RULE_python_method_expression = 174
    RULE_python_argument_list = 175
    RULE_python_ordinal_argument_list = 176
    RULE_python_named_argument_list = 177
    RULE_python_parenthesis_expression = 178
    RULE_python_identifier_expression = 179
    RULE_python_literal_expression = 180
    RULE_python_identifier = 181
    RULE_java_statement = 182
    RULE_java_expression = 183
    RULE_java_primary_expression = 184
    RULE_java_this_expression = 185
    RULE_java_new_expression = 186
    RULE_java_selector_expression = 187
    RULE_java_method_expression = 188
    RULE_java_arguments = 189
    RULE_java_item_expression = 190
    RULE_java_parenthesis_expression = 191
    RULE_java_identifier_expression = 192
    RULE_java_class_identifier_expression = 193
    RULE_java_literal_expression = 194
    RULE_java_identifier = 195
    RULE_csharp_statement = 196
    RULE_csharp_expression = 197
    RULE_csharp_primary_expression = 198
    RULE_csharp_this_expression = 199
    RULE_csharp_new_expression = 200
    RULE_csharp_selector_expression = 201
    RULE_csharp_method_expression = 202
    RULE_csharp_arguments = 203
    RULE_csharp_item_expression = 204
    RULE_csharp_parenthesis_expression = 205
    RULE_csharp_identifier_expression = 206
    RULE_csharp_literal_expression = 207
    RULE_csharp_identifier = 208

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"full_argument_list", 
                   u"typed_argument", u"statement", u"flush_statement", 
                   u"store_statement", u"method_call_statement", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"break_statement", 
                   u"return_statement", u"expression", u"unresolved_expression", 
                   u"unresolved_selector", u"invocation_expression", u"invocation_trailer", 
                   u"instance_expression", u"instance_selector", u"document_expression", 
                   u"blob_expression", u"constructor_expression", u"write_statement", 
                   u"ambiguous_expression", u"filtered_list_suffix", u"fetch_store_expression", 
                   u"sorted_expression", u"argument_assignment_list", u"with_argument_assignment_list", 
                   u"argument_assignment", u"assign_instance_statement", 
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
                   u"python_category_binding", u"python_module", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"attribute_identifier_list", 
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
        super(EParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
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
            if hasattr(listener, "enterEnum_category_declaration"):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_category_declaration"):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = EParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(EParser.DEFINE)
            self.state = 419
            localctx.name = self.type_identifier()
            self.state = 420
            self.match(EParser.AS)
            self.state = 421
            self.match(EParser.ENUMERATED)
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 422
                self.match(EParser.CATEGORY)
                pass
            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 423
                localctx.derived = self.type_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 426
                localctx.attrs = self.attribute_list()
                self.state = 427
                self.match(EParser.COMMA)
                self.state = 428
                self.match(EParser.AND)
                pass

            elif la_ == 2:
                self.state = 430
                self.match(EParser.WITH)
                pass


            self.state = 433
            self.symbols_token()
            self.state = 434
            self.match(EParser.COLON)
            self.state = 435
            self.indent()
            self.state = 436
            localctx.symbols = self.category_symbol_list()
            self.state = 437
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
            if hasattr(listener, "enterEnum_native_declaration"):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_native_declaration"):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = EParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(EParser.DEFINE)
            self.state = 440
            localctx.name = self.type_identifier()
            self.state = 441
            self.match(EParser.AS)
            self.state = 442
            self.match(EParser.ENUMERATED)
            self.state = 443
            localctx.typ = self.native_type()
            self.state = 444
            self.match(EParser.WITH)
            self.state = 445
            self.symbols_token()
            self.state = 446
            self.match(EParser.COLON)
            self.state = 447
            self.indent()
            self.state = 448
            localctx.symbols = self.native_symbol_list()
            self.state = 449
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
            if hasattr(listener, "enterNative_symbol"):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol"):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = EParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            localctx.name = self.symbol_identifier()
            self.state = 452
            self.match(EParser.WITH)
            self.state = 453
            localctx.exp = self.expression(0)
            self.state = 454
            self.match(EParser.AS)
            self.state = 455
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
            if hasattr(listener, "enterCategory_symbol"):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol"):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = EParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            localctx.name = self.symbol_identifier()
            self.state = 458
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.AND:
                self.state = 459
                self.match(EParser.AND)
                self.state = 460
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
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Variable_identifier_listContext
            self.index = None # Variable_identifierContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)

        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def INDEX(self):
            return self.getToken(EParser.INDEX, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(EParser.Attribute_constraintContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_declaration"):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_declaration"):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = EParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(EParser.DEFINE)
            self.state = 464
            localctx.name = self.attribute_identifier()
            self.state = 465
            self.match(EParser.AS)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 466
                self.match(EParser.STORABLE)


            self.state = 469
            localctx.typ = self.typedef(0)
            self.state = 470
            self.match(EParser.ATTRIBUTE)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.IN or _la==EParser.MATCHING:
                self.state = 471
                localctx.match = self.attribute_constraint()


            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 474
                self.match(EParser.WITH)
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EParser.VARIABLE_IDENTIFIER:
                    self.state = 475
                    localctx.indices = self.variable_identifier_list()
                    self.state = 478
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==EParser.AND:
                        self.state = 476
                        self.match(EParser.AND)
                        self.state = 477
                        localctx.index = self.variable_identifier()




                self.state = 482
                self.match(EParser.INDEX)


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
            if hasattr(listener, "enterConcrete_category_declaration"):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_category_declaration"):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = EParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(EParser.DEFINE)
            self.state = 486
            localctx.name = self.type_identifier()
            self.state = 487
            self.match(EParser.AS)
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 488
                self.match(EParser.STORABLE)


            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 491
                self.match(EParser.CATEGORY)
                pass
            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 492
                localctx.derived = self.derived_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 495
                localctx.attrs = self.attribute_list()
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EParser.COMMA:
                    self.state = 496
                    self.match(EParser.COMMA)
                    self.state = 497
                    self.match(EParser.AND)
                    self.state = 498
                    self.match(EParser.METHODS)
                    self.state = 499
                    self.match(EParser.COLON)
                    self.state = 500
                    self.indent()
                    self.state = 501
                    localctx.methods = self.member_method_declaration_list()
                    self.state = 502
                    self.dedent()



            elif la_ == 2:
                self.state = 506
                self.match(EParser.WITH)
                self.state = 507
                self.match(EParser.METHODS)
                self.state = 508
                self.match(EParser.COLON)
                self.state = 509
                self.indent()
                self.state = 510
                localctx.methods = self.member_method_declaration_list()
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
            if hasattr(listener, "enterSingleton_category_declaration"):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleton_category_declaration"):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = EParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(EParser.DEFINE)
            self.state = 516
            localctx.name = self.type_identifier()
            self.state = 517
            self.match(EParser.AS)
            self.state = 518
            self.match(EParser.SINGLETON)
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 519
                localctx.attrs = self.attribute_list()
                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EParser.COMMA:
                    self.state = 520
                    self.match(EParser.COMMA)
                    self.state = 521
                    self.match(EParser.AND)
                    self.state = 522
                    self.match(EParser.METHODS)
                    self.state = 523
                    self.match(EParser.COLON)
                    self.state = 524
                    self.indent()
                    self.state = 525
                    localctx.methods = self.member_method_declaration_list()
                    self.state = 526
                    self.dedent()



            elif la_ == 2:
                self.state = 530
                self.match(EParser.WITH)
                self.state = 531
                self.match(EParser.METHODS)
                self.state = 532
                self.match(EParser.COLON)
                self.state = 533
                self.indent()
                self.state = 534
                localctx.methods = self.member_method_declaration_list()
                self.state = 535
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
            if hasattr(listener, "enterDerivedListItem"):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerivedListItem"):
                listener.exitDerivedListItem(self)


    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.copyFrom(ctx)

        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDerivedList"):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerivedList"):
                listener.exitDerivedList(self)



    def derived_list(self):

        localctx = EParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                localctx.items = self.type_identifier_list()
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                localctx.items = self.type_identifier_list()
                self.state = 541
                self.match(EParser.AND)
                self.state = 542
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
            if hasattr(listener, "enterOperator_method_declaration"):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_method_declaration"):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = EParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(EParser.DEFINE)
            self.state = 547
            localctx.op = self.operator()
            self.state = 548
            self.match(EParser.AS)
            self.state = 549
            self.match(EParser.OPERATOR)
            self.state = 550
            self.match(EParser.RECEIVING)
            self.state = 551
            localctx.arg = self.operator_argument()
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 552
                self.match(EParser.RETURNING)
                self.state = 553
                localctx.typ = self.typedef(0)


            self.state = 556
            self.match(EParser.DOING)
            self.state = 557
            self.match(EParser.COLON)
            self.state = 558
            self.indent()
            self.state = 559
            localctx.stmts = self.statement_list()
            self.state = 560
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

        def AS(self):
            return self.getToken(EParser.AS, 0)

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
            if hasattr(listener, "enterSetter_method_declaration"):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetter_method_declaration"):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = EParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(EParser.DEFINE)
            self.state = 563
            localctx.name = self.variable_identifier()
            self.state = 564
            self.match(EParser.AS)
            self.state = 565
            self.match(EParser.SETTER)
            self.state = 566
            self.match(EParser.DOING)
            self.state = 567
            self.match(EParser.COLON)
            self.state = 568
            self.indent()
            self.state = 569
            localctx.stmts = self.statement_list()
            self.state = 570
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
            super(EParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

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


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def getRuleIndex(self):
            return EParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_setter_declaration"):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_setter_declaration"):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = EParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(EParser.DEFINE)
            self.state = 573
            localctx.name = self.variable_identifier()
            self.state = 574
            self.match(EParser.AS)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 575
                self.match(EParser.NATIVE)


            self.state = 578
            self.match(EParser.SETTER)
            self.state = 579
            self.match(EParser.DOING)
            self.state = 580
            self.match(EParser.COLON)
            self.state = 581
            self.indent()
            self.state = 582
            localctx.stmts = self.native_statement_list()
            self.state = 583
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

        def AS(self):
            return self.getToken(EParser.AS, 0)

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
            if hasattr(listener, "enterGetter_method_declaration"):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGetter_method_declaration"):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = EParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(EParser.DEFINE)
            self.state = 586
            localctx.name = self.variable_identifier()
            self.state = 587
            self.match(EParser.AS)
            self.state = 588
            self.match(EParser.GETTER)
            self.state = 589
            self.match(EParser.DOING)
            self.state = 590
            self.match(EParser.COLON)
            self.state = 591
            self.indent()
            self.state = 592
            localctx.stmts = self.statement_list()
            self.state = 593
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
            super(EParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

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


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def getRuleIndex(self):
            return EParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_getter_declaration"):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_getter_declaration"):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = EParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(EParser.DEFINE)
            self.state = 596
            localctx.name = self.variable_identifier()
            self.state = 597
            self.match(EParser.AS)
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 598
                self.match(EParser.NATIVE)


            self.state = 601
            self.match(EParser.GETTER)
            self.state = 602
            self.match(EParser.DOING)
            self.state = 603
            self.match(EParser.COLON)
            self.state = 604
            self.indent()
            self.state = 605
            localctx.stmts = self.native_statement_list()
            self.state = 606
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
            if hasattr(listener, "enterNative_category_declaration"):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_declaration"):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = EParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(EParser.DEFINE)
            self.state = 609
            localctx.name = self.type_identifier()
            self.state = 610
            self.match(EParser.AS)
            self.state = 612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 611
                self.match(EParser.STORABLE)


            self.state = 614
            self.match(EParser.NATIVE)
            self.state = 615
            self.match(EParser.CATEGORY)
            self.state = 623
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 616
                localctx.attrs = self.attribute_list()
                self.state = 617
                self.match(EParser.COMMA)
                self.state = 618
                self.match(EParser.AND)
                self.state = 619
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 621
                self.match(EParser.WITH)
                self.state = 622
                self.match(EParser.BINDINGS)
                pass


            self.state = 625
            self.match(EParser.COLON)
            self.state = 626
            self.indent()
            self.state = 627
            localctx.bindings = self.native_category_bindings()
            self.state = 628
            self.dedent()
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 629
                self.lfp()
                self.state = 630
                self.match(EParser.AND)
                self.state = 631
                self.match(EParser.METHODS)
                self.state = 632
                self.match(EParser.COLON)
                self.state = 633
                self.indent()
                self.state = 634
                localctx.methods = self.native_member_method_declaration_list()
                self.state = 635
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
            return EParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_resource_declaration"):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_resource_declaration"):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = EParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.match(EParser.DEFINE)
            self.state = 640
            localctx.name = self.type_identifier()
            self.state = 641
            self.match(EParser.AS)
            self.state = 643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 642
                self.match(EParser.STORABLE)


            self.state = 645
            self.match(EParser.NATIVE)
            self.state = 646
            self.match(EParser.RESOURCE)
            self.state = 654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 647
                localctx.attrs = self.attribute_list()
                self.state = 648
                self.match(EParser.COMMA)
                self.state = 649
                self.match(EParser.AND)
                self.state = 650
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 652
                self.match(EParser.WITH)
                self.state = 653
                self.match(EParser.BINDINGS)
                pass


            self.state = 656
            self.match(EParser.COLON)
            self.state = 657
            self.indent()
            self.state = 658
            localctx.bindings = self.native_category_bindings()
            self.state = 659
            self.dedent()
            self.state = 668
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 660
                self.lfp()
                self.state = 661
                self.match(EParser.AND)
                self.state = 662
                self.match(EParser.METHODS)
                self.state = 663
                self.match(EParser.COLON)
                self.state = 664
                self.indent()
                self.state = 665
                localctx.methods = self.native_member_method_declaration_list()
                self.state = 666
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
            if hasattr(listener, "enterNative_category_bindings"):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_bindings"):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = EParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.match(EParser.DEFINE)
            self.state = 671
            self.match(EParser.CATEGORY)
            self.state = 672
            self.match(EParser.BINDINGS)
            self.state = 673
            self.match(EParser.AS)
            self.state = 674
            self.match(EParser.COLON)
            self.state = 675
            self.indent()
            self.state = 676
            localctx.items = self.native_category_binding_list(0)
            self.state = 677
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
            if hasattr(listener, "enterNativeCategoryBindingListItem"):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingListItem"):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingList"):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingList"):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 680
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 688
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryBindingListItemContext(self, EParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 682
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 683
                    self.lfp()
                    self.state = 684
                    localctx.item = self.native_category_binding() 
                self.state = 690
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.item = None # Attribute_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)
        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAttributeList"):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttributeList"):
                listener.exitAttributeList(self)


    class AttributeListItemContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListItemContext, self).__init__(parser)
            self.items = None # Attribute_identifier_listContext
            self.item = None # Attribute_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTES(self):
            return self.getToken(EParser.ATTRIBUTES, 0)
        def attribute_identifier_list(self):
            return self.getTypedRuleContext(EParser.Attribute_identifier_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAttributeListItem"):
                listener.enterAttributeListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttributeListItem"):
                listener.exitAttributeListItem(self)



    def attribute_list(self):

        localctx = EParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_attribute_list)
        try:
            self.state = 701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 691
                self.match(EParser.WITH)
                self.state = 692
                self.match(EParser.ATTRIBUTE)
                self.state = 693
                localctx.item = self.attribute_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 694
                self.match(EParser.WITH)
                self.state = 695
                self.match(EParser.ATTRIBUTES)
                self.state = 696
                localctx.items = self.attribute_identifier_list()
                self.state = 699
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 697
                    self.match(EParser.AND)
                    self.state = 698
                    localctx.item = self.attribute_identifier()


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
            if hasattr(listener, "enterAbstract_method_declaration"):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAbstract_method_declaration"):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = EParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.match(EParser.DEFINE)
            self.state = 704
            localctx.name = self.method_identifier()
            self.state = 705
            self.match(EParser.AS)
            self.state = 706
            self.match(EParser.ABSTRACT)
            self.state = 707
            self.match(EParser.METHOD)
            self.state = 710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 708
                self.match(EParser.RECEIVING)
                self.state = 709
                localctx.args = self.full_argument_list()


            self.state = 714
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 712
                self.match(EParser.RETURNING)
                self.state = 713
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
            if hasattr(listener, "enterConcrete_method_declaration"):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_method_declaration"):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = EParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(EParser.DEFINE)
            self.state = 717
            localctx.name = self.method_identifier()
            self.state = 718
            self.match(EParser.AS)
            self.state = 719
            self.match(EParser.METHOD)
            self.state = 722
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 720
                self.match(EParser.RECEIVING)
                self.state = 721
                localctx.args = self.full_argument_list()


            self.state = 726
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 724
                self.match(EParser.RETURNING)
                self.state = 725
                localctx.typ = self.typedef(0)


            self.state = 728
            self.match(EParser.DOING)
            self.state = 729
            self.match(EParser.COLON)
            self.state = 730
            self.indent()
            self.state = 731
            localctx.stmts = self.statement_list()
            self.state = 732
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


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

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
            if hasattr(listener, "enterNative_method_declaration"):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_method_declaration"):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = EParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(EParser.DEFINE)
            self.state = 735
            localctx.name = self.method_identifier()
            self.state = 736
            self.match(EParser.AS)
            self.state = 738
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 737
                self.match(EParser.NATIVE)


            self.state = 740
            self.match(EParser.METHOD)
            self.state = 743
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 741
                self.match(EParser.RECEIVING)
                self.state = 742
                localctx.args = self.full_argument_list()


            self.state = 747
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 745
                self.match(EParser.RETURNING)
                self.state = 746
                localctx.typ = self.category_or_any_type()


            self.state = 749
            self.match(EParser.DOING)
            self.state = 750
            self.match(EParser.COLON)
            self.state = 751
            self.indent()
            self.state = 752
            localctx.stmts = self.native_statement_list()
            self.state = 753
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
            if hasattr(listener, "enterTest_method_declaration"):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTest_method_declaration"):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = EParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(EParser.DEFINE)
            self.state = 756
            localctx.name = self.match(EParser.TEXT_LITERAL)
            self.state = 757
            self.match(EParser.AS)
            self.state = 758
            self.match(EParser.TEST)
            self.state = 759
            self.match(EParser.METHOD)
            self.state = 760
            self.match(EParser.DOING)
            self.state = 761
            self.match(EParser.COLON)
            self.state = 762
            self.indent()
            self.state = 763
            localctx.stmts = self.statement_list()
            self.state = 764
            self.dedent()
            self.state = 765
            self.lfp()
            self.state = 766
            self.match(EParser.AND)
            self.state = 767
            self.match(EParser.VERIFYING)
            self.state = 774
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.COLON]:
                self.state = 768
                self.match(EParser.COLON)
                self.state = 769
                self.indent()
                self.state = 770
                localctx.exps = self.assertion_list()
                self.state = 771
                self.dedent()
                pass
            elif token in [EParser.SYMBOL_IDENTIFIER]:
                self.state = 773
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
            super(EParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assertion

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion"):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion"):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = EParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
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
            if hasattr(listener, "enterFull_argument_list"):
                listener.enterFull_argument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFull_argument_list"):
                listener.exitFull_argument_list(self)




    def full_argument_list(self):

        localctx = EParser.Full_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_full_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778
            localctx.items = self.argument_list()
            self.state = 781
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.AND:
                self.state = 779
                self.match(EParser.AND)
                self.state = 780
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
            if hasattr(listener, "enterTyped_argument"):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTyped_argument"):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = EParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 783
            localctx.typ = self.category_or_any_type()
            self.state = 784
            localctx.name = self.variable_identifier()
            self.state = 786
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 785
                localctx.attrs = self.attribute_list()


            self.state = 790
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.EQ:
                self.state = 788
                self.match(EParser.EQ)
                self.state = 789
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
            if hasattr(listener, "enterCommentStatement"):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCommentStatement"):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(EParser.Store_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterStoreStatement"):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStoreStatement"):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(EParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithSingletonStatement"):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithSingletonStatement"):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(EParser.Write_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWriteStatement"):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWriteStatement"):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(EParser.While_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWhileStatement"):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhileStatement"):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(EParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithResourceStatement"):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithResourceStatement"):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(EParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRaiseStatement"):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaiseStatement"):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(EParser.Break_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBreakStatement"):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreakStatement"):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(EParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignInstanceStatement"):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignInstanceStatement"):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(EParser.If_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIfStatement"):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIfStatement"):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(EParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSwitchStatement"):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitchStatement"):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(EParser.Try_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTryStatement"):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTryStatement"):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_call_statementContext
            self.copyFrom(ctx)

        def method_call_statement(self):
            return self.getTypedRuleContext(EParser.Method_call_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodCallStatement"):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodCallStatement"):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(EParser.Return_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReturnStatement"):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturnStatement"):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(EParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignTupleStatement"):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignTupleStatement"):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureStatement"):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureStatement"):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(EParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFlushStatement"):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlushStatement"):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(EParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDoWhileStatement"):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDoWhileStatement"):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(EParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterForEachStatement"):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitForEachStatement"):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = EParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 811
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 792
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 793
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 794
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 795
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = EParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 796
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = EParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 797
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 798
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 799
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 800
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 801
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 802
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 803
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 804
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 805
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 806
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 807
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 808
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 809
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = EParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 810
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
            super(EParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(EParser.FLUSH, 0)

        def getRuleIndex(self):
            return EParser.RULE_flush_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFlush_statement"):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlush_statement"):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = EParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 813
            self.match(EParser.FLUSH)
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
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(EParser.DELETE, 0)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(EParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(EParser.STORE, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_store_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterStore_statement"):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStore_statement"):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = EParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_store_statement)
        try:
            self.state = 825
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 815
                self.match(EParser.DELETE)
                self.state = 816
                localctx.to_del = self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 817
                self.match(EParser.STORE)
                self.state = 818
                localctx.to_add = self.expression_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 819
                self.match(EParser.DELETE)
                self.state = 820
                localctx.to_del = self.expression_list()
                self.state = 821
                self.match(EParser.AND)
                self.state = 822
                self.match(EParser.STORE)
                self.state = 823
                localctx.to_add = self.expression_list()
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
            if hasattr(listener, "enterInvokeStatement"):
                listener.enterInvokeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInvokeStatement"):
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
            if hasattr(listener, "enterUnresolvedWithArgsStatement"):
                listener.enterUnresolvedWithArgsStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnresolvedWithArgsStatement"):
                listener.exitUnresolvedWithArgsStatement(self)



    def method_call_statement(self):

        localctx = EParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_call_statement)
        try:
            self.state = 832
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 827
                localctx.exp = self.unresolved_expression(0)
                self.state = 829
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 828
                    localctx.args = self.argument_assignment_list()


                pass
            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 831
                localctx.exp = self.invocation_expression()
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
            if hasattr(listener, "enterWith_resource_statement"):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_resource_statement"):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = EParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 834
            self.match(EParser.WITH)
            self.state = 835
            localctx.stmt = self.assign_variable_statement()
            self.state = 836
            self.match(EParser.COMMA)
            self.state = 837
            self.match(EParser.DO)
            self.state = 838
            self.match(EParser.COLON)
            self.state = 839
            self.indent()
            self.state = 840
            localctx.stmts = self.statement_list()
            self.state = 841
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
            if hasattr(listener, "enterWith_singleton_statement"):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_singleton_statement"):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = EParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 843
            self.match(EParser.WITH)
            self.state = 844
            localctx.typ = self.type_identifier()
            self.state = 845
            self.match(EParser.COMMA)
            self.state = 846
            self.match(EParser.DO)
            self.state = 847
            self.match(EParser.COLON)
            self.state = 848
            self.indent()
            self.state = 849
            localctx.stmts = self.statement_list()
            self.state = 850
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
            if hasattr(listener, "enterSwitch_statement"):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_statement"):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = EParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 852
            self.match(EParser.SWITCH)
            self.state = 853
            self.match(EParser.ON)
            self.state = 854
            localctx.exp = self.expression(0)
            self.state = 855
            self.match(EParser.COLON)
            self.state = 856
            self.indent()
            self.state = 857
            localctx.cases = self.switch_case_statement_list()
            self.state = 865
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 858
                self.lfp()
                self.state = 859
                self.match(EParser.OTHERWISE)
                self.state = 860
                self.match(EParser.COLON)
                self.state = 861
                self.indent()
                self.state = 862
                localctx.stmts = self.statement_list()
                self.state = 863
                self.dedent()


            self.state = 867
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
            if hasattr(listener, "enterAtomicSwitchCase"):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomicSwitchCase"):
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
            if hasattr(listener, "enterCollectionSwitchCase"):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollectionSwitchCase"):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = EParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_case_statement)
        try:
            self.state = 884
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 869
                self.match(EParser.WHEN)
                self.state = 870
                localctx.exp = self.atomic_literal()
                self.state = 871
                self.match(EParser.COLON)
                self.state = 872
                self.indent()
                self.state = 873
                localctx.stmts = self.statement_list()
                self.state = 874
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 876
                self.match(EParser.WHEN)
                self.state = 877
                self.match(EParser.IN)
                self.state = 878
                localctx.exp = self.literal_collection()
                self.state = 879
                self.match(EParser.COLON)
                self.state = 880
                self.indent()
                self.state = 881
                localctx.stmts = self.statement_list()
                self.state = 882
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
            if hasattr(listener, "enterFor_each_statement"):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFor_each_statement"):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = EParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 886
            self.match(EParser.FOR)
            self.state = 887
            self.match(EParser.EACH)
            self.state = 888
            localctx.name1 = self.variable_identifier()
            self.state = 891
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 889
                self.match(EParser.COMMA)
                self.state = 890
                localctx.name2 = self.variable_identifier()


            self.state = 893
            self.match(EParser.IN)
            self.state = 894
            localctx.source = self.expression(0)
            self.state = 895
            self.match(EParser.COLON)
            self.state = 896
            self.indent()
            self.state = 897
            localctx.stmts = self.statement_list()
            self.state = 898
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
            if hasattr(listener, "enterDo_while_statement"):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDo_while_statement"):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = EParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 900
            self.match(EParser.DO)
            self.state = 901
            self.match(EParser.COLON)
            self.state = 902
            self.indent()
            self.state = 903
            localctx.stmts = self.statement_list()
            self.state = 904
            self.dedent()
            self.state = 905
            self.lfp()
            self.state = 906
            self.match(EParser.WHILE)
            self.state = 907
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
            if hasattr(listener, "enterWhile_statement"):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhile_statement"):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = EParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 909
            self.match(EParser.WHILE)
            self.state = 910
            localctx.exp = self.expression(0)
            self.state = 911
            self.match(EParser.COLON)
            self.state = 912
            self.indent()
            self.state = 913
            localctx.stmts = self.statement_list()
            self.state = 914
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
            if hasattr(listener, "enterIf_statement"):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf_statement"):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = EParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 916
            self.match(EParser.IF)
            self.state = 917
            localctx.exp = self.expression(0)
            self.state = 918
            self.match(EParser.COLON)
            self.state = 919
            self.indent()
            self.state = 920
            localctx.stmts = self.statement_list()
            self.state = 921
            self.dedent()
            self.state = 925
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 922
                self.lfp()
                self.state = 923
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 934
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 927
                self.lfp()
                self.state = 928
                self.match(EParser.ELSE)
                self.state = 929
                self.match(EParser.COLON)
                self.state = 930
                self.indent()
                self.state = 931
                localctx.elseStmts = self.statement_list()
                self.state = 932
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
            if hasattr(listener, "enterElseIfStatementList"):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementList"):
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
            if hasattr(listener, "enterElseIfStatementListItem"):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementListItem"):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 937
            self.match(EParser.ELSE)
            self.state = 938
            self.match(EParser.IF)
            self.state = 939
            localctx.exp = self.expression(0)
            self.state = 940
            self.match(EParser.COLON)
            self.state = 941
            self.indent()
            self.state = 942
            localctx.stmts = self.statement_list()
            self.state = 943
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 957
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 945
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 946
                    self.lfp()
                    self.state = 947
                    self.match(EParser.ELSE)
                    self.state = 948
                    self.match(EParser.IF)
                    self.state = 949
                    localctx.exp = self.expression(0)
                    self.state = 950
                    self.match(EParser.COLON)
                    self.state = 951
                    self.indent()
                    self.state = 952
                    localctx.stmts = self.statement_list()
                    self.state = 953
                    self.dedent() 
                self.state = 959
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
            if hasattr(listener, "enterRaise_statement"):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaise_statement"):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = EParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 960
            self.match(EParser.RAISE)
            self.state = 961
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
            if hasattr(listener, "enterTry_statement"):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTry_statement"):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = EParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 963
            self.match(EParser.SWITCH)
            self.state = 964
            self.match(EParser.ON)
            self.state = 965
            localctx.name = self.variable_identifier()
            self.state = 966
            self.match(EParser.DOING)
            self.state = 967
            self.match(EParser.COLON)
            self.state = 968
            self.indent()
            self.state = 969
            localctx.stmts = self.statement_list()
            self.state = 970
            self.dedent()
            self.state = 971
            self.lfs()
            self.state = 973
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 972
                localctx.handlers = self.catch_statement_list()


            self.state = 986
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.OTHERWISE or _la==EParser.WHEN:
                self.state = 978
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 975
                    self.match(EParser.OTHERWISE)
                    pass
                elif token in [EParser.WHEN]:
                    self.state = 976
                    self.match(EParser.WHEN)
                    self.state = 977
                    self.match(EParser.ANY)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 980
                self.match(EParser.COLON)
                self.state = 981
                self.indent()
                self.state = 982
                localctx.anyStmts = self.statement_list()
                self.state = 983
                self.dedent()
                self.state = 984
                self.lfs()


            self.state = 995
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.ALWAYS:
                self.state = 988
                self.match(EParser.ALWAYS)
                self.state = 989
                self.match(EParser.COLON)
                self.state = 990
                self.indent()
                self.state = 991
                localctx.finalStmts = self.statement_list()
                self.state = 992
                self.dedent()
                self.state = 993
                self.lfs()


            self.state = 997
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
            if hasattr(listener, "enterCatchAtomicStatement"):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchAtomicStatement"):
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
            if hasattr(listener, "enterCatchCollectionStatement"):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchCollectionStatement"):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = EParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_catch_statement)
        try:
            self.state = 1018
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 999
                self.match(EParser.WHEN)
                self.state = 1000
                localctx.name = self.symbol_identifier()
                self.state = 1001
                self.match(EParser.COLON)
                self.state = 1002
                self.indent()
                self.state = 1003
                localctx.stmts = self.statement_list()
                self.state = 1004
                self.dedent()
                self.state = 1005
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1007
                self.match(EParser.WHEN)
                self.state = 1008
                self.match(EParser.IN)
                self.state = 1009
                self.match(EParser.LBRAK)
                self.state = 1010
                localctx.exp = self.symbol_list()
                self.state = 1011
                self.match(EParser.RBRAK)
                self.state = 1012
                self.match(EParser.COLON)
                self.state = 1013
                self.indent()
                self.state = 1014
                localctx.stmts = self.statement_list()
                self.state = 1015
                self.dedent()
                self.state = 1016
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
            super(EParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(EParser.BREAK, 0)

        def getRuleIndex(self):
            return EParser.RULE_break_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterBreak_statement"):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreak_statement"):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = EParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1020
            self.match(EParser.BREAK)
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
            if hasattr(listener, "enterReturn_statement"):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturn_statement"):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = EParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1022
            self.match(EParser.RETURN)
            self.state = 1024
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (EParser.EXECUTE - 99)) | (1 << (EParser.FETCH - 99)) | (1 << (EParser.INVOKE - 99)) | (1 << (EParser.MUTABLE - 99)) | (1 << (EParser.NOT - 99)) | (1 << (EParser.NOTHING - 99)) | (1 << (EParser.READ - 99)) | (1 << (EParser.SELF - 99)) | (1 << (EParser.SORTED - 99)) | (1 << (EParser.THIS - 99)) | (1 << (EParser.BOOLEAN_LITERAL - 99)) | (1 << (EParser.CHAR_LITERAL - 99)) | (1 << (EParser.MIN_INTEGER - 99)) | (1 << (EParser.MAX_INTEGER - 99)) | (1 << (EParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (EParser.TYPE_IDENTIFIER - 163)) | (1 << (EParser.VARIABLE_IDENTIFIER - 163)) | (1 << (EParser.TEXT_LITERAL - 163)) | (1 << (EParser.UUID_LITERAL - 163)) | (1 << (EParser.INTEGER_LITERAL - 163)) | (1 << (EParser.HEXA_LITERAL - 163)) | (1 << (EParser.DECIMAL_LITERAL - 163)) | (1 << (EParser.DATETIME_LITERAL - 163)) | (1 << (EParser.TIME_LITERAL - 163)) | (1 << (EParser.DATE_LITERAL - 163)) | (1 << (EParser.PERIOD_LITERAL - 163)) | (1 << (EParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1023
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
            if hasattr(listener, "enterIntDivideExpression"):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntDivideExpression"):
                listener.exitIntDivideExpression(self)


    class HasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.HasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(EParser.HAS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAnyExpression"):
                listener.enterHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAnyExpression"):
                listener.exitHasAnyExpression(self)


    class HasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.HasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(EParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasExpression"):
                listener.enterHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasExpression"):
                listener.exitHasExpression(self)


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
            if hasattr(listener, "enterTernaryExpression"):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTernaryExpression"):
                listener.exitTernaryExpression(self)


    class FetchStoreExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FetchStoreExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_store_expressionContext
            self.copyFrom(ctx)

        def fetch_store_expression(self):
            return self.getTypedRuleContext(EParser.Fetch_store_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchStoreExpression"):
                listener.enterFetchStoreExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchStoreExpression"):
                listener.exitFetchStoreExpression(self)


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
            if hasattr(listener, "enterNotEqualsExpression"):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotEqualsExpression"):
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
            if hasattr(listener, "enterInExpression"):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInExpression"):
                listener.exitInExpression(self)


    class DocumentExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(EParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDocumentExpression"):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocumentExpression"):
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
            if hasattr(listener, "enterNotExpression"):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotExpression"):
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
            if hasattr(listener, "enterGreaterThanExpression"):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanExpression"):
                listener.exitGreaterThanExpression(self)


    class InvocationExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InvocationExpressionContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterInvocationExpression"):
                listener.enterInvocationExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInvocationExpression"):
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
            if hasattr(listener, "enterOrExpression"):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrExpression"):
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
            if hasattr(listener, "enterCodeExpression"):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeExpression"):
                listener.exitCodeExpression(self)


    class AmbiguousExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AmbiguousExpressionContext, self).__init__(parser)
            self.exp = None # Ambiguous_expressionContext
            self.copyFrom(ctx)

        def ambiguous_expression(self):
            return self.getTypedRuleContext(EParser.Ambiguous_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAmbiguousExpression"):
                listener.enterAmbiguousExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAmbiguousExpression"):
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
            if hasattr(listener, "enterLessThanOrEqualExpression"):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanOrEqualExpression"):
                listener.exitLessThanOrEqualExpression(self)


    class ReadOneExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadOneExpressionContext, self).__init__(parser)
            self.exp = None # Read_one_expressionContext
            self.copyFrom(ctx)

        def read_one_expression(self):
            return self.getTypedRuleContext(EParser.Read_one_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReadOneExpression"):
                listener.enterReadOneExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReadOneExpression"):
                listener.exitReadOneExpression(self)


    class NotHasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotHasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def HAS(self):
            return self.getToken(EParser.HAS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAnyExpression"):
                listener.enterNotHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAnyExpression"):
                listener.exitNotHasAnyExpression(self)


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
            if hasattr(listener, "enterAndExpression"):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndExpression"):
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
            if hasattr(listener, "enterMethodCallExpression"):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodCallExpression"):
                listener.exitMethodCallExpression(self)


    class NotHasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotHasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def HAS(self):
            return self.getToken(EParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasExpression"):
                listener.enterNotHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasExpression"):
                listener.exitNotHasExpression(self)


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
            if hasattr(listener, "enterClosureExpression"):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureExpression"):
                listener.exitClosureExpression(self)


    class SortedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(EParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSortedExpression"):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSortedExpression"):
                listener.exitSortedExpression(self)


    class NotHasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotHasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def HAS(self):
            return self.getToken(EParser.HAS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAllExpression"):
                listener.enterNotHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAllExpression"):
                listener.exitNotHasAllExpression(self)


    class BlobExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.BlobExpressionContext, self).__init__(parser)
            self.exp = None # Blob_expressionContext
            self.copyFrom(ctx)

        def blob_expression(self):
            return self.getTypedRuleContext(EParser.Blob_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBlobExpression"):
                listener.enterBlobExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlobExpression"):
                listener.exitBlobExpression(self)


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
            if hasattr(listener, "enterContainsExpression"):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContainsExpression"):
                listener.exitContainsExpression(self)


    class FilteredListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FilteredListExpressionContext, self).__init__(parser)
            self.src = None # ExpressionContext
            self.copyFrom(ctx)

        def filtered_list_suffix(self):
            return self.getTypedRuleContext(EParser.Filtered_list_suffixContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFilteredListExpression"):
                listener.enterFilteredListExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFilteredListExpression"):
                listener.exitFilteredListExpression(self)


    class ConstructorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(EParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorExpression"):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorExpression"):
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
            if hasattr(listener, "enterNotContainsExpression"):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotContainsExpression"):
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
            if hasattr(listener, "enterMultiplyExpression"):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiplyExpression"):
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
            if hasattr(listener, "enterRoughlyEqualsExpression"):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRoughlyEqualsExpression"):
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
            if hasattr(listener, "enterExecuteExpression"):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExecuteExpression"):
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
            if hasattr(listener, "enterGreaterThanOrEqualExpression"):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanOrEqualExpression"):
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
            if hasattr(listener, "enterNotInExpression"):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotInExpression"):
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
            if hasattr(listener, "enterIteratorExpression"):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorExpression"):
                listener.exitIteratorExpression(self)


    class UnresolvedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.UnresolvedExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterUnresolvedExpression"):
                listener.enterUnresolvedExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnresolvedExpression"):
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
            if hasattr(listener, "enterIsNotExpression"):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotExpression"):
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
            if hasattr(listener, "enterDivideExpression"):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivideExpression"):
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
            if hasattr(listener, "enterIsExpression"):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsExpression"):
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
            if hasattr(listener, "enterMinusExpression"):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinusExpression"):
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
            if hasattr(listener, "enterAddExpression"):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddExpression"):
                listener.exitAddExpression(self)


    class HasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.HasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(EParser.HAS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAllExpression"):
                listener.enterHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAllExpression"):
                listener.exitHasAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterInstanceExpression"):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInstanceExpression"):
                listener.exitInstanceExpression(self)


    class ReadAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadAllExpressionContext, self).__init__(parser)
            self.exp = None # Read_all_expressionContext
            self.copyFrom(ctx)

        def read_all_expression(self):
            return self.getTypedRuleContext(EParser.Read_all_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReadAllExpression"):
                listener.enterReadAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReadAllExpression"):
                listener.exitReadAllExpression(self)


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
            if hasattr(listener, "enterCastExpression"):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCastExpression"):
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
            if hasattr(listener, "enterModuloExpression"):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModuloExpression"):
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
            if hasattr(listener, "enterLessThanExpression"):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanExpression"):
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
            if hasattr(listener, "enterEqualsExpression"):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEqualsExpression"):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1054
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1027
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1028
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1029
                localctx.exp = self.unresolved_expression(0)
                self.state = 1030
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 4:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1032
                self.match(EParser.MINUS)
                self.state = 1033
                localctx.exp = self.expression(44)
                pass

            elif la_ == 5:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1034
                self.match(EParser.NOT)
                self.state = 1035
                localctx.exp = self.expression(43)
                pass

            elif la_ == 6:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1036
                self.match(EParser.CODE)
                self.state = 1037
                self.match(EParser.COLON)
                self.state = 1038
                localctx.exp = self.expression(14)
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1039
                self.match(EParser.EXECUTE)
                self.state = 1040
                self.match(EParser.COLON)
                self.state = 1041
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1042
                self.match(EParser.METHOD_T)
                self.state = 1043
                self.match(EParser.COLON)
                self.state = 1044
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.BlobExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1045
                localctx.exp = self.blob_expression()
                pass

            elif la_ == 10:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1046
                localctx.exp = self.document_expression()
                pass

            elif la_ == 11:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1047
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 12:
                localctx = EParser.FetchStoreExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1048
                localctx.exp = self.fetch_store_expression()
                pass

            elif la_ == 13:
                localctx = EParser.ReadAllExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1049
                localctx.exp = self.read_all_expression()
                pass

            elif la_ == 14:
                localctx = EParser.ReadOneExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1050
                localctx.exp = self.read_one_expression()
                pass

            elif la_ == 15:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1051
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 16:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1052
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 17:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1053
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1166
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1056
                        if not self.precpred(self._ctx, 42):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 42)")
                        self.state = 1057
                        self.multiply()
                        self.state = 1058
                        localctx.right = self.expression(43)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1060
                        if not self.precpred(self._ctx, 41):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 41)")
                        self.state = 1061
                        self.divide()
                        self.state = 1062
                        localctx.right = self.expression(42)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1064
                        if not self.precpred(self._ctx, 40):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 40)")
                        self.state = 1065
                        self.modulo()
                        self.state = 1066
                        localctx.right = self.expression(41)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1068
                        if not self.precpred(self._ctx, 39):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 39)")
                        self.state = 1069
                        self.idivide()
                        self.state = 1070
                        localctx.right = self.expression(40)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1072
                        if not self.precpred(self._ctx, 38):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 38)")
                        self.state = 1073
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 1074
                        localctx.right = self.expression(39)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1075
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 1076
                        self.match(EParser.LT)
                        self.state = 1077
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1078
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 1079
                        self.match(EParser.LTE)
                        self.state = 1080
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1081
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 1082
                        self.match(EParser.GT)
                        self.state = 1083
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1084
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 1085
                        self.match(EParser.GTE)
                        self.state = 1086
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1087
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1088
                        self.match(EParser.EQ)
                        self.state = 1089
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1090
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1091
                        self.match(EParser.LTGT)
                        self.state = 1092
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1093
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1094
                        self.match(EParser.TILDE)
                        self.state = 1095
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 13:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1096
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1097
                        self.match(EParser.CONTAINS)
                        self.state = 1098
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 14:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1099
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1100
                        self.match(EParser.IN)
                        self.state = 1101
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 15:
                        localctx = EParser.HasExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1102
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1103
                        self.match(EParser.HAS)
                        self.state = 1104
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 16:
                        localctx = EParser.HasAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1105
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1106
                        self.match(EParser.HAS)
                        self.state = 1107
                        self.match(EParser.ALL)
                        self.state = 1108
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 17:
                        localctx = EParser.HasAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1109
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1110
                        self.match(EParser.HAS)
                        self.state = 1111
                        self.match(EParser.ANY)
                        self.state = 1112
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 18:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1113
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1114
                        self.match(EParser.NOT)
                        self.state = 1115
                        self.match(EParser.CONTAINS)
                        self.state = 1116
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 19:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1117
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1118
                        self.match(EParser.NOT)
                        self.state = 1119
                        self.match(EParser.IN)
                        self.state = 1120
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotHasExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1121
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1122
                        self.match(EParser.NOT)
                        self.state = 1123
                        self.match(EParser.HAS)
                        self.state = 1124
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotHasAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1125
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1126
                        self.match(EParser.NOT)
                        self.state = 1127
                        self.match(EParser.HAS)
                        self.state = 1128
                        self.match(EParser.ALL)
                        self.state = 1129
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotHasAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1130
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1131
                        self.match(EParser.NOT)
                        self.state = 1132
                        self.match(EParser.HAS)
                        self.state = 1133
                        self.match(EParser.ANY)
                        self.state = 1134
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 23:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1135
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1136
                        self.match(EParser.OR)
                        self.state = 1137
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 24:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1138
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1139
                        self.match(EParser.AND)
                        self.state = 1140
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 25:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1141
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1142
                        self.match(EParser.IF)
                        self.state = 1143
                        localctx.test = self.expression(0)
                        self.state = 1144
                        self.match(EParser.ELSE)
                        self.state = 1145
                        localctx.ifFalse = self.expression(16)
                        pass

                    elif la_ == 26:
                        localctx = EParser.IteratorExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1147
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1148
                        self.match(EParser.FOR)
                        self.state = 1149
                        self.match(EParser.EACH)
                        self.state = 1150
                        localctx.name = self.variable_identifier()
                        self.state = 1151
                        self.match(EParser.IN)
                        self.state = 1152
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 27:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1154
                        if not self.precpred(self._ctx, 37):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 37)")
                        self.state = 1155
                        self.match(EParser.AS)
                        self.state = 1156
                        localctx.right = self.category_or_any_type()
                        pass

                    elif la_ == 28:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1157
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1158
                        self.match(EParser.IS)
                        self.state = 1159
                        self.match(EParser.NOT)
                        self.state = 1160
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 29:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1161
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1162
                        self.match(EParser.IS)
                        self.state = 1163
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 30:
                        localctx = EParser.FilteredListExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.src = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1164
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1165
                        self.filtered_list_suffix()
                        pass

             
                self.state = 1170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
            if hasattr(listener, "enterUnresolvedSelector"):
                listener.enterUnresolvedSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnresolvedSelector"):
                listener.exitUnresolvedSelector(self)


    class UnresolvedIdentifierContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedIdentifierContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterUnresolvedIdentifier"):
                listener.enterUnresolvedIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnresolvedIdentifier"):
                listener.exitUnresolvedIdentifier(self)



    def unresolved_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Unresolved_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1172
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1174
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1175
                    localctx.selector = self.unresolved_selector() 
                self.state = 1180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
            if hasattr(listener, "enterUnresolved_selector"):
                listener.enterUnresolved_selector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnresolved_selector"):
                listener.exitUnresolved_selector(self)




    def unresolved_selector(self):

        localctx = EParser.Unresolved_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1181
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1182
            self.match(EParser.DOT)
            self.state = 1183
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
            if hasattr(listener, "enterInvocation_expression"):
                listener.enterInvocation_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInvocation_expression"):
                listener.exitInvocation_expression(self)




    def invocation_expression(self):

        localctx = EParser.Invocation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185
            self.match(EParser.INVOKE)
            self.state = 1186
            self.match(EParser.COLON)
            self.state = 1187
            localctx.name = self.variable_identifier()
            self.state = 1188
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
            if hasattr(listener, "enterInvocation_trailer"):
                listener.enterInvocation_trailer(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInvocation_trailer"):
                listener.exitInvocation_trailer(self)




    def invocation_trailer(self):

        localctx = EParser.Invocation_trailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1190
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
            if hasattr(listener, "enterSelectorExpression"):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectorExpression"):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(EParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectableExpression"):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectableExpression"):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1193
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1195
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1196
                    localctx.selector = self.instance_selector() 
                self.state = 1201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
            if hasattr(listener, "enterSliceSelector"):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceSelector"):
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
            if hasattr(listener, "enterMemberSelector"):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberSelector"):
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
            if hasattr(listener, "enterItemSelector"):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemSelector"):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = EParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance_selector)
        try:
            self.state = 1215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1202
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1203
                self.match(EParser.DOT)
                self.state = 1204
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1205
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1206
                self.match(EParser.LBRAK)
                self.state = 1207
                localctx.xslice = self.slice_arguments()
                self.state = 1208
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1210
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1211
                self.match(EParser.LBRAK)
                self.state = 1212
                localctx.exp = self.expression(0)
                self.state = 1213
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

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_document_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterDocument_expression"):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocument_expression"):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = EParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1217
            self.match(EParser.DOCUMENT)
            self.state = 1220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 1218
                self.match(EParser.FROM)
                self.state = 1219
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Blob_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_blob_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterBlob_expression"):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlob_expression"):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = EParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blob_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1222
            self.match(EParser.BLOB)
            self.state = 1223
            self.match(EParser.FROM)
            self.state = 1224
            self.expression(0)
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
            self.copyExp = None # ExpressionContext
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
            if hasattr(listener, "enterConstructorFrom"):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorFrom"):
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
            if hasattr(listener, "enterConstructorNoFrom"):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorNoFrom"):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = EParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1226
                localctx.typ = self.mutable_category_type()
                self.state = 1227
                self.match(EParser.FROM)
                self.state = 1228
                localctx.copyExp = self.expression(0)
                self.state = 1237
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 1230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1229
                        self.match(EParser.COMMA)


                    self.state = 1232
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1235
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
                    if la_ == 1:
                        self.state = 1233
                        self.match(EParser.AND)
                        self.state = 1234
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1239
                localctx.typ = self.mutable_category_type()
                self.state = 1245
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 1240
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1243
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        self.state = 1241
                        self.match(EParser.AND)
                        self.state = 1242
                        localctx.arg = self.argument_assignment()




                pass


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
            if hasattr(listener, "enterWrite_statement"):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWrite_statement"):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = EParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1249
            self.match(EParser.WRITE)
            self.state = 1250
            localctx.what = self.expression(0)
            self.state = 1251
            self.match(EParser.TO)
            self.state = 1252
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
            if hasattr(listener, "enterAmbiguous_expression"):
                listener.enterAmbiguous_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAmbiguous_expression"):
                listener.exitAmbiguous_expression(self)




    def ambiguous_expression(self):

        localctx = EParser.Ambiguous_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1254
            localctx.method = self.unresolved_expression(0)
            self.state = 1255
            self.match(EParser.MINUS)
            self.state = 1256
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filtered_list_suffixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Filtered_list_suffixContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.predicate = None # ExpressionContext

        def FILTERED(self):
            return self.getToken(EParser.FILTERED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_filtered_list_suffix

        def enterRule(self, listener):
            if hasattr(listener, "enterFiltered_list_suffix"):
                listener.enterFiltered_list_suffix(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFiltered_list_suffix"):
                listener.exitFiltered_list_suffix(self)




    def filtered_list_suffix(self):

        localctx = EParser.Filtered_list_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_filtered_list_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1258
            self.match(EParser.FILTERED)
            self.state = 1259
            self.match(EParser.WITH)
            self.state = 1260
            localctx.name = self.variable_identifier()
            self.state = 1261
            self.match(EParser.WHERE)
            self.state = 1262
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
            super(EParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(EParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_store_expressionContext)
            super(EParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
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
            if hasattr(listener, "enterFetchOne"):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchOne"):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_store_expressionContext)
            super(EParser.FetchManyContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
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
        def ROWS(self):
            return self.getToken(EParser.ROWS, 0)
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
            if hasattr(listener, "enterFetchMany"):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchMany"):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = EParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                localctx = EParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1264
                self.match(EParser.FETCH)
                self.state = 1265
                self.match(EParser.ONE)

                self.state = 1267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE or _la==EParser.TYPE_IDENTIFIER:
                    self.state = 1266
                    localctx.typ = self.mutable_category_type()


                self.state = 1269
                self.match(EParser.WHERE)
                self.state = 1270
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1271
                self.match(EParser.FETCH)
                self.state = 1289
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [EParser.ALL]:
                    self.state = 1272
                    self.match(EParser.ALL)
                    self.state = 1274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                    if la_ == 1:
                        self.state = 1273
                        localctx.typ = self.mutable_category_type()


                    pass
                elif token in [EParser.MUTABLE, EParser.TYPE_IDENTIFIER]:
                    self.state = 1276
                    localctx.typ = self.mutable_category_type()
                    self.state = 1278
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==EParser.ROWS:
                        self.state = 1277
                        self.match(EParser.ROWS)


                    self.state = 1280
                    localctx.xstart = self.expression(0)
                    self.state = 1281
                    self.match(EParser.TO)
                    self.state = 1282
                    localctx.xstop = self.expression(0)
                    pass
                elif token in [EParser.ROWS]:
                    self.state = 1284
                    self.match(EParser.ROWS)
                    self.state = 1285
                    localctx.xstart = self.expression(0)
                    self.state = 1286
                    self.match(EParser.TO)
                    self.state = 1287
                    localctx.xstop = self.expression(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1293
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                if la_ == 1:
                    self.state = 1291
                    self.match(EParser.WHERE)
                    self.state = 1292
                    localctx.predicate = self.expression(0)


                self.state = 1298
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
                if la_ == 1:
                    self.state = 1295
                    self.match(EParser.ORDER)
                    self.state = 1296
                    self.match(EParser.BY)
                    self.state = 1297
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


        def DESC(self):
            return self.getToken(EParser.DESC, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def key_token(self):
            return self.getTypedRuleContext(EParser.Key_tokenContext,0)


        def getRuleIndex(self):
            return EParser.RULE_sorted_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterSorted_expression"):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSorted_expression"):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = EParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1302
            self.match(EParser.SORTED)
            self.state = 1304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.DESC:
                self.state = 1303
                self.match(EParser.DESC)


            self.state = 1306
            localctx.source = self.instance_expression(0)
            self.state = 1312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 1307
                self.match(EParser.WITH)
                self.state = 1308
                localctx.key = self.instance_expression(0)
                self.state = 1309
                self.match(EParser.AS)
                self.state = 1310
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
            if hasattr(listener, "enterArgumentAssignmentListExpression"):
                listener.enterArgumentAssignmentListExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListExpression"):
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
            if hasattr(listener, "enterArgumentAssignmentListNoExpression"):
                listener.enterArgumentAssignmentListNoExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListNoExpression"):
                listener.exitArgumentAssignmentListNoExpression(self)



    def argument_assignment_list(self):

        localctx = EParser.Argument_assignment_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_argument_assignment_list)
        try:
            self.state = 1328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1314
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1315
                localctx.exp = self.expression(0)
                self.state = 1321
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1316
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1319
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                    if la_ == 1:
                        self.state = 1317
                        self.match(EParser.AND)
                        self.state = 1318
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1323
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1326
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                if la_ == 1:
                    self.state = 1324
                    self.match(EParser.AND)
                    self.state = 1325
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
            if hasattr(listener, "enterArgumentAssignmentList"):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentList"):
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
            if hasattr(listener, "enterArgumentAssignmentListItem"):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListItem"):
                listener.exitArgumentAssignmentListItem(self)



    def with_argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.With_argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1331
            self.match(EParser.WITH)
            self.state = 1332
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1334
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1335
                    self.match(EParser.COMMA)
                    self.state = 1336
                    localctx.item = self.argument_assignment() 
                self.state = 1341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def AS(self):
            return self.getToken(EParser.AS, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_assignment"):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_assignment"):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = EParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.state = 1342
                localctx.exp = self.expression(0)
                self.state = 1343
                self.match(EParser.AS)


            self.state = 1347
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
            if hasattr(listener, "enterAssign_instance_statement"):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_instance_statement"):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = EParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1349
            localctx.inst = self.assignable_instance(0)
            self.state = 1350
            self.assign()
            self.state = 1351
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
            if hasattr(listener, "enterMemberInstance"):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberInstance"):
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
            if hasattr(listener, "enterItemInstance"):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemInstance"):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = EParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_child_instance)
        try:
            self.state = 1361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1353
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1354
                self.match(EParser.DOT)
                self.state = 1355
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1356
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1357
                self.match(EParser.LBRAK)
                self.state = 1358
                localctx.exp = self.expression(0)
                self.state = 1359
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
            if hasattr(listener, "enterAssign_tuple_statement"):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_tuple_statement"):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = EParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1363
            localctx.items = self.variable_identifier_list()
            self.state = 1364
            self.assign()
            self.state = 1365
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
            if hasattr(listener, "enterLfs"):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfs"):
                listener.exitLfs(self)




    def lfs(self):

        localctx = EParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1367
                    self.match(EParser.LF) 
                self.state = 1372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

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
            if hasattr(listener, "enterLfp"):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfp"):
                listener.exitLfp(self)




    def lfp(self):

        localctx = EParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1374 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1373
                self.match(EParser.LF)
                self.state = 1376 
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
            if hasattr(listener, "enterIndent"):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIndent"):
                listener.exitIndent(self)




    def indent(self):

        localctx = EParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1379 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1378
                self.match(EParser.LF)
                self.state = 1381 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1383
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
            if hasattr(listener, "enterDedent"):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDedent"):
                listener.exitDedent(self)




    def dedent(self):

        localctx = EParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1385
                self.match(EParser.LF)
                self.state = 1390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1391
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
            if hasattr(listener, "enterNull_literal"):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNull_literal"):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = EParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1393
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
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def EOF(self):
            return self.getToken(EParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(EParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFullDeclarationList"):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFullDeclarationList"):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = EParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.COMMENT or _la==EParser.DEFINE:
                self.state = 1395
                self.declarations()


            self.state = 1398
            self.lfs()
            self.state = 1399
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

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(EParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_declarations

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclarations"):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclarations"):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = EParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
            self.declaration()
            self.state = 1407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1402
                    self.lfp()
                    self.state = 1403
                    self.declaration() 
                self.state = 1409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = EParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMENT:
                self.state = 1410
                self.comment_statement()
                self.state = 1411
                self.lfp()
                self.state = 1417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.state = 1418
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1419
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1420
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1421
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1422
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

        def native_resource_declaration(self):
            return self.getTypedRuleContext(EParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterResource_declaration"):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResource_declaration"):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = EParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1425
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
            super(EParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_declaration"):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_declaration"):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = EParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_enum_declaration)
        try:
            self.state = 1429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1427
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1428
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
            super(EParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(EParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol_list"):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol_list"):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = EParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1431
            self.native_symbol()
            self.state = 1437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,92,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1432
                    self.lfp()
                    self.state = 1433
                    self.native_symbol() 
                self.state = 1439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,92,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(EParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol_list"):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol_list"):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = EParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1440
            self.category_symbol()
            self.state = 1446
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1441
                    self.lfp()
                    self.state = 1442
                    self.category_symbol() 
                self.state = 1448
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_list"):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_list"):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = EParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1449
            self.symbol_identifier()
            self.state = 1454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1450
                self.match(EParser.COMMA)
                self.state = 1451
                self.symbol_identifier()
                self.state = 1456
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
            if hasattr(listener, "enterMatchingSet"):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingSet"):
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
            if hasattr(listener, "enterMatchingPattern"):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingPattern"):
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
            if hasattr(listener, "enterMatchingList"):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingList"):
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
            if hasattr(listener, "enterMatchingRange"):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingRange"):
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
            if hasattr(listener, "enterMatchingExpression"):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingExpression"):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = EParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_attribute_constraint)
        try:
            self.state = 1467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1457
                self.match(EParser.IN)
                self.state = 1458
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1459
                self.match(EParser.IN)
                self.state = 1460
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1461
                self.match(EParser.IN)
                self.state = 1462
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1463
                self.match(EParser.MATCHING)
                self.state = 1464
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1465
                self.match(EParser.MATCHING)
                self.state = 1466
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

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterList_literal"):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList_literal"):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = EParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1469
                self.match(EParser.MUTABLE)


            self.state = 1472
            self.match(EParser.LBRAK)
            self.state = 1474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (EParser.EXECUTE - 99)) | (1 << (EParser.FETCH - 99)) | (1 << (EParser.INVOKE - 99)) | (1 << (EParser.MUTABLE - 99)) | (1 << (EParser.NOT - 99)) | (1 << (EParser.NOTHING - 99)) | (1 << (EParser.READ - 99)) | (1 << (EParser.SELF - 99)) | (1 << (EParser.SORTED - 99)) | (1 << (EParser.THIS - 99)) | (1 << (EParser.BOOLEAN_LITERAL - 99)) | (1 << (EParser.CHAR_LITERAL - 99)) | (1 << (EParser.MIN_INTEGER - 99)) | (1 << (EParser.MAX_INTEGER - 99)) | (1 << (EParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (EParser.TYPE_IDENTIFIER - 163)) | (1 << (EParser.VARIABLE_IDENTIFIER - 163)) | (1 << (EParser.TEXT_LITERAL - 163)) | (1 << (EParser.UUID_LITERAL - 163)) | (1 << (EParser.INTEGER_LITERAL - 163)) | (1 << (EParser.HEXA_LITERAL - 163)) | (1 << (EParser.DECIMAL_LITERAL - 163)) | (1 << (EParser.DATETIME_LITERAL - 163)) | (1 << (EParser.TIME_LITERAL - 163)) | (1 << (EParser.DATE_LITERAL - 163)) | (1 << (EParser.PERIOD_LITERAL - 163)) | (1 << (EParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1473
                self.expression_list()


            self.state = 1476
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

        def LT(self):
            return self.getToken(EParser.LT, 0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_set_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterSet_literal"):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSet_literal"):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = EParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1478
                self.match(EParser.MUTABLE)


            self.state = 1481
            self.match(EParser.LT)
            self.state = 1483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (EParser.EXECUTE - 99)) | (1 << (EParser.FETCH - 99)) | (1 << (EParser.INVOKE - 99)) | (1 << (EParser.MUTABLE - 99)) | (1 << (EParser.NOT - 99)) | (1 << (EParser.NOTHING - 99)) | (1 << (EParser.READ - 99)) | (1 << (EParser.SELF - 99)) | (1 << (EParser.SORTED - 99)) | (1 << (EParser.THIS - 99)) | (1 << (EParser.BOOLEAN_LITERAL - 99)) | (1 << (EParser.CHAR_LITERAL - 99)) | (1 << (EParser.MIN_INTEGER - 99)) | (1 << (EParser.MAX_INTEGER - 99)) | (1 << (EParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (EParser.TYPE_IDENTIFIER - 163)) | (1 << (EParser.VARIABLE_IDENTIFIER - 163)) | (1 << (EParser.TEXT_LITERAL - 163)) | (1 << (EParser.UUID_LITERAL - 163)) | (1 << (EParser.INTEGER_LITERAL - 163)) | (1 << (EParser.HEXA_LITERAL - 163)) | (1 << (EParser.DECIMAL_LITERAL - 163)) | (1 << (EParser.DATETIME_LITERAL - 163)) | (1 << (EParser.TIME_LITERAL - 163)) | (1 << (EParser.DATE_LITERAL - 163)) | (1 << (EParser.PERIOD_LITERAL - 163)) | (1 << (EParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1482
                self.expression_list()


            self.state = 1485
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

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_expression_list

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_list"):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_list"):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = EParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1487
            self.expression(0)
            self.state = 1492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1488
                self.match(EParser.COMMA)
                self.state = 1489
                self.expression(0)
                self.state = 1494
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
            if hasattr(listener, "enterRange_literal"):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_literal"):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = EParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1495
            self.match(EParser.LBRAK)
            self.state = 1496
            localctx.low = self.expression(0)
            self.state = 1497
            self.match(EParser.RANGE)
            self.state = 1498
            localctx.high = self.expression(0)
            self.state = 1499
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


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(EParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorType"):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorType"):
                listener.exitIteratorType(self)


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
            if hasattr(listener, "enterSetType"):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetType"):
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
            if hasattr(listener, "enterListType"):
                listener.enterListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitListType"):
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
            if hasattr(listener, "enterDictType"):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDictType"):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(EParser.CURSOR, 0)
        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCursorType"):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCursorType"):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(EParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPrimaryType"):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrimaryType"):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 164
        self.enterRecursionRule(localctx, 164, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1502
                localctx.p = self.primary_type()
                pass
            elif token in [EParser.CURSOR]:
                localctx = EParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1503
                self.match(EParser.CURSOR)
                self.state = 1504
                self.match(EParser.LT)
                self.state = 1505
                localctx.c = self.typedef(0)
                self.state = 1506
                self.match(EParser.GT)
                pass
            elif token in [EParser.ITERATOR]:
                localctx = EParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1508
                self.match(EParser.ITERATOR)
                self.state = 1509
                self.match(EParser.LT)
                self.state = 1510
                localctx.i = self.typedef(0)
                self.state = 1511
                self.match(EParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,103,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1523
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
                    if la_ == 1:
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1515
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1516
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1517
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1518
                        self.match(EParser.LBRAK)
                        self.state = 1519
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1520
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1521
                        self.match(EParser.LCURL)
                        self.state = 1522
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

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
            if hasattr(listener, "enterNativeType"):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeType"):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCategoryType"):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategoryType"):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = EParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_primary_type)
        try:
            self.state = 1530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1528
                localctx.n = self.native_type()
                pass
            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1529
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
            if hasattr(listener, "enterPeriodType"):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodType"):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanType"):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanType"):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDocumentType"):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocumentType"):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterType"):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterType"):
                listener.exitCharacterType(self)


    class VersionTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.VersionTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VERSION(self):
            return self.getToken(EParser.VERSION, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionType"):
                listener.enterVersionType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionType"):
                listener.exitVersionType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextType"):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextType"):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(EParser.IMAGE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterImageType"):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImageType"):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeType"):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeType"):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerType"):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerType"):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeType"):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeType"):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBlobType"):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlobType"):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDType"):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDType"):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalType"):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalType"):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCodeType"):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeType"):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateType"):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateType"):
                listener.exitDateType(self)



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_native_type)
        try:
            self.state = 1547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1532
                self.match(EParser.BOOLEAN)
                pass
            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1533
                self.match(EParser.CHARACTER)
                pass
            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1534
                self.match(EParser.TEXT)
                pass
            elif token in [EParser.IMAGE]:
                localctx = EParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1535
                self.match(EParser.IMAGE)
                pass
            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1536
                self.match(EParser.INTEGER)
                pass
            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1537
                self.match(EParser.DECIMAL)
                pass
            elif token in [EParser.DOCUMENT]:
                localctx = EParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1538
                self.match(EParser.DOCUMENT)
                pass
            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1539
                self.match(EParser.DATE)
                pass
            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1540
                self.match(EParser.DATETIME)
                pass
            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1541
                self.match(EParser.TIME)
                pass
            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1542
                self.match(EParser.PERIOD)
                pass
            elif token in [EParser.VERSION]:
                localctx = EParser.VersionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1543
                self.match(EParser.VERSION)
                pass
            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1544
                self.match(EParser.CODE)
                pass
            elif token in [EParser.BLOB]:
                localctx = EParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1545
                self.match(EParser.BLOB)
                pass
            elif token in [EParser.UUID]:
                localctx = EParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1546
                self.match(EParser.UUID)
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
            super(EParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_type"):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_type"):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = EParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1549
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
            if hasattr(listener, "enterMutable_category_type"):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMutable_category_type"):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = EParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1551
                self.match(EParser.MUTABLE)


            self.state = 1554
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
            if hasattr(listener, "enterCode_type"):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_type"):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = EParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1556
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
            if hasattr(listener, "enterConcreteCategoryDeclaration"):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteCategoryDeclaration"):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(EParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryDeclaration"):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryDeclaration"):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(EParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingletonCategoryDeclaration"):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingletonCategoryDeclaration"):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = EParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_category_declaration)
        try:
            self.state = 1561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1558
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1559
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1560
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

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier_list"):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier_list"):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = EParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1563
            self.type_identifier()
            self.state = 1568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1564
                self.match(EParser.COMMA)
                self.state = 1565
                self.type_identifier()
                self.state = 1570
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_method_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_identifier"):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_identifier"):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = EParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_method_identifier)
        try:
            self.state = 1573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1571
                self.variable_identifier()
                pass
            elif token in [EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1572
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
            super(EParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(EParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTypeIdentifier"):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTypeIdentifier"):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSymbolIdentifier"):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbolIdentifier"):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterVariableIdentifier"):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableIdentifier"):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = EParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_identifier)
        try:
            self.state = 1578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1575
                self.variable_identifier()
                pass
            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1576
                self.type_identifier()
                pass
            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1577
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
            super(EParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier"):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier"):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = EParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1580
            self.match(EParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def getRuleIndex(self):
            return EParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier"):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier"):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = EParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1582
            _la = self._input.LA(1)
            if not(_la==EParser.STORABLE or _la==EParser.VARIABLE_IDENTIFIER):
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
            super(EParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier"):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier"):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = EParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1584
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
            if hasattr(listener, "enterSymbol_identifier"):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_identifier"):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = EParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1586
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

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(EParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_argument_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_list"):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_list"):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = EParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1588
            self.argument()
            self.state = 1593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1589
                self.match(EParser.COMMA)
                self.state = 1590
                self.argument()
                self.state = 1595
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
            if hasattr(listener, "enterOperatorArgument"):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorArgument"):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(EParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeArgument"):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeArgument"):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = EParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1596
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1597
                    self.match(EParser.MUTABLE)


                self.state = 1600
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

        def named_argument(self):
            return self.getTypedRuleContext(EParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(EParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_operator_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_argument"):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_argument"):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = EParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_operator_argument)
        try:
            self.state = 1605
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1603
                self.named_argument()
                pass
            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ITERATOR, EParser.CURSOR, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1604
                self.typed_argument()
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

    class Named_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_named_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterNamed_argument"):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNamed_argument"):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = EParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1607
            self.variable_identifier()
            self.state = 1610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.EQ:
                self.state = 1608
                self.match(EParser.EQ)
                self.state = 1609
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
            if hasattr(listener, "enterCode_argument"):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_argument"):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = EParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1612
            self.code_type()
            self.state = 1613
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

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def getRuleIndex(self):
            return EParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_or_any_type"):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_or_any_type"):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = EParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_category_or_any_type)
        try:
            self.state = 1617
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ITERATOR, EParser.CURSOR, EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1615
                self.typedef(0)
                pass
            elif token in [EParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1616
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
            super(EParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(EParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyListType"):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyListType"):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyType"):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyType"):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyDictType"):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyDictType"):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 204
        self.enterRecursionRule(localctx, 204, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1620
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1628
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1622
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1623
                        self.match(EParser.LBRAK)
                        self.state = 1624
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1625
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1626
                        self.match(EParser.LCURL)
                        self.state = 1627
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

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

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(EParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration_list"):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration_list"):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = EParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633
            self.member_method_declaration()
            self.state = 1639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1634
                    self.lfp()
                    self.state = 1635
                    self.member_method_declaration() 
                self.state = 1641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

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
            if hasattr(listener, "enterMember_method_declaration"):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration"):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = EParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_member_method_declaration)
        try:
            self.state = 1647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1642
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1643
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1644
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1645
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1646
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

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration_list"):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration_list"):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = EParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1649
            self.native_member_method_declaration()
            self.state = 1655
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1650
                    self.lfp()
                    self.state = 1651
                    self.native_member_method_declaration() 
                self.state = 1657
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(EParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(EParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration"):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration"):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = EParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_native_member_method_declaration)
        try:
            self.state = 1661
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1658
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1659
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1660
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
            if hasattr(listener, "enterPython2CategoryBinding"):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2CategoryBinding"):
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
            if hasattr(listener, "enterPython3CategoryBinding"):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3CategoryBinding"):
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
            if hasattr(listener, "enterJavaCategoryBinding"):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCategoryBinding"):
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
            if hasattr(listener, "enterCSharpCategoryBinding"):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCategoryBinding"):
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
            if hasattr(listener, "enterJavaScriptCategoryBinding"):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptCategoryBinding"):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = EParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_native_category_binding)
        try:
            self.state = 1673
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1663
                self.match(EParser.JAVA)
                self.state = 1664
                localctx.binding = self.java_class_identifier_expression(0)
                pass
            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1665
                self.match(EParser.CSHARP)
                self.state = 1666
                localctx.binding = self.csharp_identifier_expression(0)
                pass
            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1667
                self.match(EParser.PYTHON2)
                self.state = 1668
                localctx.binding = self.python_category_binding()
                pass
            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1669
                self.match(EParser.PYTHON3)
                self.state = 1670
                localctx.binding = self.python_category_binding()
                pass
            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1671
                self.match(EParser.JAVASCRIPT)
                self.state = 1672
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
            super(EParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_category_binding"):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_category_binding"):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = EParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1675
            self.identifier()
            self.state = 1677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                self.state = 1676
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
            if hasattr(listener, "enterPython_module"):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_module"):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = EParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1679
            self.match(EParser.FROM)
            self.state = 1680
            self.module_token()
            self.state = 1681
            self.match(EParser.COLON)
            self.state = 1682
            self.identifier()
            self.state = 1687
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1683
                    self.match(EParser.DOT)
                    self.state = 1684
                    self.identifier() 
                self.state = 1689
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

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

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_category_binding"):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_category_binding"):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = EParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1690
            self.identifier()
            self.state = 1692
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
            if la_ == 1:
                self.state = 1691
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
            if hasattr(listener, "enterJavascript_module"):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_module"):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = EParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1694
            self.match(EParser.FROM)
            self.state = 1695
            self.module_token()
            self.state = 1696
            self.match(EParser.COLON)
            self.state = 1698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1697
                self.match(EParser.SLASH)


            self.state = 1700
            self.javascript_identifier()
            self.state = 1705
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1701
                    self.match(EParser.SLASH)
                    self.state = 1702
                    self.javascript_identifier() 
                self.state = 1707
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

            self.state = 1710
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                self.state = 1708
                self.match(EParser.DOT)
                self.state = 1709
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

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier_list"):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier_list"):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = EParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1712
            self.variable_identifier()
            self.state = 1717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1713
                self.match(EParser.COMMA)
                self.state = 1714
                self.variable_identifier()
                self.state = 1719
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
            super(EParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier_list"):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier_list"):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = EParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_attribute_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720
            self.attribute_identifier()
            self.state = 1725
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,131,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1721
                    self.match(EParser.COMMA)
                    self.state = 1722
                    self.attribute_identifier() 
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

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(EParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_declaration"):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_declaration"):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = EParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_method_declaration)
        try:
            self.state = 1732
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,132,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1728
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1729
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1730
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1731
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
            super(EParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(EParser.COMMENT, 0)

        def getRuleIndex(self):
            return EParser.RULE_comment_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterComment_statement"):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComment_statement"):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = EParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1734
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

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_statement_list"):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_statement_list"):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = EParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1736
            self.native_statement()
            self.state = 1742
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1737
                    self.lfp()
                    self.state = 1738
                    self.native_statement() 
                self.state = 1744
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(EParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpNativeStatement"):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpNativeStatement"):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(EParser.Java_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaNativeStatement"):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaNativeStatement"):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptNativeStatement"):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptNativeStatement"):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2NativeStatement"):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2NativeStatement"):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3NativeStatement"):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3NativeStatement"):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = EParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_native_statement)
        try:
            self.state = 1755
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1745
                self.match(EParser.JAVA)
                self.state = 1746
                self.java_statement()
                pass
            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1747
                self.match(EParser.CSHARP)
                self.state = 1748
                self.csharp_statement()
                pass
            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1749
                self.match(EParser.PYTHON2)
                self.state = 1750
                self.python_native_statement()
                pass
            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1751
                self.match(EParser.PYTHON3)
                self.state = 1752
                self.python_native_statement()
                pass
            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1753
                self.match(EParser.JAVASCRIPT)
                self.state = 1754
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
            super(EParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(EParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_native_statement"):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_native_statement"):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = EParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1757
            self.python_statement()
            self.state = 1759
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.SEMI:
                self.state = 1758
                self.match(EParser.SEMI)


            self.state = 1762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.FROM:
                self.state = 1761
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
            super(EParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_native_statement"):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_native_statement"):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = EParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1764
            self.javascript_statement()
            self.state = 1766
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.SEMI:
                self.state = 1765
                self.match(EParser.SEMI)


            self.state = 1769
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.FROM:
                self.state = 1768
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
            super(EParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.StatementContext)
            else:
                return self.getTypedRuleContext(EParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterStatement_list"):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStatement_list"):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = EParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1771
            self.statement()
            self.state = 1777
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1772
                    self.lfp()
                    self.state = 1773
                    self.statement() 
                self.state = 1779
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.AssertionContext)
            else:
                return self.getTypedRuleContext(EParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_assertion_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion_list"):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion_list"):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = EParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1780
            self.assertion()
            self.state = 1786
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1781
                    self.lfp()
                    self.state = 1782
                    self.assertion() 
                self.state = 1788
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_case_statement_list"):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_case_statement_list"):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = EParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1789
            self.switch_case_statement()
            self.state = 1795
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1790
                    self.lfp()
                    self.state = 1791
                    self.switch_case_statement() 
                self.state = 1797
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,141,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCatch_statement_list"):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatch_statement_list"):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = EParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1798
            self.catch_statement()
            self.state = 1804
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,142,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1799
                    self.lfp()
                    self.state = 1800
                    self.catch_statement() 
                self.state = 1806
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,142,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralListLiteral"):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralListLiteral"):
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
            if hasattr(listener, "enterLiteralRangeLiteral"):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralRangeLiteral"):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralSetLiteral"):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralSetLiteral"):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = EParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_literal_collection)
        try:
            self.state = 1821
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1807
                self.match(EParser.LBRAK)
                self.state = 1808
                localctx.low = self.atomic_literal()
                self.state = 1809
                self.match(EParser.RANGE)
                self.state = 1810
                localctx.high = self.atomic_literal()
                self.state = 1811
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1813
                self.match(EParser.LBRAK)
                self.state = 1814
                self.literal_list_literal()
                self.state = 1815
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1817
                self.match(EParser.LT)
                self.state = 1818
                self.literal_list_literal()
                self.state = 1819
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
            if hasattr(listener, "enterMinIntegerLiteral"):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinIntegerLiteral"):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(EParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateLiteral"):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateLiteral"):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanLiteral"):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanLiteral"):
                listener.exitBooleanLiteral(self)


    class VersionLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.VersionLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def VERSION_LITERAL(self):
            return self.getToken(EParser.VERSION_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionLiteral"):
                listener.enterVersionLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionLiteral"):
                listener.exitVersionLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(EParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHexadecimalLiteral"):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHexadecimalLiteral"):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(EParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDLiteral"):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDLiteral"):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(EParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMaxIntegerLiteral"):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMaxIntegerLiteral"):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(EParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeLiteral"):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeLiteral"):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(EParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodLiteral"):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodLiteral"):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalLiteral"):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalLiteral"):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextLiteral"):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextLiteral"):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(EParser.Null_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNullLiteral"):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNullLiteral"):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerLiteral"):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerLiteral"):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(EParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeLiteral"):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeLiteral"):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterLiteral"):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterLiteral"):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = EParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_atomic_literal)
        try:
            self.state = 1838
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1823
                localctx.t = self.match(EParser.MIN_INTEGER)
                pass
            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1824
                localctx.t = self.match(EParser.MAX_INTEGER)
                pass
            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1825
                localctx.t = self.match(EParser.INTEGER_LITERAL)
                pass
            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1826
                localctx.t = self.match(EParser.HEXA_LITERAL)
                pass
            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1827
                localctx.t = self.match(EParser.CHAR_LITERAL)
                pass
            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1828
                localctx.t = self.match(EParser.DATE_LITERAL)
                pass
            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1829
                localctx.t = self.match(EParser.TIME_LITERAL)
                pass
            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1830
                localctx.t = self.match(EParser.TEXT_LITERAL)
                pass
            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1831
                localctx.t = self.match(EParser.DECIMAL_LITERAL)
                pass
            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1832
                localctx.t = self.match(EParser.DATETIME_LITERAL)
                pass
            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1833
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)
                pass
            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1834
                localctx.t = self.match(EParser.PERIOD_LITERAL)
                pass
            elif token in [EParser.VERSION_LITERAL]:
                localctx = EParser.VersionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1835
                localctx.t = self.match(EParser.VERSION_LITERAL)
                pass
            elif token in [EParser.UUID_LITERAL]:
                localctx = EParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1836
                localctx.t = self.match(EParser.UUID_LITERAL)
                pass
            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1837
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
            super(EParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(EParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_list_literal"):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_list_literal"):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = EParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1840
            self.atomic_literal()
            self.state = 1845
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1841
                self.match(EParser.COMMA)
                self.state = 1842
                self.atomic_literal()
                self.state = 1847
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
            if hasattr(listener, "enterThisExpression"):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThisExpression"):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesisExpression"):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesisExpression"):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralExpression"):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralExpression"):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifierExpression"):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifierExpression"):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = EParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_selectable_expression)
        try:
            self.state = 1852
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1848
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1849
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1850
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1851
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
            if hasattr(listener, "enterThis_expression"):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThis_expression"):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = EParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1854
            _la = self._input.LA(1)
            if not(_la==EParser.SELF or _la==EParser.THIS):
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
            super(EParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def getRuleIndex(self):
            return EParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesis_expression"):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesis_expression"):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = EParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1856
            self.match(EParser.LPAR)
            self.state = 1857
            self.expression(0)
            self.state = 1858
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

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(EParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return EParser.RULE_literal_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_expression"):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_expression"):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = EParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_literal_expression)
        try:
            self.state = 1862
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.UUID_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL, EParser.VERSION_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1860
                self.atomic_literal()
                pass
            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT, EParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1861
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
            super(EParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(EParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(EParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return EParser.RULE_collection_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterCollection_literal"):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollection_literal"):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = EParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_collection_literal)
        try:
            self.state = 1869
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1864
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1865
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1866
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1867
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1868
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
            super(EParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(EParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_tuple_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterTuple_literal"):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTuple_literal"):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = EParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1872
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1871
                self.match(EParser.MUTABLE)


            self.state = 1874
            self.match(EParser.LPAR)
            self.state = 1876
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (EParser.EXECUTE - 99)) | (1 << (EParser.FETCH - 99)) | (1 << (EParser.INVOKE - 99)) | (1 << (EParser.MUTABLE - 99)) | (1 << (EParser.NOT - 99)) | (1 << (EParser.NOTHING - 99)) | (1 << (EParser.READ - 99)) | (1 << (EParser.SELF - 99)) | (1 << (EParser.SORTED - 99)) | (1 << (EParser.THIS - 99)) | (1 << (EParser.BOOLEAN_LITERAL - 99)) | (1 << (EParser.CHAR_LITERAL - 99)) | (1 << (EParser.MIN_INTEGER - 99)) | (1 << (EParser.MAX_INTEGER - 99)) | (1 << (EParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (EParser.TYPE_IDENTIFIER - 163)) | (1 << (EParser.VARIABLE_IDENTIFIER - 163)) | (1 << (EParser.TEXT_LITERAL - 163)) | (1 << (EParser.UUID_LITERAL - 163)) | (1 << (EParser.INTEGER_LITERAL - 163)) | (1 << (EParser.HEXA_LITERAL - 163)) | (1 << (EParser.DECIMAL_LITERAL - 163)) | (1 << (EParser.DATETIME_LITERAL - 163)) | (1 << (EParser.TIME_LITERAL - 163)) | (1 << (EParser.DATE_LITERAL - 163)) | (1 << (EParser.PERIOD_LITERAL - 163)) | (1 << (EParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1875
                self.expression_tuple()


            self.state = 1878
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

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(EParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_dict_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_literal"):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_literal"):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = EParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1881
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1880
                self.match(EParser.MUTABLE)


            self.state = 1883
            self.match(EParser.LCURL)
            self.state = 1885
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (EParser.EXECUTE - 99)) | (1 << (EParser.FETCH - 99)) | (1 << (EParser.INVOKE - 99)) | (1 << (EParser.MUTABLE - 99)) | (1 << (EParser.NOT - 99)) | (1 << (EParser.NOTHING - 99)) | (1 << (EParser.READ - 99)) | (1 << (EParser.SELF - 99)) | (1 << (EParser.SORTED - 99)) | (1 << (EParser.THIS - 99)) | (1 << (EParser.BOOLEAN_LITERAL - 99)) | (1 << (EParser.CHAR_LITERAL - 99)) | (1 << (EParser.MIN_INTEGER - 99)) | (1 << (EParser.MAX_INTEGER - 99)) | (1 << (EParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (EParser.TYPE_IDENTIFIER - 163)) | (1 << (EParser.VARIABLE_IDENTIFIER - 163)) | (1 << (EParser.TEXT_LITERAL - 163)) | (1 << (EParser.UUID_LITERAL - 163)) | (1 << (EParser.INTEGER_LITERAL - 163)) | (1 << (EParser.HEXA_LITERAL - 163)) | (1 << (EParser.DECIMAL_LITERAL - 163)) | (1 << (EParser.DATETIME_LITERAL - 163)) | (1 << (EParser.TIME_LITERAL - 163)) | (1 << (EParser.DATE_LITERAL - 163)) | (1 << (EParser.PERIOD_LITERAL - 163)) | (1 << (EParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1884
                self.dict_entry_list()


            self.state = 1887
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

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_expression_tuple

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_tuple"):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_tuple"):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = EParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1889
            self.expression(0)
            self.state = 1890
            self.match(EParser.COMMA)
            self.state = 1899
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (EParser.EXECUTE - 99)) | (1 << (EParser.FETCH - 99)) | (1 << (EParser.INVOKE - 99)) | (1 << (EParser.MUTABLE - 99)) | (1 << (EParser.NOT - 99)) | (1 << (EParser.NOTHING - 99)) | (1 << (EParser.READ - 99)) | (1 << (EParser.SELF - 99)) | (1 << (EParser.SORTED - 99)) | (1 << (EParser.THIS - 99)) | (1 << (EParser.BOOLEAN_LITERAL - 99)) | (1 << (EParser.CHAR_LITERAL - 99)) | (1 << (EParser.MIN_INTEGER - 99)) | (1 << (EParser.MAX_INTEGER - 99)) | (1 << (EParser.SYMBOL_IDENTIFIER - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (EParser.TYPE_IDENTIFIER - 163)) | (1 << (EParser.VARIABLE_IDENTIFIER - 163)) | (1 << (EParser.TEXT_LITERAL - 163)) | (1 << (EParser.UUID_LITERAL - 163)) | (1 << (EParser.INTEGER_LITERAL - 163)) | (1 << (EParser.HEXA_LITERAL - 163)) | (1 << (EParser.DECIMAL_LITERAL - 163)) | (1 << (EParser.DATETIME_LITERAL - 163)) | (1 << (EParser.TIME_LITERAL - 163)) | (1 << (EParser.DATE_LITERAL - 163)) | (1 << (EParser.PERIOD_LITERAL - 163)) | (1 << (EParser.VERSION_LITERAL - 163)))) != 0):
                self.state = 1891
                self.expression(0)
                self.state = 1896
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==EParser.COMMA:
                    self.state = 1892
                    self.match(EParser.COMMA)
                    self.state = 1893
                    self.expression(0)
                    self.state = 1898
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
            super(EParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(EParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry_list"):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry_list"):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = EParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1901
            self.dict_entry()
            self.state = 1906
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1902
                self.match(EParser.COMMA)
                self.state = 1903
                self.dict_entry()
                self.state = 1908
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
            if hasattr(listener, "enterDict_entry"):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry"):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = EParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1909
            localctx.key = self.expression(0)
            self.state = 1910
            self.match(EParser.COLON)
            self.state = 1911
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
            if hasattr(listener, "enterSliceFirstAndLast"):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstAndLast"):
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
            if hasattr(listener, "enterSliceLastOnly"):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceLastOnly"):
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
            if hasattr(listener, "enterSliceFirstOnly"):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstOnly"):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = EParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_slice_arguments)
        try:
            self.state = 1922
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,156,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1913
                localctx.first = self.expression(0)
                self.state = 1914
                self.match(EParser.COLON)
                self.state = 1915
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1917
                localctx.first = self.expression(0)
                self.state = 1918
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1920
                self.match(EParser.COLON)
                self.state = 1921
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

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_variable_statement"):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_variable_statement"):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = EParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1924
            self.variable_identifier()
            self.state = 1925
            self.assign()
            self.state = 1926
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
            super(EParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(EParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(EParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterChildInstance"):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitChildInstance"):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRootInstance"):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRootInstance"):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 278
        self.enterRecursionRule(localctx, 278, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1929
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1935
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1931
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1932
                    self.child_instance() 
                self.state = 1937
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsATypeExpression"):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsATypeExpression"):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsOtherExpression"):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsOtherExpression"):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = EParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_is_expression)
        try:
            self.state = 1942
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,158,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1938
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1939
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1940
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1941
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
            super(EParser.Read_all_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def ALL(self):
            return self.getToken(EParser.ALL, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_all_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_all_expression"):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_all_expression"):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = EParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1944
            self.match(EParser.READ)
            self.state = 1945
            self.match(EParser.ALL)
            self.state = 1946
            self.match(EParser.FROM)
            self.state = 1947
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
            super(EParser.Read_one_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def ONE(self):
            return self.getToken(EParser.ONE, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_one_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_one_expression"):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_one_expression"):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = EParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1949
            self.match(EParser.READ)
            self.state = 1950
            self.match(EParser.ONE)
            self.state = 1951
            self.match(EParser.FROM)
            self.state = 1952
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
            if hasattr(listener, "enterOrder_by_list"):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by_list"):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = EParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1954
            self.order_by()
            self.state = 1959
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,159,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1955
                    self.match(EParser.COMMA)
                    self.state = 1956
                    self.order_by() 
                self.state = 1961
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,159,self._ctx)

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
            if hasattr(listener, "enterOrder_by"):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by"):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = EParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1962
            self.variable_identifier()
            self.state = 1967
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1963
                    self.match(EParser.DOT)
                    self.state = 1964
                    self.variable_identifier() 
                self.state = 1969
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

            self.state = 1971
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                self.state = 1970
                _la = self._input.LA(1)
                if not(_la==EParser.ASC or _la==EParser.DESC):
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
            if hasattr(listener, "enterOperatorPlus"):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorPlus"):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorDivide"):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorDivide"):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorIDivide"):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorIDivide"):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMultiply"):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMultiply"):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMinus"):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMinus"):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorModulo"):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorModulo"):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = EParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_operator)
        try:
            self.state = 1979
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1973
                self.match(EParser.PLUS)
                pass
            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1974
                self.match(EParser.MINUS)
                pass
            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1975
                self.multiply()
                pass
            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1976
                self.divide()
                pass
            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1977
                self.idivide()
                pass
            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1978
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
            super(EParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_new_token

        def enterRule(self, listener):
            if hasattr(listener, "enterNew_token"):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNew_token"):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = EParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1981
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1982
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
            if hasattr(listener, "enterKey_token"):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey_token"):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = EParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1984
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1985
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
            super(EParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_module_token

        def enterRule(self, listener):
            if hasattr(listener, "enterModule_token"):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModule_token"):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = EParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1987
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1988
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
            super(EParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_value_token

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_token"):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_token"):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = EParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1990
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1991
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
            if hasattr(listener, "enterSymbols_token"):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbols_token"):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = EParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1993
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1994
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
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)




    def assign(self):

        localctx = EParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1996
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
            if hasattr(listener, "enterMultiply"):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiply"):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = EParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1998
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
            if hasattr(listener, "enterDivide"):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivide"):
                listener.exitDivide(self)




    def divide(self):

        localctx = EParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2000
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
            if hasattr(listener, "enterIdivide"):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdivide"):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = EParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2002
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
            if hasattr(listener, "enterModulo"):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModulo"):
                listener.exitModulo(self)




    def modulo(self):

        localctx = EParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2004
            _la = self._input.LA(1)
            if not(_la==EParser.PERCENT or _la==EParser.MODULO):
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
            if hasattr(listener, "enterJavascriptStatement"):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptStatement"):
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
            if hasattr(listener, "enterJavascriptReturnStatement"):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptReturnStatement"):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = EParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_javascript_statement)
        try:
            self.state = 2013
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2006
                self.match(EParser.RETURN)
                self.state = 2007
                localctx.exp = self.javascript_expression(0)
                self.state = 2008
                self.match(EParser.SEMI)
                pass
            elif token in [EParser.LPAR, EParser.LBRAK, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.UUID, EParser.NONE, EParser.NULL, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2010
                localctx.exp = self.javascript_expression(0)
                self.state = 2011
                self.match(EParser.SEMI)
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
            if hasattr(listener, "enterJavascriptSelectorExpression"):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptSelectorExpression"):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptPrimaryExpression"):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptPrimaryExpression"):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 314
        self.enterRecursionRule(localctx, 314, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2016
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2022
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,164,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 2018
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2019
                    localctx.child = self.javascript_selector_expression() 
                self.state = 2024
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,164,self._ctx)

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
            if hasattr(listener, "enterJavascript_primary_expression"):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_primary_expression"):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = EParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_primary_expression)
        try:
            self.state = 2032
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2025
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2026
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2027
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2028
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2029
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2030
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2031
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
            if hasattr(listener, "enterJavascript_this_expression"):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_this_expression"):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = EParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2034
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
            if hasattr(listener, "enterJavascript_new_expression"):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_new_expression"):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = EParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2036
            self.new_token()
            self.state = 2037
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
            if hasattr(listener, "enterJavaScriptMemberExpression"):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMemberExpression"):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptItemExpression"):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptItemExpression"):
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
            if hasattr(listener, "enterJavaScriptMethodExpression"):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMethodExpression"):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = EParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_selector_expression)
        try:
            self.state = 2044
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,166,self._ctx)
            if la_ == 1:
                localctx = EParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2039
                self.match(EParser.DOT)
                self.state = 2040
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = EParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2041
                self.match(EParser.DOT)
                self.state = 2042
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = EParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2043
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
            if hasattr(listener, "enterJavascript_method_expression"):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_method_expression"):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = EParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2046
            localctx.name = self.javascript_identifier()
            self.state = 2047
            self.match(EParser.LPAR)
            self.state = 2049
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (EParser.LPAR - 20)) | (1 << (EParser.LBRAK - 20)) | (1 << (EParser.BOOLEAN - 20)) | (1 << (EParser.CHARACTER - 20)) | (1 << (EParser.TEXT - 20)) | (1 << (EParser.INTEGER - 20)) | (1 << (EParser.DECIMAL - 20)) | (1 << (EParser.DATE - 20)) | (1 << (EParser.TIME - 20)) | (1 << (EParser.DATETIME - 20)) | (1 << (EParser.PERIOD - 20)) | (1 << (EParser.VERSION - 20)) | (1 << (EParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.THIS - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.BOOLEAN_LITERAL - 121)) | (1 << (EParser.CHAR_LITERAL - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)) | (1 << (EParser.DOLLAR_IDENTIFIER - 121)) | (1 << (EParser.TEXT_LITERAL - 121)) | (1 << (EParser.INTEGER_LITERAL - 121)) | (1 << (EParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2048
                localctx.args = self.javascript_arguments(0)


            self.state = 2051
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
            if hasattr(listener, "enterJavascriptArgumentList"):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentList"):
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
            if hasattr(listener, "enterJavascriptArgumentListItem"):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentListItem"):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2054
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2061
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,168,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 2056
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2057
                    self.match(EParser.COMMA)
                    self.state = 2058
                    localctx.item = self.javascript_expression(0) 
                self.state = 2063
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

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
            if hasattr(listener, "enterJavascript_item_expression"):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_item_expression"):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = EParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2064
            self.match(EParser.LBRAK)
            self.state = 2065
            localctx.exp = self.javascript_expression(0)
            self.state = 2066
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
            if hasattr(listener, "enterJavascript_parenthesis_expression"):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_parenthesis_expression"):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = EParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2068
            self.match(EParser.LPAR)
            self.state = 2069
            localctx.exp = self.javascript_expression(0)
            self.state = 2070
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
            if hasattr(listener, "enterJavascript_identifier_expression"):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier_expression"):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = EParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2072
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
            if hasattr(listener, "enterJavascriptIntegerLiteral"):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptIntegerLiteral"):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptBooleanLiteral"):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptBooleanLiteral"):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptCharacterLiteral"):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptCharacterLiteral"):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptTextLiteral"):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptTextLiteral"):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptDecimalLiteral"):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptDecimalLiteral"):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = EParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_literal_expression)
        try:
            self.state = 2079
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2074
                localctx.t = self.match(EParser.INTEGER_LITERAL)
                pass
            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2075
                localctx.t = self.match(EParser.DECIMAL_LITERAL)
                pass
            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2076
                localctx.t = self.match(EParser.TEXT_LITERAL)
                pass
            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2077
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)
                pass
            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2078
                localctx.t = self.match(EParser.CHAR_LITERAL)
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

        def VERSION(self):
            return self.getToken(EParser.VERSION, 0)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def NONE(self):
            return self.getToken(EParser.NONE, 0)

        def NULL(self):
            return self.getToken(EParser.NULL, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier"):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier"):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = EParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2081
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (EParser.BOOLEAN - 50)) | (1 << (EParser.CHARACTER - 50)) | (1 << (EParser.TEXT - 50)) | (1 << (EParser.INTEGER - 50)) | (1 << (EParser.DECIMAL - 50)) | (1 << (EParser.DATE - 50)) | (1 << (EParser.TIME - 50)) | (1 << (EParser.DATETIME - 50)) | (1 << (EParser.PERIOD - 50)) | (1 << (EParser.VERSION - 50)) | (1 << (EParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)) | (1 << (EParser.DOLLAR_IDENTIFIER - 121)))) != 0)):
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
            if hasattr(listener, "enterPythonStatement"):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonStatement"):
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
            if hasattr(listener, "enterPythonReturnStatement"):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonReturnStatement"):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = EParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_python_statement)
        try:
            self.state = 2086
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2083
                self.match(EParser.RETURN)
                self.state = 2084
                localctx.exp = self.python_expression(0)
                pass
            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.UUID, EParser.NONE, EParser.NULL, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2085
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
            if hasattr(listener, "enterPythonSelectorExpression"):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelectorExpression"):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(EParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPrimaryExpression"):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPrimaryExpression"):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 340
        self.enterRecursionRule(localctx, 340, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2089
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2095
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2091
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2092
                    localctx.child = self.python_selector_expression() 
                self.state = 2097
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

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
            if hasattr(listener, "enterPythonParenthesisExpression"):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonParenthesisExpression"):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifierExpression"):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifierExpression"):
                listener.exitPythonIdentifierExpression(self)


    class PythonSelfExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonSelfExpressionContext, self).__init__(parser)
            self.exp = None # Python_self_expressionContext
            self.copyFrom(ctx)

        def python_self_expression(self):
            return self.getTypedRuleContext(EParser.Python_self_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelfExpression"):
                listener.enterPythonSelfExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelfExpression"):
                listener.exitPythonSelfExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(EParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonLiteralExpression"):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonLiteralExpression"):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonGlobalMethodExpression"):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonGlobalMethodExpression"):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = EParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_primary_expression)
        try:
            self.state = 2103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,172,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonSelfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2098
                localctx.exp = self.python_self_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2099
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 3:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2100
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 4:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2101
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 5:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2102
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
            super(EParser.Python_self_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_self_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_self_expression"):
                listener.enterPython_self_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_self_expression"):
                listener.exitPython_self_expression(self)




    def python_self_expression(self):

        localctx = EParser.Python_self_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_self_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2105
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
            if hasattr(listener, "enterPythonMethodExpression"):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonMethodExpression"):
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
            if hasattr(listener, "enterPythonItemExpression"):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonItemExpression"):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = EParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_python_selector_expression)
        try:
            self.state = 2113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2107
                self.match(EParser.DOT)
                self.state = 2108
                localctx.exp = self.python_method_expression()
                pass
            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2109
                self.match(EParser.LBRAK)
                self.state = 2110
                localctx.exp = self.python_expression(0)
                self.state = 2111
                self.match(EParser.RBRAK)
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
            if hasattr(listener, "enterPython_method_expression"):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_method_expression"):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = EParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2115
            localctx.name = self.python_identifier()
            self.state = 2116
            self.match(EParser.LPAR)
            self.state = 2118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (EParser.LPAR - 20)) | (1 << (EParser.BOOLEAN - 20)) | (1 << (EParser.CHARACTER - 20)) | (1 << (EParser.TEXT - 20)) | (1 << (EParser.INTEGER - 20)) | (1 << (EParser.DECIMAL - 20)) | (1 << (EParser.DATE - 20)) | (1 << (EParser.TIME - 20)) | (1 << (EParser.DATETIME - 20)) | (1 << (EParser.PERIOD - 20)) | (1 << (EParser.VERSION - 20)) | (1 << (EParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.THIS - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.BOOLEAN_LITERAL - 121)) | (1 << (EParser.CHAR_LITERAL - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)) | (1 << (EParser.DOLLAR_IDENTIFIER - 121)) | (1 << (EParser.TEXT_LITERAL - 121)) | (1 << (EParser.INTEGER_LITERAL - 121)) | (1 << (EParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2117
                localctx.args = self.python_argument_list()


            self.state = 2120
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
            if hasattr(listener, "enterPythonOrdinalOnlyArgumentList"):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalOnlyArgumentList"):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedOnlyArgumentList"):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedOnlyArgumentList"):
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
            if hasattr(listener, "enterPythonArgumentList"):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonArgumentList"):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = EParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_python_argument_list)
        try:
            self.state = 2128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,175,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2122
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2123
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2124
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2125
                self.match(EParser.COMMA)
                self.state = 2126
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
            if hasattr(listener, "enterPythonOrdinalArgumentList"):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentList"):
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
            if hasattr(listener, "enterPythonOrdinalArgumentListItem"):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentListItem"):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2131
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,176,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2133
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2134
                    self.match(EParser.COMMA)
                    self.state = 2135
                    localctx.item = self.python_expression(0) 
                self.state = 2140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,176,self._ctx)

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
            if hasattr(listener, "enterPythonNamedArgumentList"):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentList"):
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
            if hasattr(listener, "enterPythonNamedArgumentListItem"):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentListItem"):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 354
        self.enterRecursionRule(localctx, 354, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2142
            localctx.name = self.python_identifier()
            self.state = 2143
            self.match(EParser.EQ)
            self.state = 2144
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2146
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2147
                    self.match(EParser.COMMA)
                    self.state = 2148
                    localctx.name = self.python_identifier()
                    self.state = 2149
                    self.match(EParser.EQ)
                    self.state = 2150
                    localctx.exp = self.python_expression(0) 
                self.state = 2156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

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
            if hasattr(listener, "enterPython_parenthesis_expression"):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_parenthesis_expression"):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = EParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2157
            self.match(EParser.LPAR)
            self.state = 2158
            localctx.exp = self.python_expression(0)
            self.state = 2159
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
            if hasattr(listener, "enterPythonChildIdentifier"):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonChildIdentifier"):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPromptoIdentifier"):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPromptoIdentifier"):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifier"):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifier"):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2162
                self.match(EParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.UUID, EParser.NONE, EParser.NULL, EParser.READ, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2163
                localctx.name = self.python_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,179,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2166
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2167
                    self.match(EParser.DOT)
                    self.state = 2168
                    localctx.name = self.python_identifier() 
                self.state = 2173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,179,self._ctx)

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
            if hasattr(listener, "enterPythonIntegerLiteral"):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIntegerLiteral"):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonBooleanLiteral"):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonBooleanLiteral"):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonCharacterLiteral"):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonCharacterLiteral"):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonTextLiteral"):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonTextLiteral"):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonDecimalLiteral"):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonDecimalLiteral"):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = EParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_python_literal_expression)
        try:
            self.state = 2179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2174
                localctx.t = self.match(EParser.INTEGER_LITERAL)
                pass
            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2175
                localctx.t = self.match(EParser.DECIMAL_LITERAL)
                pass
            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2176
                localctx.t = self.match(EParser.TEXT_LITERAL)
                pass
            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2177
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)
                pass
            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2178
                localctx.t = self.match(EParser.CHAR_LITERAL)
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

        def VERSION(self):
            return self.getToken(EParser.VERSION, 0)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

        def NONE(self):
            return self.getToken(EParser.NONE, 0)

        def NULL(self):
            return self.getToken(EParser.NULL, 0)

        def getRuleIndex(self):
            return EParser.RULE_python_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_identifier"):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_identifier"):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = EParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2181
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (EParser.BOOLEAN - 50)) | (1 << (EParser.CHARACTER - 50)) | (1 << (EParser.TEXT - 50)) | (1 << (EParser.INTEGER - 50)) | (1 << (EParser.DECIMAL - 50)) | (1 << (EParser.DATE - 50)) | (1 << (EParser.TIME - 50)) | (1 << (EParser.DATETIME - 50)) | (1 << (EParser.PERIOD - 50)) | (1 << (EParser.VERSION - 50)) | (1 << (EParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.THIS - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)))) != 0)):
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
            if hasattr(listener, "enterJavaReturnStatement"):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaReturnStatement"):
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
            if hasattr(listener, "enterJavaStatement"):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaStatement"):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = EParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_java_statement)
        try:
            self.state = 2190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2183
                self.match(EParser.RETURN)
                self.state = 2184
                localctx.exp = self.java_expression(0)
                self.state = 2185
                self.match(EParser.SEMI)
                pass
            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.UUID, EParser.NONE, EParser.NULL, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2187
                localctx.exp = self.java_expression(0)
                self.state = 2188
                self.match(EParser.SEMI)
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
            if hasattr(listener, "enterJavaSelectorExpression"):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaSelectorExpression"):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(EParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaPrimaryExpression"):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaPrimaryExpression"):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 366
        self.enterRecursionRule(localctx, 366, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2193
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,182,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2195
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2196
                    localctx.child = self.java_selector_expression() 
                self.state = 2201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,182,self._ctx)

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
            if hasattr(listener, "enterJava_primary_expression"):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_primary_expression"):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = EParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_primary_expression)
        try:
            self.state = 2207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,183,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2202
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2203
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2204
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2205
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2206
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
            if hasattr(listener, "enterJava_this_expression"):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_this_expression"):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = EParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2209
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
            if hasattr(listener, "enterJava_new_expression"):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_new_expression"):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = EParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2211
            self.new_token()
            self.state = 2212
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
            if hasattr(listener, "enterJavaItemExpression"):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaItemExpression"):
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
            if hasattr(listener, "enterJavaMethodExpression"):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaMethodExpression"):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = EParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_selector_expression)
        try:
            self.state = 2217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2214
                self.match(EParser.DOT)
                self.state = 2215
                localctx.exp = self.java_method_expression()
                pass
            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2216
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
            if hasattr(listener, "enterJava_method_expression"):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_method_expression"):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = EParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2219
            localctx.name = self.java_identifier()
            self.state = 2220
            self.match(EParser.LPAR)
            self.state = 2222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (EParser.LPAR - 20)) | (1 << (EParser.BOOLEAN - 20)) | (1 << (EParser.CHARACTER - 20)) | (1 << (EParser.TEXT - 20)) | (1 << (EParser.INTEGER - 20)) | (1 << (EParser.DECIMAL - 20)) | (1 << (EParser.DATE - 20)) | (1 << (EParser.TIME - 20)) | (1 << (EParser.DATETIME - 20)) | (1 << (EParser.PERIOD - 20)) | (1 << (EParser.VERSION - 20)) | (1 << (EParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.THIS - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.BOOLEAN_LITERAL - 121)) | (1 << (EParser.CHAR_LITERAL - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)) | (1 << (EParser.NATIVE_IDENTIFIER - 121)) | (1 << (EParser.DOLLAR_IDENTIFIER - 121)) | (1 << (EParser.TEXT_LITERAL - 121)) | (1 << (EParser.INTEGER_LITERAL - 121)) | (1 << (EParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2221
                localctx.args = self.java_arguments(0)


            self.state = 2224
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
            if hasattr(listener, "enterJavaArgumentListItem"):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentListItem"):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentList"):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentList"):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2227
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2229
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2230
                    self.match(EParser.COMMA)
                    self.state = 2231
                    localctx.item = self.java_expression(0) 
                self.state = 2236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

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
            if hasattr(listener, "enterJava_item_expression"):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_item_expression"):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = EParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2237
            self.match(EParser.LBRAK)
            self.state = 2238
            localctx.exp = self.java_expression(0)
            self.state = 2239
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
            if hasattr(listener, "enterJava_parenthesis_expression"):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_parenthesis_expression"):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = EParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2241
            self.match(EParser.LPAR)
            self.state = 2242
            localctx.exp = self.java_expression(0)
            self.state = 2243
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
            if hasattr(listener, "enterJavaIdentifier"):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIdentifier"):
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
            if hasattr(listener, "enterJavaChildIdentifier"):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildIdentifier"):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 384
        self.enterRecursionRule(localctx, 384, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2246
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,187,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2248
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2249
                    self.match(EParser.DOT)
                    self.state = 2250
                    localctx.name = self.java_identifier() 
                self.state = 2255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,187,self._ctx)

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
            if hasattr(listener, "enterJavaClassIdentifier"):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaClassIdentifier"):
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
            if hasattr(listener, "enterJavaChildClassIdentifier"):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildClassIdentifier"):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 386
        self.enterRecursionRule(localctx, 386, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2257
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,188,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2259
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2260
                    localctx.name = self.match(EParser.DOLLAR_IDENTIFIER) 
                self.state = 2265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,188,self._ctx)

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
            if hasattr(listener, "enterJavaBooleanLiteral"):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaBooleanLiteral"):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCharacterLiteral"):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCharacterLiteral"):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIntegerLiteral"):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIntegerLiteral"):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaTextLiteral"):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaTextLiteral"):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaDecimalLiteral"):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaDecimalLiteral"):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = EParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_java_literal_expression)
        try:
            self.state = 2271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2266
                localctx.t = self.match(EParser.INTEGER_LITERAL)
                pass
            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2267
                localctx.t = self.match(EParser.DECIMAL_LITERAL)
                pass
            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2268
                localctx.t = self.match(EParser.TEXT_LITERAL)
                pass
            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2269
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)
                pass
            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2270
                localctx.t = self.match(EParser.CHAR_LITERAL)
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

        def VERSION(self):
            return self.getToken(EParser.VERSION, 0)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def NONE(self):
            return self.getToken(EParser.NONE, 0)

        def NULL(self):
            return self.getToken(EParser.NULL, 0)

        def getRuleIndex(self):
            return EParser.RULE_java_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_identifier"):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_identifier"):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = EParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2273
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (EParser.BOOLEAN - 50)) | (1 << (EParser.CHARACTER - 50)) | (1 << (EParser.TEXT - 50)) | (1 << (EParser.INTEGER - 50)) | (1 << (EParser.DECIMAL - 50)) | (1 << (EParser.DATE - 50)) | (1 << (EParser.TIME - 50)) | (1 << (EParser.DATETIME - 50)) | (1 << (EParser.PERIOD - 50)) | (1 << (EParser.VERSION - 50)) | (1 << (EParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)) | (1 << (EParser.NATIVE_IDENTIFIER - 121)) | (1 << (EParser.DOLLAR_IDENTIFIER - 121)))) != 0)):
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
            if hasattr(listener, "enterCSharpReturnStatement"):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpReturnStatement"):
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
            if hasattr(listener, "enterCSharpStatement"):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpStatement"):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = EParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_csharp_statement)
        try:
            self.state = 2282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2275
                self.match(EParser.RETURN)
                self.state = 2276
                localctx.exp = self.csharp_expression(0)
                self.state = 2277
                self.match(EParser.SEMI)
                pass
            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.UUID, EParser.NONE, EParser.NULL, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2279
                localctx.exp = self.csharp_expression(0)
                self.state = 2280
                self.match(EParser.SEMI)
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
            if hasattr(listener, "enterCSharpSelectorExpression"):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpSelectorExpression"):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPrimaryExpression"):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPrimaryExpression"):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 394
        self.enterRecursionRule(localctx, 394, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2285
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2287
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2288
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

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
            if hasattr(listener, "enterCsharp_primary_expression"):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_primary_expression"):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = EParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_primary_expression)
        try:
            self.state = 2299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,192,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2294
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2295
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2296
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2297
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2298
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
            if hasattr(listener, "enterCsharp_this_expression"):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_this_expression"):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = EParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2301
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
            if hasattr(listener, "enterCsharp_new_expression"):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_new_expression"):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = EParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2303
            self.new_token()
            self.state = 2304
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
            if hasattr(listener, "enterCSharpMethodExpression"):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpMethodExpression"):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpItemExpression"):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpItemExpression"):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = EParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_selector_expression)
        try:
            self.state = 2309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2306
                self.match(EParser.DOT)
                self.state = 2307
                localctx.exp = self.csharp_method_expression()
                pass
            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2308
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
            if hasattr(listener, "enterCsharp_method_expression"):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_method_expression"):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = EParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2311
            localctx.name = self.csharp_identifier()
            self.state = 2312
            self.match(EParser.LPAR)
            self.state = 2314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (EParser.LPAR - 20)) | (1 << (EParser.BOOLEAN - 20)) | (1 << (EParser.CHARACTER - 20)) | (1 << (EParser.TEXT - 20)) | (1 << (EParser.INTEGER - 20)) | (1 << (EParser.DECIMAL - 20)) | (1 << (EParser.DATE - 20)) | (1 << (EParser.TIME - 20)) | (1 << (EParser.DATETIME - 20)) | (1 << (EParser.PERIOD - 20)) | (1 << (EParser.VERSION - 20)) | (1 << (EParser.UUID - 20)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.THIS - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.BOOLEAN_LITERAL - 121)) | (1 << (EParser.CHAR_LITERAL - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)) | (1 << (EParser.DOLLAR_IDENTIFIER - 121)) | (1 << (EParser.TEXT_LITERAL - 121)) | (1 << (EParser.INTEGER_LITERAL - 121)) | (1 << (EParser.DECIMAL_LITERAL - 121)))) != 0):
                self.state = 2313
                localctx.args = self.csharp_arguments(0)


            self.state = 2316
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
            if hasattr(listener, "enterCSharpArgumentList"):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentList"):
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
            if hasattr(listener, "enterCSharpArgumentListItem"):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentListItem"):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 406
        self.enterRecursionRule(localctx, 406, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2319
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2321
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2322
                    self.match(EParser.COMMA)
                    self.state = 2323
                    localctx.item = self.csharp_expression(0) 
                self.state = 2328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

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
            if hasattr(listener, "enterCsharp_item_expression"):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_item_expression"):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = EParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2329
            self.match(EParser.LBRAK)
            self.state = 2330
            localctx.exp = self.csharp_expression(0)
            self.state = 2331
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
            if hasattr(listener, "enterCsharp_parenthesis_expression"):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_parenthesis_expression"):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = EParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2333
            self.match(EParser.LPAR)
            self.state = 2334
            localctx.exp = self.csharp_expression(0)
            self.state = 2335
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
            if hasattr(listener, "enterCSharpIdentifier"):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIdentifier"):
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
            if hasattr(listener, "enterCSharpChildIdentifier"):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpChildIdentifier"):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPromptoIdentifier"):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPromptoIdentifier"):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 412
        self.enterRecursionRule(localctx, 412, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2338
                self.match(EParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.VERSION, EParser.UUID, EParser.NONE, EParser.NULL, EParser.READ, EParser.SELF, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2339
                localctx.name = self.csharp_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,197,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2342
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2343
                    self.match(EParser.DOT)
                    self.state = 2344
                    localctx.name = self.csharp_identifier() 
                self.state = 2349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,197,self._ctx)

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
            if hasattr(listener, "enterCSharpBooleanLiteral"):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpBooleanLiteral"):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIntegerLiteral"):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIntegerLiteral"):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpDecimalLiteral"):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpDecimalLiteral"):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCharacterLiteral"):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCharacterLiteral"):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpTextLiteral"):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpTextLiteral"):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = EParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_csharp_literal_expression)
        try:
            self.state = 2355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2350
                self.match(EParser.INTEGER_LITERAL)
                pass
            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2351
                self.match(EParser.DECIMAL_LITERAL)
                pass
            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2352
                self.match(EParser.TEXT_LITERAL)
                pass
            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2353
                self.match(EParser.BOOLEAN_LITERAL)
                pass
            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2354
                self.match(EParser.CHAR_LITERAL)
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

        def VERSION(self):
            return self.getToken(EParser.VERSION, 0)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def NONE(self):
            return self.getToken(EParser.NONE, 0)

        def NULL(self):
            return self.getToken(EParser.NULL, 0)

        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_identifier"):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_identifier"):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = EParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2357
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (EParser.BOOLEAN - 50)) | (1 << (EParser.CHARACTER - 50)) | (1 << (EParser.TEXT - 50)) | (1 << (EParser.INTEGER - 50)) | (1 << (EParser.DECIMAL - 50)) | (1 << (EParser.DATE - 50)) | (1 << (EParser.TIME - 50)) | (1 << (EParser.DATETIME - 50)) | (1 << (EParser.PERIOD - 50)) | (1 << (EParser.VERSION - 50)) | (1 << (EParser.UUID - 50)))) != 0) or ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & ((1 << (EParser.NONE - 121)) | (1 << (EParser.NULL - 121)) | (1 << (EParser.READ - 121)) | (1 << (EParser.SELF - 121)) | (1 << (EParser.TEST - 121)) | (1 << (EParser.WRITE - 121)) | (1 << (EParser.SYMBOL_IDENTIFIER - 121)) | (1 << (EParser.TYPE_IDENTIFIER - 121)) | (1 << (EParser.VARIABLE_IDENTIFIER - 121)))) != 0)):
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
        self._predicates[16] = self.native_category_binding_list_sempred
        self._predicates[37] = self.else_if_statement_list_sempred
        self._predicates[43] = self.expression_sempred
        self._predicates[44] = self.unresolved_expression_sempred
        self._predicates[45] = self.unresolved_selector_sempred
        self._predicates[47] = self.invocation_trailer_sempred
        self._predicates[48] = self.instance_expression_sempred
        self._predicates[49] = self.instance_selector_sempred
        self._predicates[58] = self.argument_assignment_list_sempred
        self._predicates[59] = self.with_argument_assignment_list_sempred
        self._predicates[62] = self.child_instance_sempred
        self._predicates[82] = self.typedef_sempred
        self._predicates[102] = self.any_type_sempred
        self._predicates[139] = self.assignable_instance_sempred
        self._predicates[140] = self.is_expression_sempred
        self._predicates[146] = self.new_token_sempred
        self._predicates[147] = self.key_token_sempred
        self._predicates[148] = self.module_token_sempred
        self._predicates[149] = self.value_token_sempred
        self._predicates[150] = self.symbols_token_sempred
        self._predicates[157] = self.javascript_expression_sempred
        self._predicates[163] = self.javascript_arguments_sempred
        self._predicates[170] = self.python_expression_sempred
        self._predicates[176] = self.python_ordinal_argument_list_sempred
        self._predicates[177] = self.python_named_argument_list_sempred
        self._predicates[179] = self.python_identifier_expression_sempred
        self._predicates[183] = self.java_expression_sempred
        self._predicates[189] = self.java_arguments_sempred
        self._predicates[192] = self.java_identifier_expression_sempred
        self._predicates[193] = self.java_class_identifier_expression_sempred
        self._predicates[197] = self.csharp_expression_sempred
        self._predicates[203] = self.csharp_arguments_sempred
        self._predicates[206] = self.csharp_identifier_expression_sempred
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
                return self.precpred(self._ctx, 42)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 41)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 40)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 39)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 38)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 37)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 8)
         

    def unresolved_expression_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.precpred(self._ctx, 1)
         

    def unresolved_selector_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.wasNot(EParser.WS)
         

    def invocation_trailer_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.willBe(EParser.LF)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.wasNot(EParser.WS)
         

            if predIndex == 37:
                return self.wasNot(EParser.WS)
         

            if predIndex == 38:
                return self.wasNot(EParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.was(EParser.WS)
         

    def with_argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.wasNot(EParser.WS)
         

            if predIndex == 42:
                return self.wasNot(EParser.WS)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.precpred(self._ctx, 1)
         




