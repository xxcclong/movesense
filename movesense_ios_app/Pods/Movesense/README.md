# Movesense iOS and Android Libraries

#iOS
## Example

To run the example project, clone the repo, and run `pod install` in the IOS/iOS-Example directory first. Make sure you have configured your ssh public key to bitbucket beforehand. This phase should not produce any errors:

```
$ cd IOS/iOS-Example/
$ pod install
Analyzing dependencies
Pre-downloading: `Movesense` from `ssh://git@altssh.bitbucket.org:443/suunto/movesense-mobile-lib.git`
Pre-downloading: `SwiftCharts` from `https://github.com/i-schuetz/SwiftCharts.git`, branch `master`
Downloading dependencies
Installing Movesense (1.0.0)
Installing PromiseKit (4.1.3)
Installing SwiftCharts (0.5.1)
Installing SwiftyJSON (3.1.4)
Installing Toast-Swift (2.0.0)
Generating Pods project
Integrating client project
Sending stats
Pod installation complete! There are 5 dependencies from the Podfile and 5 total pods installed.
```

Then open movesense-swiftapp.xcworkspace and build target 'movesense-swiftapp'. 

### Bundle identifier ###

You need to replace 'com.suunto.movesense' bundle identifier with your own bundle identifier.

### Signing ###

In order to sign the application, you need to setup your own developer provisioning profile in Xcode.

### Running the application ###

After the previous step, you are ready to go and can install the application on the device. 

However, you still need to enable the developer certificate in Settings -> General -> Device Management.

Finally, run the app!

## Installation

Movesense is available through [CocoaPods](http://cocoapods.org). To install
it, simply add the following line to your Podfile:

```ruby
pod 'Movesense', :git => 'ssh://git@altssh.bitbucket.org:443/suunto/movesense-mobile-lib.git'
```
## Usage

See IOS/Movesense/readme.txt

# Android

## Example


Open 'Android/samples/ConnectivityAPISample/build.gradle' in Android Studio (the sample shows how to connect to Movesense and how to do a simple GET request). For more complex data queries (such as sensors) consult *Android/samples/sampleapp*

## Known issues

 - Going outside BLE range causes the app to crash in *sampleapp*. (should work in *ConnectivityAPISample*)

# Firmware Update

## Wireless Update over Bluetooth Low-energy
The latest Movesense device firmware supports wireless update using Nordic's DFU protocol. This requires operation of both the Movesense Example App as well as the Nordic's nRF Toolbox.

**WARNING: in case the new firmware is not based on the latest Movesense stack, the device looses the capability to be updated!!!**

![movesense-mobile-lib-dfu.png](https://bitbucket.org/repo/oGbGqA/images/26723009-movesense-mobile-lib-dfu.png)

# General

## Frequently Asked Questions

FAQ can be found via http://stackoverflow.com/search?q=movesense. If your problem is not addressed there, please [post](http://stackoverflow.com/questions/ask) a new question, and include [tag:movesense] in the message body.

## Bug Reports

Please report bugs by [raising](https://bitbucket.org/suunto/movesense-mobile-lib/issues/new) an Issue via Bitbucket.

## Contributions
Your input is appreciated and we encourage you to post your contributions as pull requests to this repository.

## License

See the [LICENSE.pdf](./LICENSE.pdf) file for more info.