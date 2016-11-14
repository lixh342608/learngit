package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import javax.servlet.http.Cookie;

public final class AppPanel_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.Vector _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public Object getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=utf-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("<!-- saved from url=(0014)about:internet -->\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("<!-- saved from url=(0014)about:internet -->\r\n");
      out.write("<html lang=\"en\">\r\n");
      out.write("\r\n");
      out.write("<!-- \r\n");
      out.write("Smart developers always View Source. \r\n");
      out.write("\r\n");
      out.write("This application was built using Adobe Flex, an open source framework\r\n");
      out.write("for building rich Internet applications that get delivered via the\r\n");
      out.write("Flash Player or to desktops via Adobe AIR. \r\n");
      out.write("\r\n");
      out.write("Learn more about Flex at http://flex.org \r\n");
      out.write("// -->\r\n");
      out.write("\r\n");
      out.write("<head>\r\n");
      out.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\r\n");
      out.write("\r\n");
      out.write("<!--  BEGIN Browser History required section -->\r\n");
      out.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"history/history.css\" />\r\n");
      out.write("<!--  END Browser History required section -->\r\n");
      out.write("\r\n");
      out.write("<title>电子商务供应链管理系统</title>\r\n");
      out.write("<script src=\"AC_OETags.js\" language=\"javascript\"></script>\r\n");
      out.write("<script src=\"ef.js\" language=\"javascript\"></script>\r\n");
      out.write("\r\n");
      out.write("<!--  BEGIN Browser History required section -->\r\n");
      out.write("<script src=\"history/history.js\" language=\"javascript\"></script>\r\n");
      out.write("<!--  END Browser History required section -->\r\n");
      out.write("\r\n");
      out.write("<!--  add by pengwei,BEGIN 蓝牙电子称脚本 ocx.js  -->\r\n");
      out.write("<script src=\"swf/lms/wms/pack/ocx.js?20131202\" language=\"javascript\"></script>\r\n");
      out.write("<!--  END  -->\r\n");
      out.write("\r\n");
      out.write("<style>\r\n");
      out.write("body { margin: 0px; overflow:hidden }\r\n");
      out.write(".apppanelCss {\r\n");
      out.write("\tposition: absolute;\r\n");
      out.write("\tz-index: 1;\r\n");
      out.write("}\r\n");
      out.write(".myFrameCss{\r\n");
      out.write("\tposition: absolute;\r\n");
      out.write("\tz-index: 2;\r\n");
      out.write("}\r\n");
      out.write("</style>\r\n");
      out.write("</head>\r\n");
      out.write("\r\n");
      out.write("<body scroll='no'>\r\n");
      out.write("<script language=\"JavaScript\" type=\"text/javascript\">\r\n");
      out.write("<!--\r\n");
      out.write("\t\tAC_FL_RunContent(\r\n");
      out.write("\t\t\t\t\t\"src\", \"AppPanel\",\r\n");
      out.write("\t\t\t\t\t\"width\", \"100%\",\r\n");
      out.write("\t\t\t\t\t\"height\", \"100%\",\r\n");
      out.write("\t\t\t\t\t\"align\", \"middle\",\r\n");
      out.write("\t\t\t\t\t\"id\", \"AppPanel\",\r\n");
      out.write("\t\t\t\t\t\"quality\", \"high\",\r\n");
      out.write("\t\t\t\t\t\"bgcolor\", \"#ffffff\",\r\n");
      out.write("\t\t\t\t\t\"name\", \"AppPanel\",\r\n");
      out.write("\t\t\t\t\t\"allowScriptAccess\",\"sameDomain\",\r\n");
      out.write("\t\t\t\t\t\"type\", \"application/x-shockwave-flash\",\r\n");
      out.write("\t\t\t\t\t\"pluginspage\", \"http://www.adobe.com/go/getflashplayer\"\r\n");
      out.write("\t);\r\n");
      out.write("// -->\r\n");
      out.write("function modifyAppPanel(state) {\r\n");
      out.write("\tvar panel = document.getElementById('AppPanel');\r\n");
      out.write("\tif(state=='1'){\r\n");
      out.write("\t\tpanel.className = '';\r\n");
      out.write("\t}else{\r\n");
      out.write("\t\tpanel.className = 'apppanelCss';\r\n");
      out.write("\t}\r\n");
      out.write("}\r\n");
      out.write("\r\n");
      out.write("function modifyMyFrame(){\r\n");
      out.write("\tvar myFrame = document.querySelector('div[id^=myFrame]:last-child')\r\n");
      out.write("\tmyFrame.className='myFrameCss';\r\n");
      out.write("}\r\n");
      out.write("</script>\r\n");
      out.write("<iframe id=\"myFrame\" name=\"myFrame\"\r\n");
      out.write("    frameborder=\"0\"\r\n");
      out.write("    style=\"position:absolute;background-color:transparent;border:0px;visibility:hidden;\"></iframe>\r\n");
      out.write("<noscript>\r\n");
      out.write("\t<object classid=\"clsid:D27CDB6E-AE6D-11cf-96B8-444553540000\"\r\n");
      out.write("\t\t\tid=\"AppPanel\" width=\"100%\" height=\"100%\"\r\n");
      out.write("\t\t\tcodebase=\"http://fpdownload.macromedia.com/get/flashplayer/current/swflash.cab\">\r\n");
      out.write("\t\t\t<param name=\"movie\" value=\"AppPanel.swf\" />\r\n");
      out.write("\t\t\t<param name=\"quality\" value=\"high\" />\r\n");
      out.write("\t\t\t<param name=\"bgcolor\" value=\"#ffffff\" />\r\n");
      out.write("\t\t\t<param name=\"allowScriptAccess\" value=\"sameDomain\" />\r\n");
      out.write("\t\t\t<embed src=\"AppPanel.swf\" quality=\"high\" bgcolor=\"#ffffff\"\r\n");
      out.write("\t\t\t\twidth=\"100%\" height=\"100%\" name=\"AppPanel\" align=\"middle\"\r\n");
      out.write("\t\t\t\tplay=\"true\"\r\n");
      out.write("\t\t\t\tloop=\"false\"\r\n");
      out.write("\t\t\t\tquality=\"high\"\r\n");
      out.write("\t\t\t\tallowScriptAccess=\"sameDomain\"\r\n");
      out.write("\t\t\t\ttype=\"application/x-shockwave-flash\"\r\n");
      out.write("\t\t\t\tpluginspage=\"http://www.adobe.com/go/getflashplayer\">\r\n");
      out.write("\t\t\t</embed>\r\n");
      out.write("\t</object>\r\n");
      out.write("</noscript>\r\n");
      out.write("\r\n");
      out.write("<!-- added by pengwei,电子称重 ocx.js -->\r\n");
      out.write("<object id=\"ComSettingActive\" classid=\"clsid:F2AEE9EF-70D6-4b05-BB41-472C5254EFD0\"></object>\r\n");
      out.write("<!-- end pengwei -->\r\n");
      out.write("</body>\r\n");
      out.write("</html>\r\n");
      out.write("\r\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
