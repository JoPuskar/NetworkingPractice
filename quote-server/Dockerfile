FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build-env
WORKDIR /app

COPY quote-server.csproj ./
RUN dotnet restore

COPY ./src/QuoteServer.cs ./
RUN dotnet publish -c Release -o out

# Runtime image
FROM mcr.microsoft.com/dotnet/runtime:9.0
WORKDIR /app
COPY --from=build-env /app/out ./
EXPOSE 13000
ENTRYPOINT [ "dotnet", "quote-server.dll" ]

