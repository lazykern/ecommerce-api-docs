# Widget SDK Update instructions
This article documents the changes to the <**Widget**> SDK.
## @tiktokshop/widget-kit
For native js integration
### <Version 1.0.2>
Release date:2024/2/19
Fixed some issues.
### <Version 1.0.0>
### Added
| **modules** | **description** |
| --- | --- |
| init | Added init method to support user integration and initial widgets. |
| loadWidget | Added loadWidget method to support users loading our widget page. |
| update | Added update method to support users to modify widget config. |
| preloadWidget | Added preloadWidget method to support users to preload widget resources. |
## @tiktokshop/widget-kit-react
For React component integration
### <Version 1.0.2>
Release date:2024/2/19
### Added
| **modules** | **description** |
| --- | --- |
| WidgetConfigProvider | Added WidgetConfigProvider component, the component integrates the original init, update, preload methods, WidgetConfigProvider should be used with RemoteWidget, it is recommended to use WidgetConfigProvider in the react integration scenario instead of directly calling init, update, preload. |
| RemoteWidget | Added RemoteWidget component. The original loadWidget method is integrated inside the component. Load state placeholder map and abnormal state placeholder map are provided. Users can specify widgets, load resources and render components by name. RemoteWidget should be used with WidgetConfigProvider. It is recommended to use RemoteWidget in the react integration scenario instead of calling loadWidget directly. |
### <Version 1.0.0>
### Added
| **modules** | **description** |
| --- | --- |
| init | Added init method to support user integration and initial widgets. |
| loadWidget | Added loadWidget method to support users loading our widget page. |
| update | Added update method to support users to modify widget config. |
| preloadWidget | Added preloadWidget method to support users to preload widget resources. |
# Quick start
## Configure development environment
### Frame adaptation
We support two methods of react framework integration and native js integration. Users using the react framework can use the react component method to integrate, and non-react framework users can use the native JS method to integrate.
### Install dependencies
To use react component integration, please install the following packages:
```JSON
npm install @tiktokshop/widget-kit-react
```

For native js integration, please install the following packages:
```JSON
npm install @tiktokshop/widget-kit
```

## Integrated SDK
### Preconditions

* The server needs to develop an API for obtaining short-lived tokens (refer to document [Get Widget Token](get-widget-token) for development methods). When the front-end integrates the widget page, during the initialization SDK phase, the getWidgetToken field is passed into the function to obtain the token.
* For security reasons, there are cross-origin restrictions on the interfaces in the widget page. When integrating the widget, you need to provide the domain name to the open platform for whitelist configuration.

### Init widget
react framework uses (recommended):
It is recommended to put `WidgetConfigProvider` in the outermost layer of the entire application for global unified configuration
```TypeScript
import { WidgetConfigProvider } from '@tiktokshop/widget-kit-react';

const initOptions =  {
    config:{
      shopId: 'xxx', //seller id, such as 123456
      oecRegion: 'xxx',//country,such as US
      appKey: 'xxx',//The key corresponding to the merchant's creation service
      isvInfo: {
        name: 'xxx',//ISV name,such as OPEN_PLATFORM
      },
    },
    getToken:getWidgetToken,
    // If you integrate multiple widgets, remotes can set multiple
    remotes:[
    {
      name: 'xxx',//Integrated business name, provided by the open platform,such as:@tiktokshop-widget/product:optimizer
    },
  ]
};

export default () => {
  return (
    <WidgetConfigProvider
        config={initOptions.config} 
        getToken={initOptions.getToken} 
        remotes={initOptions.remotes}
        preloadWidgetNames={['@tiktokshop-widget/product:optimizer']} 
    >
      <RemoteWidget 
        name={'@tiktokshop-widget/product:optimizer'} 
        className={'containerClass'} 
        options={{}}
      />
    </WidgetConfigProvider>
  );
};
```

native JS uses:
```TypeScript
import { init } from '@tiktokshop/widget-kit';

init({
  config: {
      shopId: 'xxx', //seller id, such as 123456
      oecRegion: 'xxx',//country,such as US
      appKey: 'xxx',//The key corresponding to the merchant's creation service
      isvInfo: {
        name: 'xxx',//ISV name,such as OPEN_PLATFORM
      },
    },
  remotes: [
    {
      name: 'xxx',//Integrated business name, provided by the open platform,such as:@tiktokshop-widget/product:optimizer
    },
  ],
  getToken: getWidgetToken,//get auth token
});
```

