
import houndify

def main():
    clientId = "7ug9avYlM-P7Hqq45rfy9w=="
    clientKey = "VHLA69_6cvdz0koCw8Q_-I-8MQ36UWnFN5roGq261kqvIEABInEnYMZsQv3o7ElcIpz6xtlR00eLIue9QreUBg=="
    userId = "tactEYEle_user"
    client = houndify.StreamingHoundClient(clientId, clientKey, userId)

    class MyListener(houndify.HoundListener):
      def onPartialTranscript(self, transcript):
        print("Partial transcript: " + transcript)

      def onFinalResponse(self, response):
        print("Final response: " + str(response))

      def onError(self, err):
        print("Error " + str(err))


    client.start(MyListener())
    client.fill(samples)
    client.finish()

main()