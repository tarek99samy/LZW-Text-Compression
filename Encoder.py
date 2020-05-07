import numpy as np

Document = open("Input.txt", "r").read()
Dictionary, EncoderOutput, = {}, np.array([])


def InitializeDict(file):
    for char in file:
        if char not in Dictionary.keys():
            Dictionary[char] = len(Dictionary)

    np.save("InitializedDictionaryKeys.npy", np.array(
        list(Dictionary.keys())), allow_pickle=True)
    np.save("InitializedDictionaryValues.npy", np.array(
        list(Dictionary.values())), allow_pickle=True)


def RunLZW(file):
    global Dictionary
    global EncoderOutput

    index = 0

    while index < len(file):
        TempIndex, TrackingString = index+1, file[index]

        while TempIndex < len(file) and (TrackingString + file[TempIndex]) in Dictionary.keys():
            TrackingString += file[TempIndex]
            TempIndex += 1

        EncoderOutput = np.append(EncoderOutput, Dictionary[TrackingString])

        if TempIndex < len(file):
            Dictionary[TrackingString+file[TempIndex]] = len(Dictionary)

        index = TempIndex

    np.save("EncoderOutput.npy", EncoderOutput, allow_pickle=True)


if __name__ == "__main__":
    InitializeDict(Document)
    RunLZW(Document)
