# Ознайомтеся за допомогою документації з класами OrderedDict, defaultdict та ChainMap модуля collections.



#                   Class collections.OrderedDict([items])
# Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.
# Added in version 3.1.
# popitem(last=True)
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO
# order if last is true or FIFO order if false.
# move_to_end(key, last=True)
# Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true
# (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:
#
# >>>
# d = OrderedDict.fromkeys('abcde')
# d.move_to_end('b')
# ''.join(d)
# 'acdeb'
# d.move_to_end('b', last=False)
# ''.join(d)
# 'bacde'
# Added in version 3.2.
# In addition to the usual mapping methods, ordered dictionaries also support reverse iteration using reversed().
# Equality tests between OrderedDict objects are order-sensitive and are implemented as list(od1.items())==list(od2.items()).
# Equality tests between OrderedDict objects and other Mapping objects are order-insensitive like regular dictionaries.
# This allows OrderedDict objects to be substituted anywhere a regular dictionary is used.
# Changed in version 3.5: The items, keys, and values views of OrderedDict now support reverse iteration using reversed().
# Changed in version 3.6: With the acceptance of PEP 468, order is retained for keyword arguments passed to the OrderedDict
# constructor and its update() method.
# Changed in version 3.9: Added merge (|) and update (|=) operators, specified in PEP 584.
# OrderedDict Examples and Recipes
# It is straightforward to create an ordered dictionary variant that remembers the order the keys were last inserted.
# If a new entry overwrites an existing entry, the original insertion position is changed and moved to the end:
# class LastUpdatedOrderedDict(OrderedDict):
#     'Store items in the order the keys were last added'
#
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value)
#         self.move_to_end(key)

# An OrderedDict would also be useful for implementing variants of functools.lru_cache():
#
# from collections import OrderedDict
# from time import time
#
# class TimeBoundedLRU:
#     "LRU Cache that invalidates and refreshes old entries."
#
#     def __init__(self, func, maxsize=128, maxage=30):
#         self.cache = OrderedDict()      # { args : (timestamp, result)}
#         self.func = func
#         self.maxsize = maxsize
#         self.maxage = maxage
#
#     def __call__(self, *args):
#         if args in self.cache:
#             self.cache.move_to_end(args)
#             timestamp, result = self.cache[args]
#             if time() - timestamp <= self.maxage:
#                 return result
#         result = self.func(*args)
#         self.cache[args] = time(), result
#         if len(self.cache) > self.maxsize:
#             self.cache.popitem(0)
#         return result
# class MultiHitLRUCache:
#     """ LRU cache that defers caching a result until
#         it has been requested multiple times.
#
#         To avoid flushing the LRU cache with one-time requests,
#         we don't cache until a request has been made more than once.
#
#     """
#
#     def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
#         self.requests = OrderedDict()   # { uncached_key : request_count }
#         self.cache = OrderedDict()      # { cached_key : function_result }
#         self.func = func
#         self.maxrequests = maxrequests  # max number of uncached requests
#         self.maxsize = maxsize          # max number of stored return values
#         self.cache_after = cache_after
#
#     def __call__(self, *args):
#         if args in self.cache:
#             self.cache.move_to_end(args)
#             return self.cache[args]
#         result = self.func(*args)
#         self.requests[args] = self.requests.get(args, 0) + 1
#         if self.requests[args] <= self.cache_after:
#             self.requests.move_to_end(args)
#             if len(self.requests) > self.maxrequests:
#                 self.requests.popitem(0)
#         else:
#             self.requests.pop(args, None)
#             self.cache[args] = result
#             if len(self.cache) > self.maxsize:
#                 self.cache.popitem(0)
#         return result


#                       ChainMap Examples and Recipes
# This section shows various approaches to working with chained maps.
# Example of simulating Python’s internal lookup chain:
# import builtins
# pylookup = ChainMap(locals(), globals(), vars(builtins))
# Example of letting user specified command-line arguments take precedence over environment variables which in turn take
# precedence over default values:
# import os, argparse
# defaults = {'color': 'red', 'user': 'guest'}
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}
# combined = ChainMap(command_line_args, os.environ, defaults)
# print(combined['color'])
# print(combined['user'])
# Example patterns for using the ChainMap class to simulate nested contexts:
#
# c = ChainMap()        # Create root context
# d = c.new_child()     # Create nested child context
# e = c.new_child()     # Child of c, independent from d
# e.maps[0]             # Current context dictionary -- like Python's locals()
# e.maps[-1]            # Root context -- like Python's globals()
# e.parents             # Enclosing context chain -- like Python's nonlocals
#
# d['x'] = 1            # Set value in current context
# d['x']                # Get first key in the chain of contexts
# del d['x']            # Delete from current context
# list(d)               # All nested values
# k in d                # Check all nested values
# len(d)                # Number of nested values
# d.items()             # All nested items
# dict(d)               # Flatten into a regular dictionary
# The ChainMap class only makes updates (writes and deletions) to the first mapping in the chain while lookups will search
# the full chain. However, if deep writes and deletions are desired, it is easy to make a subclass that updates keys
# found deeper in the chain:
#
# class DeepChainMap(ChainMap):
#     'Variant of ChainMap that allows direct updates to inner scopes'
#
#     def __setitem__(self, key, value):
#         for mapping in self.maps:
#             if key in mapping:
#                 mapping[key] = value
#                 return
#         self.maps[0][key] = value
#
#     def __delitem__(self, key):
#         for mapping in self.maps:
#             if key in mapping:
#                 del mapping[key]
#                 return
#         raise KeyError(key)
#
# >>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
# >>> d['lion'] = 'orange'         # update an existing key two levels down
# >>> d['snake'] = 'red'           # new keys get added to the topmost dict
# >>> del d['elephant']            # remove an existing key one level down
# >>> d                            # display result
# DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})



#           Defaultdict objects
# class collections.defaultdict(default_factory=None, /[, ...])
# Return a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and
# adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.
# The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining
# arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
# defaultdict objects support the following method in addition to the standard dict operations:
# __missing__(key)
# If the default_factory attribute is None, this raises a KeyError exception with the key as argument.
# If default_factory is not None, it is called without arguments to provide a default value for the given key, this value
# is inserted in the dictionary for the key, and returned.
# If calling default_factory raises an exception this exception is propagated unchanged.
# This method is called by the __getitem__() method of the dict class when the requested key is not found; whatever it
# returns or raises is then returned or raised by __getitem__().
# Note that __missing__() is not called for any operations besides __getitem__(). This means that get() will, like
# normal dictionaries, return None as a default rather than using default_factory.
# defaultdict objects support the following instance variable:
# default_factory
# This attribute is used by the __missing__() method; it is initialized from the first argument to the constructor,
# if present, or to None, if absent.
# Changed in version 3.9: Added merge (|) and update (|=) operators, specified in PEP 584.
# defaultdict Examples
# Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:
# >>>
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created
# using the default_factory function which returns an empty list. The list.append() operation then attaches the value to
# the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the
# list.append() operation adds another value to the list. This technique is simpler and faster than an equivalent
# technique using dict.setdefault():
# >>>
# d = {}
# for k, v in s:
#     d.setdefault(k, []).append(v)
#
# sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):
#
# >>>
# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1
#
# sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
# When a letter is first encountered, it is missing from the mapping, so the default_factory function calls int() to
# supply a default count of zero. The increment operation then builds up the count for each letter.