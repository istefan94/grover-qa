get_store_collection = """
    query {
        storeCollection {
            nodes {
                id
                code
                defaultCurrency
            }
        }
    }
    """

get_by_id = """
    query {{
        store (id: {0}) {{
            id
            code
            alternativeLocales
            defaultCurrency
            defaultLocale
        }}
    }}
    """

invalid_query = """
    query {
        store () 
    }
    """

crash_srv = """
    query {
        store {
            alternativeLocales
            defaultCurrency
            defaultLocale
        }
    }
    """
