class pCss(object):
    def css(self):
        pass;

class pHtml(object):
    def getArgs(self, args):
        return ' '.join(args[1:]);
    def getInner(self, args):
        return ' '.join(args[:1]);
    def divStruct(self, *args):
        return ''.join(['<div ', self.getArgs(args),'>', self.getInner(args), '</div>']);
    def bodyStruct(self, *args):
        return ''.join(['<body ', self.getArgs(args),'>', self.getInner(args),'</body>']);
    def titleStruct(self, *args):
        return ''.join(['<title>',self.getInner(args),'</title>']);
    def headStruct(self, *args):
        return ''.join(['<head>',self.getInner(args),'</head>']);
    def htmlStruct(self, *args):
        return ''.join(['<html>',self.getInner(args),'</html>']);
    def heading(self, *args):
        return ''.join(['<h',self.getArgs(args),'>',self.getInner(args),'<h',self.getArgs(args),'>']);
    def paragraph(self, *args):
        return ''.join(['<p>', self.getInner(args), '</p>']);
    def lineBreak(self, *args):
        return ''.join([self.getInner(args), '<br>']);
    def sLink(self, *arg):
        return ''.join(['<link ', self.getInner(args), '/>'])
    def link(self, *args):
        return ''.join(['<a href="',self.getArgs(args),'">',self.getInner(args), '</a>']);
    def image(self, *args):
        return ''.join(['<img ',self.getInner(args),'>']);
    def span(self, *args):
        return ''.join(['<span ',self.getArgs(args),'>',self.getInner(args),'</span>']);
    def abbreviation(self, *args):
        return ''.join(['<abbr ', self.getArgs(args),'>',self.getInner(args),'</abbr>']);