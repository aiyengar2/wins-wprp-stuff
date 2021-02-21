## How to Use

Put this file on the machine and run the following on powershell:

```xml
<WindowsPerformanceRecorder Version="1">
  <Profiles>
    <EventCollector Id="Collector" Name="rancher-wins">
      <BufferSize Value="256"/>
      <Buffers Value="100"/>
    </EventCollector>
    <EventProvider Id="rancher-wins" Name="5576fd67-6511-5769-010b-45638098b239"/>
    <Profile Id="Test.Verbose.File" Name="Test" Description="Test" LoggingMode="File" DetailLevel="Verbose">
      <Collectors>
        <EventCollectorId Value="Collector">
          <EventProviders>
            <EventProviderId Value="rancher-wins"/>
          </EventProviders>
        </EventCollectorId>
      </Collectors>
    </Profile>
  </Profiles>
</WindowsPerformanceRecorder>
```

```powershell
wpr -start wins.wprp -filemode
wpr -stop wins.etl
```

You can then view the logs via:

```powershell
Get-WinEvent -Path .\wins.etl -Oldest | Format-List -Property *
```