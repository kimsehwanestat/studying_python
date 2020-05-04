# HTTP (HyperText Transfer Protocol)

    HTTP는 서버와 클라이언트가 텍스트, 이미지, 동영상등의 데이터를 주고 받을 때 사용하는 포로토콜이다.
    오늘날 웹을 구성하는 포로콜이다.
    텍스트 기반의 데이터로는 `HTML, CSS, javascript` 등이 있다. 
    웹서비스에 동장학는 요소 외에 HTTP(S)로 주고 받는 데이터로는 `JSON, XML`이 있다.
    웹으로 보는 이미지, 영상, 파일 같은 바이너리 데이터도 HTTP멀티파트나 `Base64`로 인코딩 하여 사용한다.
    `JSON`등을 `HTTP`와 함께 사용하는 `RESTful API` 가 있다.

## 무상태성
    HTTP는 요청 메시지를 보내기 직전까지 대상 컴퓨터가 연결 가능한지, 메시지를 
    응답 할 수 있는 상태인지 알 방법이 없다. 그래서 `stateless` 프로토콜이라고 한다.
    클라이언트가 서버로 HTTP요청을 보내면 서버는 이에 대한 응답을 보낸 다음 바로 소켓 연결을 닫는다

    모든 HTTP는 요청과 응답이 일대일로 대응되어야 하므로 요청을 받은 서버는 반드시 응답을 보내야만 한다
    클라이언트는 항상 자신이 보낸 요청이 실패했는지, 정상적으로 왔는지 알 수 있어서 로직이 단순해진다.

    그러나 클라이언트는 서버로 HTTP요청을 보내기 직전까지 실제로 서버가 동작하는지 알 방법은 없다.
    서버가 요청을 받더라도 클라이언트가 지정했던 시간 안에 응답을 보내지 못할 수 있어서 클라이언트는 각 상황에 대해 어떻게
    처리 해야 할 것 인지 결정해야 한다.

    TCP는 HTTP와 달리 연결을 끊지 않고 명시적으로 연걸을 끊기 전(소켓을 닫기 전)까지 메시지를 계속 주고 받는다.
    TCP는 텍스트가 아닌 바이너리 데이터를 사용하고, HTTP는 TCP프로콜 텍스트 기반의 HTTP 헤더와 메시지까지 사용하기 때문에
    패킷 크기가 상대적으로 크다. TCP패킷은 상대적으로 가벼워서 많은 사용자를 처리 할 수록 TCP가 HTTP보다 빠르다.

    하지만 HTTP는 각 요청이 소켓 1개를 점유하기 떄문에 문제가 생기지 않는데, TCP의 경우 여러 요청이 소켓 1개를 공동으로 사용하기 때문에 모든 요청이 1개의 소켓 안에 섞여서 이 부분에 대한 로직은 복잡해지게 된다.






