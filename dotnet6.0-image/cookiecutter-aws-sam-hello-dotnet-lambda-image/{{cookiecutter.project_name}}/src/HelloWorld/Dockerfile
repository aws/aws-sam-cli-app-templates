ARG SAM_BUILD_MODE=Release
FROM public.ecr.aws/lambda/dotnet:6 AS base
FROM mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim as build

ARG SAM_BUILD_MODE
ENV ENV_BUILD_MODE = ${SAM_BUILD_MODE}

WORKDIR /src
COPY ["HelloWorld.csproj", "HelloWorld/"]
RUN dotnet restore "HelloWorld/HelloWorld.csproj"

WORKDIR "/src/HelloWorld"
COPY . .

RUN dotnet build "HelloWorld.csproj" --configuration ${SAM_BUILD_MODE} --output /app/build

FROM build AS publish
RUN if [ "$ENV_BUILD_MODE" = "Debug" ]; \
then dotnet publish "HelloWorld.csproj" --configuration "Debug" --runtime linux-x64 --self-contained false --output /app/publish; \
else dotnet publish "HelloWorld.csproj" --configuration "Release" --runtime linux-x64 --self-contained false --output /app/publish -p:PublishReadyToRun=true; fi


FROM base AS final
WORKDIR /var/task
COPY --from=publish /app/publish .
CMD ["HelloWorld::HelloWorld.Function::FunctionHandler"]