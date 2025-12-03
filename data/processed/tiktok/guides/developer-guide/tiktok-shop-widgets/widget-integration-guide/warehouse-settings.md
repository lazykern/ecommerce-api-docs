Available market:US&UK
## What is the "Warehouse setting" widget?
Before listing products, the seller needs to set up the correct Warehouse/ Pickup addresses. When the seller chooses courier pickup services, TikTok Shop will retrieve this address and schedule courier pickup.
Painpoint:

* Seller may have no chance to know this information or set shipping template without logging into Seller center.
* The high failure rate of API listing products is mainly caused by not setting shipping templates

Warehouse Settings widgets can enable the Seller to enter the delivery warehouse and return warehouse information, including warehouse contact person, address, and sales range.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/8aa31dd80b8e4a95a9a3a38fa4252f64~tplv-10qhjjqwgv-image.image" width="1031px" /></div>

## Showcase
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/4f6766cd54624bb1bfdced1369418c64~tplv-10qhjjqwgv-image.image" width="1982px" /></div>

## Integration demo
## React framework
Configure preload in `WidgetConfigProvider` preloadWidgetNames, you can put `WidgetConfigProvider` to the outermost preload time
```TypeScript
import { WidgetConfigProvider,RemoteWidget } from '@tiktokshop/widget-kit-react';

const getWidgetToken = async () => {
  const res: any = await get('https://xxx/api/v1/widget/access_token', {
    outer_shop_id: 'xxx',
    partner_type: '1',
  });
  if (res?.code === 0) {
    return res?.data;
  }
  return {};
};

const initOptions = {
  config: {
    shopId: 'xxx', //seller id, such as 123456
    oecRegion: 'xxx', //country,such as US
    appKey: 'xxx', //The key corresponding to the merchant's creation service
    isvInfo: {
      name: 'xxx', //ISV name,such as OPEN_PLATFORM
    },
  },
  getToken: getWidgetToken, //get auth token
  remotes: [
    {
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/logistics:warehouse
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/logistics:warehouse']}>
      <RemoteWidget
        name={'@tiktokshop-widget/logistics:warehouse'}
        className={'containerClass'}
        options={{
            onResult: (data: { code: number }) => {
              if (data.code === 0) {
                //Callback function for successful warehouse submission
              }
            },
            type: 'management',
        }} //Pass in the props required by the widget. If there are none, you don't need to pass them in.
      />
    </WidgetConfigProvider>
  );
};
```

## Native js
```JSON
import React, { useEffect } from 'react';
import { get } from './utils/fetch';
import { loadWidget, init, WidgetComponent } from '@tiktokshop/widget-kit';

const name = '@tiktokshop-widget/logistics:warehouse';
let view = null;
export default () => {
  const getWidgetToken = async () => {
    const res: any = await get('https://xxx/api/v1/widget/access_token', {
      outer_shop_id: 'xxx',
      partner_type: '1',
    });
    if (res?.code === 0) {
      return res?.data;
    }
    return {};
  };

  const initWidget = () => {//It is recommended to initialize the widget in the outer layer and execute the preloadWidget([name]) method to preload resources.
    init({
      config: {
        shopId: 'xxx',
        oecRegion: 'US',
        appKey: 'xxx',
        isvInfo: {
          name: 'OPEN_PLATFORM',
        },
      },
      remotes: [
        {
          name,
        },
      ],
      getToken: getWidgetToken,
    });
  };
  useEffect(() => {
    initWidget();
    loadWidget(name).then((component: WidgetComponent) => {
      view = component.create(
        document.getElementById('widget-preview-container')!,
      );
      view?.render({
          onResult: (data: { code: number }) => {
              if (data.code === 0) {
                //Callback function for successful warehouse submission
              }
            },
            type: 'management',
      });
    });
    return () => {
      view?.unmount();
    };
  }, []);
  return (
    <div
      className="widget-preview-container"
      id="widget-preview-container"></div>
  );
};
```

# Change log
| Release date | Update |
| --- | --- |
| 2024/2/22 | The first version is launched, providing basic functions of adding warehouse. |
# Widget SDK User Guide
[Widget SDK User Guide](widget-sdk-user-guide)