package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.util.Hashtable;
import java.util.StringTokenizer;
import java.util.Locale;
import java.io.StringWriter;
import java.io.PrintWriter;
import com.enterfly.framework.presentation.*;
import com.enterfly.framework.web.*;
import com.enterfly.framework.agent.RequestAgent;
import com.enterfly.framework.context.IUser;
import com.enterfly.framework.context.BusinessContext;
import com.enterfly.framework.util.Timer;
import com.enterfly.framework.util.Logger;
import java.util.Enumeration;

public final class getXml_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {


    private final static String LOCALE_INFO       = "__locale__";
    private final static String LOCALE_INFO_DELIM = "-";

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
      response.setContentType("text/xml;charset=utf-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");

    Timer timer = new Timer("getXml.jsp");
    String sessionId = "";
    String xml = "";
    //登陆超时异常编码，默认1 表示未登陆超时 2表示目前已经登陆超时
    String errorCode = "1";
    String[] info = new String[] {
        "analyze request data and construct business context",
        "setup context",
        "process",
        "put data in request",
        "po to xml"
    };
    try {
    	request.setCharacterEncoding("utf-8");
        RequestWrapper wrapper = new RequestWrapper(request, response);
        
        Hashtable requestData = wrapper.getData();
        
        //if(RequestWrapper.CONTAINER_ENCODING==null){
        	//Enumeration names=requestData.keys();
        	//while(names.hasMoreElements()){
        		//String name=(String)names.nextElement();
        		//String value=(String)requestData.get(name);
        		//value=new String(value.getBytes("8859_1"),"GB2312");
        		//requestData.put(name,value);
        	//}
        //}
        
        BusinessContext ctx = new BusinessContext();

        IUser user = (IUser)request.getSession(false).getAttribute("USER");
        
        if (user == null) {
        	errorCode = "2";
            throw new Exception("会话超时,请重新登陆!");
        }
        
        ctx.importUserInfo(user);
        
        String localeInfo = (String)requestData.get(LOCALE_INFO);
        
        Locale locale = null;
        if (localeInfo != null) {
            StringTokenizer st = new StringTokenizer(localeInfo, LOCALE_INFO_DELIM);
            int count = st.countTokens();
            
            if (count == 1) {
                locale = new Locale(st.nextToken().trim().toLowerCase(),null);
            } else if (count == 2) {
                locale = new Locale(st.nextToken().trim().toLowerCase(), st.nextToken().trim().toUpperCase());
            } else { // >= 3
                locale = new Locale(st.nextToken().trim().toLowerCase(), st.nextToken().trim().toUpperCase(), st.nextToken().trim());
            }
        }
        ctx.setCurrentLocale((locale == null) ? request.getLocale() : locale);
    
    	ctx.setIPAddress(request.getRemoteAddr());
    		
    	timer.snapshot(info[0]);
    	ctx.setRequestData(requestData);
    	ctx.setHttpSession(request.getSession());
    	
        sessionId = request.getSession().getId();
    	ctx.setSessionGuid(sessionId);
    			
    	String pageId = (String) requestData.get("PAGE");
    	String action = (String) requestData.get("ACTION");
    
    	ctx.setCurrentPOName(pageId);
    	ctx.setCurrentAction(action);
    	timer.snapshot(info[1]);
    
    	if(Logger.isDebugEnabled()){
    	Logger.debug(
    		new StringBuffer()
    			.append(" - Page ID = ")
    			.append(pageId)
    			.toString());
    	Logger.debug(
    		new StringBuffer()
    			.append(" - Action = ")
    			.append(action)
    			.toString());
    	}
    
    	RequestAgent agent = EventDispatcher.getRequestAgent();
    	
    	ctx = agent.process(ctx);
    	timer.snapshot(info[2]);
    	//request.setAttribute("PAGE", ctx);
    	timer.snapshot(info[3]);
    
        PresentationObject po =(PresentationObject)ctx.getPOObject(pageId);
        xml = Presentation2XML.toXml(po);
        timer.snapshot(info[4]);
    } catch (Throwable e) {
        StringWriter sw = new StringWriter();
        e.printStackTrace(new PrintWriter(sw));
        
        String errorInfo = sw.getBuffer().toString();
        if(errorCode.equals("2")){
        	 xml = new StringBuffer("<Error>")
             .append("<message>")
             .append(errorCode)
             .append("</message>")
             .append("<stack_trace>")
             .append(errorInfo)
             .append("</stack_trace>")
             .append("</Error>")
             .toString();
        }else{
	        xml = new StringBuffer("<Error>")
	                .append("<message>")
	                .append(e.getMessage())
	                .append("</message>")
	                .append("<stack_trace>")
	                .append(errorInfo)
	                .append("</stack_trace>")
	                .append("</Error>")
	                .toString();
        }
	    Logger.error("get XML",e);
    }finally{
    	errorCode = "1";
    }
    timer.showAll();
    response.setCharacterEncoding("utf-8");
    response.setHeader("Pragma","no-cache");
    response.setHeader("Cache-Control","no-cache");
    response.setDateHeader("Expires",0);
    //System.out.println(xml);
    

      out.write('\r');
      out.write('\n');
      out.print(xml);
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