### Preload widget
If the widget page is not displayed on the first screen, the resources can be loaded in advance by preloading, which can reduce the loading time of subsequent components and improve the page response speed.
react framework uses:
Configure preload in `WidgetConfigProvider` preloadWidgetNames, you can put `WidgetConfigProvider` to the outermost preload time
```JSON
// For react component integration
import { preloadWidget } from '@tiktokshop/widget-kit-react';

export default () => {
  return (
    <WidgetConfigProvider
        config={initOptions.config} 
        getToken={initOptions.getToken} 
        remotes={initOptions.remotes}
        preloadWidgetNames={['@tiktokshop-widget/product:optimizer']} 
    >
      <RemoteWidget 
        name={'@tiktokshop-widget/product:optimizer'} 
        className={'containerClass'} 
        options={{}}
      />
    </WidgetConfigProvider>
  );
};
```

native JS uses:
Preloading with `preloadWidget`
```JSON
// For native js integration
import { preloadWidget } from '@tiktokshop/widget-kit';//Reference method depends on the selected integration scheme

preloadWidget(['@tiktokshop-widget/product:optimizer']);
```

### Load widget
react framework uses:
```JavaScript
import { RemoteWidget } from "@tiktokshop/widget-kit-react";

const name = "@tiktokshop-widget/product:optimizer";

export function Test() {
  return <RemoteWidget 
      name={name} 
      className={'widget-preview-container'} 
      options={{}}
    />;
}
```

native JS uses:
```JSON
import { loadWidget, WidgetComponent } from '@tiktokshop/widget-kit';

//load widget
const name = '@tiktokshop-widget/product:optimizer';
let view = null;
loadWidget(name).then((component: WidgetComponent) => {
  view = component.create(
    document.getElementById('widget-preview-container')!,
  );
  view?.render({});
});

//create a mount element
<div
  className="widget-preview-container"
  id="widget-preview-container">
</div>
```

### Update widget config
When the merchant's shop information needs to be modified, the shop and other information can be updated by using the update method.
react framework uses:
Update WidgetConfigProvider parameters to update widget configuration
native JS uses:
```JSON

import { update } from '@tiktokshop/widget-kit';//Reference method depends on the selected integration scheme

update({
  config: {
      shopId: 'xxx', //seller id, such as 123456
      oecRegion: 'xxx',//country,such as US
      appKey: 'xxx',//The key corresponding to the merchant's creation service
      isvInfo: {
        name: 'xxx',//ISV name,such as OPEN_PLATFORM
      },
    },
  getToken: getWidgetToken,//get auth token
});
```

# Reference API

### Input Parameters
| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| config | Object | Y |  | basic config of widget |
| shopId | string | Y | '123456' | seller id, used for event tracking |
| oecRegion | string | Y | 'US' | seller region, fill in the standard code of the country where the merchant is located, such as 'US', 'GB', and so on. |
| appKey | string | Y | 'xxxxx' | authorized by the service market, used for authentication |
| isvInfo | Object | Y |  | ISV related information |
| name | string | Y | 'xxxxx' | the name of ISV |
| getToken | Promise | Y |  | promise method to get token |
| token | string | Y | 'eyJhbGciOiJIUzUxMxxxxxxxx' | token |
| expire_at | string | Y | '1703227531' | expiration |
| remotes | []Object | Y |  |  |
| name | string | Y | '@tiktokshop-widget/product:optimizer' | Integrated widget name, provided by the open platform |

The output parameters of loadWidget in @tiktokshop/widget-kit-react and @tiktokshop/widget-kit are different. The specific differences are as follows:
### @tiktokshop/widget-kit-react
#### Input Parameters
| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| name | string | Y | '@tiktokshop-widget/product:optimizer' | Integrated widget name, provided by the open platform |
#### Output Parameters
| Properties | Type | Sample |
| --- | --- | --- |
| Component <br> (custom name) | React.ComponentType | `JSON <br> const Component = loadWidget(name); <br> return ( <br> <div> <br> <Component /> <br> </div> <br> ); <br>` |
### @tiktokshop/widget-kit
#### Input Parameters
| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| name | string | Y | '@tiktokshop-widget/product:optimizer' | Integrated widget name, provided by the open platform |
#### Output Parameters
| Properties | Type | Sample |
| --- | --- | --- |
| component <br> (custom name) | Promise | `JSON <br> loadWidget(name).then((component: WidgetComponent) => { <br> view = component.create( <br> document.getElementById('widget-preview-container'), <br> ); <br> view?.render({}); <br> }); <br> <br> return ( <br> <div <br> className="widget-preview-container" <br> id="widget-preview-container"></div> <br> ); <br>` |
| create | (el: HTMLElement) => WidgetView |  |
| render | (props: Record<string, any>) => Promise |  |
| unmount() | Promise |  |
| update | (props: Record<string, any>) => Promise |  |

| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| name | string | Y | '@tiktokshop-widget/product:optimizer' | Integrated widget name, provided by the open platform |

| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| config | Object | N |  | basic config of widget |
| shopId | string | Y | '123456' | seller id, used for event tracking |
| oecRegion | string | Y | 'US' | seller region, used for traffic scheduling |
| appKey | string | Y | 'xxxxx' | authorized by the service market, used for authentication |
| isvInfo | Object | Y |  | ISV related information |
| name | string | Y | 'OPEN_PLATFORM' | the name of ISV |
| getToken | Promise | N |  | promise method to get token |
| token | string | Y | 'eyJhbGciOiJIUzUxMxxxxxxxx' | token |
| expire_at | string | Y | '1703227531' | expiration |

WidgetConfigProvider only exists in @tiktokshop/widget-kit-react
| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| config | Object | Y |  | basic config of widget |
| shopId | string | Y | '123456' | seller id, used for event tracking |
| oecRegion | string | Y | 'US' | seller region, fill in the standard code of the country where the merchant is located, such as 'US', 'GB', 'ID', and so on. |
| appKey | string | Y | 'xxxxx' | authorized by the service market, used for authentication |
| isvInfo | Object | Y |  | ISV related information |
| name | string | Y | 'xxxxx' | the name of ISV |
| getToken | Promise | Y |  | promise method to get token |
| token | string | Y | 'eyJhbGciOiJIUzUxMxxxxxxxx' | token |
| expire_at | string | Y | '1703227531' | expiration |
| remotes | []Object | Y |  |  |
| name | string | Y | '@tiktokshop-widget/product:optimizer' | Integrated widget name, provided by the open platform |
| preloadWidgetNames | string[] | N | ['@tiktokshop-widget/product:optimizer'] | Integrated widget name, provided by the open platform |

RemoteWidget only exists in @tiktokshop/widget-kit-react
| Properties | Type | Require | Sample | Properties description |
| --- | --- | --- | --- | --- |
| name | string | Y | '@tiktokshop-widget/product:optimizer' | Integrated widget name, provided by the open platform |
| className | string | N | '' | dom node's classname |
| style | CSSProperties | N | `JSON <br> { <br> "width":100 <br> } <br>` | dom node's style |
| options | Record<string,any> | N |  | Configuration of incoming widget components |

```JSON
export interface WidgetComponent {
  create: (el: HTMLElement) => WidgetView;
}
```


```JSON
export interface WidgetView {
  render: (props: Record<string, any>) => Promise<void>;
  unmount(): Promise<void>;
  update: (props: Record<string, any>) => Promise<void>;
}
```

# Error message list
| **Error message** | **description** |
| --- | --- |
| Please call init first | You need to initialize [init](https://bytedance.larkoffice.com/docx/VmDKdqmlCokkwcx5srecegJongc#doxcnZJv54tgHadJdfTbSydf4nc) first before using it |
| Current name configuration not found | Incorrect resource loading, please check if the resource is abnormal |
|  |  |
# FAQ
If you encounter problems while using the SDK, you can refer to this document to solve them.

1. The widget page fails to load, and the interface for obtaining the token repeatedly initiates a request.

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/48565dbe760d4a4783c023756b8bc146~tplv-10qhjjqwgv-image.image" width="1116px" /></div>

solution: Check the return value and parameters of the interface /api/v1/seller/widget/get, usually because the token is not passed in. Check the return value of getToken in the code and ensure that the following data is returned.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/e51e5883f9ab45eabb29dc106e834b50~tplv-10qhjjqwgv-image.image" width="1284px" /></div>

```SQL
if (res?.code === 0) {
      return res?.data;//The token interfaces of different access parties return different data structures, and the ways of obtaining data are different here.
    }
```


2. Interface/api/v1/seller/widget/get error list

| error code | error message | reason |
| --- | --- | --- |
| 36017010 | Widget domain not match | The domain name configured in the whitelist does not match the actual one. |
| 36017005 | Widget Token Is Expired | The widget token has expired |
| 36017006 | Widget token is invalid | The widget token was sent incorrectly |
| 36017008 | app_key is not match | app_key is not match |
| 36017009 | Widget Token Shop Not Match | Your input shopid is not consistent with the shop info in widget. |
| 36004003 | invalid client_key | Appkey whitelist is not configured. You need to provide the domain name and appKey to the open platform and configure the whitelist. |
| I01008 | Traffic is invalid | The shop region is not matched with server room. In most cases, it was caused by unmatched shop_id and region. |

3. The error is reported as follows

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/fcd2300daa394c109f177c97f0d291b2~tplv-10qhjjqwgv-image.image" width="720px" /></div>

Solution: The widget name is wrong, please refer to the integration documentation to check again.