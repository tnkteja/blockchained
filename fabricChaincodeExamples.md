### Chaincode example 01

Participant A and Participant B have blockchain initialised to somevalues. Then Particiant A gives some value to partipant B.

Interesting aspects of the chaincode are Using `GetTxTimestamp() api` just any other way to make a timestamp.

### Chaincode example 02

Same as the above example but the key values for Participant A and Participant B are stored post deduction.

Interesting aspects are deleting provision for the key values of Participat A and Participant B. And Querying the key Values for the Participants A and B.

API's Used -  DelState(), GetState(), PutState()

### Chaincode example 03

Again same as the above example  even more to be the first example. Keyvalues of the participants are initialised aand query back.

### Chaincode example 04

Things get very interesting and take a new turn way from the begining itself, instead of making things happen in the same chaincode, another chain code altogether is invoked and called, yet in the usual way using the bytefied arguments.

Interesting API's : util.ToChaincodeArgs("someFunctionName", "array","of","arguments")  InvokeChaincode("chaincodename", args, "")

### Chaincode example 05

Same as above using a new chaincode for doing the job. One interesting thing will be a payload is sent back in the reponse, and not so new sending error incase of not success.

### eventsender

This is special example and probably all examples that follow this will be a special example in its own. The keyvalue pair is updated by a participant and alternatively notified back with a Event, with the payload.

Interesting API's : sendEvent("someEventName", []byte("some byte array"))

### invokereturnsvalue

Same as the above example, but the response is sent back with the payload.

### map

Performs same as some of the above, but additionally with a special method to retrieve a part of the keys.

Interesting API's : RangeQueryState("lexographically start key", "lexographically end key")

### passthru

Same as one of the example above invoking another chaincode to do the job.

### rbac

This is as mentioned and saw it coming a special example. Keyvalues of the participants are accepted, but their roles are checked beforehand, from a separetely maintained table, with an additional method to create a role into the table.



*** Table - RBAC ***
::

Interesting API's : GetCallerMetadata ,impl.NewAccessControlShim(someStubHandle).VerifySignature( participantCertificate, participantSignature, [..] ) ,
Column, someStubHandle.GetRow("someRowName", someColumnsHandle),  someRow.GetColumns(),  someStub.InsertRow  , someStub.ReplaceRow, 



### Snippets

<!-- 
err := stub.CreateTable("RBAC", []*shim.ColumnDefinition{
	&shim.ColumnDefinition{Name: "ID", Type: shim.ColumnDefinition_BYTES, Key: true},
	&shim.ColumnDefinition{Name: "Roles", Type: shim.ColumnDefinition_STRING, Key: false},
})

if err != nil {
	return shim.Error("Failed creating RBAC table.")
} 
-->
