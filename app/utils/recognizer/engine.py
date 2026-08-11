class RecognizerEngine:


    def __init__(
        self,
        plugins=None,
        threshold=0.95
    ):

        self.threshold = threshold

        self.plugins = plugins or []



    def register(
        self,
        plugin
    ):

        self.plugins.append(plugin)



    def recognize(
        self,
        column_name,
        values
    ):


        values = [
            str(v).strip()
            for v in values
            if v is not None
        ]


        if not values:
            return None



        results = []


        for plugin in self.plugins:

            result = plugin.recognize(
                column_name,
                values
            )

            results.append(result)



        candidates = [

            r for r in results

            if r["confidence"]
            >= self.threshold

        ]


        if not candidates:

            return {

                "type":"unknown",

                "confidence":0
            }



        return max(
            candidates,
            key=lambda x:x["confidence"]
        )
