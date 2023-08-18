// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "PythonFunctionLibrary.generated.h"

/**
 * 
 */
UCLASS()
class PYRUNTIMEUTILITY_API UPythonFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintCallable, Category = "Python Utilities")
	static FString ConvertBytesToString(const TArray<uint8>& DataBuffer);
};
