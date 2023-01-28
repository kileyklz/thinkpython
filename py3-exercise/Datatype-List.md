# List number -- GenericAlias
for Python 3.10.4 , list method include
```py
dir(list)
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
## Start from a define list
help (list.pop)
pop(self, index=-1, /)
    Remove and return item at index (default last).
    
index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.
remove(self, value, /)
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.
```py
NUM= [ 2, 5, 7, 100, 33, 77, 5]
print (NUM)
type (NUM)
```

## Get reverse order

<details><summary>show</summary>
<p>

```py
print (NUM.reverse())
```

</p>
</details>

## List order -- sort

<details><summary>show</summary>
<p>

```py
print (NUM.sort())
```

</p>
</details>

## List Locate element 

Get the first elements

<details><summary>show</summary>
<p>

```py
print (list.fetch(0))
```

</p>
</details>

Get the last elements

<details><summary>show</summary>
<p>

```py
print (list[len(list)-1])
```

</p>
</details>

Get all element

<details><summary>show</summary>
<p>

```py
print (len(list))
```

</p>
</details>

Get the last 3 elements

<details><summary>show</summary>
<p>

```py
print (list.fetch(len(list)-3)
```

</p>
</details>

Get the first 3 elements 

<details><summary>show</summary>
<p>

```py
print (list.fetch(3))
```

</p>
</details>

## Modify List

Append 213 to list

<details><summary>show</summary>
<p>

```py
print (list.append(213))
```

</p>
</details>

Modify the second element to 6

<details><summary>show</summary>
<p>

```py
print (list.append('6'))
```

</p>
</details>
## List in List

## New List

```py
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=fruits
print(newlist)
```

### what's happen ?

```py
print(newlist.clear())
```
<details><summary>show</summary>
<p>
remove all elements from newlist , got "[]"

</p>
</details>

### what's happen ?

```py
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```
<details><summary>show</summary>
<p>

```py
['apple', 'banana', 'mango']
## x get fruits elements one by one 
## if x contain "a" then append to "newlist"
```

</p>
</details>


