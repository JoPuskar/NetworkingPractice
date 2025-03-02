using System.Net;
using System.Net.Sockets;
using System.Text;

class QuoteServer
{
private static readonly Dictionary<string, string> quotes = new Dictionary<string, string>()
{
    {"Be the change you wish to see in the world.", "Mahatma Gandhi"},
    {"I think, therefore I am.", "René Descartes"},
    {"To be or not to be, that is the question.", "William Shakespeare"},
    {"In three words I can sum up everything I've learned about life: it goes on.", "Robert Frost"},
    {"Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"},
    {"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.", "Albert Einstein"},
    {"Be yourself; everyone else is already taken.", "Oscar Wilde"},
    {"All that we are is the result of what we have thought.", "Buddha"},
    {"Life is what happens when you're busy making other plans.", "John Lennon"},
    {"The only way to do great work is to love what you do.", "Steve Jobs"}

};
private static Random random = new Random();

private static readonly Guid ServerId = Guid.NewGuid();

static void Main(string[] arg)
{
    TcpListener? server = null;
try
    {
        Int32 port = 13000;
        IPAddress localAddr = IPAddress.Any;

        server = new TcpListener(localAddr, port);

        server.Start();
        Console.WriteLine($"Quote Server {ServerId} running on port " +port);
        Console.WriteLine("Press Ctrl-C to stop server");

        while(true) {
            // Blocking call
            TcpClient client = server.AcceptTcpClient();
            Console.WriteLine("Connected to client!");

            NetworkStream stream = client.GetStream();

            var quoteList = new List<KeyValuePair<string, string>>(quotes);
            var randomQuote = quoteList[random.Next(quoteList.Count)];
            string responseMsg = $"[{ServerId}]\"{randomQuote.Key}\" - {randomQuote.Value}\n";
            byte[] msg = Encoding.ASCII.GetBytes(responseMsg);
            stream.Write(msg, 0, msg.Length);
            Console.WriteLine($"Sent: {responseMsg}");

            client.Close();
            

        }
    }
catch(SocketException e)
    {
        Console.WriteLine("SocketException: {0}", e);
    }
finally
    {
        server?.Stop();
    }
}
}