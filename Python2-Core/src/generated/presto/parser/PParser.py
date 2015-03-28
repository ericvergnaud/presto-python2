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
        buf.write(u"\u0099\u07d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00ba\t\u00ba\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u017b\n")
        buf.write(u"\2\3\2\5\2\u017e\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write(u"\3\5\3\5\5\5\u0197\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\5\6\u01a4\n\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\5\7\u01b1\n\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\5\7\u01b8\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\5\b\u01c5\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3")
        buf.write(u"\n\5\n\u01cf\n\n\3\n\3\n\3\n\5\n\u01d4\n\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5")
        buf.write(u"\13\u01e3\n\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u0203\n")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\5\17\u0210\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\7\21\u0225\n\21\f\21\16\21\u0228\13\21\3\22")
        buf.write(u"\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u0231\n\23\3\23\3")
        buf.write(u"\23\3\23\5\23\u0236\n\23\3\24\3\24\3\24\3\24\5\24\u023c")
        buf.write(u"\n\24\3\24\3\24\3\24\5\24\u0241\n\24\3\24\3\24\3\24\3")
        buf.write(u"\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u024d\n\25\3\25")
        buf.write(u"\3\25\3\25\5\25\u0252\n\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u026a\n\26\3\27\3")
        buf.write(u"\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0275\n\30")
        buf.write(u"\3\30\3\30\5\30\u0279\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write(u"\u028a\n\31\3\32\3\32\3\32\5\32\u028f\n\32\3\32\3\32")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\5\33\u0298\n\33\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\7\34\u029f\n\34\f\34\16\34\u02a2\13\34")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u02aa\n\35\3\36\3")
        buf.write(u"\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 ")
        buf.write(u"\u02c7\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write(u"!\3!\3!\5!\u02da\n!\3\"\3\"\3\"\3\"\5\"\u02e0\n\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write(u"$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0302")
        buf.write(u"\n%\3%\3%\3%\3%\3%\3%\3%\5%\u030b\n%\3&\3&\3&\3&\3&\3")
        buf.write(u"&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u0320\n&")
        buf.write(u"\f&\16&\u0323\13&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\5(\u0330\n(\3(\3(\3(\3(\3(\3(\3(\5(\u0339\n(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\5(\u0342\n(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0359\n)\3*")
        buf.write(u"\3*\5*\u035d\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\5+\u0371\n+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\7+\u03d1")
        buf.write(u"\n+\f+\16+\u03d4\13+\3,\3,\3-\3-\3-\3-\3-\7-\u03dd\n")
        buf.write(u"-\f-\16-\u03e0\13-\3.\3.\3.\3.\3.\3.\5.\u03e8\n.\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u03f7\n/\3\60\3")
        buf.write(u"\60\3\61\3\61\3\61\5\61\u03fe\n\61\3\61\3\61\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\5\62\u0407\n\62\3\62\3\62\3\62\7\62\u040c")
        buf.write(u"\n\62\f\62\16\62\u040f\13\62\3\63\3\63\3\63\3\63\3\64")
        buf.write(u"\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3")
        buf.write(u"\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\5\67\u042d\n\67\3\67\3\67\38\38\38\38\39\3")
        buf.write(u"9\39\39\39\39\39\39\59\u043d\n9\3:\3:\3:\3:\3;\7;\u0444")
        buf.write(u"\n;\f;\16;\u0447\13;\3<\6<\u044a\n<\r<\16<\u044b\3=\6")
        buf.write(u"=\u044f\n=\r=\16=\u0450\3=\3=\3>\7>\u0456\n>\f>\16>\u0459")
        buf.write(u"\13>\3>\3>\3?\3?\3@\5@\u0460\n@\3@\3@\3@\3A\3A\3A\3A")
        buf.write(u"\3A\3A\3A\7A\u046c\nA\fA\16A\u046f\13A\3B\3B\3B\3B\3")
        buf.write(u"B\5B\u0476\nB\3C\3C\3D\3D\5D\u047c\nD\3E\3E\3E\3E\3E")
        buf.write(u"\3E\3E\7E\u0485\nE\fE\16E\u0488\13E\3F\3F\3F\3F\3F\3")
        buf.write(u"F\3F\7F\u0491\nF\fF\16F\u0494\13F\3G\3G\3G\3G\3G\3G\7")
        buf.write(u"G\u049c\nG\fG\16G\u049f\13G\3H\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write(u"H\3H\5H\u04ab\nH\3I\3I\5I\u04af\nI\3I\3I\3J\3J\5J\u04b5")
        buf.write(u"\nJ\3J\3J\3K\3K\3K\3K\3K\3K\7K\u04bf\nK\fK\16K\u04c2")
        buf.write(u"\13K\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M")
        buf.write(u"\3M\7M\u04d5\nM\fM\16M\u04d8\13M\3N\3N\5N\u04dc\nN\3")
        buf.write(u"O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u04e8\nO\3P\3P\3Q\3Q")
        buf.write(u"\3R\3R\3S\3S\3S\5S\u04f3\nS\3T\3T\3T\3T\3T\3T\7T\u04fb")
        buf.write(u"\nT\fT\16T\u04fe\13T\3U\3U\5U\u0502\nU\3V\3V\3V\5V\u0507")
        buf.write(u"\nV\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\7Z\u0515\nZ\f")
        buf.write(u"Z\16Z\u0518\13Z\3[\3[\5[\u051c\n[\3\\\3\\\5\\\u0520\n")
        buf.write(u"\\\3]\3]\3]\5]\u0525\n]\3^\3^\3^\3_\3_\5_\u052c\n_\3")
        buf.write(u"`\3`\3`\3`\3`\3`\3`\3`\3`\7`\u0537\n`\f`\16`\u053a\13")
        buf.write(u"`\3a\3a\3a\3a\3a\3a\3a\7a\u0543\na\fa\16a\u0546\13a\3")
        buf.write(u"b\3b\3b\3b\5b\u054c\nb\3c\3c\3c\3c\3c\3c\3c\3c\3c\3c")
        buf.write(u"\5c\u0558\nc\3d\3d\5d\u055c\nd\3e\3e\3e\3e\3e\3e\7e\u0564")
        buf.write(u"\ne\fe\16e\u0567\13e\3f\3f\3f\3g\3g\5g\u056e\ng\3h\3")
        buf.write(u"h\3h\3h\5h\u0574\nh\3h\3h\3h\7h\u0579\nh\fh\16h\u057c")
        buf.write(u"\13h\3h\3h\5h\u0580\nh\3i\3i\3i\3i\3i\3i\7i\u0588\ni")
        buf.write(u"\fi\16i\u058b\13i\3j\3j\3j\3j\5j\u0591\nj\3k\3k\3k\3")
        buf.write(u"k\3k\3k\3k\7k\u059a\nk\fk\16k\u059d\13k\3l\3l\3l\3l\3")
        buf.write(u"l\3l\3l\3l\3l\3l\5l\u05a9\nl\3m\3m\5m\u05ad\nm\3m\5m")
        buf.write(u"\u05b0\nm\3n\3n\5n\u05b4\nn\3n\5n\u05b7\nn\3o\3o\3o\3")
        buf.write(u"o\3o\3o\3o\7o\u05c0\no\fo\16o\u05c3\13o\3p\3p\3p\3p\3")
        buf.write(u"p\3p\3p\7p\u05cc\np\fp\16p\u05cf\13p\3q\3q\3q\3q\3q\3")
        buf.write(u"q\3q\7q\u05d8\nq\fq\16q\u05db\13q\3r\3r\3r\3r\3r\3r\3")
        buf.write(u"r\7r\u05e4\nr\fr\16r\u05e7\13r\3s\3s\3s\3s\3s\3s\3s\3")
        buf.write(u"s\3s\3s\3s\3s\3s\3s\5s\u05f7\ns\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\5t\u0606\nt\3u\3u\3u\3u\3u\3u\7u\u060e")
        buf.write(u"\nu\fu\16u\u0611\13u\3v\3v\3v\3v\5v\u0617\nv\3w\3w\3")
        buf.write(u"x\3x\3x\3x\3y\3y\5y\u0621\ny\3z\3z\3z\3z\3z\5z\u0628")
        buf.write(u"\nz\3{\3{\5{\u062c\n{\3{\3{\3|\3|\5|\u0632\n|\3|\3|\3")
        buf.write(u"}\3}\3}\3}\3}\3}\7}\u063c\n}\f}\16}\u063f\13}\3~\3~\3")
        buf.write(u"~\3~\3~\3~\7~\u0647\n~\f~\16~\u064a\13~\3\177\3\177\3")
        buf.write(u"\177\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3")
        buf.write(u"\u0080\3\u0080\3\u0080\3\u0080\5\u0080\u0659\n\u0080")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0082\3\u0082\7\u0082\u0664\n\u0082\f\u0082\16\u0082")
        buf.write(u"\u0667\13\u0082\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083")
        buf.write(u"\u066d\n\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\5\u0084\u0675\n\u0084\3\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0086\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087\3\u0088")
        buf.write(u"\3\u0088\3\u0089\3\u0089\3\u008a\3\u008a\3\u008b\3\u008b")
        buf.write(u"\3\u008c\3\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write(u"\3\u008d\3\u008d\5\u008d\u0691\n\u008d\3\u008e\3\u008e")
        buf.write(u"\3\u008e\3\u008e\3\u008e\7\u008e\u0698\n\u008e\f\u008e")
        buf.write(u"\16\u008e\u069b\13\u008e\3\u008f\3\u008f\3\u008f\5\u008f")
        buf.write(u"\u06a0\n\u008f\3\u0090\3\u0090\3\u0090\5\u0090\u06a5")
        buf.write(u"\n\u0090\3\u0091\3\u0091\3\u0091\5\u0091\u06aa\n\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\7\u0092\u06b4\n\u0092\f\u0092\16\u0092\u06b7")
        buf.write(u"\13\u0092\3\u0093\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094")
        buf.write(u"\3\u0094\3\u0094\3\u0095\3\u0095\3\u0095\3\u0095\3\u0095")
        buf.write(u"\3\u0095\7\u0095\u06c7\n\u0095\f\u0095\16\u0095\u06ca")
        buf.write(u"\13\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096\5\u0096")
        buf.write(u"\u06d1\n\u0096\3\u0097\3\u0097\3\u0098\3\u0098\3\u0098")
        buf.write(u"\5\u0098\u06d8\n\u0098\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write(u"\3\u0099\7\u0099\u06df\n\u0099\f\u0099\16\u0099\u06e2")
        buf.write(u"\13\u0099\3\u009a\3\u009a\3\u009a\3\u009a\5\u009a\u06e8")
        buf.write(u"\n\u009a\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write(u"\5\u009b\u06f0\n\u009b\3\u009c\3\u009c\3\u009c\5\u009c")
        buf.write(u"\u06f5\n\u009c\3\u009c\3\u009c\3\u009d\3\u009d\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\5\u009d\u06ff\n\u009d\3\u009e")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\7\u009e\u0707")
        buf.write(u"\n\u009e\f\u009e\16\u009e\u070a\13\u009e\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\7\u009f\u0717\n\u009f\f\u009f\16\u009f")
        buf.write(u"\u071a\13\u009f\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a1")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\7\u00a1\u0726")
        buf.write(u"\n\u00a1\f\u00a1\16\u00a1\u0729\13\u00a1\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u0730\n\u00a2\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\5\u00a4\u073b\n\u00a4\3\u00a5\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\7\u00a5\u0742\n\u00a5\f\u00a5\16\u00a5")
        buf.write(u"\u0745\13\u00a5\3\u00a6\3\u00a6\3\u00a6\5\u00a6\u074a")
        buf.write(u"\n\u00a6\3\u00a7\3\u00a7\3\u00a7\5\u00a7\u074f\n\u00a7")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\5\u00a8\u0754\n\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\7\u00a9\u075e\n\u00a9\f\u00a9\16\u00a9\u0761\13\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\7\u00ac\u0771\n\u00ac\f\u00ac\16\u00ac\u0774\13\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\7\u00ad")
        buf.write(u"\u077c\n\u00ad\f\u00ad\16\u00ad\u077f\13\u00ad\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u0786\n\u00ae")
        buf.write(u"\3\u00af\3\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\5\u00b0\u0791\n\u00b0\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u0798\n\u00b1\f\u00b1")
        buf.write(u"\16\u00b1\u079b\13\u00b1\3\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write(u"\u07a0\n\u00b2\3\u00b3\3\u00b3\3\u00b3\5\u00b3\u07a5")
        buf.write(u"\n\u00b3\3\u00b4\3\u00b4\3\u00b4\5\u00b4\u07aa\n\u00b4")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\7\u00b5\u07b4\n\u00b5\f\u00b5\16\u00b5\u07b7")
        buf.write(u"\13\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\7\u00b8\u07c7\n\u00b8\f\u00b8\16\u00b8\u07ca")
        buf.write(u"\13\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\5\u00b9")
        buf.write(u"\u07d1\n\u00b9\3\u00ba\3\u00ba\3\u00ba\2* \66JTXb\u0080")
        buf.write(u"\u0088\u008a\u008c\u0094\u0098\u00a6\u00b2\u00be\u00c0")
        buf.write(u"\u00d0\u00d4\u00dc\u00de\u00e0\u00e2\u00e8\u00f8\u00fa")
        buf.write(u"\u0102\u011a\u0122\u0128\u0130\u013a\u013c\u0140\u0148")
        buf.write(u"\u0150\u0156\u0158\u0160\u0168\u016e\u00bb\2\4\6\b\n")
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
        buf.write(u"\u0170\u0172\2\7\3\2KL\3\2\"#\4\2{{\u0081\u0081\4\2\'")
        buf.write(u"\'ii\7\2\64<vv\u0080\u0080\u0089\u0089\u008e\u0090\u0823")
        buf.write(u"\2\u0174\3\2\2\2\4\u0185\3\2\2\2\6\u018f\3\2\2\2\b\u0193")
        buf.write(u"\3\2\2\2\n\u019a\3\2\2\2\f\u01a7\3\2\2\2\16\u01bb\3\2")
        buf.write(u"\2\2\20\u01c8\3\2\2\2\22\u01ca\3\2\2\2\24\u01da\3\2\2")
        buf.write(u"\2\26\u01e9\3\2\2\2\30\u01f3\3\2\2\2\32\u01fd\3\2\2\2")
        buf.write(u"\34\u020a\3\2\2\2\36\u0217\3\2\2\2 \u021d\3\2\2\2\"\u0229")
        buf.write(u"\3\2\2\2$\u022b\3\2\2\2&\u0237\3\2\2\2(\u0247\3\2\2\2")
        buf.write(u"*\u0258\3\2\2\2,\u026b\3\2\2\2.\u026d\3\2\2\2\60\u0289")
        buf.write(u"\3\2\2\2\62\u028b\3\2\2\2\64\u0297\3\2\2\2\66\u0299\3")
        buf.write(u"\2\2\28\u02a9\3\2\2\2:\u02ab\3\2\2\2<\u02b2\3\2\2\2>")
        buf.write(u"\u02b9\3\2\2\2@\u02d9\3\2\2\2B\u02db\3\2\2\2D\u02e8\3")
        buf.write(u"\2\2\2F\u02f1\3\2\2\2H\u02f8\3\2\2\2J\u030c\3\2\2\2L")
        buf.write(u"\u0324\3\2\2\2N\u0327\3\2\2\2P\u0358\3\2\2\2R\u035a\3")
        buf.write(u"\2\2\2T\u0370\3\2\2\2V\u03d5\3\2\2\2X\u03d7\3\2\2\2Z")
        buf.write(u"\u03e7\3\2\2\2\\\u03f6\3\2\2\2^\u03f8\3\2\2\2`\u03fa")
        buf.write(u"\3\2\2\2b\u0406\3\2\2\2d\u0410\3\2\2\2f\u0414\3\2\2\2")
        buf.write(u"h\u0418\3\2\2\2j\u041d\3\2\2\2l\u0424\3\2\2\2n\u0430")
        buf.write(u"\3\2\2\2p\u043c\3\2\2\2r\u043e\3\2\2\2t\u0445\3\2\2\2")
        buf.write(u"v\u0449\3\2\2\2x\u044e\3\2\2\2z\u0457\3\2\2\2|\u045c")
        buf.write(u"\3\2\2\2~\u045f\3\2\2\2\u0080\u0464\3\2\2\2\u0082\u0475")
        buf.write(u"\3\2\2\2\u0084\u0477\3\2\2\2\u0086\u047b\3\2\2\2\u0088")
        buf.write(u"\u047d\3\2\2\2\u008a\u0489\3\2\2\2\u008c\u0495\3\2\2")
        buf.write(u"\2\u008e\u04aa\3\2\2\2\u0090\u04ac\3\2\2\2\u0092\u04b2")
        buf.write(u"\3\2\2\2\u0094\u04b8\3\2\2\2\u0096\u04c3\3\2\2\2\u0098")
        buf.write(u"\u04c9\3\2\2\2\u009a\u04db\3\2\2\2\u009c\u04e7\3\2\2")
        buf.write(u"\2\u009e\u04e9\3\2\2\2\u00a0\u04eb\3\2\2\2\u00a2\u04ed")
        buf.write(u"\3\2\2\2\u00a4\u04f2\3\2\2\2\u00a6\u04f4\3\2\2\2\u00a8")
        buf.write(u"\u0501\3\2\2\2\u00aa\u0506\3\2\2\2\u00ac\u0508\3\2\2")
        buf.write(u"\2\u00ae\u050a\3\2\2\2\u00b0\u050c\3\2\2\2\u00b2\u050e")
        buf.write(u"\3\2\2\2\u00b4\u051b\3\2\2\2\u00b6\u051f\3\2\2\2\u00b8")
        buf.write(u"\u0521\3\2\2\2\u00ba\u0526\3\2\2\2\u00bc\u052b\3\2\2")
        buf.write(u"\2\u00be\u052d\3\2\2\2\u00c0\u053b\3\2\2\2\u00c2\u054b")
        buf.write(u"\3\2\2\2\u00c4\u0557\3\2\2\2\u00c6\u0559\3\2\2\2\u00c8")
        buf.write(u"\u055d\3\2\2\2\u00ca\u0568\3\2\2\2\u00cc\u056b\3\2\2")
        buf.write(u"\2\u00ce\u056f\3\2\2\2\u00d0\u0581\3\2\2\2\u00d2\u0590")
        buf.write(u"\3\2\2\2\u00d4\u0592\3\2\2\2\u00d6\u05a8\3\2\2\2\u00d8")
        buf.write(u"\u05aa\3\2\2\2\u00da\u05b1\3\2\2\2\u00dc\u05b8\3\2\2")
        buf.write(u"\2\u00de\u05c4\3\2\2\2\u00e0\u05d0\3\2\2\2\u00e2\u05dc")
        buf.write(u"\3\2\2\2\u00e4\u05f6\3\2\2\2\u00e6\u0605\3\2\2\2\u00e8")
        buf.write(u"\u0607\3\2\2\2\u00ea\u0616\3\2\2\2\u00ec\u0618\3\2\2")
        buf.write(u"\2\u00ee\u061a\3\2\2\2\u00f0\u0620\3\2\2\2\u00f2\u0627")
        buf.write(u"\3\2\2\2\u00f4\u0629\3\2\2\2\u00f6\u062f\3\2\2\2\u00f8")
        buf.write(u"\u0635\3\2\2\2\u00fa\u0640\3\2\2\2\u00fc\u064b\3\2\2")
        buf.write(u"\2\u00fe\u0658\3\2\2\2\u0100\u065a\3\2\2\2\u0102\u065e")
        buf.write(u"\3\2\2\2\u0104\u066c\3\2\2\2\u0106\u0674\3\2\2\2\u0108")
        buf.write(u"\u0676\3\2\2\2\u010a\u0679\3\2\2\2\u010c\u067c\3\2\2")
        buf.write(u"\2\u010e\u067f\3\2\2\2\u0110\u0681\3\2\2\2\u0112\u0683")
        buf.write(u"\3\2\2\2\u0114\u0685\3\2\2\2\u0116\u0687\3\2\2\2\u0118")
        buf.write(u"\u0690\3\2\2\2\u011a\u0692\3\2\2\2\u011c\u069f\3\2\2")
        buf.write(u"\2\u011e\u06a4\3\2\2\2\u0120\u06a6\3\2\2\2\u0122\u06ad")
        buf.write(u"\3\2\2\2\u0124\u06b8\3\2\2\2\u0126\u06bc\3\2\2\2\u0128")
        buf.write(u"\u06c0\3\2\2\2\u012a\u06d0\3\2\2\2\u012c\u06d2\3\2\2")
        buf.write(u"\2\u012e\u06d7\3\2\2\2\u0130\u06d9\3\2\2\2\u0132\u06e7")
        buf.write(u"\3\2\2\2\u0134\u06ef\3\2\2\2\u0136\u06f1\3\2\2\2\u0138")
        buf.write(u"\u06fe\3\2\2\2\u013a\u0700\3\2\2\2\u013c\u070b\3\2\2")
        buf.write(u"\2\u013e\u071b\3\2\2\2\u0140\u071f\3\2\2\2\u0142\u072f")
        buf.write(u"\3\2\2\2\u0144\u0731\3\2\2\2\u0146\u073a\3\2\2\2\u0148")
        buf.write(u"\u073c\3\2\2\2\u014a\u0749\3\2\2\2\u014c\u074e\3\2\2")
        buf.write(u"\2\u014e\u0750\3\2\2\2\u0150\u0757\3\2\2\2\u0152\u0762")
        buf.write(u"\3\2\2\2\u0154\u0766\3\2\2\2\u0156\u076a\3\2\2\2\u0158")
        buf.write(u"\u0775\3\2\2\2\u015a\u0785\3\2\2\2\u015c\u0787\3\2\2")
        buf.write(u"\2\u015e\u0790\3\2\2\2\u0160\u0792\3\2\2\2\u0162\u079f")
        buf.write(u"\3\2\2\2\u0164\u07a4\3\2\2\2\u0166\u07a6\3\2\2\2\u0168")
        buf.write(u"\u07ad\3\2\2\2\u016a\u07b8\3\2\2\2\u016c\u07bc\3\2\2")
        buf.write(u"\2\u016e\u07c0\3\2\2\2\u0170\u07d0\3\2\2\2\u0172\u07d2")
        buf.write(u"\3\2\2\2\u0174\u0175\7V\2\2\u0175\u0176\5\u00aeX\2\u0176")
        buf.write(u"\u017d\7\25\2\2\u0177\u017a\5\u00aeX\2\u0178\u0179\7")
        buf.write(u"\22\2\2\u0179\u017b\5\"\22\2\u017a\u0178\3\2\2\2\u017a")
        buf.write(u"\u017b\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017e\5\"\22")
        buf.write(u"\2\u017d\u0177\3\2\2\2\u017d\u017c\3\2\2\2\u017e\u017f")
        buf.write(u"\3\2\2\2\u017f\u0180\7\26\2\2\u0180\u0181\7\20\2\2\u0181")
        buf.write(u"\u0182\5x=\2\u0182\u0183\5\u008aF\2\u0183\u0184\5z>\2")
        buf.write(u"\u0184\3\3\2\2\2\u0185\u0186\7V\2\2\u0186\u0187\5\u00ae")
        buf.write(u"X\2\u0187\u0188\7\25\2\2\u0188\u0189\5\u009cO\2\u0189")
        buf.write(u"\u018a\7\26\2\2\u018a\u018b\7\20\2\2\u018b\u018c\5x=")
        buf.write(u"\2\u018c\u018d\5\u0088E\2\u018d\u018e\5z>\2\u018e\5\3")
        buf.write(u"\2\2\2\u018f\u0190\5\u00b0Y\2\u0190\u0191\7-\2\2\u0191")
        buf.write(u"\u0192\5T+\2\u0192\7\3\2\2\2\u0193\u0194\5\u00b0Y\2\u0194")
        buf.write(u"\u0196\7\25\2\2\u0195\u0197\5b\62\2\u0196\u0195\3\2\2")
        buf.write(u"\2\u0196\u0197\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199")
        buf.write(u"\7\26\2\2\u0199\t\3\2\2\2\u019a\u019b\7F\2\2\u019b\u019c")
        buf.write(u"\5\u00acW\2\u019c\u019d\7\25\2\2\u019d\u019e\5\u0098")
        buf.write(u"M\2\u019e\u019f\7\26\2\2\u019f\u01a0\7\20\2\2\u01a0\u01a3")
        buf.write(u"\5x=\2\u01a1\u01a4\5\u008eH\2\u01a2\u01a4\7t\2\2\u01a3")
        buf.write(u"\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5\3\2\2")
        buf.write(u"\2\u01a5\u01a6\5z>\2\u01a6\13\3\2\2\2\u01a7\u01a8\t\2")
        buf.write(u"\2\2\u01a8\u01a9\5\u00aeX\2\u01a9\u01b0\7\25\2\2\u01aa")
        buf.write(u"\u01b1\5\20\t\2\u01ab\u01b1\5\"\22\2\u01ac\u01ad\5\20")
        buf.write(u"\t\2\u01ad\u01ae\7\22\2\2\u01ae\u01af\5\"\22\2\u01af")
        buf.write(u"\u01b1\3\2\2\2\u01b0\u01aa\3\2\2\2\u01b0\u01ab\3\2\2")
        buf.write(u"\2\u01b0\u01ac\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3")
        buf.write(u"\7\26\2\2\u01b3\u01b4\7\20\2\2\u01b4\u01b7\5x=\2\u01b5")
        buf.write(u"\u01b8\5\u00c0a\2\u01b6\u01b8\7t\2\2\u01b7\u01b5\3\2")
        buf.write(u"\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba")
        buf.write(u"\5z>\2\u01ba\r\3\2\2\2\u01bb\u01bc\7}\2\2\u01bc\u01bd")
        buf.write(u"\5\u00aeX\2\u01bd\u01be\7\25\2\2\u01be\u01bf\5\"\22\2")
        buf.write(u"\u01bf\u01c0\7\26\2\2\u01c0\u01c1\7\20\2\2\u01c1\u01c4")
        buf.write(u"\5x=\2\u01c2\u01c5\5\u00c0a\2\u01c3\u01c5\7t\2\2\u01c4")
        buf.write(u"\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2")
        buf.write(u"\2\u01c6\u01c7\5z>\2\u01c7\17\3\2\2\2\u01c8\u01c9\5\u00a6")
        buf.write(u"T\2\u01c9\21\3\2\2\2\u01ca\u01cb\7O\2\2\u01cb\u01cc\5")
        buf.write(u"\u00a8U\2\u01cc\u01ce\7\25\2\2\u01cd\u01cf\5\u00b2Z\2")
        buf.write(u"\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0")
        buf.write(u"\3\2\2\2\u01d0\u01d3\7\26\2\2\u01d1\u01d2\7\63\2\2\u01d2")
        buf.write(u"\u01d4\5\u0098M\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2")
        buf.write(u"\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\7\20\2\2\u01d6\u01d7")
        buf.write(u"\5x=\2\u01d7\u01d8\5\u00dco\2\u01d8\u01d9\5z>\2\u01d9")
        buf.write(u"\23\3\2\2\2\u01da\u01db\7O\2\2\u01db\u01dc\7q\2\2\u01dc")
        buf.write(u"\u01dd\5\u0106\u0084\2\u01dd\u01de\7\25\2\2\u01de\u01df")
        buf.write(u"\5\u00b6\\\2\u01df\u01e2\7\26\2\2\u01e0\u01e1\7\63\2")
        buf.write(u"\2\u01e1\u01e3\5\u0098M\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write(u"\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\7\20\2\2\u01e5")
        buf.write(u"\u01e6\5x=\2\u01e6\u01e7\5\u00dco\2\u01e7\u01e8\5z>\2")
        buf.write(u"\u01e8\25\3\2\2\2\u01e9\u01ea\7O\2\2\u01ea\u01eb\5\u00ac")
        buf.write(u"W\2\u01eb\u01ec\7|\2\2\u01ec\u01ed\7\25\2\2\u01ed\u01ee")
        buf.write(u"\7\26\2\2\u01ee\u01ef\7\20\2\2\u01ef\u01f0\5x=\2\u01f0")
        buf.write(u"\u01f1\5\u00dco\2\u01f1\u01f2\5z>\2\u01f2\27\3\2\2\2")
        buf.write(u"\u01f3\u01f4\7O\2\2\u01f4\u01f5\5\u00acW\2\u01f5\u01f6")
        buf.write(u"\7`\2\2\u01f6\u01f7\7\25\2\2\u01f7\u01f8\7\26\2\2\u01f8")
        buf.write(u"\u01f9\7\20\2\2\u01f9\u01fa\5x=\2\u01fa\u01fb\5\u00dc")
        buf.write(u"o\2\u01fb\u01fc\5z>\2\u01fc\31\3\2\2\2\u01fd\u01fe\7")
        buf.write(u"j\2\2\u01fe\u01ff\t\2\2\2\u01ff\u0200\5\u00aeX\2\u0200")
        buf.write(u"\u0202\7\25\2\2\u0201\u0203\5\"\22\2\u0202\u0201\3\2")
        buf.write(u"\2\2\u0202\u0203\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205")
        buf.write(u"\7\26\2\2\u0205\u0206\7\20\2\2\u0206\u0207\5x=\2\u0207")
        buf.write(u"\u0208\5\36\20\2\u0208\u0209\5z>\2\u0209\33\3\2\2\2\u020a")
        buf.write(u"\u020b\7j\2\2\u020b\u020c\7x\2\2\u020c\u020d\5\u00ae")
        buf.write(u"X\2\u020d\u020f\7\25\2\2\u020e\u0210\5\"\22\2\u020f\u020e")
        buf.write(u"\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write(u"\u0212\7\26\2\2\u0212\u0213\7\20\2\2\u0213\u0214\5x=")
        buf.write(u"\2\u0214\u0215\5\36\20\2\u0215\u0216\5z>\2\u0216\35\3")
        buf.write(u"\2\2\2\u0217\u0218\7e\2\2\u0218\u0219\7\20\2\2\u0219")
        buf.write(u"\u021a\5x=\2\u021a\u021b\5 \21\2\u021b\u021c\5z>\2\u021c")
        buf.write(u"\37\3\2\2\2\u021d\u021e\b\21\1\2\u021e\u021f\5\u00c4")
        buf.write(u"c\2\u021f\u0226\3\2\2\2\u0220\u0221\f\3\2\2\u0221\u0222")
        buf.write(u"\5v<\2\u0222\u0223\5\u00c4c\2\u0223\u0225\3\2\2\2\u0224")
        buf.write(u"\u0220\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2")
        buf.write(u"\2\u0226\u0227\3\2\2\2\u0227!\3\2\2\2\u0228\u0226\3\2")
        buf.write(u"\2\2\u0229\u022a\5\u00d0i\2\u022a#\3\2\2\2\u022b\u022c")
        buf.write(u"\7@\2\2\u022c\u022d\7O\2\2\u022d\u022e\5\u00a8U\2\u022e")
        buf.write(u"\u0230\7\25\2\2\u022f\u0231\5\u00b2Z\2\u0230\u022f\3")
        buf.write(u"\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write(u"\u0235\7\26\2\2\u0233\u0234\7\63\2\2\u0234\u0236\5\u0098")
        buf.write(u"M\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236%\3")
        buf.write(u"\2\2\2\u0237\u0238\7O\2\2\u0238\u0239\5\u00a8U\2\u0239")
        buf.write(u"\u023b\7\25\2\2\u023a\u023c\5\u00b2Z\2\u023b\u023a\3")
        buf.write(u"\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\3\2\2\2\u023d")
        buf.write(u"\u0240\7\26\2\2\u023e\u023f\7\63\2\2\u023f\u0241\5\u0098")
        buf.write(u"M\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242")
        buf.write(u"\3\2\2\2\u0242\u0243\7\20\2\2\u0243\u0244\5x=\2\u0244")
        buf.write(u"\u0245\5\u00dco\2\u0245\u0246\5z>\2\u0246\'\3\2\2\2\u0247")
        buf.write(u"\u0248\7O\2\2\u0248\u0249\7j\2\2\u0249\u024a\5\u00a8")
        buf.write(u"U\2\u024a\u024c\7\25\2\2\u024b\u024d\5\u00b2Z\2\u024c")
        buf.write(u"\u024b\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e\3\2\2")
        buf.write(u"\2\u024e\u0251\7\26\2\2\u024f\u0250\7\63\2\2\u0250\u0252")
        buf.write(u"\5\u0098M\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write(u"\u0253\3\2\2\2\u0253\u0254\7\20\2\2\u0254\u0255\5x=\2")
        buf.write(u"\u0255\u0256\5\u00d4k\2\u0256\u0257\5z>\2\u0257)\3\2")
        buf.write(u"\2\2\u0258\u0259\7O\2\2\u0259\u025a\7\u0080\2\2\u025a")
        buf.write(u"\u025b\7\u0091\2\2\u025b\u025c\7\25\2\2\u025c\u025d\7")
        buf.write(u"\26\2\2\u025d\u025e\7\20\2\2\u025e\u025f\5x=\2\u025f")
        buf.write(u"\u0260\5\u00dco\2\u0260\u0261\5z>\2\u0261\u0262\5v<\2")
        buf.write(u"\u0262\u0263\7Z\2\2\u0263\u0269\7\20\2\2\u0264\u0265")
        buf.write(u"\5x=\2\u0265\u0266\5\u00dep\2\u0266\u0267\5z>\2\u0267")
        buf.write(u"\u026a\3\2\2\2\u0268\u026a\5\u00b0Y\2\u0269\u0264\3\2")
        buf.write(u"\2\2\u0269\u0268\3\2\2\2\u026a+\3\2\2\2\u026b\u026c\5")
        buf.write(u"T+\2\u026c-\3\2\2\2\u026d\u026e\5\u00acW\2\u026e\u026f")
        buf.write(u"\7\20\2\2\u026f\u0274\5\u00bc_\2\u0270\u0271\7\25\2\2")
        buf.write(u"\u0271\u0272\5\"\22\2\u0272\u0273\7\26\2\2\u0273\u0275")
        buf.write(u"\3\2\2\2\u0274\u0270\3\2\2\2\u0274\u0275\3\2\2\2\u0275")
        buf.write(u"\u0278\3\2\2\2\u0276\u0277\7-\2\2\u0277\u0279\5\u00f0")
        buf.write(u"y\2\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279/\3")
        buf.write(u"\2\2\2\u027a\u028a\5\62\32\2\u027b\u028a\5n8\2\u027c")
        buf.write(u"\u028a\5r:\2\u027d\u028a\5R*\2\u027e\u028a\5H%\2\u027f")
        buf.write(u"\u028a\5> \2\u0280\u028a\5B\"\2\u0281\u028a\5F$\2\u0282")
        buf.write(u"\u028a\5D#\2\u0283\u028a\5L\'\2\u0284\u028a\5N(\2\u0285")
        buf.write(u"\u028a\5h\65\2\u0286\u028a\5:\36\2\u0287\u028a\5<\37")
        buf.write(u"\2\u0288\u028a\5&\24\2\u0289\u027a\3\2\2\2\u0289\u027b")
        buf.write(u"\3\2\2\2\u0289\u027c\3\2\2\2\u0289\u027d\3\2\2\2\u0289")
        buf.write(u"\u027e\3\2\2\2\u0289\u027f\3\2\2\2\u0289\u0280\3\2\2")
        buf.write(u"\2\u0289\u0281\3\2\2\2\u0289\u0282\3\2\2\2\u0289\u0283")
        buf.write(u"\3\2\2\2\u0289\u0284\3\2\2\2\u0289\u0285\3\2\2\2\u0289")
        buf.write(u"\u0286\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u0288\3\2\2")
        buf.write(u"\2\u028a\61\3\2\2\2\u028b\u028c\5\64\33\2\u028c\u028e")
        buf.write(u"\7\25\2\2\u028d\u028f\5b\62\2\u028e\u028d\3\2\2\2\u028e")
        buf.write(u"\u028f\3\2\2\2\u028f\u0290\3\2\2\2\u0290\u0291\7\26\2")
        buf.write(u"\2\u0291\63\3\2\2\2\u0292\u0298\5\u00a8U\2\u0293\u0294")
        buf.write(u"\5\66\34\2\u0294\u0295\7\24\2\2\u0295\u0296\5\u00a8U")
        buf.write(u"\2\u0296\u0298\3\2\2\2\u0297\u0292\3\2\2\2\u0297\u0293")
        buf.write(u"\3\2\2\2\u0298\65\3\2\2\2\u0299\u029a\b\34\1\2\u029a")
        buf.write(u"\u029b\5\u00aaV\2\u029b\u02a0\3\2\2\2\u029c\u029d\f\3")
        buf.write(u"\2\2\u029d\u029f\58\35\2\u029e\u029c\3\2\2\2\u029f\u02a2")
        buf.write(u"\3\2\2\2\u02a0\u029e\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1")
        buf.write(u"\67\3\2\2\2\u02a2\u02a0\3\2\2\2\u02a3\u02a4\7\24\2\2")
        buf.write(u"\u02a4\u02aa\5\u00acW\2\u02a5\u02a6\7\27\2\2\u02a6\u02a7")
        buf.write(u"\5T+\2\u02a7\u02a8\7\30\2\2\u02a8\u02aa\3\2\2\2\u02a9")
        buf.write(u"\u02a3\3\2\2\2\u02a9\u02a5\3\2\2\2\u02aa9\3\2\2\2\u02ab")
        buf.write(u"\u02ac\7\u0085\2\2\u02ac\u02ad\5\u0100\u0081\2\u02ad")
        buf.write(u"\u02ae\7\20\2\2\u02ae\u02af\5x=\2\u02af\u02b0\5\u00dc")
        buf.write(u"o\2\u02b0\u02b1\5z>\2\u02b1;\3\2\2\2\u02b2\u02b3\7\u0085")
        buf.write(u"\2\2\u02b3\u02b4\5\u00aeX\2\u02b4\u02b5\7\20\2\2\u02b5")
        buf.write(u"\u02b6\5x=\2\u02b6\u02b7\5\u00dco\2\u02b7\u02b8\5z>\2")
        buf.write(u"\u02b8=\3\2\2\2\u02b9\u02ba\7\177\2\2\u02ba\u02bb\7o")
        buf.write(u"\2\2\u02bb\u02bc\5T+\2\u02bc\u02bd\7\20\2\2\u02bd\u02be")
        buf.write(u"\5x=\2\u02be\u02c6\5\u00e0q\2\u02bf\u02c0\5v<\2\u02c0")
        buf.write(u"\u02c1\7s\2\2\u02c1\u02c2\7\20\2\2\u02c2\u02c3\5x=\2")
        buf.write(u"\u02c3\u02c4\5\u00dco\2\u02c4\u02c5\5z>\2\u02c5\u02c7")
        buf.write(u"\3\2\2\2\u02c6\u02bf\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7")
        buf.write(u"\u02c8\3\2\2\2\u02c8\u02c9\5z>\2\u02c9?\3\2\2\2\u02ca")
        buf.write(u"\u02cb\7\u0086\2\2\u02cb\u02cc\5\u00e6t\2\u02cc\u02cd")
        buf.write(u"\7\20\2\2\u02cd\u02ce\5x=\2\u02ce\u02cf\5\u00dco\2\u02cf")
        buf.write(u"\u02d0\5z>\2\u02d0\u02da\3\2\2\2\u02d1\u02d2\7\u0086")
        buf.write(u"\2\2\u02d2\u02d3\7b\2\2\u02d3\u02d4\5\u00e4s\2\u02d4")
        buf.write(u"\u02d5\7\20\2\2\u02d5\u02d6\5x=\2\u02d6\u02d7\5\u00dc")
        buf.write(u"o\2\u02d7\u02d8\5z>\2\u02d8\u02da\3\2\2\2\u02d9\u02ca")
        buf.write(u"\3\2\2\2\u02d9\u02d1\3\2\2\2\u02daA\3\2\2\2\u02db\u02dc")
        buf.write(u"\7^\2\2\u02dc\u02df\5\u00acW\2\u02dd\u02de\7\22\2\2\u02de")
        buf.write(u"\u02e0\5\u00acW\2\u02df\u02dd\3\2\2\2\u02df\u02e0\3\2")
        buf.write(u"\2\2\u02e0\u02e1\3\2\2\2\u02e1\u02e2\7b\2\2\u02e2\u02e3")
        buf.write(u"\5T+\2\u02e3\u02e4\7\20\2\2\u02e4\u02e5\5x=\2\u02e5\u02e6")
        buf.write(u"\5\u00dco\2\u02e6\u02e7\5z>\2\u02e7C\3\2\2\2\u02e8\u02e9")
        buf.write(u"\7R\2\2\u02e9\u02ea\7\20\2\2\u02ea\u02eb\5x=\2\u02eb")
        buf.write(u"\u02ec\5\u00dco\2\u02ec\u02ed\5z>\2\u02ed\u02ee\5v<\2")
        buf.write(u"\u02ee\u02ef\7\u0088\2\2\u02ef\u02f0\5T+\2\u02f0E\3\2")
        buf.write(u"\2\2\u02f1\u02f2\7\u0088\2\2\u02f2\u02f3\5T+\2\u02f3")
        buf.write(u"\u02f4\7\20\2\2\u02f4\u02f5\5x=\2\u02f5\u02f6\5\u00dc")
        buf.write(u"o\2\u02f6\u02f7\5z>\2\u02f7G\3\2\2\2\u02f8\u02f9\7a\2")
        buf.write(u"\2\u02f9\u02fa\5T+\2\u02fa\u02fb\7\20\2\2\u02fb\u02fc")
        buf.write(u"\5x=\2\u02fc\u02fd\5\u00dco\2\u02fd\u0301\5z>\2\u02fe")
        buf.write(u"\u02ff\5v<\2\u02ff\u0300\5J&\2\u0300\u0302\3\2\2\2\u0301")
        buf.write(u"\u02fe\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u030a\3\2\2")
        buf.write(u"\2\u0303\u0304\5v<\2\u0304\u0305\7U\2\2\u0305\u0306\7")
        buf.write(u"\20\2\2\u0306\u0307\5x=\2\u0307\u0308\5\u00dco\2\u0308")
        buf.write(u"\u0309\5z>\2\u0309\u030b\3\2\2\2\u030a\u0303\3\2\2\2")
        buf.write(u"\u030a\u030b\3\2\2\2\u030bI\3\2\2\2\u030c\u030d\b&\1")
        buf.write(u"\2\u030d\u030e\7U\2\2\u030e\u030f\7a\2\2\u030f\u0310")
        buf.write(u"\5T+\2\u0310\u0311\7\20\2\2\u0311\u0312\5x=\2\u0312\u0313")
        buf.write(u"\5\u00dco\2\u0313\u0314\5z>\2\u0314\u0321\3\2\2\2\u0315")
        buf.write(u"\u0316\f\3\2\2\u0316\u0317\5v<\2\u0317\u0318\7U\2\2\u0318")
        buf.write(u"\u0319\7a\2\2\u0319\u031a\5T+\2\u031a\u031b\7\20\2\2")
        buf.write(u"\u031b\u031c\5x=\2\u031c\u031d\5\u00dco\2\u031d\u031e")
        buf.write(u"\5z>\2\u031e\u0320\3\2\2\2\u031f\u0315\3\2\2\2\u0320")
        buf.write(u"\u0323\3\2\2\2\u0321\u031f\3\2\2\2\u0321\u0322\3\2\2")
        buf.write(u"\2\u0322K\3\2\2\2\u0323\u0321\3\2\2\2\u0324\u0325\7u")
        buf.write(u"\2\2\u0325\u0326\5T+\2\u0326M\3\2\2\2\u0327\u0328\7\u0084")
        buf.write(u"\2\2\u0328\u0329\5\u00acW\2\u0329\u032a\7\20\2\2\u032a")
        buf.write(u"\u032b\5x=\2\u032b\u032c\5\u00dco\2\u032c\u032d\5z>\2")
        buf.write(u"\u032d\u032f\5t;\2\u032e\u0330\5\u00e2r\2\u032f\u032e")
        buf.write(u"\3\2\2\2\u032f\u0330\3\2\2\2\u0330\u0338\3\2\2\2\u0331")
        buf.write(u"\u0332\7X\2\2\u0332\u0333\7\20\2\2\u0333\u0334\5x=\2")
        buf.write(u"\u0334\u0335\5\u00dco\2\u0335\u0336\5z>\2\u0336\u0337")
        buf.write(u"\5t;\2\u0337\u0339\3\2\2\2\u0338\u0331\3\2\2\2\u0338")
        buf.write(u"\u0339\3\2\2\2\u0339\u0341\3\2\2\2\u033a\u033b\7]\2\2")
        buf.write(u"\u033b\u033c\7\20\2\2\u033c\u033d\5x=\2\u033d\u033e\5")
        buf.write(u"\u00dco\2\u033e\u033f\5z>\2\u033f\u0340\5t;\2\u0340\u0342")
        buf.write(u"\3\2\2\2\u0341\u033a\3\2\2\2\u0341\u0342\3\2\2\2\u0342")
        buf.write(u"\u0343\3\2\2\2\u0343\u0344\5t;\2\u0344O\3\2\2\2\u0345")
        buf.write(u"\u0346\7X\2\2\u0346\u0347\5\u00b0Y\2\u0347\u0348\7\20")
        buf.write(u"\2\2\u0348\u0349\5x=\2\u0349\u034a\5\u00dco\2\u034a\u034b")
        buf.write(u"\5z>\2\u034b\u034c\5t;\2\u034c\u0359\3\2\2\2\u034d\u034e")
        buf.write(u"\7X\2\2\u034e\u034f\7b\2\2\u034f\u0350\7\27\2\2\u0350")
        buf.write(u"\u0351\5\u008cG\2\u0351\u0352\7\30\2\2\u0352\u0353\7")
        buf.write(u"\20\2\2\u0353\u0354\5x=\2\u0354\u0355\5\u00dco\2\u0355")
        buf.write(u"\u0356\5z>\2\u0356\u0357\5t;\2\u0357\u0359\3\2\2\2\u0358")
        buf.write(u"\u0345\3\2\2\2\u0358\u034d\3\2\2\2\u0359Q\3\2\2\2\u035a")
        buf.write(u"\u035c\7y\2\2\u035b\u035d\5T+\2\u035c\u035b\3\2\2\2\u035c")
        buf.write(u"\u035d\3\2\2\2\u035dS\3\2\2\2\u035e\u035f\b+\1\2\u035f")
        buf.write(u"\u0360\7#\2\2\u0360\u0371\5T+!\u0361\u0362\7l\2\2\u0362")
        buf.write(u"\u0371\5T+ \u0363\u0371\5X-\2\u0364\u0371\5Z.\2\u0365")
        buf.write(u"\u0366\7>\2\2\u0366\u0367\7\25\2\2\u0367\u0368\5T+\2")
        buf.write(u"\u0368\u0369\7\26\2\2\u0369\u0371\3\2\2\2\u036a\u036b")
        buf.write(u"\7Y\2\2\u036b\u036c\7\25\2\2\u036c\u036d\5\u00acW\2\u036d")
        buf.write(u"\u036e\7\26\2\2\u036e\u0371\3\2\2\2\u036f\u0371\5V,\2")
        buf.write(u"\u0370\u035e\3\2\2\2\u0370\u0361\3\2\2\2\u0370\u0363")
        buf.write(u"\3\2\2\2\u0370\u0364\3\2\2\2\u0370\u0365\3\2\2\2\u0370")
        buf.write(u"\u036a\3\2\2\2\u0370\u036f\3\2\2\2\u0371\u03d2\3\2\2")
        buf.write(u"\2\u0372\u0373\f\37\2\2\u0373\u0374\5\u0110\u0089\2\u0374")
        buf.write(u"\u0375\5T+ \u0375\u03d1\3\2\2\2\u0376\u0377\f\36\2\2")
        buf.write(u"\u0377\u0378\5\u0112\u008a\2\u0378\u0379\5T+\37\u0379")
        buf.write(u"\u03d1\3\2\2\2\u037a\u037b\f\35\2\2\u037b\u037c\5\u0116")
        buf.write(u"\u008c\2\u037c\u037d\5T+\36\u037d\u03d1\3\2\2\2\u037e")
        buf.write(u"\u037f\f\34\2\2\u037f\u0380\5\u0114\u008b\2\u0380\u0381")
        buf.write(u"\5T+\35\u0381\u03d1\3\2\2\2\u0382\u0383\f\33\2\2\u0383")
        buf.write(u"\u0384\t\3\2\2\u0384\u03d1\5T+\34\u0385\u0386\f\32\2")
        buf.write(u"\2\u0386\u0387\7*\2\2\u0387\u03d1\5T+\33\u0388\u0389")
        buf.write(u"\f\31\2\2\u0389\u038a\7+\2\2\u038a\u03d1\5T+\32\u038b")
        buf.write(u"\u038c\f\30\2\2\u038c\u038d\7(\2\2\u038d\u03d1\5T+\31")
        buf.write(u"\u038e\u038f\f\27\2\2\u038f\u0390\7)\2\2\u0390\u03d1")
        buf.write(u"\5T+\30\u0391\u0392\f\24\2\2\u0392\u0393\7/\2\2\u0393")
        buf.write(u"\u03d1\5T+\25\u0394\u0395\f\23\2\2\u0395\u0396\7.\2\2")
        buf.write(u"\u0396\u03d1\5T+\24\u0397\u0398\f\22\2\2\u0398\u0399")
        buf.write(u"\7\60\2\2\u0399\u03d1\5T+\23\u039a\u039b\f\21\2\2\u039b")
        buf.write(u"\u039c\7r\2\2\u039c\u03d1\5T+\22\u039d\u039e\f\20\2\2")
        buf.write(u"\u039e\u039f\7C\2\2\u039f\u03d1\5T+\21\u03a0\u03a1\f")
        buf.write(u"\17\2\2\u03a1\u03a2\7a\2\2\u03a2\u03a3\5T+\2\u03a3\u03a4")
        buf.write(u"\7U\2\2\u03a4\u03a5\5T+\20\u03a5\u03d1\3\2\2\2\u03a6")
        buf.write(u"\u03a7\f\r\2\2\u03a7\u03a8\7b\2\2\u03a8\u03d1\5T+\16")
        buf.write(u"\u03a9\u03aa\f\f\2\2\u03aa\u03ab\7N\2\2\u03ab\u03d1\5")
        buf.write(u"T+\r\u03ac\u03ad\f\13\2\2\u03ad\u03ae\7N\2\2\u03ae\u03af")
        buf.write(u"\7A\2\2\u03af\u03d1\5T+\f\u03b0\u03b1\f\n\2\2\u03b1\u03b2")
        buf.write(u"\7N\2\2\u03b2\u03b3\7D\2\2\u03b3\u03d1\5T+\13\u03b4\u03b5")
        buf.write(u"\f\t\2\2\u03b5\u03b6\7l\2\2\u03b6\u03b7\7b\2\2\u03b7")
        buf.write(u"\u03d1\5T+\n\u03b8\u03b9\f\b\2\2\u03b9\u03ba\7l\2\2\u03ba")
        buf.write(u"\u03bb\7N\2\2\u03bb\u03d1\5T+\t\u03bc\u03bd\f\7\2\2\u03bd")
        buf.write(u"\u03be\7l\2\2\u03be\u03bf\7N\2\2\u03bf\u03c0\7A\2\2\u03c0")
        buf.write(u"\u03d1\5T+\b\u03c1\u03c2\f\6\2\2\u03c2\u03c3\7l\2\2\u03c3")
        buf.write(u"\u03c4\7N\2\2\u03c4\u03c5\7D\2\2\u03c5\u03d1\5T+\7\u03c6")
        buf.write(u"\u03c7\f\26\2\2\u03c7\u03c8\7d\2\2\u03c8\u03c9\7l\2\2")
        buf.write(u"\u03c9\u03d1\5\u0104\u0083\2\u03ca\u03cb\f\25\2\2\u03cb")
        buf.write(u"\u03cc\7d\2\2\u03cc\u03d1\5\u0104\u0083\2\u03cd\u03ce")
        buf.write(u"\f\16\2\2\u03ce\u03cf\7E\2\2\u03cf\u03d1\5\u00bc_\2\u03d0")
        buf.write(u"\u0372\3\2\2\2\u03d0\u0376\3\2\2\2\u03d0\u037a\3\2\2")
        buf.write(u"\2\u03d0\u037e\3\2\2\2\u03d0\u0382\3\2\2\2\u03d0\u0385")
        buf.write(u"\3\2\2\2\u03d0\u0388\3\2\2\2\u03d0\u038b\3\2\2\2\u03d0")
        buf.write(u"\u038e\3\2\2\2\u03d0\u0391\3\2\2\2\u03d0\u0394\3\2\2")
        buf.write(u"\2\u03d0\u0397\3\2\2\2\u03d0\u039a\3\2\2\2\u03d0\u039d")
        buf.write(u"\3\2\2\2\u03d0\u03a0\3\2\2\2\u03d0\u03a6\3\2\2\2\u03d0")
        buf.write(u"\u03a9\3\2\2\2\u03d0\u03ac\3\2\2\2\u03d0\u03b0\3\2\2")
        buf.write(u"\2\u03d0\u03b4\3\2\2\2\u03d0\u03b8\3\2\2\2\u03d0\u03bc")
        buf.write(u"\3\2\2\2\u03d0\u03c1\3\2\2\2\u03d0\u03c6\3\2\2\2\u03d0")
        buf.write(u"\u03ca\3\2\2\2\u03d0\u03cd\3\2\2\2\u03d1\u03d4\3\2\2")
        buf.write(u"\2\u03d2\u03d0\3\2\2\2\u03d2\u03d3\3\2\2\2\u03d3U\3\2")
        buf.write(u"\2\2\u03d4\u03d2\3\2\2\2\u03d5\u03d6\5\u00aeX\2\u03d6")
        buf.write(u"W\3\2\2\2\u03d7\u03d8\b-\1\2\u03d8\u03d9\5\u00eav\2\u03d9")
        buf.write(u"\u03de\3\2\2\2\u03da\u03db\f\3\2\2\u03db\u03dd\5\\/\2")
        buf.write(u"\u03dc\u03da\3\2\2\2\u03dd\u03e0\3\2\2\2\u03de\u03dc")
        buf.write(u"\3\2\2\2\u03de\u03df\3\2\2\2\u03dfY\3\2\2\2\u03e0\u03de")
        buf.write(u"\3\2\2\2\u03e1\u03e8\5^\60\2\u03e2\u03e8\5j\66\2\u03e3")
        buf.write(u"\u03e8\5f\64\2\u03e4\u03e8\5l\67\2\u03e5\u03e8\5\62\32")
        buf.write(u"\2\u03e6\u03e8\5`\61\2\u03e7\u03e1\3\2\2\2\u03e7\u03e2")
        buf.write(u"\3\2\2\2\u03e7\u03e3\3\2\2\2\u03e7\u03e4\3\2\2\2\u03e7")
        buf.write(u"\u03e5\3\2\2\2\u03e7\u03e6\3\2\2\2\u03e8[\3\2\2\2\u03e9")
        buf.write(u"\u03ea\6/ \3\u03ea\u03eb\7\24\2\2\u03eb\u03f7\5\u00ac")
        buf.write(u"W\2\u03ec\u03ed\6/!\3\u03ed\u03ee\7\27\2\2\u03ee\u03ef")
        buf.write(u"\5\u00fe\u0080\2\u03ef\u03f0\7\30\2\2\u03f0\u03f7\3\2")
        buf.write(u"\2\2\u03f1\u03f2\6/\"\3\u03f2\u03f3\7\27\2\2\u03f3\u03f4")
        buf.write(u"\5T+\2\u03f4\u03f5\7\30\2\2\u03f5\u03f7\3\2\2\2\u03f6")
        buf.write(u"\u03e9\3\2\2\2\u03f6\u03ec\3\2\2\2\u03f6\u03f1\3\2\2")
        buf.write(u"\2\u03f7]\3\2\2\2\u03f8\u03f9\5\u00a2R\2\u03f9_\3\2\2")
        buf.write(u"\2\u03fa\u03fb\5\u009eP\2\u03fb\u03fd\7\25\2\2\u03fc")
        buf.write(u"\u03fe\5b\62\2\u03fd\u03fc\3\2\2\2\u03fd\u03fe\3\2\2")
        buf.write(u"\2\u03fe\u03ff\3\2\2\2\u03ff\u0400\7\26\2\2\u0400a\3")
        buf.write(u"\2\2\2\u0401\u0402\b\62\1\2\u0402\u0403\5T+\2\u0403\u0404")
        buf.write(u"\6\62#\3\u0404\u0407\3\2\2\2\u0405\u0407\5d\63\2\u0406")
        buf.write(u"\u0401\3\2\2\2\u0406\u0405\3\2\2\2\u0407\u040d\3\2\2")
        buf.write(u"\2\u0408\u0409\f\3\2\2\u0409\u040a\7\22\2\2\u040a\u040c")
        buf.write(u"\5d\63\2\u040b\u0408\3\2\2\2\u040c\u040f\3\2\2\2\u040d")
        buf.write(u"\u040b\3\2\2\2\u040d\u040e\3\2\2\2\u040ec\3\2\2\2\u040f")
        buf.write(u"\u040d\3\2\2\2\u0410\u0411\5\u00acW\2\u0411\u0412\5\u010e")
        buf.write(u"\u0088\2\u0412\u0413\5T+\2\u0413e\3\2\2\2\u0414\u0415")
        buf.write(u"\7v\2\2\u0415\u0416\7_\2\2\u0416\u0417\5T+\2\u0417g\3")
        buf.write(u"\2\2\2\u0418\u0419\7\u0089\2\2\u0419\u041a\5T+\2\u041a")
        buf.write(u"\u041b\7\u0083\2\2\u041b\u041c\5T+\2\u041ci\3\2\2\2\u041d")
        buf.write(u"\u041e\7\\\2\2\u041e\u041f\5\u00acW\2\u041f\u0420\7_")
        buf.write(u"\2\2\u0420\u0421\5T+\2\u0421\u0422\7\u0087\2\2\u0422")
        buf.write(u"\u0423\5T+\2\u0423k\3\2\2\2\u0424\u0425\7~\2\2\u0425")
        buf.write(u"\u0426\7\25\2\2\u0426\u042c\5X-\2\u0427\u0428\7\22\2")
        buf.write(u"\2\u0428\u0429\5\u0108\u0085\2\u0429\u042a\7-\2\2\u042a")
        buf.write(u"\u042b\5X-\2\u042b\u042d\3\2\2\2\u042c\u0427\3\2\2\2")
        buf.write(u"\u042c\u042d\3\2\2\2\u042d\u042e\3\2\2\2\u042e\u042f")
        buf.write(u"\7\26\2\2\u042fm\3\2\2\2\u0430\u0431\5\u0102\u0082\2")
        buf.write(u"\u0431\u0432\5\u010e\u0088\2\u0432\u0433\5T+\2\u0433")
        buf.write(u"o\3\2\2\2\u0434\u0435\69%\3\u0435\u0436\7\24\2\2\u0436")
        buf.write(u"\u043d\5\u00acW\2\u0437\u0438\69&\3\u0438\u0439\7\27")
        buf.write(u"\2\2\u0439\u043a\5T+\2\u043a\u043b\7\30\2\2\u043b\u043d")
        buf.write(u"\3\2\2\2\u043c\u0434\3\2\2\2\u043c\u0437\3\2\2\2\u043d")
        buf.write(u"q\3\2\2\2\u043e\u043f\5\u00d0i\2\u043f\u0440\5\u010e")
        buf.write(u"\u0088\2\u0440\u0441\5T+\2\u0441s\3\2\2\2\u0442\u0444")
        buf.write(u"\7\7\2\2\u0443\u0442\3\2\2\2\u0444\u0447\3\2\2\2\u0445")
        buf.write(u"\u0443\3\2\2\2\u0445\u0446\3\2\2\2\u0446u\3\2\2\2\u0447")
        buf.write(u"\u0445\3\2\2\2\u0448\u044a\7\7\2\2\u0449\u0448\3\2\2")
        buf.write(u"\2\u044a\u044b\3\2\2\2\u044b\u0449\3\2\2\2\u044b\u044c")
        buf.write(u"\3\2\2\2\u044cw\3\2\2\2\u044d\u044f\7\7\2\2\u044e\u044d")
        buf.write(u"\3\2\2\2\u044f\u0450\3\2\2\2\u0450\u044e\3\2\2\2\u0450")
        buf.write(u"\u0451\3\2\2\2\u0451\u0452\3\2\2\2\u0452\u0453\7\3\2")
        buf.write(u"\2\u0453y\3\2\2\2\u0454\u0456\7\7\2\2\u0455\u0454\3\2")
        buf.write(u"\2\2\u0456\u0459\3\2\2\2\u0457\u0455\3\2\2\2\u0457\u0458")
        buf.write(u"\3\2\2\2\u0458\u045a\3\2\2\2\u0459\u0457\3\2\2\2\u045a")
        buf.write(u"\u045b\7\4\2\2\u045b{\3\2\2\2\u045c\u045d\7k\2\2\u045d")
        buf.write(u"}\3\2\2\2\u045e\u0460\5\u0080A\2\u045f\u045e\3\2\2\2")
        buf.write(u"\u045f\u0460\3\2\2\2\u0460\u0461\3\2\2\2\u0461\u0462")
        buf.write(u"\5t;\2\u0462\u0463\7\2\2\3\u0463\177\3\2\2\2\u0464\u0465")
        buf.write(u"\bA\1\2\u0465\u0466\5\u0082B\2\u0466\u046d\3\2\2\2\u0467")
        buf.write(u"\u0468\f\3\2\2\u0468\u0469\5v<\2\u0469\u046a\5\u0082")
        buf.write(u"B\2\u046a\u046c\3\2\2\2\u046b\u0467\3\2\2\2\u046c\u046f")
        buf.write(u"\3\2\2\2\u046d\u046b\3\2\2\2\u046d\u046e\3\2\2\2\u046e")
        buf.write(u"\u0081\3\2\2\2\u046f\u046d\3\2\2\2\u0470\u0476\5\n\6")
        buf.write(u"\2\u0471\u0476\5\u00a4S\2\u0472\u0476\5\u0084C\2\u0473")
        buf.write(u"\u0476\5\u0086D\2\u0474\u0476\5\u00d2j\2\u0475\u0470")
        buf.write(u"\3\2\2\2\u0475\u0471\3\2\2\2\u0475\u0472\3\2\2\2\u0475")
        buf.write(u"\u0473\3\2\2\2\u0475\u0474\3\2\2\2\u0476\u0083\3\2\2")
        buf.write(u"\2\u0477\u0478\5\34\17\2\u0478\u0085\3\2\2\2\u0479\u047c")
        buf.write(u"\5\2\2\2\u047a\u047c\5\4\3\2\u047b\u0479\3\2\2\2\u047b")
        buf.write(u"\u047a\3\2\2\2\u047c\u0087\3\2\2\2\u047d\u047e\bE\1\2")
        buf.write(u"\u047e\u047f\5\6\4\2\u047f\u0486\3\2\2\2\u0480\u0481")
        buf.write(u"\f\3\2\2\u0481\u0482\5v<\2\u0482\u0483\5\6\4\2\u0483")
        buf.write(u"\u0485\3\2\2\2\u0484\u0480\3\2\2\2\u0485\u0488\3\2\2")
        buf.write(u"\2\u0486\u0484\3\2\2\2\u0486\u0487\3\2\2\2\u0487\u0089")
        buf.write(u"\3\2\2\2\u0488\u0486\3\2\2\2\u0489\u048a\bF\1\2\u048a")
        buf.write(u"\u048b\5\b\5\2\u048b\u0492\3\2\2\2\u048c\u048d\f\3\2")
        buf.write(u"\2\u048d\u048e\5v<\2\u048e\u048f\5\b\5\2\u048f\u0491")
        buf.write(u"\3\2\2\2\u0490\u048c\3\2\2\2\u0491\u0494\3\2\2\2\u0492")
        buf.write(u"\u0490\3\2\2\2\u0492\u0493\3\2\2\2\u0493\u008b\3\2\2")
        buf.write(u"\2\u0494\u0492\3\2\2\2\u0495\u0496\bG\1\2\u0496\u0497")
        buf.write(u"\5\u00b0Y\2\u0497\u049d\3\2\2\2\u0498\u0499\f\3\2\2\u0499")
        buf.write(u"\u049a\7\22\2\2\u049a\u049c\5\u00b0Y\2\u049b\u0498\3")
        buf.write(u"\2\2\2\u049c\u049f\3\2\2\2\u049d\u049b\3\2\2\2\u049d")
        buf.write(u"\u049e\3\2\2\2\u049e\u008d\3\2\2\2\u049f\u049d\3\2\2")
        buf.write(u"\2\u04a0\u04a1\7b\2\2\u04a1\u04ab\5\u0090I\2\u04a2\u04a3")
        buf.write(u"\7b\2\2\u04a3\u04ab\5\u0092J\2\u04a4\u04a5\7b\2\2\u04a5")
        buf.write(u"\u04ab\5\u0096L\2\u04a6\u04a7\7f\2\2\u04a7\u04ab\7\u0091")
        buf.write(u"\2\2\u04a8\u04a9\7f\2\2\u04a9\u04ab\5T+\2\u04aa\u04a0")
        buf.write(u"\3\2\2\2\u04aa\u04a2\3\2\2\2\u04aa\u04a4\3\2\2\2\u04aa")
        buf.write(u"\u04a6\3\2\2\2\u04aa\u04a8\3\2\2\2\u04ab\u008f\3\2\2")
        buf.write(u"\2\u04ac\u04ae\7\27\2\2\u04ad\u04af\5\u0094K\2\u04ae")
        buf.write(u"\u04ad\3\2\2\2\u04ae\u04af\3\2\2\2\u04af\u04b0\3\2\2")
        buf.write(u"\2\u04b0\u04b1\7\30\2\2\u04b1\u0091\3\2\2\2\u04b2\u04b4")
        buf.write(u"\7*\2\2\u04b3\u04b5\5\u0094K\2\u04b4\u04b3\3\2\2\2\u04b4")
        buf.write(u"\u04b5\3\2\2\2\u04b5\u04b6\3\2\2\2\u04b6\u04b7\7(\2\2")
        buf.write(u"\u04b7\u0093\3\2\2\2\u04b8\u04b9\bK\1\2\u04b9\u04ba\5")
        buf.write(u"T+\2\u04ba\u04c0\3\2\2\2\u04bb\u04bc\f\3\2\2\u04bc\u04bd")
        buf.write(u"\7\22\2\2\u04bd\u04bf\5T+\2\u04be\u04bb\3\2\2\2\u04bf")
        buf.write(u"\u04c2\3\2\2\2\u04c0\u04be\3\2\2\2\u04c0\u04c1\3\2\2")
        buf.write(u"\2\u04c1\u0095\3\2\2\2\u04c2\u04c0\3\2\2\2\u04c3\u04c4")
        buf.write(u"\7\27\2\2\u04c4\u04c5\5T+\2\u04c5\u04c6\7\23\2\2\u04c6")
        buf.write(u"\u04c7\5T+\2\u04c7\u04c8\7\30\2\2\u04c8\u0097\3\2\2\2")
        buf.write(u"\u04c9\u04ca\bM\1\2\u04ca\u04cb\5\u009aN\2\u04cb\u04d6")
        buf.write(u"\3\2\2\2\u04cc\u04cd\f\5\2\2\u04cd\u04d5\7,\2\2\u04ce")
        buf.write(u"\u04cf\f\4\2\2\u04cf\u04d0\7\27\2\2\u04d0\u04d5\7\30")
        buf.write(u"\2\2\u04d1\u04d2\f\3\2\2\u04d2\u04d3\7\31\2\2\u04d3\u04d5")
        buf.write(u"\7\32\2\2\u04d4\u04cc\3\2\2\2\u04d4\u04ce\3\2\2\2\u04d4")
        buf.write(u"\u04d1\3\2\2\2\u04d5\u04d8\3\2\2\2\u04d6\u04d4\3\2\2")
        buf.write(u"\2\u04d6\u04d7\3\2\2\2\u04d7\u0099\3\2\2\2\u04d8\u04d6")
        buf.write(u"\3\2\2\2\u04d9\u04dc\5\u009cO\2\u04da\u04dc\5\u009eP")
        buf.write(u"\2\u04db\u04d9\3\2\2\2\u04db\u04da\3\2\2\2\u04dc\u009b")
        buf.write(u"\3\2\2\2\u04dd\u04e8\7\64\2\2\u04de\u04e8\7\65\2\2\u04df")
        buf.write(u"\u04e8\7\66\2\2\u04e0\u04e8\7\67\2\2\u04e1\u04e8\78\2")
        buf.write(u"\2\u04e2\u04e8\79\2\2\u04e3\u04e8\7;\2\2\u04e4\u04e8")
        buf.write(u"\7:\2\2\u04e5\u04e8\7<\2\2\u04e6\u04e8\7>\2\2\u04e7\u04dd")
        buf.write(u"\3\2\2\2\u04e7\u04de\3\2\2\2\u04e7\u04df\3\2\2\2\u04e7")
        buf.write(u"\u04e0\3\2\2\2\u04e7\u04e1\3\2\2\2\u04e7\u04e2\3\2\2")
        buf.write(u"\2\u04e7\u04e3\3\2\2\2\u04e7\u04e4\3\2\2\2\u04e7\u04e5")
        buf.write(u"\3\2\2\2\u04e7\u04e6\3\2\2\2\u04e8\u009d\3\2\2\2\u04e9")
        buf.write(u"\u04ea\7\u008f\2\2\u04ea\u009f\3\2\2\2\u04eb\u04ec\7")
        buf.write(u">\2\2\u04ec\u00a1\3\2\2\2\u04ed\u04ee\7?\2\2\u04ee\u00a3")
        buf.write(u"\3\2\2\2\u04ef\u04f3\5\f\7\2\u04f0\u04f3\5\32\16\2\u04f1")
        buf.write(u"\u04f3\5\16\b\2\u04f2\u04ef\3\2\2\2\u04f2\u04f0\3\2\2")
        buf.write(u"\2\u04f2\u04f1\3\2\2\2\u04f3\u00a5\3\2\2\2\u04f4\u04f5")
        buf.write(u"\bT\1\2\u04f5\u04f6\5\u00aeX\2\u04f6\u04fc\3\2\2\2\u04f7")
        buf.write(u"\u04f8\f\3\2\2\u04f8\u04f9\7\22\2\2\u04f9\u04fb\5\u00ae")
        buf.write(u"X\2\u04fa\u04f7\3\2\2\2\u04fb\u04fe\3\2\2\2\u04fc\u04fa")
        buf.write(u"\3\2\2\2\u04fc\u04fd\3\2\2\2\u04fd\u00a7\3\2\2\2\u04fe")
        buf.write(u"\u04fc\3\2\2\2\u04ff\u0502\5\u00acW\2\u0500\u0502\5\u00ae")
        buf.write(u"X\2\u0501\u04ff\3\2\2\2\u0501\u0500\3\2\2\2\u0502\u00a9")
        buf.write(u"\3\2\2\2\u0503\u0507\5\u00acW\2\u0504\u0507\5\u00aeX")
        buf.write(u"\2\u0505\u0507\5\u00b0Y\2\u0506\u0503\3\2\2\2\u0506\u0504")
        buf.write(u"\3\2\2\2\u0506\u0505\3\2\2\2\u0507\u00ab\3\2\2\2\u0508")
        buf.write(u"\u0509\7\u0090\2\2\u0509\u00ad\3\2\2\2\u050a\u050b\7")
        buf.write(u"\u008f\2\2\u050b\u00af\3\2\2\2\u050c\u050d\7\u008e\2")
        buf.write(u"\2\u050d\u00b1\3\2\2\2\u050e\u050f\bZ\1\2\u050f\u0510")
        buf.write(u"\5\u00b4[\2\u0510\u0516\3\2\2\2\u0511\u0512\f\3\2\2\u0512")
        buf.write(u"\u0513\7\22\2\2\u0513\u0515\5\u00b4[\2\u0514\u0511\3")
        buf.write(u"\2\2\2\u0515\u0518\3\2\2\2\u0516\u0514\3\2\2\2\u0516")
        buf.write(u"\u0517\3\2\2\2\u0517\u00b3\3\2\2\2\u0518\u0516\3\2\2")
        buf.write(u"\2\u0519\u051c\5\u00ba^\2\u051a\u051c\5\u00b6\\\2\u051b")
        buf.write(u"\u0519\3\2\2\2\u051b\u051a\3\2\2\2\u051c\u00b5\3\2\2")
        buf.write(u"\2\u051d\u0520\5\u00b8]\2\u051e\u0520\5.\30\2\u051f\u051d")
        buf.write(u"\3\2\2\2\u051f\u051e\3\2\2\2\u0520\u00b7\3\2\2\2\u0521")
        buf.write(u"\u0524\5\u00acW\2\u0522\u0523\7-\2\2\u0523\u0525\5\u00f0")
        buf.write(u"y\2\u0524\u0522\3\2\2\2\u0524\u0525\3\2\2\2\u0525\u00b9")
        buf.write(u"\3\2\2\2\u0526\u0527\5\u00a0Q\2\u0527\u0528\5\u00acW")
        buf.write(u"\2\u0528\u00bb\3\2\2\2\u0529\u052c\5\u0098M\2\u052a\u052c")
        buf.write(u"\5\u00be`\2\u052b\u0529\3\2\2\2\u052b\u052a\3\2\2\2\u052c")
        buf.write(u"\u00bd\3\2\2\2\u052d\u052e\b`\1\2\u052e\u052f\7D\2\2")
        buf.write(u"\u052f\u0538\3\2\2\2\u0530\u0531\f\4\2\2\u0531\u0532")
        buf.write(u"\7\27\2\2\u0532\u0537\7\30\2\2\u0533\u0534\f\3\2\2\u0534")
        buf.write(u"\u0535\7\31\2\2\u0535\u0537\7\32\2\2\u0536\u0530\3\2")
        buf.write(u"\2\2\u0536\u0533\3\2\2\2\u0537\u053a\3\2\2\2\u0538\u0536")
        buf.write(u"\3\2\2\2\u0538\u0539\3\2\2\2\u0539\u00bf\3\2\2\2\u053a")
        buf.write(u"\u0538\3\2\2\2\u053b\u053c\ba\1\2\u053c\u053d\5\u00c2")
        buf.write(u"b\2\u053d\u0544\3\2\2\2\u053e\u053f\f\3\2\2\u053f\u0540")
        buf.write(u"\5v<\2\u0540\u0541\5\u00c2b\2\u0541\u0543\3\2\2\2\u0542")
        buf.write(u"\u053e\3\2\2\2\u0543\u0546\3\2\2\2\u0544\u0542\3\2\2")
        buf.write(u"\2\u0544\u0545\3\2\2\2\u0545\u00c1\3\2\2\2\u0546\u0544")
        buf.write(u"\3\2\2\2\u0547\u054c\5\26\f\2\u0548\u054c\5\30\r\2\u0549")
        buf.write(u"\u054c\5\22\n\2\u054a\u054c\5\24\13\2\u054b\u0547\3\2")
        buf.write(u"\2\2\u054b\u0548\3\2\2\2\u054b\u0549\3\2\2\2\u054b\u054a")
        buf.write(u"\3\2\2\2\u054c\u00c3\3\2\2\2\u054d\u054e\7\n\2\2\u054e")
        buf.write(u"\u0558\5\u0158\u00ad\2\u054f\u0550\7\13\2\2\u0550\u0558")
        buf.write(u"\5\u016e\u00b8\2\u0551\u0552\7\f\2\2\u0552\u0558\5\u00c6")
        buf.write(u"d\2\u0553\u0554\7\r\2\2\u0554\u0558\5\u00c6d\2\u0555")
        buf.write(u"\u0556\7\16\2\2\u0556\u0558\5\u00ccg\2\u0557\u054d\3")
        buf.write(u"\2\2\2\u0557\u054f\3\2\2\2\u0557\u0551\3\2\2\2\u0557")
        buf.write(u"\u0553\3\2\2\2\u0557\u0555\3\2\2\2\u0558\u00c5\3\2\2")
        buf.write(u"\2\u0559\u055b\5\u00aaV\2\u055a\u055c\5\u00c8e\2\u055b")
        buf.write(u"\u055a\3\2\2\2\u055b\u055c\3\2\2\2\u055c\u00c7\3\2\2")
        buf.write(u"\2\u055d\u055e\7_\2\2\u055e\u055f\5\u00caf\2\u055f\u0560")
        buf.write(u"\7\20\2\2\u0560\u0565\5\u00aaV\2\u0561\u0562\7\24\2\2")
        buf.write(u"\u0562\u0564\5\u00aaV\2\u0563\u0561\3\2\2\2\u0564\u0567")
        buf.write(u"\3\2\2\2\u0565\u0563\3\2\2\2\u0565\u0566\3\2\2\2\u0566")
        buf.write(u"\u00c9\3\2\2\2\u0567\u0565\3\2\2\2\u0568\u0569\7\u0090")
        buf.write(u"\2\2\u0569\u056a\6f\64\3\u056a\u00cb\3\2\2\2\u056b\u056d")
        buf.write(u"\5\u00aaV\2\u056c\u056e\5\u00ceh\2\u056d\u056c\3\2\2")
        buf.write(u"\2\u056d\u056e\3\2\2\2\u056e\u00cd\3\2\2\2\u056f\u0570")
        buf.write(u"\7_\2\2\u0570\u0571\5\u00caf\2\u0571\u0573\7\20\2\2\u0572")
        buf.write(u"\u0574\7%\2\2\u0573\u0572\3\2\2\2\u0573\u0574\3\2\2\2")
        buf.write(u"\u0574\u0575\3\2\2\2\u0575\u057a\5\u012c\u0097\2\u0576")
        buf.write(u"\u0577\7%\2\2\u0577\u0579\5\u012c\u0097\2\u0578\u0576")
        buf.write(u"\3\2\2\2\u0579\u057c\3\2\2\2\u057a\u0578\3\2\2\2\u057a")
        buf.write(u"\u057b\3\2\2\2\u057b\u057f\3\2\2\2\u057c\u057a\3\2\2")
        buf.write(u"\2\u057d\u057e\7\24\2\2\u057e\u0580\5\u012c\u0097\2\u057f")
        buf.write(u"\u057d\3\2\2\2\u057f\u0580\3\2\2\2\u0580\u00cf\3\2\2")
        buf.write(u"\2\u0581\u0582\bi\1\2\u0582\u0583\5\u00acW\2\u0583\u0589")
        buf.write(u"\3\2\2\2\u0584\u0585\f\3\2\2\u0585\u0586\7\22\2\2\u0586")
        buf.write(u"\u0588\5\u00acW\2\u0587\u0584\3\2\2\2\u0588\u058b\3\2")
        buf.write(u"\2\2\u0589\u0587\3\2\2\2\u0589\u058a\3\2\2\2\u058a\u00d1")
        buf.write(u"\3\2\2\2\u058b\u0589\3\2\2\2\u058c\u0591\5$\23\2\u058d")
        buf.write(u"\u0591\5&\24\2\u058e\u0591\5(\25\2\u058f\u0591\5*\26")
        buf.write(u"\2\u0590\u058c\3\2\2\2\u0590\u058d\3\2\2\2\u0590\u058e")
        buf.write(u"\3\2\2\2\u0590\u058f\3\2\2\2\u0591\u00d3\3\2\2\2\u0592")
        buf.write(u"\u0593\bk\1\2\u0593\u0594\5\u00d6l\2\u0594\u059b\3\2")
        buf.write(u"\2\2\u0595\u0596\f\3\2\2\u0596\u0597\5v<\2\u0597\u0598")
        buf.write(u"\5\u00d6l\2\u0598\u059a\3\2\2\2\u0599\u0595\3\2\2\2\u059a")
        buf.write(u"\u059d\3\2\2\2\u059b\u0599\3\2\2\2\u059b\u059c\3\2\2")
        buf.write(u"\2\u059c\u00d5\3\2\2\2\u059d\u059b\3\2\2\2\u059e\u059f")
        buf.write(u"\7\n\2\2\u059f\u05a9\5\u0146\u00a4\2\u05a0\u05a1\7\13")
        buf.write(u"\2\2\u05a1\u05a9\5\u015e\u00b0\2\u05a2\u05a3\7\f\2\2")
        buf.write(u"\u05a3\u05a9\5\u00d8m\2\u05a4\u05a5\7\r\2\2\u05a5\u05a9")
        buf.write(u"\5\u00d8m\2\u05a6\u05a7\7\16\2\2\u05a7\u05a9\5\u00da")
        buf.write(u"n\2\u05a8\u059e\3\2\2\2\u05a8\u05a0\3\2\2\2\u05a8\u05a2")
        buf.write(u"\3\2\2\2\u05a8\u05a4\3\2\2\2\u05a8\u05a6\3\2\2\2\u05a9")
        buf.write(u"\u00d7\3\2\2\2\u05aa\u05ac\5\u012e\u0098\2\u05ab\u05ad")
        buf.write(u"\7\21\2\2\u05ac\u05ab\3\2\2\2\u05ac\u05ad\3\2\2\2\u05ad")
        buf.write(u"\u05af\3\2\2\2\u05ae\u05b0\5\u00c8e\2\u05af\u05ae\3\2")
        buf.write(u"\2\2\u05af\u05b0\3\2\2\2\u05b0\u00d9\3\2\2\2\u05b1\u05b3")
        buf.write(u"\5\u0118\u008d\2\u05b2\u05b4\7\21\2\2\u05b3\u05b2\3\2")
        buf.write(u"\2\2\u05b3\u05b4\3\2\2\2\u05b4\u05b6\3\2\2\2\u05b5\u05b7")
        buf.write(u"\5\u00ceh\2\u05b6\u05b5\3\2\2\2\u05b6\u05b7\3\2\2\2\u05b7")
        buf.write(u"\u00db\3\2\2\2\u05b8\u05b9\bo\1\2\u05b9\u05ba\5\60\31")
        buf.write(u"\2\u05ba\u05c1\3\2\2\2\u05bb\u05bc\f\3\2\2\u05bc\u05bd")
        buf.write(u"\5v<\2\u05bd\u05be\5\60\31\2\u05be\u05c0\3\2\2\2\u05bf")
        buf.write(u"\u05bb\3\2\2\2\u05c0\u05c3\3\2\2\2\u05c1\u05bf\3\2\2")
        buf.write(u"\2\u05c1\u05c2\3\2\2\2\u05c2\u00dd\3\2\2\2\u05c3\u05c1")
        buf.write(u"\3\2\2\2\u05c4\u05c5\bp\1\2\u05c5\u05c6\5,\27\2\u05c6")
        buf.write(u"\u05cd\3\2\2\2\u05c7\u05c8\f\3\2\2\u05c8\u05c9\5v<\2")
        buf.write(u"\u05c9\u05ca\5,\27\2\u05ca\u05cc\3\2\2\2\u05cb\u05c7")
        buf.write(u"\3\2\2\2\u05cc\u05cf\3\2\2\2\u05cd\u05cb\3\2\2\2\u05cd")
        buf.write(u"\u05ce\3\2\2\2\u05ce\u00df\3\2\2\2\u05cf\u05cd\3\2\2")
        buf.write(u"\2\u05d0\u05d1\bq\1\2\u05d1\u05d2\5@!\2\u05d2\u05d9\3")
        buf.write(u"\2\2\2\u05d3\u05d4\f\3\2\2\u05d4\u05d5\5v<\2\u05d5\u05d6")
        buf.write(u"\5@!\2\u05d6\u05d8\3\2\2\2\u05d7\u05d3\3\2\2\2\u05d8")
        buf.write(u"\u05db\3\2\2\2\u05d9\u05d7\3\2\2\2\u05d9\u05da\3\2\2")
        buf.write(u"\2\u05da\u00e1\3\2\2\2\u05db\u05d9\3\2\2\2\u05dc\u05dd")
        buf.write(u"\br\1\2\u05dd\u05de\5P)\2\u05de\u05e5\3\2\2\2\u05df\u05e0")
        buf.write(u"\f\3\2\2\u05e0\u05e1\5v<\2\u05e1\u05e2\5P)\2\u05e2\u05e4")
        buf.write(u"\3\2\2\2\u05e3\u05df\3\2\2\2\u05e4\u05e7\3\2\2\2\u05e5")
        buf.write(u"\u05e3\3\2\2\2\u05e5\u05e6\3\2\2\2\u05e6\u00e3\3\2\2")
        buf.write(u"\2\u05e7\u05e5\3\2\2\2\u05e8\u05e9\7\27\2\2\u05e9\u05ea")
        buf.write(u"\5\u00e6t\2\u05ea\u05eb\7\23\2\2\u05eb\u05ec\5\u00e6")
        buf.write(u"t\2\u05ec\u05ed\7\30\2\2\u05ed\u05f7\3\2\2\2\u05ee\u05ef")
        buf.write(u"\7\27\2\2\u05ef\u05f0\5\u00e8u\2\u05f0\u05f1\7\30\2\2")
        buf.write(u"\u05f1\u05f7\3\2\2\2\u05f2\u05f3\7*\2\2\u05f3\u05f4\5")
        buf.write(u"\u00e8u\2\u05f4\u05f5\7(\2\2\u05f5\u05f7\3\2\2\2\u05f6")
        buf.write(u"\u05e8\3\2\2\2\u05f6\u05ee\3\2\2\2\u05f6\u05f2\3\2\2")
        buf.write(u"\2\u05f7\u00e5\3\2\2\2\u05f8\u0606\7\u008c\2\2\u05f9")
        buf.write(u"\u0606\7\u008d\2\2\u05fa\u0606\7\u0092\2\2\u05fb\u0606")
        buf.write(u"\7\u0093\2\2\u05fc\u0606\7\u008b\2\2\u05fd\u0606\7\u0097")
        buf.write(u"\2\2\u05fe\u0606\7\u0096\2\2\u05ff\u0606\7\u0091\2\2")
        buf.write(u"\u0600\u0606\7\u0094\2\2\u0601\u0606\7\u0095\2\2\u0602")
        buf.write(u"\u0606\7\u008a\2\2\u0603\u0606\7\u0098\2\2\u0604\u0606")
        buf.write(u"\5|?\2\u0605\u05f8\3\2\2\2\u0605\u05f9\3\2\2\2\u0605")
        buf.write(u"\u05fa\3\2\2\2\u0605\u05fb\3\2\2\2\u0605\u05fc\3\2\2")
        buf.write(u"\2\u0605\u05fd\3\2\2\2\u0605\u05fe\3\2\2\2\u0605\u05ff")
        buf.write(u"\3\2\2\2\u0605\u0600\3\2\2\2\u0605\u0601\3\2\2\2\u0605")
        buf.write(u"\u0602\3\2\2\2\u0605\u0603\3\2\2\2\u0605\u0604\3\2\2")
        buf.write(u"\2\u0606\u00e7\3\2\2\2\u0607\u0608\bu\1\2\u0608\u0609")
        buf.write(u"\5\u00e6t\2\u0609\u060f\3\2\2\2\u060a\u060b\f\3\2\2\u060b")
        buf.write(u"\u060c\7\22\2\2\u060c\u060e\5\u00e6t\2\u060d\u060a\3")
        buf.write(u"\2\2\2\u060e\u0611\3\2\2\2\u060f\u060d\3\2\2\2\u060f")
        buf.write(u"\u0610\3\2\2\2\u0610\u00e9\3\2\2\2\u0611\u060f\3\2\2")
        buf.write(u"\2\u0612\u0617\5\u00eex\2\u0613\u0617\5\u00f0y\2\u0614")
        buf.write(u"\u0617\5\u00aaV\2\u0615\u0617\5\u00ecw\2\u0616\u0612")
        buf.write(u"\3\2\2\2\u0616\u0613\3\2\2\2\u0616\u0614\3\2\2\2\u0616")
        buf.write(u"\u0615\3\2\2\2\u0617\u00eb\3\2\2\2\u0618\u0619\t\4\2")
        buf.write(u"\2\u0619\u00ed\3\2\2\2\u061a\u061b\7\25\2\2\u061b\u061c")
        buf.write(u"\5T+\2\u061c\u061d\7\26\2\2\u061d\u00ef\3\2\2\2\u061e")
        buf.write(u"\u0621\5\u00e6t\2\u061f\u0621\5\u00f2z\2\u0620\u061e")
        buf.write(u"\3\2\2\2\u0620\u061f\3\2\2\2\u0621\u00f1\3\2\2\2\u0622")
        buf.write(u"\u0628\5\u0096L\2\u0623\u0628\5\u0090I\2\u0624\u0628")
        buf.write(u"\5\u0092J\2\u0625\u0628\5\u00f6|\2\u0626\u0628\5\u00f4")
        buf.write(u"{\2\u0627\u0622\3\2\2\2\u0627\u0623\3\2\2\2\u0627\u0624")
        buf.write(u"\3\2\2\2\u0627\u0625\3\2\2\2\u0627\u0626\3\2\2\2\u0628")
        buf.write(u"\u00f3\3\2\2\2\u0629\u062b\7\25\2\2\u062a\u062c\5\u00f8")
        buf.write(u"}\2\u062b\u062a\3\2\2\2\u062b\u062c\3\2\2\2\u062c\u062d")
        buf.write(u"\3\2\2\2\u062d\u062e\7\26\2\2\u062e\u00f5\3\2\2\2\u062f")
        buf.write(u"\u0631\7\31\2\2\u0630\u0632\5\u00fa~\2\u0631\u0630\3")
        buf.write(u"\2\2\2\u0631\u0632\3\2\2\2\u0632\u0633\3\2\2\2\u0633")
        buf.write(u"\u0634\7\32\2\2\u0634\u00f7\3\2\2\2\u0635\u0636\b}\1")
        buf.write(u"\2\u0636\u0637\5T+\2\u0637\u063d\3\2\2\2\u0638\u0639")
        buf.write(u"\f\3\2\2\u0639\u063a\7\22\2\2\u063a\u063c\5T+\2\u063b")
        buf.write(u"\u0638\3\2\2\2\u063c\u063f\3\2\2\2\u063d\u063b\3\2\2")
        buf.write(u"\2\u063d\u063e\3\2\2\2\u063e\u00f9\3\2\2\2\u063f\u063d")
        buf.write(u"\3\2\2\2\u0640\u0641\b~\1\2\u0641\u0642\5\u00fc\177\2")
        buf.write(u"\u0642\u0648\3\2\2\2\u0643\u0644\f\3\2\2\u0644\u0645")
        buf.write(u"\7\22\2\2\u0645\u0647\5\u00fc\177\2\u0646\u0643\3\2\2")
        buf.write(u"\2\u0647\u064a\3\2\2\2\u0648\u0646\3\2\2\2\u0648\u0649")
        buf.write(u"\3\2\2\2\u0649\u00fb\3\2\2\2\u064a\u0648\3\2\2\2\u064b")
        buf.write(u"\u064c\5T+\2\u064c\u064d\7\20\2\2\u064d\u064e\5T+\2\u064e")
        buf.write(u"\u00fd\3\2\2\2\u064f\u0650\5T+\2\u0650\u0651\7\20\2\2")
        buf.write(u"\u0651\u0652\5T+\2\u0652\u0659\3\2\2\2\u0653\u0654\5")
        buf.write(u"T+\2\u0654\u0655\7\20\2\2\u0655\u0659\3\2\2\2\u0656\u0657")
        buf.write(u"\7\20\2\2\u0657\u0659\5T+\2\u0658\u064f\3\2\2\2\u0658")
        buf.write(u"\u0653\3\2\2\2\u0658\u0656\3\2\2\2\u0659\u00ff\3\2\2")
        buf.write(u"\2\u065a\u065b\5\u00acW\2\u065b\u065c\5\u010e\u0088\2")
        buf.write(u"\u065c\u065d\5T+\2\u065d\u0101\3\2\2\2\u065e\u065f\b")
        buf.write(u"\u0082\1\2\u065f\u0660\5\u00acW\2\u0660\u0665\3\2\2\2")
        buf.write(u"\u0661\u0662\f\3\2\2\u0662\u0664\5p9\2\u0663\u0661\3")
        buf.write(u"\2\2\2\u0664\u0667\3\2\2\2\u0665\u0663\3\2\2\2\u0665")
        buf.write(u"\u0666\3\2\2\2\u0666\u0103\3\2\2\2\u0667\u0665\3\2\2")
        buf.write(u"\2\u0668\u0669\6\u0083?\3\u0669\u066a\7\u0090\2\2\u066a")
        buf.write(u"\u066d\5\u00bc_\2\u066b\u066d\5T+\2\u066c\u0668\3\2\2")
        buf.write(u"\2\u066c\u066b\3\2\2\2\u066d\u0105\3\2\2\2\u066e\u0675")
        buf.write(u"\7\"\2\2\u066f\u0675\7#\2\2\u0670\u0675\5\u0110\u0089")
        buf.write(u"\2\u0671\u0675\5\u0112\u008a\2\u0672\u0675\5\u0114\u008b")
        buf.write(u"\2\u0673\u0675\5\u0116\u008c\2\u0674\u066e\3\2\2\2\u0674")
        buf.write(u"\u066f\3\2\2\2\u0674\u0670\3\2\2\2\u0674\u0671\3\2\2")
        buf.write(u"\2\u0674\u0672\3\2\2\2\u0674\u0673\3\2\2\2\u0675\u0107")
        buf.write(u"\3\2\2\2\u0676\u0677\7\u0090\2\2\u0677\u0678\6\u0085")
        buf.write(u"@\3\u0678\u0109\3\2\2\2\u0679\u067a\7\u0090\2\2\u067a")
        buf.write(u"\u067b\6\u0086A\3\u067b\u010b\3\2\2\2\u067c\u067d\7\u0090")
        buf.write(u"\2\2\u067d\u067e\6\u0087B\3\u067e\u010d\3\2\2\2\u067f")
        buf.write(u"\u0680\7-\2\2\u0680\u010f\3\2\2\2\u0681\u0682\7$\2\2")
        buf.write(u"\u0682\u0111\3\2\2\2\u0683\u0684\7%\2\2\u0684\u0113\3")
        buf.write(u"\2\2\2\u0685\u0686\7&\2\2\u0686\u0115\3\2\2\2\u0687\u0688")
        buf.write(u"\t\5\2\2\u0688\u0117\3\2\2\2\u0689\u068a\7y\2\2\u068a")
        buf.write(u"\u068b\5\u011a\u008e\2\u068b\u068c\7\21\2\2\u068c\u0691")
        buf.write(u"\3\2\2\2\u068d\u068e\5\u011a\u008e\2\u068e\u068f\7\21")
        buf.write(u"\2\2\u068f\u0691\3\2\2\2\u0690\u0689\3\2\2\2\u0690\u068d")
        buf.write(u"\3\2\2\2\u0691\u0119\3\2\2\2\u0692\u0693\b\u008e\1\2")
        buf.write(u"\u0693\u0694\5\u011c\u008f\2\u0694\u0699\3\2\2\2\u0695")
        buf.write(u"\u0696\f\3\2\2\u0696\u0698\5\u011e\u0090\2\u0697\u0695")
        buf.write(u"\3\2\2\2\u0698\u069b\3\2\2\2\u0699\u0697\3\2\2\2\u0699")
        buf.write(u"\u069a\3\2\2\2\u069a\u011b\3\2\2\2\u069b\u0699\3\2\2")
        buf.write(u"\2\u069c\u06a0\5\u0126\u0094\2\u069d\u06a0\5\u0128\u0095")
        buf.write(u"\2\u069e\u06a0\5\u012a\u0096\2\u069f\u069c\3\2\2\2\u069f")
        buf.write(u"\u069d\3\2\2\2\u069f\u069e\3\2\2\2\u06a0\u011d\3\2\2")
        buf.write(u"\2\u06a1\u06a2\7\24\2\2\u06a2\u06a5\5\u0120\u0091\2\u06a3")
        buf.write(u"\u06a5\5\u0124\u0093\2\u06a4\u06a1\3\2\2\2\u06a4\u06a3")
        buf.write(u"\3\2\2\2\u06a5\u011f\3\2\2\2\u06a6\u06a7\5\u012c\u0097")
        buf.write(u"\2\u06a7\u06a9\7\25\2\2\u06a8\u06aa\5\u0122\u0092\2\u06a9")
        buf.write(u"\u06a8\3\2\2\2\u06a9\u06aa\3\2\2\2\u06aa\u06ab\3\2\2")
        buf.write(u"\2\u06ab\u06ac\7\26\2\2\u06ac\u0121\3\2\2\2\u06ad\u06ae")
        buf.write(u"\b\u0092\1\2\u06ae\u06af\5\u011a\u008e\2\u06af\u06b5")
        buf.write(u"\3\2\2\2\u06b0\u06b1\f\3\2\2\u06b1\u06b2\7\22\2\2\u06b2")
        buf.write(u"\u06b4\5\u011a\u008e\2\u06b3\u06b0\3\2\2\2\u06b4\u06b7")
        buf.write(u"\3\2\2\2\u06b5\u06b3\3\2\2\2\u06b5\u06b6\3\2\2\2\u06b6")
        buf.write(u"\u0123\3\2\2\2\u06b7\u06b5\3\2\2\2\u06b8\u06b9\7\27\2")
        buf.write(u"\2\u06b9\u06ba\5\u011a\u008e\2\u06ba\u06bb\7\30\2\2\u06bb")
        buf.write(u"\u0125\3\2\2\2\u06bc\u06bd\7\25\2\2\u06bd\u06be\5\u011a")
        buf.write(u"\u008e\2\u06be\u06bf\7\26\2\2\u06bf\u0127\3\2\2\2\u06c0")
        buf.write(u"\u06c1\b\u0095\1\2\u06c1\u06c2\5\u012c\u0097\2\u06c2")
        buf.write(u"\u06c8\3\2\2\2\u06c3\u06c4\f\3\2\2\u06c4\u06c5\7\24\2")
        buf.write(u"\2\u06c5\u06c7\5\u012c\u0097\2\u06c6\u06c3\3\2\2\2\u06c7")
        buf.write(u"\u06ca\3\2\2\2\u06c8\u06c6\3\2\2\2\u06c8\u06c9\3\2\2")
        buf.write(u"\2\u06c9\u0129\3\2\2\2\u06ca\u06c8\3\2\2\2\u06cb\u06d1")
        buf.write(u"\7\u0092\2\2\u06cc\u06d1\7\u0094\2\2\u06cd\u06d1\7\u0091")
        buf.write(u"\2\2\u06ce\u06d1\7\u008a\2\2\u06cf\u06d1\7\u008b\2\2")
        buf.write(u"\u06d0\u06cb\3\2\2\2\u06d0\u06cc\3\2\2\2\u06d0\u06cd")
        buf.write(u"\3\2\2\2\u06d0\u06ce\3\2\2\2\u06d0\u06cf\3\2\2\2\u06d1")
        buf.write(u"\u012b\3\2\2\2\u06d2\u06d3\t\6\2\2\u06d3\u012d\3\2\2")
        buf.write(u"\2\u06d4\u06d5\7y\2\2\u06d5\u06d8\5\u0130\u0099\2\u06d6")
        buf.write(u"\u06d8\5\u0130\u0099\2\u06d7\u06d4\3\2\2\2\u06d7\u06d6")
        buf.write(u"\3\2\2\2\u06d8\u012f\3\2\2\2\u06d9\u06da\b\u0099\1\2")
        buf.write(u"\u06da\u06db\5\u0132\u009a\2\u06db\u06e0\3\2\2\2\u06dc")
        buf.write(u"\u06dd\f\3\2\2\u06dd\u06df\5\u0134\u009b\2\u06de\u06dc")
        buf.write(u"\3\2\2\2\u06df\u06e2\3\2\2\2\u06e0\u06de\3\2\2\2\u06e0")
        buf.write(u"\u06e1\3\2\2\2\u06e1\u0131\3\2\2\2\u06e2\u06e0\3\2\2")
        buf.write(u"\2\u06e3\u06e8\5\u013e\u00a0\2\u06e4\u06e8\5\u0140\u00a1")
        buf.write(u"\2\u06e5\u06e8\5\u0142\u00a2\2\u06e6\u06e8\5\u0136\u009c")
        buf.write(u"\2\u06e7\u06e3\3\2\2\2\u06e7\u06e4\3\2\2\2\u06e7\u06e5")
        buf.write(u"\3\2\2\2\u06e7\u06e6\3\2\2\2\u06e8\u0133\3\2\2\2\u06e9")
        buf.write(u"\u06ea\7\24\2\2\u06ea\u06f0\5\u0136\u009c\2\u06eb\u06ec")
        buf.write(u"\7\27\2\2\u06ec\u06ed\5\u0130\u0099\2\u06ed\u06ee\7\30")
        buf.write(u"\2\2\u06ee\u06f0\3\2\2\2\u06ef\u06e9\3\2\2\2\u06ef\u06eb")
        buf.write(u"\3\2\2\2\u06f0\u0135\3\2\2\2\u06f1\u06f2\5\u0144\u00a3")
        buf.write(u"\2\u06f2\u06f4\7\25\2\2\u06f3\u06f5\5\u0138\u009d\2\u06f4")
        buf.write(u"\u06f3\3\2\2\2\u06f4\u06f5\3\2\2\2\u06f5\u06f6\3\2\2")
        buf.write(u"\2\u06f6\u06f7\7\26\2\2\u06f7\u0137\3\2\2\2\u06f8\u06ff")
        buf.write(u"\5\u013a\u009e\2\u06f9\u06ff\5\u013c\u009f\2\u06fa\u06fb")
        buf.write(u"\5\u013a\u009e\2\u06fb\u06fc\7\22\2\2\u06fc\u06fd\5\u013c")
        buf.write(u"\u009f\2\u06fd\u06ff\3\2\2\2\u06fe\u06f8\3\2\2\2\u06fe")
        buf.write(u"\u06f9\3\2\2\2\u06fe\u06fa\3\2\2\2\u06ff\u0139\3\2\2")
        buf.write(u"\2\u0700\u0701\b\u009e\1\2\u0701\u0702\5\u0130\u0099")
        buf.write(u"\2\u0702\u0708\3\2\2\2\u0703\u0704\f\3\2\2\u0704\u0705")
        buf.write(u"\7\22\2\2\u0705\u0707\5\u0130\u0099\2\u0706\u0703\3\2")
        buf.write(u"\2\2\u0707\u070a\3\2\2\2\u0708\u0706\3\2\2\2\u0708\u0709")
        buf.write(u"\3\2\2\2\u0709\u013b\3\2\2\2\u070a\u0708\3\2\2\2\u070b")
        buf.write(u"\u070c\b\u009f\1\2\u070c\u070d\5\u0144\u00a3\2\u070d")
        buf.write(u"\u070e\7-\2\2\u070e\u070f\5\u0130\u0099\2\u070f\u0718")
        buf.write(u"\3\2\2\2\u0710\u0711\f\3\2\2\u0711\u0712\7\22\2\2\u0712")
        buf.write(u"\u0713\5\u0144\u00a3\2\u0713\u0714\7-\2\2\u0714\u0715")
        buf.write(u"\5\u0130\u0099\2\u0715\u0717\3\2\2\2\u0716\u0710\3\2")
        buf.write(u"\2\2\u0717\u071a\3\2\2\2\u0718\u0716\3\2\2\2\u0718\u0719")
        buf.write(u"\3\2\2\2\u0719\u013d\3\2\2\2\u071a\u0718\3\2\2\2\u071b")
        buf.write(u"\u071c\7\25\2\2\u071c\u071d\5\u0130\u0099\2\u071d\u071e")
        buf.write(u"\7\26\2\2\u071e\u013f\3\2\2\2\u071f\u0720\b\u00a1\1\2")
        buf.write(u"\u0720\u0721\5\u0144\u00a3\2\u0721\u0727\3\2\2\2\u0722")
        buf.write(u"\u0723\f\3\2\2\u0723\u0724\7\24\2\2\u0724\u0726\5\u0144")
        buf.write(u"\u00a3\2\u0725\u0722\3\2\2\2\u0726\u0729\3\2\2\2\u0727")
        buf.write(u"\u0725\3\2\2\2\u0727\u0728\3\2\2\2\u0728\u0141\3\2\2")
        buf.write(u"\2\u0729\u0727\3\2\2\2\u072a\u0730\7\u0092\2\2\u072b")
        buf.write(u"\u0730\7\u0094\2\2\u072c\u0730\7\u0091\2\2\u072d\u0730")
        buf.write(u"\7\u008a\2\2\u072e\u0730\7\u008b\2\2\u072f\u072a\3\2")
        buf.write(u"\2\2\u072f\u072b\3\2\2\2\u072f\u072c\3\2\2\2\u072f\u072d")
        buf.write(u"\3\2\2\2\u072f\u072e\3\2\2\2\u0730\u0143\3\2\2\2\u0731")
        buf.write(u"\u0732\t\6\2\2\u0732\u0145\3\2\2\2\u0733\u0734\7y\2\2")
        buf.write(u"\u0734\u0735\5\u0148\u00a5\2\u0735\u0736\7\21\2\2\u0736")
        buf.write(u"\u073b\3\2\2\2\u0737\u0738\5\u0148\u00a5\2\u0738\u0739")
        buf.write(u"\7\21\2\2\u0739\u073b\3\2\2\2\u073a\u0733\3\2\2\2\u073a")
        buf.write(u"\u0737\3\2\2\2\u073b\u0147\3\2\2\2\u073c\u073d\b\u00a5")
        buf.write(u"\1\2\u073d\u073e\5\u014a\u00a6\2\u073e\u0743\3\2\2\2")
        buf.write(u"\u073f\u0740\f\3\2\2\u0740\u0742\5\u014c\u00a7\2\u0741")
        buf.write(u"\u073f\3\2\2\2\u0742\u0745\3\2\2\2\u0743\u0741\3\2\2")
        buf.write(u"\2\u0743\u0744\3\2\2\2\u0744\u0149\3\2\2\2\u0745\u0743")
        buf.write(u"\3\2\2\2\u0746\u074a\5\u0154\u00ab\2\u0747\u074a\5\u0156")
        buf.write(u"\u00ac\2\u0748\u074a\5\u015a\u00ae\2\u0749\u0746\3\2")
        buf.write(u"\2\2\u0749\u0747\3\2\2\2\u0749\u0748\3\2\2\2\u074a\u014b")
        buf.write(u"\3\2\2\2\u074b\u074c\7\24\2\2\u074c\u074f\5\u014e\u00a8")
        buf.write(u"\2\u074d\u074f\5\u0152\u00aa\2\u074e\u074b\3\2\2\2\u074e")
        buf.write(u"\u074d\3\2\2\2\u074f\u014d\3\2\2\2\u0750\u0751\5\u015c")
        buf.write(u"\u00af\2\u0751\u0753\7\25\2\2\u0752\u0754\5\u0150\u00a9")
        buf.write(u"\2\u0753\u0752\3\2\2\2\u0753\u0754\3\2\2\2\u0754\u0755")
        buf.write(u"\3\2\2\2\u0755\u0756\7\26\2\2\u0756\u014f\3\2\2\2\u0757")
        buf.write(u"\u0758\b\u00a9\1\2\u0758\u0759\5\u0148\u00a5\2\u0759")
        buf.write(u"\u075f\3\2\2\2\u075a\u075b\f\3\2\2\u075b\u075c\7\22\2")
        buf.write(u"\2\u075c\u075e\5\u0148\u00a5\2\u075d\u075a\3\2\2\2\u075e")
        buf.write(u"\u0761\3\2\2\2\u075f\u075d\3\2\2\2\u075f\u0760\3\2\2")
        buf.write(u"\2\u0760\u0151\3\2\2\2\u0761\u075f\3\2\2\2\u0762\u0763")
        buf.write(u"\7\27\2\2\u0763\u0764\5\u0148\u00a5\2\u0764\u0765\7\30")
        buf.write(u"\2\2\u0765\u0153\3\2\2\2\u0766\u0767\7\25\2\2\u0767\u0768")
        buf.write(u"\5\u0148\u00a5\2\u0768\u0769\7\26\2\2\u0769\u0155\3\2")
        buf.write(u"\2\2\u076a\u076b\b\u00ac\1\2\u076b\u076c\5\u015c\u00af")
        buf.write(u"\2\u076c\u0772\3\2\2\2\u076d\u076e\f\3\2\2\u076e\u076f")
        buf.write(u"\7\24\2\2\u076f\u0771\5\u015c\u00af\2\u0770\u076d\3\2")
        buf.write(u"\2\2\u0771\u0774\3\2\2\2\u0772\u0770\3\2\2\2\u0772\u0773")
        buf.write(u"\3\2\2\2\u0773\u0157\3\2\2\2\u0774\u0772\3\2\2\2\u0775")
        buf.write(u"\u0776\b\u00ad\1\2\u0776\u0777\5\u0156\u00ac\2\u0777")
        buf.write(u"\u077d\3\2\2\2\u0778\u0779\f\3\2\2\u0779\u077a\7\35\2")
        buf.write(u"\2\u077a\u077c\7\u008f\2\2\u077b\u0778\3\2\2\2\u077c")
        buf.write(u"\u077f\3\2\2\2\u077d\u077b\3\2\2\2\u077d\u077e\3\2\2")
        buf.write(u"\2\u077e\u0159\3\2\2\2\u077f\u077d\3\2\2\2\u0780\u0786")
        buf.write(u"\7\u0092\2\2\u0781\u0786\7\u0094\2\2\u0782\u0786\7\u0091")
        buf.write(u"\2\2\u0783\u0786\7\u008a\2\2\u0784\u0786\7\u008b\2\2")
        buf.write(u"\u0785\u0780\3\2\2\2\u0785\u0781\3\2\2\2\u0785\u0782")
        buf.write(u"\3\2\2\2\u0785\u0783\3\2\2\2\u0785\u0784\3\2\2\2\u0786")
        buf.write(u"\u015b\3\2\2\2\u0787\u0788\t\6\2\2\u0788\u015d\3\2\2")
        buf.write(u"\2\u0789\u078a\7y\2\2\u078a\u078b\5\u0160\u00b1\2\u078b")
        buf.write(u"\u078c\7\21\2\2\u078c\u0791\3\2\2\2\u078d\u078e\5\u0160")
        buf.write(u"\u00b1\2\u078e\u078f\7\21\2\2\u078f\u0791\3\2\2\2\u0790")
        buf.write(u"\u0789\3\2\2\2\u0790\u078d\3\2\2\2\u0791\u015f\3\2\2")
        buf.write(u"\2\u0792\u0793\b\u00b1\1\2\u0793\u0794\5\u0162\u00b2")
        buf.write(u"\2\u0794\u0799\3\2\2\2\u0795\u0796\f\3\2\2\u0796\u0798")
        buf.write(u"\5\u0164\u00b3\2\u0797\u0795\3\2\2\2\u0798\u079b\3\2")
        buf.write(u"\2\2\u0799\u0797\3\2\2\2\u0799\u079a\3\2\2\2\u079a\u0161")
        buf.write(u"\3\2\2\2\u079b\u0799\3\2\2\2\u079c\u07a0\5\u016c\u00b7")
        buf.write(u"\2\u079d\u07a0\5\u016e\u00b8\2\u079e\u07a0\5\u0170\u00b9")
        buf.write(u"\2\u079f\u079c\3\2\2\2\u079f\u079d\3\2\2\2\u079f\u079e")
        buf.write(u"\3\2\2\2\u07a0\u0163\3\2\2\2\u07a1\u07a2\7\24\2\2\u07a2")
        buf.write(u"\u07a5\5\u0166\u00b4\2\u07a3\u07a5\5\u016a\u00b6\2\u07a4")
        buf.write(u"\u07a1\3\2\2\2\u07a4\u07a3\3\2\2\2\u07a5\u0165\3\2\2")
        buf.write(u"\2\u07a6\u07a7\5\u0172\u00ba\2\u07a7\u07a9\7\25\2\2\u07a8")
        buf.write(u"\u07aa\5\u0168\u00b5\2\u07a9\u07a8\3\2\2\2\u07a9\u07aa")
        buf.write(u"\3\2\2\2\u07aa\u07ab\3\2\2\2\u07ab\u07ac\7\26\2\2\u07ac")
        buf.write(u"\u0167\3\2\2\2\u07ad\u07ae\b\u00b5\1\2\u07ae\u07af\5")
        buf.write(u"\u0160\u00b1\2\u07af\u07b5\3\2\2\2\u07b0\u07b1\f\3\2")
        buf.write(u"\2\u07b1\u07b2\7\22\2\2\u07b2\u07b4\5\u0160\u00b1\2\u07b3")
        buf.write(u"\u07b0\3\2\2\2\u07b4\u07b7\3\2\2\2\u07b5\u07b3\3\2\2")
        buf.write(u"\2\u07b5\u07b6\3\2\2\2\u07b6\u0169\3\2\2\2\u07b7\u07b5")
        buf.write(u"\3\2\2\2\u07b8\u07b9\7\27\2\2\u07b9\u07ba\5\u0160\u00b1")
        buf.write(u"\2\u07ba\u07bb\7\30\2\2\u07bb\u016b\3\2\2\2\u07bc\u07bd")
        buf.write(u"\7\25\2\2\u07bd\u07be\5\u0160\u00b1\2\u07be\u07bf\7\26")
        buf.write(u"\2\2\u07bf\u016d\3\2\2\2\u07c0\u07c1\b\u00b8\1\2\u07c1")
        buf.write(u"\u07c2\5\u0172\u00ba\2\u07c2\u07c8\3\2\2\2\u07c3\u07c4")
        buf.write(u"\f\3\2\2\u07c4\u07c5\7\24\2\2\u07c5\u07c7\5\u0172\u00ba")
        buf.write(u"\2\u07c6\u07c3\3\2\2\2\u07c7\u07ca\3\2\2\2\u07c8\u07c6")
        buf.write(u"\3\2\2\2\u07c8\u07c9\3\2\2\2\u07c9\u016f\3\2\2\2\u07ca")
        buf.write(u"\u07c8\3\2\2\2\u07cb\u07d1\7\u0092\2\2\u07cc\u07d1\7")
        buf.write(u"\u0094\2\2\u07cd\u07d1\7\u0091\2\2\u07ce\u07d1\7\u008a")
        buf.write(u"\2\2\u07cf\u07d1\7\u008b\2\2\u07d0\u07cb\3\2\2\2\u07d0")
        buf.write(u"\u07cc\3\2\2\2\u07d0\u07cd\3\2\2\2\u07d0\u07ce\3\2\2")
        buf.write(u"\2\u07d0\u07cf\3\2\2\2\u07d1\u0171\3\2\2\2\u07d2\u07d3")
        buf.write(u"\t\6\2\2\u07d3\u0173\3\2\2\2\u0097\u017a\u017d\u0196")
        buf.write(u"\u01a3\u01b0\u01b7\u01c4\u01ce\u01d3\u01e2\u0202\u020f")
        buf.write(u"\u0226\u0230\u0235\u023b\u0240\u024c\u0251\u0269\u0274")
        buf.write(u"\u0278\u0289\u028e\u0297\u02a0\u02a9\u02c6\u02d9\u02df")
        buf.write(u"\u0301\u030a\u0321\u032f\u0338\u0341\u0358\u035c\u0370")
        buf.write(u"\u03d0\u03d2\u03de\u03e7\u03f6\u03fd\u0406\u040d\u042c")
        buf.write(u"\u043c\u0445\u044b\u0450\u0457\u045f\u046d\u0475\u047b")
        buf.write(u"\u0486\u0492\u049d\u04aa\u04ae\u04b4\u04c0\u04d4\u04d6")
        buf.write(u"\u04db\u04e7\u04f2\u04fc\u0501\u0506\u0516\u051b\u051f")
        buf.write(u"\u0524\u052b\u0536\u0538\u0544\u054b\u0557\u055b\u0565")
        buf.write(u"\u056d\u0573\u057a\u057f\u0589\u0590\u059b\u05a8\u05ac")
        buf.write(u"\u05af\u05b3\u05b6\u05c1\u05cd\u05d9\u05e5\u05f6\u0605")
        buf.write(u"\u060f\u0616\u0620\u0627\u062b\u0631\u063d\u0648\u0658")
        buf.write(u"\u0665\u066c\u0674\u0690\u0699\u069f\u06a4\u06a9\u06b5")
        buf.write(u"\u06c8\u06d0\u06d7\u06e0\u06e7\u06ef\u06f4\u06fe\u0708")
        buf.write(u"\u0718\u0727\u072f\u073a\u0743\u0749\u074e\u0753\u075f")
        buf.write(u"\u0772\u077d\u0785\u0790\u0799\u079f\u07a4\u07a9\u07b5")
        buf.write(u"\u07c8\u07d0")
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
                     u"'expecting'", u"'extends'", u"'fetch'", u"'finally'", 
                     u"'for'", u"'from'", u"'getter'", u"'if'", u"'in'", 
                     u"'invoke'", u"'is'", u"'mappings'", u"'matching'", 
                     u"'method'", u"'methods'", u"'modulo'", u"'native'", 
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
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FINALLY", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INVOKE", u"IS", u"MAPPINGS", u"MATCHING", u"METHOD", 
                      u"METHODS", u"MODULO", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"OPEN", u"OPERATOR", 
                      u"OR", u"OTHERWISE", u"PASS", u"RAISE", u"READ", u"RECEIVING", 
                      u"RESOURCE", u"RETURN", u"RETURNING", u"SELF", u"SETTER", 
                      u"SINGLETON", u"SORTED", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"WITH", u"WHEN", u"WHERE", 
                      u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", u"CHAR_LITERAL", 
                      u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
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
    RULE_test_method_declaration = 20
    RULE_assertion = 21
    RULE_typed_argument = 22
    RULE_statement = 23
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
    RULE_assertion_list = 110
    RULE_switch_case_statement_list = 111
    RULE_catch_statement_list = 112
    RULE_literal_collection = 113
    RULE_atomic_literal = 114
    RULE_literal_list_literal = 115
    RULE_selectable_expression = 116
    RULE_this_expression = 117
    RULE_parenthesis_expression = 118
    RULE_literal_expression = 119
    RULE_collection_literal = 120
    RULE_tuple_literal = 121
    RULE_dict_literal = 122
    RULE_expression_tuple = 123
    RULE_dict_entry_list = 124
    RULE_dict_entry = 125
    RULE_slice_arguments = 126
    RULE_assign_variable_statement = 127
    RULE_assignable_instance = 128
    RULE_is_expression = 129
    RULE_operator = 130
    RULE_key_token = 131
    RULE_value_token = 132
    RULE_symbols_token = 133
    RULE_assign = 134
    RULE_multiply = 135
    RULE_divide = 136
    RULE_idivide = 137
    RULE_modulo = 138
    RULE_javascript_statement = 139
    RULE_javascript_expression = 140
    RULE_javascript_primary_expression = 141
    RULE_javascript_selector_expression = 142
    RULE_javascript_method_expression = 143
    RULE_javascript_arguments = 144
    RULE_javascript_item_expression = 145
    RULE_javascript_parenthesis_expression = 146
    RULE_javascript_identifier_expression = 147
    RULE_javascript_literal_expression = 148
    RULE_javascript_identifier = 149
    RULE_python_statement = 150
    RULE_python_expression = 151
    RULE_python_primary_expression = 152
    RULE_python_selector_expression = 153
    RULE_python_method_expression = 154
    RULE_python_argument_list = 155
    RULE_python_ordinal_argument_list = 156
    RULE_python_named_argument_list = 157
    RULE_python_parenthesis_expression = 158
    RULE_python_identifier_expression = 159
    RULE_python_literal_expression = 160
    RULE_python_identifier = 161
    RULE_java_statement = 162
    RULE_java_expression = 163
    RULE_java_primary_expression = 164
    RULE_java_selector_expression = 165
    RULE_java_method_expression = 166
    RULE_java_arguments = 167
    RULE_java_item_expression = 168
    RULE_java_parenthesis_expression = 169
    RULE_java_identifier_expression = 170
    RULE_java_class_identifier_expression = 171
    RULE_java_literal_expression = 172
    RULE_java_identifier = 173
    RULE_csharp_statement = 174
    RULE_csharp_expression = 175
    RULE_csharp_primary_expression = 176
    RULE_csharp_selector_expression = 177
    RULE_csharp_method_expression = 178
    RULE_csharp_arguments = 179
    RULE_csharp_item_expression = 180
    RULE_csharp_parenthesis_expression = 181
    RULE_csharp_identifier_expression = 182
    RULE_csharp_literal_expression = 183
    RULE_csharp_identifier = 184

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"member_method_declaration", u"operator_method_declaration", 
                   u"setter_method_declaration", u"getter_method_declaration", 
                   u"native_category_declaration", u"native_resource_declaration", 
                   u"native_category_mappings", u"native_category_mapping_list", 
                   u"attribute_list", u"abstract_method_declaration", u"concrete_method_declaration", 
                   u"native_method_declaration", u"test_method_declaration", 
                   u"assertion", u"typed_argument", u"statement", u"method_call", 
                   u"method_selector", u"callable_parent", u"callable_selector", 
                   u"with_resource_statement", u"with_singleton_statement", 
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
    MAPPINGS=99
    MATCHING=100
    METHOD=101
    METHODS=102
    MODULO=103
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
    TEXT_LITERAL=143
    INTEGER_LITERAL=144
    HEXA_LITERAL=145
    DECIMAL_LITERAL=146
    DATETIME_LITERAL=147
    TIME_LITERAL=148
    DATE_LITERAL=149
    PERIOD_LITERAL=150
    COMMENT=151

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
            self.state = 370
            self.match(PParser.ENUM)
            self.state = 371 
            localctx.name = self.type_identifier()
            self.state = 372
            self.match(PParser.LPAR)
            self.state = 379
            token = self._input.LA(1)
            if token in [PParser.TYPE_IDENTIFIER]:
                self.state = 373 
                localctx.derived = self.type_identifier()
                self.state = 376
                _la = self._input.LA(1)
                if _la==PParser.COMMA:
                    self.state = 374
                    self.match(PParser.COMMA)
                    self.state = 375 
                    localctx.attrs = self.attribute_list()



            elif token in [PParser.VARIABLE_IDENTIFIER]:
                self.state = 378 
                localctx.attrs = self.attribute_list()

            else:
                raise NoViableAltException(self)

            self.state = 381
            self.match(PParser.RPAR)
            self.state = 382
            self.match(PParser.COLON)
            self.state = 383 
            self.indent()
            self.state = 384 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 385 
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
            self.state = 387
            self.match(PParser.ENUM)
            self.state = 388 
            localctx.name = self.type_identifier()
            self.state = 389
            self.match(PParser.LPAR)
            self.state = 390 
            localctx.typ = self.native_type()
            self.state = 391
            self.match(PParser.RPAR)
            self.state = 392
            self.match(PParser.COLON)
            self.state = 393 
            self.indent()
            self.state = 394 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 395 
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
            self.state = 397 
            localctx.name = self.symbol_identifier()
            self.state = 398
            self.match(PParser.EQ)
            self.state = 399 
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
            self.state = 401 
            localctx.name = self.symbol_identifier()
            self.state = 402
            self.match(PParser.LPAR)
            self.state = 404
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 403 
                localctx.args = self.argument_assignment_list(0)


            self.state = 406
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
            self.state = 408
            self.match(PParser.ATTR)
            self.state = 409 
            localctx.name = self.variable_identifier()
            self.state = 410
            self.match(PParser.LPAR)
            self.state = 411 
            localctx.typ = self.typedef(0)
            self.state = 412
            self.match(PParser.RPAR)
            self.state = 413
            self.match(PParser.COLON)
            self.state = 414 
            self.indent()
            self.state = 417
            token = self._input.LA(1)
            if token in [PParser.IN, PParser.MATCHING]:
                self.state = 415 
                localctx.match = self.attribute_constraint()

            elif token in [PParser.PASS]:
                self.state = 416
                self.match(PParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 419 
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
            self.state = 421
            _la = self._input.LA(1)
            if not(_la==PParser.CATEGORY or _la==PParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 422 
            localctx.name = self.type_identifier()
            self.state = 423
            self.match(PParser.LPAR)
            self.state = 430
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 424 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 425 
                localctx.attrs = self.attribute_list()
                pass

            elif la_ == 3:
                self.state = 426 
                localctx.derived = self.derived_list()
                self.state = 427
                self.match(PParser.COMMA)
                self.state = 428 
                localctx.attrs = self.attribute_list()
                pass


            self.state = 432
            self.match(PParser.RPAR)
            self.state = 433
            self.match(PParser.COLON)
            self.state = 434 
            self.indent()
            self.state = 437
            token = self._input.LA(1)
            if token in [PParser.DEF]:
                self.state = 435 
                localctx.methods = self.category_method_declaration_list(0)

            elif token in [PParser.PASS]:
                self.state = 436
                self.match(PParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 439 
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
            self.state = 441
            self.match(PParser.SINGLETON)
            self.state = 442 
            localctx.name = self.type_identifier()
            self.state = 443
            self.match(PParser.LPAR)
            self.state = 444 
            localctx.attrs = self.attribute_list()
            self.state = 445
            self.match(PParser.RPAR)
            self.state = 446
            self.match(PParser.COLON)
            self.state = 447 
            self.indent()
            self.state = 450
            token = self._input.LA(1)
            if token in [PParser.DEF]:
                self.state = 448 
                localctx.methods = self.category_method_declaration_list(0)

            elif token in [PParser.PASS]:
                self.state = 449
                self.match(PParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 452 
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
            self.state = 454 
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
            self.state = 456
            self.match(PParser.DEF)
            self.state = 457 
            localctx.name = self.method_identifier()
            self.state = 458
            self.match(PParser.LPAR)
            self.state = 460
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 459 
                localctx.args = self.argument_list(0)


            self.state = 462
            self.match(PParser.RPAR)
            self.state = 465
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 463
                self.match(PParser.RARROW)
                self.state = 464 
                localctx.typ = self.typedef(0)


            self.state = 467
            self.match(PParser.COLON)
            self.state = 468 
            self.indent()
            self.state = 469 
            localctx.stmts = self.statement_list(0)
            self.state = 470 
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
            self.state = 472
            self.match(PParser.DEF)
            self.state = 473
            self.match(PParser.OPERATOR)
            self.state = 474 
            localctx.op = self.operator()
            self.state = 475
            self.match(PParser.LPAR)
            self.state = 476 
            localctx.arg = self.operator_argument()
            self.state = 477
            self.match(PParser.RPAR)
            self.state = 480
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 478
                self.match(PParser.RARROW)
                self.state = 479 
                localctx.typ = self.typedef(0)


            self.state = 482
            self.match(PParser.COLON)
            self.state = 483 
            self.indent()
            self.state = 484 
            localctx.stmts = self.statement_list(0)
            self.state = 485 
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
            self.state = 487
            self.match(PParser.DEF)
            self.state = 488 
            localctx.name = self.variable_identifier()
            self.state = 489
            self.match(PParser.SETTER)
            self.state = 490
            self.match(PParser.LPAR)
            self.state = 491
            self.match(PParser.RPAR)
            self.state = 492
            self.match(PParser.COLON)
            self.state = 493 
            self.indent()
            self.state = 494 
            localctx.stmts = self.statement_list(0)
            self.state = 495 
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
            self.state = 497
            self.match(PParser.DEF)
            self.state = 498 
            localctx.name = self.variable_identifier()
            self.state = 499
            self.match(PParser.GETTER)
            self.state = 500
            self.match(PParser.LPAR)
            self.state = 501
            self.match(PParser.RPAR)
            self.state = 502
            self.match(PParser.COLON)
            self.state = 503 
            self.indent()
            self.state = 504 
            localctx.stmts = self.statement_list(0)
            self.state = 505 
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
            self.state = 507
            self.match(PParser.NATIVE)
            self.state = 508
            _la = self._input.LA(1)
            if not(_la==PParser.CATEGORY or _la==PParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 509 
            localctx.name = self.type_identifier()
            self.state = 510
            self.match(PParser.LPAR)
            self.state = 512
            _la = self._input.LA(1)
            if _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 511 
                localctx.attrs = self.attribute_list()


            self.state = 514
            self.match(PParser.RPAR)
            self.state = 515
            self.match(PParser.COLON)
            self.state = 516 
            self.indent()
            self.state = 517 
            localctx.mappings = self.native_category_mappings()
            self.state = 518 
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
            self.state = 520
            self.match(PParser.NATIVE)
            self.state = 521
            self.match(PParser.RESOURCE)
            self.state = 522 
            localctx.name = self.type_identifier()
            self.state = 523
            self.match(PParser.LPAR)
            self.state = 525
            _la = self._input.LA(1)
            if _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 524 
                localctx.attrs = self.attribute_list()


            self.state = 527
            self.match(PParser.RPAR)
            self.state = 528
            self.match(PParser.COLON)
            self.state = 529 
            self.indent()
            self.state = 530 
            localctx.mappings = self.native_category_mappings()
            self.state = 531 
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
            self.state = 533
            self.match(PParser.MAPPINGS)
            self.state = 534
            self.match(PParser.COLON)
            self.state = 535 
            self.indent()
            self.state = 536 
            localctx.items = self.native_category_mapping_list(0)
            self.state = 537 
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

            self.state = 540 
            localctx.item = self.native_category_mapping()
            self._ctx.stop = self._input.LT(-1)
            self.state = 548
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
                    self.state = 542
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 543 
                    self.lfp()
                    self.state = 544 
                    localctx.item = self.native_category_mapping() 
                self.state = 550
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
            self.state = 551 
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
            self.state = 553
            self.match(PParser.ABSTRACT)
            self.state = 554
            self.match(PParser.DEF)
            self.state = 555 
            localctx.name = self.method_identifier()
            self.state = 556
            self.match(PParser.LPAR)
            self.state = 558
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 557 
                localctx.args = self.argument_list(0)


            self.state = 560
            self.match(PParser.RPAR)
            self.state = 563
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 561
                self.match(PParser.RARROW)
                self.state = 562 
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
            self.state = 565
            self.match(PParser.DEF)
            self.state = 566 
            localctx.name = self.method_identifier()
            self.state = 567
            self.match(PParser.LPAR)
            self.state = 569
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 568 
                localctx.args = self.argument_list(0)


            self.state = 571
            self.match(PParser.RPAR)
            self.state = 574
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 572
                self.match(PParser.RARROW)
                self.state = 573 
                localctx.typ = self.typedef(0)


            self.state = 576
            self.match(PParser.COLON)
            self.state = 577 
            self.indent()
            self.state = 578 
            localctx.stmts = self.statement_list(0)
            self.state = 579 
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
            self.state = 581
            self.match(PParser.DEF)
            self.state = 582
            self.match(PParser.NATIVE)
            self.state = 583 
            localctx.name = self.method_identifier()
            self.state = 584
            self.match(PParser.LPAR)
            self.state = 586
            _la = self._input.LA(1)
            if _la==PParser.CODE or _la==PParser.VARIABLE_IDENTIFIER:
                self.state = 585 
                localctx.args = self.argument_list(0)


            self.state = 588
            self.match(PParser.RPAR)
            self.state = 591
            _la = self._input.LA(1)
            if _la==PParser.RARROW:
                self.state = 589
                self.match(PParser.RARROW)
                self.state = 590 
                localctx.typ = self.typedef(0)


            self.state = 593
            self.match(PParser.COLON)
            self.state = 594 
            self.indent()
            self.state = 595 
            localctx.stmts = self.native_statement_list(0)
            self.state = 596 
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
            super(PParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEF(self):
            return self.getToken(PParser.DEF, 0)

        def TEST(self):
            return self.getToken(PParser.TEST, 0)

        def LPAR(self):
            return self.getToken(PParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PParser.RPAR, 0)

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


        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)


        def EXPECTING(self):
            return self.getToken(PParser.EXPECTING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(PParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PParser.Statement_listContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(PParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(PParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return PParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = PParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(PParser.DEF)
            self.state = 599
            self.match(PParser.TEST)
            self.state = 600
            localctx.name = self.match(PParser.TEXT_LITERAL)
            self.state = 601
            self.match(PParser.LPAR)
            self.state = 602
            self.match(PParser.RPAR)
            self.state = 603
            self.match(PParser.COLON)
            self.state = 604 
            self.indent()
            self.state = 605 
            localctx.stmts = self.statement_list(0)
            self.state = 606 
            self.dedent()
            self.state = 607 
            self.lfp()
            self.state = 608
            self.match(PParser.EXPECTING)
            self.state = 609
            self.match(PParser.COLON)
            self.state = 615
            token = self._input.LA(1)
            if token in [PParser.LF]:
                self.state = 610 
                self.indent()
                self.state = 611 
                localctx.exps = self.assertion_list(0)
                self.state = 612 
                self.dedent()

            elif token in [PParser.SYMBOL_IDENTIFIER]:
                self.state = 614 
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
            super(PParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(PParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PParser.RULE_assertion

        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = PParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617 
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
        self.enterRule(localctx, 44, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619 
            localctx.name = self.variable_identifier()
            self.state = 620
            self.match(PParser.COLON)
            self.state = 621 
            localctx.typ = self.category_or_any_type()
            self.state = 626
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 622
                self.match(PParser.LPAR)
                self.state = 623 
                localctx.attrs = self.attribute_list()
                self.state = 624
                self.match(PParser.RPAR)


            self.state = 630
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 628
                self.match(PParser.EQ)
                self.state = 629 
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
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 647
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = PParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 632 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = PParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 633 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = PParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 634 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = PParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 635 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 5:
                localctx = PParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 636 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 6:
                localctx = PParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 637 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 7:
                localctx = PParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 638 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 8:
                localctx = PParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 639 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 9:
                localctx = PParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 640 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 10:
                localctx = PParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 641 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 11:
                localctx = PParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 642 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 12:
                localctx = PParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 643 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 13:
                localctx = PParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 644 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 14:
                localctx = PParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 645 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 15:
                localctx = PParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 646 
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
        self.enterRule(localctx, 48, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649 
            localctx.method = self.method_selector()
            self.state = 650
            self.match(PParser.LPAR)
            self.state = 652
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 651 
                localctx.args = self.argument_assignment_list(0)


            self.state = 654
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
        self.enterRule(localctx, 50, self.RULE_method_selector)
        try:
            self.state = 661
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = PParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 656 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = PParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 657 
                localctx.parent = self.callable_parent(0)
                self.state = 658
                self.match(PParser.DOT)
                self.state = 659 
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 664 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 670
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CallableSelectorContext(self, PParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 666
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 667 
                    localctx.select = self.callable_selector() 
                self.state = 672
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_callable_selector)
        try:
            self.state = 679
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.match(PParser.DOT)
                self.state = 674 
                localctx.name = self.variable_identifier()

            elif token in [PParser.LBRAK]:
                localctx = PParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 675
                self.match(PParser.LBRAK)
                self.state = 676 
                localctx.exp = self.expression(0)
                self.state = 677
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
        self.enterRule(localctx, 56, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(PParser.WITH)
            self.state = 682 
            localctx.stmt = self.assign_variable_statement()
            self.state = 683
            self.match(PParser.COLON)
            self.state = 684 
            self.indent()
            self.state = 685 
            localctx.stmts = self.statement_list(0)
            self.state = 686 
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
        self.enterRule(localctx, 58, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(PParser.WITH)
            self.state = 689 
            localctx.typ = self.type_identifier()
            self.state = 690
            self.match(PParser.COLON)
            self.state = 691 
            self.indent()
            self.state = 692 
            localctx.stmts = self.statement_list(0)
            self.state = 693 
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
        self.enterRule(localctx, 60, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            self.match(PParser.SWITCH)
            self.state = 696
            self.match(PParser.ON)
            self.state = 697 
            localctx.exp = self.expression(0)
            self.state = 698
            self.match(PParser.COLON)
            self.state = 699 
            self.indent()
            self.state = 700 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 708
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 701 
                self.lfp()
                self.state = 702
                self.match(PParser.OTHERWISE)
                self.state = 703
                self.match(PParser.COLON)
                self.state = 704 
                self.indent()
                self.state = 705 
                localctx.stmts = self.statement_list(0)
                self.state = 706 
                self.dedent()


            self.state = 710 
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
        self.enterRule(localctx, 62, self.RULE_switch_case_statement)
        try:
            self.state = 727
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = PParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 712
                self.match(PParser.WHEN)
                self.state = 713 
                localctx.exp = self.atomic_literal()
                self.state = 714
                self.match(PParser.COLON)
                self.state = 715 
                self.indent()
                self.state = 716 
                localctx.stmts = self.statement_list(0)
                self.state = 717 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = PParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 719
                self.match(PParser.WHEN)
                self.state = 720
                self.match(PParser.IN)
                self.state = 721 
                localctx.exp = self.literal_collection()
                self.state = 722
                self.match(PParser.COLON)
                self.state = 723 
                self.indent()
                self.state = 724 
                localctx.stmts = self.statement_list(0)
                self.state = 725 
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
        self.enterRule(localctx, 64, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.match(PParser.FOR)
            self.state = 730 
            localctx.name1 = self.variable_identifier()
            self.state = 733
            _la = self._input.LA(1)
            if _la==PParser.COMMA:
                self.state = 731
                self.match(PParser.COMMA)
                self.state = 732 
                localctx.name2 = self.variable_identifier()


            self.state = 735
            self.match(PParser.IN)
            self.state = 736 
            localctx.source = self.expression(0)
            self.state = 737
            self.match(PParser.COLON)
            self.state = 738 
            self.indent()
            self.state = 739 
            localctx.stmts = self.statement_list(0)
            self.state = 740 
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
        self.enterRule(localctx, 66, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            self.match(PParser.DO)
            self.state = 743
            self.match(PParser.COLON)
            self.state = 744 
            self.indent()
            self.state = 745 
            localctx.stmts = self.statement_list(0)
            self.state = 746 
            self.dedent()
            self.state = 747 
            self.lfp()
            self.state = 748
            self.match(PParser.WHILE)
            self.state = 749 
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
        self.enterRule(localctx, 68, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self.match(PParser.WHILE)
            self.state = 752 
            localctx.exp = self.expression(0)
            self.state = 753
            self.match(PParser.COLON)
            self.state = 754 
            self.indent()
            self.state = 755 
            localctx.stmts = self.statement_list(0)
            self.state = 756 
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
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            self.match(PParser.IF)
            self.state = 759 
            localctx.exp = self.expression(0)
            self.state = 760
            self.match(PParser.COLON)
            self.state = 761 
            self.indent()
            self.state = 762 
            localctx.stmts = self.statement_list(0)
            self.state = 763 
            self.dedent()
            self.state = 767
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 764 
                self.lfp()
                self.state = 765 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 776
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 769 
                self.lfp()
                self.state = 770
                self.match(PParser.ELSE)
                self.state = 771
                self.match(PParser.COLON)
                self.state = 772 
                self.indent()
                self.state = 773 
                localctx.elseStmts = self.statement_list(0)
                self.state = 774 
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 779
            self.match(PParser.ELSE)
            self.state = 780
            self.match(PParser.IF)
            self.state = 781 
            localctx.exp = self.expression(0)
            self.state = 782
            self.match(PParser.COLON)
            self.state = 783 
            self.indent()
            self.state = 784 
            localctx.stmts = self.statement_list(0)
            self.state = 785 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 799
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ElseIfStatementListItemContext(self, PParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 787
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 788 
                    self.lfp()
                    self.state = 789
                    self.match(PParser.ELSE)
                    self.state = 790
                    self.match(PParser.IF)
                    self.state = 791 
                    localctx.exp = self.expression(0)
                    self.state = 792
                    self.match(PParser.COLON)
                    self.state = 793 
                    self.indent()
                    self.state = 794 
                    localctx.stmts = self.statement_list(0)
                    self.state = 795 
                    self.dedent() 
                self.state = 801
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
            self.match(PParser.RAISE)
            self.state = 803 
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
        self.enterRule(localctx, 76, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 805
            self.match(PParser.TRY)
            self.state = 806 
            localctx.name = self.variable_identifier()
            self.state = 807
            self.match(PParser.COLON)
            self.state = 808 
            self.indent()
            self.state = 809 
            localctx.stmts = self.statement_list(0)
            self.state = 810 
            self.dedent()
            self.state = 811 
            self.lfs()
            self.state = 813
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 812 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 822
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 815
                self.match(PParser.EXCEPT)
                self.state = 816
                self.match(PParser.COLON)
                self.state = 817 
                self.indent()
                self.state = 818 
                localctx.anyStmts = self.statement_list(0)
                self.state = 819 
                self.dedent()
                self.state = 820 
                self.lfs()


            self.state = 831
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 824
                self.match(PParser.FINALLY)
                self.state = 825
                self.match(PParser.COLON)
                self.state = 826 
                self.indent()
                self.state = 827 
                localctx.finalStmts = self.statement_list(0)
                self.state = 828 
                self.dedent()
                self.state = 829 
                self.lfs()


            self.state = 833 
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
        self.enterRule(localctx, 78, self.RULE_catch_statement)
        try:
            self.state = 854
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = PParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 835
                self.match(PParser.EXCEPT)
                self.state = 836 
                localctx.name = self.symbol_identifier()
                self.state = 837
                self.match(PParser.COLON)
                self.state = 838 
                self.indent()
                self.state = 839 
                localctx.stmts = self.statement_list(0)
                self.state = 840 
                self.dedent()
                self.state = 841 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = PParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 843
                self.match(PParser.EXCEPT)
                self.state = 844
                self.match(PParser.IN)
                self.state = 845
                self.match(PParser.LBRAK)
                self.state = 846 
                localctx.exp = self.symbol_list(0)
                self.state = 847
                self.match(PParser.RBRAK)
                self.state = 848
                self.match(PParser.COLON)
                self.state = 849 
                self.indent()
                self.state = 850 
                localctx.stmts = self.statement_list(0)
                self.state = 851 
                self.dedent()
                self.state = 852 
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
        self.enterRule(localctx, 80, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 856
            self.match(PParser.RETURN)
            self.state = 858
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 857 
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = PParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 861
                self.match(PParser.MINUS)
                self.state = 862 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 2:
                localctx = PParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 863
                self.match(PParser.NOT)
                self.state = 864 
                localctx.exp = self.expression(30)
                pass

            elif la_ == 3:
                localctx = PParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 865 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = PParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 866 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = PParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 867
                self.match(PParser.CODE)
                self.state = 868
                self.match(PParser.LPAR)
                self.state = 869 
                localctx.exp = self.expression(0)
                self.state = 870
                self.match(PParser.RPAR)
                pass

            elif la_ == 6:
                localctx = PParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 872
                self.match(PParser.EXECUTE)
                self.state = 873
                self.match(PParser.LPAR)
                self.state = 874 
                localctx.name = self.variable_identifier()
                self.state = 875
                self.match(PParser.RPAR)
                pass

            elif la_ == 7:
                localctx = PParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 877 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 976
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 974
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = PParser.MultiplyExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 880
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 881 
                        self.multiply()
                        self.state = 882 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 2:
                        localctx = PParser.DivideExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 884
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 885 
                        self.divide()
                        self.state = 886 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 3:
                        localctx = PParser.ModuloExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 888
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 889 
                        self.modulo()
                        self.state = 890 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 4:
                        localctx = PParser.IntDivideExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 892
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 893 
                        self.idivide()
                        self.state = 894 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 5:
                        localctx = PParser.AddExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 896
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 897
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PParser.PLUS or _la==PParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 898 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 6:
                        localctx = PParser.LessThanExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 899
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 900
                        self.match(PParser.LT)
                        self.state = 901 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 7:
                        localctx = PParser.LessThanOrEqualExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 902
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 903
                        self.match(PParser.LTE)
                        self.state = 904 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 8:
                        localctx = PParser.GreaterThanExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 905
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 906
                        self.match(PParser.GT)
                        self.state = 907 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 9:
                        localctx = PParser.GreaterThanOrEqualExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 908
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 909
                        self.match(PParser.GTE)
                        self.state = 910 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 10:
                        localctx = PParser.EqualsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 911
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 912
                        self.match(PParser.EQ2)
                        self.state = 913 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 11:
                        localctx = PParser.NotEqualsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 914
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 915
                        self.match(PParser.XEQ)
                        self.state = 916 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 12:
                        localctx = PParser.RoughlyEqualsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 917
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 918
                        self.match(PParser.TEQ)
                        self.state = 919 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 13:
                        localctx = PParser.OrExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 920
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 921
                        self.match(PParser.OR)
                        self.state = 922 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 14:
                        localctx = PParser.AndExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 923
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 924
                        self.match(PParser.AND)
                        self.state = 925 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 15:
                        localctx = PParser.TernaryExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 926
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 927
                        self.match(PParser.IF)
                        self.state = 928 
                        localctx.test = self.expression(0)
                        self.state = 929
                        self.match(PParser.ELSE)
                        self.state = 930 
                        localctx.ifFalse = self.expression(14)
                        pass

                    elif la_ == 16:
                        localctx = PParser.InExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 932
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 933
                        self.match(PParser.IN)
                        self.state = 934 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 17:
                        localctx = PParser.ContainsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 935
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 936
                        self.match(PParser.CONTAINS)
                        self.state = 937 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 18:
                        localctx = PParser.ContainsAllExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 938
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 939
                        self.match(PParser.CONTAINS)
                        self.state = 940
                        self.match(PParser.ALL)
                        self.state = 941 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 19:
                        localctx = PParser.ContainsAnyExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 942
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 943
                        self.match(PParser.CONTAINS)
                        self.state = 944
                        self.match(PParser.ANY)
                        self.state = 945 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 20:
                        localctx = PParser.NotInExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 946
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 947
                        self.match(PParser.NOT)
                        self.state = 948
                        self.match(PParser.IN)
                        self.state = 949 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 21:
                        localctx = PParser.NotContainsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 950
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 951
                        self.match(PParser.NOT)
                        self.state = 952
                        self.match(PParser.CONTAINS)
                        self.state = 953 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 22:
                        localctx = PParser.NotContainsAllExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 954
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 955
                        self.match(PParser.NOT)
                        self.state = 956
                        self.match(PParser.CONTAINS)
                        self.state = 957
                        self.match(PParser.ALL)
                        self.state = 958 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 23:
                        localctx = PParser.NotContainsAnyExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 959
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 960
                        self.match(PParser.NOT)
                        self.state = 961
                        self.match(PParser.CONTAINS)
                        self.state = 962
                        self.match(PParser.ANY)
                        self.state = 963 
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 24:
                        localctx = PParser.IsNotExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 964
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 965
                        self.match(PParser.IS)
                        self.state = 966
                        self.match(PParser.NOT)
                        self.state = 967 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 25:
                        localctx = PParser.IsExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 968
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 969
                        self.match(PParser.IS)
                        self.state = 970 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = PParser.CastExpressionContext(self, PParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 971
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 972
                        self.match(PParser.AS)
                        self.state = 973 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 978
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 979 
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 982 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 988
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.SelectorExpressionContext(self, PParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 984
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 985 
                    localctx.selector = self.instance_selector() 
                self.state = 990
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_method_expression)
        try:
            self.state = 997
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = PParser.DocumentExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 991 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 2:
                localctx = PParser.FetchExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 992 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 3:
                localctx = PParser.ReadExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 993 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 4:
                localctx = PParser.SortedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 994 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 5:
                localctx = PParser.MethodCallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 995 
                localctx.exp = self.method_call()
                pass

            elif la_ == 6:
                localctx = PParser.ConstructorExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 996 
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
        self.enterRule(localctx, 90, self.RULE_instance_selector)
        try:
            self.state = 1012
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = PParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 999
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1000
                self.match(PParser.DOT)
                self.state = 1001 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = PParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1002
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1003
                self.match(PParser.LBRAK)
                self.state = 1004 
                localctx.xslice = self.slice_arguments()
                self.state = 1005
                self.match(PParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = PParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1007
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1008
                self.match(PParser.LBRAK)
                self.state = 1009 
                localctx.exp = self.expression(0)
                self.state = 1010
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
        self.enterRule(localctx, 92, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1014 
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
        self.enterRule(localctx, 94, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1016 
            localctx.typ = self.category_type()
            self.state = 1017
            self.match(PParser.LPAR)
            self.state = 1019
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1018 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1021
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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1028
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = PParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1024 
                localctx.exp = self.expression(0)
                self.state = 1025
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = PParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1027 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1035
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ArgumentAssignmentListItemContext(self, PParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1030
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1031
                    self.match(PParser.COMMA)
                    self.state = 1032 
                    localctx.item = self.argument_assignment() 
                self.state = 1037
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 98, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1038 
            localctx.name = self.variable_identifier()
            self.state = 1039 
            self.assign()
            self.state = 1040 
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
        self.enterRule(localctx, 100, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1042
            self.match(PParser.READ)
            self.state = 1043
            self.match(PParser.FROM)
            self.state = 1044 
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
        self.enterRule(localctx, 102, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1046
            self.match(PParser.WRITE)
            self.state = 1047 
            localctx.what = self.expression(0)
            self.state = 1048
            self.match(PParser.TO)
            self.state = 1049 
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
        self.enterRule(localctx, 104, self.RULE_fetch_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1051
            self.match(PParser.FETCH)
            self.state = 1052 
            localctx.name = self.variable_identifier()
            self.state = 1053
            self.match(PParser.FROM)
            self.state = 1054 
            localctx.source = self.expression(0)
            self.state = 1055
            self.match(PParser.WHERE)
            self.state = 1056 
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
        self.enterRule(localctx, 106, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1058
            self.match(PParser.SORTED)
            self.state = 1059
            self.match(PParser.LPAR)
            self.state = 1060 
            localctx.source = self.instance_expression(0)
            self.state = 1066
            _la = self._input.LA(1)
            if _la==PParser.COMMA:
                self.state = 1061
                self.match(PParser.COMMA)
                self.state = 1062 
                self.key_token()
                self.state = 1063
                self.match(PParser.EQ)
                self.state = 1064 
                localctx.key = self.instance_expression(0)


            self.state = 1068
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
        self.enterRule(localctx, 108, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1070 
            localctx.inst = self.assignable_instance(0)
            self.state = 1071 
            self.assign()
            self.state = 1072 
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
        self.enterRule(localctx, 110, self.RULE_child_instance)
        try:
            self.state = 1082
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = PParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1074
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1075
                self.match(PParser.DOT)
                self.state = 1076 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = PParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1077
                if not self.wasNot(PParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(PParser.WS)")
                self.state = 1078
                self.match(PParser.LBRAK)
                self.state = 1079 
                localctx.exp = self.expression(0)
                self.state = 1080
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
        self.enterRule(localctx, 112, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1084 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1085 
            self.assign()
            self.state = 1086 
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
        self.enterRule(localctx, 114, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1091
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1088
                    self.match(PParser.LF) 
                self.state = 1093
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
        self.enterRule(localctx, 116, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1095 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1094
                self.match(PParser.LF)
                self.state = 1097 
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
        self.enterRule(localctx, 118, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1099
                self.match(PParser.LF)
                self.state = 1102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PParser.LF):
                    break

            self.state = 1104
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
        self.enterRule(localctx, 120, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PParser.LF:
                self.state = 1106
                self.match(PParser.LF)
                self.state = 1111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1112
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
        self.enterRule(localctx, 122, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1114
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
        self.enterRule(localctx, 124, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = PParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1117
            _la = self._input.LA(1)
            if ((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (PParser.ABSTRACT - 62)) | (1 << (PParser.ATTR - 62)) | (1 << (PParser.CATEGORY - 62)) | (1 << (PParser.CLASS - 62)) | (1 << (PParser.DEF - 62)) | (1 << (PParser.ENUM - 62)) | (1 << (PParser.NATIVE - 62)) | (1 << (PParser.SINGLETON - 62)))) != 0):
                self.state = 1116 
                localctx.items = self.declarations(0)


            self.state = 1119 
            self.lfs()
            self.state = 1120
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
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1123 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.DeclarationListItemContext(self, PParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1125
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1126 
                    self.lfp()
                    self.state = 1127 
                    localctx.item = self.declaration() 
                self.state = 1133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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
        self.enterRule(localctx, 128, self.RULE_declaration)
        try:
            self.state = 1139
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = PParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1134 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1135 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = PParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1136 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = PParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1137 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = PParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1138 
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
        self.enterRule(localctx, 130, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1141 
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
        self.enterRule(localctx, 132, self.RULE_enum_declaration)
        try:
            self.state = 1145
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = PParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1143 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1144 
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
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1148 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.NativeSymbolListItemContext(self, PParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1150
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1151 
                    self.lfp()
                    self.state = 1152 
                    localctx.item = self.native_symbol() 
                self.state = 1158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1160 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CategorySymbolListItemContext(self, PParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1163 
                    self.lfp()
                    self.state = 1164 
                    localctx.item = self.category_symbol() 
                self.state = 1170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1172 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.SymbolListItemContext(self, PParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1174
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1175
                    self.match(PParser.COMMA)
                    self.state = 1176 
                    localctx.item = self.symbol_identifier() 
                self.state = 1181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        self.enterRule(localctx, 140, self.RULE_attribute_constraint)
        try:
            self.state = 1192
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = PParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1182
                self.match(PParser.IN)
                self.state = 1183 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = PParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1184
                self.match(PParser.IN)
                self.state = 1185 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = PParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1186
                self.match(PParser.IN)
                self.state = 1187 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = PParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1188
                self.match(PParser.MATCHING)
                self.state = 1189
                localctx.text = self.match(PParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = PParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1190
                self.match(PParser.MATCHING)
                self.state = 1191 
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
        self.enterRule(localctx, 142, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1194
            self.match(PParser.LBRAK)
            self.state = 1196
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1195 
                localctx.items = self.expression_list(0)


            self.state = 1198
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
        self.enterRule(localctx, 144, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1200
            self.match(PParser.LT)
            self.state = 1202
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1201 
                localctx.items = self.expression_list(0)


            self.state = 1204
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
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1207 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ValueListItemContext(self, PParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1209
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1210
                    self.match(PParser.COMMA)
                    self.state = 1211 
                    localctx.item = self.expression(0) 
                self.state = 1216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

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
        self.enterRule(localctx, 148, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1217
            self.match(PParser.LBRAK)
            self.state = 1218 
            localctx.low = self.expression(0)
            self.state = 1219
            self.match(PParser.RANGE)
            self.state = 1220 
            localctx.high = self.expression(0)
            self.state = 1221
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
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1224 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1234
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        localctx = PParser.SetTypeContext(self, PParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1226
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1227
                        self.match(PParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = PParser.ListTypeContext(self, PParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1228
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1229
                        self.match(PParser.LBRAK)
                        self.state = 1230
                        self.match(PParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = PParser.DictTypeContext(self, PParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1231
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1232
                        self.match(PParser.LCURL)
                        self.state = 1233
                        self.match(PParser.RCURL)
                        pass

             
                self.state = 1238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

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
        self.enterRule(localctx, 152, self.RULE_primary_type)
        try:
            self.state = 1241
            token = self._input.LA(1)
            if token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.CODE]:
                localctx = PParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1239 
                localctx.n = self.native_type()

            elif token in [PParser.TYPE_IDENTIFIER]:
                localctx = PParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1240 
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
        self.enterRule(localctx, 154, self.RULE_native_type)
        try:
            self.state = 1253
            token = self._input.LA(1)
            if token in [PParser.BOOLEAN]:
                localctx = PParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1243
                localctx.t1 = self.match(PParser.BOOLEAN)

            elif token in [PParser.CHARACTER]:
                localctx = PParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1244
                localctx.t1 = self.match(PParser.CHARACTER)

            elif token in [PParser.TEXT]:
                localctx = PParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1245
                localctx.t1 = self.match(PParser.TEXT)

            elif token in [PParser.INTEGER]:
                localctx = PParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1246
                localctx.t1 = self.match(PParser.INTEGER)

            elif token in [PParser.DECIMAL]:
                localctx = PParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1247
                localctx.t1 = self.match(PParser.DECIMAL)

            elif token in [PParser.DATE]:
                localctx = PParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1248
                localctx.t1 = self.match(PParser.DATE)

            elif token in [PParser.DATETIME]:
                localctx = PParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1249
                localctx.t1 = self.match(PParser.DATETIME)

            elif token in [PParser.TIME]:
                localctx = PParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1250
                localctx.t1 = self.match(PParser.TIME)

            elif token in [PParser.PERIOD]:
                localctx = PParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1251
                localctx.t1 = self.match(PParser.PERIOD)

            elif token in [PParser.CODE]:
                localctx = PParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1252
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
        self.enterRule(localctx, 156, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1255
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
        self.enterRule(localctx, 158, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1257
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
        self.enterRule(localctx, 160, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259
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
        self.enterRule(localctx, 162, self.RULE_category_declaration)
        try:
            self.state = 1264
            token = self._input.LA(1)
            if token in [PParser.CATEGORY, PParser.CLASS]:
                localctx = PParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1261 
                localctx.decl = self.concrete_category_declaration()

            elif token in [PParser.NATIVE]:
                localctx = PParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1262 
                localctx.decl = self.native_category_declaration()

            elif token in [PParser.SINGLETON]:
                localctx = PParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1263 
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
        _startState = 164
        self.enterRecursionRule(localctx, 164, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1267 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.TypeIdentifierListItemContext(self, PParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1269
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1270
                    self.match(PParser.COMMA)
                    self.state = 1271 
                    localctx.item = self.type_identifier() 
                self.state = 1276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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
        self.enterRule(localctx, 166, self.RULE_method_identifier)
        try:
            self.state = 1279
            token = self._input.LA(1)
            if token in [PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1277 
                localctx.name = self.variable_identifier()

            elif token in [PParser.TYPE_IDENTIFIER]:
                localctx = PParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1278 
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
        self.enterRule(localctx, 168, self.RULE_identifier)
        try:
            self.state = 1284
            token = self._input.LA(1)
            if token in [PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1281 
                localctx.name = self.variable_identifier()

            elif token in [PParser.TYPE_IDENTIFIER]:
                localctx = PParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1282 
                localctx.name = self.type_identifier()

            elif token in [PParser.SYMBOL_IDENTIFIER]:
                localctx = PParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1283 
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
        self.enterRule(localctx, 170, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1286
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
        self.enterRule(localctx, 172, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1288
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
        self.enterRule(localctx, 174, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1290
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
        _startState = 176
        self.enterRecursionRule(localctx, 176, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1293 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ArgumentListItemContext(self, PParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1295
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1296
                    self.match(PParser.COMMA)
                    self.state = 1297 
                    localctx.item = self.argument() 
                self.state = 1302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

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
        self.enterRule(localctx, 178, self.RULE_argument)
        try:
            self.state = 1305
            token = self._input.LA(1)
            if token in [PParser.CODE]:
                localctx = PParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1303 
                localctx.arg = self.code_argument()

            elif token in [PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1304 
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
        self.enterRule(localctx, 180, self.RULE_operator_argument)
        try:
            self.state = 1309
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                localctx = PParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1307 
                localctx.arg = self.named_argument()
                pass

            elif la_ == 2:
                localctx = PParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1308 
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
        self.enterRule(localctx, 182, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1311 
            localctx.name = self.variable_identifier()
            self.state = 1314
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 1312
                self.match(PParser.EQ)
                self.state = 1313 
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
        self.enterRule(localctx, 184, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1316 
            self.code_type()
            self.state = 1317 
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
        self.enterRule(localctx, 186, self.RULE_category_or_any_type)
        try:
            self.state = 1321
            token = self._input.LA(1)
            if token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.CODE, PParser.TYPE_IDENTIFIER]:
                localctx = PParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1319 
                localctx.typ = self.typedef(0)

            elif token in [PParser.ANY]:
                localctx = PParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1320 
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
        _startState = 188
        self.enterRecursionRule(localctx, 188, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1324
            self.match(PParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1332
                    la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                    if la_ == 1:
                        localctx = PParser.AnyListTypeContext(self, PParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1326
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1327
                        self.match(PParser.LBRAK)
                        self.state = 1328
                        self.match(PParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = PParser.AnyDictTypeContext(self, PParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1329
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1330
                        self.match(PParser.LCURL)
                        self.state = 1331
                        self.match(PParser.RCURL)
                        pass

             
                self.state = 1336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

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
        _startState = 190
        self.enterRecursionRule(localctx, 190, self.RULE_category_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1338 
            localctx.item = self.category_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CategoryMethodListItemContext(self, PParser.Category_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_method_declaration_list)
                    self.state = 1340
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1341 
                    self.lfp()
                    self.state = 1342 
                    localctx.item = self.category_method_declaration() 
                self.state = 1348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
        self.enterRule(localctx, 192, self.RULE_category_method_declaration)
        try:
            self.state = 1353
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = PParser.SetterMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1349 
                localctx.decl = self.setter_method_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.GetterMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1350 
                localctx.decl = self.getter_method_declaration()
                pass

            elif la_ == 3:
                localctx = PParser.MemberMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1351 
                localctx.decl = self.member_method_declaration()
                pass

            elif la_ == 4:
                localctx = PParser.OperatorMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1352 
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
        self.enterRule(localctx, 194, self.RULE_native_category_mapping)
        try:
            self.state = 1365
            token = self._input.LA(1)
            if token in [PParser.JAVA]:
                localctx = PParser.JavaCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1355
                self.match(PParser.JAVA)
                self.state = 1356 
                localctx.mapping = self.java_class_identifier_expression(0)

            elif token in [PParser.CSHARP]:
                localctx = PParser.CSharpCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1357
                self.match(PParser.CSHARP)
                self.state = 1358 
                localctx.mapping = self.csharp_identifier_expression(0)

            elif token in [PParser.PYTHON2]:
                localctx = PParser.Python2CategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1359
                self.match(PParser.PYTHON2)
                self.state = 1360 
                localctx.mapping = self.python_category_mapping()

            elif token in [PParser.PYTHON3]:
                localctx = PParser.Python3CategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1361
                self.match(PParser.PYTHON3)
                self.state = 1362 
                localctx.mapping = self.python_category_mapping()

            elif token in [PParser.JAVASCRIPT]:
                localctx = PParser.JavaScriptCategoryMappingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1363
                self.match(PParser.JAVASCRIPT)
                self.state = 1364 
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
        self.enterRule(localctx, 196, self.RULE_python_category_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1367 
            localctx.id_ = self.identifier()
            self.state = 1369
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 1368 
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
        self.enterRule(localctx, 198, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1371
            self.match(PParser.FROM)
            self.state = 1372 
            self.module_token()
            self.state = 1373
            self.match(PParser.COLON)
            self.state = 1374 
            self.identifier()
            self.state = 1379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1375
                    self.match(PParser.DOT)
                    self.state = 1376 
                    self.identifier() 
                self.state = 1381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

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
        self.enterRule(localctx, 200, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1382
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1383
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
        self.enterRule(localctx, 202, self.RULE_javascript_category_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1385 
            localctx.id_ = self.identifier()
            self.state = 1387
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 1386 
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

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(PParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(PParser.Javascript_identifierContext,i)


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
        self.enterRule(localctx, 204, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1389
            self.match(PParser.FROM)
            self.state = 1390 
            self.module_token()
            self.state = 1391
            self.match(PParser.COLON)
            self.state = 1393
            _la = self._input.LA(1)
            if _la==PParser.SLASH:
                self.state = 1392
                self.match(PParser.SLASH)


            self.state = 1395 
            self.javascript_identifier()
            self.state = 1400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1396
                    self.match(PParser.SLASH)
                    self.state = 1397 
                    self.javascript_identifier() 
                self.state = 1402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

            self.state = 1405
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.state = 1403
                self.match(PParser.DOT)
                self.state = 1404 
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
        _startState = 206
        self.enterRecursionRule(localctx, 206, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1408 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.VariableListItemContext(self, PParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1410
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1411
                    self.match(PParser.COMMA)
                    self.state = 1412 
                    localctx.item = self.variable_identifier() 
                self.state = 1417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

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


    class TestMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a PParser.Method_declarationContext)
            super(PParser.TestMethodContext, self).__init__(parser)
            self.decl = None # Test_method_declarationContext
            self.copyFrom(ctx)

        def test_method_declaration(self):
            return self.getTypedRuleContext(PParser.Test_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterTestMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitTestMethod(self)


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
        self.enterRule(localctx, 208, self.RULE_method_declaration)
        try:
            self.state = 1422
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                localctx = PParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1418 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = PParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1419 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = PParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1420 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = PParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1421 
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
        _startState = 210
        self.enterRecursionRule(localctx, 210, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1425 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.NativeStatementListItemContext(self, PParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1427
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1428 
                    self.lfp()
                    self.state = 1429 
                    localctx.item = self.native_statement() 
                self.state = 1435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

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
        self.enterRule(localctx, 212, self.RULE_native_statement)
        try:
            self.state = 1446
            token = self._input.LA(1)
            if token in [PParser.JAVA]:
                localctx = PParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1436
                self.match(PParser.JAVA)
                self.state = 1437 
                localctx.stmt = self.java_statement()

            elif token in [PParser.CSHARP]:
                localctx = PParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1438
                self.match(PParser.CSHARP)
                self.state = 1439 
                localctx.stmt = self.csharp_statement()

            elif token in [PParser.PYTHON2]:
                localctx = PParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1440
                self.match(PParser.PYTHON2)
                self.state = 1441 
                localctx.stmt = self.python_native_statement()

            elif token in [PParser.PYTHON3]:
                localctx = PParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1442
                self.match(PParser.PYTHON3)
                self.state = 1443 
                localctx.stmt = self.python_native_statement()

            elif token in [PParser.JAVASCRIPT]:
                localctx = PParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1444
                self.match(PParser.JAVASCRIPT)
                self.state = 1445 
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
        self.enterRule(localctx, 214, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1448 
            localctx.stmt = self.python_statement()
            self.state = 1450
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 1449
                self.match(PParser.SEMI)


            self.state = 1453
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 1452 
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
        self.enterRule(localctx, 216, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1455 
            localctx.stmt = self.javascript_statement()
            self.state = 1457
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.state = 1456
                self.match(PParser.SEMI)


            self.state = 1460
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.state = 1459 
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
        _startState = 218
        self.enterRecursionRule(localctx, 218, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1463 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.StatementListItemContext(self, PParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1465
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1466 
                    self.lfp()
                    self.state = 1467 
                    localctx.item = self.statement() 
                self.state = 1473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(PParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PParser.RULE_assertion_list

     
        def copyFrom(self, ctx):
            super(PParser.Assertion_listContext, self).copyFrom(ctx)


    class AssertionListItemContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Assertion_listContext)
            super(PParser.AssertionListItemContext, self).__init__(parser)
            self.items = None # Assertion_listContext
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(PParser.LfpContext,0)

        def assertion_list(self):
            return self.getTypedRuleContext(PParser.Assertion_listContext,0)

        def assertion(self):
            return self.getTypedRuleContext(PParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssertionListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssertionListItem(self)


    class AssertionListContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a PParser.Assertion_listContext)
            super(PParser.AssertionListContext, self).__init__(parser)
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def assertion(self):
            return self.getTypedRuleContext(PParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.enterAssertionList(self)

        def exitRule(self, listener):
            if isinstance( listener, PParserListener ):
                listener.exitAssertionList(self)



    def assertion_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PParser.Assertion_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 220
        self.enterRecursionRule(localctx, 220, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1475 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.AssertionListItemContext(self, PParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1477
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1478 
                    self.lfp()
                    self.state = 1479 
                    localctx.item = self.assertion() 
                self.state = 1485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

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
        _startState = 222
        self.enterRecursionRule(localctx, 222, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1487 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,98,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.SwitchCaseStatementListItemContext(self, PParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1489
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1490 
                    self.lfp()
                    self.state = 1491 
                    localctx.item = self.switch_case_statement() 
                self.state = 1497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,98,self._ctx)

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
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1499 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,99,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CatchStatementListItemContext(self, PParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1501
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1502 
                    self.lfp()
                    self.state = 1503 
                    localctx.item = self.catch_statement() 
                self.state = 1509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,99,self._ctx)

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
        self.enterRule(localctx, 226, self.RULE_literal_collection)
        try:
            self.state = 1524
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                localctx = PParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1510
                self.match(PParser.LBRAK)
                self.state = 1511 
                localctx.low = self.atomic_literal()
                self.state = 1512
                self.match(PParser.RANGE)
                self.state = 1513 
                localctx.high = self.atomic_literal()
                self.state = 1514
                self.match(PParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = PParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1516
                self.match(PParser.LBRAK)
                self.state = 1517 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1518
                self.match(PParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = PParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1520
                self.match(PParser.LT)
                self.state = 1521 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1522
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
        self.enterRule(localctx, 228, self.RULE_atomic_literal)
        try:
            self.state = 1539
            token = self._input.LA(1)
            if token in [PParser.MIN_INTEGER]:
                localctx = PParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1526
                localctx.t = self.match(PParser.MIN_INTEGER)

            elif token in [PParser.MAX_INTEGER]:
                localctx = PParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1527
                localctx.t = self.match(PParser.MAX_INTEGER)

            elif token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1528
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.HEXA_LITERAL]:
                localctx = PParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1529
                localctx.t = self.match(PParser.HEXA_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1530
                localctx.t = self.match(PParser.CHAR_LITERAL)

            elif token in [PParser.DATE_LITERAL]:
                localctx = PParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1531
                localctx.t = self.match(PParser.DATE_LITERAL)

            elif token in [PParser.TIME_LITERAL]:
                localctx = PParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1532
                localctx.t = self.match(PParser.TIME_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1533
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1534
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.DATETIME_LITERAL]:
                localctx = PParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1535
                localctx.t = self.match(PParser.DATETIME_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1536
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.PERIOD_LITERAL]:
                localctx = PParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1537
                localctx.t = self.match(PParser.PERIOD_LITERAL)

            elif token in [PParser.NONE]:
                localctx = PParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1538 
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
        _startState = 230
        self.enterRecursionRule(localctx, 230, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1542 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,102,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.LiteralListItemContext(self, PParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1544
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1545
                    self.match(PParser.COMMA)
                    self.state = 1546 
                    localctx.item = self.atomic_literal() 
                self.state = 1551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,102,self._ctx)

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
        self.enterRule(localctx, 232, self.RULE_selectable_expression)
        try:
            self.state = 1556
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                localctx = PParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1552 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = PParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1553 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = PParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1554 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = PParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1555 
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
        self.enterRule(localctx, 234, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1558
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
        self.enterRule(localctx, 236, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1560
            self.match(PParser.LPAR)
            self.state = 1561 
            localctx.exp = self.expression(0)
            self.state = 1562
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
        self.enterRule(localctx, 238, self.RULE_literal_expression)
        try:
            self.state = 1566
            token = self._input.LA(1)
            if token in [PParser.NONE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.MIN_INTEGER, PParser.MAX_INTEGER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.HEXA_LITERAL, PParser.DECIMAL_LITERAL, PParser.DATETIME_LITERAL, PParser.TIME_LITERAL, PParser.DATE_LITERAL, PParser.PERIOD_LITERAL]:
                localctx = PParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1564 
                localctx.exp = self.atomic_literal()

            elif token in [PParser.LPAR, PParser.LBRAK, PParser.LCURL, PParser.LT]:
                localctx = PParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1565 
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
        self.enterRule(localctx, 240, self.RULE_collection_literal)
        try:
            self.state = 1573
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                localctx = PParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1568 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = PParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1569 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = PParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1570 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = PParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1571 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = PParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1572 
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
        self.enterRule(localctx, 242, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1575
            self.match(PParser.LPAR)
            self.state = 1577
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1576 
                localctx.items = self.expression_tuple(0)


            self.state = 1579
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
        self.enterRule(localctx, 244, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1581
            self.match(PParser.LCURL)
            self.state = 1583
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.LBRAK) | (1 << PParser.LCURL) | (1 << PParser.MINUS) | (1 << PParser.LT) | (1 << PParser.CODE) | (1 << PParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (PParser.EXECUTE - 87)) | (1 << (PParser.FETCH - 87)) | (1 << (PParser.NONE - 87)) | (1 << (PParser.NOT - 87)) | (1 << (PParser.READ - 87)) | (1 << (PParser.SELF - 87)) | (1 << (PParser.SORTED - 87)) | (1 << (PParser.THIS - 87)) | (1 << (PParser.BOOLEAN_LITERAL - 87)) | (1 << (PParser.CHAR_LITERAL - 87)) | (1 << (PParser.MIN_INTEGER - 87)) | (1 << (PParser.MAX_INTEGER - 87)) | (1 << (PParser.SYMBOL_IDENTIFIER - 87)) | (1 << (PParser.TYPE_IDENTIFIER - 87)) | (1 << (PParser.VARIABLE_IDENTIFIER - 87)) | (1 << (PParser.TEXT_LITERAL - 87)) | (1 << (PParser.INTEGER_LITERAL - 87)) | (1 << (PParser.HEXA_LITERAL - 87)) | (1 << (PParser.DECIMAL_LITERAL - 87)) | (1 << (PParser.DATETIME_LITERAL - 87)) | (1 << (PParser.TIME_LITERAL - 87)) | (1 << (PParser.DATE_LITERAL - 87)) | (1 << (PParser.PERIOD_LITERAL - 87)))) != 0):
                self.state = 1582 
                localctx.items = self.dict_entry_list(0)


            self.state = 1585
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
        _startState = 246
        self.enterRecursionRule(localctx, 246, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1588 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1595
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,108,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ValueTupleItemContext(self, PParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1590
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1591
                    self.match(PParser.COMMA)
                    self.state = 1592 
                    localctx.item = self.expression(0) 
                self.state = 1597
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

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
        _startState = 248
        self.enterRecursionRule(localctx, 248, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1599 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1606
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,109,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.DictEntryListItemContext(self, PParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1601
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1602
                    self.match(PParser.COMMA)
                    self.state = 1603 
                    localctx.item = self.dict_entry() 
                self.state = 1608
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

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
        self.enterRule(localctx, 250, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1609 
            localctx.key = self.expression(0)
            self.state = 1610
            self.match(PParser.COLON)
            self.state = 1611 
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
        self.enterRule(localctx, 252, self.RULE_slice_arguments)
        try:
            self.state = 1622
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = PParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1613 
                localctx.first = self.expression(0)
                self.state = 1614
                self.match(PParser.COLON)
                self.state = 1615 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = PParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1617 
                localctx.first = self.expression(0)
                self.state = 1618
                self.match(PParser.COLON)
                pass

            elif la_ == 3:
                localctx = PParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1620
                self.match(PParser.COLON)
                self.state = 1621 
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
        self.enterRule(localctx, 254, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1624 
            localctx.name = self.variable_identifier()
            self.state = 1625 
            self.assign()
            self.state = 1626 
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
        _startState = 256
        self.enterRecursionRule(localctx, 256, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1629 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1635
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.ChildInstanceContext(self, PParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1631
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1632 
                    localctx.child = self.child_instance() 
                self.state = 1637
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

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
        self.enterRule(localctx, 258, self.RULE_is_expression)
        try:
            self.state = 1642
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                localctx = PParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1638
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1639
                self.match(PParser.VARIABLE_IDENTIFIER)
                self.state = 1640 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = PParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1641 
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
        self.enterRule(localctx, 260, self.RULE_operator)
        try:
            self.state = 1650
            token = self._input.LA(1)
            if token in [PParser.PLUS]:
                localctx = PParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1644
                self.match(PParser.PLUS)

            elif token in [PParser.MINUS]:
                localctx = PParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1645
                self.match(PParser.MINUS)

            elif token in [PParser.STAR]:
                localctx = PParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1646 
                self.multiply()

            elif token in [PParser.SLASH]:
                localctx = PParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1647 
                self.divide()

            elif token in [PParser.BSLASH]:
                localctx = PParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1648 
                self.idivide()

            elif token in [PParser.PERCENT, PParser.MODULO]:
                localctx = PParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1649 
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
        self.enterRule(localctx, 262, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1652
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1653
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
        self.enterRule(localctx, 264, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1655
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1656
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
        self.enterRule(localctx, 266, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1658
            localctx.i1 = self.match(PParser.VARIABLE_IDENTIFIER)
            self.state = 1659
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
        self.enterRule(localctx, 268, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1661
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
        self.enterRule(localctx, 270, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1663
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
        self.enterRule(localctx, 272, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1665
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
        self.enterRule(localctx, 274, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1667
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
        self.enterRule(localctx, 276, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1669
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
        self.enterRule(localctx, 278, self.RULE_javascript_statement)
        try:
            self.state = 1678
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1671
                self.match(PParser.RETURN)
                self.state = 1672 
                localctx.exp = self.javascript_expression(0)
                self.state = 1673
                self.match(PParser.SEMI)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1675 
                localctx.exp = self.javascript_expression(0)
                self.state = 1676
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
        _startState = 280
        self.enterRecursionRule(localctx, 280, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1681 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1687
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavascriptSelectorExpressionContext(self, PParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1683
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1684 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1689
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,115,self._ctx)

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
        self.enterRule(localctx, 282, self.RULE_javascript_primary_expression)
        try:
            self.state = 1693
            token = self._input.LA(1)
            if token in [PParser.LPAR]:
                localctx = PParser.JavascriptParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1690 
                localctx.exp = self.javascript_parenthesis_expression()

            elif token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.JavascriptIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1691 
                localctx.exp = self.javascript_identifier_expression(0)

            elif token in [PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavascriptLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1692 
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
        self.enterRule(localctx, 284, self.RULE_javascript_selector_expression)
        try:
            self.state = 1698
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.JavascriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1695
                self.match(PParser.DOT)
                self.state = 1696 
                localctx.exp = self.javascript_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.JavascriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1697 
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
        self.enterRule(localctx, 286, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1700 
            localctx.name = self.javascript_identifier()
            self.state = 1701
            self.match(PParser.LPAR)
            self.state = 1703
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.BOOLEAN_LITERAL - 116)) | (1 << (PParser.CHAR_LITERAL - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)) | (1 << (PParser.TEXT_LITERAL - 116)) | (1 << (PParser.INTEGER_LITERAL - 116)) | (1 << (PParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1702 
                localctx.args = self.javascript_arguments(0)


            self.state = 1705
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
        _startState = 288
        self.enterRecursionRule(localctx, 288, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1708 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1715
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavascriptArgumentListItemContext(self, PParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1710
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1711
                    self.match(PParser.COMMA)
                    self.state = 1712 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1717
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

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
        self.enterRule(localctx, 290, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1718
            self.match(PParser.LBRAK)
            self.state = 1719 
            localctx.exp = self.javascript_expression(0)
            self.state = 1720
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
        self.enterRule(localctx, 292, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1722
            self.match(PParser.LPAR)
            self.state = 1723 
            localctx.exp = self.javascript_expression(0)
            self.state = 1724
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
        _startState = 294
        self.enterRecursionRule(localctx, 294, self.RULE_javascript_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavascriptIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1727 
            localctx.name = self.javascript_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1734
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,120,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavascriptChildIdentifierContext(self, PParser.Javascript_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_identifier_expression)
                    self.state = 1729
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1730
                    self.match(PParser.DOT)
                    self.state = 1731 
                    localctx.name = self.javascript_identifier() 
                self.state = 1736
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,120,self._ctx)

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
        self.enterRule(localctx, 296, self.RULE_javascript_literal_expression)
        try:
            self.state = 1742
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1737
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1738
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1739
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1740
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1741
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

        def TEST(self):
            return self.getToken(PParser.TEST, 0)

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
        self.enterRule(localctx, 298, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1744
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self.enterRule(localctx, 300, self.RULE_python_statement)
        try:
            self.state = 1749
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1746
                self.match(PParser.RETURN)
                self.state = 1747 
                localctx.exp = self.python_expression(0)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1748 
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
        _startState = 302
        self.enterRecursionRule(localctx, 302, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1752 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1758
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonSelectorExpressionContext(self, PParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1754
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1755 
                    localctx.child = self.python_selector_expression() 
                self.state = 1760
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

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
        self.enterRule(localctx, 304, self.RULE_python_primary_expression)
        try:
            self.state = 1765
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                localctx = PParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1761 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = PParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1762 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = PParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1763 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = PParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1764 
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
        self.enterRule(localctx, 306, self.RULE_python_selector_expression)
        try:
            self.state = 1773
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1767
                self.match(PParser.DOT)
                self.state = 1768 
                localctx.exp = self.python_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1769
                self.match(PParser.LBRAK)
                self.state = 1770 
                localctx.exp = self.python_expression(0)
                self.state = 1771
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
        self.enterRule(localctx, 308, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1775 
            localctx.name = self.python_identifier()
            self.state = 1776
            self.match(PParser.LPAR)
            self.state = 1778
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.BOOLEAN_LITERAL - 116)) | (1 << (PParser.CHAR_LITERAL - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)) | (1 << (PParser.TEXT_LITERAL - 116)) | (1 << (PParser.INTEGER_LITERAL - 116)) | (1 << (PParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1777 
                localctx.args = self.python_argument_list()


            self.state = 1780
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
        self.enterRule(localctx, 310, self.RULE_python_argument_list)
        try:
            self.state = 1788
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                localctx = PParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1782 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = PParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1783 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = PParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1784 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1785
                self.match(PParser.COMMA)
                self.state = 1786 
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
        _startState = 312
        self.enterRecursionRule(localctx, 312, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1791 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1798
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonOrdinalArgumentListItemContext(self, PParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1793
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1794
                    self.match(PParser.COMMA)
                    self.state = 1795 
                    localctx.item = self.python_expression(0) 
                self.state = 1800
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

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
        _startState = 314
        self.enterRecursionRule(localctx, 314, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1802 
            localctx.name = self.python_identifier()
            self.state = 1803
            self.match(PParser.EQ)
            self.state = 1804 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1814
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonNamedArgumentListItemContext(self, PParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1806
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1807
                    self.match(PParser.COMMA)
                    self.state = 1808 
                    localctx.name = self.python_identifier()
                    self.state = 1809
                    self.match(PParser.EQ)
                    self.state = 1810 
                    localctx.exp = self.python_expression(0) 
                self.state = 1816
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

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
        self.enterRule(localctx, 316, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1817
            self.match(PParser.LPAR)
            self.state = 1818 
            localctx.exp = self.python_expression(0)
            self.state = 1819
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
        _startState = 318
        self.enterRecursionRule(localctx, 318, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.PythonIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1822 
            localctx.name = self.python_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1829
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.PythonChildIdentifierContext(self, PParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1824
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1825
                    self.match(PParser.DOT)
                    self.state = 1826 
                    localctx.name = self.python_identifier() 
                self.state = 1831
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

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
        self.enterRule(localctx, 320, self.RULE_python_literal_expression)
        try:
            self.state = 1837
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1832
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1833
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1834
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1835
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1836
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

        def READ(self):
            return self.getToken(PParser.READ, 0)

        def WRITE(self):
            return self.getToken(PParser.WRITE, 0)

        def TEST(self):
            return self.getToken(PParser.TEST, 0)

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
        self.enterRule(localctx, 322, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1839
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self.enterRule(localctx, 324, self.RULE_java_statement)
        try:
            self.state = 1848
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1841
                self.match(PParser.RETURN)
                self.state = 1842 
                localctx.exp = self.java_expression(0)
                self.state = 1843
                self.match(PParser.SEMI)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1845 
                localctx.exp = self.java_expression(0)
                self.state = 1846
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
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1851 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1857
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaSelectorExpressionContext(self, PParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 1853
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1854 
                    localctx.child = self.java_selector_expression() 
                self.state = 1859
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

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
        self.enterRule(localctx, 328, self.RULE_java_primary_expression)
        try:
            self.state = 1863
            token = self._input.LA(1)
            if token in [PParser.LPAR]:
                localctx = PParser.JavaParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1860 
                localctx.exp = self.java_parenthesis_expression()

            elif token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.JavaIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1861 
                localctx.exp = self.java_identifier_expression(0)

            elif token in [PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavaLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1862 
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
        self.enterRule(localctx, 330, self.RULE_java_selector_expression)
        try:
            self.state = 1868
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1865
                self.match(PParser.DOT)
                self.state = 1866 
                localctx.exp = self.java_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1867 
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
        self.enterRule(localctx, 332, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1870 
            localctx.name = self.java_identifier()
            self.state = 1871
            self.match(PParser.LPAR)
            self.state = 1873
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.BOOLEAN_LITERAL - 116)) | (1 << (PParser.CHAR_LITERAL - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)) | (1 << (PParser.TEXT_LITERAL - 116)) | (1 << (PParser.INTEGER_LITERAL - 116)) | (1 << (PParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1872 
                localctx.args = self.java_arguments(0)


            self.state = 1875
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
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1878 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1885
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaArgumentListItemContext(self, PParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 1880
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1881
                    self.match(PParser.COMMA)
                    self.state = 1882 
                    localctx.item = self.java_expression(0) 
                self.state = 1887
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

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
        self.enterRule(localctx, 336, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
            self.match(PParser.LBRAK)
            self.state = 1889 
            localctx.exp = self.java_expression(0)
            self.state = 1890
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
        self.enterRule(localctx, 338, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892
            self.match(PParser.LPAR)
            self.state = 1893 
            localctx.exp = self.java_expression(0)
            self.state = 1894
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
        _startState = 340
        self.enterRecursionRule(localctx, 340, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1897 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1904
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaChildIdentifierContext(self, PParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 1899
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1900
                    self.match(PParser.DOT)
                    self.state = 1901 
                    localctx.name = self.java_identifier() 
                self.state = 1906
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

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
        _startState = 342
        self.enterRecursionRule(localctx, 342, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1908 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1915
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.JavaChildClassIdentifierContext(self, PParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 1910
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1911
                    self.match(PParser.DOLLAR)
                    self.state = 1912
                    localctx.name = self.match(PParser.TYPE_IDENTIFIER) 
                self.state = 1917
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

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
        self.enterRule(localctx, 344, self.RULE_java_literal_expression)
        try:
            self.state = 1923
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1918
                localctx.t = self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1919
                localctx.t = self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1920
                localctx.t = self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1921
                localctx.t = self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1922
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

        def READ(self):
            return self.getToken(PParser.READ, 0)

        def WRITE(self):
            return self.getToken(PParser.WRITE, 0)

        def TEST(self):
            return self.getToken(PParser.TEST, 0)

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
        self.enterRule(localctx, 346, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1925
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self.enterRule(localctx, 348, self.RULE_csharp_statement)
        try:
            self.state = 1934
            token = self._input.LA(1)
            if token in [PParser.RETURN]:
                localctx = PParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1927
                self.match(PParser.RETURN)
                self.state = 1928 
                localctx.exp = self.csharp_expression(0)
                self.state = 1929
                self.match(PParser.SEMI)

            elif token in [PParser.LPAR, PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1931 
                localctx.exp = self.csharp_expression(0)
                self.state = 1932
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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1937 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1943
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,142,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CSharpSelectorExpressionContext(self, PParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 1939
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1940 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 1945
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,142,self._ctx)

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
        self.enterRule(localctx, 352, self.RULE_csharp_primary_expression)
        try:
            self.state = 1949
            token = self._input.LA(1)
            if token in [PParser.LPAR]:
                localctx = PParser.CSharpParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1946 
                localctx.exp = self.csharp_parenthesis_expression()

            elif token in [PParser.BOOLEAN, PParser.CHARACTER, PParser.TEXT, PParser.INTEGER, PParser.DECIMAL, PParser.DATE, PParser.TIME, PParser.DATETIME, PParser.PERIOD, PParser.READ, PParser.TEST, PParser.WRITE, PParser.SYMBOL_IDENTIFIER, PParser.TYPE_IDENTIFIER, PParser.VARIABLE_IDENTIFIER]:
                localctx = PParser.CSharpIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1947 
                localctx.exp = self.csharp_identifier_expression(0)

            elif token in [PParser.BOOLEAN_LITERAL, PParser.CHAR_LITERAL, PParser.TEXT_LITERAL, PParser.INTEGER_LITERAL, PParser.DECIMAL_LITERAL]:
                localctx = PParser.CSharpLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1948 
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
        self.enterRule(localctx, 354, self.RULE_csharp_selector_expression)
        try:
            self.state = 1954
            token = self._input.LA(1)
            if token in [PParser.DOT]:
                localctx = PParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1951
                self.match(PParser.DOT)
                self.state = 1952 
                localctx.exp = self.csharp_method_expression()

            elif token in [PParser.LBRAK]:
                localctx = PParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1953 
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
        self.enterRule(localctx, 356, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1956 
            localctx.name = self.csharp_identifier()
            self.state = 1957
            self.match(PParser.LPAR)
            self.state = 1959
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.LPAR) | (1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.BOOLEAN_LITERAL - 116)) | (1 << (PParser.CHAR_LITERAL - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)) | (1 << (PParser.TEXT_LITERAL - 116)) | (1 << (PParser.INTEGER_LITERAL - 116)) | (1 << (PParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1958 
                localctx.args = self.csharp_arguments(0)


            self.state = 1961
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
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1964 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1971
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CSharpArgumentListItemContext(self, PParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 1966
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1967
                    self.match(PParser.COMMA)
                    self.state = 1968 
                    localctx.item = self.csharp_expression(0) 
                self.state = 1973
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

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
        self.enterRule(localctx, 360, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            self.match(PParser.LBRAK)
            self.state = 1975 
            localctx.exp = self.csharp_expression(0)
            self.state = 1976
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
        self.enterRule(localctx, 362, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1978
            self.match(PParser.LPAR)
            self.state = 1979 
            localctx.exp = self.csharp_expression(0)
            self.state = 1980
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
        _startState = 364
        self.enterRecursionRule(localctx, 364, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PParser.CSharpIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1983 
            localctx.name = self.csharp_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1990
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,147,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PParser.CSharpChildIdentifierContext(self, PParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 1985
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1986
                    self.match(PParser.DOT)
                    self.state = 1987 
                    localctx.name = self.csharp_identifier() 
                self.state = 1992
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,147,self._ctx)

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
        self.enterRule(localctx, 366, self.RULE_csharp_literal_expression)
        try:
            self.state = 1998
            token = self._input.LA(1)
            if token in [PParser.INTEGER_LITERAL]:
                localctx = PParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1993
                self.match(PParser.INTEGER_LITERAL)

            elif token in [PParser.DECIMAL_LITERAL]:
                localctx = PParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1994
                self.match(PParser.DECIMAL_LITERAL)

            elif token in [PParser.TEXT_LITERAL]:
                localctx = PParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1995
                self.match(PParser.TEXT_LITERAL)

            elif token in [PParser.BOOLEAN_LITERAL]:
                localctx = PParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1996
                self.match(PParser.BOOLEAN_LITERAL)

            elif token in [PParser.CHAR_LITERAL]:
                localctx = PParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1997
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

        def READ(self):
            return self.getToken(PParser.READ, 0)

        def WRITE(self):
            return self.getToken(PParser.WRITE, 0)

        def TEST(self):
            return self.getToken(PParser.TEST, 0)

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
        self.enterRule(localctx, 368, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2000
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PParser.BOOLEAN) | (1 << PParser.CHARACTER) | (1 << PParser.TEXT) | (1 << PParser.INTEGER) | (1 << PParser.DECIMAL) | (1 << PParser.DATE) | (1 << PParser.TIME) | (1 << PParser.DATETIME) | (1 << PParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (PParser.READ - 116)) | (1 << (PParser.TEST - 116)) | (1 << (PParser.WRITE - 116)) | (1 << (PParser.SYMBOL_IDENTIFIER - 116)) | (1 << (PParser.TYPE_IDENTIFIER - 116)) | (1 << (PParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self._predicates[95] = self.category_method_declaration_list_sempred
        self._predicates[100] = self.module_token_sempred
        self._predicates[103] = self.variable_identifier_list_sempred
        self._predicates[105] = self.native_statement_list_sempred
        self._predicates[109] = self.statement_list_sempred
        self._predicates[110] = self.assertion_list_sempred
        self._predicates[111] = self.switch_case_statement_list_sempred
        self._predicates[112] = self.catch_statement_list_sempred
        self._predicates[115] = self.literal_list_literal_sempred
        self._predicates[123] = self.expression_tuple_sempred
        self._predicates[124] = self.dict_entry_list_sempred
        self._predicates[128] = self.assignable_instance_sempred
        self._predicates[129] = self.is_expression_sempred
        self._predicates[131] = self.key_token_sempred
        self._predicates[132] = self.value_token_sempred
        self._predicates[133] = self.symbols_token_sempred
        self._predicates[140] = self.javascript_expression_sempred
        self._predicates[144] = self.javascript_arguments_sempred
        self._predicates[147] = self.javascript_identifier_expression_sempred
        self._predicates[151] = self.python_expression_sempred
        self._predicates[156] = self.python_ordinal_argument_list_sempred
        self._predicates[157] = self.python_named_argument_list_sempred
        self._predicates[159] = self.python_identifier_expression_sempred
        self._predicates[163] = self.java_expression_sempred
        self._predicates[167] = self.java_arguments_sempred
        self._predicates[170] = self.java_identifier_expression_sempred
        self._predicates[171] = self.java_class_identifier_expression_sempred
        self._predicates[175] = self.csharp_expression_sempred
        self._predicates[179] = self.csharp_arguments_sempred
        self._predicates[182] = self.csharp_identifier_expression_sempred
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
         

    def assertion_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.willBeAOrAn()
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         

    def javascript_identifier_expression_sempred(self, localctx, predIndex):
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
         



