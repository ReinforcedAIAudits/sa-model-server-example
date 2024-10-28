import http.client


class ContextManagerConnection(http.client.HTTPConnection):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def generate_audit(contract: str):
    with ContextManagerConnection('127.0.0.1:5000') as conn:
        conn.request('POST', '/submit', contract, {'Content-type': 'application/json'})
        resp = conn.getresponse()
        if resp.status != 200:
            return f'Invalid status: {resp.status}\n{resp.read()}'
        return resp.read().decode('utf-8')


if __name__ == "__main__":
    contract = """
contract Wallet_1 {
    mapping (address => uint) userBalance;

    function getBalance(address u) constant returns(uint){
        return userBalance[u];
    }

    function addToBalance() payable{
        userBalance[msg.sender] += msg.value;
    }   

    function withdrawBalance(){
        // send userBalance[msg.sender] ethers to msg.sender
        // if mgs.sender is a contract, it will call its fallback function
        if( ! (msg.sender.call.value(userBalance[msg.sender])() ) ){
            throw;
        }
        userBalance[msg.sender] = 0;
    }   
}
"""
    audit = generate_audit(contract)
    print(audit)
