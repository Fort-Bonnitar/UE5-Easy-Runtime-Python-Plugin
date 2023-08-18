// Fill out your copyright notice in the Description page of Project Settings.


#include "PythonFunctionLibrary.h"

FString UPythonFunctionLibrary::ConvertBytesToString(const TArray<uint8>& DataBuffer) {

	if (DataBuffer[DataBuffer.Num() - 1] == 0x00)
	{
		return UTF8_TO_TCHAR(DataBuffer.GetData());
	}

	TArray<uint8> tempBuffer;
	tempBuffer.SetNum(DataBuffer.Num() + 1);
	FMemory::Memcpy(tempBuffer.GetData(), DataBuffer.GetData(), DataBuffer.Num());
	tempBuffer[tempBuffer.Num() - 1] = 0x00;

	return UTF8_TO_TCHAR(tempBuffer.GetData());
}