import numpy as np

EncoderOutput = np.array([])
Document, Dictionary = "", {}


def Load():
    global EncoderOutput

    EncoderOutput = np.load("EncoderOutput.npy", allow_pickle=True)
    keys, values = np.load("InitializedDictionaryKeys.npy", allow_pickle=True), np.load(
        "InitializedDictionaryValues.npy", allow_pickle=True)

    for i in range(len(keys)):
        Dictionary[values[i]] = keys[i]


def RunInverseLZW():
    global EncoderOutput
    global Dictionary
    global Document

    Document += Dictionary[EncoderOutput[0]]
    TempString = Dictionary[EncoderOutput[0]]

    for index in range(1, len(EncoderOutput)):
        Document += Dictionary[EncoderOutput[index]]
        TempString += Dictionary[EncoderOutput[index]]
        TempIndex = 1

        while TempIndex <= len(TempString) and TempString[:TempIndex] in Dictionary.values():
            TempIndex += 1

        if TempString[:TempIndex] not in Dictionary.values():
            Dictionary[len(Dictionary)] = TempString[:TempIndex]
            TempString = TempString[TempIndex-1:]

    open("Output.txt", "w").write(Document)


if __name__ == "__main__":
    Load()
    RunInverseLZW()
