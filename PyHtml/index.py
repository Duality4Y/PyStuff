import cgi
import pHtml

s = "%s"
Html = pHtml.pHtml();
div1 = Html.divStruct('Hello there!', 'align="Center"','style="color:#444444;"');

specialDiv = Html.divStruct('Hello there!', 'align="Center"', 'style="color:#00ff00"');
specialDiv2 = Html.divStruct('This is another Test Text here!','align="Left"', 'style="color:#00ffff"');
specialDiv3 = Html.divStruct('Trolololo test lol', 'align="Right"', 'style="color:#ff0f0f"');
specialDiv4 = Html.divStruct('first prime diff', 'align="center"', 'style=\"height:150; width:50; background-color:#ff00ff;\"');


bodyStruct = ''.join([specialDiv, specialDiv2, specialDiv3, specialDiv4]);
Body = Html.bodyStruct(bodyStruct, 'bgcolor="#444444"')
htmlDoc = Html.htmlStruct(Body);

def index(req):
    
    return s% htmlDoc;