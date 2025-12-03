**Available market**
Only US
# Introduction
This widget will help sellers better understand their shop performance, manage operations effectively, and grow their business on TikTok. The data compass widget will enable sellers to access core analytics like GMV, visitors, reviews, and product rankings.
# Showcase
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/0962d033fc814cc4885aec307d1e5598~tplv-10qhjjqwgv-image.image" width="1476px" /></div>

## Core analysis
Sellers can monitor shop sales and traffic performance for a selected time period through six core metrics:
| Metric | Instruction |
| --- | --- |
| Shop GMV | The total amount paid for orders including state sales tax, shipping, and handling fees, but excluding discounts. |
| Shop orders | The total number of orders placed for this product. |
| Buyers | The total number of unique buyers who placed orders. |
| Avg. CTR per day | The daily average percentage of visitors who saw your product link and clicked through to your product. (Click-through rate per day/number of days within the selected period) |
| Shop visitors | The total number of unique visitors who viewed the product detail page. |
| Cancellations and returns | The number of orders that were returned and refunded within 30 days of delivery. |
| Reviews | The total number of buyer reviews during the selected period. |
| Avg. CVR per day | The daily average percentage of times unique visitors also placed an order. (Conversion rates per day/number of days within the selected period) |
## Shop trends
This shows core metric trends. If you click Compare With the Same Period [1], you can view a comparison of trends between the current period and previous periods.
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/e77f95873229473396225c2f2a95d7da~tplv-10qhjjqwgv-image.image)
## Products ranked by GMV
The seller can check the products Top 5 ranking list ordered by GMV, Information and indicators of products and SKUs:

* Product name/ID
* GMV
* Units sold

![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/1ebd3579c9644c0eb8bcedce59903d4d~tplv-10qhjjqwgv-image.image)
For more detailed data on TikTok Shop, you can add an entrance for merchants to click and go to Seller Center> analysis
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/81a57952e4a5470ba47399f73e9ebade~tplv-10qhjjqwgv-image.image)
# Integration demo
## React framework
Configure preload in `WidgetConfigProvider` preloadWidgetNames, you can put `WidgetConfigProvider` to the outermost preload time
1: @tiktokshop-widget/compass:metricGrid
```JSON
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
  getToken: getWidgetToken,  //get auth token
  remotes: [
    {
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/compass:metricGrid
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/compass:metricGrid']}>
      <RemoteWidget
        name={'@tiktokshop-widget/compass:metricGrid'}
        className={'containerClass'}
        options={{
            onClick: onHandleClick,//Control the jump event of clicking the 'More details' button inside the widget
        }} //Pass in the props required by the widget. If there are none, you don't need to pass them in.
      />
    </WidgetConfigProvider>
  );
};
```

2: @tiktokshop-widget/compass:performance
```SQL
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
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/compass:performance
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/compass:performance']}>
      <RemoteWidget
        name={'@tiktokshop-widget/compass:performance'}
        className={'containerClass'}
        options={{}} //Pass in the props required by the widget. If there are none, you don't need to pass them in.
      />
    </WidgetConfigProvider>
  );
};
```

# ShowCase
# Change log
| Release date | Update |
| --- | --- |
|  |  |
# Widget SDK User Guide
[Widget SDK User Guide](widget-sdk-user-guide)