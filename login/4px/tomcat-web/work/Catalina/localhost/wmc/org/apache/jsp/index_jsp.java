package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import javax.servlet.http.Cookie;

public final class index_jsp extends org.apache.jasper.runtime.HttpJspBase
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

      out.write("<!DOCTYPE html>\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("<html lang=\"zh-CN\">\r\n");
      out.write("<head>\r\n");
      out.write("\t<meta charset=\"UTF-8\">\r\n");
      out.write("\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\r\n");
      out.write("\t<title>电子商务供应链管理系统</title>\r\n");
      out.write("\t<link rel=\"stylesheet\" href=\"resources/css/iconfont/iconfont.css\" />\r\n");
      out.write("\t<link rel=\"stylesheet\" href=\"resources/css/login.css\" />\r\n");
      out.write("\t<link rel=\"stylesheet\" href=\"resources/validates/css/validationEngine.jquery.css\" type=\"text/css\"/>\r\n");
      out.write("\t<link rel=\"stylesheet\" href=\"resources/validates/css/template.css\" type=\"text/css\"/>\r\n");
      out.write("\t<script src=\"resources/validates/js/jquery-1.8.2.min.js\" type=\"text/javascript\">\r\n");
      out.write("\t</script>\r\n");
      out.write("\t<script src=\"resources/validates/js/languages/jquery.validationEngine-en.js\" type=\"text/javascript\" charset=\"utf-8\">\r\n");
      out.write("\t</script>\r\n");
      out.write("\t<script src=\"resources/validates/js/jquery.validationEngine.js\" type=\"text/javascript\" charset=\"utf-8\">\r\n");
      out.write("\t</script>\r\n");
      out.write("\t<script language=\"javascript\">\r\n");
      out.write("\t\t$(function(){\r\n");
      out.write("\t\t\tjQuery(\"#formID\").validationEngine('attach', {\r\n");
      out.write("\t\t\t\t  onValidationComplete: function(form, status){\r\n");
      out.write("\t\t\t\t  \tif(status){\r\n");
      out.write("\t\t\t\t  \t\tvar company = $(\"#COMPANY\").val();\r\n");
      out.write("\t\t\t\t  \t\tdocument.cookie=\"company=\"+company;\r\n");
      out.write("\t\t\t\t  \t\tvar user_id = $(\"#ACCOUNT\").val();\r\n");
      out.write("\t\t\t \t\t\t$(\"#USER\").val(company +\"_\" +user_id);\r\n");
      out.write("\t\t\t \t\t\t$(\"#formID\").submit();\r\n");
      out.write("\t\t\t\t  \t}\r\n");
      out.write("\t\t\t\t  },binded:false,showOneMessage:true\r\n");
      out.write("\t\t\t\t});\r\n");
      out.write("\t\t\t$(\"#errormsg\").text('");
      out.write((java.lang.String) org.apache.jasper.runtime.PageContextImpl.evaluateExpression("${errorMessage}", java.lang.String.class, (PageContext)_jspx_page_context, null));
      out.write("').css('visibility','hidden');\r\n");
      out.write("\t\t});\r\n");
      out.write("\t</script>\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("\t<div id=\"loginform-wrapper\">\r\n");
      out.write("\t\t<img src=\"resources/images/login/login_banner.jpg\" alt=\"企业广告图\" class=\"login-banner-img\">\r\n");
      out.write("\t\t<form id=\"formID\" action=\"loginDiy.sc\" method=\"post\">\r\n");
      out.write("\t\t\t<div class=\"loginform-container\">\r\n");
      out.write("\t\t\t\t<p>\r\n");
      out.write("\t\t\t\t\t<img src=\"resources/images/login/4pnt_logo.png\" alt=\"企业LOGO图\">\r\n");
      out.write("\t\t\t\t</p>\r\n");
      out.write("\t\t\t\t<h1>电子商务供应链管理系统</h1>\r\n");
      out.write("\t\t\t\t<ul>\r\n");
      out.write("\t\t\t\t\t<li>\r\n");
      out.write("\t\t\t\t\t\t<div class=\"form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t<span class=\"iconfont icon-yonghu\"></span>\r\n");
      out.write("\t\t\t\t\t\t\t<INPUT name=\"USER\"  id=\"USER\" type=hidden><input type=\"text\" placeholder=\"用户名\" class=\"validate[required] text-input\" data-errormessage-value-missing=\"用户名不能为空\" name=\"ACCOUNT\"   id=\"ACCOUNT\" >\r\n");
      out.write("\t\t\t\t\t\t</div>\r\n");
      out.write("\t\t\t\t\t</li>\r\n");
      out.write("\t\t\t\t\t<li>\r\n");
      out.write("\t\t\t\t\t\t<div class=\"form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t<span class=\"iconfont icon-cipher\"></span>\r\n");
      out.write("\t\t\t\t\t\t\t<input type=\"password\"  name=\"PASSWORD\" class=\"validate[required] text-input\"  data-errormessage-value-missing=\"密码不能为空\"  id=\"PASSWORD\"  placeholder=\"密码\">\r\n");
      out.write("\t\t\t\t\t\t</div>\r\n");
      out.write("\t\t\t\t\t</li>\r\n");
      out.write("\t\t\t\t\t<li>\r\n");
      out.write("\t\t\t\t\t\t<div class=\"form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t<span class=\"iconfont icon-gongsi\"></span>\r\n");
      out.write("\t\t\t\t\t\t\t<input type=\"text\"  name=\"COMPANY\" class=\"validate[required] text-input\"  id=\"COMPANY\" data-errormessage-value-missing=\"公司名不能为空\"  placeholder=\"公司名\">\r\n");
      out.write("\t\t\t\t\t\t</div>\r\n");
      out.write("\t\t\t\t\t</li>\r\n");
      out.write("\t\t\t\t\t<!-- <li>\r\n");
      out.write("\t\t\t\t\t\t<a href=\"\" class=\"linkto-forget\">忘记登录密码？</a> \r\n");
      out.write("\t\t\t\t\t</li>-->\r\n");
      out.write("\t\t\t\t\t<li>\r\n");
      out.write("\t\t\t\t\t\t<button type=\"submit\">登&nbsp;录</button>\r\n");
      out.write("\t\t\t\t\t</li>\r\n");
      out.write("\t\t\t\t\t<li>\r\n");
      out.write("\t\t\t\t\t\t<div id=\"errormsg\"></div>\r\n");
      out.write("\t\t\t\t\t</li>\r\n");
      out.write("\t\t\t\t</ul>\r\n");
      out.write("\t\t\t</div>\r\n");
      out.write("\t\t\t\r\n");
      out.write("\t\t</form>\r\n");
      out.write("\t</div>\r\n");
      out.write("\t<div id=\"footer\">\r\n");
      out.write("\t\t<span class=\"iconfont icon-4pnt\"></span>\r\n");
      out.write("\t\t<p>\r\n");
      out.write("\t\t\t前海四方网络科技 版权所有 粤ICP备 15073770号-1\r\n");
      out.write("\t\t\t<br>\r\n");
      out.write("\t\t\tCopyright &copy;2015 4PNT. All Rights Reserved.\r\n");
      out.write("\t\t</p>\r\n");
      out.write("\t</div>\r\n");
      out.write("</body>\r\n");
      out.write("</html>");
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
