package garden.carrot.toby.common.logback;

import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.util.ContentCachingResponseWrapper;

public class ResponseWrapper extends ContentCachingResponseWrapper {

	public ResponseWrapper(HttpServletResponse response) {
		super(response);
	}
}
